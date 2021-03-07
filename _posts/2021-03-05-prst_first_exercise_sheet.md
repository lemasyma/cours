---
title:          "PRST: Feuille 1 - Exercice"
date:           2021-03-05 14:30
categories:     [Image S8, PRST]
tags:           [Image, SCIA, PRST, S8]
description: Feuille 1 - Exercice
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/SJ6TZxemd)

<div class="alert alert-info" role="alert" markdown="1">
L'ordre des exos dans le cours est 3 $\to$ 9 $\to$ 15 $\to$ 16 $\to$ 13
</div>

# Exercice 3
1. Déterminer la fonction caractéristique de la loi de Bernoulli de paramètre $p$.
2. Déterminer la fonction caract´eristique de la loi exponentielle de paramètre $\lambda$.

<details markdown="1">
<summary>Solution</summary>
1. $X\sim\mathcal B(p), E(e^{itx}) = p\times e^{it\times 1} + (1-p)e^{it\times 0} = 1-p+p e^{it}$
2. Soit $t\in\mathbb R$:

$$
\begin{aligned}
\phi(t) = E(e^{itX}) &= \int_0^{+\infty}e^{itx}\lambda e^{-\lambda x}dx\\
&= \lambda\int_0^te^{(it-X)x}dx\\
\text{Soit } A\gt0: \int_0^Ae^{(it-X)x}dx &= \biggr[\frac{1}{it-\lambda}e^{(it-\lambda)x}\biggr]_0^A\\
&= \frac{1}{it-\lambda}e^{(it-\lambda)A} - \frac{1}{it-\lambda}\times1\\
e^{(it-\lambda)A} &= \underbrace{e^{itA}}_{\le1 \text{ car bornee}}\times e^{-\lambda A}\\
\end{aligned}\\
\lim_{A\to+\infty} e^{-\lambda A} = 0
$$

Car $\lambda\gt 0$. Par ailleurs $\vert e^{itA}\vert\le1$. Donc $\lim_{A\to+\infty}\frac{1}{it-\lambda} e^{-\lambda A} = 0$ d'ou $\lim_{A\to+\infty}\int_0^Ae^{(it-\lambda)x}dx = - \frac{1}{it-\lambda} = \frac{1}{\lambda - it}$.

Conclusion: $\int_0^{+\infty}e^{(it-\lambda)x}dx$ est bien definie et egale a $\frac{1}{\lambda - it}$

<div class="alert alert-success" role="alert" markdown="1">
$$
\phi(t) = \frac{\lambda}{\lambda - it}
$$
</div>

</details>

# Exercice 9
Dans une fabrication en série, 7% des produits présentent un défaut. 40
articles sont contrôlés
1. Que vaut la probabilité que 4 articles présentent un défaut?
2. Que vaut la probabilité que moins de 4 articles présentent un défaut?


<details markdown="1">
<summary>Solution</summary>

*Pourquoi peut-on considerer que chaque V.A. (echantillon) sont independantes les unes des autres ?*

<div class="alert alert-success" role="alert" markdown="1">
Comme c'est une **fabrication en serie**, c'est fait en tres grand nombre et un echantillon de 40 ne change rien. 
</div>

<div class="alert alert-danger" role="alert" markdown="1">
Pour parler de loi binomiale, il faut que l'echantillon soit petit par rapport a la population.
</div>

$$
\begin{aligned}
P(X=4)&=\binom{40}{4}\times0,07^4\times4,96^36\simeq0,16\\
P(X\lt4)&=P(X=1)+P(X=2)+P(X=3)\simeq 0,69
\end{aligned}
$$

</details>


# Exercice 13
Soient $\alpha$ un réel strictement positif et X une variable aléatoire dont la densité est définie par:
$f_X(x) = \alpha x^{−\alpha−1}$ pour $x \ge 1$ et $f_X(x) = 0$ sinon.
1. Vérifier que $f_X$ est bien une densité de probabilité et déterminer la fonction de répartition associée
2. Calculer $P(0 \lt X \le 2)$,
3. Pour quelles valeurs de $\alpha$, la variable aléatoire $X$ admet-elle une espérance? La calculer quand elle existe

Dans cet exercice, nous avons étudié la loi de Pareto de paramètre $\alpha$.

<details markdown="1">
<summary>Solution</summary>
1. Montrons que $f_X$ est bien une densite.

$$
\begin{aligned}
&\text{i. } f_X(x)\ge0 \text{ par construction.}\\
&\text{ii. } \int_1^{+\infty}f_X(x)dx=1?
\end{aligned}
$$

Soit $A\gt0$:

$$
\begin{aligned}
\int_1^Af_X(x)dx=\int_1^A\alpha x^{-\alpha-1}dx &= \biggr[\frac{\alpha}{-\alpha}x^{-\alpha}\biggr]_1^A\\
&= [x^{-\alpha}]_1^A
\end{aligned}
$$

On sait que 

$$
lim_{A\to+\infty}A^{-\alpha}=lim_{A\to+\infty}\frac{1}{A^\alpha} = 0
$$

D'ou 

$$
\int_1^{+\infty}f_X(x)dx=\lim_{A\to+\infty}\int_1^Af_X(x)dx = 1
$$

Fonction de repartition:

$$
F_X(x) = \int_1^x\alpha t^{-\alpha-1}dt = 1-x^{-\alpha}
$$

2.

$$
\begin{aligned}
P(0\lt x\le2) &= P(1\le Y\le2) = \int_1^2\alpha x^{-\alpha-1}dx\\
&=[-x^{-\alpha}]_1^2 = 1-\frac{1}{2^\alpha}
\end{aligned}
$$

3. $\alpha\gt 1$

</details>

# Exercice 15
Les œufs pondus par une poule ont une longueur pouvant être modélisée
à l’aide d’une loi normale d’espérance 6 et d’écart-type 1,4. Quelle est la
probabilité de trouver un oeuf:
1. d’une longueur supérieure à 8cm?
2. d’une longueur inférieure à 5cm?

<details markdown="1">
<summary>Solution</summary>
1. Notons L la v.a. consideree $L\sim\omega(6,(1,4)^2)$, $Y=\frac{X-6}{1,4}\sim\mathcal N(0,1)$

$$
\begin{aligned}
1-P(X\le8) &= 1-P(\frac{X-6}{1,4}\le \frac{8-6}{1,4}) \text{ Possible de le faire directement car 8 est positif}\\
&= 1-P(Y\le\frac{10}{7})\simeq1-P(Y\le 1,43)
\end{aligned}
$$

Cherchons 1,43 dans la table $\mathcal N(0,1)$

$$
1-P(Y\le1,43)\simeq0,92\sim0,08
$$

2.

$$
\begin{aligned}
P(X\lt5) &= P(Y\lt\frac{5-6}{1,4}) = P(Y\lt-\frac{1}{1,4})\simeq P(Y\lt-0,71)\\
&= 1-P(Y\lt0,71)
\end{aligned}
$$

D'apres la table de la loi $\mathcal N(0,1)$ $P(Y\lt0,71)\simeq0,76$ donc $P(Y\ge0,71)\simeq 0,24$ et $P(X\lt5) = P(Y\lt-0,71)\simeq0,24$

</details>

# Exercice 16
Les composants d’un autoradio ont une durée de vie pouvant être modélisée par une loi normale d’espérance 2400 (heures d’utilisation) et d’écart-type 300. Un autoradio est utilisé, en moyenne, 1000 heures par an. Quelle est la probabilité qu’un composant ait une durée de vie supérieure à 3 ans?

<details markdown="1">
<summary>Solution</summary>
Methode de professionnel:

<div class="alert alert-info" role="alert" markdown="1">
Si $X$ suit une loi normale $N(\mu,\sigma^2)$

$$
P(\mu-\sigma\le X\le\mu+\sigma)\simeq0,68\\
P(\mu-2\sigma\le X\le\mu+2\sigma)\simeq0,95\\
P(\mu-3\sigma\le X\le\mu+3\sigma)\simeq0,997\\
$$
</div>

$$
P(2400-2\times300\le X\le2400+2\times300) = P(1800\le X\le3000)\simeq0,95\\
Y=\frac{X-2400}{300}\sim\mathcal N(0,1)\\
P(X\gt3000)=P(\frac{X-2400}{300}\gt2)\Rightarrow1-P(Y\le2)\simeq1-0,997=0,023 \text{ le jeu des arrondis}
$$

</details>