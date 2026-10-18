# Handover for the next session (written 2026-10-18)

The manager reads this first, then CLAUDE.md, owner-preferences.md and the Manager Inbox.

## Etsy connection (tested 2026-10-18)
- Public tools WORK (keys set; search_listings and find_shops OK). SunnahSaplings = shop_id 68627681,
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
- Lesson 1 worksheet: pick version A, B or C (l1wsA/B/C).
- Lesson 2 worksheet: pick version A, B or C (l2wsA/B/C).
- Approve the Lesson 1 and Lesson 2 teaching-guide text (guide1, guide2).
- Approve the vowel marks we added to the lesson words ("Needs your OK" rows in Citation check).
- Open questions: make the English labels beside tracing words faint? Rename Lesson 3 "My Three Roots"
  to "My Three Principles"? How often should the 24/7 automation run (suggested: daily)?

## Next work once the owner picks
- Answer key (layout A) and teaching guide pages (layout C) for Lessons 1 and 2, from make_answerkey_l3.py /
  make_guide_l3.py, matching the chosen worksheet versions. Run tools/check_arabic.py on every page first.
- Command Center dashboard was last updated 2026-10-16/17; refresh it.
