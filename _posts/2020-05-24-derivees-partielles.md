---
layout:     post
mathjax:    true
comments:   true
title:      "CAMA : Derivees partielles"
date:       2020-24-05 10:00
tags:       Shannon CAMA
description: Fiche sur les derivees partielles
---

# CAMA : Dérivées partielles
## Les fonctions
* Une fonction $f$ est dite **scalaire** lorsque son espace d'arrivée est $\mathbb{R}$.
* Une fonction $f$ est dite **vectorielle** lorsque son espace d'arivée est $\mathbb{R}^n$ avec $n \gt 1$.

## Les derivees
Soit $f(x, y)$ une fonction scalaire:
* sa derivée partielle première en $x$ : $\frac{\partial f}{\partial x} = \partial_x f$
* sa dérivée partielle seconde en $y$ : $\frac{\partial^2 f}{\partial y^2} = \partial_{yy} f$
* sa différentielle totale $df(x, y) = \frac{\partial f}{\partial x}(x, y)dx + \frac{\partial f}{\partial y}(x, y)dy$
* $\frac{\partial(f \circ g)}{\partial x} = \frac{\partial f}{\partial g} \frac{\partial f}{\partial x}$

## Nabla $\nabla$
L'opérateur nabla pour une fonction qui part d'un espace a 2 dimensions est $$\nabla =
\begin{pmatrix}
\frac{\partial f}{\partial x} \\
\frac{\partial f}{\partial y} \\
\end{pmatrix}$$
* Pour une fonction scalaire $f:\mathbb{R}^2\to\mathbb{R}$ : $$ Gradiant : Grad(f) = \nabla f = \begin{pmatrix} \frac{\partial f}{\partial x} \\\frac{\partial f}{\partial y} \\\end{pmatrix} \\ Laplacien : \triangle f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} \space avec\space \nabla.\nabla = \triangle$$
* Pour une fonction vectorielle $f:\mathbb{R}^2\to\mathbb{R}^2$ : $$Divergence : Div(f) = \nabla.f = \frac{\partial f}{\partial x} + \frac{\partial f}{\partial y} \\ Laplacien: \triangle f = \begin{pmatrix} \frac{\partial^2 f_x}{\partial x^2} + \frac{\partial^2 f_x}{\partial y^2}\\\frac{\partial^2 f_y}{\partial x^2} + \frac{\partial^2 f_y}{\partial y^2}\end{pmatrix}$$

## Développement limité
Le D.L. d'une fonction $f:\mathbb{R}^2\to\mathbb{R}$ en ${\bf u} = (u_x, u_y)$ est:
$$
f({\bf u + \delta u}) 
= f(u) + <\nabla f(u), \delta u> + \frac{1}{2!}<\nabla^2f(u)\delta u, \delta u> + o(\Vert\delta u\Vert^2) \\ = f(u) + \partial_x f(u)\delta u_x +\partial_y f(u)\delta u_y + \partial_{xx}f\frac{\delta u_x^2}{2} + \partial_{xy}f\delta u_x \delta u_y + \partial_{yy}f\frac{\delta u_y^2}{2} + o(\Vert\delta u\Vert^2)
$$
Avec $\nabla^2 f$ la matrice hessienne de f et $<u, v>$ une autre notation du produit scalaire.
