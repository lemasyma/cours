---
title:          "PRST: Feuille de revisions"
date:           2021-03-29 10:00
categories:     [Image S8, PRST]
tags:           [Image, SCIA, PRST, S8,  loi, intervalle, confiance]
description: Feuille de revisions
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/r1lvOYyHu)

# Exercice 1
## Question 10

<div class="alert alert-warning" role="alert" markdown="1">
Cet exercice est aussi present sur la feuille pour le 17/03/2021
</div>

La loi du *demi-cercle* de Wigner de parametre $R$ a une densite nulle en dehors de $] − R; R[$. Sur $] − R; R[$, sa densite est donnee par

$$
f(x)=\frac{2}{\pi R^2}\sqrt{R^2-x^2}
$$

Nous admettrons que sa variance est donnee par $\frac{R^2}{4}$.

En deduire un estimateur du parametre $R$ par la methode des moments.

<details markdown="1">
<summary>Solution</summary>

$$
V(X)=\frac{R^2}{4}\\
\Leftrightarrow R^2=4V(X)\\
\Leftrightarrow R=2\sqrt{V(X)}
$$

<div class="alert alert-success" role="alert" markdown="1">

Donc:

$$
\hat R=2\sqrt{S^2}
$$

</div>

$$
S=\frac{1}{n-1}\sum_{i=1}^n(X_i-\bar X)^2
$$

On sait que $E(X)=0$ (symetrie).

En effet, $E(X)=\int_{-R}^Rx\times\frac{2}{\pi R^2}\sqrt{R^2-x^2}dx=0$.

La fonction devient impaire car $\times x$.

On integre une fonction impaire sur l'intervalle $] − R; R[$.

$V(X)=E(X^2)$ donc $E(X^2)=\frac{R^2}{4}$

$$
R=2\sqrt{E(X)}\Rightarrow\hat R=2\sqrt{\frac{1}{n}\sum_{i=1}^nx_i^2}
$$

</details>

## Question 11
Soient $X$ et $Y$ deux variables aleatoires independantes et suivant toutes deux une loi normale centree reduite.
Considerons les variables aleatoires $U = X + 2Y$ et $V = X − 3Y$
1. Montrer que le vecteur aleatoire $(U, V )^T$ est un vecteur gaussien.
2. Les variables aleatoires U et V sont-elles independantes ?

<details markdown="1">
<summary>Solution</summary>

1.

$X$ et $Y$ sont independants $\Rightarrow(X,Y)^T$ vecteur gaussien

$$
\begin{pmatrix}
U\\
V
\end{pmatrix}=
\begin{pmatrix}
1 & 2\\
1&-3
\end{pmatrix}
$$

<div class="alert alert-success" role="alert" markdown="1">
$(U,V)^T$ gaussien comme image d'un vecteur gaussien comme application lineaire
</div>

2.

<div class="alert alert-warning" role="alert" markdown="1">
On calcule la covariance et $Cov(U,V)=0$
</div>

$$
\begin{aligned}
Cov(X)&=E(UV)-\underbrace{E(U)E(V)}_{=0}\\
&= E((X+2Y)(X-3Y))\\
&= E(X^2-3XY+2XY-6Y^2)\\
&= E(X^2)+\underbrace{E(XY)}_{=0}-6E(Y^2)\\
&= E(X^2)-6E(Y^2)\text{ car } V(X)=E(X^2)=1\\
&=1-6=\color{green}{5}
\end{aligned}
$$

<div class="alert alert-success" role="alert" markdown="1">
Donc elles ne sont **pas** independantes.
</div>

</details>

# Exercice 5
La variable aleatoire $X$ suit une loi uniforme sur $[0;\theta]$ avec $\theta$ inconnu.

Sa densite est par definition donnee par $f(x,\theta)=\frac{1}{\theta}𝟙_{[0;\theta]}(x)$ i.e. $f(x,\theta)=1$ si $0\le x\le\theta$ sinon 0.

1. Montrer que sa densite peut etre ecrite $f(x,\theta)=\frac{1}{\theta}𝟙_{[0;1]}(\frac{x}{\theta})$
2. En deduire que la fonction de vraisemblance definie sur $[0;+\infty[\times]0;+\infty[$ s'ecrit:$$L(x_1,...,x_n,\theta)=\begin{cases}\frac{1}{\theta^n}&\text{si} \max x_i\le\theta \\ 0&\text{sinon}\end{cases}$$ ou encore $$L(x_1,...,x_n,\theta)=\frac{1}{\theta^n}𝟙_{[\max 1\le i\le n;+\infty]}(\theta)$$
3. En deduire l’estimateur du maximum de vraisemblance du parametre $\theta$
4. Quelle loi suit la v.a. $\frac{X_1}{\theta}$
5. On pose $$T=\max_{1\le i\le n}\frac{X_i}{\theta}$$. Determiner sa fonction de repartition $F_T$
6. Montrer que $\mathbb P(\alpha\le T\le1)=1-\alpha^n$
7. En deduire un reel $\alpha$ tel que $\mathbb P(T\in[\alpha;1])=0,95$
8. Considerons des observations $x_1,...,x_n$. Notons $$M=\max_{1\le i\le n}x_i$$. Deduire des questions precedentes un intervalle de confiance pour le parametre $\theta$ de niveau de confiance 0, 95.

<details markdown="1">
<summary>Solution</summary>

1.

$$
\begin{aligned}
x\in[0;\theta]&\Leftrightarrow0\le x\le\theta\\
&\Leftrightarrow0\le\frac{x}{\theta}\le1\\
&\Leftrightarrow \frac{x}{\theta}\in[0;1]
\end{aligned}
$$

<div class="alert alert-success" role="alert" markdown="1">
Donc $$𝟙_{[0;\theta]}(x)=𝟙_{[0;1]}(\frac{x}{\theta})$$
</div>

2.

$$
\begin{aligned}
L(x_1,...,x_n,\theta)&=\Pi_{i=1}^nf(x_i,\theta)\\
&= \Pi_{i=1}^n\frac{1}{\theta}𝟙_{[0;\theta]}(x_i)\\
&= \frac{1}{\theta^n}\Pi_{i=1}^n𝟙_{[0;\theta]}(x_i)
\end{aligned}
$$

Pour que ce ne soit pas egale a $0$, $x_i\in[0;\theta]$

$$
\begin{aligned}
L(x_1,...,x_n,\theta)&=\frac{1}{\theta^n}𝟙_{[0;\theta]}(\max(x_i))\\
&= \frac{1}{\theta^n}𝟙_{[\max x_i;+\infty]}(\theta)
\end{aligned}
$$

3.

EMV: $\hat\theta=\max_{1\le i\le n}(x_i)$

4.

Loi uniforme sur $[0;1]$

$$
F_{\frac{X}{\theta}}(x)=P(\frac{X}{\theta}\le x)=P(X\le\theta x)\\
\color{red}{X\sim U([0;\theta])}=
\begin{cases}
0 &\text{si } x\le0\\
\int_0^{\theta x}\frac{1}{\theta}dt=x &\text{si } \theta x\in[0;\theta]\color{red}{\Leftrightarrow x\in[0;1]}\\
1 &\text{si } \color{red}{\theta x\lt\theta\text{, i.e. } x\gt1}
\end{cases}\\
=F_U(x) \text{ avec } U=\frac{X}{\theta}\sim U([0;1])
$$

5.

$$
\begin{aligned}
F_T(x)&=P(\max\frac{X_i}{\theta}\le x)\\
&= P(\cap_{i=1}^n\{X_i\le x\})=\Pi_{i=1}^nP(\frac{X_i}{\theta}\le n) \text{ car les v.a. } x_i \text{ sont independantes}\\
&= P(\frac{X}{\theta}\le x)^n\text{ car les }\frac{x_i}{\theta}\text{ ont les memes lois}
\end{aligned}\\
F_T(x)=
\begin{cases}
0 &x\lt0\\
x^n &x\in[0;1]\\
1 &x\gt1
\end{cases}
$$

7.

Resolution d'equation:

$$
\begin{aligned}
1-\alpha^n&=0,95\\
\alpha^n&=0,05\\
\alpha&=\sqrt[n]{0,05}
\end{aligned}\\
$$

8.

$T=\max\frac{x_i}{\theta}$, $M=\max x_i$, donc $T=\frac{M}{\theta}$ (car $\theta\gt0$)

$$
P(\sqrt[n]{0,05}\le T\le1)=095\Rightarrow P(\sqrt[n]{0,05}\le\frac{M}{\theta})=0,95\\
P(1\le\frac{\theta}{M}\le(0,05)^{-\frac{1}{n}})=0,95\Leftrightarrow P(M\le\theta\le M(0,05)^{-\frac{1}{n}})=0,95
$$

<div class="alert alert-success" role="alert" markdown="1">

$$
I\subset[M, M(0,05)^{-\frac{1}{n}}]
$$

</div>

</details>
