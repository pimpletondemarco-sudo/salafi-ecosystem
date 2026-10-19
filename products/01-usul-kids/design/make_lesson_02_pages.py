"""Lesson 2 "Allah Created Us", redesign 2026-10-18 (replaces l2wsA/B/C, which are on hold).

Two pages (owner-approved): page 1 "Learn" = tracing strip + FILL-IN check (circle the right word, then write it
on the line); page 2 "Do" = lift-the-flap questions (research/design/lift-the-flap-2026-10-18.md).
3 versions of each page (A/B/C), US Letter + A4.

Content ONLY from sources/lesson-02-allah-created-us.md (VERIFIED in VERIFICATION.md, wording per TRANSLATION-REVIEW-2):
- matn as quoted by Ibn Baz, Sharh Thalathat al-Usul, Dar al-Masir, 1st ed., p. 29:
  «أَنَّ اللهَ خَلَقَنَا وَرَزَقَنَا ولم يتركنا هملاً» "Allah created us, provided for us, and did not leave us without a purpose."
  (vowel marks on «لَمْ يَتْرُكْنَا هَمَلًا» added for children, as on the earlier worksheets; owner OK pending)
- Ibn Baz, same page: «الله خلق الخلق ليعبدوه ...» "Allah created His creation to worship Him." (version C, 4th flap;
  vowel marks on «لِيَعْبُدُوهُ» added by us, owner OK pending)
- al-Uthaymeen, Dar al-Thurayya, 4th ed., p. 30: "We cannot live without food and drink, and Allah is the One who created
  our food and drink." (Learn page version B)
NOT used: the provision hadith (on hold, no hadith number); 56:63-64 (no checked English meaning in the sources yet).
Wrong options in the fill-in are either words from the lesson that do not fit the sentence, or the everyday nouns
already used before (toys, shoes): no made-up statement about Allah is offered as a choice.
"""
from pages_lib import page, dims, trace_section, fill_item, fill_section, steps_line, h2, scissors, palm_svg, CUT, CUT_W, BONE, IN

TRACE = [("خَلَقَنَا", "He created us"), ("رَزَقَنَا", "He provided for us")]
MATN_EN = "Allah created us, provided for us, and did not leave us without a purpose."
SRC_MATN = (f"Meaning of Shaykh Muhammad ibn Abdul-Wahhab's words in Thalathat al-Usul: \"{MATN_EN}\"\n"
            "      <i>Sharh Thalathat al-Usul</i>, Shaykh Abdul-Aziz Ibn Baz, Dar al-Masir, 1st ed., p. 29.")
SRC_FOOD = ("\n      Meaning of Shaykh al-Uthaymeen's words: \"We cannot live without food and drink, and Allah is the One who created our\n"
            "      food and drink.\" <i>Sharh Thalathat al-Usul</i>, Shaykh Muhammad ibn Salih al-Uthaymeen, Dar al-Thurayya, 4th ed., p. 30.")
SRC_WORSHIP = (f"Meaning of Shaykh Muhammad ibn Abdul-Wahhab's words in Thalathat al-Usul: \"{MATN_EN[:-1]},\" and of Shaykh Ibn Baz's words: \"Allah created His creation\n"
               "      to worship Him.\" <i>Sharh Thalathat al-Usul</i>, Shaykh Ibn Baz, Dar al-Masir, 1st ed., p. 29.")

ITEM_PURPOSE = fill_item("", "Allah created us, provided for us, and did not leave us without a", ["created", "purpose", "provided"])
ITEM_CREATED = fill_item("", "Allah", ["drink", "purpose", "created"], after=" us, provided for us, and did not leave us without a purpose.")
ITEM_FOOD = fill_item("", "We cannot live without food and", ["toys", "drink", "shoes"])


# ---------------------------------------------------------------- Learn page
def learn(size, v):
    w, h, _ = dims(size)
    inner = w - 96
    palm = {"A": "header", "B": "name", "C": "bottom"}[v]
    items = {"A": [ITEM_PURPOSE], "B": [ITEM_PURPOSE, ITEM_FOOD], "C": [ITEM_CREATED]}[v]
    body = trace_section(1, TRACE, inner, size=70, row_h=112, base=78, label_w=150) + fill_section(2, items)
    src = SRC_MATN + (SRC_FOOD if v == "B" else "")
    css = (".fill .blank { width: 200px; } .fitem { background: #f3efe6; border-radius: 16px; padding: 18px 26px 22px; }"
           if v == "C" else "")
    return page(size, lesson=2, pno=1, kind="Learn", title="Allah Created Us", body=body, source=src, palm=palm,
                css=css)


# ---------------------------------------------------------------- Do page: lift the flap
QS = [("Who created us?", "خَلَقَنَا", "Allah created us."),
      ("Who provided for us?", "رَزَقَنَا", "Allah provided for us."),
      ("Did Allah leave us without a purpose?", "لَمْ يَتْرُكْنَا هَمَلًا", "He did not leave us without a purpose.")]
Q4 = ("Why did Allah create us?", "لِيَعْبُدُوهُ", "To worship Him.")
STEPS = ["Cut out the flap strip.", "Cut the flaps apart.", "Fold each grey tab.",
         "Glue each tab on its grey strip.", "Read the question, then lift the flap."]
INSET = 0.25 * IN          # answer box at least 0.25 in smaller than the door on every side (F3)


def box(x, y, w, h, cls, inner=""):
    return f'<div class="{cls}" style="left:{x:.1f}px;top:{y:.1f}px;width:{w:.1f}px;height:{h:.1f}px">{inner}</div>'


def flap_unit(i, q, bx, by, sx, sy, DW, DH, T, orient, ar_size, en_size=15):
    """Base unit (glue strip + door footprint + answer box) and its flap (tab + door) on the strip."""
    n = i + 1
    qtext, ar, en = q
    ans = f'<div class="ae" style="font-size:{en_size}px">{en}</div>'   # English only on Do pages (owner 2026-10-19)
    if orient == "top":
        g = box(bx, by, DW, T, "gs", f'<span>glue tab {n} here</span>')
        foot = box(bx, by + T, DW, DH, "fp")
        a = box(bx + INSET, by + T + INSET, DW - 2 * INSET, DH - 2 * INSET, "ab", f'<i>{n}</i>{ans}')
        tab = box(sx, sy, DW, T, "tab", '<span>glue the back of this tab</span>')
        door = box(sx, sy + T, DW, DH, "door col" if DW < 2.2 * IN else "door", f'<div class="dq"><b>{n}</b><span>{qtext}</span></div><div class="lift">Lift to see the answer</div>')
        fold = (f'<line x1="{sx}" y1="{sy + T}" x2="{sx + DW}" y2="{sy + T}" class="fold"/>'
                f'<text x="{sx + DW - 8}" y="{sy + T + 17}" class="fl" text-anchor="end">fold</text>')
        outline = f'<rect x="{sx}" y="{sy}" width="{DW}" height="{DH + T}" class="cut"/>'
    else:  # tab on the left, door opens like a book
        g = box(bx, by, T, DH, "gs v", f'<span>glue tab {n}</span>')
        foot = box(bx + T, by, DW, DH, "fp")
        a = box(bx + T + INSET, by + INSET, DW - 2 * INSET, DH - 2 * INSET, "ab", f'<i>{n}</i>{ans}')
        tab = box(sx, sy, T, DH, "tab v", '<span>glue the back</span>')
        door = box(sx + T, sy, DW, DH, "door", f'<div class="dq"><b>{n}</b><span>{qtext}</span></div><div class="lift">Lift to see the answer</div>')
        fold = (f'<line x1="{sx + T}" y1="{sy}" x2="{sx + T}" y2="{sy + DH}" class="fold"/>'
                f'<text x="{sx + T + 7}" y="{sy + DH - 10}" class="fl" transform="rotate(-90 {sx + T + 7} {sy + DH - 10})" dominant-baseline="hanging">fold</text>')
        outline = f'<rect x="{sx}" y="{sy}" width="{DW + T}" height="{DH}" class="cut"/>'
    return g + foot + a + tab + door, fold, outline


def do_page(size, v):
    w, h, _ = dims(size)
    inner = w - 96
    T = round(0.45 * IN)
    parts, lines, cuts = [], [], []
    if v == "A":   # 3 flaps in a row, tabs on top (doors lift up); palm beside the base
        DW, DH = round(2.05 * IN), round(2.2 * IN)
        gap = 10
        strip_w = 3 * DW
        sx0 = (inner - strip_w) / 2
        strip_y = T + DH + 62
        for i, q in enumerate(QS):
            u = flap_unit(i, q, i * (DW + gap), 0, sx0 + i * DW, strip_y, DW, DH, T, "top", 0, 21)
            parts.append(u[0]); lines.append(u[1]); cuts.append(u[2])
        ph = 88; pw = ph * 140 / 132
        bx_end = 3 * DW + 2 * gap
        parts.append(f'<div style="left:{bx_end + (inner - bx_end - pw) / 2:.1f}px;top:{T + DH - ph:.1f}px">{palm_svg(ph)}</div>')
        stage_h = strip_y + T + DH + 4
        sc = (sx0 - 16, strip_y)
        fold_label = (sx0 + strip_w - 4, strip_y + T - 4)
    elif v == "B":  # 3 flaps stacked in one column, tabs on the left; base left half, strip right half
        DW, DH = round(2.8 * IN), round(1.84 * IN)
        gap = 14
        sx0 = inner - (DW + T) - 2
        for i, q in enumerate(QS):
            u = flap_unit(i, q, 0, i * (DH + gap), sx0, i * DH + 14, DW, DH, T, "left", 0, 23)
            parts.append(u[0]); lines.append(u[1]); cuts.append(u[2])
        ph = 88; pw = ph * 140 / 132
        parts.append(f'<div style="left:{sx0 + (DW + T - pw) / 2:.1f}px;top:{3 * DH + 14 + 24:.1f}px">{palm_svg(ph)}</div>')
        stage_h = max(3 * DH + 2 * gap, 3 * DH + 14 + 24 + ph) + 4
        sc = (sx0 - 16, 14)
        fold_label = (sx0 + T + 6, 3 * DH + 14 + 16)
    else:          # C: 2 x 2 grid, 4 questions, tabs on top; palm in the header (palm report version A)
        DW, DH = round(3.44 * IN), round(1.1 * IN)
        T = round(0.4 * IN)
        gap = 12
        base_w = 2 * DW + gap
        bx0 = (inner - base_w) / 2
        sx0 = (inner - 2 * DW) / 2
        strip_y = 2 * (T + DH) + gap + 58
        for i, q in enumerate(QS + [Q4]):
            r, c = divmod(i, 2)
            u = flap_unit(i, q, bx0 + c * (DW + gap), r * (T + DH + gap), sx0 + c * DW, strip_y + r * (T + DH), DW, DH, T, "top",
                          0, 20)
            parts.append(u[0]); lines.append(u[1]); cuts.append(u[2])
        stage_h = strip_y + 2 * (T + DH) + 4
        sc = (sx0 - 16, strip_y)
        fold_label = (sx0 + 2 * DW - 4, strip_y + T - 4)
    svg = (f'<svg style="left:0;top:0;z-index:1" width="{inner}" height="{stage_h:.0f}">{"".join(lines)}{"".join(cuts)}'
           f'</svg>')
    stage = (f'<div class="stage" style="width:{inner}px;height:{stage_h:.0f}px">{"".join(parts)}{svg}'
             f'{scissors(sc[0], sc[1], 24)}</div>')
    body = f'<section>{h2(1, "Make the flaps, then lift them")}{steps_line(STEPS)}</section>{stage}'
    css = f'''
  ol.steps {{ font-size: 16px; gap: 6px 16px; }}
  .gs {{ background: #d9d3c4; display: grid; place-items: center; }}
  .gs span, .tab span {{ font-size: 12.5px; font-weight: 700; color: #6b5b51; }}
  .gs.v span, .tab.v span {{ writing-mode: vertical-rl; transform: rotate(180deg); }}
  .fp {{ background: #f6f3ec; }}
  .ab {{ background: #fff; border-radius: 10px; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; }}
  .ab i {{ position: absolute; left: 7px; top: 3px; font-style: normal; font-weight: 800; font-size: 13px; color: #8a7d6e; }}
  .aa {{ line-height: 1.45; color: #2a1d17; }}
  .ae {{ font-weight: 800; line-height: 1.25; color: #2a1d17; padding: 0 10px; text-wrap: balance; }}
  .tab {{ background: #d9d3c4; display: grid; place-items: center; }}
  .door {{ background: {BONE}; display: flex; flex-direction: column; justify-content: center; padding: 14px 18px; gap: 8px; }}
  .dq {{ display: flex; align-items: center; gap: 12px; font-size: 18px; font-weight: 800; line-height: 1.25; }}
  .dq b {{ width: 38px; height: 38px; border-radius: 50%; background: #456f3a; color: #fff; display: grid; place-items: center; flex: none;
           font-family: "Baloo 2", sans-serif; font-size: 22px; }}
  .lift {{ font-size: 13px; font-weight: 700; color: #6b5b51; padding-left: 50px; }}
  .door.col {{ align-items: center; text-align: center; }}
  .door.col .dq {{ flex-direction: column; gap: 10px; }}
  .door.col .lift {{ padding-left: 0; }}
  .cut {{ fill: none; stroke: {CUT}; stroke-width: {CUT_W}; }}
  .fold {{ stroke: #6b5b51; stroke-width: 1.33; stroke-dasharray: 5 4; }}
  .fl {{ font-family: "Nunito", sans-serif; font-size: 13px; font-weight: 800; fill: #4a3a30; }}
  .sc {{ z-index: 2; }}'''
    src = SRC_WORSHIP if v == "C" else SRC_MATN
    return page(size, lesson=2, pno=2, kind="Do", title="Lift the Flaps", body=body, source=src, css=css,
                palm="header" if v == "C" else None)


if __name__ == "__main__":
    from pathlib import Path
    here = Path(__file__).parent
    for v in "ABC":
        for size, suf in [("letter", ""), ("a4", "-a4")]:
            (here / f"lesson-02-learn-v{v}{suf}.html").write_text(learn(size, v), encoding="utf-8")
            (here / f"lesson-02-do-v{v}{suf}.html").write_text(do_page(size, v), encoding="utf-8")
    print("lesson 2 pages written")
