---
title:          "ASE3: Analyse en composantes principales"
date:           2021-06-02 10:00
categories:     [tronc commun S8, ASE3]
tags:           [tronc commun, ASE3, S8, couple, loi conjointe, loi marginale]
description:    Analyse en composantes principales
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/BktQ8p4cu)

# Tableau des donnees

Les observations de $p$ variables sur $n$ individus sont regroupes en une matrice $X$ a $n$ ligned et $p$ colonnes

$$
X=\begin{matrix}te_1 \\ \vdots \\ te_i \\ \vdots \\te_n\end{matrix}\begin{pmatrix}
X^{(1)} &\dots &X^{(j)} &\dots &X^{(p)}\\
\vdots&\vdots&\vdots&\vdots&\vdots\\
\dots&\dots &\color{red}{X_i^{(j)}} &\dots &\dots\\
\vdots&\vdots&\vdots&\vdots&\vdots\\
\dots&\dots&\dots&\dots&\dots
\end{pmatrix}\\
te_i=(X_i^{(1)},X_i^{(2)},\dots,X_i^{(j)},\dots,X_i^{(p)})\\
e_i=\begin{pmatrix}X_i^{(1)} \\ \vdots \\ X_i^{(j)} \\ \vdots \\ X_i^{(p)}\end{pmatrix}
$$

$$X_i^{(j)}$$ est la valeur prise par la variable $X$ sur le ieme individu.

# Matrice des poids

On associe a chaque indvidu un poids $P_i\ge0$ (probabilite de choisir l'individu)

$$
\sum_{i=1}^nP_i=1, D=
\begin{pmatrix}
    P_1 &0&\dots&0 \\ 
    0 &P_2&\dots&0 \\ 
    \vdots &\vdots &\ddots&\vdots\\
    0 &0 &\dots &P_n
    \end{pmatrix}
$$

Si $P_i=\frac{1}{n}\Rightarrow D=\frac{1}{n}I_n$ ou $I_n$ matrice identite $$\begin{pmatrix} 1&0&\dots &0 \\ 0&1&\dots&0 \\ \vdots&\vdots&\ddots &\vdots \\ 0 & 0&\dots&1 \end{pmatrix}$$ $\forall i=1,\dots,n$

# Centre de gravite
La vecteur $g$ des moyennes arithmetiques de chaque variable $X^{(j)}$ est definie par $g=(\bar X^{(1)},\bar X^{(2)},\dots,\bar X^{(p)})$

$$
\bar X^{(j)}=\sum_{i=j}^nP_iX_i^{(j)}\quad\text{moyenne de } X^{(j)}
$$