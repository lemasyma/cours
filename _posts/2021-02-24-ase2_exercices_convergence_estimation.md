---
title:          "ASE2: TD 1"
date:           2021-02-24 10:00
categories:     [tronc commun S8, ASE2]
tags:           [tronc commun, ASE2, S8]
description: TD 1
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/BkBV8jmMO)

# Exercice 1
Determiner les fonctions caracteristiques dans les cas suivants:
## $X$ suit la loi binomiale $B(n,p)$
<details markdown="1">
<summary>Solution</summary>
$X$ suit la loi $B(n,p)$.
$X$ est une somme independante de variables de Bernoulli $B(p)$.

$$
X = \sum^n_{j=1}X_j
$$

ou $X_j\to B(p) \forall j = 1,..., n$

D'apres le cours, on a calcule la fonction caracteristique de Bernouilli $\phi_{x_j}(t) = q + pe^{it}$ avec $q = 1-p$ or les $X_i$ sont independantes

$$
\phi_{\sum_{j=1}^{k}X_j} = \Pi^k_{j=1}\phi_{X_j}(t) = (q+pe^{it})^n
$$

Remarque: Comme 2e methode on peut calculer directement $\phi_X(t)$, $X\to B(n,p)$

$$
\begin{aligned}
\phi_X(t) &= \sum^n_{k=0}e^{itk}P(X=k)\\
&= \sum^n_{k=0}e^{itk}\binom{n}{k}p^k(1-p)^{n-k} \\
&= \sum^n_{k=0}\binom{n}{k}(pe^{it})^k(1-p)^{n-k}\\
&= (1-p+pe^{it})^n \text{ (Netwon)}\\
&= (q+pe^{it})^n
\end{aligned}
$$

</details>

## $X$ suit la loi de Poissons $P(\lambda)$
<details markdown="1">
<summary>Solution</summary>
$X\to P(\lambda)$ Poisson de parametre $\lambda$.

$$
\begin{aligned}
P(X=k) &= e^{-\lambda}\frac{\lambda^k}{k!} \forall k\in\mathbb N\\
\phi_X(t) &= \sum_{k=0}^{+\infty}e^{itk}P(X=k) = \sum_{k=0}^{+\infty}e^{itk}e^{-\lambda}\frac{\lambda^k}{k!}\\
&=e^{-\lambda}\sum_{k=0}^{+\infty}\frac{(\lambda e^{it})^{k}}{k!}\\
\end{aligned}
$$

Rappel: $\sum_0^{+\infty}\frac{x^k}{k!} = e^x$

Donc:

$$
\begin{aligned}
phi_X(t) &= e^{-\lambda}\exp(\lambda e^{it})\\
&= \exp(-\lambda+\lambda e^{it})
\end{aligned}
$$

</details>

## $X$ suit la loi uniforme $U[-a,a]$
<details markdown="1">
<summary>Solution</summary>
$X\to U_{[-a, a]}$ (Loi uniforme sur $[-a, a]$)
Sa densite est:
$$
f(x)=
\begin{cases}
    \frac{1}{2a} &\forall x\in [-a, a]\\
    0 &\text{sinon}
\end{cases}
$$

Donc:

$$
\begin{aligned}
\phi_X(t) &= \int_{\mathbb R}e^{itx}f(x)dx = \frac{1}{2a}\int_{-a}^ae^{itx}dx\\
&= \frac{1}{2a}\biggr[\frac{e^{itx}}{it}\biggr]^a_{-a} = \frac{1}{2a}\biggr(\frac{e^{ita} - e^{-ita}}{it}\biggr)\\
&\Rightarrow \phi_X(t) = \frac{2i\sin(at)}{2ait} = \frac{sin(at)}{at}
\end{aligned}
$$

</details>

## $X$ suit la loi normale $N(0,1)$
<details markdown="1">
<summary>Solution</summary>
$X\to N(0,1)$ (Loi normale centree reduite)
En utilisant la formule de Mac-Laurin:

$$
\phi_X(t) = \sum_{k=0}^{+\infty}\frac{t^k}{k!}i^kE(X^k)
$$

or $X\to N(0,1)$

$E(X^k) = 0$ si $k$ impair et $E(X^{2k}) = \frac{(2k)!}{2^kk!}$

Donc:

$$
\begin{aligned}
\phi_X(t) &= \sum_{k=0}^{+\infty}\frac{(-\frac{t^2}{2})^k}{k!} \\
&= e^{-\frac{t^2}{2}}
\end{aligned}
$$

</details>

# Exercice 2
Soit $X_n$ une suite de variables aleatoires de densite $f(x)=\frac{ne^{-nx}}{(1+e^{-nx})^2}$.
Montrer que $X_n\to^P_{n\to+\infty}0$

<details markdown="1">
<summary>Solution</summary>
$X_n$ suite de VA

$f_n(x) = \frac{ne^{-nx}}{(1+e^{-nx})^2}$

On veut montrer que $X_n\to^P_{n\to+\infty}0$

$$
\begin{aligned}
P(\vert X_n\vert\gt\varepsilon) &= 1 - P(\vert X_n\vert\le\varepsilon)\\
&= 1 - P(-\varepsilon\le X_n\le\varepsilon)\\
&= 1 - \int_{-\varepsilon}^{\varepsilon}f_n(x)dx\\
&= 1-\int_{-\varepsilon}^{\varepsilon}\frac{ne^{-nx}}{(1+e^{-nx})^2}dx\\
&= 1 - \biggr[\frac{1}{1+e^{-nx}}\biggr]_{-\varepsilon}^{\varepsilon} = 1-\frac{1}{1+e^{-n\varepsilon}}+\frac{1}{1+e^{n\varepsilon}}\\
\lim_{n\to+\infty}P(\vert X_n\vert\gt\varepsilon) &= 1- 1 + 0 =0\\
\end{aligned}\\
$$

Donc $X_n\to^{P}_{n\to+\infty}0$
</details>
