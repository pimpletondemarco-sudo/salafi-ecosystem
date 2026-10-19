"""Answer key for Lesson 2 "Allah Created Us": layout A (owner-accepted for every lesson, 2026-10-18),
one version, US Letter and A4. Two pages, one per student page of the owner's picks (2026-10-19):
  page 1 = Learn version A (trace two words + circle-then-write "...without a ____"),
  page 2 = Do version C (four lift-the-flaps in a 2 x 2 grid, shown lifted open with their answers).

Built exactly like make_answerkey_l1.py: a small filled-in copy of the student page on the left (the SAME generator
and data, make_lesson_02_pages.learn/do_page(key=True)), the answers down the right (Arabic with its meaning allowed,
since the key is for parents), one source box across the bottom. Text comes from guide/answer-key-lesson-02.md
(parsed, never retyped); check() makes sure it agrees with the pages.
Sources: the matn as quoted by Ibn Baz and Ibn Baz's «الله خلق الخلق ليعبدوه», both Sharh Thalathat al-Usul,
Dar al-Masir, 1st ed., p. 29 (VERIFIED in sources/VERIFICATION.md, Lesson 2 rows).
"""
import re
from worksheet_lib import HERE
from guide_lib import parse_key, header, footer, doc, PRODUCT
from make_answerkey_l3 import CSS, CHECK, copy_box
import make_lesson_02_pages as L2

LEARN_V, DO_V = "A", "C"   # owner's picks for Lesson 2

EXTRA = '''
  .row .n { width: 26px; height: 26px; border-radius: 50%; background: #c4bbb1; color: #fff; display: grid; place-items: center;
            font-family: "Baloo 2", sans-serif; font-weight: 800; font-size: 15px; flex: none; }
  .row .stack { display: flex; flex-direction: column; gap: 1px; }
  .row.fl { align-items: flex-start; margin-bottom: 11px; }
  .row.fl .n, .row.fl .ck { margin-top: 1px; }
  .row .qq { font-size: 13.5px; font-weight: 700; color: #6b5b51; line-height: 1.3; }
  .row .mean { display: flex; flex-direction: column; font-size: 13px; font-weight: 600; color: #6b5b51; line-height: 1.3; }
  .row .mean .ar { font-size: 20px; min-width: 0; text-align: left; line-height: 1.6; }
  .row .mean.in { flex-direction: row; align-items: baseline; gap: 8px; }
  .ans .say { margin: 0 0 6px; }
  .ans .note { font-size: 13.5px; line-height: 1.4; margin: 8px 0 0; }
  .strip { margin-top: 14px; }
  .strip .two { display: flex; gap: 22px; margin: 4px 0 2px; }
  .strip .two > div { flex: 1; min-width: 0; }
  .strip .two > div:first-child { flex: 1.3; }
  .strip .q { margin: 0; }
  .strip i { white-space: nowrap; }
  .strip .two .q { text-align: right; }
  header .ar { white-space: nowrap; }
  header { gap: 18px; }
  header h1 { font-size: 29px; }
'''

MEAN_RE = re.compile(r'^(.*?) \(Arabic: ([^,]+), ([^,]+), "(.+)"\)$')


def key_text():
    md = (PRODUCT / "guide" / "answer-key-lesson-02.md").read_text(encoding="utf-8")
    acts = {a["n"]: a for a in parse_key(2)}
    meanings = re.findall(r"^Meaning: (.+)$", md, re.M)          # [matn meaning, Ibn Baz meaning]
    in_ar = re.search(r"^In Arabic: (\S.*?) \(([^)]+)\), meaning \"(.+)\"\.?$", md, re.M)
    for a in acts.values():   # Meaning / In Arabic lines go in the source box and the answer row, not the activity text
        for m in meanings:
            a["text"] = a["text"].replace("Meaning: " + m, "")
        a["text"] = a["text"].replace(in_ar[0], "").strip()
    flaps = []
    for q, _, rest in acts[3]["items"]:
        m = MEAN_RE.match(rest)
        flaps.append((re.sub(r"^\d+\. ", "", q), m[1], m[2], m[3], m[4]))   # question, answer, arabic, translit, meaning
    return acts, meanings, (in_ar[1], in_ar[2], in_ar[3]), flaps


def check(acts, meanings, flaps):
    """The key text and the page data must agree (top buyer complaint: keys that don't match)."""
    assert [(ar, en) for ar, _, en in acts[1]["items"]] == L2.TRACE
    assert acts[2]["answer"].startswith(f"<b>{L2.FILL['purpose'][3]}</b>.")
    assert L2.FILL["purpose"][0] + " " + L2.FILL["purpose"][3] + "." in acts[2]["answer"]
    assert meanings[0] == L2.MATN_EN
    assert [(q, a) for q, a, *_ in flaps] == [(q, en) for q, _, en in L2.QS + [L2.Q4]]
    assert [ar for _, _, ar, _, _ in flaps] == [ar for _, ar, _ in L2.QS + [L2.Q4]]
    assert "Dar al-Masir, 1st ed., p. 29" in acts[2]["source"] and "Dar al-Masir, 1st ed., p. 29" in acts[3]["source"]
    assert acts[2]["arabic"] == "أَنَّ اللهَ خَلَقَنَا وَرَزَقَنَا ولم يتركنا هملاً" and acts[3]["arabic"] == "الله خلق الخلق ليعبدوه"
    txt = str(acts) + str(flaps)
    assert "the book" not in txt.lower() and "Internal" not in txt and ".md" not in txt


def strip(acts, meanings):
    return (f'<div class="strip"><b>Source for these answers.</b>'
            f'<div class="two"><div><b>Shaykh Muhammad ibn Abdul-Wahhab wrote in <i>Thalathat al-Usul</i>:</b>'
            f'<div class="q">{acts[2]["arabic"]}</div><b>Meaning of his words:</b> {meanings[0]}</div>'
            f'<div><b>Shaykh Ibn Baz explains:</b><div class="q">{acts[3]["arabic"]}</div>'
            f'<b>Meaning of Shaykh Ibn Baz\'s words:</b> {meanings[1]}</div></div>'
            f'Both from {acts[3]["source"]} Shaykh Ibn Baz quotes the words of <i>Thalathat al-Usul</i> and explains them on that page.</div>')


def learn_answers(acts, in_ar):
    t, f = acts[1], acts[2]
    rows = "".join(f'<div class="row"><span class="ar">{ar}</span><span>{en}<br><span class="tr">{tr}</span></span></div>'
                   for ar, tr, en in t["items"])
    a1 = (f'<section class="ans"><h2><b>1</b>{t["title"]}</h2><p class="t">{t["text"].rstrip(":")} '
          f'(shown in green).</p>{rows}</section>')
    ans = f["answer"][0].upper() + f["answer"][1:]
    ar, tr, mean = in_ar
    a2 = (f'<section class="ans"><h2><b>2</b>{f["title"]}</h2><p class="say">{CHECK} {ans}</p>'
          f'<div class="row"><span class="stack"><span class="mean in">In Arabic:<span class="ar">{ar}</span></span>'
          f'<span class="tr">{tr}: {mean}</span></span></div></section>')
    return a1 + a2


def do_answers(acts, flaps):
    o = acts[3]
    rows = "".join(f'<div class="row fl"><span class="n">{i + 1}</span>{CHECK}<span class="stack"><span class="qq">{q}</span>'
                   f'<span class="a">{a}</span><span class="mean"><span class="ar">{ar}</span>"{mean}"</span></span></div>'
                   for i, (q, a, ar, _, mean) in enumerate(flaps))
    return (f'<section class="ans"><h2><b>1</b>{o["title"]}</h2><p class="t">{o["text"].split(" Flaps")[0].rstrip(":")}:</p>{rows}'
            f'<p class="note">The flaps are glued by their tabs; lifting each one shows its answer. The Arabic is for you; '
            f'the children\'s flaps are in English.</p></section>')


def page(size, pno, kind, title, answers, filled, foot, src):
    hd = header(f"For parents: answers to Lesson 2, page {pno} ({kind})", f"Answer Key: {title}")
    ft = footer(f'<b>For parents.</b> {foot}', f'Answer Key, Lesson 2, page {pno}')
    body = (f'<div style="display:flex;gap:24px;flex:1;min-height:0">'
            f'<div>{copy_box(filled, size, 0.555)}<div class="cap">Lesson 2, page {pno}, filled in.</div></div>'
            f'<div style="flex:1;min-width:0">{answers}</div></div>{src}')
    return hd + f'<main>{body}</main>' + ft


def make():
    acts, meanings, in_ar, flaps = key_text()
    check(acts, meanings, flaps)
    src = strip(acts, meanings)
    for size, suf in [("letter", ""), ("a4", "-a4")]:
        (HERE / f"lesson-02-answerkey-learn-filled{suf}.html").write_text(L2.learn(size, LEARN_V, key=True), encoding="utf-8")
        (HERE / f"lesson-02-answerkey-do-filled{suf}.html").write_text(L2.do_page(size, DO_V, key=True), encoding="utf-8")
        pages = [page(size, 1, "Learn", "Allah Created Us", learn_answers(acts, in_ar),
                      f"lesson-02-answerkey-learn-filled{suf}.html",
                      "The small copy shows each answer in green. Tracing has no single answer.", src),
                 page(size, 2, "Do", "Lift the Flaps", do_answers(acts, flaps),
                      f"lesson-02-answerkey-do-filled{suf}.html",
                      "The small copy shows each flap lifted open and its answer in green.", src)]
        (HERE / f"lesson-02-answerkey{suf}.html").write_text(doc(size, CSS + EXTRA, pages), encoding="utf-8")


if __name__ == "__main__":
    make()
    print("lesson 2 answer key written")
