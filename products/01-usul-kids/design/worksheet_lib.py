"""Shared worksheet template for The Three Fundamental Principles (cover v4 style).

Built from the owner's Lesson 3 feedback (2026-10-17), so every lesson follows it:
- bubble tracing with a dashed centre line, hollow letter dots, grey harakat, green start dots;
  model word on the RIGHT, two tracing copies, a blank box to write alone (design research + owner example)
- Noto Sans Arabic for worksheet Arabic; Amiri only for the product name in the header
- Match: only the real pairs, no extra left-over option (owner: it looked like an error)
- Fill-in: one step pair only, "circle the right word, then write it on the line" (no separate write line)
- Footer: "Meaning of Shaykh X's words: ..." (no bracketed "(meaning)"); real book, publisher,
  edition and printed page, NO publication year
- colour kept 0.3in inside the paper edge; white page for cheap home printing; US Letter and A4
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent / "tools"))
from arabic_trace import shape_word, centerlines, stretch

HERE = Path(__file__).parent
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Amiri:wght@700'
         '&family=Noto+Sans+Arabic:wght@500;600&family=Baloo+2:wght@700;800&family=Nunito:wght@600;700;800&display=swap">')

INK, MUTED, GREEN, LINE, LINE2 = "#2a1d17", "#6b5b51", "#456f3a", "#c9bea6", "#e2dccf"
SIZE, ROW_H, BASE = 72, 112, 76          # defaults: word size, row height, baseline y in the row
FACE, WT = "sans", 500                    # Noto Sans Arabic: even strokes, clear teeth for tracing
BUB, BUB_IN = 13.5, 10                    # bubble outline width, inner (white) width

def _poly(l):
    return "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in l)

def word(r, x, kind, BASE=BASE, ink=INK, cls=""):
    """Place a word with its right edge at x (Arabic starts on the right).
    model: solid letters. trace: bubble outline with a dashed centre line (owner's example),
    hollow dots, light grey harakat, green start dot at each letter group."""
    left = x - r["width"]
    c = f' class="{cls}"' if cls else ""
    g = f'<g{c} transform="translate({left:.1f} {BASE})">'
    if kind == "model":
        g += "".join(f'<path d="{d}" fill="{ink}"/>' for d in r["bodies"] + r["dots"] + r["marks"])
        return g + "</g>"
    ds = [_poly(l) for l in r["lines"]]
    cap = 'fill="none" stroke-linecap="round" stroke-linejoin="round"'
    g += "".join(f'<path d="{d}" {cap} stroke="{INK}" stroke-width="{BUB}"/>' for d in ds)
    g += "".join(f'<path d="{d}" {cap} stroke="#fff" stroke-width="{BUB_IN}"/>' for d in ds)
    g += "".join(f'<path d="{d}" {cap} stroke="#7d7260" stroke-width="1.4" stroke-dasharray="3.6 2.8"/>' for d in ds)
    g += "".join(f'<circle cx="{a:.1f}" cy="{b:.1f}" r="{max(rr, 4.2):.1f}" fill="#fff" stroke="{INK}" stroke-width="1.6"/>' for a, b, rr in r["dots"])
    g += "".join(f'<path d="{d}" fill="#b3a892"/>' for d in r["marks"])
    g += "".join(f'<circle cx="{a:.1f}" cy="{b:.1f}" r="3.4" fill="{GREEN}"/>' for a, b in r["starts"])
    return g + "</g>"

def trace_row(ar, en, width, SIZE=SIZE, ROW_H=ROW_H, BASE=BASE, label_w=92, key=False):
    cells = 4
    cw = (width - label_w) / cells
    # shrink a long word just enough to leave clear space between copies
    size = SIZE
    probe = shape_word(ar, size, weight=WT, gap=0.12, face=FACE)["width"] + BUB
    if probe > cw - 26:
        size = SIZE * (cw - 26) / probe
    r = shape_word(ar, size, weight=WT, gap=0.12, face=FACE)
    t = centerlines(ar, size, weight=WT, face=FACE, spur=0.1, kashida=0)
    # cells left to right: blank, trace, trace, model (model on the right)
    svg = [f'<svg class="trow" viewBox="0 0 {width} {ROW_H}" width="{width}" height="{ROW_H}">']
    svg.append(f'<line x1="0" x2="{width - label_w - 8}" y1="{BASE}" y2="{BASE}" stroke="{LINE}" stroke-width="2"/>')
    svg.append(f'<line x1="0" x2="{width - label_w - 8}" y1="{BASE + 28}" y2="{BASE + 28}" stroke="{LINE2}" stroke-width="1.5"/>')
    svg.append(f'<rect x="6" y="6" width="{cw - 18:.1f}" height="{ROW_H - 10}" rx="12" fill="none" stroke="#d6cdbb" stroke-width="1.5"/>')
    for i, kind in [(1, "trace"), (2, "trace"), (3, "model")]:
        w_ = t if kind == "trace" else r
        right = cw * i + (cw + w_["width"]) / 2
        svg.append(word(w_, right, kind, BASE, cls="stu" if key else ""))
    if key:  # answer key: the word the child writes alone, in green, inside the blank box
        svg.append(word(r, (cw - 12 + r["width"]) / 2, "model", BASE, ink=GREEN, cls="ans"))
    svg.append(f'<text x="{width}" y="{BASE - 2}" text-anchor="end" class="en">{en}</text>')
    svg.append("</svg>")
    return "".join(svg)

def build(size, spec, key=False):
    """key=True: the filled-in answer-key copy of the same page (answer-key research 2026-10-17):
    same generator and data, student content faded, panels as outlines, answers in bold green."""
    w, h, page = (816, 1056, "8.5in 11in") if size == "letter" else (794, 1123, "210mm 297mm")
    inner = w - 96
    tsize, trow, tbase = spec.get("trace_size", SIZE), spec.get("row_h", ROW_H), spec.get("base", BASE)
    trace_rows = "".join(trace_row(ar, en, inner, tsize, trow, tbase, spec.get('label_w', 92), key) for ar, en in spec["trace"])
    def h2(n, title, small=""):
        return f'<h2><b>{n}</b>{title}' + (f' <small>{small}</small>' if small else "") + '</h2>'
    def trace_sec(n):
        return f'<section>{h2(n, "Trace the words", "Start at the <i></i> and go right to left. Then write it alone in the box.")}{trace_rows}</section>'
    def match_sec(n):
        left = "".join(f'<div class="mi"><div class="mw">{ar}</div><span class="dot"></span></div>' for ar in spec["match_left"])
        right = "".join(f'<div class="mi"><span class="dot"></span><div class="me">{en}</div></div>' for en in spec["match_right"])
        lines = ""
        if key:  # columns use space-around, so item i is centred at H*(2i+1)/(2n)
            H, cnt, lw, rw = spec.get('match_h', 176), len(spec["match_left"]), spec.get('match_lw', 190), spec.get('match_rw', 200)
            pairs = dict(spec["trace"])
            for i, ar in enumerate(spec["match_left"]):
                j = spec["match_right"].index(pairs[ar])
                y1, y2 = H * (2 * i + 1) / (2 * cnt), H * (2 * j + 1) / (2 * cnt)
                lines += (f'<line x1="{lw - 7}" y1="{y1:.1f}" x2="{inner - rw + 7}" y2="{y2:.1f}" stroke="{GREEN}" stroke-width="5" stroke-linecap="round"/>'
                          f'<circle cx="{lw - 7}" cy="{y1:.1f}" r="11" fill="{GREEN}"/><circle cx="{inner - rw + 7}" cy="{y2:.1f}" r="11" fill="{GREEN}"/>')
            lines = f'<svg class="mlines" width="{inner}" height="{H}">{lines}</svg>'
        return (f'<section>{h2(n, "Match", "Draw a line from each word to its meaning.")}'
                f'<div class="match"><div class="mcol">{left}</div><div class="mcol r">{right}</div>{lines}</div></section>')
    def bank_sec(n):
        b = spec["bank"]
        words = "".join(f'<span>{ar}</span>' for ar in b["words"])
        cards = "".join(f'<div class="bcard"><div class="bq">{en}</div><div class="bbox"></div></div>' for en in b["meanings"])
        return (f'<section>{h2(n, "Write the word", "Find the Arabic word for each meaning in the box. Copy it on the line.")}'
                f'<div class="bank">{words}</div><div class="bcards">{cards}</div></section>')
    def act3_sec(n):
        a3 = spec["act3"]
        if a3["kind"] == "fill":
            return (f'<section>{h2(n, "Fill in the missing word", "Circle the right word, then write it on the line.")}'
                    f'<div class="said">{a3["said"]}</div>'
                    f'<div class="fill">{a3["before"]} <span class="blank">{a3["answer"] if key else ""}</span>{a3.get("after", ".")}</div>'
                    f'<div class="choices">' + "".join(f'<span{chk(c)}>{c}</span>' for c in a3["choices"]) + '</div></section>')
        return (f'<section>{h2(n, "Circle the right answer")}'  # circle only, no writing
                f'<div class="said">{a3["said"]}</div>'
                f'<div class="fill">{a3["question"]}</div>'
                f'<div class="choices">' + "".join(f'<span{chk(c)}>{c}</span>' for c in a3["choices"]) + '</div></section>')
    def chk(c):
        return ' class="ok"' if key and c == spec["act3"].get("answer") else ""
    makers = {"trace": trace_sec, "match": match_sec, "bank": bank_sec, "act3": act3_sec}
    sections = "\n    ".join(makers[a](k + 1) for k, a in enumerate(spec.get("acts", ["trace", "match", "act3"])))
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8">{FONTS}<style>
  @page {{ size: {page}; margin: 0; }}
  html, body {{ margin: 0; background: #fff; }}
  .page {{ width: {w}px; height: {h}px; box-sizing: border-box; padding: 29px 0; display: flex; flex-direction: column;
          font-family: "Nunito", sans-serif; color: {INK}; overflow: hidden; }}
  .band {{ margin: 0 29px; background: #e5e1d8; border-radius: 14px; }}
  header {{ padding: 14px 19px 12px; display: flex; align-items: center; justify-content: space-between; }}
  header .k {{ font-weight: 700; font-size: 14px; color: {MUTED}; }}
  header h1 {{ font-family: "Baloo 2", sans-serif; font-weight: 800; font-size: 34px; line-height: 1; margin: 3px 0 0; }}
  header .ar {{ font-family: "Amiri", serif; font-weight: 700; direction: rtl; font-size: 34px; color: {GREEN}; line-height: 1.3; }}
  .name {{ padding: 16px 48px 0; font-weight: 700; font-size: 16px; display: flex; gap: 40px; }}
  .name span {{ display: inline-block; width: 210px; border-bottom: 2px solid {INK}; margin-left: 8px; }}
  main {{ flex: 1; padding: 0 48px; display: flex; flex-direction: column; justify-content: space-evenly; }}
  h2 {{ font-family: "Baloo 2", sans-serif; font-weight: 800; font-size: 23px; margin: 0 0 6px; display: flex; align-items: center; gap: 12px; white-space: nowrap; }}
  h2 b {{ width: 34px; height: 34px; border-radius: 50%; background: {GREEN}; color: #fff; display: grid; place-items: center; font-size: 19px; flex: none; }}
  h2 small {{ font-family: "Nunito", sans-serif; font-weight: 700; font-size: 15px; color: {MUTED}; }}
  h2 small i {{ font-style: normal; display: inline-block; width: 10px; height: 10px; border-radius: 50%; background: {GREEN}; margin: 0 2px; }}
  .trow {{ display: block; }}
  .trow .en {{ font-family: "Nunito", sans-serif; font-weight: 800; font-size: 15px; fill: {MUTED}; }}
  .match {{ display: flex; justify-content: space-between; height: {spec.get('match_h', 176)}px; }}
  .mcol {{ width: {spec.get('match_lw', 190)}px; display: flex; flex-direction: column; justify-content: space-around; }}
  .mcol.r {{ width: {spec.get('match_rw', 200)}px; }}
  .mi {{ display: flex; align-items: center; }}
  .mcol:not(.r) .mi {{ justify-content: flex-end; }}
  .mw {{ font-family: "Noto Sans Arabic", sans-serif; font-weight: 600; font-size: {spec.get('match_ar_size', 46)}px; line-height: {spec.get('match_lh', 1)}; direction: rtl; text-align: right; padding-right: 18px; }}
  .me {{ font-weight: 800; font-size: 20px; padding-left: 16px; }}
  .dot {{ width: 14px; height: 14px; border-radius: 50%; background: {GREEN}; flex: none; }}
  .said {{ font-size: 16px; font-weight: 700; color: {MUTED}; margin-bottom: 4px; }}
  .fill {{ font-size: 22px; font-weight: 700; line-height: 1.2; white-space: nowrap; }}
  .fill .blank {{ display: inline-block; width: 230px; height: 28px; border-bottom: 2px solid {INK}; vertical-align: baseline; margin-left: 4px; }}
  .choices {{ white-space: nowrap; display: flex; align-items: center; gap: 14px; margin-top: 14px; }}
  .choices span {{ font-family: "Baloo 2", sans-serif; font-weight: 700; font-size: 22px; color: {INK}; border: 1.5px solid #c9bea6; border-radius: 10px; padding: 3px 12px 1px; }}
  .bank {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 10px 22px; padding: 8px 14px; border: 1.5px solid #c9bea6; border-radius: 12px; }}
  .bank span {{ font-family: "Noto Sans Arabic", sans-serif; font-weight: 600; font-size: {spec.get('bank_ar_size', 32)}px; line-height: 1.5; direction: rtl; }}
  .bcards {{ display: grid; align-items: end; grid-template-columns: repeat({len(spec.get('bank', {}).get('meanings', [1]))}, 1fr); gap: 14px; margin-top: 12px; }}
  .bq {{ font-weight: 800; font-size: 17px; text-align: center; }}
  .bbox {{ height: {spec.get('bank_box_h', 64)}px; border-bottom: 2px solid {INK}; background: linear-gradient(transparent 60%, {LINE2} 60%, {LINE2} calc(60% + 1.5px), transparent calc(60% + 1.5px)); }}
  footer {{ padding: 11px 19px 12px; font-size: 12.5px; line-height: 1.45; color: #4a3a30;
           display: flex; justify-content: space-between; align-items: flex-end; gap: 24px; }}
  footer b {{ color: {INK}; }}
  .brand {{ text-align: right; white-space: nowrap; font-size: 12.5px; }}
  .brand div {{ font-family: "Baloo 2", sans-serif; font-weight: 800; font-size: 19px; color: {INK}; }}
  .brand i {{ font-style: normal; color: {GREEN}; }}
{KEY_CSS if key else ""}</style></head><body><div class="page{' key' if key else ''}">
  <header class="band">
    <div><div class="k">The Three Fundamental Principles, Lesson {spec["lesson"]}</div><h1>{spec["title"]}</h1></div>
    <div class="ar">الأُصُولُ الثَّلَاثَةُ</div>
  </header>
  <div class="name"><div>Name:<span></span></div><div>Date:<span style="width:130px"></span></div></div>
  <main>
    {sections}
  </main>
  <footer class="band">
    <div><b>Source for parents:</b> {spec["source"]}</div>
    <div class="brand"><div>Sunnah<i>Saplings</i></div>Answers: Answer Key, Lesson {spec["lesson"]}</div>
  </footer>
</div></body></html>'''


KEY_CSS = f"""
  .key {{ color: #a39a92; }}
  .key .band {{ background: none; box-shadow: inset 0 0 0 2px #d6cdbb; }}
  .key header .ar, .key .brand i {{ color: #a39a92; }}
  .key header h1, .key .brand div, .key footer b, .key footer, .key header .k, .key h2 small {{ color: #a39a92; }}
  .key h2 b {{ background: #c4bbb1; }}
  .key .name span, .key .fill .blank {{ border-color: #c4bbb1; }}
  .key .stu {{ opacity: .38; }}
  .key .mw, .key .me {{ color: #a39a92; }}
  .key .dot {{ background: #c4bbb1; }}
  .key .match {{ position: relative; }}
  .key .mlines {{ position: absolute; left: 0; top: 0; }}
  .key .choices span {{ color: #a39a92; }}
  .key .fill .blank {{ color: {GREEN}; font-family: "Baloo 2", sans-serif; font-weight: 800; font-size: 30px; text-align: center; line-height: 28px; }}
  .key .choices span.ok {{ color: {GREEN}; border: 5px solid {GREEN}; border-radius: 999px; padding: 0 14px; margin: -4px -4px; }}
"""


def write(spec, stem):
    for size, suffix in [("letter", ""), ("a4", "-a4")]:
        (HERE / f"{stem}{suffix}.html").write_text(build(size, spec), encoding="utf-8")
