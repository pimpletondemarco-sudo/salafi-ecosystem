# Halal Etsy Business — Salafi Homeschool Printables

Shop: **SunnahSaplings** (etsy.com/shop/SunnahSaplings). Goal: $100,000 in halal income.
Business #1: digital printables (worksheets, workbooks,
coloring pages) for Muslim homeschool children, sold on Etsy.

## Non-negotiable sourcing rules

All Islamic content must come from the Quran, the authentic Sunnah, and these approved scholars only:

| Scholar | Approved source |
|---|---|
| Shaykh Abdul-Aziz Ibn Baz | binbaz.org.sa, or his books on Shamela |
| Shaykh Salih al-Fawzan | his books on Shamela (e.g. book 8600); alfawzan.af.org.sa has an expired certificate as of 2026-10-16 |
| Shaykh Muhammad ibn Salih al-Uthaymeen | binothaimeen.net, or his books on Shamela |
| Shaykh Abdul-Muhsin al-Abbad al-Badr | his books on Shamela (official site to be confirmed) |
| Shaykh Abdur-Razzaq al-Badr | al-badr.net, or his books on Shamela |
| Shaykh al-Islam Ibn Taymiyyah | his printed works via Shamela (e.g. Majmu' al-Fatawa), cited by volume/page |
| Imam Ibn al-Qayyim | his printed works via Shamela, cited by volume/page |
| Shaykh al-Islam Muhammad ibn Abdul-Wahhab | his works via Shamela (e.g. Thalathat al-Usul), approved by owner 2026-10-16 |

Base texts (matn) that these scholars explained may be used as quoted inside the approved
scholars' explanations.

- NEVER use random websites, blogs, Wikipedia, or AI memory as a source for religious content.
- Every ayah: cite surah:ayah. Every hadith: cite collection + number, and the grading given by an
  approved scholar or the Shamela page footnote. Weak/fabricated hadith are never used.
- Every scholarly point: cite book title, Shamela book_id/page (and printed page), or the exact
  scholar-website URL.
- If a source cannot be verified, the content is DROPPED, not guessed.
- On anything a customer sees (pages, answer keys, guides, listings), cite the REAL book, never
  "Shamela book N": title, scholar, publisher, edition, and PRINTED page. Known editions:
  - *Sharh Thalathat al-Usul*, Shaykh Muhammad ibn Salih al-Uthaymeen, Dar al-Thurayya, 4th ed. 1424 AH / 2004
  - *Sharh Thalathat al-Usul*, Shaykh Abdul-Aziz Ibn Baz, Dar al-Masir, 1st ed. 1418 AH / 1997
  Shamela IDs and page links stay in the internal source files so the checker can re-verify.
- English renderings of Arabic are marked as "meaning" (not a literal translation of the Quran).
- Quran text on pages: the King Fahd Complex (Madinah) mushaf. English meanings of ayat: The Noble
  Quran (Hilali-Khan) only. Never print ayat from the scholars' book transcriptions.
- Final religious content is approved by the owner / a trusted student of knowledge before sale.

## Design rules

- NO drawings of living beings with souls (people, animals, birds, faces) — following the
  position of Shaykh Ibn Baz, Shaykh al-Uthaymeen, and Shaykh al-Fawzan.
  Allowed: plants, trees, dates, fruit, masjids, the Kaaba, landscapes, stars/moon, geometric
  patterns, Arabic calligraphy, objects (books, lanterns, prayer mats).
- Mockups and listing photos: only templates with no people, hands, or animals (flat-lays, desks,
  clipboards, frames).
- No music references, no celebrations of bid'ah (e.g. mawlid), no non-Islamic holidays.
- NO AI-generated-looking art (owner rejected Canva AI covers). Use designer-made Canva templates
  the owner picks, or licensed hand-drawn clipart with a commercial-use licence.
- Ayat are NEVER typed by hand into any design tool: copy them programmatically from the quran.ai
  connector output, and check every character after placing them.
- Modest, clean, child-friendly style. Arabic text fully voweled (with harakat) for children.
- Print format: US Letter AND A4 versions, high-resolution PDF.

## Product 1

English name: **The Three Fundamental Principles** (subtitle "Thalathat al-Usul for Kids"), Arabic
الأُصُولُ الثَّلَاثَةُ. Use this exact name on covers, pages and listings (it is the name buyers search).

## What every workbook includes

1. Student pages (lessons, activities, coloring).
2. **Answer key for parents**: every activity's answers, page by page, with the source line for
   each religious answer.
3. **Teaching guide** written so ANY adult can teach it, even with no Arabic or Islamic study:
   per lesson, a goal, a 2-minute plain-English background, a script of what to say, how to
   pronounce key Arabic words (simple transliteration), common child questions with sourced
   answers, and a review game. Every point comes from the lesson's verified sources only.

## Workflow

0. `manager` runs first each session: reads the owner's answers and standing decisions in the
   Manager Inbox (https://claude.ai/artifact/VNuDQRmwG98fFFieuzoF5G), assigns work, and asks the
   owner when unsure. It may approve layouts; religious content always goes to the owner.
   `market-researcher` studies what sells, competitors and prices → `research/`.
1. `source-researcher` agent gathers content → `products/<id>/sources/*.md` (with citations).
2. `citation-checker` agent re-verifies every citation against Shamela / the scholar's site.
3. `workbook-designer` agent builds the PDF/Canva pages from verified sources only.
4. Owner review → Etsy listing (title, tags, description, mockups).

## Command Center dashboard

https://claude.ai/artifact/6WtLBQMe6KkiQefsA8yzXo — after every work session, update its
agents, pipeline, income and activity files (upload new JSON asset, then update the dataset's
`url`, `name`, `updated`).

## Salafi Ecosystem HQ (animated office)

https://claude.ai/artifact/BCd54vTVJYCLqBpP1zTp1D — robots move and work according to each
agent's `status` in its store. Every agent sets its own status to "working" at the start of a task
and back to "ready"/"idle" when done, and adds one `log` entry. Robots are faceless by design.

## Tools

- Shamela connector (claude.ai custom connector) — primary research tool.
- quran.ai connector (quran.com data) — the ONLY source for printed ayat: Arabic edition
  `ar-qpc-hafs` (King Fahd Complex text) and English edition `en-al-hilali-khan`. Call
  fetch_grounding_rules first. Never type ayat from memory or from book transcriptions.
- Canva connector — the MAIN design tool (owner's choice for quality): covers, workbook pages,
  Etsy mockups. Check every Canva result for people, hands, faces or animals and remove them before
  showing it. Code-built HTML/SVG pages are only a fallback.
- PDF skill — final printable PDFs.
