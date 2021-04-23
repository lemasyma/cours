---
title:          "PRST: Les differentes lois - Exercice"
date:           2021-02-24 15:30
categories:     [Image S8, PRST]
tags:           [Image, SCIA, PRST, S8]
description: Les differentes lois - Exercice
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/r1o44y4Md)

# Exercice 4

<details markdown="1">
<summary>Solution</summary>

Soit $\omega_1,...,\omega_n$ les issues i.e.
$\Omega = \{\omega_1;...;\omega_n\}$
$$
\begin{aligned}
E(X\times Y) &= \sum_{\omega\in\Omega}(X(\omega) + Y(\omega))\\
&= \underbrace{\sum_{\omega\in\Omega} p(\omega)X\vert\omega\vert}_{=E(X)} + \underbrace{\sum_{\omega\in\Omega} p(\omega)Y\vert\omega\vert}_{=E(Y)}\\
&= E(X) + E(Y)
\end{aligned}
$$

$$
\begin{aligned}
E(\lambda X) &= \sum_{\omega\in\Omega}p(\omega)\lambda X(\omega)\\
&= \lambda\sum_{\omega\in\Omega}p(\omega)X(\omega)\\
&= \lambda E(X)
\end{aligned}
$$

</details>

# Exercice 3

Determiner la loi $\mathcal B(3, \frac{1}{3})$

<details markdown="1">
<summary>Solution</summary>

- $P(X = x_1) = \binom{3}{0}\times\frac{1}{3}^0\times\frac{2}{3}^3 = \frac{8}{27}$
- $P(X = x_2) = \binom{3}{1}\times\frac{1}{3}^1\times\frac{2}{3}^2  = \frac{4}{9}$
- $P(X = x_3) = \binom{3}{2}\times\frac{1}{3}^2\times\frac{2}{3}^1  = \frac{2}{9}$
- $P(X = x_4) = \binom{3}{3}\times\frac{1}{3}^3\times\frac{2}{3}^0  = \frac{1}{27}$

|$P(X)$|$\frac{8}{27}$|$\frac{4}{9}$|$\frac{2}{9}$|$\frac{1}{27}$|
|-|-|-|-|-|
|$X$|$x_1$|$x_2$|$x_3$|$x_4$|

</details>

# Exercice 14
Soit $X$ une variable aleatoire suivant une loi geometrique. Montrer que $P(X\gt n+k\vert X\gt k) = P(X\gt n)$ pour tous entiers naturels $k$ et $n$.
Nous dirons que la loi geometrique est *sans memoire*.


<details markdown="1">
<summary>Solution</summary>
Soient $n$ et $k$ deux entiers naturels.

$$
\begin{aligned}
P(X\gt n) &= \sum_{k\gt n} pq^{k-1}\\
&= pq^n + pq^{n+2} +...\\
&= pq^n(1+q+q^2+...)
\end{aligned}
$$

Or $\sum_{k\ge0}q^k=\frac{1}{1-q}$ pour $0\le q\lt1$

D'ou:

$$
P(X\gt n) = pq^n\times\frac{1}{1-q} = pq^n\times\frac{1}{p} = q^n
$$

Ainsi:

$$
P(X\gt n+k\vert X\gt k) = \frac{P(\{X=n+k\}\cap\{x\gt k\})}{P(X\gt k)}
$$

Or $\{X=n+k\}\cap\{x\gt k\} = \{X\gt n+k\}$

D'ou:

$$
P(X\gt n + k) = \frac{P(X\gt n + k)}{P(X\gt k)} = \frac{q^{n+k}}{q^k} = q^n = P(X\gt n)
$$
</details>

# Exercice 6
Considerons une variable aleatoire $X$ suivant une loi de Poisson de parametre 3
1. Calculer $P(X=10)$
2. Calculer $E(X)$ et $V(X)$


<details markdown="1">
<summary>Solution</summary>
$$
P(X=10) = e^{-3}\times\frac{3^{10}}{10!}\\
E(X) = V(X) = 3
$$
</details>

# Exercice 11
La variable aleatoire $U$ suit une loi uniforme sur l'intervalle $[2;5]$.
Calculer $P(U)\in[2;3]$ et $E(U)$

<details markdown="1">
<summary>Solution</summary>
$P(U) = \frac{1}{3}$
</details>
