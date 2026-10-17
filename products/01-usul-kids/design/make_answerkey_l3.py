"""Answer key page for Lesson 3 "My Three Roots": 3 layout versions (A, B, C), US Letter and A4.

Follows research/design/answer-key-2026-10-17.md:
- a reduced, filled-in copy of the student page, built by the SAME generator and data as the worksheet
  (worksheet_lib.build(..., key=True) with make_worksheet_l3.SPEC), so the key can never disagree with it
- answers in bold brand green with a check mark (never red); student content faded; panels as outlines
- source strip under the religious answer: "Meaning of Shaykh X's words", Arabic, title, scholar,
  publisher, edition, printed page (no year)
- "For parents" on the page; one page per student page; separate PDF file per version
Text comes from guide/answer-key-lesson-03.md (parsed, never retyped). Later lessons: call make(n, SPEC, ...).
"""
import re
from worksheet_lib import build, HERE, GREEN, INK, MUTED
from guide_lib import parse_key, header, footer, doc, inline
import make_worksheet_l3 as ws

CHECK = (f'<svg class="ck" viewBox="0 0 20 20" width="18" height="18"><circle cx="10" cy="10" r="10" fill="{GREEN}"/>'
         f'<path d="M5.5 10.4l3 3 6-6.6" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>')

CSS = f'''
  .copy {{ position: relative; flex: none; border-radius: 10px; box-shadow: 0 0 0 2px #d6cdbb; overflow: hidden; background: #fff; }}
  .copy iframe {{ border: 0; transform-origin: 0 0; position: absolute; left: 0; top: 0; }}
  .cap {{ font-size: 12.5px; color: {MUTED}; font-weight: 700; margin-top: 6px; }}
  .ans h2 {{ font-size: 19px; margin-bottom: 4px; }}
  .ans h2 b {{ width: 26px; height: 26px; font-size: 15px; }}
  .ans .t {{ font-size: 13.5px; line-height: 1.4; margin: 0 0 6px; }}
  .row {{ display: flex; align-items: center; gap: 10px; font-size: 15px; font-weight: 700; line-height: 1.15; margin: 0 0 5px; }}
  .row .ar {{ font-family: "Noto Sans Arabic", sans-serif; font-weight: 600; font-size: 25px; line-height: 1.5; direction: rtl; min-width: 64px; text-align: right; }}
  .row .tr {{ font-style: italic; font-weight: 600; color: {MUTED}; font-size: 13.5px; }}
  .row .to {{ color: {MUTED}; font-weight: 800; }}
  .a, .ans p b {{ color: {GREEN}; font-weight: 800; }}
  .ck {{ flex: none; vertical-align: -3px; }}
  .say {{ font-size: 15px; line-height: 1.4; font-weight: 700; }}
  .strip {{ border-radius: 12px; box-shadow: inset 0 0 0 2px #d6cdbb; padding: 10px 14px 9px; font-size: 12.5px; line-height: 1.45; color: #4a3a30; }}
  .strip .q {{ font-family: "Noto Sans Arabic", sans-serif; direction: rtl; text-align: right; font-size: 20px; font-weight: 500; color: {INK}; line-height: 1.6; margin: 2px 0; }}
  .strip b {{ color: {INK}; }}
  .how {{ margin-top: 18px; font-size: 13.5px; line-height: 1.4; }}
  .how h3 {{ font-family: "Baloo 2", sans-serif; font-weight: 800; font-size: 17px; margin: 0 0 4px; }}
  .how ol {{ margin: 0; padding-left: 20px; }}
  .how li {{ margin-bottom: 3px; }}
  .strip .q {{ white-space: nowrap; }}
  .strip .q.sm {{ font-size: 16.5px; }}
  .row {{ gap: 8px; }}
  .row .ar {{ min-width: 52px; }}
  section.ans {{ margin-bottom: 14px; }}
'''


HOWTO = ('<div class="how"><h3>How to check</h3><ol><li>Put your child\'s page beside this one.</li>'
         '<li>Look for the green answers and check marks.</li>'
         '<li>If your child asks "how do we know?", read the source together.</li></ol></div>')


def copy_box(src, size, scale):
    w, h = (816, 1056) if size == "letter" else (794, 1123)
    return (f'<div class="copy" style="width:{w * scale:.0f}px;height:{h * scale:.0f}px">'
            f'<iframe src="{src}" width="{w}" height="{h}" scrolling="no" style="transform:scale({scale})"></iframe></div>')


def blocks(acts, spec):
    out = {}
    for a in acts:
        head = f'<h2><b>{a["n"]}</b>{a["title"]}</h2>'
        if a["n"] == 1:
            rows = "".join(f'<div class="row"><span class="ar">{ar}</span><span>{en}<br><span class="tr">{t}</span></span></div>'
                           for ar, t, en in a["items"])
            out[1] = (f'<section class="ans">{head}<p class="t">{a["text"].strip().rstrip(":")}, and wrote it alone in the box '
                      f'(shown in green).</p>{rows}</section>')
        elif a["items"]:
            rows = "".join(f'<div class="row">{CHECK}<span class="ar">{ar}</span><span class="to">→</span><span class="a">{en}</span>'
                           f'</div>' for ar, _, en in a["items"])
            out[a["n"]] = f'<section class="ans">{head}{rows}</section>'
        else:
            ans = a["answer"][0].upper() + a["answer"][1:]
            out[a["n"]] = f'<section class="ans">{head}<p class="say">{CHECK} {ans}</p></section>'
            src = spec["source"].replace("\n", " ")
            out["strip"] = (f'<div class="strip"><b>Source for this answer.</b> {src}'
                            f'<div class="q">{a["arabic"]}</div></div>')
    return out


def check(acts, spec):
    """The key text and the worksheet data must agree (top buyer complaint: keys that don't match)."""
    pairs = dict(spec["trace"])
    for a in acts:
        for ar, _, en in a["items"]:
            assert pairs[ar] == en, (ar, en)
        if a["answer"]:
            word = re.search(r"<b>(.+?)</b>", a["answer"])[1]
            assert word in spec["act3"]["choices"]
            spec["act3"]["answer"] = word
            assert a["source"].rstrip(".") in spec["source"].replace("\n      ", " "), "key source differs from worksheet footer"


def page(n, spec, acts, size, v, filled):
    b = blocks(acts, spec)
    w = 816 if size == "letter" else 794
    k = f"For parents: answers to the Lesson {n} worksheet"
    hd = header(k, f'Answer Key: {spec["title"]}')
    ft = footer('<b>For parents.</b> The small copy shows each answer in green. Tracing has no single answer.',
                f'Answer Key, Lesson {n}')
    if v == "A":   # copy left, answers right, source strip across the bottom
        s = 0.59
        body = (f'<div style="display:flex;gap:24px;flex:1;min-height:0">'
                f'<div>{copy_box(filled, size, s)}<div class="cap">The worksheet, filled in.</div></div>'
                f'<div style="flex:1;min-width:0">{b[1]}{b[2]}{b[3]}</div></div>{b["strip"]}')
    elif v == "B":  # answers first, in three columns; copy below left; source + how-to beside it
        s = 0.5
        body = (f'<div style="display:grid;grid-template-columns:1.1fr 1fr 1fr;gap:6px 22px">{b[1]}{b[2]}{b[3]}</div>'
                f'<div style="display:flex;gap:26px;margin-top:auto;align-items:flex-start">'
                f'<div>{copy_box(filled, size, s)}<div class="cap">The worksheet, filled in.</div></div>'
                f'<div style="flex:1;min-width:0">{b["strip"].replace('class="q"', 'class="q sm"')}{HOWTO}</div></div>')
    else:          # C: tracing + match notes left, copy right; fill-in answer and its source across the bottom
        s = 0.57
        body = (f'<div style="display:flex;gap:26px">'
                f'<div style="flex:1;min-width:0">{b[1]}{b[2]}</div>'
                f'<div>{copy_box(filled, size, s)}<div class="cap">The worksheet, filled in.</div></div></div>'
                f'<div style="display:grid;grid-template-columns:1fr 1.35fr;gap:26px;margin-top:auto;align-items:start">'
                f'<div>{b[3]}</div>{b["strip"]}</div>')
    return hd + f'<main>{body}</main>' + ft


def make(n, spec, filled_stem, out_stem):
    acts = parse_key(n)
    check(acts, spec)
    for size, suf in [("letter", ""), ("a4", "-a4")]:
        (HERE / f"{filled_stem}{suf}.html").write_text(build(size, spec, key=True), encoding="utf-8")
    for v in "ABC":
        for size, suf in [("letter", ""), ("a4", "-a4")]:
            html = doc(size, CSS, [page(n, spec, acts, size, v, f"{filled_stem}{suf}.html")])
            (HERE / f"{out_stem}-v{v}{suf}.html").write_text(html, encoding="utf-8")


if __name__ == "__main__":
    spec = dict(ws.SPEC, act3=dict(ws.SPEC["act3"]))
    make(3, spec, "lesson-03-answerkey-filled", "lesson-03-answerkey")
    print("answer key pages written")
