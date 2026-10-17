# Translation Review 2: our English meanings vs. the trusted translators

Reviewed by: translation-reviewer · 2026-10-17 · INTERNAL ONLY (not for customers)
Scope: every English label, scholar sentence and footer meaning in
`design/make_worksheet_l1.py`, `make_worksheet_l2.py`, `make_worksheet_l3.py` (and the shared header in
`worksheet_lib.py`), plus every "Simple meaning" line in `sources/lesson-01..03 *.md`.

Copyright: the short quotes below are for checking only. They must NOT be pasted into products.
Every "suggested wording" is our own wording, matched to the translators' terms.

## Plain-English summary: what to change

Overall our meanings are faithful. Nothing is WRONG. Five small wording changes bring us in line with the
terms the trusted translators share:

1. **"four things" → "four matters".** Both Abu Khadeejah and Hasan as-Somali call them "matters" (Abu
   Khadeejah also says "affairs"). Change the Lesson 1 title "The Four Things We Must Learn" to
   **"The Four Matters We Must Learn"**, and the question "Who must learn these four things?" to
   **"Who must learn these four matters?"**
2. **"He provides for us" → "He provided for us".** Both translators use the past tense (رَزَقَنَا), the same
   tense as "He created us". Use it on the Lesson 2 trace, match and word-bank labels.
3. **"without purpose" → "without a purpose".** Both translators say "did not leave us without a purpose".
   Use **"He did not leave us without a purpose"** on the Lesson 2 labels and in the footer.
4. **Lesson 2 matn meaning (source file):** say "these three matters", "act upon them" and "provided for us",
   as both translators do: *"Every Muslim, male and female, must learn these three matters and act upon
   them. The first: Allah created us, provided for us, and did not leave us without a purpose."*
5. **Ibn Baz's "Allah created us to worship Him…":** his Arabic says الخلق ("the creation" / "them"), not "us",
   and gives three words (هملاً، سداً، عبثاً). No trusted translation of this Ibn Baz footnote was reachable, so
   this is a faithfulness note against the Arabic, not a translator's wording. Suggested: *"Allah created His
   creation to worship Him. He did not create them without a purpose or for nothing."*

Smaller, optional points: say "the religion of Islam" (both translators) in the Lesson 1 knowledge meaning;
"Acting upon it" instead of "Acting on it" (both say "act upon"); keep "Patience" as the one-word label (it
renders the printed word الصَّبْرُ), but in the guide explain that the matn means patience with the harm met
on this path (both translators keep "harm"). Make "We can't" (source file) and "We cannot" (worksheet) the
same. Keep "root" in the usul/tree line: Hasan as-Somali says "trunk", but Hilali-Khan 14:24, which our rules
require for that ayah, says "root".

Edition note for the owner (no change made, Arabic is not ours to edit): Abu Khadeejah's matn (p. 20)
reads «خَلَقَنَا لِعِبَادَتِهِ» ("created us to worship Him"); the Ibn Baz matn we quote (Dar al-Masir p. 29)
reads «خَلَقَنَا وَرَزَقَنَا» without «لعبادته». Both are real editions; our worksheet follows Ibn Baz.

**Abu Iyaad (abuiyaad.com):** the site has **no translation of Thalathat al-Usul or of its explanations**.
I indexed every category and monthly archive (258 links) and searched the full text of all 238 articles.
Only a few shared terms appear (see "Abu Iyaad" column). So no line could be checked against his rendering
of the same passage; those are NOT FOUND. Where he uses a term, it agrees with the others.

## Sources used

| Key | Translator | Work | Where read |
|---|---|---|---|
| AK | Abu Khadeejah 'Abdul-Wahid | *The Three Fundamentals of Islam and Their Proofs* (Study Guide ebook), Salafi Publications, 2nd ed. Feb 2021 | owner's PDF `research/translations/abukhadeejah-three-fundamentals-ebook-2021/Three-Fundamentals-Study-Guide-2021-Ebook-V1.4.pdf` (printed page numbers from the "PAGE n" footers) |
| HS | Hasan as-Somali | *A Gift to the Intellects in Explanation of the Three Fundamental Principles*, Shaykh 'Ubaid al-Jabiri, Salafi Publications, 1st ed. 2007 | owner's PDF `research/translations/emaanlibrary-ubayd-jabiri-three-fundamentals/Exp-Three-Fundamental-Principles-Ubaid-Al-Jaabiree.pdf` (printed page numbers; same file as emaanlibrary.com book page `/book/explanation-of-the-three-fundamental-principles-shaykh-ubaid-al-jaabiree/`) |
| AI | Abu Iyaad Amjad Rafiq | articles on abuiyaad.com | live site, 2026-10-17 (URLs per row) |

Not reached / not usable:
- abukhadeejah.com, sunnahpublishing.net (Maaz Qureshi), authenticstatements.com, troid.org, rasheedbarbee.com:
  connection refused from this session (tested 2026-10-17). **Rasheed Barbee and Maaz Qureshi could not be
  checked at all** (no PDF of theirs in `research/translations/`).
- abuiyaad.com: home page reset the connection once; `/sitemap.xml` returns HTTP 500; the site search ignores
  the query. Worked around by crawling `/c/<category>/<n>` and `/archives/<yyyy>/<mm>/<n>`.
- emaanlibrary.com also hosts an English *Explanation of the Three Fundamental Principles* by Shaykh Ibn Baz,
  but it is translated by Umm 'A'ishah Rumaysah Bond (Maktabatulirshad, 2017), who is **not** on the owner's
  list, so it was not used. Its children's book PDF has no text layer and no translator I could read; not used.
- No trusted translation of **al-Uthaymeen's** or **Ibn Baz's** own *Sharh* was reachable, so lines quoting
  those two scholars' explanations are NOT FOUND for the exact passage (terms still compared).

## Table

Verdicts: MATCHES / IMPROVE / WRONG / NOT FOUND (no reference covers that passage).
"Agreed term" = the term the trusted translators share for this item.

### Lesson 1: the four matters (make_worksheet_l1.py, lesson-01-four-matters.md)

| # | Where | Our wording | AK (Abu Khadeejah) | HS (Hasan as-Somali / al-Jabiri) | AI (Abu Iyaad, abuiyaad.com) | AI2 (Abu Iyaad, other sites) | Agreed term | Verdict | Suggested wording (ours) |
|---|---|---|---|---|---|---|---|---|---|
| 1.1 | header, all worksheets | "The Three Fundamental Principles" | "the Three Fundamental Principles", p. 105 (last line of the matn); cover title "The Three Fundamentals" | title "The Three Fundamental Principles" (title page) | NOT FOUND (only the Arabic title transliterated, "al-Uṣūl al-Thalāthah", footnote 15, https://abuiyaad.com/a/badawi-hijab) | NOT FOUND | Three Fundamental Principles | MATCHES | keep |
| 1.2 | L1 title | "The Four Things We Must Learn" | "learn four affairs", p. 14; "The four matters that are incumbent…", p. 5 | "knowledge of four matters", p. 20 | NOT FOUND | NOT FOUND | four **matters** | IMPROVE | "The Four Matters We Must Learn" |
| 1.3 | L1 version C question | "Who must learn these four things?" | as 1.2 | as 1.2 | NOT FOUND | NOT FOUND | matters | IMPROVE | "Who must learn these four matters?" |
| 1.4 | trace / match / bank | "Knowledge" | "Firstly: Knowledge", p. 14 | "Knowledge", p. 20 | NOT FOUND | NOT FOUND | Knowledge | MATCHES | keep |
| 1.5 | trace | "Action" | "To act upon that knowledge", p. 15 | "Action upon that", p. 20 | NOT FOUND | NOT FOUND | action / act upon | MATCHES | keep |
| 1.6 | match / bank | "Acting on it" | "act upon", p. 15 | "Action upon that", p. 20 | NOT FOUND | NOT FOUND | act **upon** | MATCHES (optional) | "Acting upon it" |
| 1.7 | trace | "Calling" | "To invite others to that", p. 15 | "Calling to that", p. 20 | "those who call to it" (Ibn al-Qayyim, different passage), https://abuiyaad.com/a/ibn-al-qayyim-ahl-al-sunnah-strangers | NOT FOUND | calling (HS, AI) / inviting (AK) | MATCHES | keep |
| 1.8 | match / bank | "Calling others to it" | "invite others to that", p. 15 | "Calling to that", p. 20 | as 1.7 | NOT FOUND | calling to it | MATCHES | keep |
| 1.9 | trace / match / bank | "Patience" | "To bear patiently the harms encountered in that path", p. 16 | "Patiently persevering and bearing any harm encountered upon that way", p. 20 | "have patience upon the harm" (Ibn al-Qayyim, different passage), same URL as 1.7 | NOT FOUND | patience **with the harm** | MATCHES for the printed word الصَّبْرُ | keep the label; in the guide/answer key add "(being patient when we are harmed for it)" |
| 1.10 | L1 footer + act 3; source line 27 | "Action is the fruit of knowledge." (al-Uthaymeen, p. 22) | NOT FOUND | al-Jabiri says the same: "Action is the fruit of knowledge", p. 25 (different scholar, same idea) | NOT FOUND | NOT FOUND | — | MATCHES (literal rendering of «والعمل في الحقيقة هو ثمرة العلم»; we only drop "في الحقيقة", "in reality") | keep; optional "Action, in truth, is the fruit of knowledge." |
| 1.11 | L1 footer (C); source line 8 | "Every believer, male and female, young and old, must learn these matters." (Ibn Baz) | NOT FOUND (same idea in AK's own introduction: "suitable for the old, the young… the male and the female", p. 6; not the same passage) | NOT FOUND | NOT FOUND | NOT FOUND | matters | NOT FOUND (terms agree) | keep |
| 1.12 | L1 version C choices | "Every believer, young and old" / "Only grown-ups" | — | — | — | NOT FOUND | — | NOT FOUND (taken from 1.11) | keep |
| 1.13 | source line 23 | "Knowledge means knowing Allah, His Prophet and Islam with proofs: 'Allah said' and 'the Messenger said', not by opinion, nor by the saying of so-and-so." | first half = matn: "knowledge of Allāh, His Prophet and the religion of Islām with the proofs", p. 14 | "knowledge of Allaah, and knowledge of His Prophet and knowledge of the religion Islam with the proofs", p. 20 | NOT FOUND | NOT FOUND | the **religion of** Islam, with **the** proofs | IMPROVE (first half); second half (Ibn Baz) NOT FOUND | "Knowledge means knowing Allah, knowing His Prophet ﷺ and knowing the religion of Islam, with the proofs: 'Allah said' and 'the Messenger said', not by opinion and not by what so-and-so said." |
| 1.14 | source line 31 | "Calling others must be with knowledge and clear insight." (al-Uthaymeen) | NOT FOUND | NOT FOUND for this passage; HS renders بصيرة in 12:108 as "sure knowledge", p. 32 | NOT FOUND | NOT FOUND | — | NOT FOUND | keep |
| 1.15 | source line 37 | "Patience in obeying Allah, patience in staying away from what He forbade, and patience with what Allah decrees." (al-Uthaymeen) | NOT FOUND | al-Jabiri gives the same three kinds: "Patience upon the obedience of Allaah… in avoiding the disobedience… with regard to the decree", p. 43 | NOT FOUND | NOT FOUND | obedience / forbidden or disobedience / decree | MATCHES | keep |

### Lesson 2: Allah created us (make_worksheet_l2.py, lesson-02-allah-created-us.md)

| # | Where | Our wording | AK (Abu Khadeejah) | HS (Hasan as-Somali / al-Jabiri) | AI (Abu Iyaad, abuiyaad.com) | AI2 (Abu Iyaad, other sites) | Agreed term | Verdict | Suggested wording (ours) |
|---|---|---|---|---|---|---|---|---|---|
| 2.1 | L2 title | "Allah Created Us" | "Allāh created us", p. 21 | "Allaah created us", p. 57 | NOT FOUND | NOT FOUND | created us | MATCHES | keep |
| 2.2 | trace / match / bank | "He created us" | as 2.1 | as 2.1 | NOT FOUND | NOT FOUND | created us | MATCHES | keep |
| 2.3 | trace / match / bank | "He provides for us" | "He provided for us", p. 21 | "provided sustenance for us", p. 57 | NOT FOUND | NOT FOUND | **provided** for us (past) | IMPROVE | "He provided for us" |
| 2.4 | match / bank; L2 footer | "He did not leave us without purpose" | "did not leave us without a purpose", p. 21 | "He did not leave us without a purpose", p. 57 | "not in vain and without purpose" (on Allah's wisdom, post by Admin), https://abuiyaad.com/a/allah-grants-wisdom | NOT FOUND | without **a** purpose | IMPROVE | "He did not leave us without a purpose" |
| 2.5 | L2 footer (A, B) | "Allah created us, provides for us, and did not leave us without purpose," | as 2.3 and 2.4 | as 2.3 and 2.4 | as 2.4 | NOT FOUND | provided / without a purpose | IMPROVE | "Allah created us, provided for us, and did not leave us without a purpose," |
| 2.6 | source line 8 (matn) | "Every Muslim, male and female, must learn three matters and act on them. The first: Allah created us, gives us our provision, and did not leave us without purpose." | "obligated upon every male and female Muslim to learn the following three affairs and act in accordance to them", p. 20 | "obligatory upon every Muslim, male and female, to learn and act upon the following three matters", p. 57 | NOT FOUND | NOT FOUND | these three matters; act upon them; provided for us; without a purpose | IMPROVE | "Every Muslim, male and female, must learn these three matters and act upon them. The first: Allah created us, provided for us, and did not leave us without a purpose." |
| 2.7 | L2 act 3 (A, B) choices | "To worship Him" / "For nothing" | "created us to worship Him", p. 21 (his matn edition) | "the purpose that Allaah created the creation", p. 58 | "for Men and Jinn to worship Him", https://abuiyaad.com/a/allah-grants-wisdom | NOT FOUND | worship | MATCHES | keep |
| 2.8 | L2 footer; source line 13 | "Allah created us to worship Him. He did not create us for nothing." (Ibn Baz: «الله خلق الخلق ليعبدوه فلم يخلقهم هملاً، ولا سداً، ولا عبثاً») | NOT FOUND (Ibn Baz) | NOT FOUND (Ibn Baz); al-Jabiri on the matn: "He did not leave them aimlessly and wastefully", p. 58 | NOT FOUND | NOT FOUND | worship; without a purpose | IMPROVE (faithfulness to the Arabic: الخلق = "the creation", three words given) | "Allah created His creation to worship Him. He did not create them without a purpose or for nothing." |
| 2.9 | source line 21 | "You did not make yourself. Your parents did not make you. You did not come by accident." (al-Uthaymeen, summary) | NOT FOUND | NOT FOUND (al-Jabiri: "brought us into existence from nothing", p. 57, different passage) | NOT FOUND | NOT FOUND | — | NOT FOUND | keep (already marked as our summary) |
| 2.10 | L2 act 3 (C) + footer; source line 27 | "We cannot live without food and drink, and Allah is the One who created our food and drink." (al-Uthaymeen) | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | — | NOT FOUND | keep; make the source file say "cannot" like the worksheet |

### Lesson 3: the three principles (make_worksheet_l3.py, lesson-03-three-questions.md)

| # | Where | Our wording | AK (Abu Khadeejah) | HS (Hasan as-Somali / al-Jabiri) | AI (Abu Iyaad, abuiyaad.com) | AI2 (Abu Iyaad, other sites) | Agreed term | Verdict | Suggested wording (ours) |
|---|---|---|---|---|---|---|---|---|---|
| 3.1 | L3 title | "My Three Roots" | "The Three Principles", p. 29 | "three principles", p. 92 | NOT FOUND | NOT FOUND | three principles | MATCHES as a child-friendly design title (the header already gives the real name) | keep; owner may prefer "My Three Principles" |
| 3.2 | trace / match | "My Lord" | "My Lord is…", p. 29 | "My Lord is Allaah", p. 93 | NOT FOUND | NOT FOUND | My Lord | MATCHES | keep |
| 3.3 | trace / match | "My Religion" | "his Religion", p. 29 | "My religion is Islam", p. 93 | NOT FOUND | NOT FOUND | my religion (capital R only in AK) | MATCHES | keep |
| 3.4 | trace / match | "My Prophet" | "his Prophet", p. 29 | "My Prophet is Muhammed", p. 93 | NOT FOUND | NOT FOUND | My Prophet | MATCHES | keep |
| 3.5 | L3 act 3 + footer; source line 12 | "These three principles gather the whole religion" (+ source: "…These are the questions a person is asked in the grave.") (Ibn Baz) | NOT FOUND for Ibn Baz; AK's intro: "the questions that a person will be asked in his grave", p. 5 | NOT FOUND for Ibn Baz; al-Jabiri: "the three questions that the servant will be asked in his grave", p. 93 | NOT FOUND | NOT FOUND | three principles; asked in his grave | MATCHES (terms) | keep |
| 3.6 | source line 7 (matn) | "If you are asked: what are the three principles every person must know? Say: that the servant knows his Lord, his religion and his Prophet Muhammad ﷺ." | "If it is said to you: 'What are the three principles that every person is obligated to know?' … to know his Lord, his Religion and his Prophet", p. 29 | "So if it is said to you: 'What are the three principles which a person must know?' … knowledge of His Lord and His religion, and His Prophet", p. 92 | NOT FOUND | NOT FOUND | three principles; must know | MATCHES | keep |
| 3.7 | source line 19 | "'Usul' means foundations: what other things are built on, like the foundation of a wall, or the root of a tree that the branches grow from." (al-Uthaymeen) | NOT FOUND | al-Jabiri gives the same definition: "Something that other things are built upon… (foundation) of a wall and… (trunk) of a tree", p. 92 | NOT FOUND | NOT FOUND | foundation; built upon | MATCHES (HS says "trunk"; we say "root", which matches Hilali-Khan 14:24, "whose root is firmly fixed") | keep |
| 3.8 | source line 23 (coloring labels) | "My Lord / My religion / My Prophet ﷺ" | as 3.2–3.4 | as 3.2–3.4 | NOT FOUND | NOT FOUND | — | MATCHES | keep |

## What Abu Iyaad's site does contain (for the record)

Searched 2026-10-17: all categories (`/c/<name>/<page>`, incl. Knowledge Base), all monthly archives
2012–2026, then full text of 238 articles for "Three Fundamental", "Thalathat/al-Uṣūl al-Thalāthah",
"four matters", "did not leave us", "without purpose", "fruit of knowledge", and the Arabic
«الأصول الثلاثة», «المسائل الأربع», «يتركنا», «ثمرة العلم», «تجمع الدين». Hits:
- https://abuiyaad.com/a/badawi-hijab: footnote 15 names "al-Uṣūl al-Thalāthah" (Arabic title, no English name).
- https://abuiyaad.com/a/allah-grants-wisdom (posted by "Admin"): "not in vain and without purpose" / "to worship Him".
- https://abuiyaad.com/a/ibn-al-qayyim-ahl-al-sunnah-strangers: "call to it and have patience upon the harm".
No other passage from Thalathat al-Usul or its explanations was found.

## Short summary

- 33 lines checked. MATCHES: 20 · IMPROVE: 8 (1.2, 1.3, 1.13, 2.3, 2.4, 2.5, 2.6, 2.8) · WRONG: 0 ·
  NOT FOUND (no trusted translation of that passage): 5 (1.11, 1.12, 1.14, 2.9, 2.10). Some MATCHES rows have
  optional wording notes.
- Shared terms to use everywhere: **the Three Fundamental Principles**, **matters** (not "things"),
  **act upon**, **provided for us**, **without a purpose**, **worship**, **My Lord / my religion / My Prophet**,
  **three principles**.
- Not reached: abukhadeejah.com, sunnahpublishing.net, authenticstatements.com, troid.org, rasheedbarbee.com
  (refused). Rasheed Barbee and Maaz Qureshi not checked. No approved English translation of Ibn Baz's or
  al-Uthaymeen's *Sharh* was available, so their sentences were checked against the Arabic only.
- No product, design or source file was changed. The owner decides which suggestions to apply.
