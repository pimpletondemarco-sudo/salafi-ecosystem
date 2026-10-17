"""Teaching guide pages for Lesson 3 "The Three Questions": 3 layout versions (A, B, C), 2 pages each,
US Letter and A4.

Follows research/design/teaching-guide-2026-10-17.md:
- two pages per lesson, same order: page 1 = teach it (Before you start box, background, script,
  Arabic words, review game); page 2 = go deeper (If your child asks, From the Scholars)
- script: green "Say:" label, the parent's words in bold, actions in plain text, "or say it in your own words"
- From the Scholars as outlined panels (white inside to save ink): Arabic right-aligned, then
  "Meaning of Shaykh X's words:", then title, scholar, publisher, edition, printed page (no year)
- ayah text copied by code from sources/quran-ayat.md (quran.ai: King Fahd Complex text, Hilali-Khan)
All religious text is parsed from guide/teaching-guide-lesson-03.md (owner-accepted); nothing retyped.
Internal notes (e.g. the digital copy's typing slip) are left out of the customer page.
"""
import re
from guide_lib import parse_guide, header, footer, doc, ayat, HERE, GREEN, INK, MUTED, BONE

LESSON = {  # practical, non-religious details for the "Before you start" box
    "n": 3,
    "time": "About 15 to 20 minutes.",
    "need": "The printed worksheet and colouring page, a pencil, crayons, paper and scissors for the game.",
    "pages": 'Worksheet "My Three Roots" and the date-palm colouring page. Answers: Answer Key, Lesson 3.',
}

AR = re.compile("([ء-ْٰ]+(?: ﷺ)?)")


def arw(html):
    """Isolate each Arabic word inside English text so the words stay in reading order."""
    return AR.sub(r'<span class="arw">\1</span>', html)


def game_steps(text):
    parts = []
    for sent in re.split(r"(?<=\.) ", text):
        for k, p in enumerate(sent.split(" and your child ")):
            parts.append(("Your child " + p) if k else p)
    return [p if p.endswith(".") else p + "." for p in parts]


# a small line drawing of the game objects only: three paper root cards and a paper leaf (no living beings)
GAME_ART = f'''<svg class="gart" viewBox="0 0 176 70" width="176" height="70" fill="#fff" stroke="{INK}" stroke-width="2" stroke-linejoin="round" stroke-linecap="round">
  <path d="M4 6h34v40l-17 18-17-18z"/><path d="M48 6h34v40l-17 18-17-18z"/><path d="M92 6h34v40l-17 18-17-18z"/>
  <path d="M12 22h18M56 22h18M100 22h18" stroke="#b3a892" stroke-width="3"/>
  <path d="M138 54c0-26 14-42 34-46 2 22-10 42-34 46z" fill="#fff"/><path d="M138 54c8-12 18-26 30-40" fill="none"/></svg>'''

CSS = f'''
  main {{ font-size: 13.5px; line-height: 1.4; }}
  .saw {{ font-family: "Noto Sans Arabic", sans-serif; font-size: 1.15em; line-height: 1; }}
  .arw {{ font-family: "Noto Sans Arabic", sans-serif; font-weight: 600; font-size: 1.2em; unicode-bidi: isolate; direction: rtl; }}
  .box {{ background: {BONE}; border-radius: 14px; padding: 10px 16px 9px; margin-bottom: 12px; }}
  .box h3, .sec h3 {{ font-family: "Baloo 2", sans-serif; font-weight: 800; font-size: 19px; line-height: 1.15; margin: 0 0 5px; }}
  .box dl {{ display: grid; grid-template-columns: 76px 1fr; gap: 2px 10px; margin: 0; }}
  .box dt {{ font-weight: 800; }}
  .box dd {{ margin: 0; }}
  .sec {{ margin-bottom: 10px; }}
  .sec h3 small {{ font-family: "Nunito", sans-serif; font-weight: 700; font-size: 13px; color: {MUTED}; margin-left: 6px; }}
  .say {{ display: grid; grid-template-columns: 38px 1fr; gap: 2px 6px; margin: 0 0 4px; }}
  .say .lb {{ color: {GREEN}; font-weight: 800; }}
  .say .act {{ grid-column: 2; color: {INK}; }}
  .say b {{ font-weight: 800; }}
  table.words {{ border-collapse: collapse; width: 100%; }}
  table.words td {{ padding: 2px 10px 2px 0; vertical-align: middle; }}
  table.words td.ar {{ font-family: "Noto Sans Arabic", sans-serif; font-weight: 600; font-size: 23px; direction: rtl; text-align: right; line-height: 1.35; white-space: nowrap; width: 1%; padding-right: 16px; }}
  table.words td.sy {{ font-weight: 800; white-space: nowrap; }}
  table.words td.mn {{ color: {MUTED}; }}
  .note {{ font-size: 12.5px; color: {MUTED}; margin-top: 3px; }}
  ol.steps {{ margin: 0; padding-left: 22px; }}
  ol.steps li {{ margin-bottom: 3px; }}
  .game {{ display: flex; gap: 16px; align-items: flex-start; }}
  .gart {{ flex: none; }}
  .qa p {{ margin: 0 0 6px; }}
  .qa b {{ font-weight: 800; }}
  .qa .src i {{ color: inherit; }}
  .panel {{ border-radius: 12px; box-shadow: inset 0 0 0 2px {GREEN}; padding: 8px 13px 7px; margin-bottom: 8px; break-inside: avoid; }}
  .panel h4 {{ font-family: "Baloo 2", sans-serif; font-weight: 800; font-size: 15.5px; margin: 0 0 2px; line-height: 1.2; }}
  .panel .q {{ font-family: "Noto Sans Arabic", sans-serif; font-weight: 500; font-size: 18px; direction: rtl; text-align: right; line-height: 1.5; margin: 0 0 2px; }}
  .panel .q.quran {{ font-family: "Amiri Quran", "Amiri", serif; font-weight: 400; font-size: 21px; line-height: 1.75; margin-bottom: 7px; }}
  .panel .m {{ font-size: 13px; line-height: 1.38; margin: 0 0 2px; }}
  .panel .src {{ font-size: 11.5px; }}
  .panel .m b {{ font-weight: 800; }}
  .intro {{ font-size: 12.5px; color: {MUTED}; margin: -2px 0 6px; }}
'''


def parts(g):
    p = {}
    p["box"] = (f'<div class="box"><h3>Before you start</h3><dl>'
                f'<dt>Goal</dt><dd>{g["goal"]}</dd><dt>Time</dt><dd>{LESSON["time"]}</dd>'
                f'<dt>You need</dt><dd>{LESSON["need"]}</dd><dt>Pages</dt><dd>{LESSON["pages"]}</dd></dl></div>')
    p["bg"] = ('<div class="sec"><h3>Background for you<small>2 minutes to read</small></h3>'
               + "".join(f"<p>{x}</p>" for x in g["background"]) + '</div>')
    lines = ""
    for act, say in g["script"]:
        lines += '<div class="say">' + (f'<span></span><span class="act">{act}</span>' if act else "")
        lines += f'<span class="lb">Say:</span><span><b>{arw(say)}</b></span></div>'
    p["script"] = ('<div class="sec"><h3>Say it like this<small>Read the bold lines aloud, or say them in your own words.</small></h3>'
                   f'{lines}</div>')
    rows = "".join(f'<tr><td class="ar">{a}</td><td class="sy">{s}</td><td class="mn">{m}</td></tr>' for a, s, m in g["words"])
    p["words"] = ('<div class="sec"><h3>Say the Arabic words</h3>'
                  f'<table class="words">{rows}</table><div class="note">Capital letters show the strong part of the word. '
                  '"ee" as in <i>see</i>, "oo" as in <i>moon</i>, "aa" as in <i>father</i>, "th" as in <i>think</i>.</div></div>')
    steps = "".join(f"<li>{arw(s)}</li>" for s in game_steps(g["game"]))
    p["game"] = (f'<div class="sec"><h3>Review game: {g["game_title"]}<small>5 minutes, paper and pencil only</small></h3>'
                 f'<div class="game"><ol class="steps">{steps}</ol>{GAME_ART}</div></div>')
    qa = "".join(f'<p><b>{q}</b> {arw(a)}</p>' for q, a in g["asks"])
    p["asks"] = f'<div class="sec qa"><h3>If your child asks…</h3>{qa}</div>'
    panels = []
    for i, q in enumerate(g["quotes"], 1):
        cls = "q quran" if q["kind"] == "ayah" else "q"
        if q["kind"] == "ayah":
            ar_check, _ = ayat(q["ref"])
            assert ar_check == q["arabic"]
        ar = q["arabic"]
        if q["kind"] == "ayah":  # keep the last word and the ayah number together (no characters changed)
            head_, last2 = ar.rsplit(" ", 2)[0], " ".join(ar.rsplit(" ", 2)[1:])
            ar = f'{head_} <span style="white-space:nowrap">{last2}</span>'
            assert re.sub("<[^>]+>", "", ar) == q["arabic"]
        panels.append(f'<div class="panel"><h4>{i}. {q["title"]}</h4><div class="{cls}">{ar}</div>'
                      f'<p class="m"><b>{q["label"]}</b> "{q["meaning"]}"</p><div class="src">{q["source"]}</div></div>')
    p["panels"] = panels
    p["scholars_h"] = ('<h3 style="font-family:\'Baloo 2\',sans-serif;font-weight:800;font-size:19px;margin:0 0 4px">From the Scholars</h3>'
                       '<p class="intro">The scholars\' own words, with the meaning in plain English and the book and printed page.</p>')
    return p


def pages(g, v):
    p = parts(g)
    n = LESSON["n"]
    h1 = header(f"Teaching Guide, Lesson {n}: teach it", g["title"])
    h2 = header(f"Teaching Guide, Lesson {n}: go deeper", g["title"])
    f1 = footer("<b>For parents.</b> You can teach the whole lesson from this page. Page 2 has the scholars' words and answers to questions.",
                f"Teaching Guide, Lesson {n}, page 1 of 2")
    f2 = footer("<b>For parents.</b> English lines give the meaning of the Arabic, not a word-for-word translation.",
                f"Teaching Guide, Lesson {n}, page 2 of 2")
    P = p["panels"]
    if v == "A":   # one column, classic order
        b1 = p["box"] + p["bg"] + p["script"] + p["words"] + p["game"]
        b2 = p["asks"] + p["scholars_h"] + "".join(P)
    elif v == "B":  # main column + sidebar; scholars in a 2 x 2 grid
        b1 = (f'<div style="display:grid;grid-template-columns:1fr 286px;gap:26px;flex:1">'
              f'<div>{p["bg"]}{p["script"]}{p["game"]}</div><div>{p["box"]}{p["words"].replace("font-size: 26px", "")}</div></div>')
        b2 = (p["scholars_h"] + f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:0 14px">'
              f'<div>{P[0]}{P[2]}</div><div>{P[1]}{P[3]}</div></div>' + p["asks"])
    else:          # C: overview strip, lesson as 4 numbered steps; scholars as English | Arabic rows
        strip = p["box"].replace('<dl>', '<dl class="strip">')
        steps = [("Read the background", p["bg"]), ("Teach with the script", p["script"]),
                 ("Practise the Arabic words", p["words"]), ("Play the review game", p["game"])]
        b1 = strip + "".join(
            f'<div class="step"><h2><b>{k}</b>{t}</h2>{re.sub(r"<h3>.*?</h3>", "", body, count=1)}</div>'
            for k, (t, body) in enumerate(steps, 1))
        rows = "".join(re.sub(r'<div class="panel"><h4>(.*?)</h4>(<div class="q[^"]*">.*?</div>)(.*)</div>$',
                              r'<div class="panel row2"><div><h4>\1</h4>\3</div>\2</div>', x) for x in P)
        b2 = f'<div class="qa2">{p["asks"]}</div>' + p["scholars_h"] + rows
    return [h1 + f'<main class="v{v}">{b1}</main>' + f1, h2 + f'<main class="v{v}">{b2}</main>' + f2]


CSS_C = '''
  .vC .box dl.strip { grid-template-columns: 62px 1fr 74px 1fr; }
  .vC .step { margin-bottom: 10px; }
  .vC .intro { display: none; }
  .vC .panel .q { font-size: 17px; }
  .vC .panel .q.quran { font-size: 19px; }
  .vC .step h2 { font-size: 19px; margin-bottom: 4px; }
  .vC .step h2 b { width: 27px; height: 27px; font-size: 15px; }
  .vC .step .sec { margin: 0 0 0 37px; }
  .vC .panel.row2 { display: grid; grid-template-columns: 1.3fr 1fr; gap: 14px; align-items: center; }
  .vC .panel.row2 .q { margin: 0; }
  .vC .qa2 .qa { columns: 2; column-gap: 24px; margin-bottom: 8px; }
  .vC .qa2 .qa h3 { column-span: all; }
  .vC .qa2 .qa p { margin-bottom: 6px; break-inside: avoid; font-size: 13px; }
  .vC .panel.row2 { padding-top: 7px; padding-bottom: 6px; }
  .vB .box dl { grid-template-columns: 1fr; gap: 0; }
  .vB .box dt { margin-top: 5px; }
  .vB table.words, .vB table.words tbody, .vB table.words tr { display: block; }
  .vB table.words tr { margin-bottom: 5px; }
  .vB table.words td { display: inline; padding: 0; }
  .vB table.words td.ar { display: block; width: auto; text-align: left; font-size: 24px; line-height: 1.4; padding: 0; }
  .vB table.words td.sy::after { content: " "; }
  .vB .game { flex-direction: column; gap: 6px; }
'''


if __name__ == "__main__":
    g = parse_guide(LESSON["n"])
    for v in "ABC":
        for size, suf in [("letter", ""), ("a4", "-a4")]:
            html = doc(size, CSS + CSS_C, pages(g, v)).replace("ﷺ", '<span class="saw">ﷺ</span>')
            (HERE / f"lesson-03-guide-v{v}{suf}.html").write_text(html, encoding="utf-8")
    print("guide pages written")
