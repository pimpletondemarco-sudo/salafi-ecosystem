# Design research: style, trends and activity variety — 2026-10-18

Researcher: market-researcher. Owner's question: "look at designs, style etc, make sure mine is up to
date and relevant and not repetitive with activities." Product: `products/01-usul-kids` (*The Three
Fundamental Principles*, Thalathat al-Usul for Kids, ages 6–10). Market and design research only:
**no religious content is written here.** Lesson topics after Lesson 3 are a planning outline that the
source-researcher must confirm from the approved explanations; every word printed in an activity
comes only from verified source files. Nothing here may be copied (designs, text or images).
Companion reports (still valid): `tracing-`, `matching-`, `fill-in-`, `worksheet-layout-`,
`answer-key-`, `teaching-guide-2026-10-17.md`. The competitor price/keyword report is being written
separately (`research/market-2026-10-18.md`); this report does not repeat it.

## What I could and could not reach (read this first)

- **Reached: the Etsy public API (read-only)**, 2026-10-18: 9 keyword searches (983 unique listings,
  882 of them Islamic-related), `get_listing_images` for 9 listings, and shop reviews for 6 shops
  (1,000+ reviews available; ~500 read). Listing ids and shop ids are given for every point.
  The API gives favourites and views, **not sales**; I use favourites (`num_favorers`) and views as
  the popularity signal and say so. Only read tools were used; our shop (68627681) was not touched.
- **Could NOT view any listing image.** `i.etsystatic.com` is refused by the session proxy
  (`connect_rejected`, curl 403) and WebFetch cannot resolve it (ENOTFOUND). So for images I only have
  what the API returns: number of images, pixel size/aspect ratio, dominant colour (hex, saturation)
  and the seller's alt text. **I did not see the competitors' page designs** and do not describe them.
- **Web search** (2026-10-18): returned mostly vendor blogs, freelancer gigs and SEO mirror pages; no
  credible 2026 trend report for kids' printables was found. Used only as weak, labelled evidence.
- Pinterest, TpT and Amazon pages were not reachable in earlier sessions (see 2026-10-17 reports);
  not retried.

## 1. Our current pages (viewed 2026-10-18)

Viewed: `cover-A4-bone-green.png`, `lesson-01-worksheet-four-things-vA.png`,
`lesson-02-worksheet-allah-created-us-vB.png`, `lesson-03-worksheet-three-roots.png`,
`lesson-03-coloring-roots.png`; activity headings of all 7 worksheet versions read from their HTML.

| Page | Activities (in order) |
|---|---|
| L1 vA | Trace the words · Match · Fill in the missing word |
| L1 vB | Trace the words · Write the word · Fill in the missing word |
| L1 vC | Trace the words · Match · Circle the right answer |
| L2 vA | Trace the words · Match · Circle the right answer |
| L2 vB | Trace the words · Write the word · Circle the right answer |
| L2 vC | Trace the words · Match · Fill in the missing word |
| L3 (accepted) | Trace the words · Match · Fill in the missing word |
| L3 coloring | Colour the palm with three labelled roots |

Style: white page; rounded bone (#e5e1d8) header and footer panels inside the margin; green
numbered circles; Baloo 2 headings, Nunito text, Noto Sans Arabic for worksheet Arabic, Amiri for the
product name; no illustration on any worksheet; "Source for parents" footer with the real book and
printed page. Cover: bone/green/chocolate, flat date palm with three labelled roots, sunrise disc,
layered hills.

**Repetition, measured:** all 7 worksheet versions use the **same three-slot template**:
slot 1 is always tracing, slot 2 is matching or "write the word", slot 3 is fill-in or circle-the-answer.
Only 5 activity types exist across the product, all of them pen-on-paper recall at the same
difficulty. If Lessons 4–14 follow this template, a child does the same page about 14 times.
**This is the main problem the owner sensed.** The look itself is not the problem (§2).

## 2. Is our style current? — evidence from Etsy (API, 2026-10-18)

### 2a. Colour and the look of listing images
Dominant colour of the **first (thumbnail) image**, from `get_listing_images`:

| Listing (id, shop) | Created | Favs / views | Thumb colour | Saturation |
|---|---|---|---|---|
| Back to School Bundle 3–4 (4347382244, 57890470) — top general seller | 2025-08-06 | 4,227 / 97,857 | #F3F6F6 near-white | 1 |
| 99 Names of Allah Activity Book (4321057693, 55494720) | 2025-06-15 (images 2026-10) | 90 / 2,854 | #EDECE5 off-white | 3 |
| Islamic Homeschool Bundle, faceless, sourced (4576889107, 68082686) | 2026-09-17 | 0 / 1 | #F8F4EB off-white | 5 |
| Islamic Curriculum Pre-K (1526040281, 8198311) — images redone 2025 | 2023-07-18 | 193 / 5,950 | #C2CFCF grey-blue | 6 |
| Islamic Activity Book 6–9 (4347953176, 57491818) | 2025-08-07 | 68 / 2,019 | #F0E5DA pale peach | 9 |
| Little Muslim Busy Book (1439945308, 26116957) | 2023-04-04 | 1,827 / 51,232 | #14514B teal | 76 |
| Islamic Learning Binder (1413347270, 41577469) | 2023-02-28 | 354 / 9,705 | #EAC54A yellow | 69 |
| Islamic Basics Flashcards (1340155377, 38774185) | 2022-11-05 | 12 / 401 | #A250F5 purple | 68 |
| Little Islamic Busy Book (1679381264, 31821268) | 2024-03-10 | 872 / 27,975 | #B7816F clay/terracotta | 40 |

**Reading:** listings made or re-shot in 2025–26 use light, low-saturation thumbnails (saturation
1–9) with the colour inside the product; 2022–24 listings use saturated teal/yellow/purple
backgrounds. Bright full-bleed backgrounds now look like the older generation; terracotta/clay on
cream is the look our design principles already flag as the 2025–26 "AI tell".
→ **Our white pages with bone panels and one green accent are current.** Keep them.

### 2b. Illustration
- Buyer praise for pictures is the most repeated design compliment: "colorful and has many
  illustrations which lacks in many other workbooks for children" (41577469, 5★, 2026-02-06);
  "lots of engaging pictures" (26116957 on 1439945308, 5★, 2025-02-15); "Love the visual
  representation. My 6yo understood it" (41577469, 2025-03-14).
- Our worksheets have **no picture at all**. This is the one way our inside pages look less
  "kids' product" than competitors. Allowed subjects (CLAUDE.md): plants, palms, dates, roots,
  masjids, Kaaba, landscapes, moon/stars, books, lanterns, prayer mats, geometric patterns.
- A buyer asked a seller for "a faceless version… without facial features" (26116957, 2024-06-12);
  a 2026 competitor sells "Faceless design: geometric icons only — no people, animals, faces, or eyes"
  as its headline (4576889107). Demand for no-faces is real, and "faceless people" is the
  competitors' usual answer — ours (no living beings at all) goes further.

### 2c. Thumbnails and listing images (metadata only)
- Number of images: 10, 10, 8, 10, 8, 7, 10, 11 on the established listings above; the 2026
  sourced/faceless competitor has only **4** and 1 view (4576889107).
- First-image shape: landscape 4:3 or 5:4 on 5 of 9 (2800×2100, 3000×2396, 2500×2000, 2700×2025,
  939×653), square on 3 (2000², 1254²), portrait on 1. Alt text on 4321057693 shows the "what's
  inside" style: "showing 122 pages with colouring and tracing, learning pages, review and recall
  activities, progress tracking".
- Weak web evidence (vendor blogs, 2026): the first image is the search thumbnail; show the product in
  use (flat-lay, clipboard); ≥2000 px wide (insightagent.app; dynamicmockups.com; printify.com).

### 2d. Fonts and density
- Rounded display face + clean sans text is the mainstream kids' look; our Baloo 2 + Nunito is in that
  family and reads as current. One family per job is right (design-principles.md).
- Buyers praise single-subject pages: "the worksheets have just one subject matter… not a mix"
  (31821268, 5★, 2026-08-21). Our 3 activities on one topic per page is right.
- **Looks dated / avoid in 2026:** saturated full-bleed backgrounds; dashed "cut here" style page
  borders used as decoration; outlined (hollow) display titles; generic clipart sun-with-rays and
  cloud; emoji icons; many fonts on one page.
  → Our **coloring page** has three of these (dashed inner border, hollow outlined title, clipart
  cloud and sun) and uses a different header system from the worksheets. It is the one page whose
  style is behind.

## 3. Activity types in the market

Counts = how many of the 882 Islamic-related listings (9 API searches, 2026-10-18) mention the type in
title or description (keyword match; one listing can count for several types). It shows what buyers
see offered, not what sells best.

| Activity type | Listings | Age fit | Fits our rules? | What reviews say |
|---|---|---|---|---|
| Tracing | 388 | 4–8 | Yes (accepted format) | Praised as prep; "liked the spotted lines and shadow lines as each child focused on different outlines" (31821268, 2026-08-24) |
| Colouring | 353 | 3–9 | Yes, allowed subjects only | "kids LOVED coloring it" (36857332, 2026) |
| Matching | 255 | 4–9 | Yes (word↔meaning) | Common in every top book |
| Certificate | 178 | all | Yes | Standard end page |
| Tracker / checklist / progress | 170 | 5–10 | Yes | 99 Names book sells "progress checklist" (4321057693) |
| Reflection page | 151 | 7–10 | Yes (only from sources) | — |
| Maze | 128 | 4–8 | Yes (masjid/garden paths) | IftitahKa "mosque maze" tag (1439945308) |
| Flashcards / cards | 125 | 4–10 | Yes (text + objects) | Laminated, on rings, used in "centers" (31821268, 2026-08-21); "printed very well… great learning aid" (36857332) |
| Word search | 110 | 8–10 | Yes | Filler-type; mostly in Ramadan/Eid packs |
| Puzzle | 104 | 4–8 | Yes (geometric) | — |
| Cut and paste / cut-out | 102 | 4–9 | Yes | "The Basteln (crafting)… and the puzzles even more" (26116957, 2024) |
| Answer key | 77 | — | Yes (we have it) | Rare; 4347953176 sells a 5-page key |
| Quiz / circle the answer | 63 | 6–10 | Yes (accepted) | — |
| Sticker / reward / badges | 62 | 4–9 | Yes (no characters) | 4347953176 "Achievement Badges"; 4550952194 "Mission Complete badge" |
| Copywork / writing | 59 | 8–10 | Yes | — |
| Sequencing / ordering | 48 | 5–10 | Yes | Wudu ordering pages (4576889107) |
| Memory game | 48 | 5–10 | Yes | — |
| Mini-book / pocket book | 43 | 5–9 | Yes | "Print, Cut, Fold & Staple" (4524875434) |
| Fill-in-the-blank | 40 | 7–10 | Yes (accepted) | — |
| Discussion | 35 | 6–10 | Yes (guide) | "appreciate the guide to how to use each segment" (31821268, 2026-08-21) |
| Sorting | 35 | 4–9 | Yes | "Halal or Not? food-sorting" (4347953176) |
| Dot-to-dot | 29 | 4–7 | Yes (masjid, star) | — |
| Colour-by-code | 21 | 5–9 | Yes (geometric tiles) | — |
| Labelling / map | 19 | 7–10 | Yes | — |
| Word scramble | 18 | 8–10 | Yes | — |
| True / false | 17 | 7–10 | Yes (✓/✗ boxes, no hands) | Seerah pack "True or False" (4590459674) |
| Bingo | 13 | 5–10 | Yes | "This Eid… Bingo game was a favourite and so easy to set up" (36857332, 2026-06-07) |
| I spy | 13 | 4–7 | Only with objects | — |
| Spinner / wheel | 12 | 6–10 | Yes | Arabic "letters wheel matching game" (4333817300, 81 favs) |
| Crossword | 11 | 9–10 | Yes | — |
| Timeline | 7 | 8–10 | Yes | Seerah "9-Event Timeline" (4590459674) |
| Lift-the-flap | 5 | 5–9 | Yes | Rare → a gap |

**How the best-favourited Islamic products mix activities (from their own contents lists):**
- Little Muslim Busy Book (1439945308; 1,827 favs): 11 activity pages, about 9 different types
  (matching, puzzle, left/right, counting beads, maze, tracing, positions, sorting).
- Little Islamic Busy Book (1679381264; 872 favs): 35 pages = 13 activity + 8 cut-out + 13 information
  pages; 16 named activities, almost no type repeated twice in a row.
- Islamic Activity Book 6–9 (4347953176): trace & match, colour, tracker, dua cut-out cards, treasure
  map game, sorting, badges, 5-page answer key.
- 99 Names (4321057693, 122 pages): learn page + colour + trace for each Name, then **separate review
  and recall pages**, final challenge, progress checklist.
- Sellers market against sameness: "hands on and engaging rather then boring worksheets"
  (1154091941); "real learning — not just busy work" (53526508 listings).

**What parents praise / complain about in hands-on pages (reviews, Etsy API):**
- Praise: hands-on and fine-motor work ("strengthens hand muscles", 21723207, 2025; many similar);
  laminating and re-using pages (31821268, 41577469, 36857332 — very common); a lesson plan with
  "zero guess work" (31821268, 2026-08-26); games for a group (bingo, 36857332, 2026-06-07).
- Complaints: cut pieces that cover the text when stuck on ("the Velcro covers some of the graphic",
  26116957, 4★, 2025-02-28); leftover elements that are never used ("hexagon listed on every page…
  never used", 21723207, 2026-03-27 — same lesson as the owner's "no left-over option" rule);
  "I would add a black and white printer friendly version" (21723207, twice, 2026-03-27); listing
  shows colour but file is not ("I was expecting it will be color", 21723207, 2★, 2025-03-12);
  content errors noticed by parents ("shawm instead of sawm", 26116957, 2024-02-28; English letters
  that "don't align correctly to the Arabic", 36857332, 2★, 2026-08-12).
- No review found that names a specific activity as boring. "Boring worksheets" appears only in
  seller copy. Evidence for "variety matters" is therefore: how top sellers build their books, buyer
  praise for hands-on/games, and educator advice (weak web sources) — not a direct complaint.

## 4. Audit: our pages vs the market

| Keep (current and right) | Change | Add |
|---|---|---|
| White page, bone panels inside margins, one green accent | Every lesson uses the same 3-slot template | A different main activity each lesson (§5) |
| Baloo 2 / Nunito / Noto Sans Arabic | Coloring page: dashed border, hollow title, clipart cloud/sun, different header | One small allowed spot illustration per worksheet |
| 3 activities max, one topic per page | Instructions small (16 px) and grey | Hands-on pages: cut-and-glue, flap, fold mini-book, cards |
| "Source for parents" footer — nobody else has it | Only recall tasks; no game or review page | Review pages every 3 lessons + a progress "sapling" chart |
| Accepted tracing / match / fill-in / key A / guide C formats | Cover sun has a soft glow (design-principles: no glows) | Listing images: 8–10 images, 4:3 landscape thumbnail |

## 5. Proposed activity plan per lesson

**Rule for every lesson (keeps the owner's accepted formats):**
- **Page 1 "Learn" (same layout every lesson, for recognition):** header, a short *Key words* tracing
  strip (accepted tracing format, 1–4 words) and one **check activity** using an accepted format
  (match, or circle-then-write fill-in, or ✓/✗ true/false). The check alternates so two lessons in a
  row never use the same one.
- **Page 2 "Do" (changes every lesson):** one **main activity** of a different type from the lesson
  before, preferably hands-on.
- Every 3 lessons, a **Review page** (game). One **coloring page** about every 3 lessons, in the
  worksheet header system. One whole-book **"My sapling grows" progress chart**: a palm or sapling
  outline with one leaf per lesson to colour (no characters).
- Each new activity type needs its own design-research report before design (CLAUDE.md step 2c):
  sorting, sequencing, cut-and-glue build, lift-the-flap, fold mini-book, cards/memory, colour-by-code,
  maze, true/false, timeline, spinner, progress chart. I can write these next.

Topics for Lessons 4–14 follow the order of *Thalathat al-Usul* as a **planning outline only**; the
source-researcher fixes the real split and wording. The activity words always come from the
lesson's verified source file.

| Lesson (topic, outline) | Key words strip | Check activity (page 1) | Main activity (page 2) | Extra |
|---|---|---|---|---|
| 1 The four matters | Trace 4 words | Match (word ↔ meaning) | **Sequence**: cut and glue the four matters onto 4 numbered stepping stones in the book's order | Progress chart starts |
| 2 Allah created us, provided for us, not without purpose | Trace 2 words | Circle-then-write fill-in | **Lift-the-flap questions**: short questions on flaps, sourced answers under them (from al-Uthaymeen's reason proof) | Optional seed-planting record page (56:63–64 idea, owner to approve) |
| 3 The three principles (three questions) | Trace 3 words | Match | **Build the roots**: cut three labelled root pieces and glue them under a palm outline (source file idea: "foundation blocks") | Coloring page (restyled); **Review 1** (spinner or memory pairs, L1–3) |
| 4 Second matter (outline) | Trace | ✓/✗ true/false | **Sort**: cut-and-glue cards into two labelled columns, pairs given by the source | — |
| 5 Third matter (outline) | Trace | Circle-then-write fill-in | **Colour-by-answer**: geometric tile/8-point-star pattern, each answer has a colour | — |
| 6 The upright way: worship Allah alone (outline) | Trace | Match | **Fold mini-book** (one sheet → 8-page booklet) for the lesson's key sentences | **Review 2** (bingo for 2+ children, L4–6); coloring page |
| 7 First principle: knowing your Lord; His signs and creations (outline) | Trace | ✓/✗ true/false | **Label and sort**: night/day/sun/moon and heavens/earth picture cards (all allowed subjects) into "signs" and "creations" as the source groups them | — |
| 8 Kinds of worship (outline) | Trace | Circle-then-write fill-in | **Cards + memory game**: Arabic word / meaning pairs | — |
| 9 Second principle: Islam and its pillars (outline) | Trace | Match | **Build**: cut and glue labelled pillars under a roof (only if the source uses the "built upon" wording; else a labelled staircase of levels) | **Review 3** (spinner, L7–9); coloring page |
| 10 Iman (outline) | Trace | ✓/✗ true/false | **Lift-the-flap** (one flap per item) | — |
| 11 Ihsan; the questions in the hadith (outline) | Trace | Circle-then-write fill-in | **Sequence**: order the question cards as they come in the hadith | No drawing of the questioner (he appeared as a man) |
| 12 Third principle: the Prophet ﷺ, name, lineage, age (outline) | Trace | Match | **Timeline / number line**: before and after prophethood, numbers from the source | **Review 4** (memory pairs, L10–12); coloring page (Makkah landscape, no people) |
| 13 Prophethood, the call, the hijrah (outline) | Trace | ✓/✗ true/false | **Map maze**: path from Makkah to Madinah through landscape and masjids (no people, no camels) | — |
| 14 Resurrection; the messengers; final points (outline) | Trace | Circle-then-write fill-in | **Q&A flip book**: whole-book review, question on front, sourced answer inside | **Final review**, crossword/word search for 8–10 (bonus), certificate |

Check: no two neighbouring lessons share a main activity or a check activity. Over the book the child
meets 12 different main activity types, plus 4 review games, with tracing as the constant warm-up.

**Lessons 1 and 2 now (owner is holding the picks):** keep the accepted page-1 style (header, tracing,
one check) and add the page-2 main activity above, instead of choosing between the A/B/C pages that
all share the same template. Lesson 3 already accepted: add its page 2 ("Build the roots") and use the
restyled coloring page.

## 6. Recommendations, ranked (keep / change / add)

1. **Change: split each lesson into a fixed "Learn" page and a changing "Do" page** (plan in §5),
   so no two lessons in a row share a main activity. Evidence: our 7 versions use one template
   (§1); top Islamic books mix 9–16 activity types (1439945308, 1679381264, 4347953176, 2026-10-18).
2. **Add hands-on pages: cut-and-glue, lift-the-flap, fold mini-book, cards.** Design every glue
   spot so a piece never covers text (Velcro complaint, 26116957 review 2025-02-28), and use only
   pieces that are needed (hexagon complaint, 21723207 review 2026-03-27; owner's "no left-over"
   rule). Lift-the-flap is offered by only 5 of 882 Islamic listings → a visible gap.
3. **Add one small allowed spot illustration per worksheet** (palm, roots, dates, lantern, open book,
   masjid outline), line-art, low ink, same style throughout. Evidence: buyer praise for
   illustrations (41577469 review 2026-02-06; 26116957 review 2025-02-15). Licensed or hand-drawn
   only, never AI-looking (CLAUDE.md).
4. **Change: restyle the coloring page** into the worksheet system (rounded header panel, Baloo title
   solid not hollow, no dashed border, no clipart cloud/sun; keep the palm and roots). Owner question
   to ask: whether an ayah should be printed on a page children colour and may throw away (religious
   judgement — owner's call; I make no recommendation).
5. **Add review pages every 3 lessons and a "My sapling grows" progress chart.** Evidence: review /
   recall pages and progress checklists are sold as features (4321057693 alt text, 2026-10-17);
   group games praised (36857332 bingo review 2026-06-07); 170 listings offer trackers.
6. **Keep the colour system and fonts.** 2025–26 listings use light, low-saturation thumbnails
   (§2a); ours matches. Do not move to bright full-bleed or cream + terracotta.
7. **Add a black-and-white check for every hands-on page** and say "prints well in black and
   white" in the listing (requested twice, 21723207, 2026-03-27). Make sure listing mockups show the
   real colours of the file (2★ mismatch review, 21723207, 2025-03-12).
8. **Change: instructions to 17–18 px** (as in worksheet-layout report); hands-on pages need a
   numbered 1-2-3 "Cut / Fold / Glue" line with words, no hand icons.
9. **Listing images (later):** 8–10 images; first image landscape 4:3 (2700×2025) flat-lay of cover
   + 2–3 inner pages on a light neutral ground; one "what's inside" image listing the activity types;
   one image for the answer key + teaching guide; one for "every page cited". The 2026 sourced
   competitor's 4 plain images got 1 view (4576889107).
10. **Keep** the source footer, answer key A and guide C. With new activity types, the answer key needs
    a small filled-in copy of page 2 too (sorted columns glued, flaps opened).

## 7. Warnings: competitor patterns that break our rules (selling points for us)

- Prayer-position, wudu and "Let's go to Mosque" pages draw children (1439945308 buyer asked for "both
  girl and boy prayer illustrations", 2024-03); a buyer had to request a faceless version (26116957,
  2024-06-12). "Faceless" figures are still drawings of people.
- Animals: "Be Kind to Every Cat" page (4347953176); "animals by continent" (4483490182); Arabic
  alphabet books with an animal per letter (tracing report).
- Felt busy books with "finger puppets" (4361409082).
- Non-Islamic holidays in the same shops (Halloween 4396257817, Christmas 4351566448); music worksheets
  in search results (4385713742).
- Facts with no source or wrong terms ("shawm", 26116957 review; Arabic–English mismatch, 36857332
  review). Only one 2026 competitor (4576889107) lists hadith numbers — still no scholar's book and
  page, and it states it was made "with AI assistance". Most competitors disclose AI use
  (4590459674, 4518026037 "AI design software"). Our hand-checked, cited pages stay a clear difference.
- An existing competitor already sells "Islamic Basics Flashcards… tawheed… questions in the grave"
  (1340155377, shop 38774185, £2.99, 12 favs): our Lesson 3 cards must look clearly different and add
  the sources.

## Sources

Etsy Open API v3 via the read-only Etsy connector, accessed 2026-10-18 (favourites/views are Etsy's
counters on that date; no sales data):
- search_listings: "islamic kids activity book printable", "islamic worksheets kids", "muslim kids
  workbook", "islamic homeschool printable", "kids activity workbook printable homeschool",
  "islamic studies curriculum kids printable", "islamic busy book", "pillars of islam iman worksheets",
  "islamic homeschool workbook aqeedah tawheed kids" (0 results). 983 unique listings aggregated.
- get_listing_images: 1439945308, 1679381264, 1413347270, 1526040281, 4321057693, 1340155377,
  4576889107, 4347382244, 4347953176.
- get_reviews_by_listing: 1439945308 (0), 1679381264 (5), 1413347270 (0).
- get_reviews_by_shop: 26116957 (55 reviews), 31821268 (100 of 1,176), 8198311 (100 of 114),
  36857332 (100 of 1,023), 21723207 (100 of 338), 41577469 (43).
- Listing pages (URLs as returned by the API), e.g. https://www.etsy.com/listing/4576889107/islamic-homeschool-bundle-wudu-salah ;
  https://www.etsy.com/listing/1340155377/islamic-basics-flashcards-for-kids ;
  https://www.etsy.com/listing/4519572359/islamic-curriculum-checklist-progress ;
  https://www.etsy.com/listing/4590459674/islamic-homeschool-bundle-3-printable ;
  https://www.etsy.com/listing/4446519480/all-access-volume-1 ;
  https://www.etsy.com/listing/1291132532/pillars-of-faith-iman-worksheet

Not reachable (2026-10-18): i.etsystatic.com (proxy connect_rejected / ENOTFOUND) — no image viewed.

Web search, 2026-10-18 (weak evidence, vendor/blog content):
- https://www.insightagent.app/guides/etsy-listing-photos-digital-downloads
- https://dynamicmockups.com/?p=58584 ; https://printify.com/knowledge-hub/scale-your-etsy-photography-shop-with-intentional-aesthetics/
- https://vocal.media/bookclub/how-to-create-math-workbooks-for-amazon-kdp-in-2026
- https://www.rainbowresource.com/history-lapbooks-and-kits ; https://homeschoolconnections.com/homeschooling-lapbooking/ ; https://sanoma.it/articolo/spazio-primaria/lapbooks-uses
- https://careerfoundry.com/en/wp-json/wp/v2/posts/4405 ; https://admin.valsparpaint.co.uk/valspar-trade/blog-events/colour-trends-for-2025 (general 2025 colour forecasts; disagree with each other)

Our files (read only, not changed): products/01-usul-kids/design/*.png and *.html (lessons 1–3,
coloring, cover), products/01-usul-kids/sources/lesson-01..03*.md, owner-preferences.md,
design-principles.md, research/design/*-2026-10-17.md.
