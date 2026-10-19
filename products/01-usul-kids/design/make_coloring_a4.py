"""A4 versions of the Lesson 3 coloring pages, derived from the Letter HTML (the source of truth).

The Letter pages are hand-built (816x1056). A4 is 794x1123: same frame, header and footer (they are
anchored to the page edges), the picture centred across the narrower width and moved down by half the
extra height so the white space stays balanced. Run after any change to the Letter files.
"""
import re
from pathlib import Path

HERE = Path(__file__).parent
W_L, H_L, W_A, H_A = 816, 1056, 794, 1123

for stem in ["lesson-03-coloring-roots", "lesson-03-coloring-roots-simple"]:
    s = (HERE / f"{stem}.html").read_text(encoding="utf-8")
    s = s.replace("@page { size: 8.5in 11in;", "@page { size: 210mm 297mm;", 1)
    s = s.replace(f"width: {W_L}px; height: {H_L}px;", f"width: {W_A}px; height: {H_A}px;", 1)
    m = re.search(r"  svg \{ position: absolute; left: (\d+)px; top: (\d+)px; \}", s)
    w = int(re.search(r'<svg width="(\d+)"', s).group(1))
    left, top = (W_A - w) // 2, int(m.group(2)) + (H_A - H_L) // 2
    s = s.replace(m.group(0), f"  svg {{ position: absolute; left: {left}px; top: {top}px; }}")
    (HERE / f"{stem}-a4.html").write_text(s, encoding="utf-8")
    print("wrote", f"{stem}-a4.html")
