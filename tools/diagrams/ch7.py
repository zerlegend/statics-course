from figlib import *
import math

def rot(origin, s, h, th):
    """point at s along slope and h above it (slope angle th degrees), eng coords"""
    t = math.radians(th)
    return (origin[0] + s * math.cos(t) - h * math.sin(t), origin[1] + s * math.sin(t) + h * math.cos(t))

def incline(f, th, L=6.0, s0=2.6, bw=1.3, bh=0.8):
    top = (L * math.cos(math.radians(th)), L * math.sin(math.radians(th)))
    f.poly([(0, 0), (L * math.cos(math.radians(th)), 0), top], fill="#f3f4f6", c=INK, w=2.5)
    f.ground(-0.5, L * math.cos(math.radians(th)) + 0.5, 0)
    corners = [rot((0, 0), s0, 0, th), rot((0, 0), s0 + bw, 0, th), rot((0, 0), s0 + bw, bh, th), rot((0, 0), s0, bh, th)]
    f.poly(corners, fill=FILL, c=INK, w=2.5)
    f.angle(L * math.cos(math.radians(th)), 0, 46, 180 - th, 180, f"{th}°", lr=-1) if False else None
    return top

# ---- Example 7.1: block on 20 degree incline
th = 20
f = Fig(580, 380, sc=75, ox=50, oy=330)
incline(f, th)
cen = rot((0, 0), 2.6 + 0.65, 0.4, th); cont = rot((0, 0), 2.6 + 0.65, 0, th)
f.arrow(*cen, cen[0], cen[1] - 0.85, c=RED, w=3); f.text(cen[0], cen[1] - 0.85, "W = 392.4 N", dx=14, dy=6, a="start", c=RED, b=True)
n_tip = rot((0, 0), 2.6 + 0.65, 1.2, th); f.arrow(*cont, *n_tip, c=BLUE, w=3); f.text(*n_tip, "N", dx=-12, dy=-4, c=BLUE, b=True)
f_tip = rot((0, 0), 2.6 + 0.65 + 0.7, 0.0, th); f.arrow(*cont, *f_tip, c=BLUE, w=3, d=None) if False else None
f_t = rot((0, 0), 2.6 + 0.65 + 0.8, 0.12, th); f_s = rot((0, 0), 2.6 + 0.65, 0.12, th)
f.arrow(*f_s, *f_t, c=GRN, w=3); f.text(*f_t, "F (friction, up slope)", dx=10, dy=-4, a="start", c=GRN, b=True)
p_s = rot((0, 0), 2.6 + 1.3, 0.55, th); p_t = rot((0, 0), 2.6 + 1.3 + 0.8, 0.55, th)
f.arrow(*p_s, *p_t, c=RED, w=3); f.text(*p_t, "P (holding force)", dx=10, dy=-8, a="start", c=RED, b=True)
f.angle(6 * math.cos(math.radians(th)), 0, 60, 180 - th, 180, "", c=GRY); f.text(6 * math.cos(math.radians(th)), 0, "20°", dx=-84, dy=-8, c=GRY, sz=13)
f.text_px(30, 28, "μ_{s} = 0.35,  m = 40 kg", a="start", c=GRY, sz=13)
f.save("ex7-1-incline")

# ---- wedge figure
def wedge(name, theta, W, mu, Plabel="P"):
    f = Fig(640, 360, sc=62, ox=130, oy=290)
    Lw = 5.6; H = Lw * math.tan(math.radians(theta))
    f.ground(-1.6, 6.4, 0)
    f.poly([(0, 0), (Lw, 0), (0, H)], fill=FILL, c=INK, w=2.5)
    x1, x2 = 2.1, 3.5
    ys = lambda x: H - x * math.tan(math.radians(theta))
    f.poly([(x1, ys(x1)), (x2, ys(x2)), (x2, 2.6), (x1, 2.6)], fill="#e5e7eb", c=INK, w=2.5)
    f.wall(x1 - 0.15, ys(x1) + 0.02, 3.0, side=-1); f.wall(x2 + 0.15, ys(x2) + 0.02, 3.0, side=1)
    f.arrow(2.8, 3.7, 2.8, 2.65, c=RED, w=3); f.text(2.8, 3.7, f"W = {W} N", dx=14, dy=6, a="start", c=RED, b=True)
    f.arrow(-1.5, 0.35, -0.05, 0.35, c=RED, w=3); f.text(-1.5, 0.35, Plabel, dx=-8, dy=-6, a="end", c=RED, b=True)
    f.angle(Lw, 0, 56, 180 - theta, 180, "", c=GRY); f.text(Lw, 0, f"{theta}°", dx=-96, dy=-12, c=GRY, sz=13)
    f.text(2.8, 1.5, "block", c=INK, sz=13); f.text(0.7, 0.3, "wedge", c=INK, sz=13)
    f.text(x1 - 0.2, 3.1, "smooth guides", dx=-6, a="end", c=GRY, sz=12)
    f.text_px(30, 28, f"μ = {mu} on the wedge–block and wedge–floor surfaces", a="start", c=GRY, sz=13)
    f.save(name)
wedge("ex7-2-wedge", 10, 2000, 0.25)

# ---- ladder figure
def ladder(name, person):
    f = Fig(560, 410, sc=76, ox=110, oy=335)
    f.wall(0, 0, 4.6, side=-1); f.ground(-0.2, 4.0, 0)
    f.line(3, 0, 0, 4, c=INK, w=6)
    f.dot(3, 0); f.dot(0, 4)
    f.arrow(1.5, 2, 1.5, 1.2, c=RED, w=3); f.text(1.5, 1.2, "200 N (ladder)", dx=-8, dy=14, a="end", c=RED, b=True)
    if person:
        s = 2.708; px, py = 3 - 0.6 * s, 0.8 * s
        f.arrow(px, py, px, py - 0.95, c=RED, w=3); f.dot(px, py, r=4, c=RED)
        f.text(px, py - 0.95, "800 N (person at s)", dx=-10, dy=16, a="end", c=RED, b=True)
    f.arrow(0, 4, 0.95, 4, c=BLUE, w=3); f.text(0.95, 4, "N_{w}", dx=8, dy=5, a="start", c=BLUE, b=True)
    f.arrow(3, 0, 3, 1.1, c=BLUE, w=3); f.text(3, 1.1, "N_{f}", dx=10, dy=4, a="start", c=BLUE, b=True)
    f.arrow(3, 0.1, 2.0, 0.1, c=GRN, w=3); f.text(2.0, 0.1, "F", dx=-4, dy=-10, a="end", c=GRN, b=True)
    f.dim(0, 0, 3, 0, "3 m", off=44); f.dim(0, 0, 0, 4, "4 m", off=-36)
    f.text(0.8, 3.0, "5 m", dx=18, dy=-4, a="start", c=GRY, sz=13)
    f.text_px(300, 40, "smooth wall, μ_{s} = 0.4 at the floor", a="start", c=GRY, sz=13)
    f.save(name)
ladder("ex7-3-ladder", True)
ladder("p7-4-ladder-empty", False)

# ---- Tutorial 1: crate pushed on floor
f = Fig(520, 340, sc=100, ox=150, oy=215)
f.ground(-1.2, 3.2, 0)
f.rect(0, 0, 1.4, 1.0, fill=FILL, c=INK, w=2.5); f.text(0.7, 0.5, "30 kg", c=INK, sz=14)
f.arrow(-1.0, 0.5, 0, 0.5, c=RED, w=3); f.text(-1.0, 0.5, "P", dx=-8, dy=5, a="end", c=RED, b=True)
f.arrow(0.7, 0.5, 0.7, -0.0, c=RED, w=0.01) if False else f.arrow(0.7, 1.0, 0.7, 0.0, c="#e59a92", w=0.01) if False else None
f.arrow(0.7, 0.9, 0.7, 1.6, c=RED, w=0.01) if False else None
f.arrow(0.7, 1.7, 0.7, 1.05, c=RED, w=3); f.text(0.7, 1.7, "W", dx=12, dy=4, a="start", c=RED, b=True)
f.arrow(0.7, 0, 0.7, 0.65, c=BLUE, w=3) if False else None
f.arrow(0.7, -0.75, 0.7, -0.05, c=BLUE, w=3); f.text(0.7, -0.75, "N", dx=10, dy=14, a="start", c=BLUE, b=True)
f.arrow(1.4, -0.0, 0.5, 0.0, c=GRN, w=0.01) if False else None
f.arrow(1.2, 0.08, 0.3, 0.08, c=GRN, w=3) if False else None
f.arrow(2.3, 0.1, 1.45, 0.1, c=GRN, w=3); f.text(2.3, 0.1, "F (friction)", dx=6, dy=-8, a="start", c=GRN, b=True)
f.text_px(20, 28, "μ_{s} = 0.45, μ_{k} = 0.35", a="start", c=GRY, sz=13)
f.save("p7-1-crate-push")

# ---- Tutorial 2: angle of repose
th = 22
f = Fig(540, 340, sc=75, ox=50, oy=300)
top = incline(f, th, L=6.2, s0=3.0)
f.angle(6.2 * math.cos(math.radians(th)), 0, 60, 180 - th, 180, "", c=GRY); f.text(6.2 * math.cos(math.radians(th)), 0, "θ = 22° (slipping begins)", dx=-92, dy=-30, a="end", c=GRY, sz=13) if False else f.text(6.2 * math.cos(math.radians(th)), 0, "22°", dx=-84, dy=-8, c=GRY, sz=13)
f.text(3.6 * math.cos(math.radians(th)), 3.6 * math.sin(math.radians(th)), "block just begins to slide", dx=-10, dy=-70, a="end", c=GRY, sz=13)
f.save("p7-2-repose")

# ---- Tutorial 3: crate, slide or tip
f = Fig(560, 360, sc=140, ox=170, oy=300)
f.ground(-1.0, 2.4, 0)
f.rect(0, 0, 0.8, 1.2, fill=FILL, c=INK, w=2.5)
f.arrow(-0.9, 1.0, 0, 1.0, c=RED, w=3); f.text(-0.9, 1.0, "P", dx=-8, dy=5, a="end", c=RED, b=True)
f.arrow(0.4, 0.6, 0.4, -0.0, c=RED, w=3) if False else None
f.dot(0.4, 0.6, r=4, c=RED); f.arrow(0.4, 0.6, 0.4, 0.0, c=RED, w=3); f.text(0.4, 0.3, "W", dx=-10, dy=0, a="end", c=RED, b=True)
f.dim(0, 0, 0.8, 0, "0.8 m", off=28); f.dim(0.8, 0, 0.8, 1.2, "1.2 m", off=30)
f.dim(0, 0, 0, 1.0, "h = 1.0 m", off=-34) if False else f.dim(0, 0, 0, 1.0, "h = 1.0 m", off=-52)
f.text_px(30, 30, "μ_{s} = 0.5. Which happens first: sliding or tipping?", a="start", c=GRY, sz=13)
f.save("p7-3-slide-or-tip")

# ---- Tutorial 5: unwrapped screw thread
f = Fig(520, 280, sc=70, ox=60, oy=200)
f.poly([(0, 0), (5.5, 0), (5.5, 1.0)], fill=FILL, c=INK, w=2.5)
f.dim(0, 0, 5.5, 0, "2π r  (r = 15 mm)", off=28); f.dim(5.5, 0, 5.5, 1.0, "L = 6 mm", off=34)
f.angle(0, 0, 60, 0, 10.3, "", c=GRY); f.text(0, 0, "α", dx=82, dy=-6, c=GRY, i=True, sz=15)
f.text(2.6, 0.7, "unwrapped thread (not to scale)", dx=-10, dy=-8, a="end", c=GRY, sz=12)
f.save("p7-5-screw-thread")

# ---- Tutorial 6: wedge (15 deg)
wedge("p7-6-wedge", 15, 3000, 0.2)
