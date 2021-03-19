---
title:          "ASE2: Convergence et estimation, suite"
date:           2021-03-17 9:00
categories:     [tronc commun S8, ASE2]
tags:           [tronc commun, ASE2, S8, loi, estimation]
description: Convergence et estimation, suite
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/ByGBD4kNd)

$\bar X$ est un exemple d’estimateur de la moyenne $m=E(X)$ (sert a approximer la moyenne de la population globale)

<div class="alert alert-danger" role="alert" markdown="1">
Utile quand on a un parametre inconnu.
</div>

<div class="alert alert-info" role="alert" markdown="1">
**Definition**:
On appelle variance empirique, la statistique : 

$$
S^2=\frac{1}{n}\sum_{i=1}^n(X_i-\bar X)^2
$$

</div>

### Proposition
$$
S^2 = \frac{1}{n}\sum_{i=1}^nX_i^2-(\bar X)^2
$$

### Demo
$$
\begin{aligned}
S^2&=\frac{1}{n}\sum_{i=1}^n(X_i-\bar X) = \frac{1}{n}\sum_{i=1}^n(X_i^2 - X_i\bar X+\bar X^2)\\
&= \frac{1}{n}\sum_{i=1}^nX_i^2-2\bar X\sum_{i=1}^nX_i+\frac{n}{n}\bar X^2\\
&= \frac{1}{n}\sum_{i=1}^nX_i^2-2\bar X^2+\bar X=\frac{1}{n}\sum_{i=1}^nX_i^-(\bar X)
\end{aligned}
$$

Montrons que $S^2\to^P\sigma^2$ lorsque $n\to+\infty$

D’après la loi des grands nombres, on a:
$\bar X\frac{1}{n}\sum_{i=1}^nX_i\to^Pm=E(X)$ quand $n\to+\infty$
et $\frac{1}{n}\sum_{i=1}^n\to^PE(X^2)$ quand $n\to+\infty$
Donc $S^2=\frac{1}{n}\sum_{i=1}^nX_i^2-(\bar X)^2\to^PE(X^2)-E^2(X)=\sigma^2=V(X)$

<div class="alert alert-warning" role="alert" markdown="1">
$S^2$ est un estimateur de la variance.
</div>

<div class="alert alert-info" role="alert" markdown="1">
**Definition**
On considère une population $X$, distribuée suivant une loi de probabilité qui dépend d’un paramètre $\theta$ inconnu. On prélève un échantillon $(X_1,X_2,...,X_n)$ de $X$, on appelle estimateur de $\theta$, toute variable aléatoire $T_n$ fonction de l’échantillon:

$$
T_n=f(X_1,X_2,...X_n)
$$

</div>

On appelle biais de l’estimateur la quantité $b(T_n)=E(T_n)-\theta$

<div class="alert alert-danger" role="alert" markdown="1">
On dit que l’estimateur est sans biais si $b(T_n)=0\Leftrightarrow E(T_n)=\theta$.
</div>
Comme exemple $\bar X$ est un estimateur sans biais de $m=E(X)$ puisque $E(\bar X) = m$

<div class="alert alert-info" role="alert" markdown="1">
**Definition**
On dit qu’une suite $(T_n)$ d’estimateurs de $\theta$ est asymptotiquement (cad au voisinage de $+\infty$) sans biais et si

$$
lim_{n\to+\infty}(E(T_n))=\theta
$$

</div>

On appelle risque quadratique de $T_n$ ou erreur quadratique: 
$$
R(T_n)=E((T_n-\theta)^2)
$$

### Propositiom
Le risque quadratique est : 

$$
R(T_n) = V(T_n)+(E(T_n)-\theta)^2
$$

### Démonstration

$$
(T_n-\theta)^2=(T_n-E(T_n)+E(T_n)-\theta)^2\\
\begin{aligned}
E((T_n-\theta)^2)&=E((T_n-E(T_n))^2)+2E((T_n-E(T_n))(E(T_n)-\theta))+E((E(T_n)-\theta)^2)\\
&= V(T_n)+2(E(T_n)-\theta)(E(T_n)-E(T_n))+(E(T_n)-\theta)^2\\
\end{aligned}\\
\text{Donc } R(T_n) = V(T_n)+(E(T_n)=\theta)^2
$$

### Remarque
Si l’estimateur est sans biais $b(T_n)=E(T_n)-\theta=0$
Alors $R(T_n)=V(T_n)$
Donc si on a deux estimateurs sans biais du paramètre $\theta$, le plus précis est celui de variance minimale.

<div class="alert alert-info" role="alert" markdown="1">
**Definition**
On dit que l’estimateur $T_n$ est convergent si cet estimateur converge en probabilité vers le paramètre $\theta$.
On ecrira $T_n\to^P\theta$ lorsque $n\to+\infty$
</div>

<div class="alert alert-info" role="alert" markdown="1">
**Definition**
On appelle vraisemblance de $\theta$, la densité de l’échantillon $(X_1,X_2,...,X_n)$:

$$
\begin{cases}
L(x_1,x_2,...,x_n,\theta)=\Pi_{i=1}^nP(X_i=x_i) &\text{(dans le cas discret)}\\
L(x_1,x_2,...,x_n,\theta)=\Pi_{i=1}^nf(x_i) &\text{(dans le cas continu)}
\end{cases}
$$

</div>