from figlib import *

def joint(f, x, y, label=None, dx=0, dy=0):
    px, py = f.P(x, y)
    f.circle_px(px, py, 5, fill="#fff", c=INK, w=2)
    if label:
        f.text_px(px + dx, py + dy, label, sz=14, b=True)

# ---- Example 4.1: triangular truss
f = Fig(560, 450, sc=60, ox=100, oy=335)
A, B, C = (0, 0), (3, 4), (6, 0)
f.line(*A, *B, w=3.5); f.line(*B, *C, w=3.5); f.line(*A, *C, w=3.5)
f.pin(*A); f.roller(*C)
for p, lab, dx, dy in ((A, "A", -18, 6), (B, "B", 18, -8), (C, "C", 18, 6)):
    joint(f, *p, lab, dx, dy)
f.arrow(3, 5.0, 3, 4.15, c=RED, w=3); f.text(3, 4.9, "30 kN", dx=-14, dy=0, a="end", c=RED, b=True)
f.dim(0, 0, 0, 4, "4 m", off=-34)
f.dim(0, -1.5, 3, -1.5, "3 m", off=0.1); f.dim(3, -1.5, 6, -1.5, "3 m", off=0.1)
f.text(1.2, 2.2, "AB", dx=-16, c=GRY, sz=13); f.text(4.8, 2.2, "BC", dx=16, c=GRY, sz=13); f.text(3, 0, "AC", dy=-8, c=GRY, sz=13)
f.save("ex4-1-truss-joints")

# ---- Example 4.2: Warren truss with section
f = Fig(700, 400, sc=66, ox=70, oy=290)
pts = {"A": (0, 0), "C": (4, 0), "E": (8, 0), "B": (2, 3), "D": (6, 3)}
for a, b in ("AB", "BC", "CD", "DE", "BD", "AC", "CE"):
    f.line(*pts[a], *pts[b], w=3.5)
f.pin(0, 0); f.roller(8, 0)
f.line(3, -0.7, 3, 3.7, c="#7c3aed", w=2, d="8,5")
f.text(3, 3.7, "section", dx=6, dy=-6, a="start", c="#7c3aed", sz=13)
for k, (dx, dy) in {"A": (-18, 6), "C": (-18, 24), "E": (18, 6), "B": (0, -14), "D": (0, -14)}.items():
    joint(f, *pts[k], k, dx, dy)
f.arrow(4, -0.5, 4, -1.6, c=RED, w=3) if False else f.arrow(4, 0, 4, -1.4, c=RED, w=3)
f.text(4, -1.4, "24 kN", dx=12, dy=8, a="start", c=RED, b=True)
f.dim(0, -2.0, 4, -2.0, "4 m", off=0.1); f.dim(4, -2.0, 8, -2.0, "4 m", off=0.1)
f.dim(8, 0, 8, 3, "3 m", off=34)
f.save("ex4-2-truss-section")

# ---- Example 4.3: frame with two-force member
f = Fig(560, 420, sc=70, ox=100, oy=130)
f.wall(0, -3.7, 1.3, side=-1)
f.line(0, 0, 4, 0, c=INK, w=7)
f.line(3, 0, 0, -3, c=GRY, w=4)
for p, lab, dx, dy in (((0, 0), "A", 18, -14), ((4, 0), "C", 18, 22), ((3, 0), "D", 14, 22), ((0, -3), "E", 18, 16)):
    joint(f, *p, lab, dx, dy)
f.arrow(4, 1.2, 4, 0.14, c=RED, w=3); f.text(4, 1.2, "12 kN", dx=12, dy=4, a="start", c=RED, b=True)
f.text(1.5, -1.5, "DE (two-force member)", dx=16, dy=-6, a="start", c=GRY, sz=13)
f.dim(0, 0, 3, 0, "3 m", off=-30); f.dim(3, 0, 4, 0, "1 m", off=-30)
f.dim(0, 0, 0, -3, "3 m", off=26)
f.save("ex4-3-frame")

# ---- Tutorial 4: bracket
f = Fig(520, 390, sc=62, ox=100, oy=330)
f.wall(0, -0.6, 4.8, side=-1)
f.line(0, 0, 3, 4, c=INK, w=5); f.line(0, 4, 3, 4, c=INK, w=5)
joint(f, 0, 0, "A", -18, 6); joint(f, 0, 4, "D", -18, 6); joint(f, 3, 4, "C", 14, -10)
f.arrow(3, 5.0, 3, 4.1, c=RED, w=3); f.text(3, 5.0, "40 kN", dx=12, dy=6, a="start", c=RED, b=True)
f.text(1.5, 2, "strut CA", dx=-10, dy=-4, a="end", c=GRY, sz=13); f.text(1.5, 4, "tie CD", dy=-12, c=GRY, sz=13)
f.dim(0, 0, 3, 0, "run 3 m", off=26); f.dim(3, 0, 3, 4, "rise 4 m", off=30)
f.save("p4-4-bracket")
