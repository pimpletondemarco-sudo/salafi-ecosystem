"""The ONE small palm picture allowed on every worksheet (owner 2026-10-18: "one small PALM picture only").

Simplified from the owner-chosen cover v4 palm (cover-A4-bone-green.html), following
research/design/palm-spot-illustration-2026-10-18.md:
- trunk: one slightly curved tapered shape in the cover's trunk brown, 4 ring marks
- 7 fronds, each a single leaf shape with 4 notches (no individual leaflets), cover greens
- three short root lines, no labels; no sun, glow, hills or shadow
- default has NO dates (owner: palm only); dates=True adds one small cluster for the owner to compare
- variant "line": outline-only version for black-and-white pages, the progress chart and colouring
Drawn by us in SVG: no clipart, no licence risk, no AI art.
Usage: palm_svg(height_px) -> inline <svg>; python3 palm_spot.py writes assets/palm-spot*.svg
"""
import math
from pathlib import Path

GREEN, GREEN2, TRUNK, RING, DATE, INK = "#456f3a", "#5f8a4f", "#8a5a33", "#6b4022", "#6b3a22", "#2a1d17"
VB_W, VB_H = 140, 132
CROWN = (70.0, 40.0)
# (control angle, tip angle, length): degrees from straight up, clockwise positive
FRONDS = [(-70, -128, 58), (70, 128, 58), (-48, -98, 60), (48, 98, 60), (-24, -58, 50), (24, 58, 50), (-3, 8, 36)]


def _frond(ctrl_a, tip_a, length, width=5.0, notches=(0.42, 0.56, 0.7, 0.84)):
    cx, cy = CROWN
    d = lambda a, r: (cx + r * math.sin(math.radians(a)), cy - r * math.cos(math.radians(a)))
    p0, p1, p2 = (cx, cy), d(ctrl_a, length * 0.62), d(tip_a, length)
    def at(t):
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        dx = 2 * (1 - t) * (p1[0] - p0[0]) + 2 * t * (p2[0] - p1[0])
        dy = 2 * (1 - t) * (p1[1] - p0[1]) + 2 * t * (p2[1] - p1[1])
        n = math.hypot(dx, dy) or 1
        return x, y, -dy / n, dx / n
    N = 40
    top, bot = [], []
    for i in range(N + 1):
        t = i / N
        x, y, nx, ny = at(t)
        w = width * math.sin(math.pi * min(t * 1.08, 1)) ** 0.75 * (1 - 0.35 * t) if t < 1 else 0
        wt, wb = w, w
        for c in notches:  # V-shaped notch on both edges
            k = max(0.0, 1 - abs(t - c) / 0.035)
            wt *= 1 - 0.55 * k
            wb *= 1 - 0.55 * max(0.0, 1 - abs(t - c - 0.06) / 0.035)
        top.append((x + nx * wt, y + ny * wt)); bot.append((x - nx * wb, y - ny * wb))
    pts = top + bot[::-1]
    return "M" + " L".join(f"{a:.2f} {b:.2f}" for a, b in pts) + "Z"


def palm_svg(height=92, variant="color", dates=False, cls="palm"):
    """Inline SVG of the spot palm, `height` px tall (about 0.95 in at 96 px/in by default)."""
    w = height * VB_W / VB_H
    line = variant == "line"
    trunk = "M67.6 42 C67 64 65.8 88 63.8 112 L75.2 112 C73.6 88 72.8 64 72.4 42 Z"
    rings = "M67.4 60 Q70 62 72.6 60 M66.9 74 Q70 76 73.1 74 M66.3 88 Q70 90.2 73.7 88 M65.6 101 Q70 103.4 74.4 101"
    roots = "M66 111 C61 117 55 120 49 122 M69.5 112 L69.5 125 M73 111 C78 117 84 120 90 122"
    s = [f'<svg class="{cls}" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {VB_W} {VB_H}" width="{w:.1f}" height="{height:.1f}" role="img" aria-label="date palm">']
    if line:
        s.append(f'<path d="{roots}" fill="none" stroke="{INK}" stroke-width="2.2" stroke-linecap="round"/>')
        s.append(f'<path d="{trunk}" fill="#fff" stroke="{INK}" stroke-width="2"/>')
        s.append(f'<path d="{rings}" fill="none" stroke="{INK}" stroke-width="1.3" stroke-linecap="round"/>')
        for i, f in enumerate(FRONDS):
            s.append(f'<path d="{_frond(*f)}" fill="#fff" stroke="{INK}" stroke-width="1.8" stroke-linejoin="round"/>')
    else:
        s.append(f'<path d="{roots}" fill="none" stroke="{TRUNK}" stroke-width="3" stroke-linecap="round"/>')
        s.append(f'<path d="{trunk}" fill="{TRUNK}"/>')
        s.append(f'<path d="{rings}" fill="none" stroke="{RING}" stroke-width="1.6" stroke-linecap="round" opacity=".7"/>')
        for i, f in enumerate(FRONDS):
            s.append(f'<path d="{_frond(*f)}" fill="{GREEN if i % 2 == 0 else GREEN2}"/>')
    if dates:
        for x, y in [(76, 48), (81, 47), (78.5, 52), (83.5, 51.5), (81, 56)]:
            s.append(f'<circle cx="{x}" cy="{y}" r="2.9" fill="{"#fff" if line else DATE}" stroke="{INK if line else "#4a2716"}" stroke-width="{1.3 if line else 0.8}"/>')
    s.append("</svg>")
    return "".join(s)


if __name__ == "__main__":
    out = Path(__file__).parent / "assets"
    out.mkdir(exist_ok=True)
    (out / "palm-spot.svg").write_text(palm_svg(264), encoding="utf-8")
    (out / "palm-spot-line.svg").write_text(palm_svg(264, "line"), encoding="utf-8")
    (out / "palm-spot-dates.svg").write_text(palm_svg(264, dates=True), encoding="utf-8")
    print("palm svgs written")
