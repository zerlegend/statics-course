"""Figures for the sine and cosine laws (Chapter 1)."""
from figlib import *
import math

def pf(w, h):  # pixel-like figure, y measured upward from the bottom
    return Fig(w, h, sc=1, ox=0, oy=h)

def hatch_support(f, x, y, ang_deg):
    """small ceiling pad where a cable is attached (cable leaves toward angle ang_deg)"""
    f.circle(x, y, 5, fill="#fff", c=INK, w=2)
    f.line(x - 14, y + 8, x + 14, y + 8, c=INK, w=2) if False else None

# ---- general triangle + vector triangle
f = pf(720, 322)
f.text_px(110, 26, "Triangle with sides a, b, c", c=INK, sz=14, b=True)
Av, Bv, Cv = (50, 70), (250, 70), (140, 230)
f.poly([Av, Bv, Cv], fill=FILL, c=INK, w=2.5)
f.angle(*Av, 34, 0, 60.6, "", c=GRY); f.text(*Av, "A", dx=44, dy=-8, c=GRY, sz=14, i=True)
f.angle(*Bv, 34, 124.5, 180, "", c=GRY); f.text(*Bv, "B", dx=-44, dy=-8, c=GRY, sz=14, i=True)
f.angle(*Cv, 34, 240.6, 304.5, "", c=GRY); f.text(*Cv, "C", dx=0, dy=54, c=GRY, sz=14, i=True)
f.text(195, 150, "a", dx=12, dy=4, c=INK, sz=16, i=True, b=True); f.text(95, 150, "b", dx=-12, dy=4, c=INK, sz=16, i=True, b=True); f.text(150, 70, "c", dy=22, c=INK, sz=16, i=True, b=True)
f.text_px(150, 280, "Law of sines:  a / sin A = b / sin B = c / sin C", c=INK, sz=13)
f.text_px(150, 300, "Law of cosines:  c^{2} = a^{2} + b^{2} − 2ab cos C", c=INK, sz=13)
# vector part
f.text_px(500, 26, "Adding two vectors", c=INK, sz=14, b=True)
O = (400, 70); th = 70
A_tip = (O[0] + 130 * math.cos(math.radians(20)), O[1] + 130 * math.sin(math.radians(20)))
B_tip = (O[0] + 100 * math.cos(math.radians(20 + th)), O[1] + 100 * math.sin(math.radians(20 + th)))
R_tip = (A_tip[0] + B_tip[0] - O[0], A_tip[1] + B_tip[1] - O[1])
f.line(*A_tip, *R_tip, c=GRY, w=1.3, d="5,4"); f.line(*B_tip, *R_tip, c=GRY, w=1.3, d="5,4")
f.arrow(*O, *A_tip); f.arrow(*O, *B_tip); f.arrow(*O, *R_tip, c=GRN, w=3)
f.text(*A_tip, "A", dx=10, dy=14, c=RED, b=True); f.text(*B_tip, "B", dx=-12, dy=-6, c=RED, b=True); f.text(*R_tip, "R", dx=10, dy=-4, c=GRN, b=True)
f.angle(*O, 46, 20, 20 + th, "", c=GRY); f.text(*O, "θ", dx=52, dy=-40, c=GRY, i=True, sz=15)
f.angle(*A_tip, 30, 20 + th, 200, "", c=GRY); f.text(*A_tip, "γ", dx=-6, dy=-30, c=GRY, i=True, sz=15)
f.text_px(540, 236, "Triangle rule: γ = 180° − θ", c=INK, sz=13)
f.text_px(540, 256, "R² = A² + B² − 2AB cos γ", c=INK, sz=13)
f.text_px(540, 276, "   = A² + B² + 2AB cos θ", c=INK, sz=13)
f.save("ch1-triangle-laws")

# ---- Example 1.4: three panels
f = pf(800, 340)
f.text_px(150, 24, "(a) Two forces, 60° apart", c=INK, sz=14, b=True)
O = (40, 90)
F1 = (O[0] + 160, O[1]); F2 = (O[0] + 60, O[1] + 103.9); Rr = (O[0] + 220, O[1] + 103.9)
f.line(*F1, *Rr, c=GRY, w=1.3, d="5,4"); f.line(*F2, *Rr, c=GRY, w=1.3, d="5,4")
f.arrow(*O, *F1); f.arrow(*O, *F2); f.arrow(*O, *Rr, c=GRN, w=3)
f.text(O[0] + 80, O[1], "F_{1} = 400 N", dx=0, dy=24, c=RED, b=True, sz=13); f.text(*F2, "F_{2} = 300 N", dx=10, dy=-6, c=RED, b=True, a="start", sz=13)
f.text(*Rr, "R = ?", dx=8, dy=-4, a="start", c=GRN, b=True)
f.angle(*O, 36, 0, 60, "", c=GRY); f.text(*O, "60°", dx=44, dy=-34, c=GRY, sz=12)
f.angle(*O, 72, 0, 25.3, "", c=GRN); f.text(*O, "α = ?", dx=84, dy=-14, c=GRN, sz=12, a="start")
f.dot(*O)
# panel b
f.text_px(450, 24, "(b) 500 N load on two cables", c=INK, sz=14, b=True)
ring = (440, 190)
S1 = (ring[0] - 150 * math.cos(math.radians(30)), ring[1] + 150 * math.sin(math.radians(30)))
S2 = (ring[0] + 110 * math.cos(math.radians(45)), ring[1] + 110 * math.sin(math.radians(45)))
for S in (S1, S2):
    f.circle(*S, 6, fill=FILL, c=INK, w=2)
    f.line(S[0] - 16, S[1] + 8, S[0] + 16, S[1] + 8, c=INK, w=3) if False else None
f.line(*ring, *S1, c="#334155", w=2.6); f.line(*ring, *S2, c="#334155", w=2.6)
f.line(ring[0] - 90, ring[1], ring[0] + 90, ring[1], c=GRY, w=1, d="4,4")
f.circle(*ring, 6, fill="#fff", c=INK, w=2)
f.arrow(*ring, ring[0], ring[1] - 95, c=RED, w=3.2); f.text(ring[0], ring[1] - 95, "W = 500 N", dx=0, dy=18, c=RED, b=True)
f.angle(*ring, 56, 150, 180, "", c=GRY); f.text(*ring, "30°", dx=-80, dy=-26, c=GRY, sz=12)
f.angle(*ring, 50, 0, 45, "", c=GRY); f.text(*ring, "45°", dx=66, dy=-16, c=GRY, sz=12)
f.text(*S1, "T_{1}", dx=8, dy=-8, a="start", c=BLUE, b=True, sz=14); f.text(*S2, "T_{2}", dx=-8, dy=-8, a="end", c=BLUE, b=True, sz=14)
# panel c: force triangle
f.text_px(675, 24, "(c) Force triangle", c=INK, sz=14, b=True)
L = (620, 90); Rv = (760, 90); Ap = (L[0] + 102.5 * math.cos(math.radians(60)), L[1] + 102.5 * math.sin(math.radians(60)))
f.arrow(*L, *Rv, c=RED, w=2.8); f.arrow(*Rv, *Ap, c=BLUE, w=2.8); f.arrow(*Ap, *L, c=BLUE, w=2.8)
f.text(690, 90, "W = 500 N", dy=22, c=RED, b=True, sz=13)
f.text(*Ap, "T_{1}", dx=-30, dy=10, c=BLUE, b=True, a="end") if False else f.text((L[0] + Ap[0]) / 2, (L[1] + Ap[1]) / 2, "T_{1}", dx=-18, dy=0, c=BLUE, b=True, a="end")
f.text((Rv[0] + Ap[0]) / 2, (Rv[1] + Ap[1]) / 2, "T_{2}", dx=16, dy=0, c=BLUE, b=True, a="start")
f.text(*L, "60°", dx=28, dy=-16, c=GRY, sz=12); f.text(*Rv, "45°", dx=-30, dy=-16, c=GRY, sz=12); f.text(*Ap, "75°", dx=0, dy=22, c=GRY, sz=12)
f.text_px(675, 318, "(rotated so that W is horizontal)", c=GRY, sz=11)
f.save("ex1-4-force-triangle")

# ---- Problem 6
f = pf(440, 300)
O = (150, 90)
F1 = (O[0] + 200, O[1]); F2 = (O[0] + 120 * math.cos(math.radians(110)), O[1] + 120 * math.sin(math.radians(110)))
f.arrow(*O, *F1); f.arrow(*O, *F2)
f.text(*F1, "70 N", dx=-4, dy=22, c=RED, b=True, a="end"); f.text(*F2, "50 N", dx=-6, dy=-6, a="end", c=RED, b=True)
f.angle(*O, 44, 0, 110, "", c=GRY); f.text(*O, "110°", dx=58, dy=-48, c=GRY, sz=13)
f.text(*O, "R = ?  and its angle from the 70 N force", dx=-110, dy=60, a="start", c=GRN, sz=13)
f.dot(*O)
f.save("p1-6-two-forces-110")

# ---- Problem 7
f = pf(440, 320)
ring = (220, 140)
S1 = (ring[0] - 150 * math.cos(math.radians(30)), ring[1] + 150 * math.sin(math.radians(30)))
S2 = (ring[0] + 130 * math.cos(math.radians(50)), ring[1] + 130 * math.sin(math.radians(50)))
for S in (S1, S2): f.circle(*S, 6, fill=FILL, c=INK, w=2)
f.line(*ring, *S1, c="#334155", w=2.6); f.line(*ring, *S2, c="#334155", w=2.6)
f.line(ring[0] - 100, ring[1], ring[0] + 100, ring[1], c=GRY, w=1, d="4,4")
f.circle(*ring, 6, fill="#fff", c=INK, w=2)
f.arrow(*ring, ring[0], ring[1] - 90, c=RED, w=3.2); f.text(ring[0], ring[1] - 90, "800 N", dx=0, dy=18, c=RED, b=True)
f.angle(*ring, 58, 150, 180, "", c=GRY); f.text(*ring, "30°", dx=-84, dy=-24, c=GRY, sz=12)
f.angle(*ring, 52, 0, 50, "", c=GRY); f.text(*ring, "50°", dx=70, dy=-18, c=GRY, sz=12)
f.text(*S1, "cable A", dx=-2, dy=-12, c=BLUE, b=True, sz=13); f.text(*S2, "cable B", dx=0, dy=-12, c=BLUE, b=True, sz=13)
f.save("p1-7-two-cables")
