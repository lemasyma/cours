---
title:          "PRST: Seance 5"
date:           2021-03-24 14:30
categories:     [Image S8, PRST]
tags:           [Image, SCIA, PRST, S8,  loi, intervalle, confiance]
description: Seance 5
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/B1G7eT_Vu)

- $X_1$ suit une loi normale
- $S_n^{2*}:=\frac{1}{n}\sum_{i=1}^n(X_i-m)^2$
- $\frac{nS_n^{2*}}{\sigma^2}$ suit une loi $\mathcal X^2(n)$

<div class="alert alert-danger" role="alert" markdown="1">
**A connaitre**
$$
\begin{aligned}
X_i&\sim\mathcal N(m,\sigma^2)\\
X_i-m&\sim\mathcal N(0,\sigma^2)\\
\frac{X_i-m}{\sigma}&\sim\mathcal N(0,1)
\end{aligned}
$$
</div>

$$
\sum_{i=1}^n\frac{(X_i-m)^2}{\sigma^2}\sim\mathcal X^2(n)\\
S_n^{2*}=\frac{1}{n}\sum_{i=1}^n(X_i-m)^2\\
\frac{nS_n^{2*}}{\sigma^2}\sim\mathcal X^2(n)\\
\mathcal X^2_{\frac{\alpha}{2}} \le \frac{nS_n^{2*}}{\sigma^2} \le\mathcal X^2_{1-\frac{\alpha}{2}}\\
\frac{1}{\mathcal X^2_{1-\frac{\alpha}{2}}}\le\frac{\sigma^2}{nS_n^{2*}}\le \frac{1}{\mathcal X^2_{\frac{\alpha}{2}}}\\
\frac{nS_n^{2*}}{\mathcal X^2_{1-\frac{\alpha}{2}}}\le\sigma^2\le\frac{nS_n^{2*}}{\mathcal X^2_{\frac{\alpha}{2}}}
$$

<div class="alert alert-warning" role="alert" markdown="1">
$$
P(\mathcal X^2_{\frac{\alpha}{2}} \le \frac{nS_n^{2*}}{\sigma^2} \le\mathcal X^2_{1-\frac{\alpha}{2}}) = 1 - \alpha
$$

La loi $\mathcal X^2$ **n'est pas symetrique**.
</div>

<div class="alert alert-info" role="alert" markdown="1">
*L'intervalle de confiance* au niveau $1-\alpha$ pour la variance $\sigma^2$ est:

$$
[\frac{nS_n^{2*}}{\mathcal X^2_{1-\frac{\alpha}{2}}};\frac{nS_n^{2*}}{\mathcal X^2_{\frac{\alpha}{2}}}]
$$

</div>

- $X_1$ suit une loi normal
- $\bar X_n$ est un estimateur sans biais de $m$
- $S_n^2:=\frac{1}{n-1}\sum_{i=1}^n(X_i-\bar X_n)^2$
- $\frac{(n-1)S_n^2}{\sigma^2}$ suit une loi $\mathcal X^2(n-1)$
- $P(\mathcal X^2_{\frac{\alpha}{2}} \le \frac{nS_n^{2*}}{\sigma^2} \le\mathcal X^2_{1-\frac{\alpha}{2}}) = 1 - \alpha$

<div class="alert alert-info" role="alert" markdown="1">
*L'intervalle de confiance* au niveau $1-\alpha$ pour la variance $\sigma^2$ est:

$$
[(n-1)\frac{s_n^{2}}{\mathcal X^2_{1-\frac{\alpha}{2}}};(n-1)\frac{s_n^{2}}{\mathcal X^2_{\frac{\alpha}{2}}}]
$$

</div>