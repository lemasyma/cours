---
title:          "OCVX2: Approche lineaire"
date:           2021-09-27 14:00
categories:     [Image S9, OCVX2]
tags:           [Image, SCIA, S9, OCVX2]
math: true
description: Approche lineaire
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/S1x-NEyNY)

# Exercice 1

On considere la fonction differentiable

$$
\begin{aligned}
f:\mathbb R^2&\to\mathbb R\\
(x,y)&\mapsto 3x^2+y^2
\end{aligned}
$$

1. Representer les courbes de niveaux 2 et 4 de $f$ dans le plan euclidien
2. A quel lieu correspond la condition $f(x,y)\le4$
3. On s'interesse au probleme d'optimisation $(P)$ minimiser $f_0(x,y)=2x+y$ sujet a $3x^2+y^2\le4$. Representer la courbe de niveau de la fonction objectif qui correspond a la valeur optimale de $(P)$
4. Comment trouver le point optimal correspondant a $(P)$? Faire le calcul

<details markdown="1">
<summary>Solution</summary>

1.

$$
f(x,y)=3x^2+y^2\\
\begin{aligned}
\mathcal C_2&=\{3x^2+y^2=2\}\\
&= \{\frac{3}{2}x^2+\frac{1}{2}y^2=1\}
\end{aligned}
$$

<div class="alert alert-success" role="alert" markdown="1">
Il s'agit de l'equation d'une elipse de:
- demi grand axe $a$
- demi petit axe $b$

$$
\biggr(\frac{x}{a}\biggr)^2+\biggr(\frac{y}{b}\biggr)^2 =1
$$



![](https://i.imgur.com/tjUnZER.png)



</div>

<div class="alert alert-info" role="alert" markdown="1">
**Rappel**

$$
2\pi r\to\pi(a+b)\\
\pi r^2\to\pi a b
$$

</div>

$$
\mathcal C_2 (f)=\{3x^2+y^2=2\}
$$

Ellipse de:
- demi grand axe $\sqrt{2}$ sur $O_y$
- demi petit axe $\sqrt{\frac{2}{3}}$ sur $O_x$


$$
\mathcal C_4 (f)=\{3x^2+y^2=4\}
$$

Ellipse de:
- demi grand axe $2$ sur $O_y$
- demi petit axe $\frac{2}{\sqrt{3}}$ sur $O_y$



![](https://i.imgur.com/Ata2jUJ.png)



> Zoli dessin

2.

![](https://i.imgur.com/8QPlLUr.png)

3.

$$
\begin{aligned}
(P) \quad\text{min} f_0(x,y)&=2x+y\\
3x^2+y^2&\le4\Leftrightarrow \mathcal C_{\le 4}(f)
\end{aligned}
$$

$$
\mathcal C_0 = \{2x+y=0\}\\
\vec u=\binom{-1}{2}\\
\vec n=\binom{2}{1}
$$


![](https://i.imgur.com/yaDunl1.png)


<div class="alert alert-success" role="alert" markdown="1">
Pour minimiser, on part dans le sens inverse du vecteur normal.
</div>



![](https://i.imgur.com/aKkXOd5.png)



Notre point optimal: $p^{\*} = (x^{\*}, y^{\*})$

$$
p*\in\mathcal C_4(f)\Leftrightarrow 3x^{*^2}+y^{*^2}=4\\
p*\in\mathcal C_{f_0^*}\Leftrightarrow 2x^*+y^*=f_0^*
$$

<div class="alert alert-danger" role="alert" markdown="1">

Le gradient d'une fonction en un point donne est orthogonal a la courbe de niveau qui passe par ce point la.

</div>

![](https://i.imgur.com/a2Hia0V.png)


En $p^{\*}$:

$$
\nabla \vec f(p^*) = \lambda\vec n\\
\nabla \vec f(p^*) + \lambda\vec n = 0\quad\lambda \gt 0
$$

$$
f(x,y)=3x^2+y^2\\
\nabla f = (\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}) = (6x, 2y)\\
\begin{aligned}
\nabla f(p^* = (x^*, y^*)) = (6x^*, 2y^*) = \lambda\binom{2}{1}&\Leftrightarrow \begin{cases}
6 x^* = 2\lambda\\
2y^* = \lambda
\end{cases}\\
&\Leftrightarrow 6x^* = 4y^*\\
&\Leftrightarrow \color{green}{\boxed{y^* = \frac{3}{2}x^*}}
\end{aligned}\\
\begin{aligned}
3x^{*^2}+y^{*^2} = 4\Rightarrow 3x^{*^2}+(\frac{3}{2}x^*)^2&=4\\
3x^{*^2}+\frac{9}{4}x^{*^2}&=4\\
\frac{21}{4}x^{*^2}&=4\\
x^{*^2}&=\frac{16}{21}
\end{aligned}
$$

Donc:

$$
x^*=\frac{4}{\sqrt{21}}\quad\text{ou}\quad\color{green}{\boxed{-\frac{4}{21}}}\\
\text{et}\quad \color{green}{\boxed{y^*=-\frac{6}{\sqrt{21}}}}
$$

</details>

# Exercice 2

On considere le probleme d'optimisation $(P)$ minimiser $f_0(x,y)=x+y$ sujet a $x+2y\le3,x\in B$ avec $B\in\mathbb R^2$ l'intersection de l'epigraphe de $x\mapsto-\sqrt{x}$.
1. Dessiner le lieu admissible de $(P)$
2. Representer la courbe de niveau $f_0$ qui realise le minimum de $(P)$
3. Calculer le point optimal ainsi que la valeur optimale de $(P)$

<details markdown="1">
<summary>Solution</summary>

<div class="alert alert-info" role="alert" markdown="1">
**Rappel: Epigraphe**

Tout ce qu'il y a au-dessus du graphe de la fonction

$$
\text{epi}(f) = \{(x,t)\vert t\ge f(x)\}
$$

</div>

1.


![](https://i.imgur.com/jST1Su2.png)


$$
x+2y-3=0 \quad (D)\\
(3,0)\in D \\ \vec u=\binom{-2}{1}\\\vec n =\binom{1}{2}
$$


![](https://i.imgur.com/76C9bSf.png)


Avec la courbe $\mathcal C_0$:


![](https://i.imgur.com/UyExZB4.png)


Avec $p^{\*}=(x^{\*}, y^{\*})$:


![](https://i.imgur.com/KRqYVKD.png)


2.


![](https://i.imgur.com/AaGgkeQ.png)


Le vecteur normal au graphe va etre colineaire au vecteur normal de notre courbe de niveau.

*Gradient de quoi ?*
> On est sur le graphe et pas la ligne de niveau

*Est-ce qu'on peut exprimer le graphe comme ligne de niveau ?*
> Toutes les representations parametriques peuvent s'ecrire en representation implicite (l'inverse n'etant pas vrai)

<div class="alert alert-success" role="alert" markdown="1">
Notre graphe de $y\mapsto-\sqrt{x}$ est:

$$
\{(x,y) \text{ tq } y=-\sqrt{x}\}\\
\{(x,y)\text{ tq } \sqrt{x}+y=0\}\\
= \mathcal C_0(g)
$$

Avec:

$$
\begin{aligned}
g: \mathbb R^2&\to\mathbb R\\
(x,y)&\mapsto \sqrt{x} + y
\end{aligned}
$$

</div>

Condition d'optimalite: en $p^{\*}=(x^{\*}, y^{\*})$,

$$
\nabla g(p^*) = \lambda \vec n_0\\
\begin{aligned}
\nabla g(x,y) &= (\frac{\partial g}{\partial x}, \frac{\partial g}{\partial y})\\
&= (\frac{1}{2\sqrt{x}}, 1)
\end{aligned}
$$

En $p^{\*}$:

$$
\begin{aligned}
&\begin{cases}
\frac{1}{2\sqrt{x^*}} = \lambda\\
1 = \lambda\\
\end{cases}\\
&\Leftrightarrow
\begin{cases}
\lambda =1\\
\frac{1}{2\sqrt{x^*}}=1\\
\end{cases}\\
&\Leftrightarrow
\begin{cases}
x^*=\frac{1}{4}\\
y^*=-\frac{1}{2}
\end{cases}
\end{aligned}
$$

<div class="alert alert-success" role="alert" markdown="1">
Valeur optimale:

$$
x^* + y^* = \frac{1}{4}-\frac{1}{2} = \color{green}{\boxed{-\frac{1}{4}}}
$$

</div>
</details>
