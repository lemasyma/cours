---
title:          "CAMA : ma12 Méthodes itératives"
date:           2020-04-27 10:00
categories:     [S6, Shannon, CAMA]
tags:           [S6, CAMA, Shannon]
math: true
description: Méthodes itératives
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/ByMD5LGTL)
# Cours du 27 / 04

## La simulation numérique
![](https://i.imgur.com/ztx6iDL.jpg)
<div class="alert alert-info" role="alert" markdown="1">
Pour faire cette image, on transforme des **équations physique** en **systèmes matriciels** ou les inconnues sont définies en chaque point d'un maillage a définir.
</div>
Dans ce cas l'inconnue est la pression et le maillage est une boîte imaginaire comprenant l'avion et l'air qui circule autour.
Si la boîte est un cube avec 1000 points dans chaque direction, on a 1 milliard de points et une matrice a 1 trillion d'éléments : 
$$
\begin{bmatrix}
a_{11} \; a_{12} \ldots a_{1,10^9} \\
a_{21} \; a_{22} \ldots a_{2,10^9} \\
 \vdots \\
a_{10^9,1} a_{n2} \ldots a_{10^9,10^9} \\
\end{bmatrix}
\;
\begin{bmatrix}
p_{1} \\
p_{2} \\
\vdots \\
p_{10^9} \\
\end{bmatrix}=
\begin{bmatrix}
f_{1} \\
f_{2} \\
\vdots \\
f_{10^9} \\
\end{bmatrix}
$$
Cela prendrait 300 000 ans à inverser la matrice.
<div class="alert alert-danger" role="alert" markdown="1">
**Inverser une matrice ou résoudre par une méthode directe n'est pas la bonne solution pour résoudre un grand système matriciel.**
</div>
## Méthodes itératives
<div class="alert alert-info" role="alert" markdown="1">
Les méthodes itératives s'approchent pas à pas de la solution recherchée et permettent de trouver une approximation de ${\bf x}$ dans $A\, {\bf x} = b$.
</div>
On arrête le calcul lorsqu'on est à une distance choisie de la solution, appelée **l'erreur.**
<div class="alert alert-warning" role="alert" markdown="1">
**On cherchera jamais à avoir une erreur plus petite que notre précision maximale**.
</div>
On a une formule $\; {\bf x}^{t+1} = B \, {\bf x}^t + {\bf c}\;$ ou en Python:

``` python
x = np.random(size = c.size)
while np.square(x - old_x) > seuil:
    old_x = x
    x = B @ x + c
```

<div class="alert alert-success" role="alert">
Si ${\bf x}$ converge on a atteint un point fixe, c.a.d ${\bf x}^{t+1} = {\bf x}^t$ et donc 

$${\bf x}^t = B \, {\bf x}^t + {\bf c} \quad \textrm{c.a.d.} \quad (Id -B) \, {\bf x}^t = {\bf c}$$
</div>

## Méthode de Jacobi
<div class="alert alert-info" role="alert" markdown="1">
La méthode de Jacobi découpe la matrice A en M et N avec

* $M$ : matrice diagonale des éléments de la diagonale de $A$
* $N = M - A$  (donc 0 sur la diagonale et l'opposé des éléments de $A$ ailleurs)

Le système à resoudre est $(M - N) {\bf x} = {\bf b}$.
</div>
La formule iterative pour $k + 1$ est : 
$$
M \; {\bf x}^{k+1} =  N\; {\bf x}^k + {\bf b}
$$
Comme $M$ est une matrice diagonale : 

$$
\begin{array}{l}
a_{11} x_1^{k+1} = \qquad -a_{12} \, x_2^k - a_{13} \, x_3^k  \ldots - a_{1n} \, x_n^k + b_1 \\
a_{22} x_2^{k+1} = -a_{21} \, x_1^k \qquad - a_{23} \, x_3^k  \ldots - a_{2n} \, x_n^k + b_2 \\
a_{33} x_3^{k+1} = -a_{31} \, x_1^k - a_{32} \, x_3^k  \qquad \ldots - a_{3n} \, x_n^k + b_3 \\
 \vdots \\
a_{nn} x_n^{k+1} = -a_{n1} \, x_1^k - a_{n2} \, x_3^k  \ldots - a_{n-1,n-1} \, x_{n-1}^k \qquad + b_n \\
\end{array}
$$
Pour calculer $x_i^{k+1}$ il faut diviser par $a_{ii}$ donc **il faut que $A$ n'ait pas pas de zéro sur sa diagonale**.
``` python
A = np.random.randint(10, size=(4,4))
b = A.sum(axis=1) # la solution est [1,1,1,1]
```
```
A:
 [[2 2 6 1]
 [3 9 6 1]
 [0 1 9 0]
 [0 9 3 4]] 
b:
 [11 19 10 16] 
```
``` python
M = np.diag(A)        # vecteur
N = np.diag(M) - A    # np.diag d'une matrice donne un vecteur, np.diag d'un vecteur donne une matrice
```
```
M:
 [[2 0 0 0]
 [0 9 0 0]
 [0 0 9 0]
 [0 0 0 4]]
N:
 [[ 0 -2 -6 -1]
 [-3  0 -6 -1]
 [ 0 -1  0  0]
 [ 0 -9 -3  0]]
```
``` python
x = np.random.random(4)
for i in range(20):
    x = (N @ x + b) / M
```
```
...
x_16 = [-4.194 -1.298  0.76  -4.026]
x_17 = [6.531 3.45  1.255 6.35 ]
x_18 = [-4.891 -1.608  0.728 -4.704]
x_19 = [7.277 3.779 1.29  7.073]
```
<div class="alert alert-warning" role="alert" markdown="1">
Ca ne converge pas.
</div>
2e essai :
``` python
A = np.random.randint(10, size=(4,4))
A = A + np.diag(A.sum(axis=0))
b = A.sum(axis=1) # la solution est [1,1,1,1]
```
```
A:
 [[24  2  4  8]
 [ 0 24  9  3]
 [ 4  6 16  5]
 [ 6  2  1 32]] 
b:
 [38 36 31 41] 
```
``` python
M = np.diag(A)        # vecteur
N = np.diag(M) - A    # np.diag d'une matrice donne un vecteur, np.diag d'un vecteur donne une matrice
```
```
M:
 [[24  0  0  0]
 [ 0 24  0  0]
 [ 0  0 16  0]
 [ 0  0  0 32]]
N:
 [[ 0 -2 -4 -8]
 [ 0  0 -9 -3]
 [-4 -6  0 -5]
 [-6 -2 -1  0]]
```
``` python
x = np.random.random(4)
for i in range(20):
    x = (N @ x + b) / M
```
```
...
x_17 = [1. 1. 1. 1.]
x_18 = [1. 1. 1. 1.]
x_19 = [1. 1. 1. 1.]
```
### Pourquoi le 2e cas marche ?
<div class="alert alert-info" role="alert" markdown="1">
Pour qu'une méthode itérative du type  ${\bf x} = B\; {\bf x} + {\bf c}$  converge il faut au choix :
* $\rho(B) < 1\quad$ 
    * $\rho$ : le rayon spectral (la plus grande valeur propre en valeur absolue)
* $||B|| < 1\quad$ où  : 
$$
||B|| = \sup_{\bf v} \frac{||B\, {\bf v}||}{||\textbf{v}||} = \sup_{\textbf{v} \, t.q. ||\textbf{v}|| = 1} ||B\, {\bf v}|| = \sup_{\textbf{v} \, t.q. ||\textbf{v}|| \le 1} ||B\, {\bf v}||
$$
</div>

#### Cas de la méthode de Jacobi
* On respecte ces conditions si $A$ est a **diagonale dominante**, c.a.d. que chaque élément de la diagonale est plus grand que tous les autres de sa ligne et colonne.
* Jacobi converge aussi si $A$ est symétrique, réelle et définie positive ($\forall {\bf x}, \; {\bf x}^T \, A \, {\bf x} > 0$).