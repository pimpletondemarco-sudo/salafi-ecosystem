"""Two-page lessons (owner-approved 2026-10-18): a "Learn" page and a "Do" page per lesson.

Shared shell for the redesigned Lesson 1 and Lesson 2 pages. Same look as the accepted Lesson 3 worksheet v6
(worksheet_lib.py): white page, rounded bone header/footer panels kept 0.3 in inside the paper edge,
Baloo 2 / Nunito / Noto Sans Arabic (Amiri only for the product name), green numbered circles,
"For parents: ... Teaching Guide, Lesson N" footer (owner 2026-10-19; `source` is kept as an internal
record only, not printed), accepted tracing format (worksheet_lib.trace_row).
New here:
- the ONE small palm picture (palm_spot.py) in one of three places (palm report §4):
  "header" (inside the header panel, left), "name" (top right beside Name/Date), "bottom" (bottom right, above footer)
- absolute-positioned "stage" helpers for hands-on Do pages (cut-and-glue, lift-the-flap)
- cut lines: solid 2 pt dark grey (sequence/flap reports R4/F5), a small scissors icon (an object), no hands
"""
from worksheet_lib import FONTS, INK, MUTED, GREEN, LINE, LINE2, trace_row, parents_note, KEY_CSS
from palm_spot import palm_svg

CUT = "#4a4a4a"          # cut lines: solid, 2 pt
CUT_W = 2.67              # 2 pt at 96 px/in
BONE, BONE2, GLUE = "#e5e1d8", "#f3efe6", "#d9d3c4"
IN = 96                   # px per inch
CHECK = (f'<svg class="ck" viewBox="0 0 20 20" width="26" height="26"><circle cx="10" cy="10" r="10" fill="{GREEN}"/>'
         f'<path d="M5.5 10.4l3 3 6-6.6" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def dims(size):
    return (816, 1056, "8.5in 11in") if size == "letter" else (794, 1123, "210mm 297mm")


def scissors(x, y, s=24, rot=0):
    """Small scissors icon (an object) centred at x, y."""
    return (f'<svg class="sc" style="position:absolute;left:{x - s / 2:.1f}px;top:{y - s / 2:.1f}px;transform:rotate({rot}deg)" '
            f'width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{CUT}" stroke-width="2" stroke-linecap="round">'
            f'<circle cx="5.5" cy="6.5" r="3.2" fill="#fff"/><circle cx="5.5" cy="17.5" r="3.2" fill="#fff"/>'
            f'<path d="M8.3 8.2 L22 17.2 M8.3 15.8 L22 6.8"/></svg>')


def steps_line(items):
    """Numbered 1-2-3 instruction line, words not icons, 17-18 px (reports R5 / F7)."""
    return '<ol class="steps">' + "".join(f'<li><b>{i + 1}</b>{t}</li>' for i, t in enumerate(items)) + '</ol>'


def h2(n, title, small=""):
    return f'<h2><b>{n}</b>{title}' + (f' <small>{small}</small>' if small else "") + '</h2>'


def trace_section(n, words, inner, size=62, row_h=92, base=64, label_w=110, key=False):
    rows = "".join(trace_row(ar, en, inner, size, row_h, base, label_w, key=key) for ar, en in words)
    return (f'<section>{h2(n, "Trace the words", "Start at the <i></i> and go right to left. Then write it alone in the box.")}'
            f'{rows}</section>')


def match_section(n, left, right, h=200, lw=210, rw=240, ar_size=34, panel=False, inner=720, pairs=None):
    """Match: only the real pairs (owner 2026-10-17), Arabic left, English right, shuffled.
    pairs={arabic: english} draws the answer-key lines in green (columns use space-around, so item i is
    centred at h*(2i+1)/(2n); the panel adds 6px / 24px padding)."""
    lines = ""
    if pairs:
        px, py = (24, 6) if panel else (0, 0)
        x1, x2, cnt = px + lw - 7, inner - px - rw + 7, len(left)
        for i, ar in enumerate(left):
            j = right.index(pairs[ar])
            y1, y2 = py + h * (2 * i + 1) / (2 * cnt), py + h * (2 * j + 1) / (2 * cnt)
            lines += (f'<line x1="{x1}" y1="{y1:.1f}" x2="{x2}" y2="{y2:.1f}" stroke="{GREEN}" stroke-width="5" stroke-linecap="round"/>'
                      f'<circle cx="{x1}" cy="{y1:.1f}" r="11" fill="{GREEN}"/><circle cx="{x2}" cy="{y2:.1f}" r="11" fill="{GREEN}"/>')
        lines = f'<svg class="mlines" width="{inner}" height="{h + 2 * py}">{lines}</svg>'
    L = "".join(f'<div class="mi"><div class="mw" style="font-size:{ar_size}px">{ar}</div><span class="dot"></span></div>' for ar in left)
    R = "".join(f'<div class="mi"><span class="dot"></span><div class="me">{en}</div></div>' for en in right)
    return (f'<section>{h2(n, "Match", "Draw a line from each word to its meaning.")}'
            f'<div class="match{" panel" if panel else ""}" style="height:{h}px"><div class="mcol" style="width:{lw}px">{L}</div>'
            f'<div class="mcol r" style="width:{rw}px">{R}</div>{lines}</div></section>')


def fill_item(said, before, choices, after=".", ar=None):
    """Circle the right word, then write it on the line (owner 2026-10-17: two steps only)."""
    arb = f'<div class="fill-ar">{ar[0]}<span>{ar[1]}</span></div>' if ar else ""
    return (f'<div class="fitem">{arb}<div class="said">{said}</div>'
            f'<div class="fill">{before} <span class="blank"></span>{after}</div>'
            f'<div class="choices"><em>Circle one:</em>' + "".join(f'<span>{c}</span>' for c in choices) + '</div></div>')


def fill_section(n, items):
    return f'<section>{h2(n, "Fill in the missing word", "Circle the right word, then write it on the line.")}{"".join(items)}</section>'


def page(size, *, lesson, pno, kind, title, body, source, palm=None, css="", cls="", palm_h=92, key=False):
    """key=True: the filled-in answer-key copy of the same page (student content faded, panels as outlines,
    answers in green). The footer stays the student footer, so the copy shows the page exactly as printed."""
    if key:
        css += KEY_CSS + PAGE_KEY_CSS
        cls = (cls + " key").strip()
    w, h, pg = dims(size)
    inner = w - 96
    header_palm = palm_svg(66, cls="palm hp") if palm == "header" else ""
    name_palm = palm_svg(78, cls="palm np") if palm == "name" else ""
    bottom_palm = f'<div class="palmrow">{palm_svg(84, cls="palm bp")}</div>' if palm == "bottom" else ""
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8">{FONTS}<style>
  @page {{ size: {pg}; margin: 0; }}
  html, body {{ margin: 0; background: #fff; }}
  .page {{ width: {w}px; height: {h}px; box-sizing: border-box; padding: 29px 0; display: flex; flex-direction: column;
          font-family: "Nunito", sans-serif; color: {INK}; overflow: hidden; position: relative; }}
  .band {{ margin: 0 29px; background: {BONE}; border-radius: 14px; }}
  header {{ padding: 12px 19px 10px; display: flex; align-items: center; gap: 14px; }}
  header .t {{ flex: 1; }}
  header .k {{ font-weight: 700; font-size: 14px; color: {MUTED}; }}
  header h1 {{ font-family: "Baloo 2", sans-serif; font-weight: 800; font-size: 34px; line-height: 1; margin: 3px 0 0; letter-spacing: -0.01em; }}
  header .ar {{ font-family: "Amiri", serif; font-weight: 700; direction: rtl; font-size: 34px; color: {GREEN}; line-height: 1.3; }}
  .name {{ padding: 14px 48px 0; font-weight: 700; font-size: 16px; display: flex; align-items: flex-end; gap: 40px; }}
  .name span {{ display: inline-block; width: 210px; border-bottom: 2px solid {INK}; margin-left: 8px; }}
  .name .palm {{ margin-left: auto; margin-bottom: -4px; }}
  header:has(.hp) h1 {{ font-size: 29px; white-space: nowrap; }}
  header:has(.hp) .ar {{ font-size: 28px; }}
  main {{ flex: 1; padding: 0 48px 10px; display: flex; flex-direction: column; justify-content: space-evenly; position: relative; }}
  .palmrow {{ padding: 0 48px 4px; display: flex; justify-content: flex-end; }}
  h2 {{ font-family: "Baloo 2", sans-serif; font-weight: 800; font-size: 23px; margin: 0 0 6px; display: flex; align-items: center; gap: 12px; white-space: nowrap; }}
  h2 b {{ width: 34px; height: 34px; border-radius: 50%; background: {GREEN}; color: #fff; display: grid; place-items: center; font-size: 19px; flex: none; }}
  h2 small {{ font-family: "Nunito", sans-serif; font-weight: 700; font-size: 16px; color: {MUTED}; white-space: normal; }}
  h2 small i {{ font-style: normal; display: inline-block; width: 10px; height: 10px; border-radius: 50%; background: {GREEN}; margin: 0 2px; }}
  .trow {{ display: block; }}
  .trow .en {{ font-family: "Nunito", sans-serif; font-weight: 800; font-size: 15px; fill: {MUTED}; }}
  .faint .trow .en {{ font-size: 13px; font-weight: 700; fill: #aaa093; }}
  .match {{ display: flex; justify-content: space-between; }}
  .match.panel {{ background: {BONE2}; border-radius: 14px; padding: 6px 24px; }}
  .mcol {{ display: flex; flex-direction: column; justify-content: space-around; }}
  .mi {{ display: flex; align-items: center; }}
  .mcol:not(.r) .mi {{ justify-content: flex-end; }}
  .mw {{ font-family: "Noto Sans Arabic", sans-serif; font-weight: 600; line-height: 1.6; direction: rtl; text-align: right; padding-right: 18px; }}
  .me {{ font-weight: 800; font-size: 20px; padding-left: 16px; }}
  .dot {{ width: 14px; height: 14px; border-radius: 50%; background: {GREEN}; flex: none; }}
  .fitem + .fitem {{ margin-top: 30px; }}
  .said {{ font-size: 17px; font-weight: 700; color: {MUTED}; margin-bottom: 6px; }}
  .fill {{ font-size: 23px; font-weight: 700; line-height: 1.6; }}
  .fill .blank {{ display: inline-block; width: 230px; height: 30px; border-bottom: 2px solid {INK}; vertical-align: baseline; margin-left: 4px; }}
  .choices {{ display: flex; align-items: center; gap: 14px; margin-top: 12px; }}
  .choices em {{ font-style: normal; font-weight: 700; font-size: 17px; color: {MUTED}; }}
  .choices span {{ font-family: "Baloo 2", sans-serif; font-weight: 700; font-size: 23px; color: {INK}; border: 1.5px solid #c9bea6; border-radius: 10px; padding: 3px 14px 1px; }}
  .fill-ar {{ float: right; text-align: center; margin: 0 0 6px 24px; font-family: "Noto Sans Arabic", sans-serif; font-weight: 600; font-size: 34px; line-height: 1.7; direction: rtl; background: {BONE2}; border-radius: 14px; padding: 6px 22px 8px; }}
  .fill-ar span {{ display: block; direction: ltr; font-family: "Nunito", sans-serif; font-size: 14px; font-weight: 700; color: {MUTED}; line-height: 1.3; }}
  ol.steps {{ list-style: none; margin: 4px 0 0; padding: 0; display: flex; flex-wrap: wrap; gap: 6px 20px; font-size: 17px; font-weight: 700; }}
  ol.steps li {{ display: flex; align-items: center; gap: 7px; }}
  ol.steps b {{ width: 24px; height: 24px; border-radius: 50%; background: {GREEN}; color: #fff; display: grid; place-items: center; font-size: 14px; flex: none; }}
  .stage {{ position: relative; margin: 0 auto; }}
  .stage > * {{ position: absolute; box-sizing: border-box; }}
  .num {{ width: 43px; height: 43px; border-radius: 50%; background: {GREEN}; color: #fff; display: grid; place-items: center;
          font-family: "Baloo 2", sans-serif; font-weight: 800; font-size: 25px; line-height: 1; }}
  .ar {{ font-family: "Noto Sans Arabic", sans-serif; font-weight: 600; direction: rtl; line-height: 1.6; }}
  footer {{ padding: 11px 19px 12px; font-size: 12.5px; line-height: 1.45; color: #4a3a30;
           display: flex; justify-content: space-between; align-items: flex-end; gap: 24px; }}
  footer b {{ color: {INK}; }}
  .brand {{ text-align: right; white-space: nowrap; font-size: 12.5px; }}
  .brand div {{ font-family: "Baloo 2", sans-serif; font-weight: 800; font-size: 19px; color: {INK}; }}
  .brand i {{ font-style: normal; color: {GREEN}; }}
{css}</style></head><body><div class="page {cls}">
  <header class="band">{header_palm}
    <div class="t"><div class="k">The Three Fundamental Principles, Lesson {lesson}, page {pno}: {kind}</div><h1>{title}</h1></div>
    <div class="ar">الأُصُولُ الثَّلَاثَةُ</div>
  </header>
  <div class="name"><div>Name:<span></span></div><div>Date:<span style="width:130px"></span></div>{name_palm}</div>
  <main>
    {body}
  </main>{bottom_palm}
  <footer class="band">
    <div class="pn">{parents_note(lesson)}</div>
    <div class="brand"><div>Sunnah<i>Saplings</i></div>Lesson {lesson}, page {pno}. Answers: Answer Key, Lesson {lesson}</div>
  </footer>
</div></body></html>'''


PAGE_KEY_CSS = f"""
  .key .palm {{ opacity: .38; }}
  .key .faint .trow .en, .key .trow .en {{ fill: #b9b0a6; }}
  .key .match.panel {{ background: none; box-shadow: inset 0 0 0 2px #e2dccf; }}
  .key ol.steps b, .key .num {{ background: #c4bbb1; }}
  .key ol.steps, .key h2 {{ color: #a39a92; }}
  .key .stone {{ background: #f1eee8; }}
  .key .strip {{ opacity: .38; }}
  .key .sc {{ opacity: .38; }}
"""
