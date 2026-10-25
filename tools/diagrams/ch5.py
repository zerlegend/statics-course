from figlib import *
import math

def curve_area(f, fn, x0, x1, n=60, fill=FILL):
    pts = [(x0 + (x1 - x0) * k / n, fn(x0 + (x1 - x0) * k / n)) for k in range(n + 1)]
    f.poly(pts + [(x1, 0), (x0, 0)], fill=fill, c=INK, w=2)

# ---- Example 5.1
f = Fig(560, 430, sc=40, ox=80, oy=375)
f.arrow(-0.4, 0, 5, 0, c=GRY, w=1.5, head=8); f.arrow(0, -0.4, 0, 8.8, c=GRY, w=1.5, head=8)
f.text(5, 0, "x", dx=10, dy=5, c=GRY, i=True); f.text(0, 8.8, "y", dy=-8, c=GRY, i=True)
curve_area(f, lambda x: 0.5 * x * x, 0, 4)
f.rect(2, 0, 2.15, 2, fill="#93c5fd", c=BLUE, w=1.5)
f.dot(2.075, 1, r=3.5, c=BLUE)
f.text(2.15, 1.0, "element dA = y dx", dx=140, dy=-60, a="start", c=BLUE, sz=13) if False else None
f.line(2.075, 1, 1.0, 5.2, c=BLUE, w=1, d="3,3"); f.text(0.3, 5.2, "strip dA = y dx", dx=0, dy=0, a="start", c=BLUE, sz=13); f.text(0.3, 5.2, "x̃ = x, ỹ = y/2", dx=0, dy=18, a="start", c=BLUE, sz=13)
f.dot(3.0, 2.4, r=5, c=GRN); f.line(3.0, 2.4, 0.3, 3.6, c=GRN, w=1, d="3,3"); f.text(0.3, 3.6, "centroid (3.0, 2.4) m", dx=-2, dy=-8, a="start", c=GRN, b=True)
f.text(0.3, 7.6, "y = 0.5 x²", dx=0, a="start", c=INK, i=True, sz=15)
f.dim(0, 0, 4, 0, "4 m", off=28); f.dim(4, 0, 4, 8, "8 m", off=30)
f.save("ex5-1-integration")

# ---- Example 5.2: plate with hole
f = Fig(580, 420, sc=52, ox=70, oy=360)
f.rect(0, 0, 8, 6, fill=FILL, c=INK, w=2.5)
f.circle(5, 3, 1.5, fill="#ffffff", c=INK, w=2.5)
f.dot(4, 3, r=4, c=GRY); f.dot(5, 3, r=4, c=GRY); f.dot(3.83, 3, r=6, c=GRN)
f.line(4, 3, 1.6, 4.6, c=GRY, w=1, d="3,3"); f.text(1.6, 4.6, "centroid of rectangle (4, 3)", dx=-2, dy=-6, a="start", c=GRY, sz=12)
f.text(5, 3, "hole (5, 3)", dy=-24, c=GRY, sz=12)
f.line(3.83, 3, 3.3, 1.65, c=GRN, w=1, d="3,3"); f.text(0.4, 1.4, "X̄ = 3.83 m, Ȳ = 3.00 m", dx=-2, dy=-6, a="start", c=GRN, b=True)
f.dot(0, 0); f.text(0, 0, "O", dx=-14, dy=16)
f.dim(0, 0, 8, 0, "8 m", off=28); f.dim(8, 0, 8, 6, "6 m", off=30)
f.text(5, 4.5, "r = 1.5 m", dy=-4, c=INK, sz=12)
f.text_px(290, 395, "(hole centered at (5, 3) m)", c=GRY, sz=12) if False else None
f.save("ex5-2-plate-hole")

# ---- Example 5.3: Pappus cone
f = Fig(520, 420, sc=62, ox=100, oy=360)
f.poly([(0, 0), (3, 0), (0, 5)], fill=FILL, c=INK, w=2.5)
f.line(0, -0.5, 0, 5.6, c=GRY, w=2, d="9,5"); f.text(0, 5.6, "axis of revolution", dx=8, dy=0, a="start", c=GRY, sz=13)
f.dot(1, 5 / 3, r=5, c=GRN); f.text(1, 5 / 3, "centroid of area", dx=10, dy=18, a="start", c=GRN, sz=12)
f.dim(0, 5 / 3, 1, 5 / 3, "r̄ = 1 m", off=-30) if False else None
f.line(0, 5 / 3, 1, 5 / 3, c=GRN, w=1.5, d="3,3"); f.text(0.5, 5 / 3, "r̄ = 1 m", dy=-8, c=GRN, sz=12)
f.dot(1.5, 2.5, r=5, c=BLUE); f.text(1.5, 2.5, "centroid of slant line", dx=12, dy=-4, a="start", c=BLUE, sz=12)
f.text(1.5, 2.5, "L = 5.83 m, r̄ = 1.5 m", dx=12, dy=14, a="start", c=BLUE, sz=12)
f.dim(0, 0, 3, 0, "3 m", off=28); f.dim(0, 0, 0, 5, "5 m", off=-30)
f.text(0, 0, "", dx=0)
f.save("ex5-3-pappus-cone")

# ---- Tutorial 1: semicircle
f = Fig(420, 300, sc=200, ox=210, oy=230)
f.poly([(0.6 * math.cos(math.radians(a)), 0.6 * math.sin(math.radians(a))) for a in range(0, 181, 4)], fill=FILL, c=INK, w=2.5)
f.axes(-0.75, 0, 0.75, 0.85, "x", "y") if False else None
f.line(-0.75, 0, 0.75, 0, c=GRY, w=1.2, d="5,4")
y = 4 * 0.6 / (3 * math.pi)
f.dot(0, y, r=5, c=GRN); f.text(0, y, "centroid", dx=10, dy=4, a="start", c=GRN, b=True)
f.dim(0, 0, 0, y, "ȳ = ?", off=-34) if False else None
f.line(0, 0, 0, y, c=GRN, w=1.5, d="3,3"); f.text(0, y / 2, "ȳ = ?", dx=-8, a="end", c=GRN, sz=15)
f.dim(-0.6, 0, 0.6, 0, "r = 0.6 m (radius)", off=28) if False else f.dim(0, 0, 0.6, 0, "r = 0.6 m", off=26)
f.save("p5-1-semicircle")

# ---- Tutorial 2: y = sqrt(x)
f = Fig(480, 260, sc=62, ox=70, oy=200)
f.arrow(-0.3, 0, 4.9, 0, c=GRY, w=1.5, head=8); f.arrow(0, -0.2, 0, 2.5, c=GRY, w=1.5, head=8)
f.text(4.9, 0, "x", dx=10, dy=5, c=GRY, i=True); f.text(0, 2.5, "y", dy=-8, c=GRY, i=True)
curve_area(f, lambda x: math.sqrt(x), 0, 4)
f.text(1.2, 1.5, "y = √x", dx=-6, dy=-6, a="end", i=True)
f.dim(0, 0, 4, 0, "4 m", off=26); f.dim(4, 0, 4, 2, "2 m", off=30)
f.save("p5-2-sqrt-curve")

# ---- Tutorial 3: T-shape
f = Fig(460, 330, sc=26, ox=60, oy=275)
f.poly([(0, 6), (5, 6), (5, 0), (7, 0), (7, 6), (12, 6), (12, 8), (0, 8)], fill=FILL, c=INK, w=2.5)
f.arrow(-0.6, 0, 13, 0, c=GRY, w=1.2, head=7) if False else None
f.line(-0.6, 0, 12.8, 0, c=GRY, w=1.2, d="5,4"); f.text(12.8, 0, "y = 0", dx=8, dy=4, a="start", c=GRY, sz=12)
f.dim(0, 8, 12, 8, "12 m", off=-22); f.dim(12, 6, 12, 8, "2 m", off=24); f.dim(12, 0, 12, 6, "6 m", off=24)
f.dim(5, 0, 7, 0, "2 m", off=22)
f.save("p5-3-t-shape")

# ---- Tutorial 4: plate with square hole
f = Fig(460, 395, sc=30, ox=60, oy=325)
f.rect(0, 0, 10, 10, fill=FILL, c=INK, w=2.5); f.rect(5, 3, 9, 7, fill="#ffffff", c=INK, w=2.5)
f.dot(0, 0); f.text(0, 0, "O", dx=-12, dy=16)
f.dot(7, 5, r=3.5, c=GRY); f.text(7, 5, "(7, 5)", dy=-12, c=GRY, sz=12)
f.dim(0, 0, 10, 0, "10 m", off=24); f.dim(10, 0, 10, 10, "10 m", off=28)
f.dim(5, 7, 9, 7, "4 m", off=-18) if False else f.text(7, 3, "4 m × 4 m hole", dy=18, c=INK, sz=12)
f.save("p5-4-plate-square-hole")

# ---- Tutorial 5: L-shaped wire
f = Fig(400, 340, sc=62, ox=90, oy=280)
f.arrow(-0.4, 0, 3.6, 0, c=GRY, w=1.5, head=8); f.arrow(0, -0.3, 0, 4.5, c=GRY, w=1.5, head=8)
f.text(3.6, 0, "x", dx=10, dy=5, c=GRY, i=True); f.text(0, 4.5, "y", dy=-8, c=GRY, i=True)
f.line(0, 4, 0, 0, c=INK, w=5); f.line(0, 0, 3, 0, c=INK, w=5)
f.dim(0, 0, 3, 0, "3 m", off=26); f.dim(0, 0, 0, 4, "4 m", off=-30)
f.save("p5-5-l-wire")

# ---- Tutorial 6: torus
f = Fig(440, 300, sc=100, ox=90, oy=150)
f.line(0, -1.2, 0, 1.2, c=GRY, w=2, d="9,5"); f.text(0, 1.2, "axis", dx=10, dy=4, a="start", c=GRY, sz=13)
f.circle(2, 0, 0.5, fill=FILL, c=INK, w=2.5)
f.dot(2, 0, r=4, c=GRN); f.text(2.5, 0, "r = 0.5 m", dx=10, dy=5, a="start", c=INK, sz=13)
f.dim(0, 0, 2, 0, "2 m", off=-70)
f.line(2, 0, 2.5, 0, c=INK, w=1.2)
f.save("p5-6-torus")
