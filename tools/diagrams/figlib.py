"""Tiny SVG helper for statics diagrams (engineering coordinates, y up)."""
import math, re, os

RED = "#c0392b"    # applied forces
BLUE = "#1f6feb"   # reactions / unknowns
GRN = "#1a7f37"    # results / centroids
GRY = "#6b7280"    # dimensions, construction
INK = "#1f2937"    # structure
FILL = "url(#conc)"   # shaded areas
FONT = "Helvetica, Arial, sans-serif"


DEFS = """<defs>
<pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse"><path d="M24 0H0V24" fill="none" stroke="#eef2f7" stroke-width="1"/></pattern>
<pattern id="conc" width="9" height="9" patternUnits="userSpaceOnUse"><rect width="9" height="9" fill="#d5dfeb"/><circle cx="2" cy="2" r="0.8" fill="#aebccd"/><circle cx="6.5" cy="5" r="0.7" fill="#b9c6d6"/><circle cx="4" cy="7.5" r="0.6" fill="#a4b3c6"/></pattern>
<pattern id="soil" width="10" height="10" patternUnits="userSpaceOnUse"><rect width="10" height="10" fill="#e9dcc6"/><circle cx="2" cy="3" r="1" fill="#c9b390"/><circle cx="7" cy="7" r="0.9" fill="#b89f78"/><circle cx="8" cy="2" r="0.6" fill="#d6c3a2"/></pattern>
<pattern id="brick" width="24" height="12" patternUnits="userSpaceOnUse"><rect width="24" height="12" fill="#c98a6b"/><path d="M0 6H24M12 0V6M0 6V12M24 6V12" stroke="#e8d3c6" stroke-width="1.2" fill="none"/></pattern>
<linearGradient id="steelg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f4f7fb"/><stop offset="1" stop-color="#a9b5c5"/></linearGradient>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#cfe6fb"/><stop offset="1" stop-color="#f5faff"/></linearGradient>
<filter id="sh" x="-10%" y="-10%" width="125%" height="130%"><feDropShadow dx="1.5" dy="2.5" stdDeviation="2" flood-color="#0f172a" flood-opacity="0.22"/></filter>
</defs>"""


def fmt(t):
    t = t.replace("&", "&amp;")
    t = re.sub(r"\^\{(.*?)\}", r'<tspan dy="-5" font-size="10">\1</tspan><tspan dy="5">&#8203;</tspan>', t)
    return re.sub(r"_\{(.*?)\}", r'<tspan dy="4" font-size="10">\1</tspan><tspan dy="-4">&#8203;</tspan>', t)


class Fig:
    def __init__(s, w, h, sc=40, ox=40, oy=None):
        s.w, s.h, s.sc, s.ox = w, h, sc, ox
        s.oy = h - 40 if oy is None else oy
        s.e = []

    # --- coordinates
    def X(s, x): return s.ox + s.sc * x
    def Y(s, y): return s.oy - s.sc * y
    def P(s, x, y): return (s.X(x), s.Y(y))

    # --- pixel primitives
    def raw(s, t): s.e.append(t)

    def line_px(s, x1, y1, x2, y2, c=INK, w=2, d=None):
        if w >= 3.4 and c == INK and not d:   # structural member: bevelled steel look
            s.raw(f'<line x1="{x1 + 1.5:.1f}" y1="{y1 + 2.5:.1f}" x2="{x2 + 1.5:.1f}" y2="{y2 + 2.5:.1f}" stroke="#0f172a" stroke-opacity="0.18" stroke-width="{w}" stroke-linecap="round"/>')
            s.raw(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#1f2937" stroke-width="{w}" stroke-linecap="round"/>')
            s.raw(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#8294ab" stroke-width="{max(1.2, w - 3.2):.1f}" stroke-linecap="round"/>')
            return
        da = f' stroke-dasharray="{d}"' if d else ""
        s.raw(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{c}" stroke-width="{w}"{da} stroke-linecap="round"/>')

    def arrow_px(s, x1, y1, x2, y2, c=RED, w=2.5, d=None, head=10):
        L = math.hypot(x2 - x1, y2 - y1)
        if L < 2:
            return
        ux, uy = (x2 - x1) / L, (y2 - y1) / L
        bx, by = x2 - ux * head, y2 - uy * head
        s.line_px(x1, y1, bx, by, c, w, d)
        k = head * 0.38
        s.raw(f'<polygon points="{x2:.1f},{y2:.1f} {bx - uy * k:.1f},{by + ux * k:.1f} {bx + uy * k:.1f},{by - ux * k:.1f}" fill="{c}"/>')

    def poly_px(s, pts, fill="none", c=INK, w=2, d=None, close=True):
        p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
        da = f' stroke-dasharray="{d}"' if d else ""
        tag = "polygon" if close else "polyline"
        flt = ' filter="url(#sh)"' if (close and fill not in ("none", "#fff", "#ffffff") and not fill.startswith("url(#steel")) else ""
        s.raw(f'<{tag} points="{p}" fill="{fill}" stroke="{c}" stroke-width="{w}"{da} stroke-linejoin="round"{flt}/>')

    def text_px(s, x, y, t, a="middle", c=INK, sz=14, i=False, b=False):
        st = ' font-style="italic"' if i else ""
        wt = ' font-weight="bold"' if b else ""
        s.raw(f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{a}" fill="{c}" font-size="{sz}"{st}{wt}>{fmt(t)}</text>')

    def circle_px(s, x, y, r, fill="none", c=INK, w=2, d=None):
        da = f' stroke-dasharray="{d}"' if d else ""
        s.raw(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}" stroke="{c}" stroke-width="{w}"{da}/>')

    # --- engineering wrappers
    def line(s, x1, y1, x2, y2, c=INK, w=2, d=None):
        s.line_px(*s.P(x1, y1), *s.P(x2, y2), c=c, w=w, d=d)

    def arrow(s, x1, y1, x2, y2, c=RED, w=2.5, d=None, head=10):
        s.arrow_px(*s.P(x1, y1), *s.P(x2, y2), c=c, w=w, d=d, head=head)

    def poly(s, pts, fill="none", c=INK, w=2, d=None, close=True):
        s.poly_px([s.P(x, y) for x, y in pts], fill, c, w, d, close)

    def rect(s, x1, y1, x2, y2, fill="none", c=INK, w=2, d=None):
        s.poly([(x1, y1), (x2, y1), (x2, y2), (x1, y2)], fill, c, w, d)

    def circle(s, x, y, r, fill="none", c=INK, w=2, d=None):
        s.circle_px(*s.P(x, y), r * s.sc, fill, c, w, d)

    def text(s, x, y, t, dx=0, dy=0, a="middle", c=INK, sz=14, i=False, b=False):
        px, py = s.P(x, y)
        s.text_px(px + dx, py + dy, t, a, c, sz, i, b)

    def dot(s, x, y, r=4, c=INK):
        px, py = s.P(x, y)
        s.circle_px(px, py, r, fill=c, c=c, w=1)

    # --- angle / moment arcs (radius in pixels)
    def arc_pts(s, x, y, r, a1, a2, n=40):
        cx, cy = s.P(x, y)
        return [(cx + r * math.cos(math.radians(a1 + (a2 - a1) * k / n)),
                 cy - r * math.sin(math.radians(a1 + (a2 - a1) * k / n))) for k in range(n + 1)]

    def angle(s, x, y, r, a1, a2, label="", lr=None, c=GRY):
        s.poly_px(s.arc_pts(x, y, r, a1, a2), c=c, w=1.5, close=False)
        if label:
            lr = lr or r + 14
            cx, cy = s.P(x, y)
            m = math.radians((a1 + a2) / 2)
            s.text_px(cx + lr * math.cos(m), cy - lr * math.sin(m) + 5, label, c=c, sz=13)

    def moment(s, x, y, r, a1, a2, c=BLUE, label="", lpos=None):
        pts = s.arc_pts(x, y, r, a1, a2)
        s.poly_px(pts[:-1], c=c, w=2.5, close=False)
        a = math.radians(a2)
        sgn = 1 if a2 > a1 else -1
        tx, ty = sgn * -math.sin(a), sgn * -math.cos(a)
        hx, hy = pts[-1]
        s.arrow_px(hx - tx * 6, hy - ty * 6, hx, hy, c=c, w=2.5, head=9)
        if label:
            cx, cy = s.P(x, y)
            lx, ly = lpos if lpos else (0, -r - 8)
            s.text_px(cx + lx, cy + ly, label, c=c, sz=14)

    # --- structure symbols
    def hatch(s, x1, y1, x2, y2, nx, ny, n=8, L=9):
        """hatch marks along pixel line, extending toward (nx, ny) side."""
        for k in range(n + 1):
            t = k / n
            px, py = x1 + (x2 - x1) * t, y1 + (y2 - y1) * t
            s.line_px(px, py, px + nx * L, py + ny * L, c=GRY, w=1.2)

    def ground(s, x1, x2, y, n=None):
        px1, py = s.P(x1, y); px2, _ = s.P(x2, y)
        s.raw(f'<rect x="{min(px1, px2):.1f}" y="{py:.1f}" width="{abs(px2 - px1):.1f}" height="11" fill="url(#soil)"/>')
        s.line_px(px1, py, px2, py, w=2.5)
        s.hatch(px1, py, px2, py, -0.7, 1, n or max(3, int(abs(px2 - px1) / 9)), 10)

    def ceiling(s, x1, x2, y, n=None):
        px1, py = s.P(x1, y); px2, _ = s.P(x2, y)
        s.line_px(px1, py, px2, py, w=2)
        s.hatch(px1, py, px2, py, 0.7, -1, n or max(3, int(abs(px2 - px1) / 9)), 10)

    def wall(s, x, y1, y2, side=-1):
        px, py1 = s.P(x, y1); _, py2 = s.P(x, y2)
        s.line_px(px, py1, px, py2, w=2)
        s.hatch(px, py1, px, py2, side * 1, -0.7, max(3, int(abs(py2 - py1) / 9)), 10)

    def pin(s, x, y):
        px, py = s.P(x, y)
        s.poly_px([(px, py), (px - 12, py + 20), (px + 12, py + 20)], fill="url(#steelg)")
        s.line_px(px - 20, py + 20, px + 20, py + 20, w=2)
        s.hatch(px - 20, py + 20, px + 20, py + 20, -0.7, 1, 5, 9)
        s.circle_px(px, py, 3.5, fill="#fff")

    def roller(s, x, y):
        px, py = s.P(x, y)
        s.poly_px([(px, py), (px - 12, py + 17), (px + 12, py + 17)], fill="url(#steelg)")
        s.circle_px(px - 6, py + 21, 4, fill="url(#steelg)", w=1.6)
        s.circle_px(px + 6, py + 21, 4, fill="url(#steelg)", w=1.6)
        s.line_px(px - 20, py + 25, px + 20, py + 25, w=2)
        s.hatch(px - 20, py + 25, px + 20, py + 25, -0.7, 1, 5, 9)

    def dim(s, x1, y1, x2, y2, label, off=22, c=GRY):
        """Dimension line between two eng points, offset `off` px along the normal (pixel frame)."""
        ax, ay = s.P(x1, y1); bx, by = s.P(x2, y2)
        L = math.hypot(bx - ax, by - ay) or 1
        nx, ny = -(by - ay) / L, (bx - ax) / L
        sg = 1 if off > 0 else -1
        ax2, ay2, bx2, by2 = ax + nx * off, ay + ny * off, bx + nx * off, by + ny * off
        s.line_px(ax, ay, ax2 + nx * 5 * sg, ay2 + ny * 5 * sg, c=c, w=1)
        s.line_px(bx, by, bx2 + nx * 5 * sg, by2 + ny * 5 * sg, c=c, w=1)
        mx, my = (ax2 + bx2) / 2, (ay2 + by2) / 2
        s.arrow_px(mx, my, ax2, ay2, c=c, w=1.2, head=7)
        s.arrow_px(mx, my, bx2, by2, c=c, w=1.2, head=7)
        if abs(ny) >= abs(nx):   # mostly horizontal dimension line
            s.text_px(mx, my + sg * ny * 15 + 4 - (4 if sg * ny > 0 else 0) * 0, label, c=c, sz=13)
        else:                    # mostly vertical
            s.text_px(mx + sg * nx * 8, my + 4, label, a="start" if sg * nx > 0 else "end", c=c, sz=13)

    def axes(s, x0, y0, x1, y1, lx="x", ly="y"):
        s.arrow(x0, y0, x1, y0, c=GRY, w=1.5, head=8)
        s.arrow(x0, y0, x0, y1, c=GRY, w=1.5, head=8)
        s.text(x1, y0, lx, dx=10, dy=5, c=GRY, i=True)
        s.text(x0, y1, ly, dx=0, dy=-8, c=GRY, i=True)

    # --- output
    def svg(s):
        body = "\n".join(s.e)
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {s.w} {s.h}" width="{s.w}" height="{s.h}" '
                f'font-family="{FONT}">\n{DEFS}\n<rect width="{s.w}" height="{s.h}" rx="10" fill="#ffffff"/>'
                f'<rect width="{s.w}" height="{s.h}" rx="10" fill="url(#grid)" stroke="#cbd5e1"/>\n{body}\n</svg>\n')

    def save(s, name, outdir="../../docs/chapters/img"):
        os.makedirs(outdir, exist_ok=True)
        with open(os.path.join(outdir, name + ".svg"), "w") as f:
            f.write(s.svg())


class Fig3(Fig):
    """Oblique 3D view: x toward viewer (down-left), y to the right, z up."""
    def __init__(s, w, h, sc=30, ox=None, oy=None, kx=0.45, kz=0.32):
        super().__init__(w, h, sc, ox if ox is not None else w // 2, oy if oy is not None else h - 50)
        s.kx, s.kz = kx, kz

    def p3(s, x, y, z):
        return (s.ox + s.sc * (y - s.kx * x), s.oy - s.sc * (z - s.kz * x))

    def line3(s, a, b, **k): s.line_px(*s.p3(*a), *s.p3(*b), **k)
    def arrow3(s, a, b, **k): s.arrow_px(*s.p3(*a), *s.p3(*b), **k)
    def dot3(s, a, r=4, c=INK):
        s.circle_px(*s.p3(*a), r, fill=c, c=c, w=1)
    def text3(s, pt, t, dx=0, dy=0, **k):
        px, py = s.p3(*pt)
        s.text_px(px + dx, py + dy, t, **k)

    def axes3(s, L=(4, 4, 4)):
        s.arrow3((0, 0, 0), (L[0], 0, 0), c=GRY, w=1.5, head=8)
        s.arrow3((0, 0, 0), (0, L[1], 0), c=GRY, w=1.5, head=8)
        s.arrow3((0, 0, 0), (0, 0, L[2]), c=GRY, w=1.5, head=8)
        s.text3((L[0], 0, 0), "x", dx=-10, dy=10, c=GRY, i=True)
        s.text3((0, L[1], 0), "y", dx=10, dy=5, c=GRY, i=True)
        s.text3((0, 0, L[2]), "z", dx=0, dy=-8, c=GRY, i=True)
