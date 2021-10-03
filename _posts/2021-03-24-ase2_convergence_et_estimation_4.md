---
title:          "ASE2: Convergence et estimation - 4"
date:           2021-03-24 9:00
categories:     [tronc commun S8, ASE2]
tags:           [tronc commun, ASE2, S8, loi, binomial, poisson, normale]
math: true
description: Convergence et estimation - 4
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/H1rOQcdEu)

# Estimateur

## Exemple

On considère un échantillon $(X_1, X_2,...,X_n)$ d'une variable de Poisson de parametre $\theta$ (inconnu)

La vraisemblance de cet echantillon est:

$$
L(x_1,x_2,...,x_n,\theta)=\Pi_{i=1}^nP(X_i=x_i)\\
L(x_1,x_2,...,x_n,\theta)=\Pi_{i=1}^ne^{-\theta}\frac{\theta^{x_i}}{x_i!}=\frac{e^{-n\theta}\theta^{\sum_{i=1}^nx_i}}{\Pi_{i=1}^nx_i!}
$$

<div class="alert alert-info" role="alert" markdown="1">
**Definition**: On appelle quantité d’information de Fisher $I_n(\theta)$ apportée par un échantillon sur le paramètre $\theta$ la quantité positive:

$$
I_n(\theta)=E((\frac{\delta \ln L}{\delta\theta})^2)
$$

</div>


## Proposition
<div class="alert alert-info" role="alert" markdown="1">
$$
I_n(\theta)=-E(\frac{\delta^2\ln L(x,\theta)}{\delta\theta^2})
$$
</div>

### Demonstration
1. $L$ etant une densite: $\int_{\mathbb R^n}L(x,\theta)dx=1$
2. En dérivant par rapport à $\theta$: $\int_{\mathbb R^n}\frac{\delta L(x,\theta)}{\delta\theta}dx=0\quad (1)$
3. En remarquant que $\frac{\delta\ln L(x,\theta)}{\delta\theta}=\frac{\frac{\delta L}{\delta\theta}(x,\theta)}{L(x,\theta)}$
4. $(1)$ donne $\int_{\mathbb R^n}\frac{\delta \ln L(x,\theta)}{\delta\theta}L(x,\theta)dx=0$

Ce qui prouve que la variable aléatoire $\frac{\delta \ln L(x,\theta)}{\delta\theta}$ est centrée et que $I_n(\theta)=V(\frac{\delta\ln L}{\delta \theta})$

Dérivons une deuxième fois par rapport à $\theta$:

$$
\int_{\mathbb R^n}\frac{\delta^2 \ln L(x,\theta)}{\delta\theta^2}L(x,\theta)dx+\int_{\mathbb R^n}\frac{\delta \ln L(x,\theta)}{\delta\theta}\frac{L(x,\theta)}{\delta\theta}dx=0\\
\int_{\mathbb R^n}\frac{\delta^2 \ln L(x,\theta)}{\delta\theta^2}L(x,\theta)dx+\int_{\mathbb R^n}(\frac{\delta \ln L(x,\theta)}{\delta\theta})^2L(x,\theta)dx=0
$$

Donc:

<div class="alert alert-success" role="alert" markdown="1">
$$
\begin{aligned}
I_n(\theta)&=E((\frac{\delta \ln L}{\delta\theta})^2)\\
&=\int_{\mathbb R^n}(\frac{\delta \ln L(x,\theta)}{\delta\theta})^2L(x,\theta)dx\\
&=-\int_{\mathbb R^n}\frac{\delta^2 \ln L(x,\theta)}{\delta\theta^2}L(x,\theta)dx\\
&=-E(\frac{\delta^2\ln L(x,\theta)}{\delta\theta^2})
\end{aligned}
$$
</div>

# Inégalité de FRECHET-DARMOIS-CRAMER-RAO(FDCR) 

<div class="alert alert-danger" role="alert" markdown="1">
On a pour tout estimateur T sans biais de $\theta$:

$$
V(T)\ge\frac{1}{I_n(\theta)}
$$

L’estimateur T sera qualifié d’efficace si la borne inférieure est atteinte, c’est-à-dire 

$$
V(T)=\frac{1}{I_n(\theta)}
$$

</div>

# Méthode du maximum de vraisemblance

<div class="alert alert-info" role="alert" markdown="1">
Cette méthode consiste, étant donnée un échantillon de valeurs $x_1,x_2,...,x_n$ à prendre comme estimation de $\theta$ la valeur de $\theta$ qui rend maximale la vraisemblance $L(x_1,x_2,...,x_n,\theta)$

On prend comme estimation de $\theta$ la solution de l’équation de la vraisemblance 

$$
\frac{\delta \ln L}{\delta\theta} = 0
$$

</div>