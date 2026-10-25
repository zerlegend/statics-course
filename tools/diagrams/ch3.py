from figlib import *
import math

# ---- Example 3.1: beam FBD with inclined load
f = Fig(640, 310, sc=58, ox=120, oy=180)
f.line(0, 0, 8, 0, c=INK, w=7)
f.dot(0, 0); f.dot(8, 0)
f.arrow(2.1, 1.2, 3, 0, c=RED, w=3)
f.arrow(2.1, 1.2, 3, 1.2, c="#e59a92", w=2, d="5,3"); f.arrow(3, 1.2, 3, 0, c="#e59a92", w=2, d="5,3")
f.text(2.55, 1.2, "6 kN", dy=-8, c=RED, sz=13); f.text(3, 0.6, "8 kN", dx=8, a="start", c=RED, sz=13)
f.text(2.1, 1.2, "10 kN", dx=-8, a="end", dy=4, c=RED, b=True)
f.arrow(0, 0, -1, 0, c=BLUE, w=3); f.text(-1, 0, "A_{x}", dy=-8, c=BLUE, b=True)
f.arrow(0, -1.1, 0, 0, c=BLUE, w=3); f.text(0, -1.1, "A_{y}", dx=-8, dy=16, a="end", c=BLUE, b=True)
f.arrow(8, -1.1, 8, 0, c=BLUE, w=3); f.text(8, -1.1, "B_{y}", dx=10, dy=16, a="start", c=BLUE, b=True)
f.text(0, 0, "A (pin)", dy=-34, dx=0, c=GRY, sz=12); f.text(8, 0, "B (roller)", dy=-18, c=GRY, sz=12)
f.dim(0, -1.1, 3, -1.1, "3 m", off=26); f.dim(3, -1.1, 8, -1.1, "5 m", off=26)
f.save("ex3-1-beam-fbd")

# ---- Example 3.2: bar, cable, pin
f = Fig(560, 390, sc=62, ox=80, oy=215)
f.wall(0, -2.3, 3.4, side=-1)
yc = 5 * math.tan(math.radians(30))
f.line(0, 0, 5, 0, c=INK, w=7)
f.line(5, 0, 0, yc, c=GRY, w=2.5)
f.dot(0, yc); f.dot(0, 0); f.dot(5, 0)
f.text(0, 0, "A", dx=-16, dy=18); f.text(5, 0, "B", dx=12, dy=-10)
f.text(2.5, yc / 2, "cable", dx=-6, dy=-22, c=GRY, i=True)
f.angle(5, 0, 46, 150, 180, "", c=GRY); f.text(5, 0, "30°", dx=-72, dy=-18, c=GRY, sz=13)
f.arrow(2.5, 0, 2.5, -0.8, c=RED, w=3); f.text(2.5, -0.8, "200 N (weight)", dx=8, dy=14, a="start", c=RED)
f.arrow(5, 0, 5, -1.2, c=RED, w=3); f.text(5, -1.2, "400 N", dx=-8, dy=14, a="end", c=RED)
f.dim(0, -1.8, 2.5, -1.8, "2.5 m", off=0.1); f.dim(2.5, -1.8, 5, -1.8, "2.5 m", off=0.1)
f.save("ex3-2-bar-cable")

# ---- Example 3.3: 3D cables
f = Fig3(600, 420, sc=32, ox=290, oy=300)
D = (0, 0, 0); A = (2, 3, 6); B = (2, -3, 6); C = (-3, 0, 4)
f.axes3((3.5, 4.5, 2.5))
for P_, n in ((A, "A"), (B, "B"), (C, "C")):
    f.line3(D, P_, c=INK, w=2.5); f.dot3(P_, r=5)
f.text3(A, "A(2, 3, 6)", dx=10, dy=-6, a="start"); f.text3(B, "B(2, −3, 6)", dx=-10, dy=-6, a="end")
f.text3(C, "C(−3, 0, 4)", dx=-10, dy=-6, a="end")
f.arrow3(D, (0, 0, -3), c=RED, w=3.2); f.text3((0, 0, -3), "W = 1040 N", dx=12, dy=4, a="start", c=RED, b=True)
f.dot3(D, r=5); f.text3(D, "D", dx=-14, dy=16)
for P_, n in ((A, "T_{A}"), (B, "T_{B}"), (C, "T_{C}")):
    f.text3(tuple(p / 2 for p in P_), n, dx=12 if n == "T_{A}" else -12, dy=4, a="start" if n == "T_{A}" else "end", c=BLUE, b=True)
f.save("ex3-3-cables-3d")

# ---- Tutorial 2: beam with two loads
f = Fig(540, 280, sc=70, ox=50, oy=150)
f.line(0, 0, 6, 0, c=INK, w=7)
f.pin(0, 0); f.roller(6, 0)
f.arrow(2, 1.2, 2, 0, c=RED, w=3); f.text(2, 1.2, "10 kN", dy=-8, c=RED)
f.arrow(5, 1.2, 5, 0, c=RED, w=3); f.text(5, 1.2, "20 kN", dy=-8, c=RED)
f.text(0, 0, "A", dx=-4, dy=-14); f.text(6, 0, "B", dx=4, dy=-14)
f.dim(0, 0, 2, 0, "2 m", off=64); f.dim(2, 0, 5, 0, "3 m", off=64); f.dim(5, 0, 6, 0, "1 m", off=64)
f.save("p3-2-beam-loads")

# ---- Tutorial 3: joint with two cables
f = Fig(520, 360, sc=80, ox=210, oy=235)
f.wall(-2, -1.2, 1.0, side=-1)
Bx, By = 2.0 * math.cos(math.radians(60)), 2.0 * math.sin(math.radians(60))
f.ceiling(0, 2.2, By)
f.line(0, 0, -2, 0, c=GRY, w=2.5); f.line(0, 0, Bx, By, c=GRY, w=2.5)
f.dot(0, 0, r=5)
f.arrow(0, 0, 0, -1.1, c=RED, w=3); f.text(0, -1.1, "500 N", dx=12, dy=4, a="start", c=RED, b=True)
f.text(0, 0, "A", dx=-16, dy=-8); f.text(-2, 0, "C", dx=10, dy=-10, a="start") if False else f.text(-2, 0, "C", dx=-4, dy=-10)
f.text(Bx, By, "B", dx=-16, dy=-8)
f.text(-1, 0, "AC (horizontal)", dy=-10, c=GRY, sz=12); f.text(Bx / 2, By / 2, "AB", dx=-20, dy=-2, c=GRY, sz=12)
f.angle(0, 0, 42, 0, 60, "60°", lr=60)
f.save("p3-3-two-cables")

# ---- Tutorial 4: cantilever FBD
f = Fig(540, 280, sc=70, ox=80, oy=160)
f.wall(0, -1.3, 1.3, side=-1)
f.line(0, 0, 3, 0, c=INK, w=7)
f.arrow(3, 1.3, 3, 0, c=RED, w=3); f.text(3, 1.3, "4 kN", dx=12, dy=4, a="start", c=RED, b=True)
f.arrow(0.3, -1.0, 0.3, 0, c=BLUE, w=3); f.text(0.3, -1.0, "A_{y}", dx=10, dy=14, a="start", c=BLUE, b=True)
f.arrow(0, 0, 0.9, 0, c=BLUE, w=2, d="5,3") if False else None
f.moment(0, 0, 38, 20, 160, c=BLUE); f.text(0, 0, "M_{A}", dx=10, dy=-58, a="start", c=BLUE, b=True)
f.dim(0, 0, 3, 0, "3 m", off=44)
f.save("p3-4-cantilever")

# ---- Tutorial 6: spring and block
f = Fig(300, 340, sc=60, ox=120, oy=300)
f.ceiling(-1, 1, 4.6)
ys = [4.6 - 0.2 * k for k in range(0, 9)]
pts = [(0, 4.6), (0, 4.35)]
for k in range(8):
    pts.append((0.28 if k % 2 == 0 else -0.28, 4.35 - 0.12 * (k + 1)))
pts += [(0, 3.3), (0, 3.1)]
f.poly(pts, c=INK, w=2, close=False)
f.rect(-0.45, 3.1, 0.45, 2.3, fill="#e5e7eb", c=INK)
f.text(0, 2.7, "block", c=INK, sz=13)
f.arrow(0, 2.3, 0, 1.3, c=RED, w=3); f.text(0, 1.3, "W = 60 N", dy=20, c=RED, b=True)
f.text(0.55, 3.85, "k = 2 kN/m", dx=4, a="start", c=GRY, sz=13)
f.save("p3-6-spring")

# ---- Tutorial 7: three supports
f = Fig(580, 220, sc=75, ox=60, oy=100)
f.line(0, 0, 6, 0, c=INK, w=7)
f.pin(0, 0); f.roller(3, 0); f.roller(6, 0)
f.text(0, 0, "A (pin)", dy=-14, c=GRY, sz=12); f.text(3, 0, "B (roller)", dy=-14, c=GRY, sz=12); f.text(6, 0, "C (roller)", dy=-14, c=GRY, sz=12)
f.save("p3-7-three-supports")
