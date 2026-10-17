"""Turns a voweled Arabic word into SVG shapes for tracing worksheets.

Shapes the word with HarfBuzz (correct joining and mark placement) using Noto Naskh Arabic
(OFL licence, fonts/), then splits it into:
  - letter bodies   -> drawn as a dotted outline for tracing
  - letter dots and harakat (marks) -> drawn solid, because small shapes in dotted
    outline become squiggles a child cannot trace (design research, tracing-2026-10-17)
Also returns the start point: the rightmost point of the word, where writing begins.
"""
from pathlib import Path
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.recordingPen import DecomposingRecordingPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
import pathops

FONT_PATH = Path(__file__).parent / "fonts" / "NotoNaskhArabic.ttf"
_cache = {}
FONTS = {"naskh": "NotoNaskhArabic.ttf", "baloo": "BalooBhaijaan2.ttf", "sans": "NotoSansArabic.ttf"}

def _load(weight, face_name="naskh"):
    key = (weight, face_name)
    if key not in _cache:
        path = FONT_PATH.parent / FONTS[face_name]
        tt = TTFont(path)
        axes = {a.axisTag: a for a in tt["fvar"].axes} if "fvar" in tt else {}
        loc = {"wght": max(axes["wght"].minValue, min(axes["wght"].maxValue, weight))} if "wght" in axes else {}
        if "wdth" in axes:
            loc["wdth"] = 100
        if loc:
            tt = instancer.instantiateVariableFont(tt, loc)
        font = hb.Font(hb.Face(hb.Blob.from_file_path(str(path))))
        if loc:
            font.set_variations(loc)
        _cache[key] = (tt, font)
    return _cache[key]

def _contours(rec):
    cur = []
    for op, args in rec.value:
        cur.append((op, args))
        if op in ("closePath", "endPath"):
            yield cur
            cur = []
    if cur:
        yield cur

NON_JOINING = set("اأإآدذرزوؤةء")  # letters that never join the letter after them


def stretch(text, n=1):
    """Insert tatweel (U+0640) between joined letters so each tooth stands apart for tracing.
    Only typography: the letters and harakat are unchanged and in the same order."""
    out, chars = [], list(text)
    isletter = lambda c: "\u0621" <= c <= "\u064A"
    for i, ch in enumerate(chars):
        out.append(ch)
        if not isletter(ch) and not ("\u064B" <= ch <= "\u0652"):
            continue
        # end of this letter's cluster (letter + its harakat)?
        nxt = chars[i + 1] if i + 1 < len(chars) else ""
        if "\u064B" <= nxt <= "\u0652":
            continue
        j = i
        while j >= 0 and not isletter(chars[j]):
            j -= 1
        base = chars[j] if j >= 0 else ""
        if base and base not in NON_JOINING and isletter(nxt):
            out.append("\u0640" * n)
    return "".join(out)

def shape_word(text, size, weight=700, small=0.17, gap=0.0, face="naskh"):
    """Returns dict(width, ascent, bodies=[d], dots=[d], marks=[d], start=(x, y)).
    Coordinates in px with x from 0 (left edge) and y=0 on the baseline (down is positive)."""
    tt, font = _load(weight, face)
    upem = tt["head"].unitsPerEm
    s = size / upem
    order = tt.getGlyphOrder()
    gs = tt.getGlyphSet()
    gdef = tt["GDEF"].table.GlyphClassDef.classDefs if "GDEF" in tt else {}
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(font, buf, {})
    # extra space (gap * size px) after each non-joining letter inside the word, so separate
    # letter groups don't touch when drawn as thick bubble outlines
    breaks = [i for i, ch in enumerate(text) if ch in NON_JOINING and
              any("\u0621" <= c <= "\u064A" for c in text[i + 1:])]
    extra_u = gap * size / s
    total = extra_u * len(breaks)
    pen_x = 0
    out = {"bodies": [], "dots": [], "marks": []}
    body = pathops.Path()   # all letter bodies, merged so joins show no seams
    first = None            # (x position, glyph top point) of the visually rightmost letter
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        name = order[info.codepoint]
        before = sum(1 for b in breaks if b < info.cluster)
        ox, oy = pen_x + pos.x_offset + (total - extra_u * before), pos.y_offset
        rec = DecomposingRecordingPen(gs)
        gs[name].draw(rec)
        is_mark = gdef.get(name) == 3
        for c in _contours(rec):
            bp = BoundsPen(gs)
            for op, args in c:
                getattr(bp, op)(*args)
            if not bp.bounds:
                continue
            x0, y0, x1, y1 = bp.bounds
            sp = SVGPathPen(gs)
            tp = TransformPen(sp, (s, 0, 0, -s, ox * s, -oy * s))
            for op, args in c:
                getattr(tp, op)(*args)
            d = sp.getCommands()
            if is_mark and "dot" in name:
                out["dots"].append(d)
            elif is_mark:
                out["marks"].append(d)
            elif max(x1 - x0, y1 - y0) < small * upem:
                out["dots"].append(d)
            else:
                tpo = TransformPen(body.getPen(), (s, 0, 0, -s, ox * s, -oy * s))
                for op, args in c:
                    getattr(tpo, op)(*args)
                # start point: top of the rightmost letter (where a child starts writing)
                pts = [pt for op, args in c for pt in args if pt is not None]
                tx, ty = max(pts, key=lambda q: q[1])
                if first is None or (ox + x1) > first[0]:
                    first = (ox + x1, ((ox + tx) * s, -(oy + ty) * s))
        pen_x += pos.x_advance
    merged = pathops.Path()
    pathops.union([body], merged.getPen())
    sp = SVGPathPen(None)
    merged.draw(sp)
    out["bodies"] = [sp.getCommands()]
    out["width"] = (pen_x + total) * s
    out["start"] = first[1] if first else None
    return out


# ---------------------------------------------------------------------------
# Centre-line tracing ("bubble" letters with a dashed line inside, as in the owner's example):
# the merged letter outline is rasterised, thinned to its centre line (skeleton), cleaned of
# short spurs, and returned as smooth polylines. The page then draws each polyline three times:
# a wide dark stroke (outline), a slightly narrower white stroke (inside), and a dashed line.
import numpy as np
from PIL import Image, ImageDraw, ImageChops
from fontTools.pens.basePen import BasePen
from skimage.morphology import skeletonize

class _Flatten(BasePen):
    def __init__(self, steps=10):
        super().__init__(None)
        self.contours, self.cur, self.steps = [], [], steps
    def _moveTo(self, p):
        self.cur = [p]
    def _lineTo(self, p):
        self.cur.append(p)
    def _curveToOne(self, p1, p2, p3):
        p0 = self.cur[-1]
        for i in range(1, self.steps + 1):
            t = i / self.steps; u = 1 - t
            self.cur.append((u**3*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t**3*p3[0],
                             u**3*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t**3*p3[1]))
    def _qCurveToOne(self, p1, p2):
        p0 = self.cur[-1]
        for i in range(1, self.steps + 1):
            t = i / self.steps; u = 1 - t
            self.cur.append((u*u*p0[0] + 2*u*t*p1[0] + t*t*p2[0], u*u*p0[1] + 2*u*t*p1[1] + t*t*p2[1]))
    def _closePath(self):
        self.contours.append(self.cur); self.cur = []
    _endPath = _closePath

_N8 = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def _edges(sk):
    """Split a skeleton image into pixel chains between endpoints/junctions."""
    pts = set(zip(*np.nonzero(sk)))
    nb = {p: [(p[0]+a, p[1]+b) for a, b in _N8 if (p[0]+a, p[1]+b) in pts] for p in pts}
    nodes = {p for p in pts if len(nb[p]) != 2}
    seen, edges = set(), []
    for n in nodes:
        for q in nb[n]:
            if (n, q) in seen:
                continue
            chain, prev, cur = [n], n, q
            while True:
                chain.append(cur)
                seen.add((prev, cur)); seen.add((cur, prev))
                if cur in nodes:
                    break
                nxt = [r for r in nb[cur] if r != prev and (cur, r) not in seen]
                if not nxt:
                    break
                prev, cur = cur, nxt[0]
            edges.append(chain)
    # closed loops with no nodes
    done = {p for e in edges for p in e}
    for p in pts - done:
        if p in done:
            continue
        chain, prev, cur = [p], None, p
        while True:
            nxt = [r for r in nb[cur] if r != prev and r not in chain]
            if not nxt:
                break
            prev, cur = cur, nxt[0]
            chain.append(cur)
        done.update(chain)
        edges.append(chain + [p])
    return edges, nb

def _smooth(poly, k=3):
    if len(poly) < 2 * k + 1:
        return poly
    a = np.array(poly, float)
    out = a.copy()
    for i in range(k, len(a) - k):
        out[i] = a[i - k:i + k + 1].mean(axis=0)
    return out.tolist()

def centerlines(text, size, weight=700, scale=8, spur=0.06, gap=0.12, kashida=1, face="naskh", hole=0.05, close=None):
    if kashida:
        text = stretch(text, kashida)
    """Returns dict(width, lines=[[(x,y),...]], starts=[(x,y)], dots=[(cx,cy,r)], marks=[d])."""
    r = shape_word(text, size, weight, gap=gap, face=face)
    from fontTools.svgLib.path import parse_path
    fl = _Flatten()
    parse_path(r["bodies"][0], fl)
    allp = [p for c in fl.contours for p in c]
    minx, miny = min(p[0] for p in allp) - 4, min(p[1] for p in allp) - 4
    W = int((max(p[0] for p in allp) - minx + 8) * scale)
    H = int((max(p[1] for p in allp) - miny + 8) * scale)
    img = Image.new("1", (W, H), 0)
    for c in fl.contours:
        layer = Image.new("1", (W, H), 0)
        ImageDraw.Draw(layer).polygon([((x - minx) * scale, (y - miny) * scale) for x, y in c], fill=1)
        img = ImageChops.logical_xor(img, layer)
    from skimage.morphology import remove_small_holes, binary_closing, disk
    mask = np.array(img.convert("L")) > 0
    # fill tiny counters (e.g. where a tooth meets the baseline), which
    # would otherwise become small loops in the centre line and make a tooth look like ف
    # close hairline gaps (keeps short teeth like ن clean), except in words with ح/خ/ج, where it
    # would seal the real narrow gap under the letter's top stroke
    if close is None:
        close = not any(ch in text for ch in "حخج")
    if close:
        mask = binary_closing(mask, disk(max(1, int(0.02 * size * scale))))
    # only hairline gaps: real letter loops (و م ة ع ف ق) must stay open
    mask = remove_small_holes(mask, max_size=int((hole * size * scale) ** 2))
    sk = skeletonize(np.ascontiguousarray(mask))
    # prune short spurs (end -> junction) a few times
    for _ in range(3):
        edges, nb = _edges(sk)
        changed = False
        for e in edges:
            ends = [p for p in (e[0], e[-1]) if len(nb[p]) == 1]
            juncs = [p for p in (e[0], e[-1]) if len(nb[p]) >= 3]
            if ends and juncs and len(e) < spur * size * scale:
                for p in e:
                    if len(nb[p]) < 3:
                        sk[p] = False
                changed = True
        if not changed:
            break
        sk = skeletonize(np.ascontiguousarray(sk, dtype=bool))
    edges, nb = _edges(sk)
    lines = []
    for e in edges:
        if len(e) < 3:
            continue
        poly = [((c / scale) + minx, (rr / scale) + miny) for rr, c in e[::2]] + [((e[-1][1] / scale) + minx, (e[-1][0] / scale) + miny)]
        lines.append(_smooth(poly))
    # start points: per connected piece, the endpoint furthest right (ties: highest)
    from skimage.measure import label
    lab = label(sk, connectivity=2)
    starts = []
    for k in range(1, lab.max() + 1):
        ends = [p for p in nb if lab[p] == k and len(nb[p]) == 1] or [p for p in nb if lab[p] == k]
        rr, c = max(ends, key=lambda p: (p[1] - 0.5 * p[0]))
        starts.append((c / scale + minx, rr / scale + miny))
    # dots: one circle per dot contour (dot glyph names contain "dot")
    dots = []
    for d in r["dots"]:
        f2 = _Flatten(); parse_path(d, f2)
        for c in f2.contours:
            xs, ys = [p[0] for p in c], [p[1] for p in c]
            dots.append(((min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2, max(max(xs) - min(xs), max(ys) - min(ys)) / 2))
    return {"width": r["width"], "lines": lines, "starts": starts, "dots": dots, "marks": r["marks"],
            "bodies": r["bodies"], "solid_dots": r["dots"]}
