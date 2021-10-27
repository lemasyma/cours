---
title:          "PRSTA: Seance 4"
date:           2021-10-27 17:00
categories:     [Image S9, PRSTA]
tags:           [Image, S9, PRSTA]
math: true
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/SyWXFkDLY)

# Rappel

<div class="alert alert-info" role="alert" markdown="1">
**Proposition**

Sous des hypotheses techniques, en notant $\hat\theta_n$ l'estimateur du maximum de vraisemblance.

$\sqrt{n!(\theta_0)}(\hat\theta_n-\theta_0)$ converge en loi vers $\mathcal N(0,1)$

Nous disons que l'estimateur du maximum de vraisemblance est normal asymptotiquement efficace ou NAE (Best asymptotically normal ou BAN)

</div>

Nous supposerons que les hypotheses techniques evoquees sont verifiees

<div class="alert alert-info" role="alert" markdown="1">
**Theoreme de Wilks**

Sous l'hypothese $(H_0)$, $R_n:=2\log T_n$ converge en loi ver une loi $\chi^2(1)$

</div>

# Cas particulier

- $H_0:\theta=\theta_0$
- $H_1:\theta\neq \theta_1$

Notons $\hat\theta$ l'EMV

<div class="alert alert-info" role="alert" markdown="1">
**Definition**

La statistique de Wald est:

$$
W_n=\frac{(\hat \theta_n-\theta_0)^2}{V(\hat\theta_n)}
$$

</div>

<div class="alert alert-info" role="alert" markdown="1">
**Theoreme**

Sous $H_0$, $W_n$ converge en loi vers un $\chi^2(1)$

</div>

# Exemple
## Premier exemple

- $X\sim\mathcal N(m,1)$
- $H_0:m=0$ contre $H_1:m\neq 0$

$$
V(\bar X_n)=V(\frac{1}{n}\sum_{i=1}^n X_i)=\frac{1}{n^2}(\sum_{i=1}^nX_i)\\
\boxed{V(\bar X_n)=\frac{1}{n^2}\times n=\frac{1}{n}}
$$

## Second exemple

- $H_0$: "le patient est sain"
- $H_1$: "le patient est malade"

<div class="alert alert-info" role="alert" markdown="1">
- $\alpha$: probabilite de rejeter $(H_0)$ alors qu'elle est vraie i.e. *probabilite de fausse alarme*
- $\beta$: probabiliter de rejeter $(H_1)$ alors qu'elle est vraie i.e., *probabilite de non detection*
- Ainsi, la puissance $\pi:=1-\beta$ est la *probabilite de detection* 
</div>


# Caracteristiques Operationnelles du Recepteur

- Elles permettent d'analyser les performances d'un test
- Expression de la puissance comme une fonction de $\alpha$
- $\beta=f(\alpha)$