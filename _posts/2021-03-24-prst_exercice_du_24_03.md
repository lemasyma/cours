---
title:          "PRST: Exos pour le 24/03"
date:           2021-03-24 15:30
categories:     [Image S8, PRST]
tags:           [Image, SCIA, PRST, S8,  loi, intervalle, confiance]
description: Exos pour le 24/03
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/r1Cp1JYEd)

# Exercice 1

Considerons une variable aleatoire $X$ suivant une loi de Poisson de parametre $0, 2$.
1. Calculer $P(X = 4)$.
2. Calculer $E(X)$ et $V(X)$.

<details markdown="1">
<summary>Solution</summary>

$P(X=4) e^{-0,2}\frac{0,2^4}{4!}=5,45\times10^{-5}$

$E(X)=0,2$

$V(X)=0,2$

</details>

# Exercice 2
La variable aleatoire $U$ suit une loi uniforme sur l’intervalle $[2; 7]$. Calculer $P(U \in [3; 5])$ puis $E(U)$.

<details markdown="1">
<summary>Solution</summary>

$P(U\in[3,5])=\frac{5-3}{7-2}=\frac{2}{5}$

$E(U)=\frac{a+b}{2}=\frac{2+7}{2}=4,5$

</details>

# Exercice 3

La loi de Skellam est definie sur $N$ comme la difference de deux variables aleatoires **independantes** suivant des lois de Poisson $\mathcal P(\lambda_1)$ et $\mathcal P(\lambda_2)$ avec $\lambda_1 \ge 0$ et $\lambda_2 \ge 0$.

Soient $N_1$ et $N_2$ des variables aleatoires **independantes** suivant respectivement des lois de Poisson $\mathcal P(\lambda_1)$ et $\mathcal P(\lambda_2)$.

Par definition, la variable aleatoire $X := N_1 − N_2$ suit une loi de Skellam de parametres $\lambda_1$ et $\lambda_2$

1. Montrer que $E(X) = \lambda_1 − \lambda_2$ et $V(X) = \lambda_1 + \lambda_2$
2. Consid´erons un echantillon $(X_1, . . . , X_n)$ de la loi de $X$. Determiner, a l’aide de la methode des moments, des estimateurs des parametres $\lambda_1$ et $\lambda_2$.

<details markdown="1">
<summary>Solution</summary>

$$
\begin{aligned}
E(X) &= E(N_1-E(N_2))\\
&= E(N_1)-E(N_2)\\
&= \lambda_1-\lambda_2
\end{aligned}
$$

$$
\begin{aligned}
V(X) &= V(N_1-N_2)\\
&= \underbrace{V(N_1) + V(-N_2)}_{N_1\text{ et }N_2\text{ sont independantes}}\\
&= \lambda_1+(-1)^2V(N_2)\\
&=\lambda_1+\lambda_2
\end{aligned}
$$

On sait que

$$
\begin{cases}
E(X)=\lambda_1-\lambda_2\\
V(X)=\lambda_1+\lambda_2
\end{cases}\\
\begin{cases}
E(X)=\lambda_1-\lambda_2\\
E(X) + V(X)=2\lambda_1
\end{cases}\\
\begin{cases}
\lambda_2=\lambda_1-E(X)=\frac{V(X)-E(X)}{2}\\
\lambda_1=\frac{E(X)+V(X)}{2}
\end{cases}
$$

D'ou, par la methode des moments:

$$
\begin{cases}
\hat\lambda_1=\frac{\bar X+S^2}{2}\\
\hat\lambda_1=\frac{S^2-\bar X}{2}\\
\end{cases}
$$

</details>