---
title:          "PRSTA: Seance 1"
date:           2021-09-22 14:30
categories:     [Image S9, PRSTA]
tags:           [Image, S9, PRSTA]
math: true
description: Seance 1
---

- Point de depart: hypothese formulee sur la population totale
- Jugement sur echantillon
- Tests d'hypothese

<div class="alert alert-info" role="alert" markdown="1">
2 hypotheses:
- hypothese nulle notee $H_0$
- Situation de reference
- Hypothese soumise au test
- hypothese alternative notee $H_1$
</div>

<div class="alert alert-success" role="alert" markdown="1">
Objectif: prise de decision a partir des donnees de l'echantillon
</div>

<div class="alert alert-warning" role="alert" markdown="1">
Ecarts eventuels entre l'echantillon et la population du au hasard de l'echantillonage
</div>

# Types de tests

- Test parametrique/non-parametrique
- Test d'adequation
- Est-ce que 2 valeurs sont egales ?
- Test de comparaison

## Point de depart

1. En cas de rejet de l'hypothese nulle
2. Les ecarts sont dits **significatifs**

Plusieurs interpretation:
- Loi de distribution inadaptee
- Echantillon non homogene
- Melange des populations avec des caracteristiques differentes
- Ecart du a des variations
- Echantillonnage pas effectue au hasard

## Que faire ?

<div class="alert alert-success" role="alert" markdown="1">
- isoler des echantillons plus homogenes
- preiciser les facteurs de variation influant sur les observations
</div>

Si l'hypothese pas nulle n'est pas rejetee
- Elle n'est pas demontree pour autant
- Elle n'est pas contredite par les faits

## Exemple grossier

1. Dans une foret, il y a $20\%$ de serpents venimeux
2. Francois preleve $100$ serpents et $38$ sont venimeux
3. Intervalle de fluctuation au seuil $0.95$

$$
\biggr[p-\frac{1}{\sqrt{n}};p+\frac{1}{\sqrt{n}}\biggr] = [0.10; 0.30]
$$


<div class="alert alert-info" role="alert" markdown="1">
**Theoreme**
Pour $95\%$ des echantillons, la proportion $f$ appartient a cet intervalle sous les conditions suivante:
1. $n\ge30$
2. $np\ge5$
3. $n(1-p)\ge5$
</div>


- $f=0.38\not\in[0.10;0.30]$
- On peut en deduire:
- Echantillon non representatif
- Variations pas dues au hasard

*Assertion sur la foret fausse ?*

## Autre exemple

- $x_1,\dots,x_n$ observations provenant d'une loi $\mathcal N(m,\sigma^2)$
- $\sigma^2$ suppose connu
- $n$ quelconque, variables aleatoires normales

$$
\frac{\sqrt{n}}{\sigma}(\bar X-m)\sim\mathcal N(0,1)\\
$$

*Qu'est-ce qu'on doit retenir ?*
> Un truc qui depend de l'echantillon
> $\mathcal N(0,1)$ ne depend plus du parametre, on peut s'amuser sans connaitre $m$

<div class="alert alert-danger" role="alert" markdown="1">
La loi ne depend pas du parametre
</div>

On va tester:
- $H_0:m=m_0$
- $H_1:m\neq m_0$

Prenons les etudiants d'Epita. Leur taille suit une loi normale de moyenne $1.70m$ et variance $0.05m$
- $H_0:m=1.7$
- $H_1:m\neq1.7$

### Hypothese $(H_0)$

$$
\frac{\sqrt{n}(\bar X_n-m_0)}{\sigma}
$$

suit une loi normale centree reduite.

D'apres les cours precedents
$$
\mathbb P(-1,96\le\frac{\sqrt{n}(\bar X_n-m_0}{\sigma}\le1,96)\simeq0,95
$$

1. Calculons $\bar x$ sur l'echantillon
2. Si $\frac{\sqrt{n}(\bar x-m_0)}{\sigma}\in[-1,96;1,96]$, l'hypothese $H_0$ est rejetee au seuil de signification $\alpha=5\%$
3. Sinon l'hypothese est acceptee

<div class="alert alert-info" role="alert" markdown="1">

**Seuil de signification** $\alpha$:
- Proba de rejeter l'hypothese nulle lorsque celle-ci est vraie
- Appele risque de premiere espece
- cf faux negatifs en medecine
- Test covid negatif en etant malade

</div>

<div class="alert alert-info" role="alert" markdown="1">
Le **risque de deuxieme espece** $\beta$ est l'inverse
- Proba d'accepter l'hypothese nulle lorsqu'elle est fausse
</div>

<div class="alert alert-danger" role="alert" markdown="1">
On ne peut pas baisser un risque sans augmenter l'autre
</div>

<div class="alert alert-info" role="alert" markdown="1">
**Region critique**
C'est la region ou on accepte
</div>

## Test de comparaison d'une proportion

- Meme principe pour $n$ grand
- $\sqrt{n}\frac{\hat p-p_0}{\sqrt{p_0(1-p_0)}}$ suit approximativement une loi normale centree reduite

1. Test bilateral $H_0:m=m_0$ et $H_1:m\neq m_0$
2. Test unilateral $H_0:m=m_0$ et $H_1:m\lt m_0$
3. Zone de rejet et region critique different

## Exemples

### Premier exemple

- $X$ suit une loi $\mathcal N(m,\sigma^2)$ avec $\sigma^2$ connu
- Test bilateral $H_0:m=m_0$ et $H_1:m\neq m_0$
- Statistique $Z_n:=\sqrt{n}\frac{\bar X_n-m_0}{\sigma}$

Sous l'hypothese $(H_0)$, $Z_n$ suit une loi normale centree reduite.
- Zone de rejet: $]-\infty;z_{1-\alpha}[\cup]z_{1-\alpha;+\infty}[$
- Region critique

$$
\biggr\{\frac{\sqrt{n}\vert \bar X_n-m_0}{\sigma}\gt z_{1-\alpha}\biggr\}
$$
- $z_{1-\alpha}$: fractile d'ordre $1-\alpha$ de la loi normale centree reduite

### Second exemple

- $X$ suit une loi $\mathcal N(m,\sigma^2)$ avec $\sigma^2$ inconnu
- Test unilateral $H_0:m=m_0$ et $H_1:m\lt m_0$
- Statistique

$$
T_n=\sqrt{n}\frac{\bar X_n-m_0}{\sqrt{S_n^2}}
$$

Sous l'hypothese $(H_0)$, $\mathcal T_n$ suit une loi $T_{n-1}$
- Zone de rejet: $]-\infty;-t_{1-\alpha}[$
- Region critique:

$$
\biggr\{\sqrt{n}\frac{\bar X_n-m_0}{\sqrt{S_n^2}}\le =t_{1-\alpha}\biggr\}
$$
- $t_{1-\alpha}$: fractile d'ordre $1-\alpha$ de la loi de Student a $n-1$ degre de liberte

# Methode de la valeur critique

- Methode due a Neyman et Pearson
- Approche ensembliste
- Ensemble des valeurs observees de la stat du test provoquant un rejet
- Zone de rejet
- Complementaire de cet ensemble: zone de non-rejet
- valeur separant ces 2 ensembles valeur critique

## Methode de la proba critique

- $\alpha$ est fixe
- proba critique ou $P_{valeur}$: plus petite valeur du risque d'erreur pour laquelle la decision serait de rejeter $H_0$
- Si $P_{value}\le\alpha$, $H_0$ est rejetee
- Si $P_{value}\gt\alpha$, pas de raison de rejeter $H_0$ au risque de premiere espece $\alpha$

### Exemple

Duree de vie des ampoules fabriquees par un industriel
- $H_0:m=8000$
- $H_1:m\neq8000$
- $\alpha=5\%$

On a un echantillon de $100$ ampoules.

$$
Z_n:=\sqrt n\frac{\bar X_n-m_0}{\sqrt{S_n^2}}
$$

suit approximativement une loi normale centree reduite

- $P_{value}=\mathbb P(Z_n\lt -1.51)\simeq0.0655$
- $P_{value} \gt\alpha$, pas de raison de rejeter l'hypothese $(H_0)$