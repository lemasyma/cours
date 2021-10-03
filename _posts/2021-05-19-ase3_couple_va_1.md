---
title:          "ASE3: Couple de variables aleatoires discretes et analyse des donnees - 2"
date:           2021-05-19 9:00
categories:     [tronc commun S8, ASE3]
tags:           [tronc commun, ASE3, S8, couple]
math: true
description: Couple de variables aleatoires discretes et analyse des donnees - 2
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/BJVEcNGFO)

# Rappels
<div class="alert alert-danger" role="alert" markdown="1">
$$
\rho(X,Y) = \frac{Cov(X,Y)}{\sigma_x\sigma_y}
$$
avec:
- $\sigma_X=\sqrt{V(X)}$
- $\sigma_Y=\sqrt{V(Y)}$
</div>

$$
Cov(X,Y)=\underbrace{<X-E(X),Y-E(Y)>}_{\text{produit scalaire}}\\
\sigma_X=\sqrt{V(X)}=\Vert X-E(X)\Vert\\
\rho(X,Y)=\frac{<X-E(X), Y-E(Y)>}{\Vert X-E(X)\Vert\Vert Y-E(Y)\Vert}
$$

![](https://i.imgur.com/QbssgtG.png)

$$
\cos(\theta)=\frac{<u,v>}{\Vert u\Vert\Vert v\Vert}
$$

<div class="alert alert-danger" role="alert" markdown="1">
$$
\rho(X,Y) = \cos(\theta)\\
\vert\rho\vert\le 1
$$
</div>

<div class="alert alert-info" role="alert" markdown="1">
**Proposition**

<div class="alert alert-danger" role="alert" markdown="1">
$$
V(X+Y)=V(X)+V(Y)+2Cov(X,Y)
$$
</div>
</div>

## Demonstration

$$
\begin{aligned}
V(X+Y)&=E((X+Y)^2) - (\underbrace{E(X+Y)}_{E(X) + E(Y)})^2\\
&=E(X^2+2XY+Y^2)-E^2(X)-2E(X)E(Y)-E^2(Y)\\
&= E(X^2)+2E(XY) + E(Y^2)-E^2(X)-2E(X)E(Y)-E^2(Y)\\
&=V(X) +V(Y)+2(E(XY)-E(X)E(Y))\\
&=\color{red}{V(X)+V(Y)+2Cov(X,Y)}
\end{aligned}
$$

**Remarque**: Si $X$ et $Y$ sont independantes $\Rightarrow$ $Cov(X,Y)=0\Rightarrow\color{red}{V(X+Y) = V(X)+V(Y)}$
