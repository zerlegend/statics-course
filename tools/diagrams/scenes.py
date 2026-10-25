"""Realistic site illustrations (one per chapter). Pixel coordinates, y down."""
from figlib import *
import math

def new(w, h):
    f = Fig(w, h, sc=1, ox=0, oy=h)
    f.raw(f'<rect width="{w}" height="{h}" rx="10" fill="url(#sky)"/>')
    return f

def D(f, x1, y1, x2, y2, label, off=22):
    f.dim(x1, f.h - y1, x2, f.h - y2, label, off=off)

def vd(f, x, y1, y2, label, side=1):
    f.arrow_px(x, (y1 + y2) / 2, x, y1, c=GRY, w=1.2, head=7); f.arrow_px(x, (y1 + y2) / 2, x, y2, c=GRY, w=1.2, head=7)
    f.text_px(x + 8 * side, (y1 + y2) / 2 + 4, label, c=GRY, sz=12, a="start" if side > 0 else "end")

def hd(f, y, x1, x2, label, above=True):
    f.arrow_px((x1 + x2) / 2, y, x1, y, c=GRY, w=1.2, head=7); f.arrow_px((x1 + x2) / 2, y, x2, y, c=GRY, w=1.2, head=7)
    f.text_px((x1 + x2) / 2, y - 6 if above else y + 16, label, c=GRY, sz=12)

def finish(f, name):
    f.raw(f'<rect width="{f.w}" height="{f.h}" rx="10" fill="none" stroke="#94a3b8" stroke-width="1.5"/>')
    f.save(name)

def bar(f, x1, y1, x2, y2, w=5):
    f.line_px(x1, y1, x2, y2, c=INK, w=w)

def conc(f, x, y, w, h):
    f.raw(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#conc)" stroke="#475569" stroke-width="1.6"/>')

def pin_px(f, x, y):
    f.circle_px(x, y, 5, fill="#fff", c=INK, w=2)

def worker(f, x, feet_y, s=1.0, arms_up=False):
    """simple site worker with hard hat; x = centre, feet_y = ground contact"""
    h = 62 * s
    f.line_px(x - 5 * s, feet_y, x - 4 * s, feet_y - 26 * s, c="#1e3a8a", w=6 * s)
    f.line_px(x + 5 * s, feet_y, x + 4 * s, feet_y - 26 * s, c="#1e3a8a", w=6 * s)
    f.raw(f'<rect x="{x - 10 * s:.1f}" y="{feet_y - 50 * s:.1f}" width="{20 * s:.1f}" height="{26 * s:.1f}" rx="5" fill="#f97316" stroke="#9a3412" stroke-width="1"/>')
    f.line_px(x - 10 * s, feet_y - 46 * s, x - 18 * s, feet_y - (58 if arms_up else 36) * s, c="#f97316", w=5 * s)
    f.line_px(x + 10 * s, feet_y - 46 * s, x + 18 * s, feet_y - (58 if arms_up else 36) * s, c="#f97316", w=5 * s)
    f.circle_px(x, feet_y - 57 * s, 7 * s, fill="#f1c9a5", c="#9a6b45", w=1)
    f.raw(f'<path d="M{x - 8.5 * s:.1f} {feet_y - 58 * s:.1f} A{8.5 * s:.1f} {8.5 * s:.1f} 0 0 1 {x + 8.5 * s:.1f} {feet_y - 58 * s:.1f} Z" fill="#facc15" stroke="#a16207" stroke-width="1"/>')

# ======== Chapter 1: cable-stayed footbridge
f = new(720, 400)
f.raw('<rect x="0" y="330" width="720" height="70" fill="#9ec5e6"/>')
for k in range(12): f.line_px(20 + k * 60, 352 + (k % 3) * 10, 52 + k * 60, 352 + (k % 3) * 10, c="#d6eaf8", w=2)
for x in (60, 660): conc(f, x - 15, 286, 30, 80)
f.raw('<rect x="40" y="270" width="640" height="16" fill="url(#conc)" stroke="#334155" stroke-width="2" filter="url(#sh)"/>')
for x in range(50, 680, 20): f.line_px(x, 270, x, 256, c="#64748b", w=1.2)
f.line_px(40, 256, 680, 256, c="#64748b", w=1.6)
f.poly_px([(338, 270), (382, 270), (368, 62), (352, 62)], fill="url(#conc)", c="#475569", w=2)
for ty, vk in ((80, 3.2), (118, 2), (156, 2)):
    v = 270 - ty; hx = v * 4 / 3
    for sgn in (-1, 1):
        f.line_px(360, ty, 360 + sgn * hx, 270, c="#334155", w=vk)
f.circle_px(360, 80, 4, fill="#fff", c=INK, w=2)
for sgn, lab in ((-1, "T = 450 kN"), (1, "T = 450 kN")):
    ux, uy = sgn * 0.8, 0.6
    f.arrow_px(360, 80, 360 + ux * 70, 80 + uy * 70, c=RED, w=3.4, head=11)
    f.text_px(360 + ux * 70 + sgn * 6, 80 + uy * 70 - 8, lab, a="end" if sgn < 0 else "start", c=RED, sz=13, b=True)
vd(f, 408, 80, 270, "30 m")
D(f, 107, 300, 360, 300, "40 m", off=0.1) if False else None
f.dim(107, f.h - 300, 360, f.h - 300, "40 m", off=-1) if False else None
f.text_px(220, 306, "40 m (horizontal from tower axis to deck anchor)", c=GRY, sz=12)
f.line_px(107, 290, 360, 290, c=GRY, w=1, d="4,3")
f.text_px(360, 24, "Cable-stayed footbridge: forces from the stay cables act on the tower top", c=INK, sz=14, b=True)
f.text_px(360, 44, "(only the top pair of cables is analysed in the example)", c=GRY, sz=12)
finish(f, "scene-ch1-bridge")

# ======== Chapter 2: tower crane
f = new(720, 446)
f.raw('<rect x="0" y="360" width="720" height="86" fill="url(#soil)"/>')
f.line_px(0, 360, 720, 360, c="#6b5b45", w=3)
conc(f, 310, 360, 80, 24)
for y in range(70, 360, 26):
    f.line_px(342, y, 358, y + 26, c="#b45309", w=2); f.line_px(358, y, 342, y + 26, c="#b45309", w=2)
f.line_px(342, 70, 342, 360, c="#d97706", w=4); f.line_px(358, 70, 358, 360, c="#d97706", w=4)
# jib
f.line_px(350, 66, 640, 66, c="#d97706", w=5); f.line_px(350, 94, 640, 66, c="#d97706", w=3)
for x in range(370, 640, 28): f.line_px(x, 66, x + 14, 94 - (x + 14 - 350) * 28 / 290, c="#b45309", w=1.6)
f.line_px(350, 66, 245, 66, c="#d97706", w=5); f.line_px(350, 40, 350, 66, c="#d97706", w=4)
f.line_px(350, 40, 640, 66, c="#475569", w=1.4); f.line_px(350, 40, 245, 66, c="#475569", w=1.4)
f.raw('<rect x="334" y="96" width="26" height="22" fill="#fde68a" stroke="#a16207" stroke-width="1.5"/>')
f.raw('<rect x="236" y="70" width="58" height="34" fill="url(#conc)" stroke="#334155" stroke-width="2" filter="url(#sh)"/>')
f.raw('<rect x="570" y="66" width="20" height="12" fill="#334155"/>')
f.line_px(580, 78, 580, 196, c="#1f2937", w=1.6)
f.raw('<rect x="556" y="196" width="48" height="18" fill="url(#conc)" stroke="#334155" stroke-width="1.8" filter="url(#sh)"/>')
f.line_px(580, 196, 566, 196, c="#1f2937", w=1.2); f.line_px(580, 196, 594, 196, c="#1f2937", w=1.2)
# building under construction
for x in (500, 560, 620): f.raw(f'<rect x="{x - 5}" y="232" width="10" height="128" fill="url(#conc)" stroke="#64748b"/>')
for y in (300, 232): f.raw(f'<rect x="486" y="{y}" width="150" height="8" fill="url(#conc)" stroke="#64748b"/>')
# force arrows
f.arrow_px(580, 14, 580, 52, c=RED, w=3.4); f.text_px(580, 12, "25 kN (load)", c=RED, sz=13, b=True)
f.arrow_px(457, 14, 457, 52, c=RED, w=3.4); f.text_px(457, 12, "30 kN (jib)", c=RED, sz=13, b=True)
f.arrow_px(265, 14, 265, 52, c=RED, w=3.4); f.text_px(265, 12, "80 kN (counterweight)", c=RED, sz=13, b=True) if False else f.text_px(300, 12, "80 kN (counterweight)", c=RED, sz=13, b=True, a="end")
f.line_px(350, 26, 350, 366, c=GRY, w=1, d="6,4"); f.text_px(350, 436, "mast axis (point O)", c=GRY, sz=12)
D(f, 350, 396, 457, 396, "14 m", off=0.1); D(f, 350, 414, 580, 414, "30 m", off=0.1); D(f, 265, 396, 350, 396, "10 m", off=0.1)
finish(f, "scene-ch2-crane")

# ======== Chapter 3: footbridge girder on abutments
f = new(720, 400)
f.raw('<rect x="0" y="300" width="720" height="100" fill="#9ec5e6"/>')
for k in range(12): f.line_px(20 + k * 60, 340 + (k % 3) * 12, 55 + k * 60, 340 + (k % 3) * 12, c="#d6eaf8", w=2)
for x in (60, 580): conc(f, x, 205, 80, 130)
# bearings
f.poly_px([(120, 205), (108, 190), (132, 190)], fill="url(#steelg)", c=INK, w=2)
f.poly_px([(560, 205), (548, 190), (572, 190)], fill="url(#steelg)", c=INK, w=2) if False else None
f.poly_px([(600, 205), (588, 190), (612, 190)], fill="url(#steelg)", c=INK, w=2)
f.circle_px(594, 210, 4, fill="url(#steelg)", c=INK, w=1.5); f.circle_px(606, 210, 4, fill="url(#steelg)", c=INK, w=1.5)
# girder + deck
f.raw('<rect x="100" y="168" width="520" height="22" fill="url(#steelg)" stroke="#334155" stroke-width="2" filter="url(#sh)"/>')
f.raw('<rect x="100" y="158" width="520" height="10" fill="url(#conc)" stroke="#475569" stroke-width="1.4"/>')
# maintenance cart: wheels at 3 m and 5 m from A (A at x=120, 40 px per m)
for xw in (240, 320):
    f.circle_px(xw, 148, 8, fill="#334155", c="#0f172a", w=1.5); f.circle_px(xw, 148, 3, fill="#cbd5e1", c="#475569", w=1)
f.raw('<rect x="226" y="112" width="108" height="30" rx="4" fill="#facc15" stroke="#a16207" stroke-width="1.8"/>')
f.raw('<rect x="300" y="96" width="28" height="18" fill="#fde68a" stroke="#a16207" stroke-width="1.4"/>')
f.arrow_px(240, 62, 240, 138, c=RED, w=3.4); f.text_px(240, 56, "20 kN", c=RED, sz=13, b=True)
f.arrow_px(320, 62, 320, 138, c=RED, w=3.4); f.text_px(320, 56, "20 kN", c=RED, sz=13, b=True)
f.arrow_px(360, 100, 360, 154, c=RED, w=3.4) if False else None
f.arrow_px(480, 62, 480, 154, c=RED, w=3.4); f.text_px(480, 56, "60 kN (deck weight, resultant at midspan)", c=RED, sz=13, b=True) if False else f.text_px(520, 44, "60 kN deck weight", c=RED, sz=13, b=True); f.text_px(520, 60, "(resultant at midspan)", c=RED, sz=12)
f.arrow_px(120, 280, 120, 194, c=BLUE, w=3.4); f.text_px(120, 298, "A_{y}", c=BLUE, sz=14, b=True)
f.arrow_px(600, 280, 600, 194, c=BLUE, w=3.4); f.text_px(600, 298, "B_{y}", c=BLUE, sz=14, b=True)
f.arrow_px(120, 190, 60, 190, c=BLUE, w=3.2); f.text_px(52, 186, "A_{x}", c=BLUE, sz=14, b=True, a="end")
f.text_px(120, 226, "pin bearing", c="#e2e8f0", sz=11); f.text_px(600, 226, "rocker bearing", c="#e2e8f0", sz=11)
D(f, 120, 372, 600, 372, "span 12 m", off=0.1)
D(f, 120, 352, 240, 352, "3 m", off=0.1); D(f, 240, 352, 320, 352, "2 m", off=0.1)
finish(f, "scene-ch3-footbridge")

# ======== Chapter 4: warehouse roof truss
f = new(720, 380)
f.raw('<rect x="0" y="320" width="720" height="60" fill="url(#soil)"/>'); f.line_px(0, 320, 720, 320, c="#6b5b45", w=3)
for x in (50, 640): f.raw(f'<rect x="{x}" y="200" width="30" height="120" fill="url(#brick)" stroke="#7c3f2a" stroke-width="1.5"/>')
A, B, C, Dd = (80, 200), (360, 62), (640, 200), (360, 200)
# roof sheeting (corrugated look)
for k in range(0, 41):
    t = k / 40
    f.line_px(A[0] + (B[0] - A[0]) * t - 6, A[1] + (B[1] - A[1]) * t - 12, A[0] + (B[0] - A[0]) * t - 6, A[1] + (B[1] - A[1]) * t - 6, c="#94a3b8", w=1.5) if False else None
f.line_px(A[0] - 14, A[1] - 6, B[0], B[1] - 14, c="#64748b", w=5); f.line_px(B[0], B[1] - 14, C[0] + 14, C[1] - 6, c="#64748b", w=5)
zz = []
for k in range(0, 61):
    t = k / 60; off = -9 if k % 2 == 0 else -13
    zz.append((A[0] - 14 + (B[0] - A[0] + 14) * t + 0, A[1] - 6 + (B[1] - 14 - (A[1] - 6)) * t + off))
for k in range(0, 61):
    t = k / 60; off = -9 if k % 2 == 0 else -13
    zz.append((B[0] + (C[0] + 14 - B[0]) * t, B[1] - 14 + (C[1] - 6 - (B[1] - 14)) * t + off))
f.poly_px(zz, c="#475569", w=1.6, close=False)
for t in (0.25, 0.5, 0.75):  # purlins
    for (p, q) in ((A, B), (B, C)):
        px, py = p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t
        f.raw(f'<rect x="{px - 6:.1f}" y="{py - 12:.1f}" width="12" height="9" fill="url(#steelg)" stroke="#334155" stroke-width="1.2"/>')
for (p, q) in ((A, B), (B, C), (A, Dd), (Dd, C), (B, Dd)): bar(f, p[0], p[1], q[0], q[1], 6)
for p in (A, B, C, Dd): pin_px(f, *p)
f.poly_px([(A[0], A[1] + 4), (A[0] - 12, A[1] + 22), (A[0] + 12, A[1] + 22)], fill="url(#steelg)", c=INK, w=2)
f.poly_px([(C[0], C[1] + 4), (C[0] - 12, C[1] + 22), (C[0] + 12, C[1] + 22)], fill="url(#steelg)", c=INK, w=2)
for p, t in ((A, "A"), (B, "B"), (C, "C"), (Dd, "D")): f.text_px(p[0] + (-16 if t == "A" else 16 if t == "C" else -16 if t == "B" else 0), p[1] + (-4 if t in "AC" else -22 if t == "B" else 26), t, c=INK, sz=14, b=True)
f.arrow_px(360, 4, 360, 46, c=RED, w=3.4); f.text_px(376, 22, "16 kN (roof, purlins, sheeting)", c=RED, sz=13, b=True, a="start")
f.arrow_px(360, 280, 360, 208, c=RED, w=3.4) if False else f.arrow_px(412, 230, 412, 206, c=RED, w=3.4) if False else None
f.arrow_px(360, 222, 360, 290, c=RED, w=3.4); f.text_px(376, 280, "6 kN (ceiling services)", c=RED, sz=13, b=True, a="start")
f.arrow_px(A[0], 296, A[0], 230, c=BLUE, w=3.2); f.text_px(A[0] + 14, 292, "A_{y}", c=BLUE, sz=13, b=True, a="start")
f.arrow_px(C[0], 296, C[0], 230, c=BLUE, w=3.2); f.text_px(C[0] + 14, 292, "C_{y}", c=BLUE, sz=13, b=True, a="start")
D(f, 80, 352, 640, 352, "span 12 m", off=0.1); vd(f, 676, 62, 200, "3 m", side=-1)
finish(f, "scene-ch4-roof-truss")

# ======== Chapter 5: gravity retaining wall
f = new(720, 420)
# ground & soil
f.raw('<rect x="0" y="330" width="720" height="90" fill="url(#soil)"/>')
f.raw('<rect x="60" y="282" width="200" height="48" fill="url(#soil)"/>')
f.poly_px([(304, 282), (304, 42), (690, 42), (690, 330), (440, 330), (440, 282)], fill="url(#soil)", c="#b89f78", w=1.2)
f.line_px(60, 282, 264, 282, c="#6b5b45", w=3); f.line_px(304, 42, 690, 42, c="#6b5b45", w=3)
# wall (concrete)
f.poly_px([(200, 330), (440, 330), (440, 282), (304, 282), (304, 42), (264, 42), (264, 282), (200, 282)], fill="url(#conc)", c="#334155", w=2.4)
f.dot(204, 330, r=4, c=INK) if False else None
f.text_px(196, 346, "O (toe)", c=INK, sz=13, a="end")
f.circle_px(200, 330, 5, fill="#fff", c=INK, w=2)
cx, cy = 200 + 1.2955 * 80, 330 - 1.1182 * 80
f.circle_px(cx, cy, 6, fill=GRN, c="#14532d", w=1.5)
f.text_px(cx + 12, cy + 24, "centroid of wall section", c=GRN, sz=13, b=True, a="start") if False else f.text_px(cx + 14, cy + 40, "centroid G", c=GRN, sz=13, b=True, a="start")
f.line_px(cx + 12, cy + 34, cx + 3, cy + 8, c=GRN, w=1.2)
f.arrow_px(cx, cy, cx, cy + 80, c=RED, w=3.6) if False else None
f.arrow_px(cx + 40, 108, cx + 40, 36, c=RED, w=0.01) if False else None
f.arrow_px(cx, 12, cx, cy - 8, c=RED, w=3.4) if False else None
f.arrow_px(cx - 90, cy, cx - 12, cy, c=RED, w=0.01) if False else None
f.arrow_px(392, 234, 312, 234, c=RED, w=3.6); f.text_px(400, 232, "P = 40 kN/m", c=RED, sz=13, b=True, a="start"); f.text_px(400, 248, "(soil thrust, 1.2 m above base)", c=RED, sz=12, a="start")
f.text_px(540, 190, "retained soil", c="#6b5b45", sz=14, i=True)
f.text_px(90, 266, "toe side", c="#6b5b45", sz=12)
D(f, 200, 330, 440, 330, "3.0 m", off=26); D(f, 200, 282, 264, 282, "0.8 m", off=-20) if False else None
hd(f, 30, 264, 304, "0.5 m"); vd(f, 232, 42, 282, "3.0 m", side=-1)
vd(f, 456, 282, 330, "0.6 m")
f.line_px(200, 330, 200, 360, c=GRY, w=1); f.line_px(264, 282, 264, 304, c=GRY, w=1) if False else None
hd(f, 262, 200, 264, "0.8 m")
f.text_px(520, 24, "Gravity retaining wall, 1 m length", c=INK, sz=14, b=True)
finish(f, "scene-ch5-retaining-wall")

# ======== Chapter 6: floor joists and steel section
f = new(720, 400)
f.raw('<defs><pattern id="wood" width="12" height="6" patternUnits="userSpaceOnUse"><rect width="12" height="6" fill="#e6c590"/><path d="M0 2Q6 0 12 2M0 5Q6 3 12 5" stroke="#b98a4e" stroke-width="0.8" fill="none"/></pattern></defs>')
f.text_px(360, 26, "Same material, different orientation and shape: area moment of inertia governs stiffness", c=INK, sz=14, b=True)
# (a) joist on edge: 50 x 200 mm at 0.9 px/mm
f.raw('<rect x="60" y="120" width="45" height="180" fill="url(#wood)" stroke="#7c5a2b" stroke-width="2" filter="url(#sh)"/>')
f.raw('<rect x="40" y="108" width="85" height="12" fill="#d8b684" stroke="#7c5a2b" stroke-width="1.5"/>')
f.text_px(82, 360, "(a) joist on edge", c=INK, sz=13, b=True)
hd(f, 322, 60, 105, "50 mm", above=False); vd(f, 140, 120, 300, "200 mm")
# (b) joist flat
f.raw('<rect x="200" y="255" width="180" height="45" fill="url(#wood)" stroke="#7c5a2b" stroke-width="2" filter="url(#sh)"/>')
f.raw('<rect x="190" y="243" width="200" height="12" fill="#d8b684" stroke="#7c5a2b" stroke-width="1.5"/>')
f.text_px(290, 360, "(b) same joist laid flat", c=INK, sz=13, b=True)
hd(f, 322, 200, 380, "200 mm", above=False); vd(f, 400, 255, 300, "50 mm")
# (c) built-up steel I-section 150x20 flanges, 10 web, 300 deep at 0.9 px/mm
pts = [(500, 100), (635, 100), (635, 118), (572.5, 118), (572.5, 352), (635, 352), (635, 370), (500, 370), (500, 352), (562.5, 352), (562.5, 118), (500, 118)]
pts = [(500, 100), (635, 100), (635, 118), (572, 118), (572, 352), (635, 352), (635, 370), (500, 370), (500, 352), (563, 352), (563, 118), (500, 118)]
f.poly_px(pts, fill="url(#steelg)", c="#1f2937", w=2.4)
f.text_px(568, 392, "(c) built-up steel section", c=INK, sz=13, b=True)
D(f, 500, 370, 635, 370, "150 mm", off=22) if False else None
f.line_px(670, 100, 670, 370, c=GRY, w=1); f.text_px(676, 240, "300 mm", c=GRY, sz=12, a="start")
f.text_px(568, 92, "flange 150 × 20, web 10 × 260", c=GRY, sz=12)
f.line_px(485, 235, 650, 235, c="#16a34a", w=1.4, d="10,4,2,4"); f.text_px(655, 239, "x̄", c="#16a34a", sz=13, i=True, a="start")
finish(f, "scene-ch6-sections")

# ======== Chapter 7: ladder against a building
f = new(720, 440)
f.raw('<rect x="0" y="390" width="720" height="50" fill="url(#soil)"/>'); f.line_px(0, 390, 720, 390, c="#6b5b45", w=3)
f.raw('<rect x="0" y="40" width="262" height="350" fill="url(#brick)" stroke="#7c3f2a" stroke-width="2"/>')
for (x, y) in ((40, 70), (150, 70), (40, 200), (150, 200)):
    f.raw(f'<rect x="{x}" y="{y}" width="64" height="86" fill="#bfdbfe" stroke="#f8fafc" stroke-width="4"/>'); f.line_px(x + 32, y, x + 32, y + 86, c="#f8fafc", w=3); f.line_px(x, y + 43, x + 64, y + 43, c="#f8fafc", w=3)
sc = 55
base = (262 + 1.5 * sc, 390); top = (262, 390 - 5.8095 * sc)
ux, uy = (top[0] - base[0]), (top[1] - base[1]); L = math.hypot(ux, uy); ux, uy = ux / L, uy / L
nx, ny = -uy, ux
for off in (-5, 5): f.line_px(base[0] + nx * off, base[1] + ny * off, top[0] + nx * off, top[1] + ny * off, c="#b45309", w=4)
for k in range(1, 20):
    t = k * 0.3 * sc
    f.line_px(base[0] + ux * t - nx * 5, base[1] + uy * t - ny * 5, base[0] + ux * t + nx * 5, base[1] + uy * t + ny * 5, c="#92400e", w=2.4)
# worker at s ~ 4.5 m
sx, sy = base[0] + ux * 4.5 * sc, base[1] + uy * 4.5 * sc
worker(f, sx + 22, sy + 14, 1.15)
# forces
mx, my = base[0] + ux * 3 * sc, base[1] + uy * 3 * sc
f.arrow_px(mx, my, mx, my + 62, c=RED, w=3.4); f.text_px(mx + 12, my + 22, "150 N (ladder)", c=RED, sz=13, b=True, a="start")
f.arrow_px(sx + 70, sy - 20, sx + 70, sy + 56, c=RED, w=3.4); f.text_px(sx + 78, sy + 76, "900 N (worker)", c=RED, sz=13, b=True, a="start")
f.arrow_px(top[0], top[1], top[0] + 72, top[1], c=BLUE, w=3.4); f.text_px(top[0] + 78, top[1] + 5, "N_{w} (smooth wall)", c=BLUE, sz=13, b=True, a="start")
f.arrow_px(base[0], base[1], base[0], base[1] - 70, c=BLUE, w=3.4); f.text_px(base[0] + 8, base[1] - 74, "N_{f}", c=BLUE, sz=13, b=True, a="start")
f.arrow_px(base[0], base[1] - 4, base[0] - 70, base[1] - 4, c=GRN, w=3.4); f.text_px(base[0] - 74, base[1] - 12, "F", c=GRN, sz=13, b=True, a="end")
D(f, 262, 415, base[0], 415, "1.5 m", off=0.1)
f.text_px(base[0] + 40, 330, "ladder length 6 m", c=GRY, sz=12, a="start")
f.line_px(262, top[1], 262, 390, c=GRY, w=1, d="4,3")
f.text_px(396, 34, "Site ladder: how steep and how rough must the ground be?", c=INK, sz=14, b=True)
finish(f, "scene-ch7-ladder")
