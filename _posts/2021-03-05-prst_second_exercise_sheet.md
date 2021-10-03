---
title:          "PRST: Feuille 2 - Exercice"
date:           2021-03-05 15:30
categories:     [Image S8, PRST]
tags:           [Image, SCIA, PRST, S8, brenoulli, binomial, loi, partiel]
math: true
description: Feuille 2 - Exercice
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/BJH0y8-X_)

<div class="alert alert-info" role="alert" markdown="1">
L'ordre des exos dans le cours est 6 $\to$ 4 $\to$ 15 $\to$ 19 $\to$ 18
</div>

# Exercice 4

Montrer que la somme de n variables aléatoires indépendantes suivant une loi de Bernoulli de paramètre p suit une loi binomiale de paramètres n et p.

<details markdown="1">
<summary>Solution</summary>
$1^{ere}$ etape: Fonction caracteristique de $\mathcal B(n,p)$, Pour $k\in\{0,1,2,...,n\}$

<div class="alert alert-danger" role="alert" markdown="1">
$$
P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}
$$
</div>

$$
\begin{aligned}
E(e^{itX})&=\sum_{k=0}^{n}e^{itk}P(X=k)\\
&= \sum_{k=0}^{n}e^{itk}\binom{n}{k}p^k(1-p)^{n-k}\\
&= \sum_{k=0}^{n}\binom{n}{k}a^kb^{n-k} = (pe^{it}+n-p)
\end{aligned}
$$

$2^e$ etape: Soient $X_1,...,X_n$ $n$ v.a. independantes de loi $\mathcal B(p)$ 

$$
\begin{aligned}
\phi_{X_1+...+X_n}(t) &= (\phi_{X_1}(t))^1\\
\phi_{X_1+...+X_n}'(t) &= (pe^{it} + 1 - p)^n
\end{aligned}
$$

</details>

# Exercice 6
<div class="alert alert-danger" role="alert" markdown="1">
Exercice qui risque d'etre au partiel !
</div>

Soient deux variables aléatoires indépendantes suivant respectivement des lois exponentielles de paramètres respectifs $\lambda1$ et $\lambda2$. Montrer que la variable aléatoire $min(X1; X2)$ suit une loi exponentielle de paramètre $\lambda1 + \lambda2$.

<details markdown="1">
<summary>Solution</summary>

On cherche:

$$
\begin{aligned}
Y&=min(X1, X2)\\
R_Y(x) &= e^{-(\lambda_1+\lambda_2)x}
\end{aligned}
$$

On pose $Y=\min(X_1,X_2)$. Par definition, pour $x\gt0$:

$$
\begin{aligned}
R_Y(x) &= P(Y\gt x)\\
&= P(min(X_1, X_2)\gt x)
\end{aligned}
$$

<div class="alert alert-warning" role="alert" markdown="1">
Point de logique: si le minimum est plus grand que $x$ alors les 2 sont plus grnads que $x$.
</div>

$$
R_Y(x) = P(\{X_1\gt x\}\cap\{X_2\gt x\})
$$

$X_1$ et $X_2$ sont independantes donc:

$$
\begin{aligned}
R_Y(x) &= P(X_1\gt X_2)P(X_2\gt x) = e^{-\lambda_1x}\times e^{-\lambda_1x}\\
&= e^{-(\lambda_1+\lambda_2)x}
\end{aligned}
$$

Conclusion: $Y\sim \xi(\lambda_1+\lambda_2)$

</details>

# Exercice 15
Soient $X$ et $Y$ deux variables aléatoires indépendantes et suivant toutes deux une loi normale centrée réduite. Considérons les variables aléatoires $U = X + Y$ et $V = X − Y$

<details markdown="1">
<summary>Solution</summary>
1. 

$$
\begin{pmatrix}
    U\\
    V
\end{pmatrix} =
\begin{pmatrix}
    1 &1\\
    1 &-1
\end{pmatrix}
\begin{pmatrix}
    X\\
    Y
\end{pmatrix}
$$

On pose:

$$
A=
\begin{pmatrix}
    1 &1\\
    1 &-1
\end{pmatrix}
$$

Toute combinaison lineaire de $U$ et $V$ es une combinaison de $X$ et $Y$, comme ce sont des vecteurs gaussien alors $(U,V)^T$ est un vecteur gaussien.

2.

$$
\begin{aligned} 
E(U)&=E(X+Y)=E(X)+E(Y)=0 \\
E(V)&=E(X-Y)=E(X)-E(Y)=0\\
E(UV)&=E(X^2-Y^2)=E(X^2)-E(Y^2)
\end{aligned}
$$

$X$ et $Y$  sont centrees.
$$
\begin{aligned}
VM(X)&=E(X^2)-\underbrace{E(X)^2}_{=0}\\
E(X^2)&=E(Y^2)=1\\
E(UV)&=1-1=0\\
Cov(U,V)&=0-0=0
\end{aligned}
$$

</details>

# Exercice 18
Soit $X$ une variable aléatoire discrète de support $\mathbb N^*$ telle que, pour tout entier $k \ge 1$,
$$
P(X = k) = \frac{\alpha}{k!}
$$
pour un certain réel $\alpha$.
1. Déterminer le réel $\alpha$
2. Calculer $E(X)$ puis $E(X(X − 1))$. En déduire $V(X)$.

<details markdown="1">
<summary>Solution</summary>

<div class="alert alert-danger" role="alert" markdown="1">
1. Par definition:

$$
\sum_{k\ge 1}P(X=k)=1
$$

</div>

$$
\sum_{k\ge1}\frac{\alpha}{k!}=1 \Rightarrow\alpha\sum_{k\ge1}\frac{1}{k!}
$$

<div class="alert alert-info" role="alert" markdown="1">
Developpement limite de $e^z$, $z\in\mathbb R$:

$$
e^{z}=\sum_{k\ge0}\frac{z^k}{k}=1
$$

</div>

$$
\begin{aligned}
\sum_{k\ge1}\frac{1}{k!}&=\sum_{k\ge0}\frac{1}{k!}=e-1\text{ developpement limite.}\\
\sum_{k\ge1}P(X=k)&=\alpha(e-1)\\ 
\text{donc } \alpha(e-1)&=1\Leftrightarrow\alpha=\frac{1}{e-1}
\end{aligned}
$$

Notons que $\alpha$ est positif.

2.
 
$$
\begin{aligned}
E(X) &= \sum_{k\ge1}X_{\alpha}P(X=k) = \sum_{k\ge1}\alpha\frac{k}{k!} = \alpha\sum_{k\ge1}\frac{1}{(k-1)!}\\
&= \alpha\sum_{j\ge0}\frac{1}{j!} = \alpha e = \frac{e}{e-1}
\end{aligned}
$$ 

Calculons $E(X(X-1))$:

$$
\begin{aligned}
E(X(X-1)) &= \sum_{k\ge1}k(k-1)P(X=k)\\
&= \sum_{k\ge1}k(k-1)\times\frac{\alpha}{k!}=\sum_{k\ge2}\frac{\alpha}{(k-2)!}\\
&= \sum_{j\ge0}\frac{\alpha}{j!}=\alpha e =  \frac{e}{e-1}\\
E(X(X-1)) + E(X) &= E(X^2) \text{ donc } E(X^2)=2 \frac{e}{e-1}\\
V(X)&=2 \frac{e}{e-1}-\biggr(\frac{e}{e-1}\biggr)^2\\
&= \frac{2e(e-1)e}{(e-1)^2} = \frac{e^2-2e}{(e-1)^2}
\end{aligned}
$$

</details>

# Exercice 19

<div class="alert alert-danger" role="alert" markdown="1">
Exercice qui risque d'etre au partiel !
</div>

Soit $(U_n)$ une suite de variables aléatoires indépendantes suivant une loi uniforme sur l’intervalle $[0; 1]$.
On pose, pour tout entier $n \ge 1$, $M_n := max(U_1, . . . , U_n)$ et $X_n = n(1−M_n)$.
1. Soit $n \ge 1$. Déterminer la fonction de répartition de $M_n$ puis celle de $Xn$.
2. Montrer que la suite $(Xn)$ converge en loi.

> Mael a 5 cousins bretons qui viennent du Morbihand...

<details markdown="1">
<summary>Solution</summary>
1.Soit $x$ un reel.

$$
\begin{aligned}
P(M_n\le x) &= P(max(U_1, . . . , U_n)\le x) = P(\{U_1\le x\}\cap...\cap\{U_n\le x\})\\
&= \Pi_{k=1}^n P(\{U_k\le x\}) = (P(U_1\le x))^n\\
&= (F(x))^n
\end{aligned}
$$

ou F designe la fonction de repartition.

Fonction de repartition de la loi $U([0;1])$:

$$
\begin{aligned}
F(x)&=
\begin{cases}
0 &\text{si } x\lt0\\
x &\text{si } x\in[0;1]\\
1 &\text{si } x\gt1
\end{cases}\\
\int_0^x1dt &= x\\
F_n(x)=P(M_n\le x) &=
\begin{cases}
0 &\text{si } x\lt0\\
x &\text{si } x\in[0;1]\\
1 &\text{si } x\gt1
\end{cases}\\
G_n(x) = P(X_n\le x) &= 1-P(X_n\gt x)\\
&= 1-P(n(1-M_n)\gt x)\\
&= 1-P(1-M_n\gt\frac{x}{n}) = 1 - P(-M_n\gt\frac{x}{n}-1)\\
&= 1-P(M_n\lt1-\frac{x}{n})\\ 
&=
\begin{cases}
1-0 &\text{si } 1-\frac{x}{n}\lt0\\
1-(1-\frac{x}{n}) &\text{si } 0\lt1-\frac{x}{n}\lt1\\
1-1 &\text{si } 1-\frac{x}{n}\gt1
\end{cases}\\
&=
\begin{cases}
0 &\text{si } x\lt0\\
1-(1-\frac{x}{n})^n &\text{si } x\in[0;n]\\
1 &\text{si } x\gt1
\end{cases}\\
\end{aligned}
$$

2.Quelle propriete du cours doit-on utiliser ?

Remarquons que:

$$
\lim_{n\to+\infty}G_n(x)=
\begin{cases}
0 &\text{ si } x\lt0\\
1-e^{-x}
\end{cases}\\
$$

Il s'agit de la fonction de repartition de la loi $\xi(1)$

Donc $X_n\Rightarrow^{\text{loi}} \xi(1)$

$\lim_{n\to+\infty}(1+\frac{z}{n})^n = e^{z}$ pour tout reel $z$.

</details>
