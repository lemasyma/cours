---
title:          "CAMA : ma41 Système matriciel non linéaire"
date:           2020-05-25 10:00
categories:     [S6, Shannon, CAMA]
tags:           [S6, CAMA, Shannon]
description: Système matriciel non linéaire
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/BJ8QNnfh8)
# Cours du 25 / 06

<div class="alert alert-info" role="alert" markdown="1">
Si la matrice $A$ dépend de ${\bf x}$ (noté $A({\bf x})$), alors le système matriciel 
$$
A({\bf x)x = b}
$$
**n'est pas linéaire**.
</div>

**Exemple :**

$$
\begin{bmatrix}
1 &  x_1 \\
2x_1 & -x_2 \\
\end{bmatrix}
\;
\begin{bmatrix}
x_{1} \\
x_{2} \\
\end{bmatrix} =
\begin{bmatrix}
b_{1} \\
b_{2} \\
\end{bmatrix}
$$

donne le système suivant non linéaire puisqu'on a des
carrés :

$$
\begin{align}
x_1 + x_1 \, x_2 &= b_1 \\
2 \, x_1^2  - x_2^2 &= b_2 
\end{align}
$$

*Comment résoudre un tel système ?*

## La méthode du point fixe
<div class="alert alert-info" role="alert" markdown="1">
La méthode du point fixe consiste à appliquer l'algorithme itératif suivant : 
$$
{\bf x}^{k+1} = g({\bf x}^k)
$$
pour résoudre $g({\bf x}) = {\bf x}$.
</div>
* $x_0$ donné
* ${\bf \bar x} = g({\bf \bar x})$ un point fixe de $g$
* ${\bf x}^{k+1} = g({\bf x}^k)$ avec $k = 0, 1, 2, ...$

***Est-ce que $g({\bf x}^k)^k$ converge ?***
* Si $\bf{x_0} \lt {\bf \bar x_2}$ : $\lim_{k\to+\infty} = {\bf \bar x_1}$
* Si $\bf{x_0} \gt {\bf \bar x_2}$ : $\lim_{k\to+\infty} = +\infty$
<div class="alert alert-warning" role="alert" markdown="1">
Selon le point de départ, la méthode converge ou diverge.
</div>

### La méthode du point fixe pour résoudre $A({\bf x)x = b}$
<div class="alert alert-danger" role="alert" markdown="1">
On doit définir une fonction $g$ telle que la solution de $J({\bf x}) = {\bf x}$ soit la solution du système matriciel non linéaire : 
$$
g({\bf x}) = A^{-1}({\bf x}) \, {\bf b}
$$
</div>
Inverser A est trop coûteux, on écrit notre algorithme itératif sous forme de problème matriciel linéaire à résoudre:
$$
A({\bf x}^k) \, {\bf x}^{k+1} = {\bf b}
$$
Si on connait ${\bf x}^k$ on peut évaluer $A({\bf x}^k)$, le système est linéaire et permet de trouver ${\bf x}^{k+1}$.
Le fonctionnement de l'algorithme va dépendre du type de la matrice $A$ et de la valeur initiale $x_0$.

#### Exemple :
$$
\begin{bmatrix}
x_0 - 2 x_1 &  x_1 \\
x_0 & 2 x_0 + x_1 \\
\end{bmatrix}
\;
\begin{bmatrix}
x_0 \\
x_1 \\
\end{bmatrix} =
\begin{bmatrix}
1 \\
9 \\
\end{bmatrix}
$$
Ce système a pour solutions [1, 2] et [2, 1].
``` python
def A(x):
    return np.array([[x[0] - 2*x[1], x[1]] ,
                     [x[0] , x[1] + 2*x[0]]]) / 10 

b = np.array([1, 9]) / 10         # avec normalisation grossière

x = np.array([1, 1])
for i in range(1, 10):
    x = lin.solve(A(x), b)
```
```
...
x^7 =  [1.37317932 2.74635363]
x^8 =  [0.72823777 1.45647516]
x^9 =  [1.37317809 2.74635608]
```
La solution oscille sans converger. La méthode du point fixe a un petit rayon de convergence.
##### Appliquon l'inertie
``` python
µ = 0.5  # on avance de moitié vers le prochain x

x = np.array([3, 2])
for i in range(1, 10):
    x_old = x
    x = lin.solve(A(x), b)
    x = µ * x + (1-µ) * x_old
```
```
...
x^9 =  [1.00876429 1.98253948]
```
<div class="alert alert-success" role="alert">
La convergence est rapide (9 iterations). L'inertie augmente le rayon de convergence : plus $\mu$ est petit plus le rayon de convergence est grand.
</div>
<div class="alert alert-info" role="alert" markdown="1">
Pour trouver les autres solutions il faut choisir un autre point initial.
</div>

## La méthode de Newton-Raphson
<div class="alert alert-danger" role="alert" markdown="1">
$$
{\bf x}^{k+1} = {\bf x} - \frac{f({\bf x_n})}{f'({\bf x_n})}
$$
</div>
<div class="alert alert-info" role="alert" markdown="1">
La méthode de Newton est une méthode de point fixe.
$$
{\bf x}^{k+1} = g({\bf x}^k)
$$
où $g({\bf x)} = {\bf x} - \frac{f({\bf x})}{f'({\bf x})}$
</div>
On souhaite résoudre notre systeme non linéaire. Grâce à la formule ci-dessus, on a en 1D:
$$
f'(x^k) \; (x^{k+1} - x^k) = - f(x^k)
$$
Ce qui donne en $n$ dimensions:
$$
J_{\bf f}({\bf x}^k) \; ({\bf x}^{k+1} - {\bf x}^k) =  - {\bf f}({\bf x}^k)
$$
avec $J_{\bf f}$ la matrice Jacobienne de ${\bf f}$ :

$$
J_{\bf f}\left({\bf x}\right)=
\begin{pmatrix} 
\dfrac{\partial f_1}{\partial x_1} & \cdots & \dfrac{\partial f_1}{\partial x_n} \\
\vdots & \ddots & \vdots \\
\dfrac{\partial f_n}{\partial x_1} & \cdots & \dfrac{\partial f_n}{\partial x_n}
\end{pmatrix}
$$
Notre système non linéaire avec $f$ une fonction vectorielle:
$$
{\bf f}({\bf x}) = A({\bf x})\, {\bf x} - {\bf b}
$$
### Exemple
On reprend le système matriciel précèdent. La matrice Jacobienne de la fonciton $f$ est : 
$$
J_{\bf f}({\bf x}) = 
\begin{bmatrix}
2 x_0 - 2 x_1 &  2 x_1  - 2 x_0\\
2 x_0 + 2 x_1 & 2 x_0 + 2 x_1 \\
\end{bmatrix}
$$
``` python
def f(x):
    return A(x) @ x - b

def J_f(x):
    return 2 * np.array([[x[0] - x[1], x[1] - x[0]],
                         [x[0] + x[1], x[0] + x[1]]])

x = np.array([3, 2])
for i in range(30):
    delta = lin.solve(J_f(x), -f(x))
    x = x + delta
```
```
...
x^29 =  [2.05693134 1.05693134]
```
On converge (moins vite) où la methode du point fixe oscille sans converger.
<div class="alert alert-warning" role="alert" markdown="1">
* Le coût de la construction de la matrice Jacobienne peut être tres élevé.
* Pour aller plus vite on peut recalculer la matrice toutes les 3 iterations ou plus.
* Il s'agit d'une matrice pleine qui rend compliqué la resolution du systeme (une methode de gradient ne marchera pas)
</div>