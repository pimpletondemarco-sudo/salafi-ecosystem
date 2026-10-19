# Handover for the next session (written 2026-10-18)

The manager reads this first, then CLAUDE.md, owner-preferences.md and the HQ (Needs you tab: version sets, approvals, questions).

## Update 2026-10-19 (workbook-designer, Lesson 2 answer key)
- Lesson 2 answer key (layout A, one version, 2 pages: Learn A + Do C with the four flaps shown lifted open) posted in the HQ as `ak2A` (no group, order 52).
  Generator: products/01-usul-kids/design/make_answerkey_l2.py (text from guide/answer-key-lesson-02.md, rewritten for Learn A / Do C);
  key mode added to make_lesson_02_pages.learn/do_page(key=True) and pages_lib.fill_item(answer=...). Student pages unchanged (byte-identical).
  Files: design/lesson-02-answerkey{,-a4}.html, -letter.pdf / -a4.pdf, -{letter,a4}-p{1,2}.png, -letter-preview.png. All pass check_arabic.

## Update 2026-10-19 (workbook-designer)
- Lesson 1 answer key (layout A, one version, 2 pages: Learn B + Do B) posted in the HQ as `ak1A` (no group, under Approve).
  Generator: products/01-usul-kids/design/make_answerkey_l1.py (text from guide/answer-key-lesson-01.md, rewritten for Learn B / Do B);
  key mode added to pages_lib.page/trace_section/match_section and make_lesson_01_pages.learn/do_page(key=True), reusable for Lesson 2.
  Files: design/lesson-01-answerkey{,-a4}.html, -letter.pdf / -a4.pdf, -{letter,a4}-p{1,2}.png. All pass check_arabic.
- Answer-key mini copies (worksheet_lib key=True) now show the Teaching Guide footer; ak3A image updated in place.
- Owner 2026-10-19 "keep student pages simple": Do pages English only (L1 Do B pieces, L2 flaps), author lines removed (L2 Learn, L3 worksheet).
  Still has an author line: lesson-03-coloring-roots(-simple) footer "Shaykh al-Uthaymeen explains: ..." (not changed; manager to decide).
- tools/render_pages.mjs now finds playwright in /opt/node-tools like render_many.mjs.

## Etsy connection (tested 2026-10-18)
- Public tools WORK. Seller sign-in WORKED 2026-10-18 via etsy-signin.mjs (get_me -> shop 68627681; no restart needed). SunnahSaplings = shop_id 68627681,
  0 listings, 0 sales.
- Seller tools (get_me, drafts, shop edits) need sign-in. The server's own "authenticate" tool cannot work
  in a cloud session (it opens a browser on the container). Use instead:
  `node scripts/etsy-signin.mjs start` -> give the owner the link; they click Allow; the browser lands on a
  "can't connect" localhost:3003 page; they paste that full address back; then
  `node scripts/etsy-signin.mjs finish "<address>"`. Needs http://localhost:3003/callback listed under
  Callback URLs at etsy.com/developers/your-apps. Tokens live in ~/.etsy-mcp/tokens.json and are lost when
  the container is reclaimed, so expect to sign in again in a new session. After signing in, the Etsy
  server may need a restart (/mcp) to pick the tokens up.

## Waiting on the owner (in the HQ Concepts panel)
- Lesson 1/2 REDESIGN posted 2026-10-18 (workbook-designer): 4 sets of 3 versions in Concepts, pick one of each:
  l1-learn (l1learnA/B/C: trace + Match), l1-do (l1doA/B/C: cut-and-glue the four matters into numbered boxes),
  l2-learn (l2learnA/B/C: trace + circle-then-write fill-in), l2-do (l2doA/B/C: lift-the-flap questions).
  Versions differ in layout and palm placement (header / beside Name / bottom). l1learnB also shows the faint
  English tracing labels (the open question below). All 24 files (Letter + A4) pass check_arabic.py.
  Files: products/01-usul-kids/design/lesson-0{1,2}-{learn,do}-v{A,B,C}[-a4].{html,png,pdf} (Letter PDF = -letter.pdf);
  generators make_lesson_01_pages.py / make_lesson_02_pages.py, shared pages_lib.py, palm_spot.py (assets/palm-spot*.svg).
  Do pages updated per owner 2026-10-18: "fold" on every tab; "Glue piece here" / "Glue each piece in its numbered box."
  The old l1wsA/B/C and l2wsA/B/C are marked "Replaced by the redesign" (kept, not deleted; ordered last).
  Needs the owner's OK besides the picks: vowel marks on لِيَعْبُدُوهُ (l2doC only) and on the lesson words as before.
  Palm with one date cluster (assets/palm-spot-dates.svg) is available if the owner wants dates on the palm.
- Approve the Lesson 1 and Lesson 2 teaching-guide text (guide1, guide2).
- Approve the vowel marks we added to the lesson words ("Needs your OK" rows in Citation check).
- Open questions: make the English labels beside tracing words faint? Rename Lesson 3 "My Three Roots"
  to "My Three Principles"? How often should the 24/7 automation run (suggested: daily)?

## Next work once the owner picks
- Answer key (layout A) and teaching guide pages (layout C) for Lessons 1 and 2, from make_answerkey_l3.py /
  make_guide_l3.py, matching the chosen Learn and Do versions (the key needs a filled copy of BOTH pages: stones
  glued in their boxes, flaps drawn open). Run tools/check_arabic.py on every page first.
- Rendering in a fresh container: `pip install --break-system-packages fonttools uharfbuzz skia-pathops scikit-image`,
  then `node tools/render_many.mjs <abs paths>` and `python3 tools/check_arabic.py ...`
  (both default to playwright in /opt/node-tools/node_modules; PW_DIR is optional).
- Command Center dashboard was last updated 2026-10-16/17; refresh it.
