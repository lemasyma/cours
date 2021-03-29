---
title:          "PRST: Feuille 2, suite"
date:           2021-03-29 9:00
categories:     [Image S8, PRST]
tags:           [Image, SCIA, PRST, S8,  loi, intervalle, confiance]
description: Feuille 2, suite
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/Skw48_1rO)

# Exercice 14

Considerons une variable aleatoire $X$ suivant une normale centree reduite et une variable aleatoire $\varepsilon$ independante de la variable aleatoire $X$ telle:

$$
P(\varepsilon=-1)=P(\varepsilon=1)=\frac{1}{2}
$$

Considerons la variable aleatoire $Y := \varepsilon X$.

1. Montrer que la variable aleatoire $Y$ suit une loi normale centree reduite
2. Calculer $Cov(X,Y)$
3. Determiner la loi de la v.a. $X+Y$
    - Si c'est trop difficile, calculer $P(X+Y=0)$
4. En deduire que le vecteur aleatoire $(X,Y)^T$ n’est pas un vecteur gaussien.
5. **Bonus**: determiner la fonction de repartition de $X+Y$

<details markdown="1">
<summary>Solution</summary>

1.
<div class="alert alert-info" role="alert" markdown="1">
Pour $Y\sim\mathcal N(0,1)$, il faut montrer que $Y$ suit la meme loi que $X$
</div>

Soit $a$ et $b$ deux reels tels que $a\le b$

$$
\begin{aligned}
P(Y\in[a;b]) &= P(\{Y\in[a;b]\}\cap\{\varepsilon=-1\}) + P(\{Y\in[a;b]\}\cap\{\varepsilon=1\})\\
&= P(\{-X\in[a;b]\}\cap\{\varepsilon=-1\}) + P(\{X\in[a;b]\}\cap\{\varepsilon=1\})
\end{aligned}
$$

Or les v.a. $\varepsilon$ et $X$ sont independantes

$$
\begin{aligned}
P(Y\in[a;b]) &= P(-X\in[a;b])\times P(\varepsilon=-1) + P(X\in[a;b])\times P(\varepsilon=1)\\
&= \frac{1}{2}P(-X\in[a;b]) + \frac{1}{2}P(X\in[a;b])\\
X&\sim\mathcal N(0,1)\\
\alpha X&\sim\mathcal N(\alpha m,\alpha\sigma^2)\\
&= \frac{1}{2}P(X\in[a;b]) + \frac{1}{2}P(X\in[a;b])\\
&= P(X\in[a;b])
\end{aligned}
$$

<div class="alert alert-success" role="alert" markdown="1">
Y suit la meme loi que $X$ donc $Y\sim\mathcal N(0,1)$
</div>

Avec la fonction caracterisitique:

$$
\begin{aligned}
\phi_Y(X) &= E(e^{it\psi})\\
&= E(e^{-it\psi}\underbrace{𝟙_{\varepsilon=-1}}_{\text{fonction indicatrice}} + e^{it\psi}𝟙_{\varepsilon=1})\\
&= E(e^{-itX}𝟙_{\varepsilon=-1} + e^{itX}𝟙_{\varepsilon=1})\\
&= E(e^{-itX} ) E(𝟙_{\varepsilon=-1}) + E(e^{itX})E(𝟙_{\varepsilon=1})\\
\end{aligned}
$$

2.

$$
\begin{aligned}
Cov(X,Y)&=E(XY)-\underbrace{E(X)}_{=0}\underbrace{E(Y)}_{=0}\\
&=E(XY)=E(\varepsilon X^2)
\end{aligned}
$$

Les v.a. $\varepsilon$ et $X$ sont independnates donc $\varepsilon$ et $X^2$ aussi.

$$
Cov(X,Y)=E(\varepsilon)E(X^2)\\
E(\varepsilon)=\frac{1}{1}\times-1+\frac{1}{1}\times1 =0
$$

3.

$$
P(X+Y=0)=P(X=-Y)=P(\varepsilon=-1)=\frac{1}{2}\\
P(X+Y=2X)=\color{red}{P(Y=X)}=P(\varepsilon =1)=\frac{1}{2}
$$

Ecrit "savamment":

$$
\delta_{a}(A)=
\begin{cases}
0 &\text{si } a\not\in A\\
1 &\text{si } a\in A
\end{cases}
$$

<div class="alert alert-danger" role="alert" markdown="1">

$$
\mu_Y=\frac{1}{2}\delta_0+\frac{1}{2}\mu_X
$$

</div>

> Mais c'est pas ce qui nous interesse lul

4.

Deux types de v.a.: discrete et continue

<div class="alert alert-danger" role="alert" markdown="1">
Y n'est pas continue car la probabilite d'etre egale a un certain nombre et toujours egal a $0$. On cherche pas un nombre mais un intervalle.
</div>

- Si $X+Y$ etait gaussienne $P(X+Y=0)=0$
- D'apres la question precedente, $P(X+Y=0)=\frac{1}{2}$
- la combinaison lineaire $X+Y$ n'est pas guassienne donc le vecteur n'est pas gaussien

Bonus:

On pose $Z=X+Y$.

$$
\begin{aligned}
P(Z\le z)&= P(\{Z\le z\}\cap\{\varepsilon=-1\})+P(\{Z\le z\}\cap\{\varepsilon=1\})\\
&= P(\{0\le z\}\cap\{\varepsilon=-1\})+P(\{2X\le z\}\cap\{\varepsilon=1\})\text{ les v.a. sont independantes}
\end{aligned}
$$

- Si $z=0$, $F_Z(z)=\frac{1}{2}\times F_X(\frac{z}{2})$
- Si $z\ge0$, $F_Z(z)=\frac{1}{2}+\frac{1}{2}F_X(\frac{z}{2})$

$$
F_Z(z)=
\begin{cases}
\frac{1}{2}F_X(\frac{z}{2}) &\text{si }z\lt0\\
\frac{1}{2}+\frac{1}{2}F_X(\frac{z}{2}) &\text{si } z\ge0
\end{cases}
$$

</details>
