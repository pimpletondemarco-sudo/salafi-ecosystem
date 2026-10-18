# Handover for the next session (written 2026-10-18)

The manager reads this first, then CLAUDE.md, owner-preferences.md and the Manager Inbox.

## First thing to do
- Owner asked: "test the Etsy connection". The Etsy MCP server (.mcp.json, scripts/etsy-mcp.sh) should load
  now that ETSY_API_KEY and ETSY_SHARED_SECRET are set as environment variables and openapi.etsy.com /
  api.etsy.com are allowed. Check both variables exist (never print them), then run a read-only
  search_listings for "thalathat al usul" / "islamic homeschool". Shop-changing tools ask the owner first;
  delete tools are blocked (.claude/settings.json). Seller tools need a one-time OAuth sign-in (may not
  work in a cloud session; test later when listing).

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
