"""Makes the A4 version of the chosen cover (v4, bone and green) from the US Letter file.

A4 is narrower and taller than Letter, so the Letter artwork is placed on a stage shifted
11px left and 33px down, and the sky and earth are extended to fill the extra height.
Nothing is stretched, so circles and Arabic text keep their true shape.
"""
from pathlib import Path

HERE = Path(__file__).parent
src = (HERE / "cover-A4-bone-green.html").read_text(encoding="utf-8")

def swap(s, old, new, count=1):
    assert s.count(old) == count, (old, s.count(old))
    return s.replace(old, new)

s = swap(src, "@page { size: 8.5in 11in; margin: 0; }", "@page { size: 210mm 297mm; margin: 0; }")
s = swap(s, ".page { width: 816px; height: 1056px; position: relative; overflow: hidden;",
         ".page { width: 794px; height: 1123px; position: relative; overflow: hidden; }\n"
         "  .stage { position: absolute; left: -11px; top: 33px; width: 816px; height: 1056px;")
s = swap(s, '<body><div class="page">', '<body><div class="page"><div class="stage">')
s = swap(s, "</div></body></html>", "</div></div></body></html>")
s = swap(s, 'svg class="art" width="816" height="1056" viewBox="0 0 816 1056"',
         'svg class="art" width="816" height="1056" viewBox="0 0 816 1056" overflow="visible"')
# Sky and paper grain: cover the extra 33px on top and 33px below.
s = swap(s, '<rect width="816" height="1056" fill="url(#sky)"/>',
         '<rect y="-60" width="816" height="1180" fill="#e9e5dc"/><rect width="816" height="1056" fill="url(#sky)"/>')
s = swap(s, '<rect width="816" height="1056" fill="#fff" filter="url(#grain)" opacity=".22"/>',
         '<rect y="-60" width="816" height="1180" fill="#fff" filter="url(#grain)" opacity=".22"/>')
# Earth band: extend to the new bottom edge.
s = swap(s, 'C200 758 600 758 816 770 V1056 H0Z', 'C200 758 600 758 816 770 V1140 H0Z')
# Footer sits on the earth band; keep it the same distance from the page edge as on Letter.
s = swap(s, ".foot { position: absolute; left: 0; right: 0; bottom: 40px;",
         ".foot { position: absolute; left: 0; right: 0; bottom: 7px;")
(HERE / "cover-A4-bone-green-a4.html").write_text(s, encoding="utf-8")
print("A4 cover written")
