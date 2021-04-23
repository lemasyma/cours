---
title:          "ASE2:  TD 1, suite (encore)"
date:           2021-03-10 9:00
categories:     [tronc commun S8, ASE2]
tags:           [tronc commun, ASE2, S8, convergence, normale, loi]
description: Suite des exercices sur la convergence et estimation
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/SyaGAgUm_)

# Exercice 5
Soit $X$ une v.a. normale centree et reduite $X\to\mathcal N(0,1)$.
Montrer que $\forall x\in\mathbb R^*_+$

$$
\int_0^x e^{-\frac{t^2}{2}}dt\ge\sqrt{\frac{\pi}{2}}(1-\frac{1}{x^2})
$$

<div class="alert alert-warning" role="alert" markdown="1">
Utiliser Tchebychev.
</div>

<details markdown="1">
<summary>Solution</summary>
Soit $X\to\mathcal N(0,1)$ (Loi normale centree reduite).

D'apres l'inegalite de Techbychev:

$$
\begin{aligned}
\forall\varepsilon\gt0, &P(\vert X-E(X)\vert\ge\varepsilon)\le\frac{V(X)}{\varepsilon^2}\\
\text{or: } &E(X) = 0 \text{ et } V(X) = 1\\
&P(\vert X\vert\ge\varepsilon)\le\frac{1}{\varepsilon^2}\\
\text{et} &P(\vert X\vert\ge\varepsilon)=1-P(\vert X\vert\le\varepsilon)\\
\text{Ca permet d'ecrire: } &P(\vert X\vert\lt\varepsilon)\ge 1-\frac{1}{\varepsilon^2}\\
\text{c.a.d.} &P(-\varepsilon\lt X\lt\varepsilon)\ge1-\frac{1}{\varepsilon^2}\\
&F(\varepsilon) - F(-\varepsilon)\ge 1-\frac{1}{\varepsilon^2} \text{ F: fonction de densite de }\mathcal N(0,1)\\
&F(\varepsilon) - (1-F(\varepsilon))\ge 1-\frac{1}{\varepsilon^2}, \forall\varepsilon\gt0\\
\Rightarrow &2F(\varepsilon) -1 \ge 1-\frac{1}{\varepsilon^2}(*)
\end{aligned}
$$

On a aussi $\frac{1}{\sqrt{2\pi}}\int_0^xe^{-\frac{t^2}{2}} = F(x) - F(0) = F(x) - \frac{1}{2}, \forall x\gt0$

$$
\begin{aligned}
\Rightarrow \int_0^xe^{-\frac{t^2}{2}} &= \sqrt{2\pi}(F(x) - \frac{1}{2})\\
&=\frac{\sqrt{2\pi}}{2}(2F(x) - 1), \forall x\gt0
\end{aligned}
$$

Grace a l'inegalite $(*)$ et en remplacant $\varepsilon$ par $x$, on obtient $\forall x\gt0$:

$$
\int_0^xe^{-\frac{t^2}{2}}=\frac{\sqrt{2\pi}}{2}(2F(x) - 1)\ge\frac{\sqrt{2\pi}}{2}(1-\frac{1}{x^2})
$$

<div class="alert alert-success" role="alert" markdown="1">
On a bien:

$$
\forall x\gt0, \int_0^Xe^{-\frac{t^2}{2}}\ge\sqrt{\frac{\pi}{2}}(1-\frac{1}{x^2})
$$
</div>

</details>

# Exercice 6

On considere une suite suite de v.a.a $(X_n), n\in\mathbb N^*$ dsitribue suivant la loi de Poisson $\mathcal P(\frac{1}{n}), (\lambda = \frac{1}{n})$. 
Montrer que $X_n$ converge en loi vers la variable aleatoire $X=0$ $(X_n\to_{n\to+\infty}^L0)$

<details markdown="1">
<summary>Solution</summary>

$(X_n), n\in\mathbb N^*$ suit  la loi de Poisson $\mathcal P(\frac{1}{n})$.

<div class="alert alert-warning" role="alert" markdown="1">
Rappel: 

$$
P(X_n=k) = e^{-\lambda}\frac{\lambda^k}{k!} \text{ (avec } \lambda = \frac{1}{n}\text{)}\\
P(X_n = k)= e^{-\frac{1}{n}}\frac{1}{n^kk!}, \forall k\in\mathbb N
$$

- Si $k=0$, $P(X_n = 0) = e^{-\frac{1}{n}}\to_{n\to+\infty}0$
- Si $k\ge1$, $P(X_n=k)=\frac{1}{n^kk!}e^{-\frac{1}{n}}\to_{n\to+\infty}0$ car $\frac{1}{n^k}\to_{n\to+\infty}0$

</div>

Conclusion: on a montre que

$$
\begin{cases}
&\lim_{n\to+\infty}P(X_n=0)=1=P(X=0) \Leftrightarrow X_n\to_{n\to+\infty}^L0 \text{ variable certaine}\\
&\lim_{n\to+\infty}P(X_n=k) = 0 = P(X=k), \forall k\ge1
\end{cases}
$$

</details>

# Exercice 7
Soir $X$ une v.a. suivant la loi exponentielle de parametre $(\lambda\gt0)$.
1. Montrer que $\forall\varepsilon\gt0$, $P(\vert X-\frac{1}{\lambda}\vert\ge\varepsilon)\le\frac{1}{\lambda^2\varepsilon^2}$
2. En deduire que $P(X\gt\frac{3}{\lambda})\le\frac{1}{4}$

<details markdown="1">
<summary>Solution</summary>
$X$ suit la loi exponentielle$(\lambda)$ de parametre $\lambda$.

1.On rappelle que $E(X)=\frac{1}{\lambda}$ et $V(X)=\frac{1}{\lambda^2}$. En appliquant l'inegalite de Tchebychev:

$$
\begin{aligned}
&P(\vert X-E(X)\vert\ge\varepsilon)\le\frac{V(X)}{\varepsilon^2}, \forall\varepsilon\gt0\\
\Rightarrow &P(\vert X-\frac{1}{\lambda}\vert\ge\varepsilon)\le\frac{\lambda}{\lambda^2\varepsilon^2}, \forall\varepsilon\gt0
\end{aligned}
$$

2.L'evenement:

$$
(\vert X-\frac{1}{\lambda}\vert\ge\varepsilon \vert) = (X-\frac{1}{\lambda}\ge\varepsilon)\cup(X-\frac{1}{\lambda}\le-\varepsilon)\\
\text{or: } A\in A\cup B
\text{donc: } (X-\frac{1}{\lambda}\ge\varepsilon)\in(\vert X-\frac{1}{\lambda}\vert\ge\varepsilon \vert)
$$

On en deduit, par croissance de la probabilite:

$$
\begin{aligned}
&P(X-\frac{1}{\lambda}\ge\varepsilon)\le P(\vert X-\frac{1}{\lambda}\vert\ge\varepsilon)\\
\Rightarrow &P(X-\frac{1}{\lambda}\ge\varepsilon)\le\frac{1}{\lambda^2\varepsilon^2} \text{ (d'apres la question 1)}
\end{aligned}
$$

<div class="alert alert-success" role="alert" markdown="1">
En choisissant $\varepsilon=\frac{2}{\lambda}\gt0$, on obtient $P(X\ge\frac{3}{\lambda})\le\frac{1}{4}$
</div>

</details>

# Exercice 8
$(X_n)$ une suite de v.a. telle que $\forall n\in\mathbb N^*$: $X_n$ suit la loi geometrique $G(\frac{1}{n})$ (de parametre $\frac{1}{n}$).
On pose $Y_n=\frac{X_n}{n}$.
1. Determiner la fonction de repartition de la suite $Y_n:P(Y_n\le x), \forall x\in\mathbb R$
2. Montrere que $Y_n\to_{n\to+\infty}^LY$ avec $Y$ suit la loi exponentielle $(\lambda = 1)$

<details markdown="1">
<summary>Solution</summary>
$(X_n), n\gt0$ une suite de v.a. geometrique $G(\frac{1}{n})$ avec $p=\frac{1}{n}$ parametre.

<div class="alert alert-warning" role="alert" markdown="1">
Rappel:

$$
\begin{aligned}
P(X_n = k) &= (1-p)^{k-1}p, \forall k\ge1\\
&= (1-\frac{1}{n})^{k-1}\frac{1}{n}
\end{aligned}
$$

</div>

1.On veut determiner la fonction de repartition de $Y_n$.

$$
\forall x\le0, P(Y_n\ge x) = P(X_n\le nx) = 0 \text{ car } nx\le0
$$

Remarque: donc $\forall x\le 0$, $\lim_{n\to+\infty}P(Y_n\le x) = 0$, $\forall x\gt 0$ (reel strictement positif).

Des que $n$ est assez grand, $nx\ge 1$.

$$
\begin{aligned}
P(Y_n\le x) &= P(X_n\le nx) = \sum_{k=1}^{[nx]}P(X_n=k) \text{ }([nx] \text{participation entiere de } nx)\\
\forall x\gt0, P(Y_n\le x) &= \sum_{k=1}^{[nx]}(1-\frac{1}{n})^{k-1}\frac{1}{n}\\
&= \frac{1}{n}\sum_{k=1}^{[nx]}(1-\frac{1}{n}^{k-1}) = \frac{1}{n}\biggr(\frac{1-(1-\frac{1}{n})^{[nk]}}{1-(1-\frac{1}{n})}\biggr)\\
&= P(Y_n\le x) = 1 - (1-\frac{1}{n})^{[nk]}
\end{aligned}
$$

Donc:

$$
F_n(X) = P(Y_n\le x) =
\begin{cases}
    0 &x\le0\\
    1-(1-\frac{1}{n})^{[nx]} &x\gt0
\end{cases}
$$

On a:

$$
(1-\frac{1}{n})^{[nx]} = \exp([nx]ln(1-\frac{1}{n}))\\
\ln(1-\frac{1}{n})\sim-\frac{1}{n} \text{ (} n \text{ au voisinage de } +\infty \text{)}\\
\text{(}\ln(1+x)\sim x\text{ au (voisinage de 0))}
$$

Par definition de la partie entiere:
$$
\begin{aligned}
&[nx]\le nx\lt[nx] + 1\\
&nx-1\lt[nx]\le nx\\
&\Rightarrow 1-\frac{1}{nx}\lt\frac{[nx]{nx}}\le1\\
&\Rightarrow\lim_{n\to+\infty}\frac{[nx]}{nx}\le1\\
&\Rightarrow [nx]\sim nx \text{ (} n \text{ au voisinage de } +\infty\text{)}
\end{aligned}
$$

Donc $[nx]\ln(1-\frac{1}{n})\sim nx(-\frac{1}{n})=-x$.

$$
\exp([nx]\ln(1-\frac{1}{n}))\sim e^{-x} \text{ (} n \text{ au voisinage de } +\infty\text{)}\\
\forall x\gt0, \lim_{n\to+\infty} F_n(x) = \lim_{n\to+\infty}P(Y_n\le x)=1-e^{-x}
$$

<div class="alert alert-success" role="alert" markdown="1">
Conclusion:

$$
\forall x\le 0, \lim_{n\to+\infty}F_n(x)=\lim_{n\to+\infty}P(Y_n\le x)=0\\
\text{et}\\
\forall x\gt0, \lim_{n\to+\infty}F_n(x)=\lim_{n\to+\infty}P(Y_n\le x)=1-e^{-x}\\
\text{or } F(x)
\begin{cases}
    0 &x\le 0 \\
    1-e^{-x} &x\gt 0
\end{cases}
$$

$F(x)$ est la fonction de repartition de la loi exponentielle$(\lambda=1)$

</div>

</details>