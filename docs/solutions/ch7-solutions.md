# Chapter 7 – Worked Solutions

[Back to Chapter 7](/chapters/ch7-friction#tutorial-problems).

## Problem 1: Starting and sliding force

![A 30 kg crate on a floor pushed horizontally by a force P, with friction, weight and normal force.](../chapters/img/p7-1-crate-push.svg)

**Step 1: Normal force.** On a horizontal floor with only $P$ horizontal, $N = W = 30(9.81) = 294.3$ N.

**Step 2: To start moving** (impending slip): $P = F_{\max} = \mu_sN = 0.45(294.3) = 132$ N.

**Step 3: To keep moving at constant speed:** $P = \mu_kN = 0.35(294.3) = 103$ N.

**Answer: 132 N to start, 103 N to keep it moving.** The force needed drops once sliding begins because $\mu_k < \mu_s$.

## Problem 2: Angle of repose

![A block on a 22 degree incline that is just starting to slide.](../chapters/img/p7-2-repose.svg)

Along the incline at impending slip: $W\sin\theta = \mu_sN$ and $N = W\cos\theta$. Dividing,

$$
\mu_s = \tan\theta = \tan 22^\circ = 0.40
$$

## Problem 3: Slide or tip?

![A crate 0.8 m wide and 1.2 m tall pushed at a height of 1.0 m, to decide whether it slides or tips.](../chapters/img/p7-3-slide-or-tip.svg)

**Slipping:** $P_{\text{slip}} = \mu_sW = 0.5\,W$.

**Tipping** about the lower right edge (the normal force has moved to that edge). Moments about that edge:

$$
P\,h = W\left(\frac{0.8}{2}\right) \;\Rightarrow\; P_{\text{tip}} = \frac{0.4\,W}{1.0} = 0.4\,W
$$

Since $0.4W < 0.5W$, the crate **tips first**. For a lower push height, for example $h = 0.6$ m, $P_{\text{tip}} = 0.67\,W$ and the crate would slide first.

## Problem 4: Ladder with no person

![A 5 m ladder against a smooth wall with no person on it, showing the reactions at the wall and the floor.](../chapters/img/p7-4-ladder-empty.svg)

**Step 1: Floor normal force.** $N_f = 200$ N.

**Step 2: Moments about the foot.** The 5 m ladder with the wall at 4 m height has horizontal extent 3 m; its weight acts 1.5 m from the foot:

$$
N_w(4) = 200(1.5) \;\Rightarrow\; N_w = 75\ \text{N}
$$

**Step 3: Friction required.** $\sum F_x = 0$: $F = N_w = 75$ N.

**Step 4: Check.** $F_{\max} = \mu_sN_f = 0.4(200) = 80$ N. Since $75 < 80$, the ladder is stable, but only just.

## Problem 5: Square-thread screw

![Unwrapped screw thread drawn as a right triangle with base 2 pi r, height equal to the lead L, and lead angle alpha.](../chapters/img/p7-5-screw-thread.svg)

**Step 1: Angles.**

$$
\alpha = \tan^{-1}\frac{L}{2\pi r} = \tan^{-1}\frac{6}{2\pi(15)} = 3.64^\circ, \qquad \phi = \tan^{-1}(0.2) = 11.31^\circ
$$

**Step 2: Raising the load.**

$$
M = Wr\tan(\alpha + \phi) = 5000(0.015)\tan(14.95^\circ) = 20.0\ \text{N·m}
$$

**Step 3: Self-locking?** Since $\phi = 11.3^\circ > \alpha = 3.64^\circ$, the screw is **self-locking**: the load will not drive the screw backwards.

**Step 4: Lowering the load.**

$$
M = Wr\tan(\phi - \alpha) = 75\tan(7.67^\circ) = 10.1\ \text{N·m}
$$

## Problem 6: Wedge (15°)

![A 15 degree wedge driven under a block in smooth guides carrying a 3000 N load, with a horizontal force P.](../chapters/img/p7-6-wedge.svg)

Use the same arrangement as Worked Example 7.2.

**Step 1: Friction angle.** $\phi = \tan^{-1}(0.2) = 11.31^\circ$.

**Step 2: Block (vertical equilibrium).** The wedge reaction on the block is inclined at $\phi$ from the normal, giving a vertical balance with $W = 3000$ N.

**Step 3: Wedge (horizontal equilibrium).** Combining the block and floor contributions:

$$
P = W\left[\tan(\theta + \phi) + \tan\phi\right] = 3000\left[\tan(26.31^\circ) + 0.2\right] = 3000(0.4944 + 0.2) = 2083\ \text{N}
$$

**Answer: $P \approx 2.08$ kN.**
