"""Checks every Arabic text on a rendered page for cut-off or overlapping letters and vowel marks.

Owner rule (2026-10-18): no Arabic or harakat may be cut off or overlap anything; every page passes this
check before it goes to the owner. Usage: python3 check_arabic.py page.html [page2.html ...] (A4 pages
must end in -a4.html). Exit code 1 if anything fails.
  CUT     ink that would print with clipping turned off is missing (cut by a box), or ink leaves the page
  OVERLAP the Arabic's ink touches other dark ink (text, not light lines or panels)
  OFFPAGE any part of the page (e.g. the footer) runs past the paper edge
"""
import json, subprocess, sys, tempfile, os
from pathlib import Path
import numpy as np
from PIL import Image

HERE = Path(__file__).parent
DARK = 165          # luminance below this counts as ink (text); light rules/panels are ignored

def ink(path, level=DARK):
    a = np.asarray(Image.open(path).convert("L"), dtype=np.int16)
    return a < level

def dilate(m, r=2):
    out = m.copy()
    for dy in range(-r, r + 1):
        for dx in range(-r, r + 1):
            out |= np.roll(np.roll(m, dy, 0), dx, 1)
    return out

def check(html):
    size = "a4" if html.endswith("-a4.html") else "letter"
    with tempfile.TemporaryDirectory() as td:
        subprocess.run(["node", str(HERE / "arabic_snap.mjs"), str(Path(html).resolve()), td, size], check=True,
                       stdout=subprocess.DEVNULL)
        idx = json.load(open(f"{td}/index.json"))
        pg = idx["page"]; problems = []
        for o in idx.get("overflow", [])[:5]:
            problems.append(("OFFPAGE", {"text": o["text"] or o["tag"], "y": 0}, f"page {o['page']}: <{o['tag']}> runs {o['by']}px past the page edge"))
        for e in idx["els"]:
            solo, free = (ink(f"{td}/{e['i']}-{m}.png", 205) for m in ("solo", "free"))  # 205: include grey vowel marks
            others = ink(f"{td}/{e['i']}-others.png")
            n = int(free.sum())
            if n == 0:
                continue
            lost = int((free & ~dilate(solo, 1)).sum())
            if lost > max(6, n * 0.004):
                problems.append(("CUT", e, f"{lost} ink pixels clipped"))
            # ink outside the page
            ys, xs = np.nonzero(free)
            c = e["clip"]
            top = c["y"] + ys.min() / 2; bot = c["y"] + ys.max() / 2
            left = c["x"] + xs.min() / 2; right = c["x"] + xs.max() / 2
            g = e.get("pg", pg)
            if top < g["y"] or bot > g["y"] + g["h"] or left < g["x"] or right > g["x"] + g["w"]:
                problems.append(("CUT", e, "ink runs off the page"))
            hit = int((dilate(solo, 1) & others).sum())
            if hit > 8:
                problems.append(("OVERLAP", e, f"{hit} pixels touch other text"))
        return problems

if __name__ == "__main__":
    bad = 0
    for h in sys.argv[1:]:
        probs = check(h)
        print(("FAIL " if probs else "ok   ") + os.path.basename(h))
        for kind, e, why in probs:
            bad += 1
            print(f"   {kind:8} «{e['text']}» at y={e['y']:.0f}: {why}")
    sys.exit(1 if bad else 0)
