# Formula Sheet

A one-page reference grouped by chapter. Vectors are bold.

## Chapter 1: Vectors

$$
\mathbf{A} = A_x\mathbf{i} + A_y\mathbf{j} + A_z\mathbf{k}, \qquad A = \sqrt{A_x^2 + A_y^2 + A_z^2}
$$

$$
\mathbf{u}_A = \frac{\mathbf{A}}{A}, \qquad \cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1
$$

$$
\mathbf{A}\cdot\mathbf{B} = AB\cos\theta = A_xB_x + A_yB_y + A_zB_z, \qquad A_B = \mathbf{A}\cdot\mathbf{u}_B
$$

$$
\mathbf{A}\times\mathbf{B} =
\begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
A_x & A_y & A_z \\
B_x & B_y & B_z
\end{vmatrix}, \qquad |\mathbf{A}\times\mathbf{B}| = AB\sin\theta
$$

$$
\mathbf{F} = m\mathbf{a}, \qquad W = mg, \qquad 1\ \text{N} = 1\ \text{kg·m/s}^2
$$

## Chapter 1 (continued): useful extras

$$
\mathbf{A}\times\mathbf{B} = -\,\mathbf{B}\times\mathbf{A}, \qquad \mathbf{A}\cdot\mathbf{B} = 0 \;\Rightarrow\; \mathbf{A}\perp\mathbf{B}
$$

$$
R = \sqrt{A^2 + B^2 + 2AB\cos\theta} \quad (\theta = \text{angle between } \mathbf{A} \text{ and } \mathbf{B}, \text{ tail to tail})
$$

$$
\text{Law of sines: } \frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}, \qquad \text{Law of cosines: } c^2 = a^2 + b^2 - 2ab\cos C
$$

$$
\text{Lami's theorem (three concurrent forces in equilibrium): } \frac{F_1}{\sin\theta_{23}} = \frac{F_2}{\sin\theta_{31}} = \frac{F_3}{\sin\theta_{12}}
$$

## Chapter 2: Moments and Resultants

$$
\mathbf{M}_O = \mathbf{r}\times\mathbf{F}, \qquad M_O = Fd
$$

$$
\mathbf{M}_O = \sum(\mathbf{r}\times\mathbf{F}) \quad \text{(Varignon's theorem)}
$$

$$
M_\lambda = \boldsymbol{\lambda}\cdot(\mathbf{r}\times\mathbf{F}) \quad \text{(moment about an axis)}
$$

$$
M_{\text{couple}} = Fd, \qquad \mathbf{R} = \sum\mathbf{F}, \qquad \mathbf{M}_O^{R} = \sum\mathbf{M}_O
$$

$$
M_O = x\,F_y - y\,F_x \quad \text{(2D moment, counter-clockwise positive)}, \qquad x\,R_y = M_O \quad \text{(line of action of the resultant)}
$$

$$
\mathbf{F} = F\,\frac{\mathbf{r}_{AB}}{|\mathbf{r}_{AB}|} \quad \text{(force along the line from A to B)}
$$

## Chapter 3: Equilibrium

$$
\sum\mathbf{F} = \mathbf{0}, \qquad \sum\mathbf{M}_O = \mathbf{0}
$$

$$
\text{2D: } \sum F_x = 0, \quad \sum F_y = 0, \quad \sum M_O = 0
$$

$$
\text{3D: } \sum F_x = \sum F_y = \sum F_z = 0, \quad \sum M_x = \sum M_y = \sum M_z = 0
$$

$$
F_{\text{spring}} = k\delta
$$

## Chapter 4: Trusses, Frames and Machines

$$
m + r = 2j \ \text{(plane truss)}, \qquad m + r = 3j \ \text{(space truss)}
$$

Method of joints: $\sum F_x = 0,\ \sum F_y = 0$ at each joint.
Method of sections: $\sum F_x = 0,\ \sum F_y = 0,\ \sum M = 0$ on a cut portion.

## Chapter 4 (continued): quick checks

Zero-force members at an unloaded joint: two non-collinear members, or the third member when two of three are collinear.
Frames: a two-force member carries force along the line joining its pins.

## Chapter 5: Centroids

$$
\bar{x} = \frac{\int x\,dA}{\int dA}, \qquad \bar{y} = \frac{\int y\,dA}{\int dA}
$$

$$
\bar{x} = \frac{\int x\,dL}{\int dL}, \qquad \bar{x} = \frac{\int x\,dV}{\int dV}
$$

$$
\bar{X} = \frac{\sum A_i\bar{x}_i}{\sum A_i}, \qquad \bar{Y} = \frac{\sum A_i\bar{y}_i}{\sum A_i} \quad \text{(composite areas)}
$$

$$
\text{Pappus: } A = 2\pi\bar{y}L, \qquad V = 2\pi\bar{y}A
$$

$$
\text{Triangle (centroid from base): } \bar{y} = \frac{h}{3}, \quad \text{Semicircle: } \bar{y} = \frac{4r}{3\pi}, \quad \text{Quarter circle: } \bar{x} = \bar{y} = \frac{4r}{3\pi}
$$

$$
\text{Holes: use negative area.} \qquad \text{Weight acts at the centroid: } M_R = W\,\bar{X}
$$

## Chapter 6: Area Moments of Inertia

$$
I_x = \int y^2\,dA, \qquad I_y = \int x^2\,dA, \qquad J_O = I_x + I_y
$$

$$
I = \bar{I} + Ad^2 \quad \text{(parallel-axis theorem)}, \qquad k = \sqrt{I/A}
$$

$$
I_{xy} = \int xy\,dA, \qquad \text{Rectangle: } \bar{I}_x = \frac{bh^3}{12}, \quad \text{Circle: } \bar{I}_x = \frac{\pi r^4}{4}
$$

$$
I_{x'} = \frac{I_x + I_y}{2} + \frac{I_x - I_y}{2}\cos 2\alpha - I_{xy}\sin 2\alpha, \qquad
\tan 2\alpha_p = \frac{-2I_{xy}}{I_x - I_y}
$$

$$
I_{\max,\min} = \frac{I_x + I_y}{2} \pm \sqrt{\left(\frac{I_x - I_y}{2}\right)^2 + I_{xy}^2}, \qquad I_{xy} = \bar{I}_{xy} + A\,d_x d_y
$$

## Chapter 7: Friction

$$
F \le \mu_s N \ \text{(static)}, \qquad F_{\max} = \mu_s N, \qquad F = \mu_k N \ \text{(kinetic)}
$$

$$
\tan\phi_s = \mu_s \quad \text{(angle of static friction)}
$$

$$
\text{Incline: impending slip at } \tan\theta = \mu_s
$$

$$
\text{Slip vs tip (width } b \text{, push at height } h\text{): } \; P_{\text{slip}} = \mu_s W, \quad P_{\text{tip}} = \frac{W\,b}{2h}
$$

$$
\text{Wedge (arrangement of Example 7.2): } \; P = W\left[\tan(\theta + \phi) + \tan\phi\right], \qquad \phi = \tan^{-1}\mu
$$

$$
\text{Square-thread screw: } \; \tan\alpha = \frac{L}{2\pi r}, \quad M_{\text{raise}} = Wr\tan(\alpha + \phi), \quad M_{\text{lower}} = Wr\tan(\phi - \alpha)
$$

$$
\text{Self-locking screw: } \phi \ge \alpha
$$

$$
\text{Ladder (smooth wall): } N_f = W_{\text{total}}, \quad N_w = F \le \mu_s N_f, \quad \sum M_{\text{foot}} = 0
$$
