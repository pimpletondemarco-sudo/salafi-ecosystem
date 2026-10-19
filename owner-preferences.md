# Owner preferences (learned from the owner's feedback)

The manager and every agent read this BEFORE making anything, so the owner doesn't have to repeat
themselves. Add a line every time the owner accepts, denies or comments. Newest first within each part.

## How work reaches the owner
- Every new page or visual: make **3 versions** (A, B, C) and post them as one set in the HQ
  (`group` + `version_label`). The owner accepts one; the HQ deletes the other two. (2026-10-17)
- Each new version of something lists the older versions it replaces (`replaces`). (2026-10-17)
- Keep only what we are going with; the owner can delete any concept. (2026-10-17)
- Citation check on a concept is ONE button, "Citation check", opening a plain table: on the page /
  Arabic / where it comes from / result. No "verified by" names on drafts. (2026-10-17)
- Ask the owner only for: religious-content approval, choosing between versions, money, publishing.
  Everything else: decide from this file and the Manager Inbox decisions. (2026-10-17)

## Covers
- Chosen: cover v4, bone/green/chocolate, scholars ribbon ("Based on the explanations of Shaykh Ibn Baz
  and Shaykh al-Uthaymeen"), date palm with three labelled roots, no sapling pot. (2026-10-16)
- Denied: crooked Arabic, stars, "misplaced and random" decoration, AI-generated look (Canva AI). (2026-10-16)
- Prefers a coloured front page over a plain one. (2026-10-16)

## Worksheets (from Lesson 3, accepted v6)
- Cut-and-glue and flap pages: every fold line is labelled 'fold'; glue areas say 'Glue piece here' and instructions use 'piece' and 'box', never 'stone'. (owner, 2026-10-18)
- NO cut-off or overlapping Arabic or vowel marks, nothing off the page: every page passes
  tools/check_arabic.py before the owner sees it. (2026-10-18)
- Tracing: bubble letters with a dashed line down the middle, hollow letter dots, grey harakat, green
  start dot; solid model word on the RIGHT, two tracing copies, a blank box to write it alone. (2026-10-17)
- Worksheet Arabic font: Noto Sans Arabic (Amiri only for the product name). (2026-10-17)
- Match: only the real pairs. No extra "left over" option (it looked like an error). (2026-10-17)
- Fill-in: two steps only: circle the right word, then write it on the line. No separate "write it"
  line. (2026-10-17)
- Footer: "Meaning of Shaykh X's words: ..." (no "(meaning)" in brackets). (2026-10-17)
- Citations customers see: title, scholar, publisher, edition, printed page. NO publication year. (2026-10-17)
- White page, colour only in rounded header/footer panels kept 0.3in inside the edge. US Letter + A4.
- Still open: whether to make the English meanings beside the tracing words small and faint.

## Answer keys (Lesson 3, accepted version A, 2026-10-18)
- Layout A: a small filled-in copy of the worksheet on the left (answers in green with ticks), the
  answers listed down the right, one source box across the bottom (Arabic + meaning + book and page).
  Use this layout for every lesson's answer key.

## Teaching guides (Lesson 3, accepted version C, 2026-10-18)
- Layout C: page 1 as numbered steps (read, teach, practise the words, play); page 2 with "If your child
  asks..." in two columns and each "From the Scholars" box with English on the left, Arabic on the right.
- Owner's reason: when children ask a question answered in a later lesson (e.g. the three questions),
  the guide says plainly that it will be answered later. Keep doing this in every lesson.

## English
- Agreed terms so far (TRANSLATION-REVIEW-2): "matters" (not "things"), "act upon it", "provided for us" (past),
  "without a purpose", "the religion of Islam ... with the proofs". (2026-10-17)
- English references: ALL the owner's trusted translators, equally, not one main one: Abu Iyaad
  (abuiyaad.com), Abu Khadeejah (abukhadeejah.com), Hasan as-Somali, Rasheed Barbee, Maaz Qureshi /
  Sunnah Publishing, and every domain the owner adds for this. Compare our English with each one that
  covers the passage; where they agree, follow their shared terms. Their sentences are for checking,
  not copied into products unless the translator gives permission. (2026-10-17, corrected same day)

## Redesign hold (owner, 2026-10-18)
- Lesson 1 and Lesson 2 worksheet picks (A/B/C) are ON HOLD. Do not build answer keys or guides from them.
- After research/design/style-and-activity-variety-2026-10-18.md is written, REDESIGN the worksheets from its
  recommendations: current 2026 style, and a different main activity mix per lesson (not the same
  tracing/match/fill-in every time). Accepted rules above (tracing format, answer key A, guide C, check_arabic) still apply.

## Pricing and listing (owner, 2026-10-18)
- First release (Lessons 1-3 + answer key + teaching guide): list at $12.99 with about 30% off at launch (~$8.99).
  Full workbook later: $16.99-$19.99. (From research/market-2026-10-18.md.)
- Listing title and 13 tags as drafted in research/market-2026-10-18.md are accepted as the starting point.

## Automation (owner, 2026-10-18)
- The manager runs on its own once a day, every morning US Eastern time (scheduled task "Daily manager run").
- Agents share work only through the repo (owner-preferences.md, NEXT-SESSION.md, research/, products/) and the
  HQ / Manager Inbox stores. Every run ends by updating NEXT-SESSION.md and pushing, so the next run sees it.
- Work reaches the main branch through a pull request the owner merges.

## Lesson structure and pictures (owner, 2026-10-18; from style-and-activity-variety-2026-10-18.md)
- APPROVED: two pages per lesson. A "Learn" page (tracing + one check activity rotating match / fill-in /
  true-false) and a "Do" page whose main hands-on activity changes every lesson (plan in the report).
- Pictures on worksheets: ONE small PALM picture only (not dates, lanterns or masjids).
- Coloring pages MAY include an ayah (owner said yes). Ayah text still only from quran.ai (ar-qpc-hafs /
  en-al-hilali-khan), checked character by character, and passes check_arabic.py.
- Each new activity type needs its own design research report before it is designed (CLAUDE.md 2c).

## Sources on pages (owner, 2026-10-19)
- Worksheets (student pages) do NOT carry the full citation at the bottom. The footer points to the guide:
  "For parents: sources and explanation are in the Teaching Guide, Lesson N."
- Teaching guide "From the Scholars" boxes give the scholar's statement TOGETHER WITH the proofs he brings for it
  from the Quran and the Sunnah: each ayah in King Fahd mushaf Arabic (quran.ai ar-qpc-hafs) with the Hilali-Khan
  meaning (en-al-hilali-khan) and surah:ayah; each hadith with collection, number and the grading from an approved
  scholar or the Shamela footnote. Only proofs the scholar himself cites in that passage, verified by citation-checker.
- Answer keys keep their source box (CLAUDE.md requires a source line for each religious answer).

## One home page (owner, 2026-10-19)
- The owner works from ONE page: the HQ (https://claude.ai/artifact/BCd54vTVJYCLqBpP1zTp1D). Tab "Needs you" shows
  version sets side by side (pick one), approvals, and questions. All agent questions go in the HQ `inbox`
  collection. The old Manager Inbox is history only.
- Every new HQ concept must have: `title` "<Set name>, version X: <short what>", `group` for version sets,
  `version_label` "Version X of N", `image` (/_blob/ id) for pages, `order`, and an `update_note` when changed.

## Never write "the book" (owner, 2026-10-19)
- On every page, answer key, guide and listing, NEVER write "the book says" or "the book's words". A reader may
  think it means the Quran. Always name the author and work, e.g. "Shaykh Muhammad ibn Abdul-Wahhab wrote in
  Thalathat al-Usul:" or "Shaykh Ibn Baz explains in his Sharh Thalathat al-Usul:". "Quran" is only ever used for the Quran.
