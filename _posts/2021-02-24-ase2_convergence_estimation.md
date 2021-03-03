---
title:          "ASE2: Convergence et estimation"
date:           2021-02-24 9:00
categories:     [tronc commun S8, ASE2]
tags:           [tronc commun, ASE2, S8]
description: Convergence et estimation
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/ByHzIFXfO)

# ASE2 : Convergence et estimation
# Introduction
<div class="alert alert-info" role="alert" markdown="1">
L'estimation: on va considerer une population qui obeit a une loi de probabilite avec un parametre $\theta$ inconnu.
</div>
L'objectif de l'estimation c'est estimer le parametre.

<div class="alert alert-success" role="alert" markdown="1">
On preleve un echantillon (suite de variables aleatoires independantes  $X_1$, $X_2$,..., $X_n$ suivant la meme loi que la population $X$) dans cette population, on va construire un **estimateur** destine a **converger** vers le parametre $\theta$.
</div>
<div class="alert alert-info" role="alert" markdown="1">
Un estimateur est une **fonction** $T = f(X_1, X_2, ..., X_n)$ de notre echantillon.
</div>

Qualites de l'estimateur:
1. Etre convergent
2. Etre precis
    - Plus la variance est minimale, plus on a un estimateur precis
3. Etre efficace

Pour etudier la convergeance, on va voir 3 types:
1. Convergence en proba
2. Convergence quadratique
3. Convergence discrete

# Rappels de la loi Gamma et la loi Normale
<div class="alert alert-info" role="alert" markdown="1">
On dit qu'une variable aleatoire positive $X$ suit une loi gamma de parametre r, notee $\gamma_r$ si sa densite est donnee par 
$$
f(x) = \frac{1}{\Gamma(r)}\exp(-x)x^{\gamma - 1}
$$
Avec $\Gamma(x) = \int^{+\infty}_0\exp(-t)t^{x-1}dt$ (fonction Gamma) definie pour $x\gt 0$
</div>

## Propriete de la fonction Gamma
1. $\Gamma(x+1)=x\Gamma(x)$ (integration par partie)
2. $\Gamma(1)=1$
3. $\Gamma(n+1)=n!$
4. $\Gamma(k+\frac{1}{2}) = \frac{1.3.5.....(2k -1)}{2^k}\Gamma(\frac{1}{2})$
5. $\Gamma(\frac{1}{2}) = \sqrt{\pi}$

Esperance de la loi $\gamma_r$: soit $X$ une variable aleatoire suivant la loi gamma de parametre r.
On a:
$$
E(x)=\frac{1}{\Gamma}\int^{+\infty}_0 t^T\exp(-t)dt = \frac{\Gamma(r+1)}{\Gamma(r)} = r
$$

Variance de la loi $\gamma_r : V(X) = E(X^2) - E^2(X)$
$$
E(X^2) = \frac{1}{\Gamma(r)}\int^{+\infty}_0 t^2\exp(-t) t^{r-1}dt = \frac{1}{\Gamma(r)}t^{r+1}\exp(-t)dt = \frac{\Gamma(r+2)}{\Gamma(r)} = r(r + 1)
$$
Donc $V(X) = r(r + 1) - r^2 = r$

## Loi Normale de parametre $(m, \sigma)$
On dit qu'une variable aleatoire $X$ suit la loi normale notee $N(m, \sigma)$ si sa densite est $f(x)=\frac{1}{\sigma\sqrt{1\pi}}\exp(-\frac{1}{2}(\frac{x-m}{\sigma})^2)$
ou:
- $m=E(X)$
- $\sigma=\sqrt{V(X)}$ (ecart-type)

Avec le changement de variable $U=\frac{X-m}{\sigma}$ (variable normale centree reduite), la densite de $U$ est $f(u) = \frac{1}{\sqrt{2\pi}}\exp(-\frac{1}{2}u^2)$.

### Montrons que $V(U) = 1$
On a $V(U) = E(U^2) = \int_{-\infty}^{+\infty}\frac{1}{\sqrt{2\pi}}u^2\exp(-\frac{1}{2}u^2)du = \frac{2}{\sqrt{2\pi}}\int^{+\infty}_{0}u^2\exp(-\frac{1}{2}u^2)du$.
Posons:
- $t = \frac{u^2}{2}$
- ut = udu

$$
\begin{aligned}
V(U) &= \frac{2}{\sqrt{2\pi}}\int^{+\infty}_{0}2t\exp(-t)\frac{dt}{\sqrt{2t}}\\
&= \frac{2}{\sqrt{\pi}}\int^{+\infty}_{0}t^{\frac{1}{2}}\exp(-t)dt\\
&= \frac{2}{\sqrt{\pi}}\Gamma(\frac{3}{2})\\
&= \frac{2}{\sqrt{\pi}}\frac{1}{2}\Gamma(\frac{1}{2})
\end{aligned}
$$
Donc $V(U) = \frac{1}{\sqrt{\pi}}\sqrt{\pi} = 1$

## Moments de la loi normale centree reduite
Soit $U$ une variable normale centree reduite, on appelle moment d'ordre $k$ de $U$: $u_k = E(U^k)$
- Si $k = 2p + 1$ alors $u_{2p+1} = 0$ (car fonction impaire)
- Si $k = 2p$ alors $u_{2p} = \frac{1}{\sqrt{2\pi}}\int^{+\infty}_{-\infty}u^{2p}\exp(-\frac{1}{2}u^2)du = \frac{2}{\sqrt{2\pi}}\int^{+\infty}_{0}u^{2p}\exp(-\frac{1}{2}u^2)du$

Posons:
- $t= \frac{u^2}{2}$
- $dt=udu$

$$
\begin{aligned}
u_{2p} &= \frac{2}{\sqrt{2\pi}}\int^{+\infty}_0(2t)^p\exp(-t)\frac{dt}{\sqrt{2\pi}}\\
&=\frac{2^p}{\sqrt{\pi}}\int^{+\infty}_0t^{p-\frac{1}{2}}\exp(-t)dt\\
&=\frac{2^p}{\sqrt{\pi}}\Gamma(p + \frac{1}{2})
\end{aligned}
$$
Or $\Gamma(p+\frac{1}{2})=\frac{1.3.5...(2p-1)}{2^p}$ et $\Gamma(\frac{1}{2}) = \sqrt{\pi}$
Donc $u_{2p}=1.3.5.....(2p-1) = \frac{(2p)!}{2^pp!}$

# Fonctions caracteristiques
## Definition
<div class="alert alert-info" role="alert" markdown="1">
la fonction caractéristique d’une variable aléatoire réelle $X$ est la transformée de Fourier de sa loi de probabilité. elle est notée $\phi_x(t)$ et on a $\phi_xE(\exp(itX))$ ($i$ complexe)
</div>
Si $X$ est une variable a densite ($X$ est une VA continue de densite $f$) alors:
$$
\phi_X(t)=\int_{\mathbb R}\exp(itx)f(x)dx
$$
Si $X$ est une variable discrète alors sa fonction caractéristique est:
$$
\phi_X(t) = \sum_k\exp(itk)P(X = k)
$$

## Proprietes
1. $\phi_{\lambda X} = \phi_X(\lambda t)$ $\forall \lambda$ un scalaire
2. $\phi_{X+a}(t) = \exp(ita)\pi_X(t)$
3. Si $X$ est une variable aleatoire d'esperance et d'ecrat-type $\sigma$ et $U = \frac{X-m}{\sigma}$
$$
\phi_{\frac{X-m}{\sigma}}(t) = \phi_U(T) = \exp(-\frac{itm}{\sigma})\phi_X(\frac{1}{\sigma})
$$

## Remarque
la fonction caractéristique se prête bien aux additions de variables aléatoires indépendantes :
Si $X$ et $Y$ sont deux variables aléatoires indépendantes alors 
$$
\phi_{X+Y}(t)=\phi_X(t)\phi_Y(t)
$$
En effet $\phi_{X+Y}(t) = E(\exp(it(X+Y))) = E(\exp(itX)\exp(itY))$
Or $X$ et $Y$ sont indépendantes $E(\exp(itX)\exp(itY)) = E(\exp(itX))E(\exp(itY))$
Donc $\phi_{X+Y}(t) = \phi_X(t)\phi_Y(t)$

## Proposition
Soit $X$ une variable aléatoire de fonction de répartition $\phi_X(t)$.
On a:
- $\phi_X(0) = 1$
- $\frac{d^k\phi_X}{dt^k}(0) = \phi_X^{(k)}(0) = t^kE(X^k)$

### Demo
Supposons que $X$ est une variable continue de densité $f$
On a $\phi_X(t)=\int_{\mathbb R}\exp(itx)f(x)\Rightarrow\phi_X(0) = \int_{\mathbb R}f(x)dx=1$ (car $f$ est une densité)
En derivant $\phi_X(t)$ par rapport a t: $\phi_x'(t)=i\int_{\mathbb R}x\exp(itx)f(x)dx$
- Si $t=0$, $\phi_X'(0) = i\int_{\mathbb R}xf(x)dx=iE(X)$

Si on dérive 2 fois, $\phi_X^{(2)}(t)=\int_{\mathbb R}(ix)^2\exp(itx)f(x)dx$
- Pour $t = 0$, $\phi_X^{(2)}(0) = (i)^2\int_{\mathbb R}x^2f(x)dx = -\int_{\mathbb R}x^2f(x)dx=-E(X^2)$

En dérivant $k$ fois par rapport à $t$: $\phi_x^{(k)}(t)=\int_{\mathbb R}(ix)^k\exp(itx)f(x)dx$
- $\phi_X^{(k)}(0) = (i^k)\int_{\mathbb R}x^kf(x)dx = i^kE(X^k)$ $\forall k\in\mathbb N$

## Formule de Mac-Laurin
<div class="alert alert-info" role="alert" markdown="1">
Si $\phi_X(t)$ est indéfiniment dérivable on a:
$$
\phi_x(t) = \sum^{+\infty}_{k=0}\frac{t^k}{k!}i^kE(X^k)
$$
</div>

### Exemple 1
Soit X une variable aléatoire continue de densité:
$$
\begin{cases}
    f(x) = \exp(-x) &\text{si } x\gt0\\
    f(x) = 0 &\text{sinon}
\end{cases}
$$
Determiner la fonction caracteristique de $X$

<details markdown="1">
<summary>Solution</summary>
On a 
$$
\begin{aligned}
\phi_X(t)&=\int_{\mathbb R}\exp(itx)f(x)dx=\int_{0}^{+\infty}\exp(itx)\exp(-x)dx = \int_{0}^{+\infty}\exp(-(1-it)x)dx\\
&= \int_{0}^{+\infty}\exp(-(1-it)x)dx = \biggr[\frac{-\exp(-(1-it)x)}{(1-it)}\biggr]^{+\infty}_{0} = \frac{1}{1-it}
\end{aligned}
$$

car $\exp(-(1-it)x) = \exp(-x)\exp(itx)\to 0$ lorsque $x\to +\infty$
Puisque $\exp(itx)$ est bornee de module 1 et $\exp(-x)\to 0$ quand $x\to +\infty$
</details>

### Exemple 2
Déterminer la fonction caractéristique de la loi de Bernoulli de paramètre $p$

<details markdown="1">
<summary>Solution</summary>
Soit X une variable de Bernoulli : 
- $X=1$ avec la probabilite $p$
- $X=0$ avec la probabilité $1-p$

$X$ étant discrète, donc sa fonction caractéristique est:
$$
\phi_X(t)\sum_k\exp(itk)P(X=k) = \sum_{k=0}^1\exp(itk)P(X=k)=P(X=0)+\exp(it)P(X=1)\\
\phi_X(t) = 1 - p + p\exp(it) = q + p\exp(it) \text{avec } q =1 - p
$$
</details>

# Convergence des suites de variables aleatoires
<div class="alert alert-info" role="alert" markdown="1">
Une suite $X_n$ de variables aléatoires étant une suite de fonctions il existe diverses façons de définir la convergence de $X_n$ dont certaines jouent un grand rôle en statistiques.
</div>

## Convergence en probabilite
### Definition
<div class="alert alert-info" role="alert" markdown="1">
La suite $X_n$ converge en probabilité vers une variable aléatoire $X$
Si $\forall\varepsilon\gt0, \eta\gt 0$ ( arbitrairement petits) il existe un entier $n_0$ tel que
$$
\forall n\gt n_o \Rightarrow P(\vert X_n-X\vert\gt\varepsilon)\lt\eta
$$
C’est-à-dire $P(\vert X_n-X\vert\gt\varepsilon)\to_{n\to+\infty}0$
</div>
<div class="alert alert-warning" role="alert" markdown="1">
On notera $(X_n)\to^PX$
</div>

<div class="alert alert-danger" role="alert" markdown="1">
Inégalité de Bienaymé-Tchebychev:
$$
P(\vert X - E(X)\vert\gt\varepsilon)\lt\frac{V(X)}{\varepsilon^2} \forall\varepsilon\gt 0
$$
</div>

### Remarque
Lorsque $E(X_n)\to_{n\to+\infty}0$, il suffit de montrer que $V(X_n)\to_{n\to+\infty} 0$ pour établir la convergence en probabilité de la suite $(X_n)$ vers a.

En effet d’après Tchebychev:
$$
P(\vert X_n-E(X_n)\vert\gt\varepsilon)\lt\frac{V(X_n)}{\varepsilon^2}\to 0
$$
Donc en passant a la limite:
$$
\lim_{n\to+\infty}P(\vert X_n - a\vert\gt\varepsilon) = 0\\ \forall\varepsilon\gt0
$$

## Convergence en moyenne quadratique
On suppose que $E(\vert X_n-X\vert^2)$ existe.

### Definition
<div class="alert alert-info" role="alert" markdown="1">
On dit qu’une suite de variables aléatoires $(X_n)$ converge en moyenne quadratique vers une variable X si 
$$
E(\vert X_n-X\vert^2)\to_{n\to+\infty}
$$
</div>
<div class="alert alert-warning" role="alert" markdown="1">
On notera $(X_n)\to^{m.q}X$
</div>

## Convergence en loi
### Definition
<div class="alert alert-info" role="alert" markdown="1">
La suite $(X_n)$ converge en loi vers la variable $X$ de fonction de répartition $F$ si en tout point de continuité de $F$ la suite $(F_n)$ des fonctions de répartition des $(X_n)$ converge vers $F$, c’est-à-dire $\lim_{n\to+\infty}F_n(x)=F(x)$ pour tout x point de continuité de F
</div>
<div class="alert alert-warning" role="alert" markdown="1">
On noter $X_n\to^LX$
</div>

### Remarque
Pour les variables discrètes, la convergence en loi est équivalente à
$$
\lim_{n\to+\infty}P(X_n=k) = P(X=k)
$$

### Theoreme
Si la suite des fonctions caractéristiques $\phi_{x_n}(T)$ converge vers $\phi_X(t)$ alors $(X_n)\to^LX$

# Applications - Convergence en loi de la binomiale vers la loi Normale
## Théorème (Moivre-laplace)
<div class="alert alert-danger" role="alert" markdown="1">
Soit $(X_n)$ une suite de variables binomiales $B(n,p)$
Alors $\frac{X_n - np}{\sqrt{npq}}\to^LN(0,1)$ lorsque $n\to+\infty$
</div>

## Demonstration
La fonction caractéristique de la loi $B(n,p)$ est:
$$
\begin{aligned}
    \phi_{X_n}(t) &= (p\exp(it)+1-p)^n \text{ donc celle de } Y_n=\frac{X_n-np}{\sqrt{npq}} \text{ est:}\\
    \phi_{Y_n} &=(p\exp(\frac{it}{\sqrt{npq}})+1-p)^n\exp(-\frac{itnp}{\sqrt{npq}})\\
    Ln(\phi_{Y_n}(t)) &= nLn(p(\exp(\frac{it}{\sqrt{npq}})-1)+1) - \frac{itnp}{\sqrt{npq}}
\end{aligned}
$$
On rappelle le développement limité de l’exponentielle à l’ordre 2: $\exp(x) \approx 1+x+\frac{x^2}{2}$ (au voisinage de 0)
$$
Ln(\phi_{Y_n}(t)) \approx nLn(p(\frac{it}{\sqrt{npq}} - \frac{t^2}{2npq})+1)-\frac{itnp}{\sqrt{npq}}
$$
On rappelle $Ln(1+x)\approx x - \frac{x^2}{2}$ (au voisinage de 0)
Donc:
$$
\begin{aligned}
Ln(\phi_{Y_n}(t))&\approx n[\frac{pit}{\sqrt{npq}}-\frac{pt^2}{2npq}+\frac{p^2t^2}{2npq}]-\frac{itnp}{\sqrt{npq}}\\
&\approx -\frac{t^2}{2q} + \frac{pt^2}{2q} = \frac{t^2}{2q}(p-1)=-\frac{t^2}{2}
\end{aligned}
$$
En composant par l’exponentielle:
$$
Ln(\phi_{Y_n}(t))\approx\exp(-\frac{t^2}{2}) \text{ caractéristique de la loi normale } N(0,1)
$$
Conclusion: $\frac{X_n-np}{\sqrt{npq}}\to^LN(0,1)$

## Remarque
<div class="alert alert-warning" role="alert" markdown="1">
Lorsque $n$ est assez grand on peut donc approximer la loi Binomiale par la loi normale. On donne généralement comme  condition $np$ et $nq\gt5$
</div>
Il convient cependant d’effectuer la correction de continuité : on obtient donc une valeur approchée de $P(X=x)$ par la surface sous la courbe de densité de la loi normale $N(np,\sqrt{npq})$ comprise entre les droites d’abscisse $x-\frac{1}{2}$ et $x+\frac{1}{2}$
$$
P(X=x)\approx P(x-\frac{1}{2}\lt X\lt x+\frac{1}{2}) = P(\frac{x-\frac{1}{2}-np}{\sqrt{npq}}\lt\frac{X-np}{\sqrt{npq}}\lt\frac{x+\frac{1}{2}-np}{\sqrt{npq}})
$$
Et $P(X\le x)\approx P(\frac{X-np}{\sqrt{npq}}\lt\frac{x+\frac{1}{2}-np}{\sqrt{npq}})$
