---
title:          "ASE3: Couple de variables aleatoires discretes et analyse des donnees - 1"
date:           2021-05-12 10:00
categories:     [tronc commun S8, ASE3]
tags:           [tronc commun, ASE3, S8, couple]
description: Couple de variables aleatoires discretes et analyse des donnees - 1
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/Skg3alKu_)

# Couple de variables aleatoires reelles et discretes

Soient $X$ et $Y$ 2 v.a reelles discretes.

<div class="alert alert-info" role="alert" markdown="1">
On appelle couple $(X,Y)$ l'application de $\Omega\to\mathbb R^2$ definie par $(X,Y)(\omega)=(X(\omega), Y(\omega))$

</div>

$X$ et $Y$ sont definis sur un meme espace probabilite ($$\underbrace{\Omega}_{\text{univers}}, \underbrace{\mathcal C}_{\text{tribu}}, \underbrace{P}_{\text{probabilite}}$$)

## La loi d'un couple $(X,Y)$ (Loi conjointe)

<div class="alert alert-info" role="alert" markdown="1">
**Definition**
On appelle loi de $(X,Y)$ l'ensemble des couples $((x_i,y_j), P_{i,j})$ ou 
- $x_i\in X(\Omega)$ l'ensemble des valeurs de $X$
- $y_j\in Y(\Omega)$ l'ensemble des valeurs de $Y$

<div class="alert alert-danger" role="alert" markdown="1">
$$
P_{ij} = \mathbb P((X=x_i)\cap(Y=y_j))
$$
</div>

</div>

Si $I = [[1, r]]$ et $J = [[1,s]]$ (ensemble discret, ensemble des indices). Les $P_{i,j}$ sont souvent donnes dans le tableau a double entres.

|$X /Y$|$y_1$|$\dots$|$y_j$|$\dots$|$y_s$|
|-|-|-|-|-|-|
|$x_1$|$P_{1,1}$|$\dots$|$P_{1,j}$|$\dots$|$P_{1,s}$|
|$\vdots$|$\vdots$||$\vdots$||$\vdots$|
|$x_i$|$P_{i,1}$|$\dots$|$P_{i,j}$|$\dots$|$P_{1,s}$|
|$\vdots$|$\vdots$||$\vdots$||$\vdots$|
|$x_r$|$P_{r,1}$|$\dots$|$P_{r,j}$|$\dots$|$P_{r,j}$|

<div class="alert alert-danger" role="alert" markdown="1">

$$
P_{i,j} \gt 0 \quad\text{et}\quad\sum_{i\in I\\ j\in J}P_{ij} = 1
$$

</div>

## Lois marginales

<div class="alert alert-info" role="alert" markdown="1">
**Definition**
Les v.a $X$ et $Y$ sont appelees variables marginales du couple $(X,Y)$. La loi de $X$ (resp. de $Y$) est appelee loi marginale de $X$ (resp. de $Y$)
</div>

**Notation**: 

$$
\forall i\in I, P(X=x_i)=P_{i\circ} \text{ et } P(X=y_j)=P_{\circ j} \\
P_{i\circ} = P(X=x_i) = \sum_{j\in J}P((X=x_i)\cap(Y=y_j)) = \sum_{j\in J}P_{ij}\\
\forall j\in J\quad P_{\circ j}=\sum_{i\in I}P((X=x_i)\cap(Y=y_j)) = \sum_{i\in I}P_{ij}
$$

### Exemple
$(X,Y)$ un couple de v.a. dont la loi conjointe est donnee par le tableau:



| $X / Y$ | 1 | 2 | 3 | 4 |$P_{i\circ}$ (Loi marginale de $X$)|
| - | - | - |-|-|-|
| 1 |$\frac{1}{16}$| $\frac{1}{16}$ | $\frac{1}{16}$ | $\frac{1}{16}$|$\frac{1}{4}$|
| 2 | 0 | $\frac{2}{16}$ |$\frac{1}{16}$| $\frac{1}{16}$ |$\frac{1}{4}$|
| 3 | 0 | 0 | $\frac{3}{16}$ | $\frac{1}{16}$ |$\frac{1}{4}$|
| 4 | 0 | 0 | 0| $\frac{4}{16}$ |$\frac{1}{4}$|
| $P_{\circ j}$ (Loi marginale de $Y$) | $\frac{1}{16}$ | $\frac{3}{16}$ |$\frac{5}{16}$ | $\frac{7}{16}$|1|

## Loi conditionnelles

<div class="alert alert-info" role="alert" markdown="1">
**Definition**

Soit $X$ une v.a reelle sur $(\Omega, \mathcal C, P)$

$$
X(\Omega) = \{x_i\vert i\in I\}, \text{soit } A\text{ un evenement }/P(A)\neq 0
$$

La loi conditionnelle de $X$ sachant $A = \{(x_i, P_A(X=x_i)), i\in I\}$

<div class="alert alert-danger" role="alert" markdown="1">

$$
P_A(X=x_i) = \frac{P((X=x_i)\cap A)}{P(A)}
$$

</div>

</div>

En particulier, $A$: <<$Y=y_i$>>

$$
P_{(Y=y_i)}(X=x_i)=\frac{P((X=x_i)\cap(Y=y_i))}{P(Y=y_j)}=\frac{P_{i,j}}{P_{\circ j}}
$$

<div class="alert alert-success" role="alert" markdown="1">

$$
P_{(Y=y_j)}(X=x_i) = \frac{P_{i,j}}{P_{\circ j}}
$$

</div>

### Exemple
On reprend l'exemple precedent

|$X_i$|1|2|3|4|
|-|-|-|-|-|
|$P_{(Y=3)}(X=x_i)$|$\frac{1}{5}$|$\frac{1}{5}$|$\frac{3}{5}$|$0$|

$$
P_{(Y=3)}(X=1)=\frac{P((X=1)\cap(Y=3))}{P(Y=3)}=\frac{\frac{1}{16}}{\frac{5}{16}} = \frac{1}{5}
$$

### Independantes
<div class="alert alert-info" role="alert" markdown="1">
**Definition**
$X$ et $Y$ sont 2 v.a. independantes ssi

<div class="alert alert-danger" role="alert" markdown="1">

$$
P((X=x)\cap(Y=y)) = P(X=x)P(Y=y)\quad\forall x\in X(\omega), \forall y\in Y(\omega)\\
\Leftrightarrow P_{ij} = P_{i\circ} \circ P_{\circ j}
$$

</div>

</div>

Soit g une fonction de $\mathbb R^2\to\mathbb R$, definie sur l'ensemble des valeurs prises par $(X,Y)$
Soit $Z=g(X,Y)$, $Z_h=g(x_i,y_j)\in Z(\Omega)$

$$
(Z=Z_k) = \cup_{(i,j) \\ Z_k = g(x_i,y_j)}((X=x_i)\cap(Y=y_j))\Rightarrow\color{red}{P(Z=Z_k)=\sum_{(i,j) \\ Z_k = g(x_i,y_j)}P((X=x_i)\cap(Y=y_i))}
$$

En particulier $Z=X+Y=g(X,Y)$

$$
P(Z=z) = \sum_{(x,y) \\ x+y=z}P((X=x)\cap(Y=y))
$$

Si $Z=X.Y=g(X,Y)$

$$
P(X.Y=z) = \sum_{(x,y) \\ x.y=z}P((X=x)\cap(Y=y))
$$

### Exemple

$(X,Y)$ couple defini par 

|$X / Y$|1|2|3|4|
|-|-|-|-|-|
|1|$\frac{1}{16}$|$\frac{1}{16}$|$\frac{1}{16}$|$\frac{1}{16}$|
|2|0|$\frac{2}{16}$|$\frac{1}{16}$|$\frac{1}{16}$|
|3|0|0|$\frac{3}{16}$|$\frac{1}{16}$|
|4|0|0|0|$\frac{4}{16}$|

Determiner la loi de $Z=X+Y$

<details markdown="1">
<summary>Solution</summary>

$$Z=\{2,3,4,5,6,7,8\}$$

|$Z_k$     |2|3|4|5|6|7|8|
|-         |-|-|-|-|-|-|-|
|$P(Z=Z_k)$|$\frac{1}{16}$|$\frac{1}{16}$|$\frac{3}{16}$|$\frac{2}{16}$|$\frac{4}{16}$|$\frac{1}{16}$|$\frac{4}{16}$|

$$
\begin{aligned}
P(Z=5) &= P(X+Y=5)\\
&= P((X=1)\cap(Y=4)) P((X=2)\cap(Y=3)) + P((X=3)\cap(Y=2)) + P((X=4)\cap(Y=1))\\
&= \frac{1}{16} + \frac{1}{16} + 0 + 0 =\frac{2}{16} = \frac{1}{8}
\end{aligned}
$$

</details>

Determiner la loi de $Z=X.Y$

<details markdown="1">
<summary>Solution</summary>

$$Z(\Omega) = \{1,2,3,4,6,8,9,12,16\}$$

|$Z_k$|1|2|3|4|6|8|9|12|16|
|-----|-|-|-|-|-|-|-|--|--|
|$P(Z=Z_k)$|$\frac{1}{16}$|$\frac{1}{16}$|$\frac{1}{16}$|$\frac{3}{16}$|$\frac{1}{16}$|$\frac{1}{16}$|$\frac{3}{16}$|$\frac{1}{16}$|$\frac{4}{16}$|

$$
\begin{aligned}
P(Z=4) &= P((X=1)\cap(Y=4)) + P((X=2)\cap(Y=2)) + P((X=4)\cap(Y=1))\\
&= \frac{1}{16} + \frac{2}{16} + 0 = \color{red}{\frac{3}{16}}
\end{aligned}
$$


</details>

## Esperance d'une fonction de 2 v.a.r discretes

$$
\begin{aligned}
X(\omega)=\{x_1,...,x_i\}\\
Y(\omega)=\{y_1,...,y_j\}
\end{aligned}
\biggr\}Z=g(X,Y)\\
E(Z) = E(g(X,Y)) = \sum_{i,j}g(x_i,y_j)P((X=x_i)\cap(Y=y_i))
$$

<div class="alert alert-success" role="alert" markdown="1">

$$
E(Z) = \sum_{i,j}g(x_i,y_j)P_{i,j}
$$

</div>

### Exemple
$g(X,Y) = X,Y$

<div class="alert alert-success" role="alert" markdown="1">

$$
\begin{aligned}
E(X.Y) &= \sum_{i,j}x_iy_jP((X=x_i)\cap(Y=y_j)) \\
&= \sum_{i,j}x_iy_jP_{i,j}
\end{aligned}
$$

</div>

## Proposition
<div class="alert alert-info" role="alert" markdown="1">
**Proposition**
Si $X$ et $Y$ sont 2 v.a. independantes alors

<div class="alert alert-danger" role="alert" markdown="1">

$$
E(X.Y) = E(X)E(Y)
$$

</div>

</div>

### Demonstration

$$
E(X.Y) = \sum_{i=1}^r\sum_{j=1}^sx_iy_jP_{i,j}
$$

or $X$ et $Y$ sont independantes $P_{i,j} = P_{i\circ}\circ P_{\circ j}$

$$
\begin{aligned}
E(X.Y) &=\sum_{i=1}^r\sum_{j=1}^sx_iy_jP_{i\circ}P_{\circ j}\\
&= \sum_{i=1}^rx_iP_i\biggr(\sum_{j=1}^sy_jP_{\circ j}\biggr)\\
&= \sum_{i=1}^rx_iP_{i\circ}E(Y)=E(X)E(Y)
\end{aligned}
$$

<div class="alert alert-success" role="alert" markdown="1">

$$
E(X.Y) = E(X)E(Y)
$$

</div>

<div class="alert alert-warning" role="alert" markdown="1">
La reciproque est fausse
</div>

### Contre-exemple

$(X,Y)$ couple de loi conjointe

|$X / Y$|0|1|2|$P_{i\circ}$ (Loi de $X$)|
|-------|-|-|-|-------------------------|
|0|$\frac{1}{20}$|$\frac{1}{4}$|0|$\frac{3}{10}$|
|1|$\frac{17}{60}$|$\frac{1}{4}$|$\frac{1}{6}$|$\frac{7}{10}$|
|$P_{\circ j}$ (Loi de $Y$)|$\frac{1}{3}$|$\frac{1}{2}$|$\frac{1}{6}$|$1$|

$$
\begin{aligned}
E(X.Y) &= \sum_{i=0}^1\sum_{j=0}^2i.jP_{i,j}\\
&= 1\times\frac{1}{4}+2\times\frac{1}{6} = \frac{1}{4} + \frac{1}{3} = \frac{7}{12}\\
E(X) &= \sum_{i=0}^1iP_{i\circ}=\frac{7}{10}\\
E(Y) &= \sum_{j=0}^2jP_{\circ j} = \frac{1}{2} + \frac{2}{6} = \frac{5}{6}\\
E(X.Y) &= \frac{7}{12} = E(X)E(Y)
\end{aligned}\\
$$

et pourtant $X$ et $Y$ ne sont pas independantes car

$$
P((X=0)\cap(Y=2)) = 0\\
P(X=0).P(Y=2) = \frac{3}{10}\times\frac{1}{6}=\frac{1}{20}
$$

## Covariance et coefficient de correlation lineaire

<div class="alert alert-info" role="alert" markdown="1">
**Definition**
$X$ et $Y$ 2 v.a. discretes.
On appelle covariance de $(X,Y)$ le nombre reel

<div class="alert alert-danger" role="alert" markdown="1">

$$
Cov(X,Y)=E((X-E(X)(Y-E(Y))))
$$

</div>
</div>

<div class="alert alert-info" role="alert" markdown="1">
**Proposition**

$$
Cov(X,Y)=E(X.Y) - E(X)E(Y)
$$

</div>

### Demonstration

$$
\begin{aligned}
Cov(X,Y) &= E(\overbrace{(X-E(X))}^{\text{var centree}}\overbrace{(Y-E(Y))}^{\text{var centree}})\\
&= E(XY-XE(Y) - E(X)Y + E(X)E(Y))\\
&= E(X.Y) - E(Y)E(X) - E(X)E(Y) + E(X)E(Y)
\end{aligned}
$$

Cat $E$ est lineaire

<div class="alert alert-success" role="alert" markdown="1">

$$
Cov(X,Y) = E(XY) - E(X)E(Y)
$$

</div>

**Remarque**: Si $X$ et $Y$ sont independantes alors $Cov(X,Y)=0$

<div class="alert alert-info" role="alert" markdown="1">
**Definition**
On appelle coefficient de correlation lineaire

<div class="alert alert-danger" role="alert" markdown="1">

$$
\mathcal C(X,Y)=\frac{Cov(X,Y)}{\sigma_x\sigma_y}
$$

</div>

- $\sigma_x=\sqrt{V(X)}$
- $\sigma_y=\sqrt{V(Y)}$
</div>
