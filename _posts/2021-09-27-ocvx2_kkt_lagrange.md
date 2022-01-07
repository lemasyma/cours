---
title:          "OCVX2: Optimisation sous contrainte par la methode des multiplicateurs de Lagrangre et conditions KKT"
date:           2021-09-27 16:00
categories:     [Image S9, OCVX2]
tags:           [Image, SCIA, S9, OCVX2]
math: true
description: Optimisation sous contrainte par la methode des multiplicateurs de Lagrangre et conditions KKT
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/HJVxl8kVt)

<div class="alert alert-info" role="alert" markdown="1">
**KKT**: Karush-Kuhn-Tucker
</div>

On va s'attaquer a des problemes de la forme:

$$
\begin{matrix}
&\text{minimiser } f(x) &f:\mathbb R^n\to\mathbb R &f\text{ convexe}\\
&x\in C &x\in\mathbb R^n &C=\text{ensemble convexe}
\end{matrix}
$$

$$
x\in C\Leftrightarrow\begin{cases}
g_i(x)\le 0 &\forall i=1,\dots,m&g_i\text{ convexe}\\
h_j(x)=0 &\forall j=1,\dots,p&h_j\text{ affine}
\end{cases}
$$

$C$ defini l'ensemble des points admissibles.

$$
\boxed{
\begin{matrix}
&\text{minimiser } f(x) &\text{equivalent a} &\text{minimiser } f(x), x\in\mathbb R^n\\
&x\in C & &\text{tq} \begin{cases}
g_i(x)\le 0 &\forall i=1,\dots,n\\
h_j(x)=0&\forall j=1,\dots,p
\end{cases}
\end{matrix}\\
\color{red}{\text{(OPT)}}}
$$

- valeur optimale $p^{\*}=f(x^{\*})$
- point optimal $x^{\*}\in\mathbb R^n$

Sans contrainte: $f$ convexe: $x^{\*}$ optimal $\Leftrightarrow\nabla f(x^{\*})=0$

<div class="alert alert-warning" role="alert" markdown="1">

Cette conditions d'optimalite n'est plus vraie des lors que l'on a des contraintes.

<div class="alert alert-danger" role="alert" markdown="1">
Dualite de Lagrange
</div>

</div>

![](https://i.imgur.com/vd6PrQC.png)

# Lagrangien

On definit le Lagrangien de (OPT) comme la fonction:

$$
\begin{aligned}
\mathscr L:\mathbb R^n\times\mathbb R^m\times\mathbb R^p&\to\mathbb R\\
(x,\alpha,\beta)&\mapsto\mathscr L(x,\alpha,\beta) = f(x)+\sum_{i=1}^m\alpha_ig_i(x)+\sum_{j=1}^p\beta_jh_j(x)
\end{aligned}\\
\begin{aligned}
&\text{variables duales}\begin{cases}
\alpha=\begin{pmatrix}
\alpha_1\\
\vdots\\
\alpha_m
\end{pmatrix}\in\mathbb R^m\\
\beta=\begin{pmatrix}
\beta_1\\
\vdots\\
\beta_p
\end{pmatrix}\in\mathbb R^p
\end{cases}\\
&\Leftrightarrow\text{multiplications de Lagrange}\\
&\Leftrightarrow\text{cout associe a chaque contrainte}
\end{aligned}
$$

<div class="alert alert-info" role="alert" markdown="1">
**Lagrangien** $\equiv$ version sans contrainte du probleme (OPT)
</div>

# Intuition

**Intuition:** pour chaque probleme d'optimisation avec contraintes, il existe un certain parametrage des variables duales tel que le minimum sans contrainte du Lagrangien par rapport a la ***variable primale*** $\equiv x$ (a variables duales fixees) coincide avec la solution du probleme de contraintes.

On appelle ***fonction objective primale***

$$
\begin{aligned}
\theta_p:\mathbb R^n&\to\mathbb R\\
x&\mapsto \max_{\alpha,\beta \\ \alpha\ge 0\forall i} \mathscr L(x,\alpha, \beta)
\end{aligned}
$$

On appelle ***probleme primal*** le probleme d'optimisation sans contrainte: $$\min_{x\in\mathbb R^n}\theta_{p}(x)$$

$x\in\mathbb R^n$ est primal admissible ssi

$$
\begin{cases}
g_i(x)\le 0&\forall i\\
h_j(x)=0 &\forall j
\end{cases}
$$

<div class="alert alert-warning" role="alert" markdown="1">

On va noter $p^{\*}$ la valeur optimale de $(P)$ et $x^{\*}$ le point optimal, $p^{\*}=\theta_{p}(x^{\*})$

</div>

On appelle ***fonction objective duale***:

$$
\begin{aligned}
\theta_D:\mathbb R^m\times\mathbb R^p&\to\mathbb R\\
(\alpha,\beta)&\mapsto\min_{x\in\mathbb R^n}\mathscr L(x,\alpha,\beta)
\end{aligned}
$$

On appelle ***probleme dual*** le probleme d'optimisation avec contrainte

$$
(D)\quad \max_{\alpha,\beta \\ \alpha_i\ge 0}\theta_D(\alpha, \beta) = \max_{\alpha, \beta \\ \alpha_i\ge 0}\min_{x}\mathscr L(x,\alpha, \beta)
$$

$(\alpha,\beta)$ est dual admissible ssi $\alpha_i\ge0$ $\forall i$.

On note egalement $(\alpha^{\*}, \beta^{\*})$ la solution de $(D)$ et $d^{\*} = \theta_D(\alpha^{\*}, \beta^{\*})$

# Interpretation du probleme primal

Dans le cas ou on a $g(x)\le0$ convexe et $h(x)=0$ affine.

Dans ce cas, le Lagrange est:

$$
\begin{aligned}
\mathscr L:\mathbb R^n\times\mathbb R\times\mathbb R&\to\mathbb R\\
(x,\alpha,\beta)&\mapsto\mathscr L(x,\alpha,\beta)=f(x)+\alpha g(x)+\beta h(x)
\end{aligned}
$$

On a:

$$
\begin{aligned}
\theta_p:\mathbb R^n&\to\mathbb R\\
x&\mapsto \max_{\alpha,\beta \\ \alpha\ge 0\forall i} \mathscr L(x,\alpha, \beta)
\end{aligned}
$$

Dans ce cas:

$$
\begin{aligned}
x&\mapsto \max_{\alpha,\beta \\ \alpha\ge 0\forall i} \mathscr L(x,\alpha, \beta)\\
\theta_{p}(x) &= \max_{\alpha, \beta \\ \alpha\ge 0}[f(x)+\alpha g(x)+\beta h(x)]
\end{aligned}
$$

<div class="alert alert-success" role="alert" markdown="1">

$\theta_p(x)$ est convexe car la somme ponderee de fonctions convexes est convexe, et le $\max$ de fonctions convexes est convexe.

</div>

$$
\theta_p(x) = f(x)+\max_{\alpha,\beta \\ \alpha\ge 0}[\alpha g(x) + \beta h(x)]
$$

- Si $g(x)\gt 0$, le crochet est maximise pour $\alpha=+\infty$ et vaut $+\infty$
- Si $g(x)\le 0$, le crochet est maximise pour $\alpha=0$
- Si $h(x)\neq 0$, le crochet est maximiser pour $\beta=(\text{signe de }h(x))\infty$ et vaut $+\infty$
- Si $h(x)=0$, le crochet vaut $0$ peu importe la valeur de $\beta$

<div class="alert alert-success" role="alert" markdown="1">

Donc si $x$ primal admissible $(g(x) \le 0$ et $h(x)=0)$, alors le crochet vaut $0$.

</div>

<div class="alert alert-danger" role="alert" markdown="1">
Si $x$ ne verifie pas les contraintes, alors le crochet vaut $+\infty$.
</div>

$$
\theta_p(x)=f(x)+\begin{cases}
0 &\text{si } x \text{ primal admissible}\\
+\infty &\text{si } x \text{ pas primal admissible}
\end{cases}\\
$$

<div class="alert alert-info" role="alert" markdown="1">

$$
\begin{aligned}
(P):\quad&\min_{x\in\mathbb R^n}\theta_p(x)\\
&\min_{x\in\mathbb R^n}f(x)+\begin{cases}
0 &\text{si } x \text{ primal admissible}\\
+\infty &\text{si } x \text{ pas primal admissible}
\end{cases}
\end{aligned}
$$

</div>
