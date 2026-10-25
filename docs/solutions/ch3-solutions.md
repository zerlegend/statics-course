# Chapter 3 – Worked Solutions

[Back to Chapter 3](/chapters/ch3-equilibrium#tutorial-problems).

## Problem 1: Unknowns at supports (2D)

![Three 2D support types: a pin with two unknown reactions, a roller with one, and a fixed support with two forces and a couple.](../chapters/img/p3-1-support-types.svg)

A **pin** prevents translation in both directions, so it has 2 unknown force components. A **roller** resists only the force normal to its surface, so it has 1 unknown. A **fixed support** prevents translation and rotation, so it has 2 force components and 1 couple (3 unknowns).

## Problem 2: Beam with two point loads

![A 6 m simply supported beam with a 10 kN load at 2 m and a 20 kN load at 5 m from the pin support.](../chapters/img/p3-2-beam-loads.svg)

**Step 1: FBD.** Unknowns $A_x$, $A_y$, $B_y$.

**Step 2: Moments about $A$.**

$$
\sum M_A = 0:\quad 6B_y - 10(2) - 20(5) = 0 \;\Rightarrow\; B_y = \frac{120}{6} = 20\ \text{kN}
$$

**Step 3: Forces.** $\sum F_y = 0$: $A_y = 30 - 20 = 10$ kN. $\sum F_x = 0$: $A_x = 0$.

**Check (moments about $B$):** $10(6) - 10(4) - 20(1) = 0$ ✓.

## Problem 3: Joint held by two cables

![Joint A held by a horizontal cable AC and a cable AB at 60 degrees above the horizontal, carrying a 500 N weight.](../chapters/img/p3-3-two-cables.svg)

$$
\sum F_y = 0:\quad T_{AB}\sin 60^\circ - 500 = 0 \;\Rightarrow\; T_{AB} = 577\ \text{N}
$$

$$
\sum F_x = 0:\quad T_{AB}\cos 60^\circ - T_{AC} = 0 \;\Rightarrow\; T_{AC} = 289\ \text{N}
$$

**Answer: $T_{AB} = 577$ N, $T_{AC} = 289$ N.**

## Problem 4: Cantilever

![A 3 m cantilever beam fixed at a wall with a 4 kN downward load at the free end and the unknown support reactions.](../chapters/img/p3-4-cantilever.svg)

$$
\sum F_y = 0:\quad A_y - 4 = 0 \;\Rightarrow\; A_y = 4\ \text{kN}\uparrow, \qquad \sum F_x = 0:\quad A_x = 0
$$

$$
\sum M_A = 0:\quad M_A - 4(3) = 0 \;\Rightarrow\; M_A = 12\ \text{kN·m (counter-clockwise)}
$$

The load tends to rotate the beam clockwise, so the support must resist with a counter-clockwise couple.

## Problem 5: Equations and unknowns (3D)

![A ball-and-socket joint with three force reactions, and a fixed support in 3D with three force and three couple reactions.](../chapters/img/p3-5-3d-supports.svg)

For a rigid body in 3D there are **6 independent equations** (three force and three moment). A ball-and-socket joint gives **3** unknown force components. A fixed support gives **6** (3 forces and 3 couples).

## Problem 6: Spring

![A 60 N block hanging from a ceiling by a spring of stiffness 2 kN/m.](../chapters/img/p3-6-spring.svg)

At equilibrium the spring force equals the weight: $k\delta = W$.

$$
\delta = \frac{W}{k} = \frac{60}{2000} = 0.030\ \text{m} = 30\ \text{mm}
$$

## Problem 7: Statical determinacy

![A beam supported by a pin at A and rollers at B and C, with no loads shown.](../chapters/img/p3-7-three-supports.svg)

Unknown reactions: pin 2 + roller 1 + roller 1 = **4**. Equilibrium equations for a body in 2D: **3**. Since $4 > 3$, the beam is **statically indeterminate to the first degree**. The reactions cannot be found from statics alone; deformation of the beam must also be considered (Strength of Materials / Structural Analysis).
