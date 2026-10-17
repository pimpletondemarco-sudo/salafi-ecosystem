"""Shared parts for the parent pages (answer key + teaching guide) of The Three Fundamental Principles.

Same look as the accepted cover v4 / worksheet (worksheet_lib.py): white page, bone #e5e1d8 header and
footer panels kept 0.3in inside the edge, green #456f3a accent, chocolate #2a1d17 ink, Baloo 2 headings,
Nunito text, Noto Sans Arabic for Arabic, Amiri only for the product name.

Content is never typed here. It is read from:
- guide/answer-key-lesson-NN.md and guide/teaching-guide-lesson-NN.md (owner-reviewed text)
- sources/quran-ayat.md (quran.ai output: King Fahd Complex text + Hilali-Khan) for every ayah
Customer citations: title, scholar, publisher, edition, printed page, NO year (owner, 2026-10-17).
Internal notes (Shamela links, "digital copy has a typing slip") are dropped from customer pages.
"""
import re
from pathlib import Path
from worksheet_lib import INK, MUTED, GREEN

HERE = Path(__file__).parent
PRODUCT = HERE.parent
BONE = "#e5e1d8"
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Amiri:wght@700&family=Amiri+Quran'
         '&family=Noto+Sans+Arabic:wght@400;500;600&family=Baloo+2:wght@700;800'
         '&family=Nunito:ital,wght@0,500;0,600;0,700;0,800;1,600&display=swap">')
PRODUCT_AR = "الأُصُولُ الثَّلَاثَةُ"
SIZES = {"letter": (816, 1056, "8.5in 11in"), "a4": (794, 1123, "210mm 297mm")}


# ---------- text helpers ----------
def inline(s):
    """Markdown bold/italic to HTML."""
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    return re.sub(r"\*(.+?)\*", r"<i>\1</i>", s)


def cite(s):
    """'*Title*, Shaykh X (Publisher, 1st ed.), p. 38' -> 'Title, Shaykh X, Publisher, 1st ed., p. 38' (no year)."""
    s = re.sub(r" \(([^()]*ed\.)\)", r", \1", s.strip())
    assert not re.search(r"\b(1[34]\d\d|19\d\d|20\d\d)\b", s), f"year in customer citation: {s}"
    return inline(s)


def no_year(html):
    for c in re.findall(r"<i>Sharh[^<]*</i>[^<]{0,120}", html):
        assert not re.search(r"\b(1[34]\d\d|19\d\d|20\d\d)\b", c), c
    return html


# ---------- sources ----------
def ayat(ref):
    """ref '14:24' or '103:1–3' -> (arabic, english) copied from sources/quran-ayat.md (quran.ai output)."""
    m = re.match(r"(\d+):(\d+)(?:[–-](\d+))?", ref)
    s, a, b = int(m[1]), int(m[2]), int(m[3] or m[2])
    rows = {}
    for line in (PRODUCT / "sources" / "quran-ayat.md").read_text(encoding="utf-8").splitlines():
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) >= 3 and re.fullmatch(r"\d+:\d+", c[0]):
            rows[c[0]] = (c[1], re.sub(r"\s*\(quran\.ai[^)]*\)\s*$", "", c[2]))
    keys = [f"{s}:{k}" for k in range(a, b + 1)]
    return " ".join(rows[k][0] for k in keys), " ".join(rows[k][1] for k in keys)


def parse_guide(n):
    """teaching-guide-lesson-NN.md -> dict of sections."""
    md = (PRODUCT / "guide" / f"teaching-guide-lesson-{n:02d}.md").read_text(encoding="utf-8")
    title = re.search(r"^# Teaching Guide — Lesson \d+: (.+)$", md, re.M)[1]
    secs = {}
    for block in re.split(r"^## ", md, flags=re.M)[1:]:
        head, _, body = block.partition("\n")
        secs[head.strip()] = body.strip()
    g = {"title": title}
    g["goal"] = inline(secs["Goal of the lesson"])
    g["background"] = [inline(p) for p in secs["Background for the parent (2 minutes)"].split("\n\n")]
    # From the Scholars
    quotes = []
    for item in re.split(r"^\*\*\d+\. ", secs["From the Scholars (commentary)"], flags=re.M)[1:]:
        head, _, rest = item.partition("**")
        q = {"title": head.strip(), "lines": rest}
        q["arabic"] = " ".join(l[1:].strip() for l in rest.splitlines() if l.startswith(">"))
        mm = re.search(r"^Meaning: (.+)$", rest, re.M)[1]
        src = re.search(r"^Source: (.+)$", rest, re.M)
        ref = re.search(r"(\d+:\d+(?:[–-]\d+)?)", head)
        if ref and ("Surah" in head or "Surat" in head or "ayah" in head.lower()):
            ar, en = ayat(ref[1])
            norm = lambda t: re.sub(r"\s+", " ", t).strip()
            assert norm(ar) == norm(q["arabic"]), f"guide ayah {ref[1]} differs from quran-ayat.md"
            q.update(kind="ayah", ref=ref[1], arabic=ar, meaning=en,
                     label="Meaning of the ayah, from <i>The Noble Qur'an</i> (Hilali-Khan):",
                     source=f"{re.search(r'(Sur(?:ah|at) [^0-9]+?) [0-9]', head)[1]} {ref[1]}. Arabic text: King Fahd Complex (Madinah) mushaf.")
        else:
            who = ("Shaykh Muhammad ibn Abdul-Wahhab" if "original text" in head else
                   "Shaykh al-Uthaymeen" if "Uthaymeen" in head else "Shaykh Ibn Baz")
            q.update(kind="quote", meaning=inline(mm.strip().strip('"')), label=f"Meaning of {who}'s words:",
                     source=cite(src[1]))
        quotes.append(q)
    g["quotes"] = quotes
    # script
    script = []
    for l in re.findall(r"^\d+\. (.+)$", secs["Say it like this (script)"], re.M):
        if l.startswith('"'):
            script.append(("", inline(l.strip('"'))))
        else:
            act, _, say = l.partition(': "')
            script.append((inline(act) + ".", inline(say.rstrip('"'))))
    g["script"] = script
    # Arabic words table
    words = []
    for l in secs["Say the Arabic words"].splitlines()[2:]:
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if len(c) == 3:
            words.append(c)
    g["words"] = words
    # If your child asks
    asks = []
    for l in re.findall(r"^- (.+)$", secs["If your child asks…"], re.M):
        m = re.match(r"\*\*(.+?)\*\* (.+)$", l)
        q, a = m[1], m[2]
        a = re.sub(r"\((\*[^*]+\*, .+?, p\. \d+)\)", lambda x: "(" + cite(x[1]) + ")", a)
        asks.append((inline(q), inline(a)))
    g["asks"] = asks
    gk = [k for k in secs if k.startswith("Review game")][0]
    g["game_title"] = gk.split(":", 1)[1].strip()
    g["game"] = inline(secs[gk])
    return g


def parse_key(n):
    """answer-key-lesson-NN.md -> list of activities {n, title, text, items, answer, source, arabic}."""
    md = (PRODUCT / "guide" / f"answer-key-lesson-{n:02d}.md").read_text(encoding="utf-8")
    acts = []
    for block in re.split(r"^## ", md, flags=re.M)[1:]:
        head, _, body = block.partition("\n")
        num, title = head.split(". ", 1)
        a = {"n": int(num), "title": title.strip(), "items": [], "text": "", "answer": "", "source": "", "arabic": ""}
        for l in body.strip().splitlines():
            l = l.strip()
            if l.startswith("- "):
                m = re.match(r"- (\S+) \(([^)]+)\): (.+)$", l)
                if m:
                    a["items"].append((m[1], m[2], m[3]))
                else:
                    ar, en = l[2:].split(" → ")
                    a["items"].append((ar.strip(), "", en.strip()))
            elif l.startswith("Answer:"):
                a["answer"] = inline(l[7:].strip())
            elif l.startswith("Source line:"):
                s = l[12:].strip().rstrip(".")
                m = re.match(r"(Shaykh [^,]+), (\*[^*]+\*), (.+)$", s)  # reorder to title first
                a["source"] = cite(f"{m[2]}, {m[1]}, {m[3]}." if m else s + ".")
            elif l.startswith("Arabic:"):
                a["arabic"] = l[7:].strip()
            elif l.startswith("(Internal"):
                continue  # internal Shamela link: never on customer pages
            elif l:
                a["text"] += inline(l) + " "
        acts.append(a)
    return acts


# ---------- page shell ----------
def css(size):
    w, h, page = SIZES[size]
    return f'''
  @page {{ size: {page}; margin: 0; }}
  html, body {{ margin: 0; background: #fff; }}
  .page {{ width: {w}px; height: {h}px; box-sizing: border-box; padding: 29px 0; display: flex; flex-direction: column;
          font-family: "Nunito", "Noto Sans Arabic", sans-serif; color: {INK}; overflow: hidden; page-break-after: always; break-after: page; }}
  .band {{ margin: 0 29px; background: {BONE}; border-radius: 14px; }}
  header {{ padding: 13px 19px 11px; display: flex; align-items: center; justify-content: space-between; }}
  header .k {{ font-weight: 700; font-size: 14px; color: {MUTED}; }}
  header h1 {{ font-family: "Baloo 2", sans-serif; font-weight: 800; font-size: 32px; line-height: 1; margin: 3px 0 0; letter-spacing: -0.01em; }}
  header .ar {{ font-family: "Amiri", serif; font-weight: 700; direction: rtl; font-size: 32px; color: {GREEN}; line-height: 1.3; }}
  main {{ flex: 1; padding: 18px 48px 14px; display: flex; flex-direction: column; min-height: 0; }}
  footer {{ padding: 10px 19px 11px; font-size: 12px; line-height: 1.45; color: #4a3a30;
           display: flex; justify-content: space-between; align-items: flex-end; gap: 24px; }}
  footer b {{ color: {INK}; }}
  .brand {{ text-align: right; white-space: nowrap; font-size: 12px; }}
  .brand div {{ font-family: "Baloo 2", sans-serif; font-weight: 800; font-size: 18px; color: {INK}; }}
  .brand i {{ font-style: normal; color: {GREEN}; }}
  h2 {{ font-family: "Baloo 2", sans-serif; font-weight: 800; font-size: 21px; line-height: 1.1; margin: 0 0 6px; display: flex; align-items: center; gap: 10px; }}
  h2 b {{ width: 30px; height: 30px; border-radius: 50%; background: {GREEN}; color: #fff; display: grid; place-items: center; font-size: 17px; flex: none; }}
  h2 small {{ font-family: "Nunito", sans-serif; font-weight: 700; font-size: 13.5px; color: {MUTED}; }}
  p {{ margin: 0 0 6px; }}
  .ar {{ font-family: "Noto Sans Arabic", sans-serif; direction: rtl; }}
  .quran {{ font-family: "Amiri Quran", "Amiri", serif; direction: rtl; }}
  .src {{ font-size: 12px; color: {MUTED}; line-height: 1.4; }}
  .src i {{ color: {INK}; }}
'''


def header(kicker, title):
    return (f'<header class="band"><div><div class="k">{kicker}</div><h1>{title}</h1></div>'
            f'<div class="ar">{PRODUCT_AR}</div></header>')


def footer(left, right):
    return (f'<footer class="band"><div>{left}</div>'
            f'<div class="brand"><div>Sunnah<i>Saplings</i></div>{right}</div></footer>')


def doc(size, extra_css, pages):
    body = "".join(f'<div class="page">{p}</div>' for p in pages)
    return no_year(f'<!doctype html><html lang="en"><head><meta charset="utf-8">{FONTS}<style>{css(size)}{extra_css}</style></head>'
                   f'<body>{body}</body></html>')
