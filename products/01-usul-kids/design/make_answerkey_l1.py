"""Answer key for Lesson 1 "The Four Matters We Must Learn": layout A (owner-accepted for every lesson, 2026-10-18),
one version, US Letter and A4. Two pages, one per student page of the owner's picks (2026-10-19):
  page 1 = Learn version B (trace + Match), page 2 = Do version B (cut and glue the four matters into numbered boxes).

Layout A, as make_answerkey_l3.py: a small filled-in copy of the student page on the left (built by the SAME
generator and data, make_lesson_01_pages.learn/do_page(key=True), so it shows the current page with its
"For parents ... Teaching Guide" footer), the answers listed down the right, one source box across the bottom.
Text comes from guide/answer-key-lesson-01.md (parsed, never retyped); check() makes sure it agrees with the pages.
Source: the four matters as headed by al-Uthaymeen, VERIFIED in sources/VERIFICATION.md (Lesson 1 rows).
"""
import re
from worksheet_lib import HERE
from guide_lib import parse_key, header, footer, doc, PRODUCT
from make_answerkey_l3 import CSS, CHECK, copy_box
import make_lesson_01_pages as L1

V = "B"   # owner's picks for Lesson 1, Learn and Do

EXTRA = '''
  .row .n { width: 26px; height: 26px; border-radius: 50%; background: #c4bbb1; color: #fff; display: grid; place-items: center;
            font-family: "Baloo 2", sans-serif; font-weight: 800; font-size: 15px; flex: none; }
  .row .stack { display: flex; flex-direction: column; }
  .ans .note { font-size: 13.5px; line-height: 1.4; margin: 8px 0 0; }
  .strip { margin-top: 14px; }
  header .ar { white-space: nowrap; }
  .row.m .ar { min-width: 70px; }
  header { gap: 18px; }
  header h1 { font-size: 29px; }
'''


def key_text():
    md = (PRODUCT / "guide" / "answer-key-lesson-01.md").read_text(encoding="utf-8")
    acts = {a["n"]: a for a in parse_key(1)}
    meaning = re.search(r"^Meaning: (.+)$", md, re.M)[1].strip()
    for a in acts.values():   # the Meaning line is printed in the source box, not in the activity text
        a["text"] = a["text"].replace("Meaning: " + meaning, "").strip()
    return acts, meaning


def check(acts):
    """The key text and the page data must agree (top buyer complaint: keys that don't match)."""
    assert [ar for ar, _, _ in acts[1]["items"]] == L1.AR
    assert [(ar, en) for ar, _, en in acts[2]["items"]] == list(zip(L1.AR, L1.EN))
    assert sorted(en for _, _, en in acts[2]["items"]) == sorted(L1.MATCH_RIGHT)
    assert [(ar, en) for ar, _, en in acts[3]["items"]] == list(zip(L1.AR, L1.EN))   # order 1-4 = order of the matn
    assert "Uthaymeen" in L1.SOURCE and "Dar al-Thurayya, 4th ed." in L1.SOURCE
    assert "the book" not in str(acts).lower() and "Internal" not in str(acts) and ".md" not in str(acts)


def strip(a, meaning):
    return (f'<div class="strip"><b>Source for these answers.</b> Shaykh al-Uthaymeen heads the four matters of '
            f'<i>Thalathat al-Usul</i> in this order in his explanation. '
            f'<b>Meaning of Shaykh al-Uthaymeen\'s words:</b> {meaning} {a["source"]}'
            f'<div class="q">{a["arabic"]}</div></div>')


def learn_answers(acts):
    t, m = acts[1], acts[2]
    rows = "".join(f'<div class="row"><span class="ar">{ar}</span><span>{en}<br><span class="tr">{tr}</span></span></div>'
                   for ar, tr, en in t["items"])
    a1 = (f'<section class="ans"><h2><b>1</b>{t["title"]}</h2><p class="t">{t["text"].rstrip(":")} '
          f'(shown in green).</p>{rows}</section>')
    rows = "".join(f'<div class="row m">{CHECK}<span class="ar">{ar}</span><span class="to">→</span><span class="a">{en}</span></div>'
                   for ar, _, en in m["items"])
    a2 = f'<section class="ans"><h2><b>2</b>{m["title"]}</h2>{rows}</section>'
    return a1 + a2


def do_answers(acts):
    o = acts[3]
    rows = "".join(f'<div class="row"><span class="n">{i + 1}</span>{CHECK}<span class="stack"><span class="ar" style="text-align:left">{ar}</span>'
                   f'<span class="a">{en}</span></span></div>' for i, (ar, _, en) in enumerate(o["items"]))
    return (f'<section class="ans"><h2><b>1</b>{o["title"]}</h2><p class="t">{o["text"].rstrip(":")}:</p>{rows}'
            f'<p class="note">Each piece sits in its numbered box. Any order other than 1, 2, 3, 4 above needs another try.</p></section>')


def page(size, pno, kind, title, answers, filled, foot, src):
    hd = header(f"For parents: answers to Lesson 1, page {pno} ({kind})", f"Answer Key: {title}")
    ft = footer(f'<b>For parents.</b> {foot}', f'Answer Key, Lesson 1, page {pno}')
    body = (f'<div style="display:flex;gap:24px;flex:1;min-height:0">'
            f'<div>{copy_box(filled, size, 0.59)}<div class="cap">Lesson 1, page {pno}, filled in.</div></div>'
            f'<div style="flex:1;min-width:0">{answers}</div></div>{src}')
    return hd + f'<main>{body}</main>' + ft


def make():
    acts, meaning = key_text()
    check(acts)
    src = strip(acts[3], meaning)
    for size, suf in [("letter", ""), ("a4", "-a4")]:
        (HERE / f"lesson-01-answerkey-learn-filled{suf}.html").write_text(L1.learn(size, V, key=True), encoding="utf-8")
        (HERE / f"lesson-01-answerkey-do-filled{suf}.html").write_text(L1.do_page(size, V, key=True), encoding="utf-8")
        pages = [page(size, 1, "Learn", "The Four Matters", learn_answers(acts),
                      f"lesson-01-answerkey-learn-filled{suf}.html",
                      "The small copy shows each answer in green. Tracing has no single answer.", src),
                 page(size, 2, "Do", "The Four Matters in Order", do_answers(acts),
                      f"lesson-01-answerkey-do-filled{suf}.html",
                      "The small copy shows each piece glued in its numbered box, in green.", src)]
        (HERE / f"lesson-01-answerkey{suf}.html").write_text(doc(size, CSS + EXTRA, pages), encoding="utf-8")


if __name__ == "__main__":
    make()
    print("lesson 1 answer key written")
