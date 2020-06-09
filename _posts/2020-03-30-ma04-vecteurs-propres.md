---
layout: post
mathjax:    true
comments:   true
title:  "CAMA : ma04"
date:   2020-03-30 10:00
tags:   Shannon CAMA
description: Vecteurs propres
---
# CAMA : ma04 Vecteurs propres
# Cours du 30 / 03

Soit A une matrice qui représente une application linéaire quelconque. Que se passe-t-il si on l'applique $n$ fois ?
![](https://i.imgur.com/Nv1qhKD.png)
```
array([[ 0.707,  0.966,  0.966,  0.707,  0.259, -0.259, -0.707, -1.061, -1.414, -1.061, -0.707, -0.   ,  0.707],
       [-0.707, -0.259,  0.259,  0.707,  0.966,  0.966,  0.707,  0.354,  0.   , -0.354, -0.707, -0.707, -0.707]])
```
```python=
# on prend une matrice de transformation au hasard (donc probablement pas orthoganale)
A = np.array([[3,2], [1,2]])
```
```python=
as1 = np.dot(A, mouse)
as2 = 3 * A @ mouse # souris 3 fois plus grande
```
![](https://i.imgur.com/ATVie90.png)
:::info
La transformation n'est pas une isométrie donc la matrice n'est pas orthogonale.
:::
:::warning
La souris 3x plus grande est isométrique car $A$ est une application linéaire.
:::
```python=
aas1 = A @ A @ mouse
aaas1 = A @ A @ A @ mouse
```
![](https://i.imgur.com/wf9vAdY.png)
La figure s'étire suivant le vecteur $(2, 1)$
:::warning
Si $A{\bf x}$ fait tourner la souris d'environ 25°, appliquer 2 ou 3 fois $A$ ne fait plus tourner la figure.
:::

## Vecteurs propres et valeurs propres
:::danger
Les valeurs et vecteurs propres respectent cette priopriété : 
$$ 
A \, {\bf v_i} = \lambda_i \, {\bf v_i} 
$$
* $(\lambda_i, {\bf v_i})$ : couple valeur / vecteur propres
:::
```python=
val_propre, vec_propre = lin.eig(A)
```
```
Valeurs propres de A : [4.+0.j 1.+0.j] 

Vecteurs propres de A (chaque vecteur propre est écrit verticalement):
 [[ 0.894 -0.707]
 [ 0.447  0.707]]
```
:::danger
Les vecteurs propres sont des **attracteurs** qui capturent tous les points si on fait un nombre infini de multiplications par $A$.
Les points **s'alignent** sur l'un des deux vecteurs propres.
:::
```python=
N = 100
cercle = np.array([[np.cos(i * 2*np.pi/N), np.sin(i * 2*np.pi/N)] for i in range(N)]).T
a10c = np.array([x for x in (A10 @ cercle).T]).T
a10cn = np.array([x/lin.norm(x) for x in a10c.T]).T  # a10c normé
nb1 = np.sum([lin.norm(a10cn[:,i] - vec_propre[:,0]) < 0.01 for i in range(N)])   \
      + np.sum([lin.norm(a10cn[:,i] + vec_propre[:,0]) < 0.01 for i in range(N)])
nb2 = np.sum([lin.norm(a10cn[:,i] - vec_propre[:,1]) < 0.01 for i in range(N)])   \
      + np.sum([lin.norm(a10cn[:,i] + vec_propre[:,1]) < 0.01 for i in range(N)])
```
```
Nombre de points proche du 1er vecteur propre :  100
Nombre de points proche du 2e  vecteur propre :  0
```
Seuls les points colinéaires au second vecteur propre le resteront, les autres rejoignent le premier vecteur propre.

## Le cas des matrices de rotation
*Quels sont les vecteurs propres d'une matrice de rotation ?*
```python=
def Rot(θ):
    return np.array([[np.cos(θ), -np.sin(θ)], [np.sin(θ), np.cos(θ)]])

R = Rot(2*np.pi/10)

R_valp, R_vecp = lin.eig(R)
```
```
Valeurs propres de R : [0.809+0.588j 0.809-0.588j] 

Vecteurs propres de R :
 [[0.707+0.j    0.707-0.j   ]
 [0.   -0.707j 0.   +0.707j]]
```
```python=
# regardons un autre angle
R = Rot(2*np.pi/3)

R_valp, R_vecp = lin.eig(R)
```
```
Valeurs propres de R : [-0.5+0.866j -0.5-0.866j] 

Vecteurs propres de R :
 [[ 0.-0.707j  0.+0.707j]
 [-0.707+0.j    -0.707-0.j]]
```
:::info
* Les valeurs et vecteurs propres sont des complexes
* Les valeurs propres ont la même norme
:::
## Symétrie axiale horizontale
$$
Sx = 
\begin{bmatrix}
1 & 0 \\
0 & -1  \\
\end{bmatrix}
$$

```python=
Sx = np.array([[1, 0], [0, -1]])

Sx_valp, Sx_vecp = lin.eig(Sx)
```
```
Valeurs propres de Sx : [ 1.+0.j -1.+0.j] 

Vecteurs propres de Sx :
 [[1. 0.]
 [0. 1.]]
```

* Une matrice diagonale modifie que la i-ième coordonnéee de ${\bf x}$ par la i-ième valeur de sa diagonale.
* Ses vecteurs propres sont ceux de la base d'origine : 
```python=
D = np.diag(np.random.randint(10,size=5))
D_valp, D_vecp = lin.eig(D)
```
```
Valeurs propres de D : [8.+0.j 8.+0.j 4.+0.j 7.+0.j 1.+0.j] 

Vecteurs propres de D :
 [[1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]]
```

## Diagonalisation d'une matrice
:::danger
En changeant de repère, on peut représenter une application linéaire par une matrice diagonale contenant ses valeurs propres.
$$
\exists P \; / \; A = P\, \Lambda \, P^{-1} \quad
$$
* avec $\Lambda$ la matrice diagonale des valeurs propres $\lambda_i$
* P matrice de passage : vecteurs propres
:::
```python=
A
vec_propre @ np.diag(val_propre) @ lin.inv(vec_propre)
```
```
A :
 [[3 2]
 [1 2]] 

𝑃 Λ inv(𝑃) :
 [[3.+0.j 2.+0.j]
 [1.+0.j 2.+0.j]
```
* **Matrice inversible :** si une des valeurs propre est nulle alors $\Lambda$ n'est pas inversible et donc A n'est pas inversible
* **Matrice non diagonalisable :** si l'ensemble des vecteurs propres ne genere pas un espace de meme dimension que d'origine, alors on ne peut pas diagonaliser la matrice
