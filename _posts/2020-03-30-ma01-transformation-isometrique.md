---
title:          "CAMA : ma01 Transformations isometriques"
date:           2020-03-30 10:00
categories:     [S6, Shannon, CAMA]
tags:           [S6, CAMA, Shannon]
description: Transformations isometriques
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/rk6uMXBnL)
# Cours du 30 / 03

``` python
angle = np.array([θ for θ in np.linspace(-np.pi/2,np.pi/2,7)])
shape1 = np.concatenate([np.array([np.cos(angle), np.sin(angle)]), 
                         np.array([[-0.5, -1, -1, -1], [1, 1, 0.5, 0]]),
                         np.array([[-0.5, 0], [-0.5, -1]])], axis=1)
```
```
[[ 0.     0.5    0.866  1.     0.866  0.5    0.    -0.5   -1.    -1.    -1.    -0.5    0.   ]
 [-1.    -0.866 -0.5    0.     0.5    0.866  1.     1.     1.     0.5    0.    -0.5   -1.   ]]
```
![](https://i.imgur.com/mDwFYuu.png)
## Matrice de rotation centrée en $(0, 0)$
<div class="alert alert-danger" role="alert" markdown="1">
$$R = \begin{bmatrix}
cos(θ) & -sin(θ) \\
sin(θ) & cos(θ)  \\
\end{bmatrix}$$
</div>
### Propriétés
* Effectue une rotation de centre (0,0) et d'angle θ
* Déterminant = 1
* Matrice orthogonale $\rightarrow$ pas de déformation ni d'agrandissement de la forme (automorphisme orthogonal)

``` python
θ = np.pi / 4

R = np.array([[np.cos(θ), -np.sin(θ)], [np.sin(θ), np.cos(θ)]])
```
```
[[ 0.707 -0.707]
 [ 0.707  0.707]]
```
``` python
R @ shape1 # multiplication de matrices
```
![](https://i.imgur.com/5gX0s31.png)
* Matrice orthogonale donc (par définition) $R.R^T = \textrm{Id}$.
* La transposée est la rotation d'angle -θ puisque sinus est une fonction impaire.

## Symétrie axiale
<div class="alert alert-danger" role="alert" markdown="1">
La symétrie horizontale tranformant (a,b) en (a,-b) est:
$$Sx = \begin{bmatrix}
1 & 0 \\
0 & -1  \\
\end{bmatrix}$$
</div>
<div class="alert alert-info" role="alert" markdown="1">
Pour avoir un symétrie axiale par rapport à une droite passant par $(0,0)$ qui a un angle $\alpha$ :
* rotation pour mettre l'axe de symétrie a l'horizontale
* appliquer la symétrie horizontale
* faire la rotation inverse
$$
S = R_{-α}^{-1}\; Sx\; R_{-α} = R_α\;Sx\; R_{-α}
$$
</div>
``` python
def Rα(α):
    return np.array([[np.cos(α), -np.sin(α)], [np.sin(α), np.cos(α)]])

Sx = np.array([[1, 0],[0,-1]])

θ = 70 * (2 * np.pi)/360  # 70 degrés

Rα(θ) @ Sx @ Rα(-θ) @ shape1
```
![](https://i.imgur.com/6xoIcP1.png)
La rotation selon l'angle est :
``` python
Rα(θ) @ Sx @ Rα(-θ)
```
```
[[-0.766  0.643]
 [ 0.643  0.766]]
```

## Translation
<div class="alert alert-warning" role="alert" markdown="1">
La translation ne peut pas etre exprimée avec un produit matriciel car ce n'est pas une **application linéaire :**
$$
T(2\;\textbf{x}) \ne 2\; T(\textbf{x})
$$
Ce n'est pas non plus une **transformation isométrique**.
</div>
* Une translation est une addition : $T(\textbf{x}) = \textbf{x} + \textbf{v}_t$.
* On change la représentation des points pour exprimer les translations sous forme de produit matriciel : $\textbf{x} = (x_1, x_2)$ devient $\textbf{x} = (x_1, x_2, 1)$
<div class="alert alert-danger" role="alert" markdown="1">
La translation par le vecteur $(v_1, v_2)$ est : 
$$T(X) = 
\begin{bmatrix}
1 & 0 & v_1\\
0 & 1 & v_2 \\
0 & 0 & 1 \\
\end{bmatrix}
\begin{bmatrix}
x_1 \\
x_2 \\
1 \\
\end{bmatrix}$$
</div>
``` python
v = np.array([1,2])

T = np.identity(3) # matrice de translation
T[0:2,2] = v
```
```
Matrice de translation:
 [[1. 0. 1.]
 [0. 1. 2.]
 [0. 0. 1.]]
```
``` python
shape1_3d = np.concatenate([shape1, np.ones((1, len(shape1[0])))], axis=0) 
# rajoute une nouvelle dimension à la matrice pour la translation
T @ shape1_3d
```
![](https://i.imgur.com/mDN8rHe.png)
<div class="alert alert-info" role="alert" markdown="1">
La matrice inverse replacant la forme orange à sa position d'origine applique la transition $-\textbf{v} = (-1,-2)$.
$$T^{-1} = 
\begin{bmatrix}
1 & 0 & -1\\
0 & 1 & -2 \\
0 & 0 & 1 \\
\end{bmatrix}$$
Ce n'est pas la transposée de T, T n'est pas **orthogonale**.
</div>
Il y a 2 types d'isométries : 
* l'isométrie *vectorielle* ou *automorphisme orthogonal* : $$\forall\, \textbf{x}, \;||\textbf{f}(\textbf{x})|| = \textbf{x}$$ et conserve les angles
* l'isométrie *geométrique* : $$\forall\, \textbf{a}, \textbf{b}, \; ||\textbf{f}(\textbf{a}) - \textbf{f}(\textbf{b})|| = ||\textbf{a} - \textbf{b}||$$.
<div class="alert alert-info" role="alert" markdown="1">
La translation est une isométrie geométrique mais pas vectorielle, c'est un **automorphisme orthogonal**.
</div>