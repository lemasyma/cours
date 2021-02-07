---
title:          "CAMA : ma05 Vectors propres -- Applications"
date:           2020-03-30 10:00
categories:     [S6, Shannon, CAMA]
tags:           [S6, CAMA, Shannon]
description: Vectors propres -- Applications
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/BkKm0wR2L)
# Cours du 30 / 03

## Nuage de points
<div style="background-color:rgba(24, 20, 255, 0.5); text-align:center; vertical-align: middle; padding:40px 0;"  markdown="1">
On peut étudier la forme d'un nuage de points par une **analyse en composantes principales (ACP)**, c.a.d. chercher les vecteurs propres de la matrice de covariance ou de corrélation.
</div>
On vérifie avec un nuage de points ayant une corrélation forte entre $x$ et $y$ : 
$$  y = 0.2 \, x + 1.45 + U(-1,1) \quad \textrm{avec U la loi uniforme qui simule du bruit.}
$$
Entre x et y il y a:
* une pente de 0.2
* un décalage vertical de 1.45 en x = 0
<div style="background-color:rgba(250, 178, 45, 0.5); text-align:center; vertical-align: middle; padding:40px 0;"  markdown="1">
On essaye de retrouver la corrélation entre x et y malgré le bruit avec seulement le nuage de points.
</div>
``` python
N = 50
x = 6 * np.random.rand(N) - 3
nuage = np.array([x, 0.2 * x + 1.45 + np.random.rand(N)])
```
![](https://i.imgur.com/3OKHvTV.png)

On cherche la droite qui minimise la distance entre les points et leur projection sur la droite.
<div style="background-color:rgba(23, 252, 31, 0.5); text-align:center; vertical-align: middle; padding:40px 0;"  markdown="1">
On construit la **matrice de covariance**, le premier vecteur propre est égal au coefficient 0.2 et est le vecteur directeur de la droite recherchée. On fait la moyenne du nuage de point dans un point de la droite. 
</div>
``` python
cov = np.cov(nuage.copy()) # estime la matrice de covariance
```
```
array([[2.744, 0.48 ],
       [0.48 , 0.168]])
```
``` python
val, vec = lin.eig(cov)
val = val.astype('float')  # on convertit puisqu'on sait que ce sont des réels
```
```
Valeurs propres de la matrice de covariance : [2.831 0.081] 

Vecteurs propres de la matrice de covariance :
 [[ 0.984 -0.177]
 [ 0.177  0.984]]
```
![](https://i.imgur.com/TnpFGdD.png)
``` python
moyenne = nuage.mean(axis=1) # Point moyen du nuage
```
```
[0.328 2.085]
```
``` python
eq_droite = lambda x: pente * (x - moyenne[0]) + moyenne[1]
```
![](https://i.imgur.com/Q2BLHjo.png)

## Matrice de covariance
<div style="background-color:rgba(252, 23, 23, 0.5); text-align:center; vertical-align: middle; padding:40px 0;"  markdown="1">
La **covariance** entre deux variables indique à quel point elles sont liées.
$$
\textrm{cov}(\textbf{x},\textbf{y}) = \frac{1}{N} \sum_{i=1}^N (x_i - \overline{\textbf{x}}) (y_i - \overline{\textbf{y}})
$$
* $N$ le nombre de points du nuage
* $\overline{\textbf{x}}$ et $\overline{\textbf{y}}$ les moyennes de $\textbf{x}$ et de $\textbf{y}$.
</div>
La matrice de covariance exprime toutes les covariances possibles : 

$$
\textrm{Cov(nuage 2D)} = 
\begin{bmatrix}
\textrm{cov}(\textbf{x},\textbf{x}) & \textrm{cov}(\textbf{x},\textbf{y}) \\
\textrm{cov}(\textbf{y},\textbf{x}) & \textrm{cov}(\textbf{y},\textbf{y})  \\
\end{bmatrix}
$$

``` python
cov = lambda x,y : np.dot((x - x.mean()), (y - y.mean())) / len(x)
Cov = lambda x,y : np.array([[cov(x,x), cov(x,y)], [cov(y,x), cov(y,y)]])
Cov(nuage[0], nuage[1])
```
```
array([[2.69 , 0.47 ],
       [0.47 , 0.164]])
```
## Fibonnacci
<div style="background-color:rgba(24, 20, 255, 0.5); text-align:center; vertical-align: middle; padding:40px 0;"  markdown="1">
Tu le sais, je le sais, on le sais Fibonnacci c'est ca :
$$x_n = x_{n-2} + x_{n-1}$$ 
* $x_0 = 1$
* $x_1 = 1$.
</div>
<div style="background-color:rgba(250, 178, 45, 0.5); text-align:center; vertical-align: middle; padding:40px 0;"  markdown="1">
Quelle est la complexité pour calculer $x_n$?
</div>
Ecrivons fibonnacci sous forme d'un système matriciel : 
$$\begin{align}
x_{n-1} &= x_{n-1} \\
x_n &= x_{n-2} + x_{n-1} \\
\end{align}$$
ce qui donne
$$\begin{bmatrix}
x_{n-1}\\
x_n  \\
\end{bmatrix} =
\begin{bmatrix}
0 & 1 \\
1 & 1 \\
\end{bmatrix}
\begin{bmatrix}
x_{n-2}\\
x_{n-1}  \\
\end{bmatrix}$$
<div style="background-color:rgba(250, 178, 45, 0.5); text-align:center; vertical-align: middle; padding:40px 0;"  markdown="1">
Calculer n produits matriciels n'est pas rentable.
</div>
<div style="background-color:rgba(23, 252, 31, 0.5); text-align:center; vertical-align: middle; padding:40px 0;"  markdown="1">
Sachant que $F = P\, D\, P^{-1}$, avec P matrice des vecteurs propres et D matrice diagonale des valeurs propres : 
$$
\begin{bmatrix}
x_{n}\\
x_{n+1}  \\
\end{bmatrix} =
\begin{bmatrix}
0 & 1 \\
1 & 1 \\
\end{bmatrix}^n
\begin{bmatrix}
x_{0}\\
x_{1}  \\
\end{bmatrix}
= (P\, D\, P^{-1})^n
\begin{bmatrix}
x_{0}\\
x_{1}  \\
\end{bmatrix}
= P\, D^n\, P^{-1}
\begin{bmatrix}
x_{0}\\
x_{1}  \\
\end{bmatrix}
$$
On peut calculer $x_n$ en **temps constant**.
</div>
``` python
fval, fvec = lin.eig(F)
fval = fval.astype('float')  # la matrice est symétrique donc ses valeurs propres sont réelles
```
```
Valeurs propres de la matrice de fibonnacci : [-0.618  1.618] 

Vecteurs propres de la matrice de fibonnacci :
 [[-0.851 -0.526]
 [ 0.526 -0.851]]
```
``` python
fibo = lambda n : (fvec @ np.diag(fval**n) @ lin.inv(fvec) @ x0)[0]
```

## Google page rank
<div style="background-color:rgba(24, 20, 255, 0.5); text-align:center; vertical-align: middle; padding:40px 0;"  markdown="1">
Soit $N$ pages web numerotées qui font référence les unes aux autres. La i-ième ligne montre par qui est référencée la i-ième page web. Il y a 1 dans la j-ième colonne si la page j cite la page i et 0 sinon.
</div>
``` python
np.random.seed(42)
A = np.random.randint(2,size=(8,8))
for i in range(len(A)):
    A[i,i] = 0   # on ne compte pas les auto-référencements
```
```
array([[0, 1, 0, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 1, 0],
       [1, 1, 0, 0, 1, 0, 1, 1],
       [1, 1, 1, 0, 1, 1, 0, 0],
       [1, 1, 1, 0, 0, 0, 0, 0],
       [0, 0, 1, 1, 1, 0, 1, 0],
       [1, 1, 0, 1, 0, 1, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0]])
```
<div style="background-color:rgba(250, 178, 45, 0.5); text-align:center; vertical-align: middle; padding:40px 0;"  markdown="1">
Le classement des pages utilise les vecteurs propres de cette matrice.
</div>
``` python
val_pr, vec_pr = lin.eig(A)
np.abs(vec_pr[:,0]).astype(float) # valeur des pages
A.sum(axis=1) # nombre de citations
```
```
Valeur des pages    : [0.217 0.153 0.376 0.489 0.243 0.514 0.47  0.071]
Nombre de citations : [2 1 5 5 3 4 5 1]
```
<div style="background-color:rgba(23, 252, 31, 0.5); text-align:center; vertical-align: middle; padding:40px 0;"  markdown="1">
* La page ayant le meilleur score n'a que 4 citations mais est citée par les 3 pages ayant 5 citations
* une page ayant 5 citations est moins bien notée que les autres car elle n'est pas citée par la meilleure page

La matrice A est une application linéaire dont l'orientation principale est celle du premier vecteur propre. Le coefficient le plus important de ce vecteur indique la page web la plus importante.
</div>