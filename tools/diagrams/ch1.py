from figlib import *
import math

def unit(v):
    L = math.sqrt(sum(c * c for c in v)); return tuple(c / L for c in v)

def arc3(f, uA, uB, r, n=24, c=GRY):
    uA, uB = unit(uA), unit(uB)
    pts = []
    for k in range(n + 1):
        t = k / n
        v = unit(tuple((1 - t) * a + t * b for a, b in zip(uA, uB)))
        pts.append(f.p3(*(r * c_ for c_ in v)))
    f.poly_px(pts, c=c, w=1.5, close=False)
    mid = unit(tuple(a + b for a, b in zip(uA, uB)))
    return f.p3(*(r * 1.35 * c_ for c_ in mid))

# ---- Example 1.1
f = Fig(560, 330, sc=2.2, ox=200, oy=285)
f.arrow(-55, 0, 125, 0, c=GRY, w=1.5, head=8); f.arrow(0, 0, 0, 118, c=GRY, w=1.5, head=8)
f.text(125, 0, "x", dx=10, dy=5, c=GRY, i=True); f.text(0, 118, "y", dy=-8, c=GRY, i=True)
Ax, Ay, Bx, By, Rx, Ry = 86.6, 50, -42.43, 42.43, 44.18, 92.43
f.line(Ax, Ay, Rx, Ry, c=GRY, w=1.2, d="5,4"); f.line(Bx, By, Rx, Ry, c=GRY, w=1.2, d="5,4")
f.arrow(0, 0, Ax, Ay); f.arrow(0, 0, Bx, By); f.arrow(0, 0, Rx, Ry, c=GRN, w=3)
f.text(Ax, Ay, "A = 100 N", dx=8, dy=16, a="start", c=RED)
f.text(Bx, By, "B = 60 N", dx=-4, dy=-8, a="end", c=RED)
f.text(Rx, Ry, "R = 102.4 N", dx=10, dy=-4, a="start", c=GRN)
f.angle(0, 0, 60, 0, 30, "30°", lr=76)
f.angle(0, 0, 100, 0, 64.4, "", c=GRN); f.text(0, 0, "64.4°", dx=98, dy=-98, c=GRN, sz=13)
f.angle(0, 0, 30, 0, 135)
f.text(0, 0, "135°", dx=-52, dy=-24, c=GRY, sz=13)
f.dot(0, 0)
f.save("ex1-1-add-2d")

# ---- Example 1.2
f = Fig3(520, 360, sc=19, ox=250, oy=305)
f.axes3((5, 7, 14))
f.line3((0, 0, 0), (0, -7, 0), c=GRY, w=1.5, d="4,3")
A, B = (3, 4, 12), (2, -6, 3)
f.arrow3((0, 0, 0), A); f.arrow3((0, 0, 0), B)
f.text3(A, "A = 3i + 4j + 12k", dx=10, dy=0, a="start", c=RED)
f.text3(B, "B = 2i − 6j + 3k", dx=-6, dy=16, a="end", c=RED)
mx, my = arc3(f, A, B, 6)
f.text_px(mx, my + 4, "θ", c=GRY, sz=15, i=True)
f.dot3((0, 0, 0))
f.save("ex1-2-angle-3d")

# ---- Example 1.3
f = Fig3(560, 360, sc=34, ox=260, oy=120)
f.axes3((4.5, 4.5, 3))
r = (2, 3, -1); F = (1.4, 0.7, -2.1); P = r
tip = tuple(a + b for a, b in zip(P, F))
M = (-2.4, 1.2, -1.2)
f.arrow3((0, 0, 0), r, c=INK, w=2.5)
f.arrow3(P, tip, c=RED, w=3)
f.arrow3((0, 0, 0), M, c=GRN, w=3)
f.dot3((0, 0, 0)); f.dot3(P)
f.text3((0, 0, 0), "O", dx=-12, dy=-6, c=INK)
f.text3(r, "r", dx=-12, dy=14, c=INK, i=True, b=True)
f.text3(tip, "F", dx=12, dy=4, c=RED, i=True, b=True)
f.text3(M, "M_{O}", dx=14, dy=16, c=GRN, b=True)
f.text_px(24, 304, "r = (2, 3, −1) m", a="start", c=INK, sz=13)
f.text_px(24, 324, "F = (20, 10, −30) N", a="start", c=RED, sz=13)
f.text_px(24, 344, "M_{O} = r × F = (−80, 40, −40) N·m   (F and M_{O} not to scale)", a="start", c=GRN, sz=13)
f.save("ex1-3-moment-3d")

# ---- Tutorial 1: 2D addition
f = Fig(520, 330, sc=2.3, ox=60, oy=205)
f.arrow(-5, 0, 190, 0, c=GRY, w=1.5, head=8); f.arrow(0, -30, 0, 100, c=GRY, w=1.5, head=8)
A = (91.93, 77.13); B = (72.5, -33.81); R = (164.43, 43.32)
f.line(*A, *R, c=GRY, w=1.2, d="5,4"); f.line(*B, *R, c=GRY, w=1.2, d="5,4")
f.arrow(0, 0, *A); f.arrow(0, 0, *B); f.arrow(0, 0, *R, c=GRN, w=3)
f.text(*A, "120 N", dx=-4, dy=-8, a="end", c=RED)
f.text(*B, "80 N", dx=8, dy=14, a="start", c=RED)
f.text(*R, "R = ?", dx=10, dy=-6, a="start", c=GRN)
f.angle(0, 0, 55, 0, 40, "40°", lr=72); f.angle(0, 0, 70, 0, -25, "25°", lr=86)
f.dot(0, 0)
f.save("p1-1-add-2d")

# ---- Tutorial 2: three forces
f = Fig(460, 330, sc=3.4, ox=205, oy=190)
f.arrow(-55, 0, 50, 0, c=GRY, w=1.5, head=8); f.arrow(0, -35, 0, 50, c=GRY, w=1.5, head=8)
f.arrow(0, 0, 30, 0); f.arrow(0, 0, 0, 40); f.arrow(0, 0, -43.3, -25)
f.text(30, 0, "P = 30 N", dy=18, c=RED); f.text(0, 40, "Q = 40 N", dx=10, dy=0, a="start", c=RED)
f.text(-43.3, -25, "S = 50 N", dx=0, dy=18, c=RED)
f.angle(0, 0, 30, 0, 210); f.text(0, 0, "210°", dx=-44, dy=-38, c=GRY, sz=13)
f.dot(0, 0)
f.save("p1-2-add-2d")

# ---- Tutorial 3: 2D dot product
f = Fig(460, 340, sc=20, ox=60, oy=190)
f.arrow(-1, 0, 14, 0, c=GRY, w=1.5, head=8); f.arrow(0, -7, 0, 9.5, c=GRY, w=1.5, head=8)
f.arrow(0, 0, 6, 8); f.arrow(0, 0, 12, -5)
f.text(6, 8, "A = (6, 8)", dx=10, dy=4, a="start", c=RED); f.text(12, -5, "B = (12, −5)", dx=-4, dy=20, a="end", c=RED)
f.angle(0, 0, 50, -22.62, 53.13); f.text(0, 0, "θ", dx=66, dy=-2, c=GRY, i=True, sz=15)
f.dot(0, 0)
f.save("p1-3-dot-2d")

# ---- Tutorial 4: 3D dot (force along a pipe)
f = Fig3(620, 330, sc=20, ox=330, oy=290)
f.axes3((4, 7, 14))
u = (4, 6, 12)
f.line3((0, 0, 0), u, c="#cbd5e1", w=10)
f.arrow3((0, 0, 0), u, c=GRY, w=2, head=9)
Fv = (6, -4, 12)
f.arrow3((0, 0, 0), Fv, c=RED, w=3)
f.text3(u, "pipe axis, u = (2i + 3j + 6k)/7", dx=14, dy=-2, a="start", c=GRY, sz=12)
f.text3(Fv, "F = (30, −20, 60) N", dx=-8, dy=-6, a="end", c=RED)
mx, my = arc3(f, u, Fv, 5)
f.text_px(mx, my + 4, "θ", c=GRY, sz=15, i=True)
f.dot3((0, 0, 0))
f.save("p1-4-dot-3d")

# ---- Tutorial 5: moment, cross product
f = Fig3(560, 380, sc=40, ox=230, oy=270)
f.axes3((3.5, 3.5, 4.2))
r = (1, 2, 3); F = (3.2, -0.8, 1.6)
tip = tuple(a + b for a, b in zip(r, F))
f.arrow3((0, 0, 0), r, c=INK, w=2.5); f.arrow3(r, tip, c=RED, w=3)
f.dot3((0, 0, 0)); f.dot3(r)
f.text3((0, 0, 0), "O", dx=-12, dy=-6)
f.text3(r, "r", dx=-14, dy=-4, i=True, b=True)
f.text3(tip, "F", dx=12, dy=4, c=RED, i=True, b=True)
f.text_px(24, 330, "r = (1, 2, 3) m", a="start", c=INK, sz=13)
f.text_px(24, 350, "F = (4, −1, 2) kN   (F drawn to a reduced scale)", a="start", c=RED, sz=13)
f.text_px(24, 24, "M_{O} = r × F", a="start", c=GRY, sz=13)
f.save("p1-5-moment-3d")
