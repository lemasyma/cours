---
title:          "CAMA : ma30"
date:           2020-05-17 10:00
categories:     [S6, Shannon, CAMA]
tags:           [S6, CAMA, Shannon]
math: true
description: Optimisation - Méthode du gradient
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/H1XbIPb3U)
# CAMA : ma30 Optimisation - Méthode du gradient
# Cours du 17/05

## Probleme d'optimisation
Soit une fonction $J : \mathbb{R}^n\to\mathbb{R}$, trouver le minimum de $J$, c.a.d trouver $u$ tel que
$$
J(u) = \inf_{v\in\mathbb{R}^n}J(v)
$$
### Problème d'optimisation avec contrainte
<div class="alert alert-info" role="alert" markdown="1">
Il est possible de chercher $u$ non pas dans $\mathbb{R}^n$ mais dans une partie de $\mathbb{R}^n$, c'est alors un problème d'optimisation avec contrainte.
</div>
**Exemple** : On cherche le minimum de $J(x, y)$ avec $x \lt y$, on cherche dans la partie de $\mathbb{R}^2$ qui vérifie $x \lt y$.

## La méthode du gradient
On imagine un problème d'optimisation en 2D comme un terrain avec du relief, $J(x, y)$ represente l'altitude en tout point $(x, y)$.
<div class="alert alert-danger" role="alert" markdown="1">
La méthode du gradient consiste a prendre un point au hasard et *descendre dans la direction qui descend le plus* afin de trouver le **minimum** de $J$.
</div>
<div class="alert alert-success" role="alert">
L'algorithme du gradient consiste à :
* prendre un point de départ au hasard $p^0 = (x_0, y_0)$
* calculer le gradient de $J$ en ce point
$$
\nabla J(x_0, y_0) = \begin{bmatrix} 
\frac{\partial J}{\partial x}  \\
\frac{\partial J}{\partial y}
\end{bmatrix} (x_0, y_0)
$$
* avancer dans la direction opposée (le gradient monte) ${\bf p}^{k+1} = {\bf p}^k - \mu \, \nabla J({\bf p}^k)$
* on recommence l'étape précédente jusqu'à avoir un point fixe, c.a.d $|| {\bf p}^{k+1} - {\bf p}^k|| < \varepsilon$ avec $\epsilon$ une petite valeur.
</div>
``` python
def J(x, y):
    return x**2 + 0.5 * y**2 - 2 * x + 3
```
``` python
x = np.linspace(-3,3,100) # genere des points a distance egale sur l'intervalle [-3,3]
y = np.linspace(-3,3,100)

mx, my = np.meshgrid(x,y)
mz = J(mx, my)
```
<div class="alert alert-danger" role="alert" markdown="1">
**Calcul du gradient :**
``` python
def grad_J(x,y):
    return np.array([2*x-2, y])   # calculé à la main à partir de J
```
</div>
<div class="alert alert-success" role="alert">
**Algorithme du gradient :**
``` python
x = np.array([0,0])  # un point au hasard
µ = 0.1     # plus il est petit et moins on avance vite
e = 0.0001  # epsilon pour la condition d'arrêt

while True:
    x_old = x
    x =  x - µ * grad_J(*x)  # *x donne en arguments toutes les valeurs de x donc x[0] en 1er arg et x[1] en 2e
    if np.square(x_old - x).sum() < e**2:
        break
```
</div>
Le minimum obtenu en appelant $J(*x)$ est au point $[1. 0.]$ ayant pour valeur $2.0000001053122918$.

## Etude de la convergence du gradient
On stocke les valeurs des points entre le point initial et le point final pour obtenir un ensemble de points et tracer des courbes de convergence.
``` python
def minimum_J(start_value, µ=0.1, e = 0.001):
    x = [np.array(start_value)]
    while True:
        x.append(x[-1] - µ * grad_J(*x[-1]))
        if np.square(x[-1] - x[-2]).sum() < e**2:
            break
```
``` python
x = minimum_J(start_value = (0,1)) # valeur initiale non alignee avec la solution
```
![](https://i.imgur.com/4f6A4yp.png)

### Impact de $\mu$
*Comment est-ce que $\mu$ influence sur la convergence?*
* $\mu = 0.1$ : on fait des *petits pas*.
* $\mu = 2$ : on diverge, les *pas* sont trop grands. On passe de $1$ a $-1$ puis $1$, $-1$ sans tomber sur la solution $0$.
* $\mu = 0.8$ : on converge en $17$ iterations contre $46$ avec $\mu = 0.1$, c'est 3x plus rapide.
* $\mu = 1$ : boucle infinie, on oscille infiniment entre $[0, 0]$ et $[2, 0]$.
<div class="alert alert-danger" role="alert" markdown="1">
La valeur de $\mu$ est **importante**. Si elle est trop petite on perd du temps, si elle est trop grande on ne trouve pas la solution.
</div>