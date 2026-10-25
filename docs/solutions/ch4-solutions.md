# Chapter 4 – Worked Solutions

[Back to Chapter 4](/chapters/ch4-structures#tutorial-problems).

## Problem 1: Determinacy

![Pratt truss with 13 members, 8 joints and 3 support reactions.](../chapters/img/p4-1-truss-13.svg)

$$
m + r = 13 + 3 = 16, \qquad 2j = 2(8) = 16
$$

The count is satisfied, so the truss is statically determinate (provided the members are arranged stably, for example as triangles).

## Problem 2: Rigidity

![Plane truss with 10 members, 7 joints and 3 support reactions, one panel lacking a diagonal.](../chapters/img/p4-2-truss-10.svg)

$$
m + r = 10 + 3 = 13, \qquad 2j = 14
$$

Since $m + r < 2j$, there are too few members, and the truss is **not rigid** (it can deform as a mechanism).

## Problem 3: Zero-force members

![Two unloaded joints: one where two non-collinear members meet, and one where three members meet with two of them collinear.](../chapters/img/p4-3-zero-force.svg)

**(a)** At an unloaded joint with two non-collinear members, equilibrium in the direction perpendicular to one member forces the other member's component to be zero. Hence both members carry zero force.

**(b)** At an unloaded joint with three members where $AE$ and $EC$ are collinear and $ED$ is not, equilibrium perpendicular to the collinear pair gives $F_{ED} = 0$. Equilibrium along the collinear line then gives $F_{AE} = F_{EC}$.

## Problem 4: Method of joints (bracket)

![A bracket with a horizontal tie CD to a wall, a strut CA with run 3 and rise 4, and a 40 kN downward load at C.](../chapters/img/p4-4-bracket.svg)

**Step 1: Geometry.** The strut $CA$ has run 3 and rise 4, so its length is 5 and the unit vector from $A$ to $C$ is $(0.6, 0.8)$. At joint $C$, assume both members in tension: the force of $CA$ on the joint acts toward $A$, direction $(-0.6, -0.8)$; the force of $CD$ acts toward $D$, direction $(-1, 0)$.

**Step 2: Equilibrium of joint $C$.**

$$
\sum F_y = 0:\quad -0.8\,F_{CA} - 40 = 0 \;\Rightarrow\; F_{CA} = -50\ \text{kN}
$$

$$
\sum F_x = 0:\quad -0.6\,F_{CA} - F_{CD} = 0 \;\Rightarrow\; F_{CD} = -0.6(-50) = +30\ \text{kN}
$$

**Answer: $CA$ = 50 kN compression, $CD$ = 30 kN tension.**

## Problem 5: Method of sections (36 kN load)

![Warren truss like Example 4.2 with a 36 kN load at joint C and a section cut.](../chapters/img/p4-5-truss-36.svg)

**Step 1: Reactions.** $\sum M_E = 0$: $8A_y = 36(4) \Rightarrow A_y = 18$ kN.

**Step 2: Section at $x = 3$ m,** left part, all cut members assumed in tension.

**Step 3: $F_{BD}$** (moments about $C$): $-18(4) - 3F_{BD} = 0 \Rightarrow F_{BD} = -24$ kN.

**Step 4: $F_{AC}$** (moments about $B$): $-18(2) + 3F_{AC} = 0 \Rightarrow F_{AC} = +12$ kN.

**Step 5: $F_{BC}$** (vertical forces): $18 - \tfrac{3}{\sqrt{13}}F_{BC} = 0 \Rightarrow F_{BC} = 6\sqrt{13} = 21.6$ kN.

**Answer: $BD$ = 24 kN (C), $BC$ = 21.6 kN (T), $AC$ = 12 kN (T).** These are 1.5 times the values for the 24 kN load, as expected for a linear problem.

## Problem 6: Frame with a two-force strut

![Frame with beam AC, a 45 degree two-force strut DE attached 2 m from A, and a 10 kN load at C.](../chapters/img/p4-6-frame-2m.svg)

**Step 1: Two-force member.** $DE$ is pinned at both ends and carries no load between, so its force acts along $DE$ at $45^\circ$. Let its compressive force push on the beam at $D$ with components $F/\sqrt{2}$ in $x$ and $y$.

**Step 2: Moments about $A$** for beam $AC$:

$$
\frac{F}{\sqrt{2}}(2) - 10(4) = 0 \;\Rightarrow\; \frac{F}{\sqrt{2}} = 20 \;\Rightarrow\; F = 28.3\ \text{kN (compression)}
$$

**Step 3: Pin $A$.** $\sum F_x = 0$: $A_x + 20 = 0 \Rightarrow A_x = -20$ kN. $\sum F_y = 0$: $A_y + 20 - 10 = 0 \Rightarrow A_y = -10$ kN. $A = \sqrt{20^2 + 10^2} = 22.4$ kN.

## Problem 7: Space truss determinacy

![Tetrahedral space truss with joints A, B, C and D and six members.](../chapters/img/p4-7-space-truss.svg)

$$
m + r = 6 + 6 = 12, \qquad 3j = 3(4) = 12
$$

The condition $m + r = 3j$ is satisfied, so the space truss is statically determinate.
