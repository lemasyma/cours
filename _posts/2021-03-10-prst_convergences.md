---
title:          "PRST: Seance 3, Convergences"
date:           2021-03-10 14:30
categories:     [Image S8, PRST]
tags:           [Image, SCIA, PRST, S8, loi, convergence, central limite, estimateur, moment, maximum de vraisemblance, exponentielle]
math: true
description: Seance 3, Convergences
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/HykZhB87d)

# Modes de convergence
## Convergence presque sure (p.s.)
1. $(X_i)$ suite de v.a definies sur le même espace $\Omega$ et $X$ une variable aléatoire également définie $\Omega$.
2. convergence ponctuelle
3. implique tous les autres.

## Convergence en probabilite
1. Meme cadre que precedemment
2. $\forall\varepsilon\gt0, \lim_{n\to+\infty}P(\vert X_n-X\vert\ge\varepsilon)=0$

## Convergence $L^2$
1. aussi appelee *convergence en moyenne quadratique* 
2. $\lim_{n\to+\infty}E(\vert X_n-X\vert)=0$
3. n'a de sens que pour les variables aléatoires telles que $E(X^2)\lt+\infty$
4. implique la convergence en probabilité,
5. n'a pas de lien avec la convergence presque sûre.

# Théorème Central Limite
## Théorème 4 (Loi forte des grands nombres)

Soit $(Xi)$ une suite de variables aléatoires i.i.d. (indépendantes et identiquement distribuées) telle que $E(\vert X_1\vert) < +\infty$.
Notons $m := E(X_1)$.

$$
\lim_{n\to+\infty}\bar X_n = m
$$

au sens de la convergence p.s. où $\bar X_n := \frac{X_1+...+X_n}{n}$

## Théorème 5 (T.C.L. cas unidimensionnel)
1. Soit $(X_i)$ une suite v.a. i.i.d.
2. Notons $m := E(X_i)$ et $\sigma^2 = V(Xi)$
3. $\frac{\sqrt{n}(\bar X_n - m)}{\sigma}$ converge en loi vers une loi normale centrée réduite.

## Cas multidimentionnel
1. Soit $(X_i)$ une suite de vecteurs aleatoires de $\mathbb R^p$ i.i.d.
2. Notons $m:=E(X_i)\in\mathbb R^p$ et $\Sigma$ la matrice de variances-covariances
3. $\sqrt{n}\biggr(\frac{1}{n}\sum_{i=1}^nX_i-m\biggr)$ converge en loi vers une loi normale multidimensionnelle $\mathcal N(0, \Sigma)$

# Premieres notions de statistique
## Echantillon de taille $n$
- Point de depart: v.a. $X$ dont l'ensemble des valeurs est note $\mathcal H$
- Donnee $n$ variables aleatoires i.i.d.
- A parti de l'echantillon, nous voudrons inferer la valeur d'un parametre (fini-dimensionnel) en estimation parametrique ou prendre une decision en decision statistique

## Modele statistique
- $\theta\in\mathbb R^d$
- $\Theta\subset\mathbb R^d$ ensemble des parametres
- $\mathcal P:=\{\mathbb P_{\theta}\vert\theta\in\Theta\}$ famille de lois indexees par $\Theta$
- **But:** estimer la valeur $\theta_0$ ou de $g(\theta_0)$

1. **Estimateur**: fonction (mesurable) $\hat\theta:\mathcal H^n\to\mathbb R^d$
2. Exemple pour le parametre $\lambda$ d'une loi $\mathcal P(\lambda)$
3. $\Theta=]0;+\infty[$
4. $\mathcal H=\mathbb N$

# Rappel
## Estimateur propose
1. $\hat\lambda:\mathcal H^n\to]0;+\infty[$
2. $\hat\lambda(x_1, ..., x_i):=\frac{1}{n}\sum_{i=1}^nx_i$
3. $\hat\lambda$ *moyenne empirique*

## Estimateur sans biais
1. $b(\hat\theta_n):=E(\hat\theta_n)-\theta$
2. dans l'exemple: $\hat\lambda_n$ est *sans biais*

*Pourquoi l'estimateur est-il sans biais ?*
Pour tout $i\in\{1,...,n\}$, $X_i\sim\mathcal P(\lambda)$.

$$
\begin{aligned}
E(X_i) &= \lambda\\
E(\hat \lambda) &= E(\frac{1}{n}\sum_{i=1}^nY_i)\\
&= \frac{1}{n}\sum_{i=1}^nE(X_i)\\
&= \frac{1}{n}\sum_{i=1}^n\lambda\\
&= \frac{1}{n}\times n\lambda = \lambda
\end{aligned}
$$

## Estimateur convergent
1. $\hat\theta_n$ convergent si $\hat\theta_n$ converge en probabilité vers $\theta$
2. $\hat\theta_n$ fortement convergent si $\hat\theta_n$ converge presque sûrement vers $\theta$

## Estimateurs de l'esperance et de la variance: cas general
- Pour l'esperance: $\bar X_n:=\frac{1}{n}\sum_{i=1}^nx_i$ a moyenne empirique
- Pour la variance: $S_n'^2:=\frac{1}{n}\sum_{i=1}^n(x_i-\bar x_n)^2$ qui est aussi égale à $\frac{1}{n}\sum_{i=1}^nx_i^2-\bar x_n^2$ la variance empirique
- $\bar X_n$ sans biais par contre $S_n'^2$ biaisé
- $S_n'^2$ parfois remplacé par $S_n^2=\frac{n}{n-1}S_n'^2$ qui est sans biais
- tous trois fortement convergents d'après la loi forte des grands nombres.

## Methode des moments
- Exploiter les moyennes et variances empiriques
- moyennes et variances sont remplaces par leurs contreparties empiriques
- fournit (en général) des estimateurs convergents du fait de la convergence des moyennes et variances empiriques
- Exemple de la loi exponentielle: $E(X)=\frac{1}{\lambda}$ donc $\lambda=\frac{1}{E(X)}$
- estimateur de $\lambda$ donné par la méthode des moments: $\hat\lambda=\frac{1}{\bar X_n}$
- $E(X^2)$ peut être remplacé par $\frac{1}{n}\sum_{i=1}^nx_i^2$ suivant le même principe
- les moments et moments centrés d'ordre supérieur peuvent être utilisés suivant le même principe
- Déterminer un autre estimateur donné par la méthode des moments pour la loi de Poisson.

# Methode du maximum de vraisemblance
## Principe
<div class="alert alert-info" role="alert" markdown="1">
Rechercher la valeur de $\theta$ en fonction des observations $x_1,...,x_n$ assurant la plus grande probabilité d'obtenir ces observations.
</div>

## Fonction de vraisemblance
1. $\mathcal H$ ensemble des valeurs que peut prendre la variable aléatoire $X$
2. pour la loi normale $\mathcal H=\mathbb R$
3. pour la loi normale $\mathcal H=\mathbb N$

<div class="alert alert-danger" role="alert" markdown="1">
1. loi depend de $\theta$ donc la densite associee aussi que nous noterons $f(x,\theta)$
2. Fonction de vraisembalnce

$$
L(x_1,...x_n,\theta):=\Pi_{i=1}^nf(x_i,\theta)
$$

</div>

## Maximum de vraisemblance
1. fonction $\hat \theta$ de $x_1,...,x_n$
2. Qui maximise $L$ i.e. telle que 
3. $L(x,\hat\theta)\ge L(x,\theta)$ pour tout $\theta\in\Theta$
4. où $\Theta$ est l'espace des paramètres

## Cas unidimensionnel
<div class="alert alert-info" role="alert" markdown="1">
Si $L$ est de classe $\mathcal C^2$ (i.e. deux fois  derivable par rapport $\theta$ et de derivee seconde continue), $\hat\theta$ est solution du systeme

$$
\begin{cases}
    \frac{\delta L}{\delta \theta} &= 0\\
    \frac{\delta^2 L}{\delta \theta^2} &\lt 0\\
\end{cases} (1)
$$
</div>

- La condition 1 est **nécessaire** et la condition 2 est **sufisante**.
- La condition 1 s'appelle *l'équation de vraisemblance*
- Pour simplifier les calculs, on peut remplacer la vraisemblance par la log-vraisemblance car la fonction logarithme est de classe $\mathcal C^2$ et strictement croissante sur $]0; +\infty[$.

<div class="alert alert-info" role="alert" markdown="1">
Ainsi $\hat\theta$ est solution du systeme:

$$
\begin{cases}
    \frac{\delta \log L}{\delta \theta} &= 0\\
    \frac{\delta^2 \log L}{\delta \theta^2} &\lt 0\\
\end{cases} (2)
$$
</div>
- La condition 1 est **nécessaire** et la condition 2 est **sufisante**.

## Logarithme
1. Particulierement utile car:
2. $\log(ab) = \log(a) + \log(b)$
3. $\log(\frac{a}{b}) = \log(a) - \log(b)$
4. $\log(a^x) = x\log(a)$

## Exemple de la loi exponentielle
1. $L(x,\lambda)=\Pi_{k=1}^n\lambda e^{-\lambda x_k} = \lambda^ne^{-\lambda}\sum_{k=1}^nx_k$
2. $\log(L(x,\lambda)) = n\log(\lambda) - \lambda\sum_{k=1}^nx_k$
3. $\log(\frac{\theta L}{\theta\lambda}(x,\lambda)) = \frac{n}{\lambda}-\sum_{k=1}x_k$
4. **Condition nécessaire** : $\hat\lambda(x)$ solution de : 

$$
\frac{n}{\lambda}-\sum_{k=1}x_k = 0\\
\hat\lambda(x) = \frac{n}{\sum_{k=1}^nx_k}
$$

<div class="alert alert-success" role="alert" markdown="1">
- **Condition sufisante**: $\frac{\delta^2\log L}{\delta\lambda^2}=-\frac{n}{\lambda^2}\lt0$
- La condition sufisante est satisfaite donc $\hat\lambda(x)$ est bien le maximum de vraisemblance.

</div>

## Estimateur du maximum de vraisemblance
1. $\hat\lambda_n = \frac{n}{\sum_{k=1}^n} = \frac{1}{\bar X_n}$
2. Il est *fortement convergent* d'apres la loi fort des grands nombres
