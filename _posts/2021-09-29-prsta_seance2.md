---
title:          "PRSTA: Seance 2"
date:           2021-09-29 14:30
categories:     [Image S9, PRSTA]
tags:           [Image, S9, PRSTA]
math: true
description: Seance 2
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/BySfn0W4t)

<div class="alert alert-info" role="alert" markdown="1">
**Regle d'echantillon**
A partir de nos observations, on decide si on rejette l'hypothese nulle ou non
</div>

Retour de la taille des epiteens: on rejette cette hypothese s'il y a un eleve qui fait plus de $1m70$.

<div class="alert alert-info" role="alert" markdown="1">
**Risque de premiere espece**
$H_0$ soit vrai
</div>

<div class="alert alert-info" role="alert" markdown="1">
**Risque de second espece**
$H_1$ soit vrai alors qu'on garde $H_0$
</div>

# Types de test

- test parametriqueon-parametrique
- test d'adequation
- test de comparaison

<div class="alert alert-info" role="alert" markdown="1">
Si l'hypothese nulle n'est pas rejetee:
- Elle n'est pas demontree pour autant
- Elle n'est pas contredite par les faits
</div>

## Test de comparaison d'une proportion

- Meme principe pour $n$ grand

$$
\sqrt{n}\frac{\hat p-p_0}{\sqrt{p_0(1-p_0)}}
$$

## Test du rapport de vraisemblance

- $H_0:\theta=\theta_0$ contre $H_1:\theta=\theta_1$
- $\theta_0\lt\theta_1$

Test de vraissemblance qui est le plus puissant

$$
T=\frac{L(X_1,...,X_n, \theta_1)}{L(X_1,...,X_n, \theta_0)}
$$

<div class="alert alert-success" role="alert" markdown="1">
Rejet de $(H_0)$ ssi $T\gt S_{\alpha}$, ou $S_{\alpha}$ est un seuil qui depend du niveau de confiance $\alpha$
</div>

## Example

- $X_i$ Poisson de parametre $\lambda$
- $H_0:\lambda=\lambda_0$ contre $H_1:\lambda=\lambda_1$
- $\lambda_0\le\lambda_1$ 

Rejet de $H_0$ si

$$
\frac{\Pi_{i=1}^ne^{-\lambda_1}\frac{\lambda_1^{X_i}}{X_i!}}{\Pi_{i=1}^ne^{-\lambda_0}\frac{\lambda_0^{X_i}}{X_i!}}\gt S_{\alpha}\\
-n(\lambda_1-\lambda_0)+\sum_{i=1}^nX_i(\log(\lambda_1)-\log(\lambda_2))\gt\log S_{\alpha}\\
\sum_{i=1}^nX_i(\log(\lambda_1)-\log(\lambda_0))\gt \log(S_{\alpha})+n(\lambda_1-\lambda_0)\\
\sum_{i=1}^nX_i\gt\underbrace{\frac{\log(S_{\alpha})+n(\lambda_1-\lambda_0)}{(\log(\lambda_1)-\log(\lambda_0))}}_{\color{blue}{n\alpha}}
$$

Rejet de $H_0$ si $\sum_{i=1}^n{x_i} > \nu_{\alpha}$

### Exemple:

- $n=2$, $\lambda_1=1$, $\lambda_2=2$, $\alpha=0,05$
- Sous $H_0$, $Y=X_1+X_2$ suit une loi $\mathcal P(2)$
- Si $\mu_{\alpha}\in]0;1]$, $\mathbb P(X_1+X_2\gt\mu_{\alpha})=1-\mathbb P(Y=0)\simeq 0.865$

### Suite de l'exemple precedent

<div class="alert alert-info" role="alert" markdown="1">
Rappel : 
- **fonction caractérique** (SAVOIR FAIRE) d'une loi X est $\phi(t) = E(e^{itX})$ 
- Pour une loi de Poisson, $P(X=k) = \frac{\lambda^k}{k!}e^{-\lambda}$
</div>

$$
\begin{aligned}
\phi_x(t)&=\sum_{k\ge0}e^{itk}P(X=k)\\
&= \sum_{k\ge 0}e^{itk}e^{-\lambda}\frac{\lambda^k}{k!}\\
&= e^{-\lambda}\sum_{k\ge 0}\frac{(\lambda e^{it})^k}{k!}  \text{ : serie}\\
&=e^{-\lambda}e^{\lambda e^{it}}
\end{aligned}\\
\color{red}{\boxed{\phi_x(t)=e^{\lambda (e^{it}-1)}}}
$$

*Loi de $X_1+X_2$ ?*

$$
\phi_{X_1+X_2}=\phi_{X_1}(t)\phi_{X_2}(t)
$$

car $X_1$ et $X_2$ sont independantes
Or $X_1$ et $X_2$ même loi donc même fonction caractérique, donc:
$$
\begin{aligned}
\phi_{X_1+X_2}&=\phi_{X_1}(t)^2\\
&=e^{(e^{it}-1)^2}\\
&= e^{2(e^{it}-1)}
\end{aligned}
$$

- Continuer jusqu'a la premiere valeur inferieure a $0.05$
- Si $\mu_{\alpha}\in]3;4]$, $\mathbb P(X_1+X_2\gt\mu_{\alpha})=1-\mathbb P(Y\le 3)\simeq 0.0527$ donc $\alpha=0.0527$
- Si $\mu_{\alpha}\in]4;5]$, $\mathbb P(X_1+X_2\gt\mu_{\alpha})=1-\mathbb P(Y\le 3)\simeq 0.0166$ donc $\alpha=0.0166$
- Test le plus puissant de risque $\alpha \le 0.05$: rejet de $H_0$ si $x_1 + x_2 > 5$

## Exemple

1. $H_0:m=m_0$ contre $H_1:m=m_1$ ou $X$ suit une loi $\mathcal N(m,1)$ et $m_0\le m_1$
2. A. N.: $m_0=1$ et $m_1=2$
3. Calculer $\alpha$
4. Calculer $\beta$

**A RENDRE 1er et 2eme EXO DE REFLEXION (moodle)**