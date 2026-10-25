# Chapter 1 – Worked Solutions

Try each tutorial problem first. Each solution shows the method, the working and a check. [Back to Chapter 1](/chapters/ch1-vectors#tutorial-problems).

## Problem 1: Adding two 2D vectors

![A 120 N force at 40 degrees above the x-axis and an 80 N force at 25 degrees below it, with the resultant marked as unknown.](../chapters/img/p1-1-add-2d.svg)

**Given:** 120 N at $40^\circ$ above $+x$; 80 N at $25^\circ$ below $+x$. **Find:** the resultant.

**Step 1: Components.**

$$
A_x = 120\cos 40^\circ = 91.93\ \text{N}, \quad A_y = 120\sin 40^\circ = 77.13\ \text{N}
$$

$$
B_x = 80\cos 25^\circ = 72.50\ \text{N}, \quad B_y = -80\sin 25^\circ = -33.81\ \text{N}
$$

**Step 2: Add.** $R_x = 164.43$ N, $R_y = 43.32$ N.

**Step 3: Magnitude and direction.**

$$
R = \sqrt{164.43^2 + 43.32^2} = 170.0\ \text{N}, \qquad \alpha = \tan^{-1}\frac{43.32}{164.43} = 14.8^\circ
$$

**Check:** $R$ is less than $120 + 80 = 200$ N and more than $120 - 80 = 40$ N ✓. **Answer: 170 N at $14.8^\circ$ above $+x$.**

## Problem 2: Three forces at a point

![Three forces at a point: 30 N along +x, 40 N along +y and 50 N at 210 degrees from +x.](../chapters/img/p1-2-add-2d.svg)

**Step 1: Resolve $S$.** $S_x = 50\cos 210^\circ = -43.30$ N, $S_y = 50\sin 210^\circ = -25.00$ N.

**Step 2: Sum.**

$$
R_x = 30 + 0 - 43.30 = -13.30\ \text{N}, \qquad R_y = 0 + 40 - 25.00 = 15.00\ \text{N}
$$

**Step 3: Resultant.** $R = \sqrt{13.30^2 + 15.00^2} = 20.0$ N. The vector is in the second quadrant, so the angle from $+x$ is $180^\circ - \tan^{-1}(15.00/13.30) = 180^\circ - 48.4^\circ = 131.6^\circ$.

**Answer: 20.0 N at $131.6^\circ$ counter-clockwise from $+x$.**

## Problem 3: Angle between 2D vectors

![Vectors A = (6, 8) and B = (12, -5) from the origin with the angle theta between them.](../chapters/img/p1-3-dot-2d.svg)

**Step 1: Dot product and magnitudes.**

$$
\mathbf{A}\cdot\mathbf{B} = (6)(12) + (8)(-5) = 32, \qquad A = 10, \quad B = 13
$$

**Step 2: Angle.**

$$
\cos\theta = \frac{32}{(10)(13)} = 0.2462 \;\Rightarrow\; \theta = 75.8^\circ
$$

**Step 3: Projection of $\mathbf{A}$ on $\mathbf{B}$.**

$$
A_B = \frac{\mathbf{A}\cdot\mathbf{B}}{B} = \frac{32}{13} = 2.46
$$

**Answer: $\theta = 75.8^\circ$, projection 2.46.**

## Problem 4: Force component along a pipe

![3D sketch of force F = (30, -20, 60) N and a pipe axis along (2, 3, 6), with the angle theta between them.](../chapters/img/p1-4-dot-3d.svg)

**Step 1: Component along $\mathbf{u}$.**

$$
F_u = \mathbf{F}\cdot\mathbf{u} = \frac{(30)(2) + (-20)(3) + (60)(6)}{7} = \frac{360}{7} = 51.4\ \text{N}
$$

**Step 2: Angle.** $F = \sqrt{30^2 + 20^2 + 60^2} = 70$ N, so

$$
\cos\theta = \frac{51.4}{70} = 0.7347 \;\Rightarrow\; \theta = 42.8^\circ
$$

**Check:** $\mathbf{u}$ is a unit vector, because $2^2 + 3^2 + 6^2 = 49 = 7^2$ ✓. **Answer: 51.4 N and $42.8^\circ$.**

## Problem 5: Moment by cross product

![3D sketch of position vector r = (1, 2, 3) m and force F = (4, -1, 2) kN acting at its tip.](../chapters/img/p1-5-moment-3d.svg)

**Step 1: Determinant.**

$$
\mathbf{M}_O = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 2 & 3 \\ 4 & -1 & 2 \end{vmatrix}
= (2\cdot 2 - 3(-1))\,\mathbf{i} + (3\cdot 4 - 1\cdot 2)\,\mathbf{j} + (1(-1) - 2\cdot 4)\,\mathbf{k}
$$

$$
\mathbf{M}_O = 7\,\mathbf{i} + 10\,\mathbf{j} - 9\,\mathbf{k}\ \text{kN·m}
$$

**Step 2: Magnitude.** $M_O = \sqrt{49 + 100 + 81} = 15.2$ kN·m. **Step 3: Moment about $z$** is the $\mathbf{k}$ component: $-9$ kN·m.

**Check:** $\mathbf{r}\cdot\mathbf{M}_O = 7 + 20 - 27 = 0$ ✓ (the moment is perpendicular to $\mathbf{r}$).

## Problem 6: Resultant of two forces at 110°

![Two forces, 70 N along the x-axis and 50 N at 110 degrees from it.](../chapters/img/p1-6-two-forces-110.svg)

**Step 1: Interior angle.** The angle between the forces (tail to tail) is $\theta = 110^\circ$, so the angle inside the force triangle is $\gamma = 180^\circ - 110^\circ = 70^\circ$.

**Step 2: Law of cosines.**

$$
R^2 = 70^2 + 50^2 - 2(70)(50)\cos 70^\circ = 7400 - 2394 = 5006 \;\Rightarrow\; R = 70.8\ \text{N}
$$

**Step 3: Law of sines** (the angle $\alpha$ between $R$ and the 70 N force is opposite the 50 N side):

$$
\frac{\sin\alpha}{50} = \frac{\sin 70^\circ}{70.8} \;\Rightarrow\; \sin\alpha = 0.664 \;\Rightarrow\; \alpha = 41.6^\circ
$$

**Check with components:** $R_x = 70 + 50\cos 110^\circ = 52.9$ N, $R_y = 50\sin 110^\circ = 47.0$ N, giving $R = 70.8$ N and $\tan^{-1}(47.0/52.9) = 41.6^\circ$ ✓.

**Answer: 70.8 N at $41.6^\circ$ from the 70 N force, toward the 50 N force.**

## Problem 7: Two cables, law of sines

![An 800 N load hanging from a ring held by cable A at 30 degrees and cable B at 50 degrees.](../chapters/img/p1-7-two-cables.svg)

**Step 1: Directions.** Cable A pulls at $150^\circ$ from $+x$, cable B at $50^\circ$, and the load acts at $270^\circ$. The angles between the lines of action are $100^\circ$ (A and B), $140^\circ$ (B and load) and $120^\circ$ (load and A).

**Step 2: Interior angles of the force triangle** (each is $180^\circ$ minus the angle between the *other* two forces): opposite the load, $180^\circ - 100^\circ = 80^\circ$; opposite $T_A$, $180^\circ - 140^\circ = 40^\circ$; opposite $T_B$, $180^\circ - 120^\circ = 60^\circ$. They add to $180^\circ$ ✓.

**Step 3: Law of sines.**

$$
\frac{800}{\sin 80^\circ} = \frac{T_A}{\sin 40^\circ} = \frac{T_B}{\sin 60^\circ}
$$

$$
T_A = \frac{800\sin 40^\circ}{\sin 80^\circ} = 522\ \text{N}, \qquad T_B = \frac{800\sin 60^\circ}{\sin 80^\circ} = 704\ \text{N}
$$

**Check by components:** horizontal $522\cos 30^\circ = 452$ N and $704\cos 50^\circ = 452$ N; vertical $522\sin 30^\circ + 704\sin 50^\circ = 261 + 539 = 800$ N ✓.

