---
title:          "OCVX: Parties de R et convexite"
date:           2021-03-18 10:00
categories:     [Image S8, OCVX]
tags:           [Image, SCIA, OCVX, S8]
description: Parties de R et convexite
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/S1Q325eE_)

# Rappels de la seance precedente
- description des sous espaces affine de $\mathbb R^n$
- sous espaces vectoriels de $\mathbb R^n$
    - $E\subset\mathbb R^n$
    - $0_{\mathbb R^n}\in E$
- Sous espace affine $A=x_0+E$, $E$ sous espace vectoriel et $x\in\mathbb R^n$

<div class="alert alert-danger" role="alert" markdown="1">
Un sous-espace affine **n'est pas** un sous-espace vectoriel.
Un sous-espace vectoriel **est** un sous-espace affine.
</div>

![](https://i.imgur.com/t1Wrl7Q.png)


$$
\begin{aligned}
(D) &= \text{{}x\in\mathbb R^n, X_0+\lambda\vec u,\lambda\in\mathbb R\text{}}\\
&= X_0+\text{{}\lambda\vec u,\lambda\in\mathbb R\text{}}\rightarrow\text{description parametrique}
\end{aligned}
$$

![](https://i.imgur.com/PFEiHGx.png)


## Description implicite

<div class="alert alert-info" role="alert" markdown="1">
**Description implicite**: ensemble des points qui verifient une certaine equation
</div>

$$
\begin{aligned}
(D)=dx \text{ tel que } <&x,n>=0\\
&x^Tn=0
\end{aligned}
$$

![](https://i.imgur.com/9QUWj1X.png)
$$
\text{{}x\text{ tel que } <x,n>=b\text{}}\\
\text{si je sais que } x_0\in(D), <x_0,n>=b\\
\begin{aligned}
\text{{}x \text{ tel que }<x,n>=b=<x_0,n>&\text{}}\\
<x,n>-<x_0,n>=0&\text{}}\\
<x-x_0,n> = 0&\text{}}
\end{aligned}
$$

# Description de parties de $\mathbb R^n$
## Ecriture implicite
On se donne une fonction 
$$
\begin{aligned}
f:\mathbb R^n&\to\mathbb R\\
x=\begin{pmatrix}
x_1\\
\vdots\\
x_n
\end{pmatrix}&\mapsto f(x)
\end{aligned}\\
\begin{aligned}
&\mathcal C_0=\text{{}x\in\mathbb R^n\vert f(x)=0\text{}}\\
&\mathcal C_x=\text{{}x\in\mathbb R^n\vert \underbrace{f(x)=x}_{g(x)=f(x)-r, \mathcal C_r(f)=\mathcal C_0(g)}\text{}}\text{ courbe de niveau }x
\end{aligned}
$$

Lieu de sous niveau
$$
\mathcal C_{\le r}(f)=\text{{}x\in\mathbb R^n\vert f(x)\le r\text{}}
$$

## Exemple
$$
\begin{aligned}
f:\mathbb R^2&\to\mathbb R\\
(x,y)&\mapsto x^2+y^2
\end{aligned}
$$

![](https://i.imgur.com/Q5P49I7.png)

## Question 3-10
$$
\begin{aligned}
f:\mathbb R^2&\to\mathbb R\\
(x,y)&\mapsto x^2+y^2
\end{aligned}\\
\begin{aligned}
\mathcal C_0(f)&=\text{{}(0,0)\text{}}\\
\mathcal C_1(f)&=\text{{}(x,y)\in\mathbb R^2 \text{ tel que } x^2+y^2=1\text{}}\Rightarrow\text{ cercle de rayon } 1\\
\mathcal C_2(f)&=\text{ cercle de rayon }\sqrt{2}
\end{aligned}
$$

![](https://i.imgur.com/Q3FuY1T.png)

$$
\begin{aligned}
g:\mathbb R^2&\to\mathbb R\\
(x,y)&\mapsto x^2+4y^2
\end{aligned}\\
$$

<div class="alert alert-warning" role="alert" markdown="1">
Equation d'une ellipse de demi grand axe $a$ et demi petit axe $b$

$$
\text{{}(x,y)\in\mathbb R^2\text{ tel que } (\frac{x}{a})^2+(\frac{y}{b})^2=1\text{}}
$$
![](https://i.imgur.com/QxEQGvv.png)


</div>

$$
a=b=r\\
(\frac{x}{a})^2+(\frac{y}{b})^2=1\Leftrightarrow x^2+y^2=r^2
$$

$$
\begin{aligned}
\mathcal C_0(g)&=\text{{}(0,0)\text{}}\\
\mathcal C_1(g)&=\text{{}(x,y)\in\mathbb R^2 \text{ tel que } \underbrace{x^2+4y^2=1}_{(\frac{x}{1})^2+(\frac{y}{\frac{1}{2}})^2=1}\text{}}\\
\mathcal C_2(g)&=\text{ de meme que }\mathcal C_1
\end{aligned}
$$
![](https://i.imgur.com/t0PEAHw.png)

## Question 3-11
Surface definie apr les 2 branches d'une hyperbole $y\mapsto\frac{1}{x}$

![](https://i.imgur.com/pNes7aG.png)

$$
\text{{}(x,y)\in\mathbb R^2, \underbrace{y=\frac{1}{x}}_{xy=1}\text{}}\\
\begin{aligned}
g:\mathbb R^2&\to\mathbb R\\
(x,y)&\mapsto xy
\end{aligned}\\
y\le\frac{1}{x}\Leftrightarrow yx\le1
$$

![](https://i.imgur.com/KUjlhq8.png)

<div class="alert alert-success" role="alert" markdown="1">
Donc pour la decrire:

$$
\text{{}(x,y)\in\mathbb R^2, xy\le1\text{}}=\mathcal C_{\le1}(g)
$$
</div>

## Ecriture parametrique
### Exemples
$$
\begin{aligned}
f:\mathbb R&\to\mathbb R\\
t&\mapsto f(t)
\end{aligned}\\
graph(f)\subset\mathbb R^2\\
\text{{}(t,f(t)),t\in\mathbb R\text{}}\rightarrow\text{ ecriture parametrique}
$$

![](https://i.imgur.com/hmzVeR1.png)

$$
\begin{aligned}
f:\mathbb R^2&\to\mathbb R\\
(x,y)&\mapsto x^2+y^2
\end{aligned}\\
graph(f)=\text{{}(x,y),f(x,y)),(x,y)\in\mathbb R^2\text{}}
$$

![](https://i.imgur.com/1SUMFS4.png)

### Definition
<div class="alert alert-info" role="alert" markdown="1">
Soit
$$
\begin{aligned}
f:\mathbb R^n&\to\mathbb R\\
t&\mapsto f(t)
\end{aligned}\\
graph(f)=\text{{}(t,f(t)),t\in\mathbb R^n\text{}}
$$
</div>

Avec une ecriture parametrique, on peut se ramener a une ecriture implicite

![](https://i.imgur.com/p8sJDe6.png)


$$
y=f(x)\Leftrightarrow f(x)-y=0\\
graph(f)=\text{{}(x,f(t)),x\in\mathbb R\text{}}\\
\begin{aligned}
graph(f) &= \text{{}(x,y),x\in\mathbb R,y=f(x)\text{}}\\
&= \text{{}(x,y), x\in\mathbb R\,\underbrace{f(x)-y}_{g(x,y)}=0\text{}}\\
&=\text{{}(x,y), g(x,y)=0\text{}}=\mathcal C_0(g)
\end{aligned}
$$

## Epigraphe (au-dessus du graphe) d'une fonction $f$
$$
Epi(f) = \text{{}(x,t),t\ge f(x)\text{}}
$$

![](https://i.imgur.com/QRdLsKH.png)

# Convexite dans $\mathbb R^n$
## Parties convexes de $\mathbb R^n$
> On va dessiner des patates et des haricots

![](https://i.imgur.com/mT6hk39.png)
*Quelle forme est convexe ?*

<div class="alert alert-danger" role="alert" markdown="1">
Si on prend 2 points quelconque de $A$ et qu'on trace ce segment, alors le segment est **inclut** dans $A$
</div>

![](https://i.imgur.com/HSmRVG8.png)

<div class="alert alert-success" role="alert" markdown="1">
$A$ est convexe et $B$ ne l'est pas.
</div>

Pour un segment entre $x$ et $y$, n'importe quel point de ce segments est une **proportion** du segment

![](https://i.imgur.com/ZN50JHY.png)
$$
tx+(1-t)y, t\in[0;1]\\
\begin{aligned}
t&=0\to y\\
t&=1\to x\\
t&= \frac{1}{2}\to\text{milieu de } [x,y]
\end{aligned}
$$

<div class="alert alert-danger" role="alert" markdown="1">
**A CONNAITRE**
<div class="alert alert-info" role="alert" markdown="1">
**Definition**: Une partie $A\subseteq\mathbb R^n$ est convexe si, et seulement si
$$
\forall x,y\in A\\
\forall t\in[0;1]\\
tx+(1-t)y\in A
$$
</div>

</div> 

### Proprietes
- tout intervall de $\mathbb R$ est convexe
- les sous espaces affines/les demi espaces sont convexes

On a $A$ et $B$ convexes
- $A\cap B\to$ convexe
- $A\cup B\to$ en general pas convexe

![](https://i.imgur.com/WxdxHKf.png)

## Enveloppe convexe d'une partie $A\subseteq\mathbb R^n$

![](https://i.imgur.com/qbMx7m8.png)

Si on a une forme non-convexe, on "bouche les trous" pour rendre la forme convexe et on obtient $conv(A)$

<div class="alert alert-info" role="alert" markdown="1">
Intersection de tous les convexes qui $\supseteq$ $A$.
- plus petit convexe qui $\supseteq$ $A$
</div>

Soit $A$ une partie de $\mathbb R^n$
$x$ un point du bord si $\forall\varepsilon\gt0, B(x,\varepsilon)\cap A\neq \emptyset$ $\to$ bord/frontiere $\delta A$

<div class="alert alert-info" role="alert" markdown="1">
On appelle:
- adherence de $A$, $\bar A=A\cup \delta A$
- interieur de $A$, $\dot A=A \setminus\delta A$
</div>

$$
A=[0;1[\to\begin{cases}
    \delta A = \text{{}\text{{}0\text{}};\text{{}1\text{}}\text{}}\\
    \bar A = [0;1]\\
    \dot A = ]0;1[
\end{cases}
$$

## Hyperplan d'appui

<div class="alert alert-info" role="alert" markdown="1">
$A$ admet un hyperplan d'appui en $x\in\delta A$
Si on peut definir un hyperplan qui separe l'espace en deux demi espaces tels que $A$ tombe integralement dans l'un des deux.

![](https://i.imgur.com/Js6UBeI.png)
</div>

<div class="alert alert-warning" role="alert" markdown="1">
$A$ admet un hyperplan d'appui de normale $\vec n$ en $x\in\delta A$ si, et seulement si,
$$
\forall y\in A, <y-x,n>\le0
$$

![](https://i.imgur.com/rTX8TqU.png)

</div>

## Question 3-20
- N’ayant pas d’hyperplan d’appui en un point donné de son bord:

![](https://i.imgur.com/r7oWRL6.png)
Haricots $\to$ pas d'hyperplan d'appui en certains points de son bord.

- Ayant plus d’un hyperplan d’appui en un même point: il faut un angle

![](https://i.imgur.com/4T0pIdP.png)

Point anguleux $\to$ plusieurs hyperplan d'appuis en ce point la

- N’ayant aucun hyperplan d’appui:

![](https://i.imgur.com/s7duGFr.png)

Pas d'hyperplan d'appui pour tous les points de bord.

- Ayant un hyperplan d'appui en tous les points de son bord:

![](https://i.imgur.com/2iw357L.png)

Pour tous les convexes

<div class="alert alert-warning" role="alert" markdown="1">
Une partie est convexe ssi on peut definir un hyperplan d'appui en tout point de son bord.
</div>

## Fonction convexes

<div class="alert alert-danger" role="alert" markdown="1">
**A CONNAITRE**
<div class="alert alert-info" role="alert" markdown="1">
Une fonction $f:\mathbb R^n\to\mathbb R$ est convexe ssi:
- $Dom f$ est convexe
- $\forall x,y\in Dom f$, $\forall t\in[0;1]$
    - $f(tx+(1-t)y)\le tf(x)+(1-t)f(y)$

![](https://i.imgur.com/DgMArOq.png)

</div>
</div>

<div class="alert alert-warning" role="alert" markdown="1">
$f$ concave si $-f$ convexe.
</div>

Les droites affines sont les seules fonctions concaves ET convexes
![](https://i.imgur.com/AH4uLza.png)

Petit bestiaire de fonctions convexes:
- $ax+b$
- $e^{\alpha x}, \forall\alpha\in\mathbb R$
- $ax^2+bx+c$, $a\ge0$
- $-\log(x)=\log(\frac{1}{x})$
- $\sqrt{x}$
- $x^n$, $n$ pair

![](https://i.imgur.com/i9Gs2qT.png)

<div class="alert alert-warning" role="alert" markdown="1">
La somme ponderee positivement de fonctions convexes est une fonction convexe

$$
f_{i_{i\ge 0}},i=1,...,N\text{convexes}\\
f=\sum_{i=1}^N\omega_if_i\\
$$
</div>

### Demonstration
$$
Dom f=\cap Dom f_i\to\text{ convexe}
$$

Soit $x,y\in Dom f$ et $t\in[0;1]$

$$
\begin{aligned}
f(tx+(1-t)y)&=\sum_{i=1}^N\omega_i\underbrace{f_i(tx+(1-t)y)}_{\le tf_i(x)+(1-t)f_i(y)\text{ car } f \text{ convexe}}\\
&\le \sum_{i=1}^N\omega_itf_i(x) + \sum_{i=1}^N\omega_i(1-t)f_i(y)\\
&\le t\underbrace{\sum_{i=1}^N\omega_if_i(x)}_{f(x)} + (1-t)\underbrace{\sum_{i=1}^N\omega_if_i(y)}_{f(y)}\\
f(tx+(1-t)y)&\le tf(x)+(1-t)f(y)
\end{aligned}
$$
- $f=\max_{i=1,...,n}f_i$ est convexe
- la composition d'une fonction convexe $f$ avec $g$ affine croissant $g\circ f$ est convexe

Lien entre partie convexe et fonction convexe:
- L'epigraphe d'une fonction convexe est une partie convexe

![](https://i.imgur.com/sfC8JsG.png)

- Tous les lieux de sous niveaux d'une fonction convexe sont des parties convexes

![](https://i.imgur.com/Ko1N4Z5.png)

En dimension 1:
![](https://i.imgur.com/IEt0cU3.png)
