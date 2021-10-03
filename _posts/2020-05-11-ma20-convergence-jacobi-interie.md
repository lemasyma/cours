---
title:          "CAMA : ma20 Convergence de Jacobi avec inertie"
date:           2020-05-11 10:00
categories:     [S6, Shannon, CAMA]
tags:           [S6, CAMA, Shannon]
math: true
description: Convergence de Jacobi avec inertie
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/rygt1_MT8)
# Cours du 11 / 05

## Ajouter de l'inertie à Jacobi
<div class="alert alert-info" role="alert" markdown="1">
La méthode de Jacobi mène au système itératif :
$$
{\bf x}^{k+1} = M^{-1} \, ( N\; {\bf x}^k + {\bf b})
$$
</div>
Cette méthode converge ssi la matrice $b$ a un rayon spectral inférieur à 1 (cf ma12).
<div class="alert alert-danger" role="alert" markdown="1">
On peut agrandir le rayon de convergence en ajoutant de **l'inertie**:
$$
{\bf x}^{k+1} =  w \, M^{-1} \, (N\; {\bf x}^k + {\bf b}) + (1-w) \, {\bf x}^k
$$
* $0 < w \le 1$.
</div>
* si $w = 1$ : Jacobi classique
* si $w = 0$ : on néglige les termes en dehors de la diagonale et $b$ donc ça ne marche pas

<div class="alert alert-warning" role="alert" markdown="1">
On parle d'inertie car on avance "moins vite": la nouvelle valeur de ${\bf x}^{k+1}$ est comprise entre l'ancienne  valeur de ${\bf x}^{k+1}$ et ${\bf x}^k$. C'est la **surrelaxation**
</div>
### Programmons l'inertie pour Jacobi
On commence pour un Jacobi qui diverge.
``` python
np.random.seed(799)

A = np.random.randint(10, size=(4,4))
b = A.sum(axis=1) # la solution est [1,1,1,1]
```
```
A:
 [[5 7 6 0]
 [1 7 2 5]
 [5 6 5 1]
 [0 6 3 7]] 
b:
 [18 15 17 16] 
```
``` python
M = np.diag(A)        # vecteur
N = np.diag(M) - A    # np.diag d'une matrice donne un vecteur, np.diag d'un vecteur donne une matrice
```
```

M:
 [[5 0 0 0]
 [0 7 0 0]
 [0 0 5 0]
 [0 0 0 7]]
N:
 [[ 0 -7 -6  0]
 [-1  0 -2 -5]
 [-5 -6  0 -1]
 [ 0 -6 -3  0]]
```
``` python
x0 = np.random.random(4)
x = x0
for i in range(20):
    x = (N @ x + b) / M
```
```
...
x_16 = [-4448.651 -1888.411 -4149.91  -1981.882]
x_17 = [7627.267 3238.983 7114.521 3399.456]
x_18 = [-13068.402  -5548.37  -12190.539  -5823.066]
x_19 = [22399.965  9511.401 20894.459  9982.548]
```
<div class="alert alert-warning" role="alert" markdown="1">
Ajoutons de l'inertie :
</div>
``` python
x = x0  # on reprend la même valeur initiale pour la comparaison
w = 0.5 # on choisit w 
for i in range(20):
    x = w * (N @ x + b) / M + (1-w) * x
```
```
...
x_17 = [1.059 0.977 0.972 1.03 ]
x_18 = [1.063 0.977 0.968 1.031]
x_19 = [1.067 0.978 0.963 1.032]
```
<div class="alert alert-success" role="alert">
La solution est [1,1,1,1], l'inertie fonctionne.
</div>
### Étudions la convergence
On trace une courbe de:
* l'erreur absolue (lorsqu'on connait la solution)
* de l'erreur relative (entre 2 ${\bf x}^i$ successifs) 
* du résidu ($||A \, {\bf x}^i - {\bf b}||$).
``` python
x = x0    # on reprend la même valeur initiale pour la comparaison
w = 0.5   # on choisit w 
error = [np.square(x - np.ones(4)).sum()]
for i in range(20):
    x = w * (N @ x + b) / M + (1-w) * x
    error.append(np.square(x - np.ones(4)).sum())
```
![](https://i.imgur.com/tbOjvyX.png)
A l'échelle logarithmique:
![](https://i.imgur.com/WM0W8Xv.png)
<div class="alert alert-warning" role="alert" markdown="1">
Il faut toujours regarder une erreur en échelle logarithmique.
</div>
En faisant le calcul sur 200 itérations : 
![](https://i.imgur.com/3dUrGA5.png)
<div class="alert alert-success" role="alert">
On s'est rapproché de la solution puis on a divergé.
</div>
#### Erreur relative
Regardons l'écart entre 2 ${\bf x}^k$ successifs.
``` python
x = x0 # on reprend la même valeur initiale pour la comparaison
w = 0.5 # on choisit w 
error2 = []
for i in range(200):
    old_x = x
    x = w * (N @ x + b) / M + (1-w) * x
    error2.append(np.square(x - old_x).sum())
```
![](https://i.imgur.com/q2oLsLi.png)
<div class="alert alert-warning" role="alert" markdown="1">
Il y a une relation entre l'écart de deux valeurs successives et l'erreur absolue.
</div>
<div class="alert alert-success" role="alert">
L'écart entre 2 ${\bf x}$ successifs est une facon de savoir quand arrêter un algorithme itératif.
</div>

#### Résidu
``` python
x = x0 # on reprend la même valeur initiale pour la comparaison
w = 0.5 # on choisit w 
residu = []
for i in range(200):
    old_x = x
    x = w * (N @ x + b) / M + (1-w) * x
    residu.append(np.square(A @ x - b).sum())
```
![](https://i.imgur.com/0mk3Iru.png)

## Normaliser
* Si la solution est un milliard, avoir une erreur de 0.1 est très bien.
* Si la solution est 0.01, avoir une erreur de 0.1 est énorme.
<div class="alert alert-info" role="alert" markdown="1">
On ne peut juger une erreur qu'avec une référence. Si on connait la solution exacte : 
$$
\frac{||{\bf x}^k - {\bf x}||}{||{\bf x}||}
$$
</div>
De même, l'erreur entre 2 itérations successives doit être normalisée : 
$$
\frac{||{\bf x}^{k+1} - {\bf x}^k||}{||{\bf x}^k||}
$$
``` python
def mk_A(seed):
    np.random.seed(seed)
    return np.random.randint(10, size=(4,4))
```
``` python
def plot_error(M, N, b, x0, w, n=200):
    x = x0 
    error = [np.square(x - np.ones(4)).sum()]
    error2 = []
    for i in range(n):
        old_x = x
        x = w * (N @ x + b) / M + (1-w) * x
        error.append(np.square(x - np.ones(4)).sum())
        error2.append(np.square(x - old_x).sum())
```
``` python
def plot_error_normalized(M, N, b, x0, w, n=200):
    x = x0 
    error = [np.square(x - np.ones(4)).sum()]
    error2 = []
    for i in range(n):
        old_x = x
        x = w * (N @ x + b) / M + (1-w) * x
        error.append((np.square(x - np.ones(4)).sum())/4) # normalisé par rapport à la solution
        error2.append((np.square(x - old_x).sum())/np.square(x).sum()) # normalisé par rapport à x
```
``` python
A = mk_A(799)
b = A.sum(axis=1)                    

M = np.diag(A)    
N = np.diag(M) - A 

x0 = np.random.random(4)
```
``` python
plot_error(M, N, b, x0, w=0.1, n=1000) 
```
![](https://i.imgur.com/TmAEH6F.png)
``` python
plot_error_normalized(M, N, b, x0, w=0.1, n=1000) 
```
![](https://i.imgur.com/2MTkNOH.png)
<div class="alert alert-success" role="alert">
L'erreur relative normalisée se stabilise.
</div>