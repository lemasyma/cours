---
title:          "PRST: Seance 4 - Intervalle de confiance"
date:           2021-03-22 10:00
categories:     [Image S8, PRST]
tags:           [Image, SCIA, PRST, S8,  loi, Student, Khi-deux, intervalle, confiance]
description: Seance 4 - Intervalle de confiance
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/BJLY0RrEu)

<div class="alert alert-info" role="alert" markdown="1">
Il y a 2 types d'estimation:
1. estimation ponctuelle (les estimateurs)
2. estimation par intervalle
</div>

Deux resultats probabilistes:
- loi forte des grand nombre
- theoreme central limite

# Intervalle de confiance pour la moyenne $m$
## Point de depart
- $(X_1,..., X_n)$ echantillon i.i.d de taille $n$
- $(x_1,...,x_n)$ réalisations de cet échantillon
- $\bar x_n = \frac{1}{n}\sum_{i=1}^nx_i$ estimation ponctuelle de la moyenne (espérance) $m$
- $S_n^2=\frac{1}{1-n}\sum_{i=1}^n(X_i\bar X_n)$ estimation ponctuelle de la variance $\sigma^2$

<div class="alert alert-info" role="alert" markdown="1">
Dans la majorite des cas, on ne connait pas la loi de probabilite d'un experience aleatoire
</div>

Dans le modele de Bernoulli avec un echantillon i.i.d de la $\mathcal B$, un intervalle de confiance au niveau $0,95$ est:
$$
[f-\frac{1}{\sqrt{n}};f+\frac{1}{\sqrt{n}}]
$$

C'est un encadrement de la valeur reelle de $p$

<div class="alert alert-danger" role="alert" markdown="1">
**Theroeme**
La proportion $p$ appartient a cet intervalle, pour $95\%$ des echantillons, sous les conditions:
- $n\ge30$
- $nf\ge5$
- $n(1-f)\ge5$
</div>

Deux cas:
1. $n$ quelconque: v.a. normales
2. $n$ grand et utilisation du TCL

## Theoreme central limite
Soit $(X_i)$ une suite de v.a. i.i.d telle que $E(X_1^2)\le+\infty$. Noton $m:=E(X_i)$ et $\theta^2=V(X_i)$

$$
\frac{\sqrt{n}(\bar X_n-m)}{\theta}
$$

converge en loi vers une loi normale centrée réduite

## Loi normale centree reduite
1. $\mathcal P(X\le0)=P(X\ge0)=0,5$
2. $\mathcal P(X\le a)=\mathcal P(X\ge a)$
3. $\mathcal P(-1,96\le X\le1,96)\simeq 0,95$ et $\mathcal P(-2,58\le X\le2,58)\simeq 0,99$

$$
m\in\biggr[\bar X_n-1,96\frac{\sigma}{\sqrt n};\bar X_n+1,96\frac{\sigma}{\sqrt n}\biggr]
$$

au niveau de confiance $0,95$

## Cas gaussien

$X_1$ suit une loi normal, $\forall n\ge 1$, $\frac{\sqrt n(\bar X_n-m)}{\sigma}$ suit une loi normale centree reduite et 

$$
\mathbb P(-1,96\le \frac{\sqrt n(\bar X_n-m)}{\sigma}\le1,96)\simeq 0,95
$$

## Cas general

$$
m\in\biggr[\bar X_n-1,96\frac{\sigma}{\sqrt n};\bar X_n+1,96\frac{\sigma}{\sqrt n}\biggr]
$$

au niveau de confiance $0,95$

<div class="alert alert-info" role="alert" markdown="1">
La forme generale de l'intervalle de confiance *asymptotique* general pour $1-\alpha$ pour la moyenne $m$ est : 

$$
\biggr[\bar X_n-z_{1-\frac{\alpha}{2}}\frac{\sigma}{\sqrt n};\bar X_n+z_{1-\frac{\alpha}{2}}\frac{\sigma}{\sqrt n}\biggr]
$$
Avec:
- $z_{1-\frac{\alpha}{2}}$: fractile d'ordre $1-\frac{\alpha}{2}$ de la loi $\mathcal N(0,1)$

</div>

### Cas particulier du modele de Bernoulli
- Intervalle de confiance pour la proportion d'un echantillon dans une population donnee
- variance inconnue
- approximation pour la loi normale possible grace au theoreme suivant:

<div class="alert alert-danger" role="alert" markdown="1">
**Theoreme de Moivre-Laplace**
$X_n$ v.a $\sim\mathcal B(n,p)$. Soit $q:=1-p$

$$
\forall x\in\mathbb R\\
\lim_{n\to+\infty}\mathbb P(\frac{X-n-np}{\sqrt{npq}}\le x)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^xe^{-\frac{t^2}{2}}dt=F(X)
$$

</div>

## Intervalle de confiance de la proportion $p$

<div class="alert alert-info" role="alert" markdown="1">
L'*intervalle de confiance asymptotique* au niveau $1-\alpha$ pour la proportion $p$ est:

$$
\biggr[\hat p - z_{1-\frac{\alpha}{2}}\frac{\sqrt{\hat p(1-\hat p)}}{\sqrt n}\biggr]
$$

</div>

## Loi du Khi-deux
$(X_1,...,X_n)$ $n$ v.a. independantes normales centrees reduite.

<div class="alert alert-warning" role="alert" markdown="1">
La v.a. $U_n:=\sum_{i=1}^nx_i^2$ suit une loi du Khi-deix a $n$ degres de liberte notee $\mathcal X^2(n)$
</div>

1. $f_{U_n}=\frac{1}{2^{\frac{n}{2}}}e^{-\frac{x}{2}}x^{\frac{x}{2} - 1}$ pour $x\ge 0$
2. $E(U_n) = n$
3. $V(U_n) = 2n$
4. $\phi_{U_n}(t)=\frac{1}{(1-2it)^{\frac{n}{2}}}$

<div class="alert alert-danger" role="alert" markdown="1">
**Theoreme**
$X$ et $Y$ deux v.a. independantes suivant respectivement $\mathcal X^2(m)$ et $\mathcal X^2(n)$ alors la v.a $X+Y$ suit une loi $\mathcal X^2(m+n)$
</div>

## Loi de Student

$X$ et $Y$ deux v.a aleatoires independantes suivant les lois $\mathcal N(0,1)$ et $\mathcal X^2(n)$.

$$
T_n=\frac{X}{\sqrt{\frac{Y}{n}}}
$$

suit une loi de Student $\mathcal T_n$ a $n$ degre de liberte

### Propriete
- $E(T_n) = 0$ (**symetrie**)
- $V(T_n)=\frac{n}{n-2}$ pour $n\gt2$

<div class="alert alert-danger" role="alert" markdown="1">
**Theoreme**
$T_n$ converge en loi vers $\mathcal N(0,1)$ lorsque $n$ tend vers $+\infty$.
</div>

### Cas gaussien
- $X_1$ suit une loi normale
- $Tn:=\frac{\sqrt n(\bar X_n-m)}{\sqrt{S_n^2}}$ suit une loi de Student a $n-1$ degrés de liberté.

<div class="alert alert-warning" role="alert" markdown="1">
L'intervall de confiance au niveau $1-\alpha$ pour la moyenne $m$ est:

$$
\biggr[\bar X_n-t_{1-\frac{\alpha}{2}}\frac{\sqrt{S_n^2}}{\sqrt n};\bar X_n+t_{1-\frac{\alpha}{2}}\frac{\sqrt{S_n^2}}{\sqrt n}\biggr]
$$

Avec:
- $t_{1-\frac{\alpha}{2}}$ fractile d'ordre $1-\frac{\alpha}{2}$ de la loi de Student $n-1$ degrés de liberté.
</div>