"""Lesson 3 worksheet "My Three Roots" in the chosen cover style (v4, bone and green).

Writes US Letter and A4 HTML files. Content comes only from
sources/lesson-03-three-questions.md (verified): the three words and Ibn Baz's line
"These three principles gather the whole religion" (Dar al-Masir, printed p. 38).
White page so it prints cheaply; colour only in the header, numbers and footer.
"""
from pathlib import Path

HERE = Path(__file__).parent
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Amiri:wght@700'
         '&family=Baloo+2:wght@700;800&family=Nunito:wght@600;700;800&display=swap">')

WORDS = [("رَبِّي", "My Lord"), ("دِينِي", "My Religion"), ("نَبِيِّي", "My Prophet")]
MATCH_RIGHT = ["My Religion", "My Prophet", "My Lord"]  # shuffled; answers in the answer key

def build(size):
    w, h, page = (816, 1056, "8.5in 11in") if size == "letter" else (794, 1123, "210mm 297mm")
    trace_rows = "".join(f'''
      <div class="trow">
        <div class="en">{en}</div>
        <div class="ar model">{ar}</div><div class="ar ghost">{ar}</div><div class="ar ghost">{ar}</div>
      </div>''' for ar, en in WORDS)
    match_rows = "".join(f'''
      <div class="mrow"><div class="ar mw">{ar}</div><span class="dot"></span><span class="gap"></span>
        <span class="dot"></span><div class="me">{en}</div></div>''' for (ar, _), en in zip(WORDS, MATCH_RIGHT))
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8">{FONTS}<style>
  @page {{ size: {page}; margin: 0; }}
  html, body {{ margin: 0; background: #fff; }}
  .page {{ width: {w}px; height: {h}px; box-sizing: border-box; display: flex; flex-direction: column;
          font-family: "Nunito", sans-serif; color: #2a1d17; overflow: hidden; }}
  .ar {{ font-family: "Amiri", serif; font-weight: 700; direction: rtl; }}
  header {{ background: #e5e1d8; padding: 26px 48px 22px; display: flex; align-items: flex-end; justify-content: space-between; }}
  header .k {{ font-weight: 700; font-size: 16px; color: #6b5b51; }}
  header h1 {{ font-family: "Baloo 2", sans-serif; font-weight: 800; font-size: 40px; line-height: 1; margin: 4px 0 0; }}
  header .ar {{ font-size: 40px; color: #456f3a; line-height: 1.3; }}
  .name {{ padding: 18px 48px 0; font-weight: 700; font-size: 16px; display: flex; gap: 40px; }}
  .name span {{ display: inline-block; width: 210px; border-bottom: 2px solid #2a1d17; margin-left: 8px; }}
  main {{ flex: 1; padding: 6px 48px 0; display: flex; flex-direction: column; justify-content: space-evenly; }}
  h2 {{ font-family: "Baloo 2", sans-serif; font-weight: 800; font-size: 24px; margin: 0 0 10px; display: flex; align-items: center; gap: 12px; }}
  h2 b {{ width: 36px; height: 36px; border-radius: 50%; background: #456f3a; color: #fff; display: grid; place-items: center; font-size: 20px; }}
  h2 small {{ font-family: "Nunito", sans-serif; font-weight: 700; font-size: 16px; color: #6b5b51; }}
  .trow {{ display: grid; grid-template-columns: 130px 1fr 1fr 1fr; align-items: end; height: 92px;
          background: linear-gradient(transparent 88px, #c9bea6 88px, #c9bea6 90px, transparent 90px); }}
  .trow .en {{ font-weight: 800; font-size: 16px; color: #6b5b51; padding-bottom: 30px; }}
  .trow .ar {{ font-size: 50px; line-height: 80px; padding-bottom: 6px; text-align: center; }}
  .model {{ color: #2a1d17; }}
  .ghost {{ color: transparent; -webkit-text-stroke: 1.4px #a89d88; }}
  .mrow {{ display: grid; grid-template-columns: 150px 14px 1fr 14px 170px; align-items: center; height: 64px; }}
  .mw {{ font-size: 40px; text-align: right; padding-right: 18px; }}
  .me {{ font-weight: 800; font-size: 20px; padding-left: 18px; }}
  .dot {{ width: 14px; height: 14px; border-radius: 50%; background: #456f3a; }}
  .fill {{ font-size: 20px; font-weight: 700; line-height: 1.6; }}
  .fill .blank {{ display: inline-block; width: 115px; border-bottom: 2px solid #2a1d17; }}
  .choices {{ display: flex; gap: 46px; margin-top: 10px; font-family: "Baloo 2", sans-serif; font-weight: 700; font-size: 24px; }}
  footer {{ background: #e5e1d8; padding: 14px 48px 16px; font-size: 13px; line-height: 1.45; color: #4a3a30;
           display: flex; justify-content: space-between; align-items: flex-end; gap: 30px; }}
  footer b {{ color: #2a1d17; }}
  .brand {{ font-family: "Baloo 2", sans-serif; font-weight: 800; font-size: 20px; color: #2a1d17; white-space: nowrap; }}
  .brand i {{ font-style: normal; color: #456f3a; }}
</style></head><body><div class="page">
  <header>
    <div><div class="k">The Three Fundamental Principles, Lesson 3</div><h1>My Three Roots</h1></div>
    <div class="ar">الأُصُولُ الثَّلَاثَةُ</div>
  </header>
  <div class="name"><div>Name:<span></span></div><div>Date:<span style="width:130px"></span></div></div>
  <main>
    <section><h2><b>1</b>Trace the words <small>Read the first one, then trace the two after it.</small></h2>{trace_rows}</section>
    <section><h2><b>2</b>Match <small>Draw a line from each word to its meaning.</small></h2>{match_rows}</section>
    <section><h2><b>3</b>Fill in the missing word <small>Circle it, then write it on the line.</small></h2>
      <div class="fill">Shaykh Ibn Baz said: these three principles gather the whole <span style="white-space:nowrap"><span class="blank"></span>.</span></div>
      <div class="choices"><span>house</span><span>religion</span><span>garden</span></div>
    </section>
  </main>
  <footer>
    <div><b>Source for parents:</b> "These three principles gather the whole religion" (meaning).
      <i>Sharh Thalathat al-Usul</i>, Shaykh Abdul-Aziz Ibn Baz, Dar al-Masir, 1st ed., 1418 AH, p. 38.</div>
    <div class="brand">Sunnah<i>Saplings</i></div>
  </footer>
</div></body></html>'''

for size, suffix in [("letter", ""), ("a4", "-a4")]:
    (HERE / f"lesson-03-worksheet-three-roots{suffix}.html").write_text(build(size), encoding="utf-8")
print("worksheets written")
