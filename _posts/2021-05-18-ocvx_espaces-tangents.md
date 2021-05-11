---
title:          "OCVX: espaces tangents"
date:           2021-04-15 9:00
categories:     [Image S8, OCVX]
tags:           [Image, SCIA, OCVX, S8]
description: Espaces tangents
---

Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/HJhyTowO_)

# Dedramatiser les espaces tangents

Pour une fonction $$\begin{aligned}f:\mathbb R&\to\mathbb R \\ x&\mapsto f(x)\end{aligned}$$

![](https://i.imgur.com/g8T7u3z.png)

$$
Gr(f) = \{(x,f(x)), x\in\mathbb R\} \subseteq \mathbb R^2
$$

Une droite affine est un sous-espace de dimension 1

![](https://i.imgur.com/S9Rjp9X.png)

$$
\begin{aligned}
\color{red}{\mathcal T_{Gr(f), p}} &= (a,f(a)) + \color{red}{\underbrace{\{\lambda(1,f'(a)),\lambda\in\mathbb R\}}_{vect((1,f'(a))) = span((1,f'(a)))}}\\
&= \{((a+\lambda), f(a) + \lambda f'(a),\lambda\mathbb R)\}\quad\text{representation parametrique de } \mathcal T_{Gr(f), p}
\end{aligned}
$$

$Gr(f)$ $\to$ courbe $y=f(x)\equiv$ courbe $$\underbrace{f(x)-y}_{g(x,y)}=0$$

On va introduire $$\begin{aligned}g:\mathbb R^2&\to\mathbb R \\ (x,y)&\mapsto f(x)-y \end{aligned}$$


$Gr(f)$ $\to$ courbe $y=f(x)\equiv$ coubre $$\underbrace{f(x)-y}_{g(x,y)}=0 \equiv\{(x,y)\in\mathbb R^2, g(x,y) = 0\}=\mathcal C_0(g)$$

<div class="alert alert-success" role="alert" markdown="1">
On passe a la courbe de niveau 0
</div>

## Que vaut $\nabla g(p)$ ?

$$
\nabla g(x,y) = (\frac{\partial g}{\partial x}, \frac{\partial g}{\partial y}) = (f'(x), -1)\\
\nabla g(p=(a,f(a))) = (f'(a), -1)
$$

On a trouve precedemment un vecteur directeur de l'espace tangent $(1, f'(a))$.

<div class="alert alert-success" role="alert" markdown="1">
On obtient 2 vecteurs orthogonaux
</div>

$$
\nabla g(p=(a,f(a))) = (f'(a), -1) \to \vec n\\
<\vec n,\vec u> = 0
$$

<div class="alert alert-danger" role="alert" markdown="1">
Le gradient d'une fonction en un point donne est **orthogonal** aux lignes de niveau de cette fonction.
</div>

![](https://i.imgur.com/OZEXDPP.png)

## Cas general

Dans le cas general $f:\mathbb R^n\to\mathbb R$

![](https://i.imgur.com/fg1jCQW.png)

Notre "bol" est:

$$
Gr(f) = \{(x,y,f(x,y)), (x,y)\in\mathbb R^2\} \subseteq\mathbb R^3
$$

On veut calculer l'espace tangent dans un point donne de l'espace

![](https://i.imgur.com/CtWTGO9.png)

On a deux directions de pentes
- *Qu'est-ce qui se passe selon $x$ ?*
    - Si on se deplace de $1$ en $x$, $\frac{\delta f}{\delta x}(x_0,y_0)$ en $z$
- *Qu'est-ce qui se passe selon $y$ ?* 
    - Si on se deplace de $1$ en $y$, $\frac{\delta f}{\delta y}(x_0,y_0)$ en $z$

Zoomons au niveau du point $p$:

![](https://i.imgur.com/4Xo6b5l.png)

Ces vecteurs generent l'espace tangent

$$
\begin{aligned}
\mathcal T_{Gr(f), p} &= p + vect\biggr(\underbrace{(\overbrace{1,0}^{e_x},\frac{\partial f}{\partial x}(x_0, y_0)}_{\in\mathbb R^3}), \underbrace{(\overbrace{0,1}^{e_y},\frac{\partial f}{\partial y}(x_0,y_0))}_{\in\mathbb R^3}\biggr)\\
&= p + vect\underbrace{((e_x, \frac{\partial f}{\partial x}), (e_y, \frac{\partial f}{\partial y}))}\\
&\{\lambda(e_x, \frac{\partial f}{\partial x}) + \mu(e_y, \frac{\partial f}{\partial y}),(\lambda,\mu\in\mathbb R^2)\}
\end{aligned}
$$

Le vrai cas general $f:\mathbb R^n\to\mathbb R$
- $n$ pertes $\frac{\partial f}{\partial x}$ selon chaque vecteur de base $e_i=(0,...0,1,...,0)$
- $n$ vecteurs de perte $$\underbrace{(\underbrace{e_i}_{\in\mathbb R^n},\frac{\partial f}{\partial x_i})}_{\in\mathbb R^{n+1}}, i=1,...,n$$

$$
\mathcal T_{Gr(f)} = vect\biggr((e,\frac{\partial f}{\partial x_1}),...,(e_n,\frac{\partial f}{\partial x_i})\biggr)\quad\text{sous espace de dim }n\text{ d'un espace de dimension }n+1\\
T_{Gr(f),p}=\{\lambda(e_1,\frac{\partial f}{\partial x_1}) + ... + \lambda_n(e_n,\frac{\partial f}{\partial x_n}), (\lambda_1,...,\lambda_n)\in\mathbb R^n\}
$$

$Gr(f)=$ surface $y=f(x_1,...,x_n)$

$$
f(x_1,...,x_n)-y=0 \equiv \{(x_1,...,x_n,y)\text{ tel que } \underbrace{f(x_1,...,x_n)-y}_{g(x_1,...,x_n,y)}=0\} = \mathcal C_0(g)\\
\begin{aligned}
g:\mathbb R^{n+1}&\to\mathbb R\\
(x_1,...,x_n,y) &\mapsto f(x_1,...,x_n)-y
\end{aligned}\\
\nabla g(x,y) = (\frac{\partial g}{\partial x_1},...,\frac{\partial g}{\partial x_n},\frac{\partial g}{\partial y}) = (\frac{\partial f}{\partial x_1},...,\frac{\partial f}{\partial x_n},-1)
$$

**Implicitement:** $$\mathcal T_{C_0(g),p} = \{x\in\mathbb R^{n+1}, \nabla g^T x = 0\}$$

## Exercice

Soit $$\begin{aligned} f:\mathbb R^2&\to\mathbb R \\ (x,y)&\mapsto ax^2+by^2 \quad (a,b)\in\mathbb (R_{*}^+)^2 \end{aligned}$$

1. Decrire l'espace tangent en tout point du graph de $f$
2. Decrire l'espace tangent a la courbe de niveau $1$ de $f$
3. Exo 4.53

1.En un point $(x,y,f(x,y))\in Gr(f)$
- perte selon $x$: $(1,0,\frac{\partial f}{\partial x}) = \color{blue}{(1,0,2ax)}$
- perte selon $y$: $(0,1,\frac{\partial f}{\partial y}) = \color{green}{(0,1,2by)}$

![](https://i.imgur.com/7444mKh.png)


$$
\begin{aligned}
\mathcal T_{Gr(f), p} = vect\biggr(&\underbrace{(1,0,2ax), (0,1,2by)}_{}\biggr) + p\\
\{\lambda(1,0,2ax) &+ \mu(0,1,2by), (\lambda,\mu)\in\mathbb R^2\} = {(\lambda,\mu,2ax\lambda + 2by\mu), (\lambda, \mu)\in\mathbb R^2}
\end{aligned}
$$

2.$\mathcal C_1(f) = \{(x,y)\in\mathbb R^2, f(x,y)=ax^2+by^2=1\}$

![](https://i.imgur.com/ER4rStq.png)

On commence par regarder que vaut le gradient de cette fonction::

$$
\nabla f(x,y) = \begin{pmatrix} 2ax \\ 2by \end{pmatrix}
$$

*Dans quel sens pointe le gradient ?*

![](https://i.imgur.com/sXLBav5.png)

*Quel est l'espace par rapport au gradient ?*

$$
\begin{aligned}
\mathcal T_{\mathcal C_1(f),p} = p + \{(x,y), \nabla f(x_0, y_0)^T\begin{pmatrix}x \\ y \end{pmatrix} &= 0\}\\
(2ax_0, 2by_0)\begin{pmatrix}x \\ y \end{pmatrix} &= 0\\
2ax_0x + 2by_0y &= 0\\
y&=-\frac{ax_0}{by_0}x
\end{aligned}\\
\mathcal T_{\mathcal C_1(f),p} = (x_0, y_0) + \{(x,y)\in\mathbb R^2, \underbrace{y = -\frac{ax_0}{by_0}x}_{\nabla f(x_0, y_0)^T\begin{pmatrix}x \\ y \end{pmatrix} = 0}\}
$$

3.*Ou est le minimum de $f$ ? Quel point minimise $ax^2 + by^2$ ?*

C'est $(0,0)$.

$$
argmin f(x,y) = ax^2 + by^2 = (0,0)
$$

![](https://i.imgur.com/We4spL8.png)

*Dans quel sens pointe le gradient en tout point de la courbe de niveau par rapport au point minimal?*

![](https://i.imgur.com/U3NHP8r.png)

<div class="alert alert-success" role="alert" markdown="1">
En tout point des courbes de niveau de $f$, $Df$ point a l'oppose du point optimal $(x^+=0, y^+=0)$
</div>

## Caracterisation au premier ordre de la convexite

![](https://i.imgur.com/khhsrOv.png)


Graphiquement, quelque soit $x$, $Gr(f)\ge \mathcal T_{Grf(x,f(x))}$, le point est toujours au-dessus de la tangente.

![](https://i.imgur.com/PsoJ5JE.png)

Si $f$ est convexe, $\forall x,y$, $f(y) - f(x)\ge f'(x)(y-x)$

<div class="alert alert-info" role="alert" markdown="1">
Pour une fonction $f:\mathbb R^n\to\mathbb R$, $f$ convexe $\Leftrightarrow$ $\forall x,y\in\mathbb R^n$ $$\color{red}{f(y)-f(x)\ge \nabla \underbrace{f(x)^T}_{\in\mathbb R^n}\underbrace{(y-x)}_{\in\mathbb R^n}}$$
</div>