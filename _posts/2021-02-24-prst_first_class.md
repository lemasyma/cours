---
title:          "PRST: Les differentes lois"
date:           2021-02-24 14:30
categories:     [Image S8, PRST]
tags:           [Image, SCIA, PRST, S8]
description: Les differentes lois
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/B12PIR7fu)

# Syllabus
1. Rappel sur les notions de probas elementaires
2. Rappel sur les variables scalaires

# Generalites
- Etude d'experiences aleatoires
- Experience aleatoire: experience dont on ne peut prevoir l'issue a l'avance mais dont on connait toutes les issues possibles
- Alea vient du latin *alea* qui est un jeu de des

## Situation elementaire
1. $n$ issues $\omega_1,..., \omega_n$
2. univers $\Omega=\{\omega_1,..., \omega_n\}$
3. Proba d'occurence associee $p_1,..., p_n$
4. loi de proba: donnees des $p_i
5. Les probas $p_i$ sont positives et verifient: $p_1+...+p_n = 1$
6. evenements: sous-ensemble de $\Omega$
7. Probabilite d'un evenements: somme des probas des issues qui le realise

Exemple d'experience aleatoire: 
- traverser la route et voir si on se fait ecraser ou non (Alexandre tu vas bien ?) $\rightarrow$ experience de Bernoulli a 2 issues

*Quelles experiences aleatoire en informatique ?*
La duree de vie d'un composant electronique

### Proprietes
- equiprobabilite: toutes les issues ayant la meme proba
- exercice: proposer une situation qui n'est pas equiprobable
- $A\cap B$: ensemble des issues qui realisent simultanement $A$ et $B$
- $A\cup B$: ensmeble des issues qui realisent au moins un des 2 evenemenents

# Conditionnement
- Soient A et B evenements (supposons $P(A) \neq 0$ et $P(B) \neq 0$)
- $P_A(B) = \frac{P(A \cap B)}{P(A)}$
- Formule de Bayes: $P_B(A) = \frac{P_A(B)\times P(A)}{P_A(B)\times P(A) + P_{\overline{A}}(B) \times P(\overline{A})}$
- $P(B) = P_A(B)\times P(A)+P_A(B)\times P(\overline{A})$

## Demonstration
$$
\begin{aligned}
P_B(A) &= \frac{P(A \cap B)}{P(B)}\\
&= \frac{P_A(B)P(A)}{P(B)}\\
&= \frac{P_A(B)P(A)}{P_A(B)\times P(A) +P_A(B)\times P(\overline{A})}
\end{aligned}
$$

<div class="alert alert-danger" role="alert" markdown="1">
C'est une proba **a posteriori**, cad apres que l'experience ait eu lieu.
</div>

# VA discrete
1. VA $X :$ fonction definie sur $\Omega$ et a valeurs dans $\mathbb R$
2. $X$ peut prendre les valeurs $x_1,..., x_n$
3. $\Omega$ sera "oublie" et on se concentrera sur les probas $p_i := P(\{\omega\in\Omega\vert X(\omega) = x_i\}):= P(X=x_i)$
4. Loi d'une variable aleatoire: donnee par des reels $P(X=x_i)$
5. *exercice*: modeliser le gain a un jeu de Pile ou Face a l'aide d'une VA (gain de 100 euros si le "Pile" et perte de 80 euros si "Face")
    - valeurs: 100 et -80
    - ex: si la piece tombe sur 2 on gagne 100 euros, sinon on en perde 80
    - $p_g = \frac{1}{6}$
    - $p_p = \frac{5}{6}$

<div class="alert alert-warning" role="alert" markdown="1">
Cf. [Exercice 4](https://lemasyma.github.io/cours/posts/prst_first_exercise/#exercice-4)
</div>

Prenons Clara et Nizar en cobayent avec leurs numero prefere

||Clara|Nizar||
|-|-|-|-|
|1|-10|30|20|
|2|50|-20|30|
|3|-10|30|20|
|4|-10|-20|-30|
|5|50|30|80|
|6|-10|-10|-20|

- $x_1 = -10$
- $x_2 = 50$
- $y_1 = -20$
- $y_2 = -10$
- $y_3 = 30$

1. **Attention, la definition des reels $p_i$ a change !**
2. Esperance: $E(X) = \sum_{i=1}^np_i(x_i-\overline x)^2$
3. Variance: $V(X) = E(X - E(X)^2) = E(X^2) - E(X)^2$

# Loi de Bernoulli
1. VA $X$ pouvant prendre les valeurs 0 et 1
2. proba de prendre la valeur 1 notee $p$
3. par consequent: $P(x=0)=1-p$
4. $E(X) = p\times1 + (1-p)\times 0 = p$ et $V(X) =E((X - E(X)^2)) = p(1-p)$
5. Loi notee $B(p)$

# Loi binomial de parametre $n$ et $p$
1. some de $n$ variables independantes suivant une loi $B(p)$
2. Nombre de succes apres $n$ repetitions d'une experience de Bernouilli
3. VA $X$ pouvant prendre les valeurs entieres comprises entre 0 et $n$
4. $P(X=k) = \binom{n}{k}p^k(1-p)^{n-k}$ pour $k\in\{0,...,n\}$
5. Loi notee $B(n,p)$
6. $\binom{n}{k}$: coefficient binomial
7. $E(X) = np$ et $V(X) = np(1-p)$


![](https://i.imgur.comQGGMsW.png)

- $\binom{4}{0} = 1$
- $\binom{4}{1} = 4$
- $\binom{4}{2} = 6$
- $\binom{4}{3} = 4$
- $\binom{4}{4} = 1$

*Comment trouver de maniere maths ?*
On utilise le triangle de Pascal
![](https://i.imgur.com/hnfU6Cy.png)


- $\binom{6}{3} = 20$
- $\binom{3}{2} = 3$

*Quels sont les elements remarquables sur le triangle de Pascal ?*
<div class="alert alert-success" role="alert" markdown="1">
- $\binom{n}{k} = \binom{n}{n-k}$
- $\binom{n}{0} = \binom{n}{n} = 1$
- $\binom{n}{1} = \binom{n}{n - 1} = n$
</div>
<div class="alert alert-warning" role="alert" markdown="1">
Cf. [Exercice 3](https://lemasyma.github.io/cours/posts/prst_first_exercise/#exercice-3)
</div>

# Loi binomial negative de parametre $n$ et $p$
1. aussi appelee *loi de Pascal*

# Loi geometrique de parametre *p*
1. nombre d'essais avant le premier succes dans une repetition de tirages inde de Bernoulli
2. $p$ : probabilite de "Succes"
3. $X$ peut prendre toutes les valeurs entieres hormis 0
4. $P(X=k)=pq^{k-1}$ ou $q=1-p$
5. $E(X) = \frac{1}{p}$ et $V(X)=\frac{q}{p^2}$
6. Loi notee $G(p)$

<div class="alert alert-danger" role="alert" markdown="1">
C'est une loi **sans memoire**.
</div>
*Qu'est-ce que ca veut dire ?*
> La loi geometrique est "sans memoire", cad que les evenements passes n'influent pas les evenements futurs.

<div class="alert alert-warning" role="alert" markdown="1">
Cf. [Exercice 14](https://lemasyma.github.io/cours/posts/prst_first_exercise/#exercice-14)
</div>



<div class="alert alert-info" role="alert" markdown="1">
Les 2 grandes lois sans memoire sont les lois:
- exponentielle
- geometrique
</div>

# Loi Poisson de parametre $\lambda$
1. $X$ peut prendre toutes les valeurs entieres
2. $\lambda$ parametre strictement positif
3. $P(X=k) = e^{-\lambda}\frac{\lambda^k}{k!}$
4. $E(X) = \lambda$ et $V(X) = \lambda$
5. loi notee $P(\lambda)$

<div class="alert alert-warning" role="alert" markdown="1">
Cf. [Exercice 6](https://lemasyma.github.io/cours/posts/prst_first_exercise/#exercice-6)
</div>

# Cadre
1. $X$ definie sur l'univers $\Omega$ et a valeurs dans $\mathbb R$ ou dans un intervalle $I$
2. $P(X\in[a;b]) = \int_a^bf(x)dx$
3. fonction $f$ appelee la *densite* de la variable aleatoire $X$
4. Pour un reel $x$ donne: $P(X=x)=0$

# Densite de probabilite
1. 2 conditions a connaitre
2. $f(x)\ge0$ pour tout reel $x\in I$
3. $\int_If(x)dx = 1$ (l'intervalle peut etre $\mathbb R$)

# Fonction de repartition
1. Soit $X$ une variable aleatoire
2. $F_X(x) := P(X\le x) = \int_{-\infty}^{x}f(t)dt$
3. Fonction de survie: $R_X(x) := P(X\gt x) = 1 - F_X(x)$

$\int_0^{+\infty}e^xdx$ a un sens dans $[0; +\infty]$

# Esperance
- formule analogue au cas discret
- si $\int_f\vert x\vert f(x)dx\lt+\infty$

# Variance
- Si $\int_fx^2\vert f(x)\vert dx\lt+\infty$ la VA $X$ est dite de carre *integrable*
- $V(X) = \int_f(x-E(X))^2f(x)fx$ est bien definie
- $V(X) = E(X^2) - E(X)^2$ (theoreme de Koenig-Huyghens)
- $V(aX) = a^2V(X)$

## Pour $X$ et $Y$
<div class="alert alert-warning" role="alert" markdown="1">
Tout depend de la dependance des variables, si $X$ et $Y$ sont independantes: $E(XY) = E(X)E(Y)$
</div>

# Loi uniforme sur l'intervalle $[a;b]$
1. $f(x) = \frac{1}{b-a}$ pour $x\in [a;b]$ et $f(x) = 0$ pour $x\not\in[a;b]$
2. $P(X\in[c;d]) = \frac{d-c}{b-a}$ si $a\le c \le c\le d \le b$ et $a\lt b$
3. $E(X) = \frac{a+b}{2}$ et $V(X) = \frac{(b-a)^2}{12}$
4. *Exercice:* demontrer ce resultat puis calculer la fonction de reparatition associes
5. Notee $U([a;b])$

<div class="alert alert-warning" role="alert" markdown="1">
CF. [Exercice 11](https://lemasyma.github.io/cours/posts/prst_first_exercise/#exercice-11)
</div>

# Loi exponentielle de parametre $\lambda\gt 0$
1. $f(x) = \lambda e^{-\lambda x}$ pour $x\ge 0$ et $f(x) = 0$ pour $x\lt0$
2. $E(X)=\frac{1}{\lambda}$ et $V(X) = \frac{1}{\lambda^2}$
3. $F(x) = 1-e^{-\lambda x}$ pour $x\ge 0$ et $F(x) = 0$ sinon
4. $R(x) = e^{-\lambda x}$ pour $x\ge 0$ et 

# Loi exponentielle
1. Loi notee $\varepsilon(\lambda)$
2. duree de vie d'un phenomene sans memoire
3. $\forall s\gt 0, \forall t \gt 0, P_{T\gt t}(T\gt s + t) = P(T\gt s)$

# Loi normale centree reduite
1. $f(x) = \frac{1}{\sqrt{2\pi}}e^{-\frac{x^2}{2}}$ pour $x\in\mathbb R$
2. $E(X) = 0$ et $V(X) = 1$
3. Loi notee $N(0;1)$

![](https://i.imgur.com/WX0beS7.png)

1. $P(X\le0)=P(X\ge0) = 0.5$
2. $P(X\le-a) = P(X\ge a)$
3. $P(-196\le X\le 1.96)\approx0.95$ et $P(-2,58\le X\le2.58)\approx 0.99$
4. Loi notee $N(0,1)$

# Loi normale de parametre $\nu$ et $\sigma$
1. Loi notee $N(\nu,\sigma^2)$
2. $X$ suit une loi $N(\nu,\sigma^2)$ si $Y = \frac{X-\nu}{\sigma}$ suit une loi normale centree reduite

![](https://i.imgur.com/Y9kXG7d.png)

- $P(\nu-\sigma\le X\le \nu+\sigma)\approx0.68$
- $P(\nu-2\sigma\le X\le \nu+2\sigma)\approx0.95$
- $P(\nu-3\sigma\le X\le \nu+3\sigma)\approx0.997$