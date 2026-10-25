# Chapter 5 – Worked Solutions

[Back to Chapter 5](/chapters/ch5-centroids#tutorial-problems).

## Problem 1: Semicircular plate

![A semicircular plate of radius 0.6 m with the unknown centroid distance from the diameter.](../chapters/img/p5-1-semicircle.svg)

By symmetry the centroid lies on the vertical axis of symmetry. From the standard result for a semicircular area:

$$
\bar{y} = \frac{4r}{3\pi} = \frac{4(0.6)}{3\pi} = 0.255\ \text{m above the diameter}
$$

## Problem 2: Area under $y = \sqrt{x}$

![The area under the curve y = square root of x from x = 0 to 4 m.](../chapters/img/p5-2-sqrt-curve.svg)

**Step 1: Element.** Vertical strip $dA = y\,dx$, with $\tilde{x} = x$ and $\tilde{y} = y/2$.

**Step 2: Area.** $A = \int_0^4 x^{1/2}\,dx = \tfrac{2}{3}(4)^{3/2} = \tfrac{16}{3} = 5.333$ m$^2$.

**Step 3: First moments.**

$$
\int\tilde{x}\,dA = \int_0^4 x^{3/2}\,dx = \tfrac{2}{5}(4)^{5/2} = 12.8\ \text{m}^3
$$

$$
\int\tilde{y}\,dA = \int_0^4 \frac{\sqrt{x}}{2}\sqrt{x}\,dx = \tfrac{1}{2}\int_0^4 x\,dx = 4\ \text{m}^3
$$

**Step 4: Centroid.** $\bar{x} = 12.8/5.333 = 2.4$ m and $\bar{y} = 4/5.333 = 0.75$ m.

## Problem 3: T-shaped area

![T-shaped area with a 12 m by 2 m flange on a 2 m by 6 m web.](../chapters/img/p5-3-t-shape.svg)

| Part | $A_i$ (m$^2$) | $\bar{y}_i$ (m) | $A_i\bar{y}_i$ |
|---|---|---|---|
| Web ($2 \times 6$) | 12 | 3 | 36 |
| Flange ($12 \times 2$) | 24 | 7 | 168 |
| **Total** | **36** | | **204** |

$$
\bar{Y} = \frac{204}{36} = 5.67\ \text{m above the bottom of the web}
$$

By symmetry the centroid is on the vertical centerline, 6 m from either edge of the flange.

## Problem 4: Square plate with a square hole

![A 10 m by 10 m square plate with a 4 m by 4 m square hole centered at (7, 5) m.](../chapters/img/p5-4-plate-square-hole.svg)

| Part | $A_i$ (m$^2$) | $\bar{x}_i$ | $\bar{y}_i$ | $A_i\bar{x}_i$ | $A_i\bar{y}_i$ |
|---|---|---|---|---|---|
| Plate | 100 | 5 | 5 | 500 | 500 |
| Hole | $-16$ | 7 | 5 | $-112$ | $-80$ |
| **Total** | **84** | | | **388** | **420** |

$$
\bar{X} = \frac{388}{84} = 4.62\ \text{m}, \qquad \bar{Y} = \frac{420}{84} = 5.00\ \text{m}
$$

## Problem 5: L-shaped wire

![L-shaped wire with a 3 m segment along x and a 4 m segment along y.](../chapters/img/p5-5-l-wire.svg)

For a line, use lengths instead of areas.

| Segment | $L_i$ (m) | $\bar{x}_i$ | $\bar{y}_i$ | $L_i\bar{x}_i$ | $L_i\bar{y}_i$ |
|---|---|---|---|---|---|
| Along $x$ | 3 | 1.5 | 0 | 4.5 | 0 |
| Along $y$ | 4 | 0 | 2 | 0 | 8 |
| **Total** | **7** | | | **4.5** | **8** |

$$
\bar{X} = \frac{4.5}{7} = 0.643\ \text{m}, \qquad \bar{Y} = \frac{8}{7} = 1.143\ \text{m}
$$

## Problem 6: Torus (Pappus)

![A circle of radius 0.5 m whose center is 2 m from a vertical axis of revolution, forming a torus.](../chapters/img/p5-6-torus.svg)

The generating area is a circle: $A_g = \pi(0.5)^2 = 0.7854$ m$^2$. Its centroid is at its centre, $\bar{r} = 2$ m from the axis.

$$
V = 2\pi\bar{r}A_g = 2\pi(2)(0.7854) = 9.87\ \text{m}^3
$$

**Check:** the closed form $2\pi^2 R r^2 = 2\pi^2(2)(0.25) = 9.87$ m$^3$ ✓.
