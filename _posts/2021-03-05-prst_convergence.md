---
title:          "PRST: Convergence"
date:           2021-03-05 14:30
categories:     [Image S8, PRST]
tags:           [Image, SCIA, PRST, S8]
math: true
description: Convergence
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/S1VJ-M6f_)

# PRST - Seance 2

# Definition
- Soit $X$ une v.a (aucune condition prescrite)
- $\phi$ definie sur $\mathbb R$ par: $\phi_X(t) = E(e^{itx})$
- $\vert e^{itx}\vert \le 1$
- $\phi(t)=\int_{\omega}e^{itx(\omega)}$
- Caracterise la loi d'une v.a, i.ei $\phi_X=\phi_Y \Rightarrow X$ et $Y$ suivent la meme loi

# Lois marginales
- Lois des v.a $X_i$
- Impossible, sans hypothese supplementaire, de determiner la loi conjointe a partir des lois marginales

## Matrice de covariance
- Matrice carre d'ordre $d$ definie par $m_{ij} = Cov$

# Indepenance de 2 variables: cas discret
1. 2 va $X$ et $Y$ sont dites *independantes* si, pour tout reel $x$ et $y$ de leur supports respectifs:
2. $P({X\le x})$
3. 2 variables aleatoires sont *independantes* si:

# Definition
- Un vecteur aleatoire $(X_1,...,X_d)$ est dit *gaussien* si toute combinaison des VA $X_k$ est gaussienne
- Un vecteur gaussien est entierement caracterise par $m=(E(X_1),...,E(X_d))^T$ et sa matrice de variance-covariances $\Sigma$. Sa loi sera notee $N(m,\Sigma)$ et nous parlerons de loi *normale multidimensionnelle*

## Proposition
Si $X$ est un vecteur gaussien et $A$ est une application lineaire definie sur $\mathbb R^+$
$Y = AX$ est un vecteur gaussien
<div class="alert alert-danger" role="alert" markdown="1">
L'image d'un vecteur gaussien par une application lineaire est un vecteur gaussien.
</div>

*Comment prouver que la d-ieme composante est gaussienne ?*
Soit $(X_1, X_2, X_3)$ un vecteur gaussien. Pourquoi $X_3$ suit-elle une loi gaussienne ?
$$
\underbrace{\begin{pmatrix}0 & 0 &1\end{pmatrix}}_{\text{application lineaire}}
\begin{pmatrix}
X_1\\
X_2\\
X_3
\end{pmatrix} = X_3
$$

On considere Leo et Alexandre jouent a un jeu de pile ou face et font bourses communes.

||Leo|
|-|-|
|pile|10 €|
|face|-10 €|

||Alexandre|Proba|
|-|-|-|
|Image|10 €|1/2|
|SCIA|5 €|1/10|
|GISTRE|-100 €|4/10|

> Ils vont pas en cours les SCIA - Alexandre

On a $(X;Y)$ avec $X$ les gains de Leo et $Y$ les gains de Alexandre. Les deux VA sont independantes

$$
P(X=1-;Y=10) = \frac{1}{2} \times \frac{1}{2} = \frac{1}{4}\\
P(X=-10;Y=100) = \frac{1}{2}\times\frac{4}{10} = 0,5\\
(E(X); E(Y)) = (0; -34,5)
$$

## Proposition
Soit $X = (X_1,..., X_d)$ un vecteur gaussien.
Les variables aleatoires $X_1,...X_d$ sont independantes si et seulement si la matrice $\Sigma$ est diagonale.
$Cov(UV) = E(UV) - E(U) \times E(V)$
$$
\Sigma =
\begin{pmatrix}
    Var(U) & Cov(U, V)\\
    Cov(U, V) & Var(U)
\end{pmatrix}
$$

# Convergence presque sure (p.s.)
1. $(X_i)$ suite de variables aleatoires sur le meme espace $\Omega$ et $X$ une variable aleatoire egalement definie $\Omega$
2. convergence ponctuelle
3. implique tous les autres
$\lim_{n\to+\infty}X_n(\omega) = Y(\omega)$ pour tous $\omega\in\Omega$

# Convergence en probabilite
1. Meme cadre que precedemment
2. $\forall\varepsilon\gt 0, \lim_{n\to+\infty}P(\vert X_n - X\vert\ge \varepsilon) = 0$

# Convergence en loi
1. Meme cadre que precedemment
2. $\lim_{n\to+\infty}F_{X_n} = F_X$

# Theoreme de Paul Levy
1. Si la suite de v.a. $(X_n)$ converge en loi vers une v.a. $X$ alors
2. $\lim_{n\to+\infty}\pi_{X_n} = \phi_X(t)$

# Convergence $L^2$
1. aussi appelee *convergence en moyenne quadratique*
2. $\lim_{n\to+\infty}E(\vert X_n - X\vert^2) = 0$
3. n'a de sens que pour les VA telles que $E(X^2)\lt+\infty$
4. implique la convergence en probabilite

# Convergence $L^1$
1. aussi appelee *convergence en moyenne*
2. $\lim_{n\to+\infty}E(\vert X_n -X\vert) = 0$

# Loi forte des grands nombres
Soit $(X_i)$ une suite de VA i.i.d. (independant et suivat la meme loi)

$$
\lim_{n\to+\infty}\overline{X_n} = E(X)
$$

au sens de la convergence p.s. ou $\overline{X_n} := \frac{X_1 + ... +  X_n}{n}$

# Cas unidimensionnel
1. Soit $(X_i)$ une suite v.a. i.i.d.
2. Noton $m:=E(X_i)$ et $\sigma^2 = V(X_i)$

<div class="alert alert-info" role="alert" markdown="1">
$X_1$ et $X_2$ deux v.a. independantes.
$$
\phi_{X_1 + X_2}(t) = \phi_{X_1}(t) + \phi_{X_2}(t)
$$
</div>

## Preuve
$$
\begin{aligned}
\phi_{X_1 + X_2}(t) &= E(e^{it(X_1 + X_2)})\\
&= E(e^{itX_1})E(e^{itX_2})
\end{aligned}
$$
Car les v.a. sont independantes
$$
\phi_{X_1+X_2} = 
$$