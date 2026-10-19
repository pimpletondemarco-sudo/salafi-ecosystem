"""Lesson 1 "The Four Matters We Must Learn", redesign 2026-10-18 (replaces l1wsA/B/C, which are on hold).

Two pages (owner-approved): page 1 "Learn" = tracing strip + MATCH check; page 2 "Do" = cut and glue the four
matters into four numbered boxes ("box", never "stone", owner 2026-10-18) in the book's order (research/design/sequence-cut-and-glue-2026-10-18.md).
3 versions of each page (A/B/C), US Letter + A4.

Content ONLY from sources/lesson-01-four-matters.md (VERIFIED in VERIFICATION.md):
- the four matters, in order, as headed in al-Uthaymeen's Sharh Thalathat al-Usul (Dar al-Thurayya, 4th ed.):
  العلم p.19, العمل به p.22, الدعوة إليه p.22, الصبر على الأذى فيه p.24. Pages use the head nouns with vowel marks
  added for children (owner OK still pending, as for the earlier worksheets).
- English labels: the agreed terms in TRANSLATION-REVIEW-2 (Knowledge, Acting upon it, Calling others to it, Patience).
- Footer meaning of matter 4: "being patient when we are hurt or troubled because of it" (VERIFICATION Fix 2).
"""
from pages_lib import page, dims, trace_section, match_section, steps_line, h2, scissors, palm_svg, CUT, CUT_W, BONE, IN

AR = ["الْعِلْمُ", "الْعَمَلُ", "الدَّعْوَةُ", "الصَّبْرُ"]
EN_TRACE = ["Knowledge", "Action", "Calling", "Patience"]
EN = ["Knowledge", "Acting upon it", "Calling others to it", "Patience"]
MATCH_RIGHT = ["Patience", "Knowledge", "Calling others to it", "Acting upon it"]   # shuffled, no straight-across pair
SHUFFLE = [2, 0, 3, 1]       # pieces on the strip: 3, 1, 4, 2 (never 1-2-3-4; no piece under its own stone)

SOURCE = ("The four matters in the order of Thalathat al-Usul, as headed in Shaykh al-Uthaymeen's explanation: knowledge, acting upon it,\n"
          "      calling others to it, and patience (being patient when we are hurt or troubled because of it).\n"
          "      <i>Sharh Thalathat al-Usul</i>, Shaykh Muhammad ibn Salih al-Uthaymeen, Dar al-Thurayya, 4th ed., pp. 19&ndash;24.")
STEPS = ["Cut out the 4 pieces.", "Put them in order.", "Glue each piece in its numbered box."]


# ---------------------------------------------------------------- Learn page
def learn(size, v):
    w, h, _ = dims(size)
    inner = w - 96
    palm = {"A": "header", "B": "name", "C": "bottom"}[v]
    body = (trace_section(1, list(zip(AR, EN_TRACE)), inner, size=60, row_h=84 if v == "C" else 88, base=62, label_w=110)
            + match_section(2, AR, MATCH_RIGHT, h={"A": 236, "B": 214, "C": 190}[v], lw=200, rw=250, ar_size=34, panel=(v == "B")))
    return page(size, lesson=1, pno=1, kind="Learn", title="The Four Matters We Must Learn", body=body,
                source=SOURCE, palm=palm, cls="faint" if v == "B" else "")


# ---------------------------------------------------------------- Do page: stepping stones
PW, PH = int(1.75 * IN), int(1.25 * IN)       # piece 1.75 x 1.25 in (R4)
SAFE = 0.15 * IN                                # glue zone 0.15 in larger than the piece on every side (R1)


def glue_zone(x, y, gw, gh):
    return (f'<div class="gz" style="left:{x:.1f}px;top:{y:.1f}px;width:{gw:.1f}px;height:{gh:.1f}px"><span>Glue piece here</span></div>')


def num(n, cx, cy):
    return f'<div class="num" style="left:{cx - 21.5:.1f}px;top:{cy - 21.5:.1f}px">{n}</div>'


def strip(cx, top, pw, ph):
    """Four pieces side by side sharing edges: one long cut, then three short cuts (R4)."""
    total = 4 * pw
    x0 = cx - total / 2
    cells = "".join(f'<div class="pc" style="width:{pw}px;height:{ph}px"><div class="ar pa">{AR[k]}</div><div class="pe">{EN[k]}</div></div>'
                    for k in SHUFFLE)
    return (f'<div class="strip" style="left:{x0:.1f}px;top:{top:.1f}px;width:{total + CUT_W:.1f}px">{cells}</div>'
            + scissors(x0 - 18, top + CUT_W / 2, 24, 0))


def road(points, width=34):
    d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in points)
    return d


def do_page(size, v):
    w, h, _ = dims(size)
    inner = w - 96
    gw, gh = PW + 2 * SAFE, PH + 2 * SAFE
    parts, svg = [], []
    stage_w, stage_left = inner, 0
    if v == "A":   # gentle zigzag path, top-left to bottom-right, ending at the palm
        pad = 10
        sw, sh = gw + 2 * pad, gh + 2 * pad
        L0, ph_ = 30, 92
        pw_ = ph_ * 140 / 132
        step = (inner - L0 - sw - pw_ - 8) / 3
        tops = [34, 34 + sh + 44, 34, 34 + sh + 44]
        xs = [L0 + i * step for i in range(4)]
        floor = tops[1] + sh
        palm_x = xs[3] + sw + 8
        centers = [(x + sw / 2, t + sh / 2) for x, t in zip(xs, tops)]
        pts = centers + [(palm_x + pw_ / 2, floor - 12)]
        svg.append(f'<path d="{road(pts)}" fill="none" stroke="#efeae0" stroke-width="40" stroke-linejoin="round" stroke-linecap="round"/>')
        for i, (x, t) in enumerate(zip(xs, tops)):
            parts.append(f'<div class="stone" style="left:{x:.1f}px;top:{t:.1f}px;width:{sw:.1f}px;height:{sh:.1f}px"></div>')
            parts.append(glue_zone(x + pad, t + pad, gw, gh))
            parts.append(num(i + 1, x - 8, t - 8))
        parts.append(f'<div style="left:{palm_x:.1f}px;top:{floor - ph_:.1f}px">{palm_svg(ph_)}</div>')
        strip_top = floor + 66
    elif v == "B":  # a straight row of 4 stones climbing like steps toward the palm
        pw_piece = int(1.5 * IN)              # 1.5 x 1.25 in pieces so four steps fit A4 (never below 1.5 x 1.0 in, R4)
        gw = pw_piece + 2 * SAFE
        stage_w = w - 2 * 34                  # steps use the page width inside a 0.35 in margin (ink >= 0.3 in from edge)
        stage_left = (inner - stage_w) / 2
        pitch = stage_w / 4
        rise, ph_ = 46, 92
        y4 = ph_ + 10
        tops = [y4 + (3 - i) * rise for i in range(4)]
        floor = tops[0] + gh + 18
        for i in range(4):
            x = i * pitch
            parts.append(f'<div class="stone step" style="left:{x + 1:.1f}px;top:{tops[i]:.1f}px;width:{pitch - 2:.1f}px;height:{floor - tops[i]:.1f}px"></div>')
            parts.append(glue_zone(x + (pitch - gw) / 2, tops[i] + 8, gw, gh))
            parts.append(num(i + 1, x + (pitch - gw) / 2 + 22, tops[i] - 26))
        pw_ = ph_ * 140 / 132
        parts.append(f'<div style="left:{3 * pitch + pitch - pw_ - 8:.1f}px;top:{y4 - ph_ - 4:.1f}px">{palm_svg(ph_)}</div>')
        strip_top = floor + 66
        global_pw = pw_piece
    else:          # C: 2 x 2 grid with arrows 1 -> 2 -> 3 -> 4 -> palm
        pad = 10
        sw, sh = gw + 2 * pad, gh + 2 * pad
        x0, gap = 30, 70
        x1 = x0 + sw + gap
        y0, y1 = 34, 34 + sh + 60
        ph_ = 92
        pw_ = ph_ * 140 / 132
        cells = [(x0, y0), (x1, y0), (x0, y1), (x1, y1)]
        for i, (x, y) in enumerate(cells):
            parts.append(f'<div class="stone" style="left:{x:.1f}px;top:{y:.1f}px;width:{sw:.1f}px;height:{sh:.1f}px"></div>')
            parts.append(glue_zone(x + pad, y + pad, gw, gh))
            parts.append(num(i + 1, x - 8, y - 8))
        palm_x = x1 + sw + 34
        def arrow(d):
            return f'<path d="{d}" fill="none" stroke="#8a7d6e" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#ah)"/>'
        svg.append('<defs><marker id="ah" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="4" markerHeight="4" orient="auto">'
                   '<path d="M0 0 L10 5 L0 10 Z" fill="#8a7d6e"/></marker></defs>')
        svg.append(arrow(f"M{x0 + sw + 10} {y0 + sh / 2} L{x1 - 14} {y0 + sh / 2}"))
        svg.append(arrow(f"M{x1 + sw * 0.35} {y0 + sh + 8} C{x1 + sw * 0.2} {y1 - 18} {x0 + sw * 0.9} {y0 + sh + 18} {x0 + sw * 0.62} {y1 - 14}"))
        svg.append(arrow(f"M{x0 + sw + 10} {y1 + sh / 2} L{x1 - 14} {y1 + sh / 2}"))
        svg.append(arrow(f"M{x1 + sw + 6} {y1 + sh - 30} L{palm_x - 6} {y1 + sh - 30}"))
        parts.append(f'<div style="left:{palm_x:.1f}px;top:{y1 + sh - ph_:.1f}px">{palm_svg(ph_)}</div>')
        strip_top = y1 + sh + 66
    piece_w = global_pw if v == "B" else PW
    stage_h = strip_top + PH + CUT_W + 4
    strip_cx = (stage_w if v == "B" else inner) / 2
    svg_html = f'<svg style="left:0;top:0" width="{stage_w}" height="{stage_h}">{"".join(svg)}</svg>' if svg else ""
    stage = (f'<div class="stage" style="width:{stage_w:.1f}px;height:{stage_h:.1f}px;margin-left:{stage_left:.1f}px">'
             f'{svg_html}{"".join(parts)}{strip(strip_cx, strip_top, piece_w, PH)}</div>')
    body = (f'<section>{h2(1, "Put the four matters in order")}{steps_line(STEPS)}</section>{stage}')
    css = f'''
  .stone {{ background: {BONE}; border-radius: 20px; }}
  .stone.step {{ border-radius: 14px 14px 4px 4px; background: #ebe7de; }}
  .gz {{ background: #fbfaf6; border-radius: 12px; display: grid; place-items: center; }}
  .gz span {{ font-size: 15px; font-weight: 700; color: #b3a99b; }}
  .strip {{ display: flex; border: {CUT_W}px solid {CUT}; background: #fff; }}
  .pc {{ box-sizing: border-box; flex: none; display: flex; flex-direction: column; align-items: center; justify-content: center;
         padding: 15px; text-align: center; }}
  .pc + .pc {{ border-left: {CUT_W}px solid {CUT}; }}
  .pa {{ font-size: 32px; line-height: 1.55; }}
  .pe {{ font-size: 15px; font-weight: 800; line-height: 1.25; color: #2a1d17; }}
  .sc {{ z-index: 2; }}'''
    return page(size, lesson=1, pno=2, kind="Do", title="The Four Matters in Order", body=body, source=SOURCE, css=css)


if __name__ == "__main__":
    from pathlib import Path
    here = Path(__file__).parent
    for v in "ABC":
        for size, suf in [("letter", ""), ("a4", "-a4")]:
            (here / f"lesson-01-learn-v{v}{suf}.html").write_text(learn(size, v), encoding="utf-8")
            (here / f"lesson-01-do-v{v}{suf}.html").write_text(do_page(size, v), encoding="utf-8")
    print("lesson 1 pages written")
