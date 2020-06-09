---
layout: post
title:  CAMA : ma32
date:   2020-17-05 10:00
tags: Shannon CAMA
description: Méthode du gradiant pour système matriciel
---

# CAMA : ma32 Méthode du gradiant pour système matriciel
# Cours du 17/05

## $Ax = b$ vu comme un probleme d'optimisation
Pour résoudre $Ax = b$ on va chercher le minimum de la fonctionnelle
$$
J(x) = \frac{1}{2}x^TAx - b.x
$$
La dérivée s'annule en ce point et est $Ax - b$

## Calcul de la dérivée
Les derivées de dimension supérieure a 1 peuvent être manipulées comme des derivées partielles ou une derivée totale. On s'intéresse à la derivée dans une direction, c.a.d la derivée partielle en $y$ si on va dans la direction de l'axe $y$.

:::info
**Définition**
$f : \Omega \subset {X\to Y}$ ($\Omega$ ouvert) est dérivable en $a\in\Omega$ si
$$
\exists f'(a)\in L(X,Y)\space tel\space que \\
f(a+h) = f'(a) + f(a)(h) + h\space\epsilon(h)
$$
avec:
* $\lim_{h\to 0}\epsilon (h) = 0$
* $L(X, Y)$ applications linéaires continues de $X$ dans $Y$
* $f'(a)\in L(X, Y)$ et non $f'$
:::
Si $f$ est dérivable en $a$ alors $\forall h \in X$
$$
f'(a)(h) = lim_{\theta\to0}\frac{f(a + \theta h) - f(a)}{\theta}
$$
:::warning
Attention à vérifier le type de chaque terme.
$f$ est une fonction scalaire donc :
* $Y = \mathbb{R}$
* $X = \mathbb{R}^n \space avec\space n\gt 1$
:::
### Notation avec le gradient
$$
f(a + h) = f(a) + (\nabla f)(a)^T h + h^T\epsilon(h)
$$
* $f$ est scalaire
* $(\nabla f)(a)$ est un vecteur dont le produit scalaire avec h donne un réel

## Calculons la dérivée de J suivant une direction
On calcule la dérivée de $J(x)$ au point $a$ suivant la direction $h$
$$
J'(a)(h) = \lim_{\theta\to0}\frac{J(a + \theta h) - J(a)}{\theta} \\
= \lim_{\theta\to 0}\frac{1}{\theta}\biggr(\frac{1}{2}(a+\theta h)^TA(a+\theta h) - b^T(a+\theta h) - \frac{1}{2}a^TAa+b^Ta\biggr) \\
= \lim_{\theta\to0}\frac{1}{\theta}\biggr(\frac{1}{2}(\theta a^TAh + \theta h^TAa +\theta^2 h^TAh) - \theta b^Th\biggr) \\
= \frac{1}{2}(a^TAh + h^TAa) - b^T h
$$
donc
$$
J':x\in\Omega\subset\mathbb{R}^n\to L(\mathbb{R}^n,\mathbb{R}) \\
x\mapsto\frac{1}{2}(x^TA + Ax)-b
$$

## A symétrique
Dans le cas ou A est symétrique, on a:
$$
J'(x) = \nabla J(x) = Ax - b
$$
:::success
Si la dérivée s'annule, c.a.d qu'on trouve le minimum, on a résolu le système matriciel
:::
:::info
Les conditions pour utiliser la méthode de gradient sont:
* A symétrique
* J a un minimum
:::

## Propriéte
:::info
Si A est symétrique et **définie positive** alors $J$ est convexe strictement et **coervice** ($\lim_{\lVert a \rVert\to\infty}J(a) = +\infty$), alors elle a un minimum.
:::
