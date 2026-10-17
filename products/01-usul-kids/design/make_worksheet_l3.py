"""Lesson 3 worksheet "My Three Roots" (v3), in the chosen cover style (v4, bone and green).

Writes US Letter and A4 HTML files. Religious content comes only from
sources/lesson-03-three-questions.md (verified): the three words and Ibn Baz's line
"These three principles gather the whole religion" (Dar al-Masir, printed p. 38).

Design research followed (research/design/):
- tracing-2026-10-17: model word on the RIGHT (Arabic is written right to left), two tracing copies,
  then a blank box to write alone; harakat solid grey; green start dot; writing line where
  letters sit plus a lighter line for tails.
- Owner's example (2026-10-17): bubble letters with a dashed centre line inside, hollow dots.
  Noto Sans Arabic (OFL): even strokes and clear teeth; a little extra space after letters
  that don't join, so separate letter groups never touch.
- worksheet-layout-2026-10-17: colour kept 0.3in inside the paper edge (home printers can't print
  to the edge); shorter header; footer says where the answers are.
- matching-2026-10-17: Arabic enlarged to 48px, rows spaced further apart.
- fill-in-2026-10-17: answer gets its own writing line (3in x 0.7in); choices in outlined boxes
  after "Circle one:".
Pending owner choices: a 4th matching option, and hiding the tracing meanings (answers to the match).
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent / "tools"))
from arabic_trace import shape_word, centerlines, stretch

HERE = Path(__file__).parent
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Amiri:wght@700'
         '&family=Noto+Sans+Arabic:wght@500;600&family=Baloo+2:wght@700;800&family=Nunito:wght@600;700;800&display=swap">')

WORDS = [("رَبِّي", "My Lord"), ("دِينِي", "My Religion"), ("نَبِيِّي", "My Prophet")]
# shuffled; answers in the answer key. A 4th left-over option was tried and removed by the owner
# (2026-10-17: it looked like a mistake on the page).
MATCH_RIGHT = ["My Religion", "My Prophet", "My Lord"]
INK, MUTED, GREEN, LINE, LINE2 = "#2a1d17", "#6b5b51", "#456f3a", "#c9bea6", "#e2dccf"
SIZE, ROW_H, BASE = 72, 112, 76          # word size, row height, baseline y in the row
FACE, WT = "sans", 500                    # Noto Sans Arabic: even strokes, clear teeth for tracing
BUB, BUB_IN = 13.5, 10                    # bubble outline width, inner (white) width

def _poly(l):
    return "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in l)

def word(r, x, kind):
    """Place a word with its right edge at x (Arabic starts on the right).
    model: solid letters. trace: bubble outline with a dashed centre line (owner's example),
    hollow dots, light grey harakat, green start dot at each letter group."""
    left = x - r["width"]
    g = f'<g transform="translate({left:.1f} {BASE})">'
    if kind == "model":
        g += "".join(f'<path d="{d}" fill="{INK}"/>' for d in r["bodies"] + r["dots"] + r["marks"])
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

def trace_row(ar, en, width):
    label_w = 92
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
        svg.append(word(w_, right, kind))
    svg.append(f'<text x="{width}" y="{BASE - 2}" text-anchor="end" class="en">{en}</text>')
    svg.append("</svg>")
    return "".join(svg)

def build(size):
    w, h, page = (816, 1056, "8.5in 11in") if size == "letter" else (794, 1123, "210mm 297mm")
    inner = w - 96
    trace_rows = "".join(trace_row(ar, en, inner) for ar, en in WORDS)
    left = "".join(f'<div class="mi"><div class="mw">{ar}</div><span class="dot"></span></div>' for ar, _ in WORDS)
    right = "".join(f'<div class="mi"><span class="dot"></span><div class="me">{en}</div></div>' for en in MATCH_RIGHT)
    match_rows = f'<div class="match"><div class="mcol">{left}</div><div class="mcol r">{right}</div></div>'
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
  .match {{ display: flex; justify-content: space-between; height: 190px; }}
  .mcol {{ width: 190px; display: flex; flex-direction: column; justify-content: space-around; }}
  .mcol.r {{ width: 200px; }}
  .mi {{ display: flex; align-items: center; }}
  .mcol:not(.r) .mi {{ justify-content: flex-end; }}
  .mw {{ font-family: "Noto Sans Arabic", sans-serif; font-weight: 600; font-size: 46px; line-height: 1; direction: rtl; text-align: right; padding-right: 18px; }}
  .me {{ font-weight: 800; font-size: 20px; padding-left: 16px; }}
  .dot {{ width: 14px; height: 14px; border-radius: 50%; background: {GREEN}; flex: none; }}
  .fill {{ font-size: 20px; font-weight: 700; line-height: 1.5; }}
  .fill .blank {{ display: inline-block; width: 90px; border-bottom: 2px solid {INK}; }}
  .answer {{ display: flex; align-items: flex-end; justify-content: space-between; gap: 24px; margin-top: 8px; }}
  .choices {{ white-space: nowrap; flex: none; display: flex; align-items: center; gap: 10px; font-weight: 800; font-size: 15px; color: {MUTED}; padding-bottom: 6px; }}
  .choices span {{ font-family: "Baloo 2", sans-serif; font-weight: 700; font-size: 22px; color: {INK}; border: 1.5px solid #c9bea6; border-radius: 10px; padding: 3px 12px 1px; }}
  .wline {{ white-space: nowrap; flex: 1; min-width: 0; font-weight: 800; font-size: 15px; color: {MUTED}; display: flex; align-items: flex-end; gap: 10px; }}
  .wline div {{ flex: 1; max-width: 288px; height: 67px; box-sizing: border-box; border-bottom: 2px solid {INK};
               background: linear-gradient(transparent 32px, {LINE2} 32px, {LINE2} 33.5px, transparent 33.5px); }}
  footer {{ padding: 11px 19px 12px; font-size: 12.5px; line-height: 1.45; color: #4a3a30;
           display: flex; justify-content: space-between; align-items: flex-end; gap: 24px; }}
  footer b {{ color: {INK}; }}
  .brand {{ text-align: right; white-space: nowrap; font-size: 12.5px; }}
  .brand div {{ font-family: "Baloo 2", sans-serif; font-weight: 800; font-size: 19px; color: {INK}; }}
  .brand i {{ font-style: normal; color: {GREEN}; }}
</style></head><body><div class="page">
  <header class="band">
    <div><div class="k">The Three Fundamental Principles, Lesson 3</div><h1>My Three Roots</h1></div>
    <div class="ar">الأُصُولُ الثَّلَاثَةُ</div>
  </header>
  <div class="name"><div>Name:<span></span></div><div>Date:<span style="width:130px"></span></div></div>
  <main>
    <section><h2><b>1</b>Trace the words <small>Start at the <i></i> and go right to left. Then write it alone in the box.</small></h2>{trace_rows}</section>
    <section><h2><b>2</b>Match <small>Draw a line from each word to its meaning.</small></h2>{match_rows}</section>
    <section><h2><b>3</b>Fill in the missing word</h2>
      <div class="fill">Shaykh Ibn Baz said: these three principles gather the whole <span class="blank"></span>.</div>
      <div class="answer">
        <div class="choices">Circle one: <span>house</span><span>religion</span><span>garden</span></div>
        <div class="wline">Write it:<div></div></div>
      </div>
    </section>
  </main>
  <footer class="band">
    <div><b>Source for parents:</b> "These three principles gather the whole religion" (meaning).
      <i>Sharh Thalathat al-Usul</i>, Shaykh Abdul-Aziz Ibn Baz, Dar al-Masir, 1st ed., 1418 AH, p. 38.</div>
    <div class="brand"><div>Sunnah<i>Saplings</i></div>Answers: Answer Key, Lesson 3</div>
  </footer>
</div></body></html>'''

for size, suffix in [("letter", ""), ("a4", "-a4")]:
    (HERE / f"lesson-03-worksheet-three-roots{suffix}.html").write_text(build(size), encoding="utf-8")
print("worksheets written")
