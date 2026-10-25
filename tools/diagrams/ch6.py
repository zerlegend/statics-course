from figlib import *
import math

AX = "#16a34a"

def centroid_axis(f, x1, x2, y, label, side="right"):
    f.line(x1, y, x2, y, c=AX, w=1.5, d="10,4,2,4")
    f.text(x2 if side == "right" else x1, y, label, dx=8 if side == "right" else -8, dy=4, a="start" if side == "right" else "end", c=AX, sz=13, i=True)

# ---- Example 6.1: rectangle, base axis and centroidal axis
f = Fig(620, 430, sc=3.2, ox=190, oy=370)
f.rect(0, 0, 60, 90, fill=FILL, c=INK, w=2.5)
f.line(-20, 0, 95, 0, c=GRY, w=1.5, d="6,4"); f.text(95, 0, "x (base)", dx=8, dy=4, a="start", c=GRY, sz=13, i=True)
centroid_axis(f, -8, 95, 45, "x̄ (centroidal)")
f.rect(0, 60, 60, 63, fill="#93c5fd", c=BLUE, w=1.2)
f.text(60, 61.5, "strip dA = b dy", dx=10, dy=4, a="start", c=BLUE, sz=12) if False else f.line(60, 61.5, 78, 75, c=BLUE, w=1, d="3,3")
f.text(78, 75, "strip dA = b dy", dx=4, dy=0, a="start", c=BLUE, sz=12)
f.text(60, 63, "", dx=0)
f.dim(0, 0, 60, 0, "b = 60 mm", off=30); f.dim(0, 0, 0, 90, "h = 90 mm", off=-52)
f.dim(60, 0, 60, 45, "d = 45 mm", off=-4) if False else None
f.dim(60, 0, 60, 45, "d = 45", off=32)
f.dot(30, 45, r=4, c=AX)
f.save("ex6-1-rectangle")

# ---- Example 6.2: T-section
f = Fig(660, 500, sc=3.2, ox=170, oy=445)
f.poly([(0, 100), (50, 100), (50, 0), (70, 0), (70, 100), (120, 100), (120, 120), (0, 120)], fill=FILL, c=INK, w=2.5)
Yb = 82.73
centroid_axis(f, -25, 150, Yb, "x̄")
f.line(60, -15, 60, 140, c=AX, w=1.5, d="10,4,2,4"); f.text(60, 140, "ȳ", dy=-8, c=AX, i=True, sz=13)
f.dot(60, Yb, r=5, c=AX)
f.dim(0, 120, 120, 120, "120", off=-26)
f.dim(120, 100, 120, 120, "20", off=24); f.dim(120, 0, 120, 100, "100", off=24)
f.dim(50, 0, 70, 0, "20", off=24)
f.dim(0, 0, 0, Yb, "Ȳ = 82.73", off=-34)
f.text(60, 110, "flange", c=GRY, sz=12); f.text(60, 40, "web", c=GRY, sz=12)
f.save("ex6-2-t-section")

# ---- Example 6.3: principal axes
f = Fig(560, 440, sc=1, ox=280, oy=270)
f.arrow(-190, 0, 190, 0, c=GRY, w=1.6, head=9); f.arrow(0, -150, 0, 160, c=GRY, w=1.6, head=9)
f.text(190, 0, "x", dx=10, dy=5, c=GRY, i=True); f.text(0, 160, "y", dy=-8, c=GRY, i=True)
t = math.radians(-26.57)
f.arrow(0, 0, 175 * math.cos(t), 175 * math.sin(t), c=GRN, w=3)
f.arrow(0, 0, -175 * math.cos(t), -175 * math.sin(t), c=GRN, w=3) if False else None
f.line(0, 0, -150 * math.cos(t), -150 * math.sin(t), c=GRN, w=2, d="6,4")
t2 = math.radians(63.43)
f.arrow(0, 0, 150 * math.cos(t2), 150 * math.sin(t2), c=RED, w=3)
f.line(0, 0, -120 * math.cos(t2), -120 * math.sin(t2), c=RED, w=2, d="6,4")
f.text(175 * math.cos(t), 175 * math.sin(t), "1", dx=12, dy=12, c=GRN, b=True, sz=16)
f.text(150 * math.cos(t2), 150 * math.sin(t2), "2", dx=12, dy=0, c=RED, b=True, sz=16)
f.angle(0, 0, 70, 0, -26.57); f.text(0, 0, "26.6°", dx=96, dy=34, c=GRY, sz=13)
f.angle(0, 0, 50, -26.57, 63.43, c="#9ca3af"); f.text(0, 0, "90°", dx=60, dy=-30, c="#9ca3af", sz=12)
f.dot(0, 0)
f.text_px(24, 30, "Given: I_{x} = 9, I_{y} = 3, I_{xy} = 4   (×10^{6} mm^{4})", a="start", c=INK, sz=13)
f.text_px(24, 52, "Axis 1 (green): I_{max} = 11 × 10^{6} mm^{4}, at 26.6° clockwise from x", a="start", c=GRN, sz=13)
f.text_px(24, 74, "Axis 2 (red): I_{min} = 1 × 10^{6} mm^{4}, at 63.4° from x", a="start", c=RED, sz=13)
f.save("ex6-3-principal-axes")

# ---- Tutorial 2: triangle
f = Fig(580, 340, sc=2.3, ox=140, oy=280)
f.poly([(0, 0), (120, 0), (60, 90)], fill=FILL, c=INK, w=2.5)
f.line(0, 0, 120, 0, c=GRY, w=1.5)
centroid_axis(f, -20, 145, 30, "centroidal axis")
f.dim(0, 0, 120, 0, "b = 120 mm", off=28); f.dim(60, 0, 60, 90, "h = 90 mm", off=-6) if False else f.dim(120, 0, 120, 90, "h = 90 mm", off=34) if False else None
f.dim(0, 0, 0, 90, "h = 90 mm", off=-52)
f.text(125, 0, "base", dx=8, dy=-6, a="start", c=GRY, sz=12)
f.save("p6-2-triangle")

# ---- Tutorial 3: hollow rectangle
f = Fig(480, 480, sc=1.1, ox=110, oy=400)
f.rect(0, 0, 200, 300, fill=FILL, c=INK, w=2.5); f.rect(40, 40, 160 - 0, 260, fill="#ffffff", c=INK, w=2.5) if False else f.rect(40, 40, 160, 260, fill="#ffffff", c=INK, w=2.5)
centroid_axis(f, -20, 225, 150, "x̄")
f.dim(0, 0, 200, 0, "200 mm", off=30); f.dim(0, 0, 0, 300, "300 mm", off=-34)
f.dim(40, 260, 160, 260, "120", off=-14) if False else f.text(100, 270, "120 × 220 (hollow)", dy=-4, c=GRY, sz=12)
f.save("p6-3-hollow-rect")

# ---- Tutorial 5: I-section
f = Fig(520, 470, sc=1.75, ox=110, oy=410)
f.poly([(0, 0), (100, 0), (100, 20), (60, 20), (60, 180), (100, 180), (100, 200), (0, 200), (0, 180), (40, 180), (40, 20), (0, 20)], fill=FILL, c=INK, w=2.5)
centroid_axis(f, -8, 108, 100, "x̄", side="left")
f.dim(0, 0, 100, 0, "100", off=26); f.dim(0, 0, 0, 200, "200", off=-34)
f.dim(100, 180, 100, 200, "20", off=24); f.dim(100, 20, 100, 180, "160", off=24) if False else f.dim(100, 20, 100, 180, "160", off=40)
f.dim(40, 100, 60, 100, "20", off=-70) if False else f.text_px(24, 28, "flanges 100 × 20, web 20 thick (dimensions in mm)", a="start", c=GRY, sz=12)
f.save("p6-5-i-section")

# ---- Tutorial 6: rectangle at origin, product of inertia
f = Fig(480, 320, sc=4, ox=70, oy=260)
f.arrow(-6, 0, 80, 0, c=GRY, w=1.5, head=8); f.arrow(0, -6, 0, 55, c=GRY, w=1.5, head=8)
f.text(80, 0, "x", dx=10, dy=5, c=GRY, i=True); f.text(0, 55, "y", dy=-8, c=GRY, i=True)
f.rect(0, 0, 60, 40, fill=FILL, c=INK, w=2.5)
f.dot(30, 20, r=5, c=AX); f.text(30, 20, "centroid (30, 20)", dx=10, dy=-10, a="start", c=AX, sz=13)
f.dim(0, 0, 60, 0, "60 mm", off=26); f.dim(60, 0, 60, 40, "40 mm", off=30)
f.text(0, 0, "O", dx=-12, dy=16)
f.save("p6-6-product-of-inertia")
