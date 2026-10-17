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
from fontTools.pens.recordingPen import RecordingPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
import pathops

FONT_PATH = Path(__file__).parent / "fonts" / "NotoNaskhArabic.ttf"
_cache = {}

def _load(weight):
    if weight not in _cache:
        tt = instancer.instantiateVariableFont(TTFont(FONT_PATH), {"wght": weight})
        face = hb.Face(hb.Blob.from_file_path(str(FONT_PATH)))
        font = hb.Font(face)
        font.set_variations({"wght": weight})
        _cache[weight] = (tt, font)
    return _cache[weight]

def _contours(rec):
    cur = []
    for op, args in rec.value:
        cur.append((op, args))
        if op in ("closePath", "endPath"):
            yield cur
            cur = []
    if cur:
        yield cur

def shape_word(text, size, weight=700, small=0.17):
    """Returns dict(width, ascent, bodies=[d], dots=[d], marks=[d], start=(x, y)).
    Coordinates in px with x from 0 (left edge) and y=0 on the baseline (down is positive)."""
    tt, font = _load(weight)
    upem = tt["head"].unitsPerEm
    s = size / upem
    order = tt.getGlyphOrder()
    gs = tt.getGlyphSet()
    gdef = tt["GDEF"].table.GlyphClassDef.classDefs if "GDEF" in tt else {}
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(font, buf, {})
    pen_x = 0
    out = {"bodies": [], "dots": [], "marks": []}
    body = pathops.Path()   # all letter bodies, merged so joins show no seams
    first = None            # (x position, glyph top point) of the visually rightmost letter
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        name = order[info.codepoint]
        ox, oy = pen_x + pos.x_offset, pos.y_offset
        rec = RecordingPen()
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
            if is_mark:
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
    out["width"] = pen_x * s
    out["start"] = first[1] if first else None
    return out
