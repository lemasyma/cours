---
title:          "PRST: Exercices de cours du 17/03"
date:           2021-03-17 14:30
categories:     [Image S8, PRST]
tags:           [Image, SCIA, PRST, S8, Fisher, EMV]
description: Exercices de cours du 17/03
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/rJ2yA214O)

<div class="alert alert-warning" role="alert" markdown="1">
Les exos sont fait dans le meme ordre que pendant le cours
</div>

# Exercice - loi normale
1. loi normale de paramètres $m$ et $\sigma$ avec $\sigma=1$
2. densite $f(x,m)=\frac{1}{\sqrt{2\pi}}e^{-\frac{(x-m)^2}{2}}$ pour $x\in\mathbb R$ et $m\in\mathbb R$
3. Déterminer l'EMV.

<details markdown="1">
<summary>Solution</summary>

$$
\begin{aligned}
L(x_1,...,x_n)&=\Pi_{i=1}^n\frac{1}{\sqrt{2\pi}}e^{-\frac{(x_i+m)^2}{2}}\\
&= \biggr(\frac{1}{\sqrt{2\pi}}\biggr)e^{-\sum_{i=1}^n\frac{(x_i-m)}{2}}
\end{aligned}
$$

Passons au logarithme.

*Est-ce que la fonction est paire ?*
Oui car $\log$ est defini sur $\mathbb R^{+*}$.

$$
\log(L(x_1,...,x_n,m))=-n\log(\sqrt{2\pi})-\sum_{i=1}^n\frac{(x_i-m)^2}{2}
$$

Derivons par rapport a m:

$$
\begin{aligned}
\frac{\delta\log(L(x_1,...,x_n,m))}{\delta m} &= -\sum_{i=1}^n\biggr[(-x_i)+m\biggr]\\
&= \sum_{i=1}^nx_i-nm\\
\end{aligned}\\
\begin{aligned}\\
\frac{\delta\log(L(x_1,...,x_n,m))}{\delta m}=0&\Leftrightarrow\sum_{i=1}^nx_i-mn=0\\
&\Leftrightarrow\frac{1}{n}\sum_{i=1}^nx_i=m
\end{aligned}
$$

Verifions la condition du second ordre:

$$
\frac{\delta\log(L(x_1,...,x_n,m))}{\delta m}=-n\lt0
$$

<div class="alert alert-success" role="alert" markdown="1">
Donc la condition suffisante est verifiee.
</div>

$\hat m = \bar X$ est l'EMV du parametre $m$.

</details>

# Exercice - loi geometrique
1. loi géométrique de paramètre $p$
2. $P(X=x)=p(1-p)^{x-1}$ pour $x\gt1$ et $p\in]0;1[$
3. Déterminer l'EMV.

<details markdown="1">
<summary>Solution</summary>

Soit $(x_1,...,x_n)\in\mathbb N^n_*$.

$$
\begin{aligned}
L(x_1,...,x_n,p)&=\Pi_{i=1}^np(1-p)^{x_i-n}\\
&=p^n(1-p)^{\sum_{i=1}^n(x_i-1)}
\end{aligned}\\
\log(L(x_1,...,x_n,p))=n\log(p)+\sum_{i=1}^n(x_i-1)\log(1-p)\\
\frac{\delta\log(L(x_1,...,x_n,p))}{\delta p}=\frac{n}{p}-\sum_{i=1}^n\frac{x_1-1}{1-p}
$$

<div class="alert alert-danger" role="alert" markdown="1">

$$
(\log u)'=\frac{u'}{u}\\
\Leftrightarrow \log (1-p) = -\frac{1}{1-p}
$$

</div>

$$
\frac{\delta\log(L(x_1,...,x_n,p))}{\delta p} = 0\\
\begin{aligned}
\frac{n}{p}=\sum_{i=1}^n\frac{x_1-1}{1-p}&\Leftrightarrow n(n-p)=p\sum_{i=1}^n(x_i-1)\\
&\Leftrightarrow n-np=p\sum_{i=1}^nx_i - np\\
&\Leftrightarrow p = \frac{n}{\sum_{i=1}^nx_i} = \frac{1}{\frac{n}{\sum_{i=1}^nx_i}} = \frac{1}{\bar X}
\end{aligned}\\
$$

<div class="alert alert-danger" role="alert" markdown="1">

$$
(\frac{1}{u})' = \frac{u'}{u}
$$

</div>

$$
(\frac{1}{1-p})'=-\frac{(-1)}{(1-p)^2}=\frac{1}{(1-p)^2}
$$

<div class="alert alert-success" role="alert" markdown="1">

$$
\frac{\delta^2\log(L(x_1,...,x_n,p))}{\delta p^2}=-\frac{n}{p}-\frac{\sum_{i=1}^n(x_i-1)}{(1-p)^2}\lt0
$$

Donc la condition suffisante est verifiee.

</div>

$\hat p =\frac{1}{\bar X}$ est l'EMV du parametre $p$.

</details>

# Exercice - information de Fisher
Déterminer l'information de Fisher pour la loi de Poisson de paramètre $\lambda$.

<details markdown="1">
<summary>Solution</summary>

$$
\log f(x,\delta)=-\delta+x\log(\lambda)-\log(x!)\\
\frac{\delta\log f(x,\lambda)}{\delta\lambda} = -n+\frac{x}{\lambda}\\
\frac{\delta^2\log f(x,\lambda)}{\delta\lambda^2}=-\frac{x}{\lambda^2}\\
\begin{aligned}
E_n\biggr(\frac{\delta^2\log f(X,\lambda)}
{\delta\lambda^2}\biggr)&=-E(\frac{X}{\lambda^2})\\
&=-\frac{1}{\lambda^2}\times\lambda=-\frac{1}{\lambda}
\end{aligned}\\
I(\lambda)=-E\biggr(\frac{\delta^2\log f(x,\lambda)}{\delta\lambda^2}\biggr)=\frac{1}{\lambda}
$$

</details>