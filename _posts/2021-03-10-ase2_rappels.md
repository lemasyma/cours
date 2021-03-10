---
title:          "ASE2: Rappels sur les lois"
date:           2021-03-10 9:00
categories:     [tronc commun S8, ASE2]
tags:           [tronc commun, ASE2, S8]
description: Rappels sur les lois
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/SJ7bOb8mO)

# ASE2 - Rappels

# Loi normale centree reduite
- $E(X) = 0$
- $V(X) = 1$
- $f(X) = \frac{1}{\sqrt{2\pi}}e^{-\frac{t^2}{2}}$
- $F(X) = \frac{1}{\sqrt{2\pi}}\int_0^Xe^{-\frac{t^2}{2}}$

# Loi Poisson
- $P(X_n=k) = e^{-\lambda}\frac{\lambda^k}{k!}$ (avec $\lambda = \frac{1}{n}$)

$$
P(X_n=k) = e^{-\lambda}\frac{\lambda^k}{k!} \text{ (avec } \lambda = \frac{1}{n}\text{)}\\
P(X_n = k)= e^{-\frac{1}{n}}\frac{1}{n^kk!}, \forall k\in\mathbb N
$$

- Si $k=0$, $P(X_n = 0) = e^{-\frac{1}{n}}\to_{n\to+\infty}0$
- Si $k\ge1$, $P(X_n=k)=\frac{1}{n^kk!}e^{-\frac{1}{n}}\to_{n\to+\infty}0$ car $\frac{1}{n^k}\to_{n\to+\infty}0$

# Loi exponentielle
- $E(X) = \frac{1}{\lambda}$
- $V(X) = \frac{1}{\lambda^2}$
- Densité de probabilité:


$$
\begin{cases}
    f(t)=0 &\text{si }t \lt 0\\
    f(t)=\frac{1}{E(X)}e^{-\frac{t}{E(X)}} &\forall t\ge0
\end{cases}\\
\Leftrightarrow 
\begin{cases}
    f(t)=\lambda e^{-\lambda t} &\text{si } t\ge0\\
    f(t)=0 &\text{si }t \lt 0\\
\end{cases}
$$

- Fonction de répartition:

$$
\begin{cases}
    F(t)=1 - e^{-\lambda t} &\text{si } t\ge0\\
    F(t)=0 &\text{si }t \lt 0\\
\end{cases}
$$

# Loi geometrique
- $E(X)=\frac{1}{p}$
- $V(X) = \frac{1-p}{p^2}$

$(X_n), n\gt0$ une suite de v.a. geometrique $G(\frac{1}{n})$ avec $p=\frac{1}{n}$ parametre.
$$
\begin{align}
P(X_n = k) &= (1-p)^{k-1}p, \forall k\ge1\\
&= (1-\frac{1}{n})^{k-1}\frac{1}{n}
\end{align}
$$