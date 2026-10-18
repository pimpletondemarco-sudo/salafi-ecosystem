# Design research: small palm spot illustration on worksheets — 2026-10-18

Researcher: market-researcher. Page element: the **one small palm picture** allowed on each worksheet
(owner decision 2026-10-18: "ONE small PALM picture only (not dates, lanterns or masjids)"). Applies to
every Learn and Do page, answer keys' page copies, and (enlarged, as an outline) the progress chart.
Product `products/01-usul-kids`. Design research only; no religious content. Nothing here may be copied.
Companion reports: `style-and-activity-variety-2026-10-18.md` (§2b, rec 3), `progress-chart-2026-10-18.md`.

## What I could and could not reach (read this first)

- **Reached: Etsy Open API (read-only), 2026-10-18.** Searches: "palm tree clipart hand drawn commercial
  use line art" (5 results, all read), "date palm clipart" (25 read). Licence text read in each
  listing's description; images of 2 clipart listings viewed (4 images, scratchpad only). Reviews read
  for 1 clipart shop (100 of 170). Our shop was not touched.
- Earlier today (style report §2e): spot art on 15 competitor listings viewed (64 images).
- **Not reachable:** Creative Market, TpT clipart sellers, Pinterest (not tried after the proxy failures
  today). Print line-weight guidance comes from **web search snippets** (print vendors and forums).
- I did not buy or download any clipart file.

## 1. How competitors use spot art on kids' worksheets (from the style report, 2026-10-18)

- Ages 6–10 Islamic books: mostly black-and-white line art with a colour title; spot pictures as memory
  aids beside items, or decorative corner art (lanterns, crescents, stars, clouds) (4321057693,
  4590459674, 4347953176, 1412385803).
- Buyer praise for pictures is the most repeated design compliment (41577469 review 2026-02-06;
  26116957 review 2025-02-15). Our worksheets have none (§1 of that report).
- 10 of 15 competitors viewed show people, faces, hands or animals; the clean ones use buildings,
  geometric icons or objects. A palm is allowed (CLAUDE.md) and is already our brand mark (cover v4).

## 2. Buy licensed clipart, or draw it in our SVG system?

What the clipart market offers (Etsy, 2026-10-18; licence words quoted from each listing):

| Listing (id, shop) | Favs / views, price | Style | Licence / origin | Fit for us |
|---|---|---|---|---|
| Palm Leaf Line Art (1376618952, shop 19431313) | 77 / 802, $2.00 | fine-line palm **leaves** only (no tree) | Commercial licence, but **prohibits** selling items "for use as graphic assets (… digital papers, … wall art digital downloads)"; allows "text-editable digital items" if the art is "flattened or locked". A printable PDF workbook is a digital download — **not clearly covered; needs written permission**. Materials list "human made". | Not a date palm; licence unclear |
| Date Fruit & Palm, hand-drawn SVG (1708924952, shop 32268660) | 11 / 283, $5.00 | engraving-style sketches (fronds, date bunches) | "hand-drawn, scanned… converted into digital vector files (using trace operation)"; commercial licence PDF (terms not shown in the listing) | Too detailed for a 1 in spot (see §3) |
| Date Palm Tree, vintage (265503305, shop 6428355) | 68 / 2,208, $3.00 | 1800s botanical engraving, "ink saver" | Allows products "in which your own creative changes have been applied"; not to redistribute the file | Hairline engraving; old-book look; a watermark on previews |
| 14 Date Palm Landscapes (4451188820, shop 59026126) | 4 / 398, $5.00 | watercolour scenes | "Files may be created using a blend of hand-drawn, digital painting, and **AI-enhanced** tools" | **Reject (AI)** |
| Ramadan Date Palm Botanical (4579630041, shop 63453789) | 0 / 10, $6.90 | multicolour botanical | "Native **AI-generated** source artwork" | **Reject (AI)** |
| Watercolour palm / dates sets (601284472, 613932505, 4400913987) | 148, 143, 14 favs | watercolour, painted | not read in full | Watercolour turns muddy at 1 in and costs ink |

Other evidence: a 1★ review of a clipart shop: "Very complicated file formats. Can't find half of the
promised images" (shop 19431313, 2025-10-28). Many 2026 clipart listings are AI-made and say so only in
the small print.

**Decision for the designer: draw the palm in our own SVG system.** Reasons:
1. **Licence certainty.** Our product is a digital download; several clipart licences exclude or do not
   clearly cover that. Our own drawing has no licence risk.
2. **No AI look, provably.** We know exactly how it was made; several "date palm" clipart sets are
   AI-made. CLAUDE.md bans AI-looking art.
3. **It matches the owner-chosen cover v4 palm** (bone/green/chocolate, flat, three labelled roots),
   so the spot palm is our brand mark on every page — what the style report (rec 6) asked for.
4. **Size and ink control:** an SVG we draw can be simplified for 1 in and recoloured for greyscale.
5. The engraving and watercolour styles on offer are too detailed for a spot (§3).

If the owner prefers a hand-drawn look later: buy only a set whose licence **names printable / digital
download products for resale**, whose seller states it is hand-drawn (no AI), and keep the receipt and
licence text in the repo (e.g. `research/licences/`). Ask the seller in writing when the licence is unclear.

## 3. Size, placement and line weight

**Size.** About **0.9–1.1 in tall** (23–28 mm) on US Letter, the same physical size on A4 — roughly
1–1.5% of the page area. Smaller than 0.75 in and the fronds merge into a blob in print; larger than
1.25 in and it competes with the activity (design-principles: one dominant element per page).

**Shape (simplified from the cover palm, not a new design):**
- Trunk: one slightly curved tapered shape with 3–4 ring marks.
- 7 fronds (not 15+): each a single leaf shape with at most 4–5 notches; no individual leaflets.
- Date clusters: the cover palm has two. The owner said "palm only, not dates", so the default is
  **no dates** on the spot palm; one version may keep a single small cluster so the owner can decide.
- Optional three short root lines; **no labels** at this size (Arabic would be under 20 px and fail the
  harakat check).
- No sun disc, no glow, no ground hills, no shadow.

**Line weight / colour.**
- Flat colour version (default): fronds green #456f3a, trunk in the cover's trunk brown (taken from
  `cover-A4-bone-green.html`, not a new colour); no outlines, or a 1 pt outline in ink colour. Every
  shape at least **1 mm** wide.
- Line-art version (for black-and-white pages and colouring): outline **1.25–1.5 pt**, inner details
  **≥ 0.75 pt**. Print guidance found (web snippets, 2026-10-18): lines under ~0.5 pt are at the edge of
  what prints reliably; 1 pt is a safe minimum for small artwork.
- Must read in greyscale: green and chocolate need different grey values (check by converting to grey).
- Ink: under 1% of the page.

**Placement — the same spot on every page** (recognition, as competitors repeat one frame — 4321057693):
- Never inside a glue zone, flap door, tracing box or writing line; never touching Arabic (keep 0.25 in
  clear of any Arabic so `check_arabic.py` overlap checks stay clean).
- Keep it inside the white page, not in the header/footer tone panels, unless version A below is chosen.
- On Do pages it can do a job: the stepping-stone path ends at it (Lesson 1); it stands beside the flap
  base (Lesson 2) — still the only picture.

## 4. Recommendations, ranked (keep / change / add)

**Add**
1. **One palm, drawn in our SVG system, simplified from cover v4** (§2–3), stored once as a shared SVG
   symbol (e.g. `products/01-usul-kids/design/assets/palm-spot.svg`) and placed by every page generator,
   so it is identical everywhere.
2. Two variants of the same drawing: flat colour (default) and line art (B&W pages, progress chart,
   colouring).

**Make 3 versions (A/B/C) of the placement for the owner:**
- A: inside the header panel at the far left, before the "The Three Fundamental Principles, Lesson N"
  line (header grows by 0 in; palm 0.8 in tall).
- B: top-right of the white page, just under the header panel, beside the Name/Date line.
- C: bottom-right of the activity area, just above the footer panel, near the SunnahSaplings wordmark.

**Keep**
3. Our white page, bone panels and single green accent; the palm uses only colours already in the system.

**Do not**
4. No second picture of any kind (dates, lanterns, masjids, stars, moon, clouds) on worksheets
   (owner 2026-10-18).
5. No bought watercolour or AI-made clipart; no engraving-style hairline art at spot size.

## 5. Warnings: competitor patterns that break our rules

- Spot art in competitor worksheets often includes animals and people (camel, cat, bee, children —
  style report §2e table).
- AI-made "Islamic" clipart is common and disclosed only in small print (4451188820 "AI-enhanced";
  4579630041 "AI-generated"). Some clipart scenes show camels by pyramids (4598030540) or couples
  (800328392) — never use mixed sets.

## Sources

Etsy Open API v3, read-only connector, accessed 2026-10-18:
- search_listings: "palm tree clipart hand drawn commercial use line art"; "date palm clipart".
- Licence/description text read: 1376618952, 1713668701, 1708924952, 265503305, 4451188820, 4579630041, 4501031785.
- get_listing_images + images viewed (scratchpad only): 1708924952 (3 of 10), 265503305 (1 of 2).
- get_reviews_by_shop: 19431313 (100 of 170 reviews).
- Listing URLs: https://www.etsy.com/listing/1376618952/palm-leaf-line-art-clipart-summer ;
  https://www.etsy.com/listing/1708924952 ; https://www.etsy.com/listing/265503305 ;
  https://www.etsy.com/listing/4451188820 ; https://www.etsy.com/listing/4579630041
- Competitor spot-art evidence: `research/design/style-and-activity-variety-2026-10-18.md` §2b, §2e.

Web search snippets, 2026-10-18 (weak evidence; print vendors and forums):
- https://support.fmexpressions.com/fine-details-spot-color (1 pt minimum line for spot work)
- https://theshirtboard.com/index.php/topic,12630.0.html (practitioners at 0.33–0.75 pt on small images)

Our files (read only): products/01-usul-kids/design/cover-A4-bone-green.png / .html (cover v4 palm),
lesson-03-worksheet-three-roots-a4.png; owner-preferences.md; design-principles.md; CLAUDE.md design rules.
