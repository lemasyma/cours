---
title:          "CAMA : ma40 Méthode du gradient conjugué"
date:           2020-05-24 10:00
categories:     [S6, Shannon, CAMA]
tags:           [S6, CAMA, Shannon]
description: Méthode du gradiant conjugué
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/H1W-VsW2L)
# Cours du 24 / 05

## Méthode du gradient conjugue

Si on a calculé le $\mu$ optimal alors la plus forte pente $\nabla J ({\bf x}^{k+1})$ sera orthogonale à la pente qui définie la droite sur laquelle on cherche $\mu$. On a donc
$$
\nabla J ({\bf x}^{k+1})^T \, . \, \nabla J ({\bf x}^k) = 0
$$
Le minimum suivant ${\bf x^{k+2}}$ sera le minimum de l'espace généré par $\nabla J ({\bf x}^{k+1})$ et $\nabla J ({\bf x}^k)$.
<div class="alert alert-warning" role="alert" markdown="1">
On ne sait pas si ${\bf x^{k+3}}$ sera calculé le long de la direction $\nabla J ({\bf x}^k)$.
</div>
Une recherche optimale du minimum d'une fonction convexe dans un espace $\mathbb{R}^n$ ne devrait pas prendre plus de $n$ itérations si on est capable de calculer le $\mu$ optimal dans la direction choisie.
On cherche le minimum dans les directions des vecteurs de la base de notre espace $\mathbb{R}^n$ afin de trouver le **minimum global**.

## Générer une base de $\mathbb{R}^n$
Si on veut trouver notre minimum global en $n$ itérations au maximum, il faut que nos directions ne soient pas redondantes et que les $n$ premières directions génèrent $\mathbb{R}^n$ ou en forment une base.
La nouvelle direction $d^k$ doit être orthogonale à toutes les directions précédentes et permet de trouver une base qui génère un espace de dimension $k + 1$.
### Le cas ${\bf Ax = b}$
La fonctionnelle à minimiser est :
$$
J({\bf x}) = \frac{1}{2} \, {\bf x}^T \, A \, {\bf x} - {\bf b}\, . {\bf x}
$$
* Si A est symétrique, son gradient est $\nabla J({\bf x}) = A \; {\bf x} - {\bf b}$

Si on calcule ${\bf x^k}$ comme avant on a l'orthogonnalité de 2 directions successives.

*Que se passe-t-il si ${\bf x^k+1}$ minimise $J$ dans l'espace $G_k$ généré par toutes les directions précédentes ?*
$$
J({\bf x}^{k+1}) = \min_{\bf v \in G_k} J({\bf x}^k + {\bf v})
$$
avec ${\bf G_k} = span\text{\{} {\bf d}^0, {\bf d}^1,\dots, {\bf d}^k\text{\}} =  \left\text{\{} {\bf v} = \sum_{i=0}^{k} \alpha_i \, {\bf d}^i \quad \forall \alpha_i \in ℝ \right\text{\}}$.
<div class="alert alert-danger" role="alert" markdown="1">
Toutes les dérivées partielles par rapport aux vecteurs de ${\bf G_k}$ sont nulles :
$$
\nabla J({\bf x}^{k+1}) \, . \, {\bf w} = 0 \quad \forall {\bf w} \in {\bf G_k}
$$
</div>
<div class="alert alert-success" role="alert">
Cela se vérifie si ${\bf w}$ est un des vecteurs de la base:
$$ 
\nabla J({\bf x}^{k+1}) \, . \, {\bf e}_i = \begin{bmatrix}
\partial J / \partial x_{1} \\
\partial J / \partial x_{2} \\
\vdots \\
\partial J / \partial x_{i} \\
\vdots \\
\partial J / \partial x_{n} \\
\end{bmatrix}
\, . \,
\begin{bmatrix}
0 \\
0 \\
\vdots \\
1 \\
\vdots \\
0 \\
\end{bmatrix} =
\frac{\partial J}{\partial x_i}({\bf x}^{k+1}) 
$$
</div>
<div class="alert alert-warning" role="alert" markdown="1">
La dérivée partielle de $J$ dans une direction ${\bf w}$ de ${\bf G_k}$ est nulle revient a dire  $\nabla J({\bf x}^{k+1})$ est orthogonal à ${\bf w}$.
</div>
#### Générer les directions  ${\bf d}^i$
La formule itérative devient :
$$
{\bf x}^{k+1} =  {\bf x}^k - µ^k\, {\bf d}^k
$$
* Pour calculer les ${\bf d}^k$ on utilise la formule des dérivées partielles de $J$ par rapport à un vecteur ${\bf w \in G_k}$ où elles sont nulles.
* ${\bf d}^i$ génèrent l'espace ${\bf G_k}$, il suffit que les dérivées partielles de $J$ par rapport ${\bf d}^i$ soient nulles
$$
\nabla J({\bf x}^{k+1}) \, . \, {\bf d}^i = 0 \quad \forall i \le k \qquad (1) \\
$$
<div class="alert alert-danger" role="alert" markdown="1">
En déroulant les calculs on obtient : 
$$
\begin{align}
\nabla J({\bf x}^{k}) \, . \, {\bf d}^i - µ^k \, A \, {\bf d}^k \, . \, {\bf d}^i &= 0 \quad \forall i \le k \\
\end{align}
$$
</div>
* Si $i \lt k$, le premier terme est nul : $$ A \, {\bf d}^k \, . \, {\bf d}^i = 0 \quad \forall i < k \qquad (2)$$
    * On a les conditions pour construire la nouvelle direction ${\bf d}^k$ $${\bf d}^k = \nabla J({\bf x}^k) 
            - \sum_{i=0}^{k-1} \frac{A\, \nabla J({\bf x}^k) \, . \, {\bf d}^i}
                                    {A\, {\bf d}^i \, . \, {\bf d}^i} \; {\bf d}^i $$
* Si $i =k$, on obtient la valeur nécessaire $µ^k$ pour garantir que $\nabla J({\bf x}^{k+1}) \, . \, {\bf d}^k = 0$ : $$
µ^k = \frac{\nabla J({\bf x}^{k}) \, . \, {\bf d}^k}
         {A \, {\bf d}^k \, . \, {\bf d}^k}
 = \frac{(A \, {\bf x}^{k} - b) \, . \, {\bf d}^k}
         {A \, {\bf d}^k \, . \, {\bf d}^k} \\
\,         
$$
## Propriété
L'ensemble des gradients de $J$ aux points $\bf{x}^i$ forment une base de l'espace ${\bf G_k}$ : 
$$
\nabla J({\bf x}^{k+1}) \perp \nabla J({\bf x}^i) \quad \forall i \le k
$$