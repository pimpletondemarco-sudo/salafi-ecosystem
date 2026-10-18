# Design research: true/false check activity — 2026-10-18

Researcher: market-researcher. Page part: the **check activity on the "Learn" page** (tracing strip +
one check that rotates match / fill-in / true-false; owner-approved 2026-10-18). First used in Lessons 4,
7, 10 and 13 in the plan (`style-and-activity-variety-2026-10-18.md` §5); the designer may use it earlier
if the manager changes the rotation. Ages 6–10. Market and design research only: **no religious
content is written here.** Nothing here may be copied (designs, text or images).
Companion reports: `matching-2026-10-17.md`, `fill-in-2026-10-17.md`, `worksheet-layout-2026-10-17.md`.

## What I could and could not reach (read this first)

- **Reached: Etsy Open API (read-only), 2026-10-18.** Search "true or false worksheets kids printable"
  (103 results, 25 read); earlier today's 882-listing Islamic set (17 mention true/false). Images of 2
  listings viewed (4 images, scratchpad only). Reviews read for 1 listing. No sales data (favourites and
  views only). Our shop was not touched.
- **Not reachable:** Teachers Pay Teachers, Pinterest (2026-10-18). Item-writing guidance below comes from
  **web search snippets** (a university e-assessment guide and a worksheet-preparation note).
- Buyer review text about true/false pages specifically: **none found** (one 5★ one-liner).

## 1. How the market does it

| Listing (id, shop) | Favs / views | Format seen in the images |
|---|---|---|
| 2nd Grade Reading Comprehension + Sequencing + True or False (4378562337, shop 40450977), $2.90 | 42 / 1,424 — top result | Third page of each story set: **cut out sentence strips and glue them under a two-column TRUE / FALSE table**. Strips in dashed boxes at the bottom. A smiling mascot character on the listing images. |
| Ten Commandments True or False (4413013767, shop 62406062), $0.99 | 3 / 803 | 10 numbered statements, each followed by **two small circles "○ True ○ False"** in a right-hand column; instruction "Read each statement. Fill in the circles true or false." Drawn children reading at the bottom. |
| Islamic: Seerah pack "True or False" (4590459674) | — | Listed as a feature only (style report §3); made with AI per its own listing. |

Patterns:
1. Two answer styles: **mark a choice beside each statement** (circles or boxes) or **cut-and-sort into
   True/False columns**. The cut-and-sort version is really a sorting activity.
2. Statements are **numbered**, one per row, with the choices **lined up in one column on the right**.
3. True/false is sold as part of a reading or review set, rarely on its own; in Islamic shops it is rare
   (17 of 882).

Item-writing advice (web snippets, 2026-10-18, weak but consistent):
- One idea per statement; plain words; no trick questions.
- Use negatives sparingly; never double negatives.
- Absolute words ("always", "never", "all") tend to signal *false* and qualifiers ("usually") signal
  *true* — children learn the cue instead of the content, so avoid both.
- Keep the page uncluttered; a cartoon border "adds visual noise without helping learning".

## 2. The religious-content risk (most important point)

A true/false item **prints a false sentence on purpose**. On a religious page, a false sentence about
Allah, the Prophet ﷺ or the religion could stick in a child's memory, and it is still "wrong content"
on our page. So:
- **False statements test the lesson's words and order, not beliefs.** Safe kinds: a word paired with
  the wrong meaning ("دِينِي means My Lord"), a wrong number or order ("There are five matters"),
  which scholar explained the book, which matter comes first. **Never** a false statement that
  attributes something to Allah, denies something about Him, or misstates a ruling.
- Every statement, true or false, is built **only from words in the verified source file**; a false
  one is made by swapping one verified word for another verified lesson word. The owner approves each
  false statement with the religious content (CLAUDE.md).
- The **answer key gives the corrected sentence** for every false item, with its source line, so the
  parent can say the right version straight away.
- The teaching guide tells the parent to say the correct sentence aloud after each false answer.

## 3. Rules for our activity

**T1 — 3 statements on the Learn page (4 at most if space allows).** It shares the page with tracing;
allow about 3.0–3.5 in of height. Mix: for 3 items use 2 true + 1 false or 1 true + 2 false, and vary
it between lessons; never all true or all false; no pattern (not T-F-T every time).

**T2 — Statements:** ≤ 10 words for the 6–8 band (English, Nunito 18 px); one idea each; no "not",
"never", "always"; numbered with our green numbered style.

**T3 — Arabic inside a statement** goes in its own chip at the **start** of the line, not mid-sentence,
so the right-to-left word never jumps about in a left-to-right sentence: `[ دِينِي ] means My Lord.`
Noto Sans Arabic, fully voweled, ≥ 32 px; passes `check_arabic.py` (Letter and A4).

**T4 — Answer choices:** two rounded outlined boxes in one aligned column on the right, each with a
symbol and a word: **"✓ True"** and **"✗ False"**; instruction "Circle True or False." Word + symbol
works for early readers and in black and white.
- **No red/green coding** for true/false (prints grey; colour-blind children; red reads as "wrong").
- **No thumbs up/down and no smiley/sad faces** — they are drawings of hands and faces (CLAUDE.md).
- Row height ≥ 0.6 in; boxes at least 0.9 × 0.45 in so a 6-year-old can circle one cleanly.

**T5 — Instruction line (17–18 px, verb first):** "Read each sentence. Circle True or False."
Teaching guide: for children who cannot read yet, the parent reads each sentence aloud.

**T6 — Ink:** white background, outlines only; no border, no mascot, no clipart. The page's one picture
stays the single small palm (owner 2026-10-18).

## 4. Recommendations for OUR page, ranked (keep / change / add)

**Keep**
1. Learn page layout: header, tracing strip (accepted format), then this one check activity, then the
   source footer and "Answers: Answer Key, Lesson N".
2. Our numbered green circles and verb-first instructions (match and fill-in reports).

**Add**
3. **The religious-content safeguards in §2** — false items only about words, numbers and order;
   owner approval; corrected sentence + source in the answer key.
4. **Mark-beside format (T4), not cut-and-sort.** Cut-and-sort belongs to the Lesson 4 "Sort" Do page;
   using it here would repeat the hands-on activity on the Learn page.
5. Answer key: the true/false part shown filled in (circles in green with a tick), and under each false
   item "Correct: …" with the source line.

**Make 3 versions (A/B/C):**
- A: statement left, "✓ True / ✗ False" boxes right (market norm, 4413013767 layout idea, our styling).
- B: two-column chips: statements in a list, a single ✓/✗ write-in box at the end of each row
  ("Write ✓ or ✗") — less reading, more writing.
- C: "Is it true?" cards: each statement in a light-tone card with the two choices under it, 3 cards
  in a row (good when statements carry an Arabic chip).

**Do not**
6. No "two truths and a lie" or trick items for this age; no absolutes; no negatives.

## 5. Warnings: competitor patterns that break our rules (selling points for us)

- 4378562337: a smiling mascot (a ball with a face, arms and hands) on every listing image; story
  passages about animals ("The Tortoise and the Hare", "The Lion and the Mouse").
- 4413013767: drawn children on the page; religious content of another faith.
- 4590459674 (Islamic seerah pack with true/false): made with AI by its own description; camels and a
  whale in its images (style report §2e).
- None of the true/false items seen gives a source for the correct answer; ours does, in the answer key.

## Sources

Etsy Open API v3, read-only connector, accessed 2026-10-18:
- search_listings: "true or false worksheets kids printable" (103 results).
- get_listing_images + images viewed (scratchpad only): 4378562337 (3 of 5), 4413013767 (1 of 4).
- get_reviews_by_listing: 4378562337 (1 review, 5★, 2026-07-21: "Love it! Just what my kids needed.").
- Listing URLs: https://www.etsy.com/listing/4378562337 ; https://www.etsy.com/listing/4413013767 ;
  https://www.etsy.com/listing/4590459674/islamic-homeschool-bundle-3-printable
- Islamic activity counts: `research/design/style-and-activity-variety-2026-10-18.md` §3.

Web search snippets, 2026-10-18 (weak evidence; pages not opened):
- https://bristol.ac.uk/esu/media/e-learning/tutorials/writing_e-assessments/page_28.htm (negatives; absolutes as cues)
- https://www.faculty.umb.edu/hannah_sevian/G660new/documents/Notes_on_preparing_worksheets.pdf (no double negatives; one idea per item)
- Templated tips pages returned by the same search (clutter, cartoon borders) — heuristics only.
