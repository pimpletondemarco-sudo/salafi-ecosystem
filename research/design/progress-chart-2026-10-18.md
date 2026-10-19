# Design research: "My sapling grows" progress chart — 2026-10-18

Researcher: market-researcher. Page: one whole-book progress chart — a palm outline with **one leaf to
colour per lesson** (plan: `style-and-activity-variety-2026-10-18.md` §5 and rec 5). Product
`products/01-usul-kids`, ages 6–10. Market and design research only: **no religious content is written
here** (lesson titles on the chart come from the verified source files). Nothing here may be copied.
Companion reports: `palm-spot-illustration-2026-10-18.md` (same palm drawing), `worksheet-layout-2026-10-17.md`.

## What I could and could not reach (read this first)

- **Reached: Etsy Open API (read-only), 2026-10-18.** Searches: "reading tracker coloring page kids
  printable" (329 results, 25 read), "islamic progress tracker kids printable" (22, all read),
  "color a leaf progress tracker tree kids printable" (0), "quran progress chart kids tree" (0).
  Images of 3 trackers viewed (6 images, scratchpad only). Reviews read for 1 listing and 1 shop.
  Favourites and views only, **no sales data**. Our shop was not touched.
- **Not reachable:** Pinterest, TpT (2026-10-18). Research on reward charts found by web search was
  low-quality templated pages with unsourced statistics; **I do not use it.**
- A "colour one leaf per lesson" tree tracker for a kids' Islamic workbook: **none found** (0 results for
  both tree searches).

## 1. The market

| Listing (id, shop) | Favs / views (2026-10-18) | How it works (from images and description) |
|---|---|---|
| Bible Reading Tracker Coloring Page (942568001, shop 19118076), $7.00, since 2021 | **614 / 13,385** — strongest tracker found | Hand-lettered line art; each book is a box of small circles, **one circle per chapter to colour**; small doodles (scroll, crown, flowers). Listing text on the image: "Color in each chapter when you finish reading it!" and "No dates, no pressure". 3 pages. |
| Juz Amma bookshelf tracker (1355400511, shop 36246273), £2.00 | 3 / 456 | 37 book spines on shelves, each labelled with a surah name, to colour when memorised; **labelled and blank versions**; flowers drawn around. |
| Juz Amma colouring tracker (4592969805, shop 67092556), $1.66, 2026-10-11 | 1 / 10 | One A4 landscape page: labelled shapes scattered over the page; "colour each labelled shape when you can recite that surah… The extra decorations can be coloured just for fun!" Mockup: flat-lay with pencils, no hands. States "Your PDF comes completely uncoloured. Coloured listing images show examples." |
| Juz Amma tracker (1776581649, shop 19005913), $7.95 | 10 / 876 | Chart / wall-art style; "approximate 5mm outer page white space margin that is often a non-printable area". |
| Islamic Studies Planner / curriculum checklist (4519572359) | 2 / 35 | Checklist tracker for a curriculum. |

Patterns:
1. **One small shape per unit, coloured when done** (circle, book spine, labelled shape). The shape is
   labelled with what was finished.
2. **Line art, low ink, uncoloured file**; the listing shows a coloured example.
3. Tone: "No dates, no pressure" — no date boxes, no deadlines.
4. A labelled version and a blank version (1355400511).
5. Kids' Islamic trackers are almost all **Qur'an memorisation** (Juz Amma). A tracker for a **study
   workbook** (lessons) is rare; a growing-palm tracker tied to the book's own symbol is not offered.

## 2. What buyers praise and complain about

- "my favorite thing is the bite-sized breakdown of each book. Other trackers just have the books
  listed… with every chapter I read, I get to color in a circle! Very satisfying!" (942568001, 5★, 2026-04-24)
- "I love the handwriting journaling doodling look" (942568001, 5★, 2026-01-18).
- "I have printed this for my children who loves seeing my quran bookshelve tracker" (shop 36246273,
  listing 1341388044, 5★, 2024-03-15) — children like a chart that matches a grown-up's.
- Complaint to avoid (other products, style report §3): listing shows colour but the file is not —
  "I was expecting it will be color" (shop 21723207, 2★, 2025-03-12). Trackers that are uncoloured say
  so plainly (4592969805).
- Owner rule (2026-10-17): nothing "left over" that looks like an error.

## 3. Rules for our chart

**P1 — Exactly one leaf per lesson in the file it ships with.** The first release has Lessons 1–3
(owner pricing decision, 2026-10-18): its chart shows a **young sapling with 3 leaves**. The full
workbook's chart has one leaf per lesson (14 in the current plan). Never ship 14 leaves with 11 that
cannot be coloured — it looks unfinished (left-over rule). Review pages: owner's choice; default is no
extra shapes (if wanted later: one date cluster per review, so they look different from lesson leaves).

**P2 — Leaves grow upward.** Lesson 1 is the lowest leaf, the last lesson the top leaf, alternating left
and right of the trunk, so colouring makes the palm "grow". Each leaf is a closed shape big enough for
crayons: at least 0.7 in across its widest part, outline 1.5–2 pt, no inner veins that split it into
tiny areas (a single centre line at 1 pt is enough).

**P3 — Label every leaf.** The lesson number in a small circle inside the leaf (Nunito 14–16 px) and,
beside the leaf or in a numbered legend down the side, the short lesson title taken from the verified
source file (English; optional fully voweled Arabic key word, which must pass `check_arabic.py`). No
dates, no stars, no score.

**P4 — Same palm as the brand.** Use the palm from our own SVG system (the cover v4 palm, owner-chosen
2026-10-16) as a **colouring outline**: trunk, fronds as leaf shapes, the three roots as on the cover
(unlabelled or labelled with the same three words as the cover only if they fit at ≥ 32 px Arabic).
Roots at the bottom give a stable base and link to Lesson 3. No sun disc, no glow, no clouds.

**P5 — Header and name.** Our rounded header panel: "My sapling grows" (or the owner's wording) and a
"Name:" line. One short instruction: "Finish a lesson, then colour its leaf." The coloured page should
be something a child is proud to pin up: leave a 1 in white margin around the palm.

**P6 — Ink and print.** Outline only, no fills (colouring page); white page; header panel tone only;
greyscale safe. US Letter + A4, inside the 0.3 in printer-safe edge (1776581649 warns about a 5 mm
non-printable margin). Portrait.

**P7 — Listing honesty.** The listing shows one coloured example **and** the plain file, and says
"Prints uncoloured, for your child to colour."

## 4. Recommendations for OUR page, ranked (keep / change / add)

**Keep**
1. Header panel, fonts and SunnahSaplings footer; no source footer is needed (no religious statement
   on this page — only lesson titles, which come from verified files).

**Add**
2. **Place it at the front of the workbook** (after the contents page) and also as its own one-page PDF
   in the download, so it can go on the fridge.
3. **One leaf per lesson, growing upward, numbered and titled (P1–P3).**
4. **Last-page link:** when every leaf is coloured, the child moves to the certificate (later page type,
   needs its own report).
5. Optional blank version (no titles) for siblings, as 1355400511 offers — owner's choice.

**Make 3 versions (A/B/C):**
- A: single tall palm centred, leaves alternating, legend of lesson titles down the left side.
- B: palm on the right, a numbered checklist of lesson titles on the left with a small leaf beside each
  title to colour as well (two places to colour; child colours both).
- C: three growth stages left to right (sapling → young palm → full palm) for the full workbook, each
  stage holding the leaves of a part of the book; for the first release, only stage one is printed.

**Do not**
6. No sticker-chart characters, smiling suns, birds or butterflies around the palm; no stars.
7. No dates, no deadlines, no scores.

## 5. Warnings: competitor patterns that break our rules (selling points for us)

- 4592969805 (Juz Amma colouring tracker): the decorations include what appears to be **a bird** among
  the shapes; planets, cakes and other doodles unrelated to the content.
- 1355399261 (same shop as 1355400511): "Rocket + Football Design" — not our style; boys/girls versions
  in other trackers (4499621634 / 4499605635).
- 942568001 is for another faith; only its mechanism (one small shape per unit) is relevant — do not copy
  its hand-lettered look or layout.

## Sources

Etsy Open API v3, read-only connector, accessed 2026-10-18:
- search_listings: "reading tracker coloring page kids printable"; "islamic progress tracker kids printable";
  "color a leaf progress tracker tree kids printable" (0); "quran progress chart kids tree" (0).
- get_listing_images + images viewed (scratchpad only): 942568001 (3 of 8), 1355400511 (2 of 3), 4592969805 (1 of 5).
- get_reviews_by_listing: 942568001 (3 reviews). get_reviews_by_shop: 36246273 (28 reviews).
- Listing URLs: https://www.etsy.com/listing/942568001 ; https://www.etsy.com/listing/1355400511 ;
  https://www.etsy.com/listing/4592969805 ; https://www.etsy.com/listing/1776581649 ;
  https://www.etsy.com/listing/4519572359/islamic-curriculum-checklist-progress
- Earlier review evidence (shop 21723207): `research/design/style-and-activity-variety-2026-10-18.md` §3.
- Owner decisions: owner-preferences.md (pricing/first release 2026-10-18; cover v4 2026-10-16; one palm picture 2026-10-18).
