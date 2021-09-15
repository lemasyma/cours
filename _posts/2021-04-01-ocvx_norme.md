---
title:          "OCVX: Norme"
date:           2021-04-01 10:00
categories:     [Image S8, OCVX]
tags:           [Image, SCIA, OCVX, S8]
description: Norme
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/S1R87WmB_)

<div class="alert alert-info" role="alert" markdown="1">
Norme:

$$
\begin{aligned}
\Vert.\Vert.\mathbb R^n&\to\mathbb R^1\\
x&\mapsto\Vert x\Vert
\end{aligned}
$$
</div>

- separation: $\Vert x\Vert=0\Rightarrow x=0$
- homogeneite: $\Vert\lambda x\Vert=\vert\lambda\vert\Vert x\Vert$
- inegalite triangulaire: $\forall x,y\in\mathbb R^n, \Vert x+y\Vert\le\Vert x\Vert+\Vert y\Vert$
- inegalite triangulaire inversee: $\forall x,y\in\mathbb R^n,\biggr\vert\Vert x\Vert-\Vert y\Vert\biggr\vert\le\Vert x-y\Vert$

$$
\Vert x\Vert=\Vert x+y-y\Vert\le\Vert x-y\Vert+\Vert y\Vert\\
\Leftrightarrow \Vert x\Vert-\Vert y\Vert\le\Vert x-y\Vert\\
\Vert y\Vert=\Vert y-x+x\Vert\le\underbrace{\Vert y-x\Vert}_{\Vert x-y\Vert}+\Vert x\Vert=\Vert x-y\Vert + \Vert x\Vert\\
\Leftrightarrow\Vert y\Vert -\Vert x\Vert\le\Vert x-y\Vert\\
\Rightarrow \biggr\vert\Vert x\Vert-\Vert y\Vert\biggr\vert\le\Vert x-y\Vert
$$

<div class="alert alert-info" role="alert" markdown="1">
A partir d'une norme, on peut definir une distance

$$
d_{\Vert.\Vert}=\Vert x.y\Vert
$$
</div>

<div class="alert alert-warning" role="alert" markdown="1">
Tout produit scalaire permet de definir une norme

$$
\Vert x\Vert=\sqrt{<x.x>}
$$
</div>

En particulier:
- $p=1$, $\Vert x\Vert_1=\sum_{i=1}^n\vert x_i\vert$
- $p=2$, $\Vert x\Vert_2=\sqrt{\sum_{i=1}^nx_i^2}$
- $p=\infty$, $$\Vert x\Vert_{\infty} = \max_{i=1,...,n}\vert x\vert$$

## Question 3.30

$$
\begin{aligned}
\Vert x-y\Vert_1&=\vert x_1.y_1\vert+\vert x_2.y_2\vert\\
&= \vert 1-3\vert+\vert2-1\vert\\
d_{\Vert.\Vert_1}(xy)&=3
\end{aligned}
$$
Distance de Manhattan

$$
\begin{aligned}
\Vert x-y\Vert_2&=\sqrt{(x_1-y_1)^2+(x_2-y_2)^2}\\
d_{\Vert.\Vert_2}&= \sqrt{4+1}\\
&=5
\end{aligned}
$$

$$
d_{\Vert.\Vert_{\infty}}=\Vert x-y\Vert_{\infty} = \max(2,1)=2
$$

# Notion de voisinage
Notion de voisinnage/boule ouverte
$\rightarrow$ generalise la notion d'intervallle pour $\mathbb R^n$, $n\ge2$
Boule ouverte centree sur un point $x_0$ de rayon $r$

$$
\mathcal B_{\Vert\Vert}(x_0,\varepsilon)=\text{{}y\in\mathbb R^n\vert\Vert x_0-y\Vert\le \varepsilon\text{}} \text{ boule ouverte}\\
$$

$$
\bar{\mathcal B}_{\Vert\Vert}(x_0,\varepsilon)=\text{{}y\in\mathbb R^n,\Vert x_0-y\Vert\le \varepsilon\text{}} \text{ boule fermee}
$$

Voisinnage de $x_0$:
$$
\mathcal V(x_0)\subseteq\mathbb R^n \text{ tq }  \exists\varepsilon\gt0\\
\mathcal B_{\Vert\Vert}(x_0,\varepsilon)\in \mathcal V(x_0)
$$

## Question 3.31

$$
\mathcal{\bar B_2}(0,1):\\
x\in(\delta\mathcal B_2(0,1))\\
\text{{}x\in\mathbb R^1,\underbrace{\Vert x\Vert_1=1\text{}}}_{x_1^2+x_2^2=1}
$$

![](https://i.imgur.com/VDKOS3j.png)



$$
\mathcal{\bar B_1}(0,1):\\
x\in\delta\mathcal B_1(0,1)\\
\text{{}x\in\mathbb R^2,\underbrace{\Vert x\Vert_2=1}_{\vert x_1\vert+\vert x_2\vert=1}\text{}}
$$

Si $x_1\gt0$, $x_2\gt0$, $x_2=1-x_1$

![](https://i.imgur.com/EXxtfVx.png)


$$
\mathcal{\bar B_{\infty}}:\\
x\in\delta\mathcal B_{infty}(0,1)\\
\text{{}x\in\mathbb R^2, \max(\vert x_1\vert,\vert x_2\vert)=1\text{}}
$$

![](https://i.imgur.com/x7KzRqA.png)

Nos formes s'emboitent:

![](https://i.imgur.com/UE3hqbO.png)

*$0\lt p\lt 1?$*
$\Vert.\Vert_p$ est une **quasi norme** $\rightarrow$ inegalite triangulaire

*$p=0?$*
$\Vert x\Vert_0=$ nombre de coordonnees non nulles du vecteur $x$

$\mathcal B_p(0,1)$ convexe ?

<div class="alert alert-warning" role="alert" markdown="1">
$A$ convexe: $\forall x,y\in A, \forall t\in[0,1]$, $tx+(1-ty)\in A$
</div>

$$
x,y\in\mathbb B_p(0,1)\Leftrightarrow \Vert x\Vert_p-\Vert y\Vert_p\lt1\\
\begin{aligned}
t\in[0,1], \Vert \underbrace{tx+(1-t)y}_{\in\mathbb B_p(0,1)}\Vert_p &\le\Vert tx\Vert_p + \Vert(1-t)y\Vert \text{ inegalite triangulaire}\\
&\le t\underbrace{\Vert x\Vert_p}_{\le 1} + (1-t)\underbrace{\Vert y\Vert_p}_{\le 1}\\
&\le t + (1-t)\\
&\le 1
\end{aligned}
$$


$\mathcal B_p(0,1)=\mathcal C_{\lt 1}\Vert.\Vert_p=$ lien de sous niveau (strict) 1.
Donc si $\Vert.\Vert_p:x\mapsto\Vert x\Vert_p$ est une fonction convexe, $\mathcal B_p(0,1)=\mathcal C_{\lt 1}\Vert.\Vert_p$ est une partie convexe.
$\rightarrow(1-t)y\le tf(x)+(1-t)f(y)$

![](https://i.imgur.com/6LNAZGv.png)


# Continuite d'une fonction de $\mathbb R^n\to\mathbb R^p$

![](https://i.imgur.com/oUkODf5.png)

$f$ continue en $a$

$$
\forall\varepsilon\gt0,\exists\eta\gt0, \vert x-a\vert\lt\eta\Rightarrow\vert f(x)-f(a)\vert\lt\varepsilon
$$

Continuite d'une fonction de $\overbrace{\mathbb R^n}^{\Vert.\Vert_n}\to\overbrace{\mathbb R^p}^{\Vert.\Vert_p}$

<div class="alert alert-info" role="alert" markdown="1">
$f$ continue en $a$ $\Leftrightarrow$
$$
\forall\varepsilon\gt0,\exists\eta\gt0, \underbrace{\Vert x-a\Vert\_{\alpha}lt\eta}_{x\in \mathcal B_{\alpha}(a,\eta)}\Rightarrow\underbrace{\Vert f(x)-f(a)\Vert_{\beta}\lt\varepsilon}_{x\in \mathcal B_{\beta}(f(a),\varepsilon)}
$$
</div>

## Equation de normes

<div class="alert alert-info" role="alert" markdown="1">
$\Vert.\Vert_{\alpha}$ et $\Vert.\Vert_{\beta}$ sont equivalentes ssi $\exists A,B\gt0$ tels que

$$
\forall x\in\mathbb R^n, A\Vert x\Vert_{\beta}\le\Vert x\Vert_T\le B\Vert x\Vert_{\beta}
$$
</div>

<div class="alert alert-danger" role="alert" markdown="1">
**Theoreme**
Toutes les normes sont equivalentes en dimension finie

![](https://i.imgur.com/5jqZxa8.png)

</div>


## Fonctions lipschitzienne
<div class="alert alert-info" role="alert" markdown="1">
**Definition: Fonctions lipschitzienne**
Une fonction est $K-$lipschitzienne s'il existe $K\gt0$ tel que

$$
\forall x,y\in\mathbb R^n, \Vert f(x)-f(y)\Vert\le K\Vert x-y\Vert
$$

</div>

<div class="alert alert-danger" role="alert" markdown="1">
**Theoreme**
Toute fonction lipschitzienne est *continue*.
</div>


### Exemple
$$
\begin{aligned}
f:\mathbb R^2&\to\mathbb R\\
x=\begin{pmatrix}x_1\\ x_2\end{pmatrix}&\mapsto x_1+x_2
\end{aligned}\\
\begin{aligned}
\begin{cases}
    x\in\mathbb R^2\\
    y\in\mathbb R^2
\end{cases}
\quad \Vert f(x)-f(y)\Vert&=\vert(x_1+x_2)-(y_1+y_2)\vert\\
&= \vert(x_1-y_1)+(x_2-y_2)\vert\le\vert x_1-y_1\vert+\vert x_2-y_2\vert
\end{aligned}\\
\Vert x- y\Vert=\biggr\Vert\begin{pmatrix}x_1\\ x_2\end{pmatrix}-\begin{pmatrix}y_1\\ y_2\end{pmatrix}\biggr\Vert=\biggr\Vert\begin{pmatrix}x_1 - y_1\\ x_2-y_2\end{pmatrix}\biggr\Vert_1=\vert x_1-y_1\vert+\vert x_2-y_2\vert
$$

## Fonctions continues

- Toutes les fonctions polynomiales sont continues.
- Toutes les fractions rationnelles $\frac{f(x)}{g(x)}, x\in\mathbb R^n$ sont continues partout ou $g(x)\neq0$
- Si $f:\mathbb R^n\to\mathbb R^p$ continue, $g:\mathbb R^n\to\mathbb R^p$ continue, $\lambda,\mu\in\mathbb R$ alors $\lambda f-\mu g$ continue.
- Si $p=1$, $fg$ continue, $\frac{f}{g}$ continue partout ou $g$ ne s'annule pas.
- Si $f:\mathbb R^n\to\mathbb R^p$ continue, $f:\mathbb R^p\to\mathbb R^n$ continue, alors $g\circ f:\mathbb R^n\to\mathbb R^m$ continue

### Exemple

$$
\begin{aligned}
f:\mathbb R^2&\to\mathbb R\\
(x,y)&\mapsto x+y
\end{aligned}
$$

*Est-ce que $x\mapsto f(x,0)$ et $y\mapsto f(0,y)$ continues $\Rightarrow$ $f$ continue ?*
Bah non ca sera trop beau.

$$
\underbrace{x\mapsto f(x,0)}_{f\circ g(t)\text{ avec } g:t\mapsto(t,0)}\\
\begin{aligned}
f:\mathbb R^2&\to\mathbb R\\
(x,y)&\mapsto
\begin{cases}
    \frac{xy}{x^2+y^2} &(x,y)+(0,0)\\
    0 &(x,y)=(0,0)
\end{cases}
\end{aligned}
$$

- Si $g:t\to(t,0)$, $f\circ g(t)=0$ $\forall t\in\mathbb R$
- Si $g:t\to(0,t)$, $f\circ g(t)=0$ $\forall t\in\mathbb R$
- Si $g:t\to(t,t)$, 

$$
f\circ g(t)=
\begin{cases}
\frac{1}{2} &t\neq0\\
0 &t=0
\end{cases}
\forall t\in\mathbb R
$$

## Exercice 3.34

<div class="alert alert-warning" role="alert" markdown="1">
**Rappel**
$$
\Vert x\Vert_1 = \sum_{i=1}^n\vert x\vert\\
\Vert x\Vert_2=\sqrt{\sum_{i=1}^nx^2}\\
\Vert x\Vert_{\infty}=\max_{i=1,..,n}\vert x_i\vert
$$
</div>

$$
\Vert x\Vert_1=\Vert x\Vert_{\infty}+\sum\vert\underbrace{\text{toutes les valeurs qui ne sont pas le max}}_{\ge 0}\vert\\
\Vert x\Vert_{\infty}\le \Vert x\Vert_1\le n\Vert x\Vert_{\infty}\\
\begin{aligned}
\Vert x\Vert_2\le\Vert x\Vert_1\quad \Vert x\Vert_2^2&=\sum_{i=1}^nx_i^2=\sum_{i=1}^n\vert x_i\vert^2\\
\Vert x\Vert_1^2&=(\sum_{i=1}^n\vert x_i\vert)^2= \sum_{i=1}^n\vert x_i\vert^2 + 2\sum_{1\le i\le j\le n}\vert x_i\vert \vert x_j\vert
\end{aligned}\\
\begin{aligned}
\Vert x\Vert_{\infty}&=\max_i\vert x_i\vert=\vert x_{\underbrace{j}_{\text{index ou le max est atteint}}}\vert\\
&= \sqrt{x_j^2}\\
\Vert x\Vert_2 &= \sqrt{\sum_{i=1}^nx_i^2}\\
&=\sqrt{x_j^2+\underbrace{\sum_{i\neq j}x_i^2}_{\ge0}}\\
&\ge\sqrt{x_j^2}\\
&\ge\vert x_j\vert\\
&\ge\Vert x\Vert_{\infty}
\end{aligned}
$$

<div class="alert alert-success" role="alert" markdown="1">

$$
\Vert\infty\Vert\le\Vert x\Vert_2\le\Vert x\Vert_1\le n\Vert x\Vert_{\infty}
$$

</div>