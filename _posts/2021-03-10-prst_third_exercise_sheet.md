---
title:          "PRST: Feuille 3 - Exercice"
date:           2021-03-10 14:30
categories:     [Image S8, PRST]
tags:           [Image, SCIA, PRST, S8]
description: Feuille 3 - Exercice
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/SygaNL8X_)

# Exercice du cours
Déterminer les estimateurs des paramètres $m$ et $\sigma$ 2 donnés par la méthode des moments pour une loi normale $N (m, \sigma^2)$.

<details markdown="1">
<summary>Solution</summary>
$$
E(\lambda) = \frac{1}{\lambda}\\
\lambda = \frac{1}{E(X)}\\
\hat\lambda=\frac{1}{\bar X_n}
$$

$X_n\to^{P.S} \frac{1}{\lambda}$ loi forte des grand normbres

$$
f:x\mapsto\frac{1}{x}, \mathcal C^{\gamma}\\
]0;+\infty[\to\mathbb R
$$

</details>

# Exercice 1
Determiner un estimateur convergent et sans biais du parametre $\lambda$ pour la loi de Poisson.

<details markdown="1">
<summary>Solution</summary>
On sait que:

$$
E(Y) = \lambda
$$

Donc l'estimateur d'ordre 1 de parametre $\lambda$ est:

$$
\hat\lambda = \bar X_n = \frac{1}{n}\sum_{i=1}^nX_i
$$

L'estimateur est **sans biais** et il est fortement convergent par la loi forte des grand nombres.

</details>

# Exercice 2
Determiner un estimateur du parametre $\alpha$ pour la loi de Pareto par la methode desmomets (cf. feuille1). 

<details markdown="1">
<summary>Solution</summary>

On sait que $E(X) = \frac{\alpha}{\alpha -1}$

$$
\alpha -1E(X) = \alpha\\
\alpha(E(X)-1) = E(X)\\
\alpha=\frac{E(X)}{E(X) - 1}\\
\bar\alpha\frac{\bar X}{\bar X -1}
$$

</details>

# Exercice 3
Determiner un estimateur du parametre $p$ pour une loi geometrique.

<details markdown="1">
<summary>Solution</summary>

$$
X\sim\mathcal E(p)\\
E(X) = \frac{1}{p}\\
\text{donc } p = \frac{1}{E(X)}\\
\bar p = \frac{1}{X}
$$

</details>

# Exercice du cours
1. loi de Pareto de parametre $\alpha$
2. densite $f(x,\alpha)=\alpha x^{-\alpha-1}$ pour $x\gt1$ et $\alpha\gt0$
3. Determiner l'EMV

<details markdown="1">
<summary>Solution</summary>

$$
\begin{aligned}
L(x_1,...,x_n,\alpha)&=\Pi_{k=1}^nf(x_k,\alpha)\\
&= \Pi_{k=1}^n\alpha x^{-\alpha-1}\\
&= \alpha^n\Pi_{k=1}^nx^{-\alpha-1}\\
\log(L(x_1,...,x_n,\alpha)) &= n\log(\alpha)+\sum_{k=1}^n\log(xk^{-\alpha-1})\\
&= n\log\alpha-(\alpha-1)\sum_{k=1}^n\log(xk)\\
\frac{\delta L}{\delta\alpha} &= \frac{n}{\alpha}-\sum_{k=1}^n\log(x_k)\\
\frac{\delta L}{\delta\alpha} = 0 &\Leftrightarrow \frac{n}{\alpha}-\sum_{k=1}^n\log(x_k)=0\\
&\Leftrightarrow \alpha=\frac{n}{\sum_{k=1}^n\log(x_k)}\\
&\Leftrightarrow \alpha=\frac{1}{\frac{1}{n}\sum_{k=1}^n\log(x_k)}\\
\frac{\delta^2L}{\delta\alpha^2}&=-\frac{n}{\alpha^2}\lt0\\
\hat\alpha &= \frac{1}{\frac{1}{n}\sum_{k=1}^n\log(x_k)} \Rightarrow\text{ EMV}
\end{aligned}
$$

</details>

# Exercice 6
Soit $X$ une varibale aleatoire suivant une loi uniforme sur $[0,\theta]$.
1. Quelle est la densite de la variable aleatoire $X$ ?
2. Quelle est son esperance ?
3. En deduire un estimateur du parametre $\theta$ par la methode des moments

<details markdown="1">
<summary>Solution</summary>
1.

$$
f(x,\theta)=
\begin{cases}
    \frac{1}{\theta} &\text{si } x\in[0,\theta]\\
    0 &\text{sinon}
\end{cases}
$$

2.

$$
E(X) = 0 + \frac{\theta}{2} = \frac{\theta}{2} \Rightarrow \theta=2\times E(X)
$$

3.

$$
\hat\theta=2\bar X
$$

</details>
