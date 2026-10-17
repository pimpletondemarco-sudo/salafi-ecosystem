# Design research: answer key pages — 2026-10-17

Researcher: market-researcher. Purpose: study how well-selling and established kids' workbooks lay out
answer keys for parents, before the `workbook-designer` builds ours for *The Three Fundamental
Principles* (Thalathat al-Usul for Kids), ages 6–10. Compared with our current text drafts
`products/01-usul-kids/guide/answer-key-lesson-01..03.md` (read only, not changed).
Market research only: no religious content written. Nothing here may be copied.
Companion report: `teaching-guide-2026-10-17.md`.

## What I could and could not reach (read this first)

- **Could not open:** Etsy (not tried: DataDome blocks it), Teachers Pay Teachers and Amazon (tried
  once each on 2026-10-17: WebFetch "ENOTFOUND"), Noor Art, Rainbow Resource, Memoria Press,
  All About Learning Press sample PDFs, Exodus Books, Well-Trained Mind forums, Cathy Duffy Reviews,
  Twinkl, Payhip, Gumroad, Furqaan Bookstore, Mecca Books, Seton, IslamHouse (proxy "connect_rejected"
  or ENOTFOUND). abukhadeejah.com answered its home page (HTTP 200) but refused an article page
  (HTTP 406) and later did not resolve.
- **Could open:** emaanlibrary.com (three free Islamic studies workbooks downloaded and inspected:
  A1, A2, A3) and salaf.com (redirect only, no children's material found).
- Everything else is from **WebSearch result snippets (2026-10-17)**: publisher and retailer
  descriptions and forum-thread summaries. **No full buyer review of an Islamic answer key could be
  read.** No listing is invented; where a point is a general convention rather than a sourced fact,
  it says so.

## 1. Common patterns in the market

| Pattern | What the evidence shows | Source |
|---|---|---|
| **Reduced copy of the student page with answers written in** | The classic format of established publishers. Wordly Wise: "a reduced copy of the exercise pages… answers are written in the blank spaces." Memoria Press guides for grades 3–7 reproduce student pages with answers overprinted, with teacher notes in the margins. | K1, K2 |
| **Answers-only list** | Used for the youngest grades: Memoria Press "Teacher Keys" for early grades give only the answers and do not reprint the pages. Also used for test keys and short items. Our current drafts are this type. | K2 |
| **Separate key (book or file), not mixed into the student pages** | Math Mammoth sells keys as separate books; Bookshark sells a Wordly Wise key alone. TpT/Easel guidance: the key is "often a separate page or document" in the resource folder; sellers say clearly in the description that a key is included. One (low-quality) page suggests separate PDF files so the parent can open the key on a second screen. | K3, K4, K5 |
| **Key at the back of the workbook** | Common in all-in-one workbooks (Essentials in Writing; Singapore word problems). One reviewer of a boxed programme disliked parent material at the back of each book: "constant flipping back and forth". | K6, T5 |
| **Answer colour** | Red bold answers in line with the question are a common worksheet convention; Math Mammoth prints keys "in a non-distracting color". Red can read as "wrong", and red prints as mid-grey on a black-and-white printer, so it can blend with black text (search summary; general printing fact, not a buyer review). | K3, K7 |
| **Islamic workbooks: keys are rare** | ISF *Learning Islam* teacher guide "supplies answers" to study questions (sold separately, ~$32). A Payhip *Muslim Character & Manners Workbook* (ages 8–12, ~$5.50, no ratings) advertises a "Parent & Teacher Answer Key". The three free Islamic workbooks inspected on emaanlibrary.com (A1–A3, 48–50 pages each) have **no answer key at all**; one says it is used with separate lesson plans and "the teacher will take you through this part". Etsy: only a Ramadan activity book was seen earlier to mention a key (fill-in report F4). | K8, K9, A1–A3 |
| **Sources on answer keys** | None of the Islamic keys or workbooks seen cite a scholar's book and page for an answer. A2 gives hadith as "(Narrated in Muslim)" with no number or grading. | A2 |

## 2. What parents praise and complain about

- **Praise:** parents value a key that lets them check fast without knowing the subject — the
  reason publishers sell keys and TpT buyers "expect answer keys and detailed teacher's guides" (K4).
  Reduced filled-in pages are kept by long-running publishers (Wordly Wise, Memoria Press), which
  suggests buyers accept them (K1, K2; no review text readable).
- **Complaint 1 — key does not match the workbook.** Well-Trained Mind thread on Essentials in Writing:
  workbook and key "do not match" (K6); earlier finding: keys that "do not always match the answers
  listed" (fill-in report F9). This is the most repeated complaint found.
- **Complaint 2 — flipping back and forth** to parent material at the back (T5).
- **Complaint 3 — key missing or sold separately / paywalled** (fill-in report F9; Safar workbook
  needs a separate teacher's guide, K8).
- **Islamic-specific:** reviewers question accuracy of Islamic facts on generic sheets (Twinkl pillar
  order, fill-in report F1). A key that shows *where the answer comes from* answers that worry.
- No complaint text about ink use on answer keys was found; general buyer complaints about ink-heavy
  borders are in `worksheet-layout-2026-10-17.md`.

## 3. Our drafts checked against the market

Our three drafts are answers-only lists in Markdown: per activity, the answer, a transliteration, and
for religious answers a "Source line" with book, scholar, publisher, edition and printed page, plus
the Arabic quote (internal Shamela link kept out of customer view).

- **Already ahead of the market:** a key exists at all; every religious answer has a real book and
  printed page; Arabic quote shown. No competitor seen does this.
- **Gaps:** (1) no visual link to the student page — a parent of a 6-year-old must match "Activity 3"
  to the page by reading; (2) no student page numbers; (3) Lesson 3 draft source line still has the
  year-free format right ("Dar al-Masir, 1st ed., p. 38") — keep it that way everywhere.

## 4. Recommendations for OUR answer key, ranked

**Change / add (most important first)**
1. **Reduced filled-in copy of each student page** (about 55–60% size, one or two per page) with the
   answers drawn in, because a parent can check a young child's page at a glance. Use the same
   generator and the same data as the student page, so the key can never disagree with the page
   (the top complaint, K6). Activities with no single answer (tracing, colouring) get a short
   "check that…" note instead of a filled copy.
2. **Answers in our brand green, bold, never red.** Red means "wrong" to children and turns mid-grey
   on black-and-white printers (K7). Make the green dark enough to stay clearly darker than the grey
   page copy when printed in greyscale, and add a small check mark or circle shape so the answer
   still stands out without colour.
3. **Source strip under each religious answer**, in small type, in the owner's footer style:
   "Meaning of Shaykh Ibn Baz's words: …" then *title*, scholar, publisher, edition, printed page —
   **no year**. Arabic quote in Noto Sans Arabic. Ayat only from the quran.ai output (King Fahd
   Complex text, Hilali-Khan meaning), never retyped.
4. **Page-by-page order with page pointers:** header "Answer Key · Lesson 3 · Student page 7", and on
   the student page footer "Answers: Answer Key p. X" (already recommended in the layout report).
5. **Placement: one "Answer Key & Sources" section at the back AND the same pages as a separate
   PDF file** in the download, so parents can skip printing it or open it on a phone beside the
   printed page (K3, K5; avoids the flipping complaint, T5).
6. **Low ink:** white page; the reduced student copy drawn in light grey outline with its colour
   header/footer panels turned to thin outlines; only the answers in green. One thin rounded
   header panel 0.3 in inside the edge, as on the worksheets.
7. **Label clearly "For parents"** on every key page, so a child does not mistake it for a worksheet.

**Keep**
8. Our citation content (real book + printed page) and the internal Shamela links kept out of the
   customer file.
9. Transliteration next to Arabic answers (helps non-Arabic-reading parents check).

**Listing**
10. Say "Answer key with sources for every answer" in the title area / first image — keys are rare
    in Islamic printables and none cite sources (K8, K9, A1–A3).

## 5. Warnings: competitor patterns that break our rules

- **Unsourced hadith and sayings:** A2 gives hadith as "(Narrated in Muslim)" with no number and no
  grading, and prints a saying attributed to Ali on every page footer with no source. We cite
  collection + number + grading, or drop the item.
- **Answer keys with smiley faces, stickers or character mascots** ("Great job!" faces) are common in
  general kids' printables (general observation, not from a specific listing): faces are drawings of
  living beings — not allowed. Use a plain check mark or a leaf/date-palm motif.
- **Story-character lessons** ("Zaid Learns How To Pray" in A1's contents) usually come with drawings
  of children; I did not render those pages, so this is unverified, but we never use people drawings.
- No music or bid'ah items seen in answer keys.

## Sources

Local (downloaded 2026-10-17 into the scratchpad, inspected with pdfinfo/pdftotext/pdfimages, sample
pages rendered at low resolution; not redistributed):
- A1 https://www.emaanlibrary.com/wp-content/uploads/2018/01/year-1_final.pdf (from https://www.emaanlibrary.com/book/islamic-studies-children-workbooks-1-5/), A4, 50 pp., "Teacher's Comment and Signature" box per lesson, no answer key
- A2 https://www.emaanlibrary.com/wp-content/uploads/2017/12/Learn-Islam-Level-01-Workbook.pdf (Manchester Salafi School, Level 1 Student Workbook), Letter, 50 pp., no answer key, "used in conjunction with … Lesson Plans"
- A3 https://www.emaanlibrary.com/wp-content/uploads/2018/01/year-3_final.pdf, Letter, 48 pp., no answer key

WebSearch snippets, 2026-10-17 (pages not opened):
- K1 https://books.modg.org/wordly-wise-5-answer-key ; https://www.bookshark.com/wordly-wise-book-10-answer-key-only
- K2 https://www.christianbook.com/dangerous-journey-memoria-press-teacher-guide/jessica-watson/9781615385249/pd/385249 ; https://www.christianbook.com/classical-composition-thesis-teacher-second-edition/jim-selby/9781615387946/pd/387946 ; https://cathyduffyreviews.com/homeschool-reviews-core-curricula/phonics-reading/readers-literature/readers-literature-grades-1-8/memoria-press-literature-guides
- K3 https://www.rainbowresource.com/021067.html (Math Mammoth key, "non-distracting color") ; https://www.bookshark.com/product/wordly-wise-book-6-answer-key-only
- K4 https://curvymonthly.curvyyoga.com/fetch.php/TN2dxD/702274/Easelteachers%20Pay%20Teachers%20Answer%20Key.pdf (low-quality mirror; TpT/Easel guidance) ; https://jenniferfindley.com/?p=142 ; https://www.weareteachers.com/teachers-pay-teachers-tips/
- K5 https://certtest.bart.gov/printable-worksheets-with-answer-keys (low-quality, unattributed; weak evidence)
- K6 https://forums.welltrainedmind.com/topic/691250-what-the-heck-essentials-in-writing-7so-many-errors/ ; https://forums.welltrainedmind.com/topic/395795-are-there-answer-keys-to-cwp
- K7 https://myworksheetmaker.groovehq.com/help/how-do-i-hide-the-answers-while-printing ; https://stg.hffa.com/archive-th-089/color-coded-cells-answer-key.pdf (red = incorrect in a grading scheme)
- K8 https://noorart.com/collections/all/products/learning-islam-teacher-guide-level-1 ; https://www.meccabooks.com/products/safar-islamic-studies-workbook-3
- K9 https://selar.com/7112344477 ; https://payhip.com/b/Cjb6Y (Muslim Character & Manners Workbook with Parent & Teacher Answer Key)
- T5 https://www.beyondthepage.com/reviews/i-wish-i-could-say-that-i-am-100-satisfied-with-o/ (parent overview at back, "flipping")
- Earlier reports: research/design/fill-in-2026-10-17.md (F1, F4, F9), worksheet-layout-2026-10-17.md
