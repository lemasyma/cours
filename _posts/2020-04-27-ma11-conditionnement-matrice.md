---
title:          "CAMA : ma11 Conditionnement d'une matrice"
date:           2020-04-27 10:00
categories:     [S6, Shannon, CAMA]
tags:           [S6, CAMA, Shannon]
description: Conditionnement d'une matrice
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/HyLZWmfa8)
# Cours du 27 / 04

Soit la matrice symétrique $A$ suivante : 
``` python
A = np.array([[10, 7, 8, 7], [7, 5, 6, 5], [8, 6, 10, 9], [7, 5, 9, 10]])
```
```
array([[10,  7,  8,  7],
       [ 7,  5,  6,  5],
       [ 8,  6, 10,  9],
       [ 7,  5,  9, 10]])
```
``` python
lin.det(A) # calcul son determinant
```
```
0.9999999999999869  # on peut arrondir a 1
```
Construisons $b$ tel que $A{\bf x} = b$ et $\bf x = [1,1,1,1]$
``` python
b = A.sum(axis=1)
```
```
[32 23 33 31]
```
``` python
x = lin.solve(A, b)
```
```
array([1., 1., 1., 1.])
```
<div class="alert alert-warning" role="alert" markdown="1">
Perturbons $b$, comme s'il y avait une erreur de mesure ou d'arrondi.
</div>
``` python
bp = [32.1, 22.9, 33.1, 30.9]
eb = lin.norm(b - bp) / lin.norm(b) 
# une erreur se mesure par rapport à la valeur de la donnée
```

```
0.0033319453118976702
```

On a une erreur de l'ordre de $0,3\%$.

<div class="alert alert-danger" role="alert" markdown="1">
On note l'erreur :
$$ \frac{||{\bf \delta b}||}{||{\bf b}||}$$
</div>
Regardons la solution ${\bf x}$ de notre système matriciel perturbé:
``` python
xp = lin.solve(A, bp)
```
```
array([  9.2, -12.6,   4.5,  -1.1])
```
<div class="alert alert-warning" role="alert" markdown="1">
La solution n'a rien n'a voir avec $[1,1,1,1]$
</div>
``` python
ex = lin.norm(x - xp) / lin.norm(x) #mesure de l'erreur
```
```
8.19847546803699
```
L'erreur est de l'ordre de 8.

``` python
ex / eb
```
```
2460.567236431514
```
<div class="alert alert-warning" role="alert" markdown="1">
C'est $2460$ fois plus que l'erreur sur $b$.
</div>

## Pourquoi ?
$$
\begin{aligned}
 A ({\bf x} + {\bf \delta x}) &= {\bf b} + {\bf \delta b} \quad \textrm{et donc} \\
 A \, {\bf \delta x} &= {\bf \delta b} \; \textrm{ puisque } A {\bf x} = {\bf b} \quad \textrm{et finalement}\\
{\bf \delta x} &= A^{-1} \, {\bf \delta b}
\end{aligned}
$$
Comme $A$ et son inverse sont des applications linéaires :

$$
||{\bf b}|| \le ||A|| \, ||{\bf x}||
\quad \textrm{et} \quad ||{\bf \delta x}|| \le ||A^{-1}|| \, ||{\bf \delta b}||
$$

donc : 

$$
\frac{||{\bf \delta x}||}{||{\bf x}||}  \le ||A^{-1}|| \, \frac{||{\bf \delta b}||}{||{\bf x}||}
\le ||A^{-1}|| \, ||A|| \, \frac{||{\bf \delta b}||}{||{\bf b}||}
$$

``` python
lin.norm(lin.inv(A)) * lin.norm(A)
```
```
3009.5787080586942
```
<div class="alert alert-danger" role="alert" markdown="1">
On appelle cela le conditionnement de $A$ : 
$$cond(A) = ||A^{-1}|| \, ||A||$$
**Une matrice mal conditionnée va générer des erreurs de calcul lors de la résolution du système matriciel.**
</div>
``` python
np.linalg.cond(A) # scipy n'a pas le conditionnement mais numpy l'a. 
```
```
2984.0927016757555 # different de 3009
```

## Perturbons la matrice
``` python
np.random.seed(0)

dA = 2 * np.random.random(size = A.shape) - 1
```
```
array([[ 0.098,  0.43 ,  0.206,  0.09 ],
       [-0.153,  0.292, -0.125,  0.784],
       [ 0.927, -0.233,  0.583,  0.058],
       [ 0.136,  0.851, -0.858, -0.826]])
``` 
``` python
ea = lin.norm(dA) / lin.norm(A) # erreur relative sur A
```
```
0.06868857112100454
```
``` python
Ap = A + dA
```
```
array([[10.098,  7.43 ,  8.206,  7.09 ],
       [ 6.847,  5.292,  5.875,  5.784],
       [ 8.927,  5.767, 10.583,  9.058],
       [ 7.136,  5.851,  8.142,  9.174]])

```
``` python
xp = lin.solve(Ap, b)
```
```
array([-12.365,  15.574,  10.146,  -5.94 ])
```
``` python
ex = lin.norm(xp - x) / lin.norm(x)
```
```
11.432687335993894
```
``` python
ex / ea # valeur de l'erreur
```
```
166.44235204505293
```
<div class="alert alert-success" role="alert">
L'erreur est moins grande.
</div>
<div class="alert alert-warning" role="alert" markdown="1">
Une erreur peut fortement perturber $A$, le conditionnement et l'erreur sont tous les deux importants.
</div>
Pour retrouver le conditionnement de $A$ dans ce cas : 
$$
\begin{align}
& (A + \Delta A) \, ({\bf x} + {\bf \delta x}) = {\bf b} \quad \textrm{et donc} \\
& A \, {\bf \delta x} + \Delta A \, ({\bf x} + {\bf \delta x}) = 0 \; \textrm{ puisque } A {\bf x} = {\bf b} \quad \textrm{et finalement}\\
& {\bf \delta x} = -A^{-1} \,\Delta A \, ({\bf x} + {\bf \delta x}) \quad \textrm{et} \\
& ||{\bf \delta x}|| \le ||A^{-1}|| \, ||\Delta A|| \, ||{\bf x} + {\bf \delta x}||
\end{align}
$$
Donc 
$$
\begin{align}
\frac{||{\bf \delta x}||}{||{\bf x} + {\bf \delta x}||}
\le ||A^{-1}|| \, ||\Delta A|| =  ||A^{-1}|| \, ||A|| \, \frac{||\Delta A||}{||A||}
\end{align}
$$
et
$$
\begin{align}
\frac{||{\bf \delta x}||}{||{\bf x} + {\bf \delta x}||}
\le cond(A) \, \frac{||\Delta A||}{||A||}
\end{align}
$$
## Propriétés
* $cond(A) \ge 1$ car $Id = A\, A^{-1}$ et donc $1 \le ||A||\, ||A^{-1}||$
* $cond(A) = cond(A^{-1})$
* $\displaystyle cond_2(A) = \frac{\max_i |\lambda_i|}{\min_i |\lambda_i|}$ si la matrice est réelle 
    * 2 indique qu'on utilise la norme 2 
    * $\lambda_i$ sont les valeurs propres de A
``` python
vp = lin.eigvals(A)
vp.max() / vp.min()
```
* si A est unitaire ou orthogonale : $cond_2(A) = 1$
* le conditionnement n'est pas modifié par transformation unitaire

## Préconditionnement
<div class="alert alert-info" role="alert" markdown="1">
Le conditionnement peut etre tranformé : 

$$
\forall A, \exists B \; \textrm{appelée matrice de préconditionnement t.q.} \quad cond(B\, A) < cond(A)
$$
</div>
<div class="alert alert-warning" role="alert" markdown="1">
On résoud $B\, A {\bf x} = B\, {\bf b}$.
</div>