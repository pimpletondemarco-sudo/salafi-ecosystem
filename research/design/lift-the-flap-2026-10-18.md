# Design research: lift-the-flap page — 2026-10-18

Researcher: market-researcher. Page: Lesson 2 "Do" page — short question flaps; the child lifts each
flap to find the sourced answer underneath (plan: `style-and-activity-variety-2026-10-18.md` §5).
Also used later for Lesson 10. Product `products/01-usul-kids`, ages 6–10. Market and design research
only: **no religious content is written here.** Questions and answers come only from the verified
Lesson 2 source file. Nothing here may be copied (designs, text or images).
Companion reports: `sequence-cut-and-glue-2026-10-18.md` (same cutting rules),
`worksheet-layout-2026-10-17.md`, `palm-spot-illustration-2026-10-18.md`.

## What I could and could not reach (read this first)

- **Reached: Etsy Open API (read-only), 2026-10-18.** Searches: "lift the flap printable worksheet"
  (91 results, 25 read), "islamic lift the flap" (6, all read), "interactive notebook flaps printable
  homeschool" (2). Images of 2 flap listings viewed (14 images, 570 px, scratchpad only, not in repo).
  Favourites and views only; **no sales data**. Our shop was not touched.
- **Not reachable:** Teachers Pay Teachers, Pinterest, biblefunforkids.com (fetch failed, 2026-10-18).
  How-to points from teacher blogs come from **web search snippets** and are labelled.
- No Etsy review text about a flap page was found (the two flap listings have no reviews).

## 1. The market

- **Islamic printable lift-the-flap is nearly empty.** "islamic lift the flap" returns 6 listings, and
  5 of them are physical board books (e.g. 1727502212, 56 favs; 4432932748, 22 favs). The only printable
  is **My First Wudu lift-the-flap (4587226715, shop 64334634), $3.99, created 2026-10-02, 0 favs /
  3 views.** The style report counted 5 of 882 Islamic listings mentioning flaps. → still a clear gap.
- General flap printables are mostly preschool crafts at $2.50–$3.50 (shop 67868218 animal habitats,
  shop 63378902 opposites). The most-favourited in the search was **Creation Lift-a-Flap (4541130691,
  shop 18715911), $5.95, 9 favs / 309 views.**

What the two viewed listings do (descriptions only, not to be copied):

| | Creation Lift-a-Flap (4541130691) | My First Wudu (4587226715) |
|---|---|---|
| Build | Two parts: a base page with a **grey strip marked "GLUE"** down the middle, and a stack of horizontal tabs that open one by one | 9 question cards + 9 answer flaps on separate pages; 21 pages in all |
| Flap action | Tabs hinge on one edge, stacked like a flip book | "Cut around the dotted flap lines, leaving the top edge attached. Fold each flap upward along its top edge. Ask the question, then lift the flap to see the answer" |
| Versions | Full colour **and black-and-white** for colouring; a blank template | A4 and US Letter; "cardstock makes the flaps sturdier" |
| Listing images | 10: flat renders on a wood background, one partly opened render, "pages included" grid | 7: AI-looking rendered cards, **a real hand lifting a flap**, icon row ("9 step cards", "A4 & US Letter") |
| Rule problems | Drawn people and animals on the flaps (Christian content) | **Cartoon boy with full face on all 18 cards**; hands in photos |

Teacher how-to advice (web snippets, weak evidence, 2026-10-18): glue the tab **before** cutting the
flaps; put glue dots on the tab only — gluing the whole back makes the page heavy and wrinkled and can
pin the flap shut; standard copy paper can be thin enough that marker or print shows through a flap;
keep content short on each flap.

## 2. The key design problem: printing on one sheet

A flap that is **folded over** another part of the same sheet shows its **back** (blank) side, so a
printed question would need double-sided printing. Home printers and parents get this wrong, and the
owner wants simple home printing. **So our flaps must be cut out and glued on, printed side up**,
like 4541130691's separate flap strip — but both parts fit on **one single-sided sheet**:

```
 ┌──────────── header panel ─────────────┐
 │ 1 Cut  2 Fold  3 Glue  4 Lift (words)  │
 │                                        │
 │  [glue strip][glue strip][glue strip]  │  ← base: grey tabs, answers below
 │  ┌ answer ┐  ┌ answer ┐  ┌ answer ┐    │
 │  └────────┘  └────────┘  └────────┘    │
 │                                (palm)  │
 │ ✂─────────────────────────────────────  │  ← one long cut frees the strip
 │  ┌ tab  ┬ tab  ┬ tab  ┐  (shared edges) │
 │  │  ?   │  ?   │  ?   │  question doors │
 │  └──────┴──────┴──────┘                 │
 └──────────── footer panel ─────────────┘
```

## 3. Rules for our page

**F1 — One sheet, single-sided, US Letter and A4.** Base on the upper half, flap strip on the lower half,
separated by one long cut line and ≥ 0.6 in of white space.

**F2 — Flap = tab + door.** Each flap is a straight-sided rectangle: a 0.45 in **tab** on top (light grey
tone, word "glue") and a **door** below it carrying the question. The fold line between tab and door is
a short-dash line 1 pt (functional, labelled "fold" once); pre-fold before gluing.
- Size for 3 flaps (Letter): door 2.3 in wide × 2.2 in tall + tab 0.45 in → flap 2.3 × 2.65 in; three
  side by side sharing edges = 6.9 in (fits Letter 7.5 in and A4 7.27 in live width).
- For 4 flaps: a 2 × 2 grid, door 3.2 × 1.8 in.
- Number of flaps = number of verified questions in the source. **No blank or spare flap** (owner's
  no-left-over rule; hexagon complaint 21723207, 2026-03-27).

**F3 — Base: the answer never peeks out and is never covered by glue.**
- Above each answer box, a grey **glue strip** exactly the size of the tab (0.45 × 2.3 in), so the child
  sees where the tab goes.
- The answer box is at least **0.25 in smaller than the door on every side** (answer window about
  1.8 × 1.7 in under a 2.3 × 2.2 in door), so a crooked glue job still hides it.
- Nothing printed under the glue strip; answer text starts ≥ 0.15 in below it.

**F4 — Stop show-through.** On ordinary 20 lb paper, dark text under a flap can show through. Give each
door's printed face a light solid tone (bone #e5e1d8 or a 20% green tint) behind the question; keep
answer text in normal ink, not extra bold. Test: print, close the flap, hold to a window. Suggest
cardstock in the teaching guide, as 4587226715 does, but the page must work on plain paper.

**F5 — Cutting for ages 6–10** (as in the sequence report): straight lines only, solid 2 pt dark-grey cut
lines, flaps sharing edges so the child makes one long cut plus 2 short cuts; 0.15 in safe zone inside
every piece for Arabic and harakat; a small scissors icon (object) on the long cut line. No rounded
corners, no curved doors.

**F6 — Content on the flaps.** Question on the door: English, 16–18 px, ≤ 12 words, with a large "?" or
the question number in a green circle. Answer under the flap: the key Arabic word fully voweled
(Noto Sans Arabic, ~34–40 px) + a short English meaning + "Answer from: Shaykh X" if the source line
fits; otherwise the source line goes in the page footer and in the answer key. All Arabic passes
`check_arabic.py` (Letter and A4). The ayah or reason-proof wording used for answers is the owner's
approved text only.

**F7 — Instructions, numbered, words not icons (no hand icons):** "1 Cut off the flap strip. 2 Cut the
3 flaps apart. 3 Fold each grey tab. 4 Glue the tab on its grey strip. 5 Read the question, then lift
the flap." Teaching-guide tip from the snippets: glue dots on the tab only.

**F8 — Ink.** White page; tone only on tabs, glue strips and doors (≈ 12–15% of the page); check in
greyscale. One small palm picture only, in the space beside the base (owner 2026-10-18).

## 4. Recommendations for OUR page, ranked (keep / change / add)

**Keep**
1. Header/footer system, fonts, "Source for parents" footer, "Answers: Answer Key, Lesson 2".

**Add**
2. **Glue-on flap strip on the same sheet (F1–F3).** This solves the one-sheet problem without
   double-sided printing and is not offered by any Islamic printable seen.
3. **Show-through tone on doors (F4).**
4. Answer key: a small copy of the page with flaps drawn open (answers visible, in green) and the source
   line under each answer (answer key A, owner 2026-10-18).
5. **Listing images (later):** one flat render of the page; one flat render with one flap drawn open
   (a simple rendered fold with a soft edge shadow is acceptable here because it shows the action — not
   a decorative shadow); one "what's inside" image. **No hands**: 4587226715 shows a hand lifting the
   flap; we show the flap already open instead. A short listing video, if wanted, must also have no hands
   (e.g. stop-motion of the flap opening).

**Make 3 versions (A/B/C):**
- A: 3 flaps in a row, tabs on top (doors lift up) — matches 4587226715's "fold upward" action children
  expect.
- B: 3 flaps stacked in one column, tabs on the left (doors open like a book), base on the left half,
  strip on the right half.
- C: 2 × 2 grid (for a 4-question lesson such as Lesson 10), tabs on top.

**Do not**
6. No fold-over-the-same-sheet design (needs double-sided printing).
7. No faces, characters or hands on flaps, icons or mockups.

## 5. Warnings: competitor patterns that break our rules (selling points for us)

- 4587226715 (the only Islamic printable flap): a cartoon boy with full face on every card, glossy
  AI-looking render, a real hand in the photos, and a disclaimer that steps "can vary between schools of
  thought" with no source. We give the question, the answer and the scholar's book and page.
- 4541130691: drawn people ("man and animals" panel), fish and birds — and religious content of another faith.
- Board books in the Islamic search (4507880271) use animal characters ("a chick is put on a mission").
- General flap crafts are mostly animals (shop 67868218: farm, ocean, forest, beehive, fox).

## Sources

Etsy Open API v3, read-only connector, accessed 2026-10-18 (favourites/views = Etsy counters that day):
- search_listings: "lift the flap printable worksheet"; "islamic lift the flap"; "interactive notebook
  flaps printable homeschool".
- get_listing_images + images viewed (scratchpad only): 4587226715 (4 of 7), 4541130691 (4 of 10).
- Listing URLs: https://www.etsy.com/listing/4587226715/lift-the-flap-wudu-activity-printable ;
  https://www.etsy.com/listing/4541130691 ; https://www.etsy.com/listing/1727502212/sensory-5-pillars-of-islam-board-book ;
  https://www.etsy.com/listing/4507880271/where-is-the-imam ; https://www.etsy.com/listing/4432932748/my-salah-lift-the-flap-book ;
  https://www.etsy.com/listing/1159580987/multiplication-flaps-interactive
- Earlier review evidence (shop 21723207): `research/design/style-and-activity-variety-2026-10-18.md` §3.

Web search snippets, 2026-10-18 (weak evidence; pages not opened):
- https://mathequalslove.net/?p=5959 (glue on edges only; glue can pin a pocket shut)
- https://deannajump.com/interactive-reading-journals-and/ (glue the tab before cutting the flaps)
- https://www.tes.com/teaching-resource/lift-the-flap-books-7079632 (fold-over flap method)
- https://www.biblefunforkids.com/2024/02/through-roof-lift-flap.html (leave top tabs attached; cardstock)
- https://smallblueprinter.com/lifeofabee/resources.html (flap halves glued over a picture)
- Paper weight / show-through claim: templated pages found by the search "interactive notebook flaps how to
  fold glue tab template tips teachers" (low quality; treat as a hint, test by printing).
