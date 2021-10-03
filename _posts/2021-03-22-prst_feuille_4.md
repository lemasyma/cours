---
title:          "PRST: Feuille 4 - Exercices"
date:           2021-03-22 11:00
categories:     [Image S8, PRST]
tags:           [Image, SCIA, PRST, S8,  loi, intervalle, confiance]
math: true
description: Feuille 4 - Exercices
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/BJekRCBEu)

# Exercice de cours
Proposer un intervalle de confiance asymptotique au niveau $0,90$ pour la moyenne $m$ d'une variable aléatoire.

<details markdown="1">
<summary>Solution</summary>

Astuce: mettre $0,05$ de chaque cote de la courbe, on cherche donc $95\%$ sur notre table de loi normale centree reduite

On a donc $1,96$ dans la table.

Cf. cours.

</details>

# Exercice de cours
François prélève 300 serpents dans une forêt et constate que 70 d'entre eux sont venimeux.
Déterminer un intervalle de confiance asymptotique pour la proportion de serpents venimeux dans cette forêt au niveau de confiance 0, 95.

<details markdown="1">
<summary>Solution</summary>

$\hat p = \frac{70}{300}\simeq0,23, n = 300$

Conditions d'applications du resultat:
1. $n\ge 30$
2. $n\hat p \ge5$
3. $n(1-p)\ge5$

$$
\hat p -1,96\frac{\sqrt{\hat p(1-\hat p)}}{\sqrt n}\simeq 0,18\\
\hat p +1,96\frac{\sqrt{\hat p(1-\hat p)}}{\sqrt n}\simeq 0,28
$$

On a donc $[0,18;0,28]$

</details>

# Exercice 1
Proposer un intervalle de confiance au niveau $0,90$ pour la moyenne $m$ pour une variable aleatoire gaussienne de variance $2$ dont nous connaissons les observations suivantes : $3,1 ; 2,4 ; 5 ; 7$ et $2,8$.

<details markdown="1">
<summary>Solution</summary>
![](https://i.imgur.com/qT6XGCQ.png)

$$
\sigma = 2\\
V(X) = \sqrt 2\\
\bar X_n \simeq 4,06\\
$$

<div class="alert alert-success" role="alert" markdown="1">
On obtient $[3,023;5,09]$
</div>

</details>

# Exercice 6

1. Soit $U_n$ une variable aleatoire suivant une loi $\mathcal X^2(n)$, $(n\ge1)$. Admettons que $\phi_{U_n}(t)=\frac{1}{(1-2it)^{\frac{n}{2}}}$ est sa fonction caracteristique.
    (a) Montrer que $E(U_n)=n$
    (b) Montrer que $V(U_n)=2n$
2. Soient $X$ et $Y$ deux variables aleatoires independantes suivant respectivement des lois $\mathcal X^2(m)$ et $\mathcal X^2(n)$. Montrer que la variable aleatoire $X+Y$ suit une loi $\mathcal X^2(m+n)$

<details markdown="1">
<summary>Solution</summary>

$$
E(X) = \frac{\phi'(0)}{i} \text{(cf chapitre 1 complement)}\\
\phi_{U_n}'(t)= \frac{ni}{(1-2it)^{\frac{n}{2}+1}}\\
E(X) = \frac{\phi_{U_n}'}{i}=n\\
$$

<div class="alert alert-danger" role="alert" markdown="1">
$$
(\frac{1}{u^n})'=-\frac{ku'}{u^{k+1}}
$$
</div>

$$
\phi_{U_n}''(t)=\frac{-(n+2)n}{(1+2it)^{\frac{n}{2}+2}}\\
E(X^2)=-\phi^{(2)}(0) = n(n+2)\\
V(X) = E(X^2)-E(X)^2=n(n+2-n)=2n
$$

$X\sim\mathcal X^2(m)$, $Y\sim\mathcal X^2(n)$

$$
\begin{aligned}
\phi_{X+Y}&=\phi_X(t)\phi_Y(t)\\
&= \frac{1}{(1-2it)^{\frac{m}{2}}}\times\frac{1}{(1-2it)^{\frac{n}{2}}}\\
&=\frac{1}{(1-2it)^{\frac{m+n}{2}}} \text{ , cqfd.}
\end{aligned}
$$

</details>
