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

**Abu Iyaad's other websites (added 2026-10-17, column "AI2"):** 26 of his other sites were reached and 23 crawled (see the
section "Abu Iyaad's other websites (2026-10-17)" below). **None of them has his English translation of
Thalathat al-Usul, or of Ibn Baz's or al-Uthaymeen's explanation of it.** He uses only the book title,
"al-Usool al-Thalaathah (the three principles)", and, in his own prose, "created them for a purpose, for
worship" and "without purpose". These agree with the terms above. **No recommendation changes.** The only
effect: all three translators now say "three principles", so "My Three Principles" is a stronger option for
the Lesson 3 title (owner's choice).

## Sources used

| Key | Translator | Work | Where read |
|---|---|---|---|
| AK | Abu Khadeejah 'Abdul-Wahid | *The Three Fundamentals of Islam and Their Proofs* (Study Guide ebook), Salafi Publications, 2nd ed. Feb 2021 | owner's PDF `research/translations/abukhadeejah-three-fundamentals-ebook-2021/Three-Fundamentals-Study-Guide-2021-Ebook-V1.4.pdf` (printed page numbers from the "PAGE n" footers) |
| HS | Hasan as-Somali | *A Gift to the Intellects in Explanation of the Three Fundamental Principles*, Shaykh 'Ubaid al-Jabiri, Salafi Publications, 1st ed. 2007 | owner's PDF `research/translations/emaanlibrary-ubayd-jabiri-three-fundamentals/Exp-Three-Fundamental-Principles-Ubaid-Al-Jaabiree.pdf` (printed page numbers; same file as emaanlibrary.com book page `/book/explanation-of-the-three-fundamental-principles-shaykh-ubaid-al-jaabiree/`) |
| AI | Abu Iyaad Amjad Rafiq | articles on abuiyaad.com | live site, 2026-10-17 (URLs per row) |
| AI2 | Abu Iyaad Amjad Rafiq | articles on his other sites (manhaj.com, aqidah.com, tawhidfirst.com and others) | live sites, 2026-10-17 (URLs per row; site list below) |
| AK-web | Abu Khadeejah 'Abdul-Wahid | *The Three Fundamentals of Islam and their Proofs*, pocket ebook, Salafi Publications, **3rd ed. Dec 2022** (ISBN 978-1-902727-47-9), and its post on abukhadeejah.com | https://abukhadeejah.com/three-fundamentals-of-islam-and-their-proofs-muhammad-ibn-abdul-wahhab-ebook-english-arabic/ (PDF linked there: `/wp-content/uploads/2022/12/Three-Principles-of-Islam-Ebook-Pocket-2022-v.1.1.pdf`), read 2026-10-17; used only to cross-check AK |

Not reached / not usable:
- sunnahpublishing.net (Maaz Qureshi), authenticstatements.com, troid.org, rasheedbarbee.com:
  connection refused from this session (tested 2026-10-17, retried after the owner widened access: still
  refused). **Rasheed Barbee and Maaz Qureshi could not be checked at all** (no PDF of theirs in
  `research/translations/`). abukhadeejah.com loads now (see "Abu Khadeejah's website" below).
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
| 1.1 | header, all worksheets | "The Three Fundamental Principles" | "the Three Fundamental Principles", p. 105 (last line of the matn); cover title "The Three Fundamentals" | title "The Three Fundamental Principles" (title page) | NOT FOUND (only the Arabic title transliterated, "al-Uṣūl al-Thalāthah", footnote 15, https://abuiyaad.com/a/badawi-hijab) | book title only: "al-Usool al-Thalaathah (the three principles)" (Abu.Iyaad, 2013, translating Shaykh Rabee), https://www.manhaj.com/manhaj/articles/iknhb-is-tazkiyah-or-graduation-required-before-one-teaches-and-gives-dawah-part-8.cfm; transliteration only, "al-Usul al-Thalaathah", in Part 12 of the same series | Three Fundamental Principles (AK, HS); Abu Iyaad glosses the title as "the three principles", which does not conflict | MATCHES | keep |
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
| 2.4 | match / bank; L2 footer | "He did not leave us without purpose" | "did not leave us without a purpose", p. 21 | "He did not leave us without a purpose", p. 57 | "not in vain and without purpose" (on Allah's wisdom, post by Admin), https://abuiyaad.com/a/allah-grants-wisdom | his own prose (not the matn): "Allaah never created men and jinn out of mere jest and play and without purpose" (Abu.Iyaad, 2011, citing Ibn al-Qayyim), https://www.aqidah.com/creed/articles/kgmbv-usamah-hasan-suhaib-hasan-darwinism-and-the-creation-of-man---part-2.cfm | without **a** purpose | IMPROVE | "He did not leave us without a purpose" |
| 2.5 | L2 footer (A, B) | "Allah created us, provides for us, and did not leave us without purpose," | as 2.3 and 2.4 | as 2.3 and 2.4 | as 2.4 | as 2.4 | provided / without a purpose | IMPROVE | "Allah created us, provided for us, and did not leave us without a purpose," |
| 2.6 | source line 8 (matn) | "Every Muslim, male and female, must learn three matters and act on them. The first: Allah created us, gives us our provision, and did not leave us without purpose." | "obligated upon every male and female Muslim to learn the following three affairs and act in accordance to them", p. 20 | "obligatory upon every Muslim, male and female, to learn and act upon the following three matters", p. 57 | NOT FOUND | NOT FOUND | these three matters; act upon them; provided for us; without a purpose | IMPROVE | "Every Muslim, male and female, must learn these three matters and act upon them. The first: Allah created us, provided for us, and did not leave us without a purpose." |
| 2.7 | L2 act 3 (A, B) choices | "To worship Him" / "For nothing" | "created us to worship Him", p. 21 (his matn edition) | "the purpose that Allaah created the creation", p. 58 | "for Men and Jinn to worship Him", https://abuiyaad.com/a/allah-grants-wisdom | "created them for a purpose, for worship" (his own prose, same article as 2.4), https://www.aqidah.com/creed/articles/kgmbv-usamah-hasan-suhaib-hasan-darwinism-and-the-creation-of-man---part-2.cfm | worship | MATCHES | keep |
| 2.8 | L2 footer; source line 13 | "Allah created us to worship Him. He did not create us for nothing." (Ibn Baz: «الله خلق الخلق ليعبدوه فلم يخلقهم هملاً، ولا سداً، ولا عبثاً») | NOT FOUND (Ibn Baz) | NOT FOUND (Ibn Baz); al-Jabiri on the matn: "He did not leave them aimlessly and wastefully", p. 58 | NOT FOUND | as 2.4 and 2.7: he says "them" (men and jinn), "for a purpose, for worship", "not … without purpose" (different passage, not Ibn Baz) | worship; without a purpose | IMPROVE (faithfulness to the Arabic: الخلق = "the creation", three words given) | "Allah created His creation to worship Him. He did not create them without a purpose or for nothing." |
| 2.9 | source line 21 | "You did not make yourself. Your parents did not make you. You did not come by accident." (al-Uthaymeen, summary) | NOT FOUND | NOT FOUND (al-Jabiri: "brought us into existence from nothing", p. 57, different passage) | NOT FOUND | NOT FOUND | — | NOT FOUND | keep (already marked as our summary) |
| 2.10 | L2 act 3 (C) + footer; source line 27 | "We cannot live without food and drink, and Allah is the One who created our food and drink." (al-Uthaymeen) | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | — | NOT FOUND | keep; make the source file say "cannot" like the worksheet |

### Lesson 3: the three principles (make_worksheet_l3.py, lesson-03-three-questions.md)

| # | Where | Our wording | AK (Abu Khadeejah) | HS (Hasan as-Somali / al-Jabiri) | AI (Abu Iyaad, abuiyaad.com) | AI2 (Abu Iyaad, other sites) | Agreed term | Verdict | Suggested wording (ours) |
|---|---|---|---|---|---|---|---|---|---|
| 3.1 | L3 title | "My Three Roots" | "The Three Principles", p. 29 | "three principles", p. 92 | NOT FOUND | "(the three principles)" as his English for the book title الأصول الثلاثة, https://www.manhaj.com/manhaj/articles/iknhb-is-tazkiyah-or-graduation-required-before-one-teaches-and-gives-dawah-part-8.cfm | three principles (all three translators: AK, HS, Abu Iyaad) | MATCHES as a child-friendly design title (the header already gives the real name) | keep, or (stronger now that all three agree) "My Three Principles"; owner decides
| 3.2 | trace / match | "My Lord" | "My Lord is…", p. 29 | "My Lord is Allaah", p. 93 | NOT FOUND | NOT FOUND | My Lord | MATCHES | keep |
| 3.3 | trace / match | "My Religion" | "his Religion", p. 29 | "My religion is Islam", p. 93 | NOT FOUND | NOT FOUND | my religion (capital R only in AK) | MATCHES | keep |
| 3.4 | trace / match | "My Prophet" | "his Prophet", p. 29 | "My Prophet is Muhammed", p. 93 | NOT FOUND | NOT FOUND | My Prophet | MATCHES | keep |
| 3.5 | L3 act 3 + footer; source line 12 | "These three principles gather the whole religion" (+ source: "…These are the questions a person is asked in the grave.") (Ibn Baz) | NOT FOUND for Ibn Baz; AK's intro: "the questions that a person will be asked in his grave", p. 5 | NOT FOUND for Ibn Baz; al-Jabiri: "the three questions that the servant will be asked in his grave", p. 93 | NOT FOUND | NOT FOUND | three principles; asked in his grave | MATCHES (terms) | keep |
| 3.6 | source line 7 (matn) | "If you are asked: what are the three principles every person must know? Say: that the servant knows his Lord, his religion and his Prophet Muhammad ﷺ." | "If it is said to you: 'What are the three principles that every person is obligated to know?' … to know his Lord, his Religion and his Prophet", p. 29 | "So if it is said to you: 'What are the three principles which a person must know?' … knowledge of His Lord and His religion, and His Prophet", p. 92 | NOT FOUND | NOT FOUND (only the book title, see 3.1) | three principles; must know | MATCHES | keep |
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

## Abu Iyaad's other websites (2026-10-17)

How: each site was tested once, then retried after the owner widened network access. Reachable sites were
crawled link by link (home, categories with paging, monthly archives, series, tags, author pages, articles),
because the sitemaps and site search are broken on several of them. The full page text was then searched for
"Three Fundamental", "three principles", "Thalathat/al-Usul al-Thalathah", "four matters/affairs",
"three matters/affairs", "did not leave us", "created us", "provided for us", "without (a) purpose",
"fruit of knowledge", "asked in the grave", "patience … harm", "acting upon", "calling to it", "male and
female", Ibn Baz / al-Uthaymeen, and the Arabic «الأصول الثلاثة», «ثلاثة الأصول», «المسائل الأربع»,
«يتركنا», «خلقنا», «ثمرة العلم», «هملا». Every hit below was read in context. Quotes are for checking only.

### Site by site

| Site | Result | Pages crawled | What was found for our passages |
|---|---|---|---|
| www.salaf.com (→ /s/) | reached | home, article list, news archive (19 items), series, tags | Nothing. Paging (`?start=`) is ignored, `/s/archives/yyyy/mm` returns 404, the sitemap has empty URLs, and the article links redirect to his other sites (wahhabis.com, kharijites.com, asharis.com, shariah.ws, aboutatheism.net). |
| www.islamagainstextremism.com | reached | 765 (all articles, categories, archives, tags, authors) | Nothing. Ibn Baz / al-Uthaymeen appear only on takfir and terrorism. One quote from Shaykh an-Najmi says "you will be asked in the grave, about your Islam and about your Prophet" (not our passage). |
| www.sunnah.tv (→ /video/) | reached | 1,304 (458 video pages) | A video series, "Explanation of the Three Principles by Shaykh 'Ubayd Al-Jabiree (English)", Parts 1–3 (`watch.cfm?v=pklfbp`, `pklnke`, `zhkbhr`). The page says it was "Translated by Abdulilaah Lahmaamee and Abu Hakeem Bilaal Davis", **not** Abu Iyaad, and it is audio/video only (YouTube embed, no transcript). Not used. |
| www.thenoblequran.com (→ /q/) | reached | home only | A JavaScript Quran-meanings app ("The Noble Qurʾān"). It exists. **Not used**: our rule prints only Hilali-Khan for ayat. |
| www.aqidah.com (→ /creed/) | reached | 392 | No Thalathat al-Usul translation. Terms only, in his own prose: "created them for a purpose, for worship" and "Allaah never created men and jinn out of mere jest and play and without purpose" (by Abu.Iyaad, 9 Jan 2011, citing Ibn al-Qayyim), https://www.aqidah.com/creed/articles/kgmbv-usamah-hasan-suhaib-hasan-darwinism-and-the-creation-of-man---part-2.cfm |
| www.tawhidfirst.com (→ /monotheism/) | reached | 213 | It has a category **"Books › The Three Principles"** (https://www.tawhidfirst.com/monotheism/categories/bu-the-three-principles.cfm), but the category is **empty** (only the sidebar shows). No translated passage. |
| www.manhaj.com (→ /manhaj/) | reached | 371 | Book title only. Abu Iyaad translates Shaykh Rabee's words as "…the books which he has studied, al-Usool al-Thalaathah (the three principles), Kitab al-Tawhid" (by Abu.Iyaad, 4 Oct 2013), https://www.manhaj.com/manhaj/articles/iknhb-is-tazkiyah-or-graduation-required-before-one-teaches-and-gives-dawah-part-8.cfm . Part 12 (al-Abbad, 6 Oct 2013) gives the title as transliteration only, "al-Usul al-Thalaathah", https://www.manhaj.com/manhaj/articles/wpvti-is-tazkiyah-or-graduation-required-before-one-teaches-and-gives-dawah-part-12.cfm |
| www.salafis.com | reached | 159 | Nothing relevant ("acting upon knowledge" appears in a passage of Ibn Taymiyyah on 'aql). |
| www.ibntaymiyyah.com | reached | 171 | Nothing relevant ("usul al-din" only). |
| www.bidah.com | reached | 142 | Nothing. |
| www.salafisounds.com | reached (rate-limited, HTTP 429 on some pages) | 5,012 + his speaker pages 1–5 | Audio only. "Explanation of the Three Fundamental Principles" series by **Abu Idrees**, **Abu Talhah Dawood Burbank**, an-Najmi's explanation by Abu Idrees, and Khalid adh-Dhafiri. **None is by Abu Iyaad**: his speaker category (https://www.salafisounds.com/category/speakers/abu-iyaad/, pages 1–5) has no Three Principles series. With no transcripts, nothing could be compared. |
| www.abovethethrone.com, www.asharis.com, www.maturidis.com, www.kharijites.com, www.takfiris.com, www.ikhwanis.com, www.wahhabis.com | reached | 268 / 681 / 132 / 98 / 184 / 196 / 151 | Nothing for our passages (creed polemics; "three questions" on asharis.com is a quiz, not the grave questions). |
| www.fatwaislam.com, www.fiqhonline.com, www.piousmuslim.com, www.prophetmuhammad.name | reached | 174 / 72 / 100 / 46 | Nothing. |
| www.madeenah.org (→ /md/) | reached | 58 | A post by "Admin" (no translator named): Shaykh Muhammad Aman al-Jami on "How have you come to know your Lord?" (https://www.madeenah.org/md/articles/ocqllcatl-fitrah-marifah-and-establishment-of-the-proof.cfm). Only a PDF link; the PDF was not read. It covers the matn's later question, not our Lesson 1–3 lines. Not used. |
| www.learnarabic.com | reached | 2,650 (stopped at the page limit) | Arabic-language site. Nothing relevant. |
| www.sahihalbukhari.com, www.sahihmuslim.com | reached (→ /sps/sbk/, /sps/smm/) | home only | Hadith collections, not translations of our passages. Not crawled further. |
| www.salafipublications.com | **blocked** (HTTP 403, Cloudflare bot challenge; retried twice) | — | — |
| www.salafibookstore.com | **blocked** (HTTP 403, Cloudflare) | — | — |
| www.islam4kids.com, aboutatheism.net | **refused** by the network (retried once after the widening) | — | — |
| sunnahpublishing.net, authenticstatements.com, troid.org (not Abu Iyaad's, for the record) | **refused** (retried) | — | — |

**Result: Abu Iyaad has no English translation of any Lesson 1–3 passage on any reachable site.** The AI2
column records only his title and term usage. It agrees with Abu Khadeejah and Hasan as-Somali, so the
"Agreed term" column changes only for 3.1 ("three principles": now all three) and gets a note on 1.1 (he
glosses the title as "the three principles"; the CLAUDE.md product name "The Three Fundamental Principles"
stays).

### Abu Khadeejah's website (abukhadeejah.com), checked against the ebook PDF

abukhadeejah.com loads now, but it rate-limits (HTTP 429/406) and then reset the connection: only 175 of
1,496 crawled URLs returned pages. What was read:
- His book post https://abukhadeejah.com/three-fundamentals-of-islam-and-their-proofs-muhammad-ibn-abdul-wahhab-ebook-english-arabic/
  repeats the same introduction as the 2021 study guide p. 5: "The four matters that are incumbent upon every
  male and female Muslim: (i) to have knowledge, (ii) to act, (iii) to invite, and (iv) to be patient in bearing the
  harm…".
- The PDF it links (pocket ebook, **3rd ed. Dec 2022**, 68 pp.) has **the same matn wording** as the 2021 study
  guide we used. Only the page numbers differ: "learn four affairs", "To act upon that knowledge", "To invite
  others to that", "To bear patiently the harms encountered in that path" (p. 16); "three affairs and act in
  accordance with them" (p. 18; the 2021 file reads "in accordance to them"); "Allāh created us to worship Him,
  He provided for us, and did not leave us without a purpose" (p. 19); "What are the three principles that every
  person is obligated to know?" (pp. 22–23); "That is the completion of the Three Fundamental Principles"
  (p. 66). So the AK column stands. The 2022 edition also has «خلقنا لعبادته», as in the edition note above.
- His reading list https://abukhadeejah.com/books-and-explanations-for-students-of-knowledge/ names the book
  "The Three Fundamental Principles (Thalāthatul-Usūl wa Adillatuhā)", which supports row 1.1.
- His PDF's terms of use allow "short extracts… precisely referenced", but no copying or reuse without his
  permission. That fits our rule: checking only, nothing pasted into products.

### Changed recommendations

None of the five main changes or the optional points changes. One option is stronger: the Lesson 3 title
**"My Three Roots" → "My Three Principles"** (optional; all three translators say "three principles"; the
header already prints "The Three Fundamental Principles").

## Short summary

- 33 lines checked. MATCHES: 20 · IMPROVE: 8 (1.2, 1.3, 1.13, 2.3, 2.4, 2.5, 2.6, 2.8) · WRONG: 0 ·
  NOT FOUND (no trusted translation of that passage): 5 (1.11, 1.12, 1.14, 2.9, 2.10). Some MATCHES rows have
  optional wording notes.
- Shared terms to use everywhere: **the Three Fundamental Principles**, **matters** (not "things"),
  **act upon**, **provided for us**, **without a purpose**, **worship**, **My Lord / my religion / My Prophet**,
  **three principles**.
- Abu Iyaad's other websites (2026-10-17): 26 reached, 23 crawled. None has his translation of our
  passages; he gives only the title "(the three principles)" and the terms "for a purpose, for worship" /
  "without purpose". No recommendation changes; "My Three Principles" becomes a stronger option for 3.1.
  abukhadeejah.com: its 2022 pocket ebook has the same wording as the 2021 PDF (page numbers differ).
- Not reached: sunnahpublishing.net, authenticstatements.com, troid.org, rasheedbarbee.com, islam4kids.com
  (refused); salafipublications.com and salafibookstore.com (HTTP 403, Cloudflare). Rasheed Barbee and Maaz
  Qureshi not checked. No approved English translation of Ibn Baz's or
  al-Uthaymeen's *Sharh* was available, so their sentences were checked against the Arabic only.
- No product, design or source file was changed. The owner decides which suggestions to apply.
