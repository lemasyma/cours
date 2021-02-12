---
title:          "CAMA : ma33 - Gradient pour résoudre Ax = b -- Exercice"
date:           2020-05-17 10:00
categories:     [S6, Shannon, CAMA]
tags:           [S6, CAMA, Shannon]
description: La méthode du gradient pour résoudre A x = b
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/B1XUcypyD)
# Cours du 17/05

# La méthode du gradient pour résoudre A x = b

Le but de ce TP est de vous laisser avancer tout seul. Reprenez les cours et programmez la méthode du gradient
pour résoudre le système matriciel $A {\bf x} = {\bf b}$ avec A symétrique et à diagonale dominante
($a_{ii} > \sum_{k \ne i} |a_{ik}|$).

* Commencez en 2D avec une matrice 2x2, vérifier que le résultat est bon et tracer la courbe de convergence
* Passez en nxn (on montrera que cela marche avec une matrice 9x9)

Il peut être intéressant de normaliser la matrice A pour éviter que les calculs explosent.

<details markdown="1">
<summary>Solution</summary>

## 2x2
~~~ python
# plein de copier coller du cours

import numpy as np
import scipy.linalg as lin
import matplotlib.pylab as plt
import plotly.offline as py
import plotly.graph_objects as go

%matplotlib inline
%config InlineBackend.figure_format = 'retina'

np.set_printoptions(precision=3, linewidth=150, suppress=True)
plt.style.use(['seaborn-whitegrid','data/cours.mplstyle'])
~~~
~~~ python
N = 2

A = np.random.randint(-10, 10, size=(N,N))
A = A * 1.0                                            # pour passer en reels
A[np.diag_indices(N)] = 0.1 + np.abs(A).sum(axis=0)    # diag dominante
A = A + A.T                                            # symétrique
A = A / np.abs(A).sum(axis=0).mean()
b = np.random.randint(-10,10,size=(N))
print(A, "\n\n", b)
~~~
~~~
[[1.037 0.184]
 [0.184 0.596]] 

 [7 2]
~~~
~~~ python
def grad_J(x):
    return A@x - b
~~~
~~~ python
def minimum_J(start_value, µ=0.1, e = 0.001):
    x = [np.array(start_value)]
    while True:
        x.append(x[-1] - µ * grad_J(x[-1]))
        if np.square(x[-1] - x[-2]).sum() < e**2:
            break
        # la suite n'est que des tests pour se protéger
        if np.square(x[-1] - x[-2]).sum() > 1E9:  # au cas où on diverge
            print("DIVERGE")
            break
        if len(x) > 1000:  # c'est trop long, je crains la boucle infinie
            print('Trop long, boucle infinie ?')
            break
    return np.array(x)

x = minimum_J(np.zeros(N))
~~~
~~~ python
x[-1] - lin.solve(A, b)
~~~
~~~
array([-0.007,  0.016])
~~~
~~~ python
plt.plot(x[:,0], x[:,1], 'x:')
~~~
![](https://i.imgur.com/S5fK3Je.png)

## nxn
~~~ python
np.abs(A)
~~~
~~~
array([[1.037, 0.184],
       [0.184, 0.596]])
~~~
~~~ python
N = 9

A = np.random.randint(-10, 10, size=(N,N))
A = A * 1.0                                            # pour passer en reels
A[np.diag_indices(N)] = 0.1 + np.abs(A).sum(axis=0)    # diag dominante
A = A + A.T                                            # symétrique
A = A / np.abs(A).sum(axis=0).mean()
b = np.random.randint(-10,10,size=(N))
~~~
~~~ python
x = minimum_J(np.zeros(N))
~~~
~~~ python
x[-1] - lin.solve(A, b)
~~~
~~~
array([ 0.   , -0.006,  0.001,  0.006,  0.017,  0.008, -0.   ,  0.014,  0.004])
~~~
~~~ python
print("Converge en %d itérations" % len(x))
x
~~~
~~~
Converge en 178 itérations
~~~
~~~
array([[  0.   ,   0.   ,   0.   , ...,   0.   ,   0.   ,   0.   ],
       [  0.3  ,  -0.2  ,   0.   , ...,   0.8  ,  -0.6  ,  -0.4  ],
       [  0.576,  -0.396,  -0.001, ...,   1.548,  -1.176,  -0.783],
       ...,
       [  3.088,  -4.714,   0.223, ...,  13.007, -14.827,  -9.853],
       [  3.088,  -4.714,   0.223, ...,  13.007, -14.827,  -9.853],
       [  3.088,  -4.714,   0.223, ...,  13.007, -14.828,  -9.854]])
~~~
</details>

# Introduire de l'inertie

Introduire de l'inertie dans la méthode du gradient. Que constate-t-on ?

<details markdown="1">
<summary>Reponse</summary>

Ajouter de l'inertie dans une méthode itérative veut dire qu'on avance moins vite vers le point suivant : 
~~~ python
x_next = ...
x = w * x_next + (1 - w) * x
~~~
avec `w` qui représente la force d'avancée (ou l'inverse du poids de l'inertie).
Dans le cas de la méthode du gradient cela donne : 
~~~ python
x_next = x - |µ| grad_J(x)
x = w * x_next + (1 - w) * x
~~~
ce qui se développe ainsi : 
~~~ python
x = w * (x - |µ| grad_J(x)) + (1 - w) x
~~~
ou
~~~ python
x = x - w * |µ| grad_J(x)
~~~
On voit donc qu'ajouter de l'inertie ne fait que modifier le paramètre µ qui justement sert à avancer plus ou moins vite. µ est déjà une sorte d'inertie.

Donc cela ne change pas la méthode et cela n'amméliore pas l'algorithme.
</details>

# Valeur optimale de µ

On note que deux directions de pente sucessives sont orthogonales si le point suivant est le minumum dans
la direction donnée ($\nabla J ({\bf x}^k$)).

$$
\nabla J ({\bf x}^{k+1})^T \; \nabla J ({\bf x}^k) = 0
$$

## Démonstration 
On veut régler µ pour arriver au minimum de J lorsqu'on avance dans la direction $- \nabla J({\bf x}^{k})$.
Cela veut dire que la dérivée partielle de $J({\bf x}^{k+1})$ par rapport à µ doit être
égale à 0 ou bien en faisant apparaitre µ dans l'équation :

$$
\frac{\partial J ({\bf x}^k - µ \; \nabla J ({\bf x}^k))}{\partial µ} = 0
$$

En développant on a

$$
\begin{aligned}
\frac{\partial J ({\bf x}^{k+1})}{\partial {\bf x}^{k+1}} \; \frac{\partial {\bf x}^{k+1}}{\partial µ} &= 0 \\
J'({\bf x}^{k+1}) \, . \, (- \nabla J ({\bf x}^k)) &= 0 \\
(A\, {\bf x}^{k+1}  - b) \, . \, \nabla J ({\bf x}^k) &= 0 \quad \textrm{puisque A est symétrique}\\
\nabla J ({\bf x}^{k+1})  \, . \, \nabla J ({\bf x}^k) &= 0 \quad \textrm{CQFD}
\end{aligned}
$$

![](https://i.imgur.com/yxvHNX9.png)

En utilisant cette propriété, évaluer la valeur optimale de µ pour atteindre le minimum dans la direction de
$\nabla J ({\bf x}^k)$.

## Exercice
Écrire le méthode du gradient avec le calcul du µ optimal à chaque itération pour résoudre $A {\bf x} = {\bf b}$.

<details markdown="1">
<summary>Solution</summary>
On reprend l'avant-dernière ligne de la démonstration et on remplace $\bf x^{k+1}$ par $\bf x^{k} -\mu\nabla J(\bf x^k)$:

$$
\begin{aligned}
(A(\bf x^k - \mu\nabla J(\bf x^k)) -b)\cdot\nabla J(\bf x^k) &= 0\\
(A\bf x^k -b - \mu A\nabla J(\bf x^k))\cdot\nabla J(\bf x^k) &= 0\\
(A\bf x^k -b)\cdot\nabla J(\bf x^k) - \mu A\nabla J(\bf x^k)) -b\cdot\nabla J(\bf x^k) &= 0\\
\mu &= \frac{\nabla J(\bf x^k)\cdot\nabla J(\bf x^k)}{A\nabla J(\bf x^k)\cdot\nabla J(\bf x^k)}
\end{aligned}
$$

~~~ python
def minimum_J(start_value, e = 0.001):
    x = [np.array(start_value)]
    while True:
        gradJ = grad_J(x[-1])
        µ = np.dot(gradJ, gradJ) / np.dot(A @ gradJ, gradJ)
        x.append(x[-1] - µ * grad_J(x[-1]))
        if np.square(x[-1] - x[-2]).sum() < e**2:
            break
        # la suite n'est que des tests pour se protéger
        if np.square(x[-1] - x[-2]).sum() > 1E9:  # au cas où on diverge
            print("DIVERGE")
            break
        if len(x) > 1000:  # c'est trop long, je crains la boucle infinie
            print('Trop long, boucle infinie ?')
            break
    return np.array(x)
~~~
~~~ python
x = minimum_J(np.zeros(N))
x[-1] - lin.solve(A, b)
~~~
~~~
array([-0., -0.,  0., -0.,  0.,  0.,  0.,  0., -0.])
~~~
~~~ python
print("Converge en %d itérations" % len(x))
x
~~~
~~~
Converge en 14 itérations
~~~
~~~
array([[  0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ],
       [  5.295,  -3.53 ,   0.   , -15.884,  -8.824,  -1.765,  14.119, -10.589,  -7.06 ],
       [  3.488,  -5.355,  -0.197, -12.432, -13.603,  -3.608,  12.295, -13.31 ,  -8.402],
       [  3.085,  -4.72 ,   0.257, -14.479, -14.586,  -3.802,  12.956, -14.127,  -9.531],
       [  3.128,  -4.877,   0.194, -13.924, -15.279,  -4.164,  12.973, -14.572,  -9.669],
       [  3.076,  -4.743,   0.232, -14.255, -15.457,  -4.161,  13.   , -14.712,  -9.837],
       [  3.091,  -4.75 ,   0.226, -14.166, -15.569,  -4.242,  13.013, -14.786,  -9.842],
       [  3.083,  -4.72 ,   0.226, -14.224, -15.6  ,  -4.239,  13.009, -14.815,  -9.863],
       [  3.087,  -4.718,   0.225, -14.208, -15.618,  -4.257,  13.011, -14.829,  -9.859],
       [  3.086,  -4.711,   0.224, -14.22 , -15.623,  -4.256,  13.008, -14.836,  -9.861],
       [  3.087,  -4.71 ,   0.223, -14.217, -15.627,  -4.26 ,  13.009, -14.839,  -9.859],
       [  3.087,  -4.708,   0.223, -14.219, -15.627,  -4.26 ,  13.008, -14.84 ,  -9.859],
       [  3.087,  -4.708,   0.222, -14.219, -15.628,  -4.261,  13.008, -14.841,  -9.858],
       [  3.087,  -4.708,   0.222, -14.219, -15.628,  -4.261,  13.007, -14.841,  -9.858]])
~~~
</details>