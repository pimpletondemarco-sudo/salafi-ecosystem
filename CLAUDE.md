# Halal Etsy Business — Salafi Homeschool Printables

Goal: $100,000 in halal income. Business #1: digital printables (worksheets, workbooks,
coloring pages) for Muslim homeschool children, sold on Etsy.

## Non-negotiable sourcing rules

All Islamic content must come from the Quran, the authentic Sunnah, and these approved scholars only:

| Scholar | Approved source |
|---|---|
| Shaykh Abdul-Aziz Ibn Baz | binbaz.org.sa, or his books on Shamela |
| Shaykh Salih al-Fawzan | alfawzan.af.org.sa, or his books on Shamela |
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
- English renderings of Arabic are marked as "meaning" (not a literal translation of the Quran).
- Final religious content is approved by the owner / a trusted student of knowledge before sale.

## Design rules

- NO drawings of living beings with souls (people, animals, birds, faces) — following the
  position of Shaykh Ibn Baz, Shaykh al-Uthaymeen, and Shaykh al-Fawzan.
  Allowed: plants, trees, dates, fruit, masjids, the Kaaba, landscapes, stars/moon, geometric
  patterns, Arabic calligraphy, objects (books, lanterns, prayer mats).
- No music references, no celebrations of bid'ah (e.g. mawlid), no non-Islamic holidays.
- Modest, clean, child-friendly style. Arabic text fully voweled (with harakat) for children.
- Print format: US Letter AND A4 versions, high-resolution PDF.

## Workflow

1. `source-researcher` agent gathers content → `products/<id>/sources/*.md` (with citations).
2. `citation-checker` agent re-verifies every citation against Shamela / the scholar's site.
3. `workbook-designer` agent builds the PDF/Canva pages from verified sources only.
4. Owner review → Etsy listing (title, tags, description, mockups).

## Command Center dashboard

https://claude.ai/artifact/6WtLBQMe6KkiQefsA8yzXo — after every work session, update its
agents, pipeline, income and activity files (upload new JSON asset, then update the dataset's
`url`, `name`, `updated`).

## Tools

- Shamela connector (claude.ai custom connector) — primary research tool.
- Canva connector — layouts, covers, Etsy mockups.
- PDF skill — final printable PDFs.
