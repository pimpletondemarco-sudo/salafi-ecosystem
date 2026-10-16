"""Builds the three cover concepts (A, B, C) as standalone HTML pages for rendering."""
import sys
from pathlib import Path

OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent

FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Amiri:wght@700'
         '&family=Baloo+2:wght@600;800&family=Nunito:wght@600;800&display=swap">')

# Faceless sapling mascot: a sprout in a pot. A plant only, no eyes or face.
def sapling(x, y, s, pot, leaf, leaf_dark, stroke="#1d2b22"):
    return f'''<g transform="translate({x} {y}) scale({s})" stroke="{stroke}" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
      <path d="M50 70 C50 50 50 40 50 28" fill="none"/>
      <path d="M50 40 C30 38 18 24 20 8 C38 8 50 22 50 40Z" fill="{leaf}"/>
      <path d="M50 32 C66 32 80 20 80 4 C62 4 50 16 50 32Z" fill="{leaf_dark}"/>
      <path d="M22 70 H78 L72 112 H28 Z" fill="{pot}"/>
      <rect x="18" y="62" width="64" height="12" rx="4" fill="{pot}"/>
    </g>'''

def star8(cx, cy, r, fill, stroke):
    import math
    pts = []
    for i in range(16):
        rad = r if i % 2 == 0 else r * 0.62
        a = math.pi / 8 * i - math.pi / 2
        pts.append(f"{cx + rad * math.cos(a):.1f},{cy + rad * math.sin(a):.1f}")
    return f'<polygon points="{" ".join(pts)}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'

BASE_CSS = '''
@page { size: 8.5in 11in; margin: 0; }
html, body { margin: 0; }
.page { width: 816px; height: 1056px; position: relative; overflow: hidden; font-family: "Nunito", sans-serif; }
.ar { font-family: "Amiri", serif; font-weight: 700; direction: rtl; }
.t { font-family: "Baloo 2", sans-serif; font-weight: 800; line-height: .95; }
.badge { position: absolute; display: grid; place-items: center; text-align: center; font-weight: 800; border-radius: 50%; }
.inc { position: absolute; left: 0; right: 0; text-align: center; font-weight: 800; letter-spacing: .3px; }
.brand { position: absolute; left: 0; right: 0; text-align: center; font-family: "Baloo 2", sans-serif; font-weight: 800; letter-spacing: 1px; }
'''

def page(css, body):
    return f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{BASE_CSS}{css}</style></head><body><div class="page">{body}</div></body></html>'

# A: Sunrise palm, warm sand and teal
A = page('''
.page { background: linear-gradient(#fbe3b8 0%, #f7c98b 55%, #e9a96a 100%); color: #173a3a; }
.ar { position:absolute; top:70px; left:0; right:0; text-align:center; font-size:64px; color:#0f5b5b; }
.t { position:absolute; top:160px; left:0; right:0; text-align:center; font-size:76px; color:#0f5b5b; }
.sub { position:absolute; top:330px; left:0; right:0; text-align:center; font-size:24px; font-weight:800; color:#7a3b12; }
.badge { width:150px; height:150px; right:52px; top:420px; background:#0f5b5b; color:#fbe3b8; font-size:17px; line-height:1.2; border:5px dashed #fbe3b8; transform:rotate(8deg); }
.inc { bottom:100px; font-size:20px; color:#173a3a; }
.brand { bottom:52px; font-size:26px; color:#0f5b5b; }
''', f'''
<svg width="816" height="1056" style="position:absolute;inset:0">
  <circle cx="408" cy="640" r="190" fill="#ffd27a"/>
  <path d="M0 800 C200 760 616 760 816 800 V1056 H0Z" fill="#c98a4b"/>
  <g stroke="#173a3a" stroke-width="4" stroke-linecap="round" fill="none">
    <path d="M396 520 C392 620 388 700 384 790 M420 520 C424 620 428 700 432 790" />
  </g>
  <path d="M396 520 C392 620 388 700 384 790 L432 790 C428 700 424 620 420 520Z" fill="#a8693a"/>
  <g fill="#2f8f6a" stroke="#173a3a" stroke-width="4" stroke-linejoin="round">
    <path d="M408 525 C360 460 270 445 200 470 C270 470 340 490 400 540Z"/>
    <path d="M408 525 C456 460 546 445 616 470 C546 470 476 490 416 540Z"/>
    <path d="M408 520 C380 470 390 410 430 375 C415 430 418 480 414 525Z"/>
    <path d="M405 530 C340 520 270 545 230 595 C290 565 350 555 405 545Z"/>
    <path d="M411 530 C476 520 546 545 586 595 C526 565 466 555 411 545Z"/>
  </g>
  <g fill="#8a3d1a"><circle cx="380" cy="560" r="10"/><circle cx="394" cy="572" r="10"/><circle cx="378" cy="580" r="10"/><circle cx="436" cy="560" r="10"/><circle cx="422" cy="572" r="10"/><circle cx="438" cy="580" r="10"/></g>
  <g stroke="#173a3a" stroke-width="7" stroke-linecap="round" fill="none"><path d="M392 795 C370 815 330 828 280 836"/><path d="M408 795 V846"/><path d="M424 795 C446 815 486 828 536 836"/></g>
  <g font-family="Amiri" font-weight="700" font-size="30" fill="#0f5b5b" text-anchor="middle"><text x="250" y="872">رَبِّي</text><text x="408" y="886">دِينِي</text><text x="566" y="872">نَبِيِّي</text></g>
  {sapling(640, 688, 0.95, "#0f5b5b", "#7ed3a4", "#3fae7a")}
</svg>
<div class="ar">الأُصُولُ الثَّلَاثَةُ</div>
<div class="t">The Three<br>Foundations</div>
<div class="sub">Thalathat al-Usul for Kids · Ages 6–10</div>
<div class="badge">Sourced<br>from the<br>Scholars</div>
<div class="inc">Workbook · Coloring · Answer Key · Teaching Guide</div>
<div class="brand">SunnahSaplings</div>
''')

# B: Mint sapling with geometric star border
stars = "".join(star8(40 + i * 82, 40, 26, "#f4c95d", "#1d2b22") + star8(40 + i * 82, 1016, 26, "#f4c95d", "#1d2b22") for i in range(10))
stars += "".join(star8(40, 122 + i * 82, 26, "#f4c95d", "#1d2b22") + star8(776, 122 + i * 82, 26, "#f4c95d", "#1d2b22") for i in range(11))
B = page('''
.page { background: #e6f5ec; color: #1d2b22; }
.inner { position:absolute; inset:86px; background:#fffdf6; border:4px solid #1d2b22; border-radius:28px; }
.ar { position:absolute; top:130px; left:0; right:0; text-align:center; font-size:58px; color:#2b7a55; }
.t { position:absolute; top:210px; left:0; right:0; text-align:center; font-size:70px; color:#1d2b22; }
.sub { position:absolute; top:375px; left:0; right:0; text-align:center; font-size:22px; font-weight:800; color:#2b7a55; }
.badge { width:136px; height:136px; left:120px; top:640px; background:#f4c95d; color:#1d2b22; font-size:16px; line-height:1.2; border:4px solid #1d2b22; }
.inc { bottom:170px; font-size:19px; }
.brand { bottom:118px; font-size:26px; color:#2b7a55; }
''', f'''
<svg width="816" height="1056" style="position:absolute;inset:0">{stars}</svg>
<div class="inner"></div>
<svg width="816" height="1056" style="position:absolute;inset:0">
  <ellipse cx="408" cy="800" rx="230" ry="28" fill="#c8ead6"/>
  {sapling(258, 430, 3.0, "#e0794c", "#7ed3a4", "#3fae7a")}
  <g font-family="Amiri" font-weight="700" font-size="28" fill="#1d2b22" text-anchor="middle">
    <rect x="300" y="610" width="216" height="46" rx="12" fill="#fffdf6" stroke="#1d2b22" stroke-width="3"/>
    <text x="408" y="643">رَبِّي · دِينِي · نَبِيِّي</text>
  </g>
</svg>
<div class="ar">الأُصُولُ الثَّلَاثَةُ</div>
<div class="t">The Three<br>Foundations</div>
<div class="sub">A Thalathat al-Usul Workbook for Ages 6–10</div>
<div class="badge">Every lesson<br>sourced &amp;<br>cited</div>
<div class="inc">Worksheets · Coloring · Tracing · Answer Key · Parent Guide</div>
<div class="brand">SunnahSaplings</div>
''')

# C: Night masjid, navy and gold
lanterns = "".join(f'''<g transform="translate({x} 0)"><path d="M0 0 V{h}" stroke="#f4c95d" stroke-width="2"/>
  <path d="M-16 {h} h32 l-6 40 h-20 Z" fill="#f4c95d" stroke="#0b1d3a" stroke-width="2"/><rect x="-10" y="{h+8}" width="20" height="24" fill="#ffe9a8"/></g>'''
  for x, h in [(110, 90), (210, 150), (606, 150), (706, 90)])
C = page('''
.page { background: radial-gradient(circle at 50% 30%, #1d3b6e, #0b1d3a 70%); color: #fdf3d6; }
.ar { position:absolute; top:230px; left:0; right:0; text-align:center; font-size:62px; color:#f4c95d; }
.t { position:absolute; top:315px; left:0; right:0; text-align:center; font-size:76px; color:#fdf3d6; }
.sub { position:absolute; top:485px; left:0; right:0; text-align:center; font-size:22px; font-weight:800; color:#f4c95d; }
.badge { width:140px; height:140px; right:70px; top:560px; background:#f4c95d; color:#0b1d3a; font-size:16px; line-height:1.2; border:4px double #0b1d3a; }
.inc { bottom:120px; font-size:19px; color:#fdf3d6; }
.brand { bottom:52px; font-size:26px; color:#f4c95d; }
''', f'''
<svg width="816" height="1056" style="position:absolute;inset:0">
  {lanterns}
  <path d="M640 120 a46 46 0 1 0 30 80 a36 36 0 1 1 -30 -80Z" fill="#f4c95d"/>
  <g fill="#fdf3d6"><circle cx="120" cy="300" r="2.5"/><circle cx="700" cy="330" r="2.5"/><circle cx="560" cy="80" r="2"/><circle cx="260" cy="60" r="2"/></g>
  <g fill="#132c55" stroke="#f4c95d" stroke-width="3">
    <path d="M150 1056 V800 H666 V1056Z"/>
    <path d="M288 800 C288 690 528 690 528 800Z"/>
    <path d="M190 800 V640 h36 V800 M590 800 V640 h36 V800"/>
    <path d="M190 640 l18 -40 l18 40 M590 640 l18 -40 l18 40"/>
    
  </g>
  {sapling(684, 905, 1.0, "#f4c95d", "#7ed3a4", "#3fae7a", "#fdf3d6")}
</svg>
<div class="ar">الأُصُولُ الثَّلَاثَةُ</div>
<div class="t">The Three<br>Foundations</div>
<div class="sub">Thalathat al-Usul for Kids · Ages 6–10</div>
<div class="badge">From the<br>Books of the<br>Scholars</div>
<div class="inc">Workbook · Coloring · Answer Key · Teaching Guide</div>
<div class="brand">SunnahSaplings</div>
''')

for name, html in [("cover-A-sunrise-palm", A), ("cover-B-mint-sapling", B), ("cover-C-night-masjid", C)]:
    (OUT / f"{name}.html").write_text(html, encoding="utf-8")
print("covers written")
