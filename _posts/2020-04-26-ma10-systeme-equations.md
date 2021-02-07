---
title:          "CAMA : ma10 Système d'équations"
date:           2020-04-26 10:00
categories:     [S6, Shannon, CAMA]
tags:           [S6, CAMA, Shannon]
description:  Système d'équations
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/ryhz1KA3U)
# Cours du 26 / 04

## Systèmes matriciels
<div style="background-color:rgba(252, 23, 23, 0.5); text-align:center; vertical-align: middle; padding:40px 0;"  markdown="1">
Un système de plusieurs équations à autant d'inconnues peut s'écrire comme système matriciel $A {\bf x} = {\bf b}$ : 
$$
\begin{bmatrix}
a_{11} a_{12} \ldots a_{1n} \\
a_{21} a_{22} \ldots a_{2n} \\
 \vdots \\
a_{n1} a_{n2} \ldots a_{nn} \\
\end{bmatrix}
\;
\begin{bmatrix}
x_{1} \\
x_{2} \\
\vdots \\
x_{n} \\
\end{bmatrix} =
\begin{bmatrix}
b_{1} \\
b_{2} \\
\vdots \\
b_{n} \\
\end{bmatrix}
$$
</div>

### Exemple
On acheté 3 fois des quantités de fruits dont nous n'avons pas le prix.
``` python
# A est la quantité de chaque fruit achetée
# x est le prix de chaque fruit
# b est la somme qu'on a payé pour chaque course

A = np.array([[6,5,4], [5,3,2], [7,3,2]])
b = np.array([11.7, 7.9, 9.5])

x = lin.inv(A) @ b
```
```
array([0.8, 0.9, 0.6])
```
## Résolution d'un système matriciel
### Méthode du pivot de Gauss
<div style="background-color:rgba(24, 20, 255, 0.5); text-align:center; vertical-align: middle; padding:40px 0;"  markdown="1">
On transforme $A$ en une matrice triangulaire pour résoudre le système de $O(n^2)$ opérations.
</div>
On met des $0$ sur la première colonne en dessous de la diagonale en multipliant $A$ par la matrice $E_1$ suivante : 
$$
E_1 = 
\begin{bmatrix}
\;1 \quad 0\; 0 \ldots 0 \\
\frac{-a_{21}}{a_{11}} \, 1\; 0  \ldots 0 \\
\frac{-a_{31}}{a_{11}} \, 0\; 1  \ldots 0 \\
\vdots \\
\frac{-a_{n1}}{a_{11}}\; 0\; 0  \ldots 1 \\
\end{bmatrix}
$$
$E_2$ sera similaire avec des termes $\frac{-a_{k2}}{a_{22}}$ sous la diagonale, de même pour les matrices $E_n$ suivantes.
<div style="background-color:rgba(250, 178, 45, 0.5); text-align:center; vertical-align: middle; padding:40px 0;"  markdown="1">
Si on multiplie $A$ par $E_1$ il faut également multiplier $b$ par $E_1$.
</div>
#### Système matriciel avec matrice triangulaire
<div style="background-color:rgba(24, 20, 255, 0.5); text-align:center; vertical-align: middle; padding:40px 0;"  markdown="1">
Il faut résoudre $U{\bf x} = c$ avec $U$ une matrice triangulaire supérieure.
</div>
On part de la dernière ligne et on obtient
$$
{\bf x}[-1] = \frac{c[-1]}{U[-1, -1]}
$$
Une fois ${\bf x}[-1]$ connu, on en déduit la valeur de ${\bf x}[-2]$, puis celle de ${\bf x}[-3]$, etc.
``` python
def solve_gauss(A, b):
    for i in range(len(A)-1):
        E = np.diag(np.array([1.,] * len(A), dtype=A.dtype))
        coefs = - A[i+1:,i] / A[i,i]
        E[i+1:,i] = coefs
        A[i:, i:] = E[i:,i:] @ A[i:,i:]
        b[i+1:] += coefs * b[i]   # multiplication terme à terme
    # A est maintenant triangulaire supérieur
    res = np.zeros(len(b), dtype=b.dtype)
    res[-1] = b[-1] / A[-1,-1]
    for i in range(len(A)-1)[::-1]:
        res[i] = (b[i] - A[i,i+1:] @ res[i+1:]) / A[i,i]
    return res
```
``` python
A = 10 * np.random.random(size=(5,5))
b = A.sum(axis=1)
```
```
A
 [[5.655 3.042 3.18  9.672 8.761]
 [3.963 9.923 9.868 7.934 6.328]
 [0.697 9.189 7.799 2.046 2.184]
 [6.314 8.533 4.879 8.112 4.583]
 [3.803 6.89  2.266 6.087 0.361]] 
b
 [30.31  38.015 21.914 32.42  19.407]
```
``` python
solve_gauss(A, b)
```
### Décomposition Lower Upper
<div style="background-color:rgba(24, 20, 255, 0.5); text-align:center; vertical-align: middle; padding:40px 0;"  markdown="1">
Si on a besoin de résoudre plusieurs systèmes matriciels avec $A$, on décompose $A$ en un produit d'une matrice triangulaire inférieure et d'une matrice triangulaire supérieure.
$$
A = LU
$$
</div>
On utilise le pivot de Gauss mais au lieu de modifier $b$, on calcule l'inverse de la matrice $E_n \ldots E_2\, E_1$ : 

$$
\begin{aligned}
E_n \ldots E_2\, E_1 \, A\, x &= E_n \ldots E_2\, E_1 \, b \quad \textrm{donc} \\
(E_n \ldots E_2\, E_1)^{-1} \, E_n \ldots E_2\, E_1 \, A\, x &=  b \\
E_1^{-1} \, E_2^{-1} \ldots E_n^{-1} \; E_n \ldots E_2\, E_1 \, A\, x &=  b \\
\end{aligned}
$$
<div style="background-color:rgba(250, 178, 45, 0.5); text-align:center; vertical-align: middle; padding:40px 0;"  markdown="1">
Ce calcul est **simple**, la matrice inverse a les valeurs opposées : 
$$
E_1^{-1} = 
\begin{bmatrix}
\;1 \quad 0\; 0 \ldots 0 \\
\frac{a_{21}}{a_{11}} \, 1\; 0  \ldots 0 \\
\frac{a_{31}}{a_{11}} \, 0\; 1  \ldots 0 \\
\vdots \\
\frac{a_{n1}}{a_{11}}\; 0\; 0  \ldots 1 \\
\end{bmatrix}
$$
</div>
<div style="background-color:rgba(250, 178, 45, 0.5); text-align:center; vertical-align: middle; padding:40px 0;"  markdown="1">
Le produit $E^{-1} = E_1^{-1} \,E_1^{-1} \,E_2^{-1} \,E_3^{-1} \, \ldots \,E_n^{-1}$ est la concaténation des colonnes : 
$$
E^{-1} = 
\begin{bmatrix}
\;1 \quad 0\; \; 0 \ldots 0 \\
\frac{a_{21}}{a_{11}} \; \; 1\; \; 0  \ldots 0 \\
\frac{a_{31}}{a_{11}} \, \frac{a_{32}}{a_{22}}  \; 1  \ldots 0 \\
\vdots \\
\frac{a_{n1}}{a_{11}}\; \frac{a_{n2}}{a_{22}}\; \frac{a_{n3}}{a_{33}}  \ldots 1 \\
\end{bmatrix}
$$
</div>
Pour résoudre $L\, U \, {\bf x} = {\bf b}$ : 
1. on résoud $L\, {\bf y}  = {\bf b}$ obtenant ${\bf y}$ 
2. on résoud $U\, {\bf x} = {\bf y}$ obtenant la solution ${\bf x}$

``` python
def LU(A):
    L = np.diag([1.,] * len(A))
    for i in range(len(A)-1):
        E = np.diag([1.,] * len(A))
        E[i+1:,i] = - A[i+1:,i] / A[i,i]
        L[i+1:,i] = -E[i+1:,i]
        A[i:, i:] = E[i:,i:] @ A[i:,i:]
    return L, A
```
``` python
A = 10 * np.random.random(size=(5,5))
L,U = LU(A.copy())  # Attention, notre fonction modifie A donc si on veut le réutiliser il faut une copie
```
```
A
 [[2.697 6.265 5.876 1.927 3.951]
 [2.495 0.021 9.085 0.504 9.23 ]
 [0.788 1.982 5.048 9.656 8.581]
 [3.19  7.474 8.344 0.124 2.577]
 [4.209 6.825 9.223 9.025 4.733]]
L
[[ 1.     0.     0.     0.     0.   ]
 [ 0.925  1.     0.     0.     0.   ]
 [ 0.292 -0.026  1.     0.     0.   ]
 [ 1.183 -0.011  0.418  1.     0.   ]
 [ 1.561  0.511 -0.529 -1.924  1.   ]]
U
[[  2.697   6.265   5.876   1.927   3.951]
 [  0.     -5.776   3.647  -1.279   5.574]
 [  0.      0.      3.427   9.059   7.573]
 [  0.      0.      0.     -5.957  -5.201]
 [  0.      0.      0.      0.    -10.285]]
```
``` python
A - (L @ U)
```
```
array([[ 0.,  0.,  0.,  0.,  0.],
       [ 0., -0.,  0.,  0.,  0.],
       [ 0.,  0., -0.,  0.,  0.],
       [ 0.,  0.,  0., -0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.]])
```
### Gauss Jordan
<div style="background-color:rgba(24, 20, 255, 0.5); text-align:center; vertical-align: middle; padding:40px 0;"  markdown="1">
On diagonalise $A$ par des multiplications matricielles similaire à celles de Gauss qui annulent aussi les termes au dessus de la diagonale : 
$$
E_3 = 
\begin{bmatrix}
1 \; 0\; \frac{-a_{11}}{a_{33}} \;  0 \ldots 0 \\
0 \; 1\; \frac{-a_{21}}{a_{33}} \;  0 \ldots 0 \\
0 \; 0\quad 1 \quad  0 \ldots 0 \\
0 \; 0\; \frac{-a_{41}}{a_{33}}  1 \ldots 0 \\
\vdots \\
0 \; 0\; \frac{-a_{n1}}{a_{33}}  0 \ldots 1 \\
\end{bmatrix}
$$
</div>
``` python
def solve_gauss_jordan(A,b):
    for i in range(len(A)):
        d1 = np.diag([1.,] * len(A))
        d1[:,i] = - A[:,i] / A[i,i]
        A = d1 @ A
        b = d1 @ b
    return b / np.diag(A)
```
``` python
A = 10 * np.random.random(size=(5,5))
b = A.sum(axis=1)
solve_gauss_jordan(A, b)
```
```
array([1., 1., 1., 1., 1.])
```