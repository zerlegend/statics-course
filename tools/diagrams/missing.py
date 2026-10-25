"""Figures for tutorial problems that previously had no diagram."""
from figlib import *
import math

AX = "#16a34a"

def pxfig(w, h):
    return Fig(w, h, sc=1, ox=0, oy=h)

def joint(f, x, y, label=None, dx=0, dy=0):
    px, py = f.P(x, y)
    f.circle_px(px, py, 5, fill="#fff", c=INK, w=2)
    if label: f.text_px(px + dx, py + dy, label, sz=14, b=True)

# ---- Ch2 P2: three concurrent forces
f = Fig(520, 360, sc=2.6, ox=240, oy=190)
f.arrow(-60, 0, 75, 0, c=GRY, w=1.5, head=8); f.arrow(0, -50, 0, 70, c=GRY, w=1.5, head=8)
f.text(75, 0, "x", dx=10, dy=5, c=GRY, i=True); f.text(0, 70, "y", dy=-8, c=GRY, i=True)
f.arrow(0, 0, 80, 0); f.arrow(0, 0, 0, 60); f.arrow(0, 0, -60, -80 * 0.75) if False else f.arrow(0, 0, -36, -48)
f.text(80, 0, "80 N", dy=20, c=RED, a="end") if False else f.text(60, 0, "80 N", dy=20, c=RED)
f.text(0, 60, "60 N", dx=10, dy=0, a="start", c=RED)
f.text(-36, -48, "100 N", dx=-8, dy=18, a="end", c=RED)
f.line(0, 0, -36, 0, c=GRY, w=1, d="3,3"); f.line(-36, 0, -36, -48, c=GRY, w=1, d="3,3")
f.text(-18, 0, "3", dy=-6, c=GRY, sz=12); f.text(-36, -24, "4", dx=-8, a="end", c=GRY, sz=12)
f.dot(0, 0)
f.save("p2-2-three-forces")

# ---- Ch3 P1: support types and unknowns
f = Fig(660, 260, sc=1, ox=0, oy=260)
def beam_stub(x1, x2, y): f.line(x1, y, x2, y, c=INK, w=7)
# pin
beam_stub(60, 150, 150); f.pin(150, 150)
f.arrow(150, 150, 150, 200, c=BLUE, w=3); f.text(150, 200, "A_{y}", dx=-8, dy=-2, a="end", c=BLUE, b=True)
f.arrow(150, 150, 200, 150, c=BLUE, w=3); f.text(200, 150, "A_{x}", dx=6, dy=5, a="start", c=BLUE, b=True)
f.text(130, 40, "Pin: 2 unknowns", c=INK, sz=14, b=True)
# roller
beam_stub(290, 380, 150); f.roller(380, 150)
f.arrow(380, 150, 380, 205, c=BLUE, w=3); f.text(380, 205, "N", dx=-8, dy=-2, a="end", c=BLUE, b=True)
f.text(360, 40, "Roller: 1 unknown", c=INK, sz=14, b=True)
# fixed
f.wall(560, 90, 200, side=1); beam_stub(480, 560, 150)
f.arrow(540, 150, 540, 205, c=BLUE, w=3); f.text(540, 205, "A_{y}", dx=-8, dy=-2, a="end", c=BLUE, b=True)
f.arrow(540, 150, 490, 150, c=BLUE, w=0.01) if False else None
f.arrow(560, 150, 515, 150, c=BLUE, w=3); f.text(512, 154, "A_{x}", dx=-4, dy=18, a="end", c=BLUE, b=True)
f.moment(560, 150, 30, 40, 140, c=GRN) if False else f.moment(560, 150, 34, 30, 150, c=GRN)
f.text(600, 150, "M_{A}", dx=-8, dy=-40, a="start", c=GRN, b=True)
f.text(560, 40, "Fixed: 3 unknowns", c=INK, sz=14, b=True)
f.save("p3-1-support-types")

# ---- Ch3 P5: 3D supports
f = Fig3(640, 330, sc=36, ox=170, oy=210)
def torque(f, c, axis, r=0.9, a0=40, a1=300, col=GRN):
    ax = {"x": ((0, 1, 0), (0, 0, 1)), "y": ((0, 0, 1), (1, 0, 0)), "z": ((1, 0, 0), (0, 1, 0))}[axis]
    u, v = ax
    pts = []
    for k in range(0, 31):
        t = math.radians(a0 + (a1 - a0) * k / 30)
        pts.append(f.p3(c[0] + r * (math.cos(t) * u[0] + math.sin(t) * v[0]),
                        c[1] + r * (math.cos(t) * u[1] + math.sin(t) * v[1]),
                        c[2] + r * (math.cos(t) * u[2] + math.sin(t) * v[2])))
    f.poly_px(pts[:-1], c=col, w=2.2, close=False)
    f.arrow_px(*pts[-2], *pts[-1], c=col, w=2.2, head=8)
# ball and socket
f.ox = 170
f.circle_px(*f.p3(0, 0, 0), 15, fill="url(#steelg)", c=INK, w=2)
for ax, lab in (((3, 0, 0), "R_{x}"), ((0, 3, 0), "R_{y}"), ((0, 0, 3), "R_{z}")):
    f.arrow3((0, 0, 0), ax, c=BLUE, w=3); f.text3(ax, lab, dx=10, dy=4, a="start", c=BLUE, b=True)
f.text_px(170, 40, "Ball-and-socket: 3 unknowns", c=INK, sz=14, b=True)
# fixed
f.ox = 470
f.raw(f'<rect x="{f.p3(0,0,0)[0] - 18:.1f}" y="{f.p3(0,0,0)[1] - 18:.1f}" width="36" height="36" fill="url(#conc)" stroke="#334155" stroke-width="2" filter="url(#sh)"/>')
for ax, lab in (((3, 0, 0), "R_{x}"), ((0, 3, 0), "R_{y}"), ((0, 0, 3), "R_{z}")):
    f.arrow3((0, 0, 0), ax, c=BLUE, w=3); f.text3(ax, lab, dx=10, dy=4, a="start", c=BLUE, b=True)
torque(f, (2.2, 0, 0), "x", 0.7); torque(f, (0, 2.2, 0), "y", 0.7); torque(f, (0, 0, 2.2), "z", 0.7)
f.text_px(470, 40, "Fixed support: 6 unknowns", c=INK, sz=14, b=True)
f.text_px(470, 60, "(3 forces in blue, 3 couples in green)", c=GRN, sz=12)
f.ox = 170
f.save("p3-5-3d-supports")

# ---- Ch4 P1: 13-member Pratt truss
f = Fig(660, 280, sc=62, ox=60, oy=200)
bot = [(0, 0), (3, 0), (6, 0), (9, 0)]; top = [(0, 2.4), (3, 2.4), (6, 2.4), (9, 2.4)]
for i in range(3): f.line(*bot[i], *bot[i + 1], w=4); f.line(*top[i], *top[i + 1], w=4)
for i in range(4): f.line(*bot[i], *top[i], w=4)
for i in range(3): f.line(*top[i], *bot[i + 1], w=4)
f.pin(0, 0); f.roller(9, 0)
for p in bot + top: joint(f, *p)
f.text_px(330, 28, "m = 13 members, j = 8 joints, r = 3 reactions", c=INK, sz=14, b=True)
f.save("p4-1-truss-13")

# ---- Ch4 P2: 10 members, 7 joints
f = Fig(660, 270, sc=62, ox=60, oy=200)
P = {"A": (0, 0), "B": (3, 0), "C": (6, 0), "D": (9, 0), "E": (1.5, 2), "F": (4.5, 2), "G": (7.5, 2)}
for a, b in ("AB", "BC", "CD", "EF", "FG", "AE", "EB", "BF", "FC", "GD"): f.line(*P[a], *P[b], w=4)
f.pin(0, 0); f.roller(9, 0)
for k, p in P.items(): joint(f, *p, k, 0, 22 if k in "ABCD" else -12)
f.text_px(330, 28, "m = 10 members, j = 7 joints, r = 3 reactions", c=INK, sz=14, b=True)
f.save("p4-2-truss-10")

# ---- Ch4 P3: zero-force joints
f = pxfig(640, 260)
f.text_px(150, 30, "(a) two non-collinear members", c=INK, sz=14, b=True)
f.line_px(60, 120, 150, 120, c=INK, w=6); f.line_px(150, 120, 220, 190, c=INK, w=6)
f.circle_px(150, 120, 6, fill="#fff", c=INK, w=2); f.text_px(150, 106, "joint, no load", c=GRY, sz=12); f.text_px(150, 235, "forces in both members = ?", c=RED, sz=13)
f.text_px(480, 30, "(b) three members, two collinear", c=INK, sz=14, b=True)
f.line_px(390, 120, 560, 120, c=INK, w=6); f.line_px(475, 120, 530, 200, c=INK, w=6)
f.circle_px(475, 120, 6, fill="#fff", c=INK, w=2); f.text_px(475, 104, "E (no load)", c=GRY, sz=12)
f.text_px(420, 140, "AE", c=GRY, sz=13, b=True); f.text_px(525, 140, "EC", c=GRY, sz=13, b=True); f.text_px(518, 190, "ED", c=GRY, sz=13, b=True)
f.text_px(480, 225, "F_{ED} = ?", c=RED, sz=13); f.text_px(480, 245, "compare F_{AE} and F_{EC}", c=RED, sz=13)
f.save("p4-3-zero-force")

# ---- Ch4 P5 / P6 variants
def warren(name, load):
    f = Fig(700, 400, sc=66, ox=70, oy=290)
    pts = {"A": (0, 0), "C": (4, 0), "E": (8, 0), "B": (2, 3), "D": (6, 3)}
    for a, b in ("AB", "BC", "CD", "DE", "BD", "AC", "CE"): f.line(*pts[a], *pts[b], w=3.5)
    f.pin(0, 0); f.roller(8, 0)
    f.line(3, -0.7, 3, 3.7, c="#7c3aed", w=2, d="8,5"); f.text(3, 3.7, "section", dx=6, dy=-6, a="start", c="#7c3aed", sz=13)
    for k, (dx, dy) in {"A": (-18, 6), "C": (-18, 24), "E": (18, 6), "B": (0, -14), "D": (0, -14)}.items(): joint(f, *pts[k], k, dx, dy)
    f.arrow(4, 0, 4, -1.4, c=RED, w=3); f.text(4, -1.4, load, dx=12, dy=8, a="start", c=RED, b=True)
    f.dim(0, -2.0, 4, -2.0, "4 m", off=0.1); f.dim(4, -2.0, 8, -2.0, "4 m", off=0.1); f.dim(8, 0, 8, 3, "3 m", off=34)
    f.save(name)
warren("p4-5-truss-36", "36 kN")

f = Fig(560, 360, sc=70, ox=100, oy=110)
f.wall(0, -2.7, 1.3, side=-1)
f.line(0, 0, 4, 0, c=INK, w=7); f.line(2, 0, 0, -2, c=GRY, w=4)
for p, lab, dx, dy in (((0, 0), "A", 18, -14), ((4, 0), "C", 18, 22), ((2, 0), "D", 14, 22), ((0, -2), "E", 18, 16)): joint(f, *p, lab, dx, dy)
f.arrow(4, 1.2, 4, 0.14, c=RED, w=3); f.text(4, 1.2, "10 kN", dx=12, dy=4, a="start", c=RED, b=True)
f.text(1.0, -1.0, "DE (two-force member)", dx=16, dy=-6, a="start", c=GRY, sz=13)
f.dim(0, 0, 2, 0, "2 m", off=-30); f.dim(2, 0, 4, 0, "2 m", off=-30); f.dim(0, 0, 0, -2, "2 m", off=26)
f.save("p4-6-frame-2m")

# ---- Ch4 P7: tetrahedral space truss
f = Fig3(560, 340, sc=44, ox=250, oy=270)
A, B, C, D = (0, -2, 0), (0, 2, 0), (3, 0, 0), (1.2, 0, 3.4)
for p, q in ((A, B), (B, C), (C, A), (A, D), (B, D), (C, D)): f.line3(p, q, c=INK, w=4)
for p, t, dx, dy in ((A, "A", -14, 6), (B, "B", 14, 6), (C, "C", -14, 14), (D, "D", 0, -12)):
    f.circle_px(*f.p3(*p), 5, fill="#fff", c=INK, w=2); f.text3(p, t, dx=dx, dy=dy, b=True)
f.text_px(30, 30, "Tetrahedral space truss", a="start", c=INK, sz=14, b=True)
f.text_px(30, 50, "m = 6 members, j = 4 joints, r = 6 reaction components", a="start", c=GRY, sz=13)
f.save("p4-7-space-truss")

# ---- Ch6 P1: circle
f = Fig(520, 340, sc=3, ox=230, oy=175)
f.circle(0, 0, 50, fill=FILL, c=INK, w=2.5)
f.line(-62, 0, 62, 0, c=AX, w=1.5, d="10,4,2,4"); f.text(62, 0, "x (diameter)", dx=8, dy=4, a="start", c=AX, sz=12, i=True)
f.arrow(0, 0, 35.4, 35.4, c=BLUE, w=2.2); f.text(18, 18, "r = 50 mm", dx=12, dy=-6, a="start", c=BLUE, sz=13)
f.dot(0, 0, r=4, c=AX)
f.save("p6-1-circle")

# ---- Ch6 P4: rectangle 100 x 200
f = Fig(480, 440, sc=1.5, ox=140, oy=390)
f.rect(0, 0, 100, 200, fill=FILL, c=INK, w=2.5)
f.line(-20, 100, 125, 100, c=AX, w=1.5, d="10,4,2,4"); f.text(125, 100, "x̄", dx=8, dy=4, a="start", c=AX, i=True, sz=13)
f.dot(50, 100, r=4, c=AX)
f.dim(0, 0, 100, 0, "b = 100 mm", off=28); f.dim(0, 0, 0, 200, "h = 200 mm", off=-34)
f.save("p6-4-rectangle")

# ---- Ch6 P7: principal axes (given values)
f = Fig(600, 440, sc=1, ox=300, oy=270)
f.arrow(-190, 0, 190, 0, c=GRY, w=1.6, head=9); f.arrow(0, -150, 0, 160, c=GRY, w=1.6, head=9)
f.text(190, 0, "x", dx=10, dy=5, c=GRY, i=True); f.text(0, 160, "y", dy=-8, c=GRY, i=True)
t1 = math.radians(-18.43); t2 = math.radians(71.57)
f.arrow(0, 0, 175 * math.cos(t1), 175 * math.sin(t1), c=GRN, w=3); f.line(0, 0, -150 * math.cos(t1), -150 * math.sin(t1), c=GRN, w=2, d="6,4")
f.arrow(0, 0, 150 * math.cos(t2), 150 * math.sin(t2), c=RED, w=3); f.line(0, 0, -120 * math.cos(t2), -120 * math.sin(t2), c=RED, w=2, d="6,4")
f.text(175 * math.cos(t1), 175 * math.sin(t1), "1", dx=12, dy=12, c=GRN, b=True, sz=16); f.text(150 * math.cos(t2), 150 * math.sin(t2), "2", dx=12, dy=0, c=RED, b=True, sz=16)
f.angle(0, 0, 70, 0, -18.43); f.text(0, 0, "α_{p}", dx=100, dy=24, c=GRY, sz=13)
f.dot(0, 0)
f.text_px(24, 30, "Given: I_{x} = 10, I_{y} = 2, I_{xy} = 3   (×10^{6} mm^{4})", a="start", c=INK, sz=13)
f.text_px(24, 52, "Find the principal moments and the angle α_{p} to the axis of I_{max}.", a="start", c=GRY, sz=13)
f.save("p6-7-principal-axes")
