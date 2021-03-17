---
title:          "ASE2: Convergence et estimation"
date:           2021-03-10 9:30
categories:     [tronc commun S8, ASE2]
tags:           [tronc commun, ASE2, S8]
description: Convergence et estimation
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/HJjhGXImd)

# Introduction
Le problème central de l’estimation en statistique est le suivant : disposant d’observations sur un échantillon de taille $n$ on souhaite en déduire les propriétés de la population dont il est issu. 

On cherchera à estimer, par exemple, la moyenne d’une population à partir de la moyenne d’un échantillon. Le mode de tirage le plus important est l’échantillonnage aléatoire simple correspondant à des tirages  équiprobables et indépendants les uns des autres.

L’une des premières qualités d’un estimateur est d’être convergent en probabilité vers le paramètre à estimer. Un échantillon de $X$ est une suite de variables aléatoires $(X_1,X_2,...,X_n)$ indépendantes et de même loi que $X$. Un estimateur d’un paramètre $\theta$ inconnu est une fonction  qui dépend de l’échantillon et donc  doit converger en probabilité vers le paramètre $\theta$. La précision d’un estimateur sera mesuré par sa variance.

# Rappels de la loi Gamma et la loi Normale
<div class="alert alert-info" role="alert" markdown="1">
On dit qu’une variable aléatoire positive $X$ suit une loi gamma de paramètre $r$, notée $\gamma_r$ si sa densité est donnée par : 

$$
f(x) = \frac{1}{\Gamma(r)}e^{-x}x^{r -1}
$$

Avec $\Gamma(x) = \int_0^{+\infty}e^{-t}t^{x-1}dt$ (fonction Gamma) definie pour $x\gt0$

</div>

## Propriétés de la fonction Gamma
1. $\Gamma(x+1)=x\Gamma(x)$ (intégration par partie)
2. $\Gamma(1) = 1$
3. $\Gamma(n+1)=n!$
4. $\Gamma(k+\frac{1}{2})=\frac{1.3.5.....(2k-1)}{2^k}\Gamma(\frac{1}{2})$
5. $\Gamma(\frac{1}{2}) = \sqrt{\pi}$

Espérance de la loi $\gamma_r$ : Soit $X$ une variable aléatoire suivant la loi gamma de paramètre $r$.
$$
E(X)=\frac{1}{\Gamma(r)}\int_0^{+\infty}te^{-t}t^{r-1}dt=\frac{1}{\Gamma(r)}\int_0^{+\infty}t^{r}e^{-t}dt=\frac{\Gamma(r+1)}{\Gamma(r)}=r
$$

Variance de la loi $\gamma_r$ : $V(X) = E(X^2)-E^2(X)$

$$
E(X^2)=\frac{1}{\Gamma(r)}\int_0^{+\infty}t^2e^{-t}t^{r-1}=\frac{1}{\Gamma(r)}\int_0^{+\infty}t^{r+1}e^{-t}dt = \frac{\Gamma(r+2)}{\Gamma(r)} = r(r+1)
$$

Donc $V(X) = r(r+1)-r^2 =r$.

## Loi Normale de paramètres$(m,\sigma)$

<div class="alert alert-info" role="alert" markdown="1">
On dit qu’une variable aléatoire $X$ suit la loi normale notée $\mathcal N(m,\sigma)$ si sa densité est

$$
f(x)=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{1}{2}(\frac{x-m}{\sigma})^2}
$$

où:
- $m = E(X)$
- $\sigma = \sqrt{V(X)}$ (écart type)

</div>
Avec le changement de variable $U=\frac{X-m}{\sigma}$ (variable normale centrée réduite), la densité de $U$ est:

$$
f(u) = \frac{1}{\sqrt{2\pi}}e^{-\frac{1}{2}u^2}
$$

### Demonstration
Montrons que $V(U) = 1$.

On a:
$$
V(U) = E(U^2) = \int_{-\infty}^{+\infty}\frac{1}{\sqrt{2\pi}}u^2e^{-\frac{1}{2}u^2}du = \frac{2}{\sqrt{2\pi}}\int_0^{+\infty}u^2e^{-\frac{1}{2}u^2}du
$$

Posons $t=\frac{u^2}{2}$, $dt = udu$

$$
V(U) = \frac{2}{\sqrt{2\pi}}\int_0^{+\infty}2te^{-t}\frac{dt}{\sqrt{2t}} = \frac{2}{\sqrt{\pi}}\Gamma(\frac{3}{2})=\frac{2}{\sqrt{\pi}}\frac{1}{2}\Gamma(\frac{1}{2})
$$
Donc $V(U) = \frac{1}{\sqrt{\pi}}\sqrt{\pi}=1$

## Moments de la loi normale centrée réduite
Soit $U$ une variable normale centrée réduite, on appelle moment d’ordre $k$ de $U$ : $u_k=E(U^k)$
- Si $k=2p+1$ alors $u_{2p+1} = 0$ (car fonction impaire)
- Si $k=2p$ alors $u_{2p} = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{+\infty}u^{2p}e^{-\frac{1}{2}u^2}du = \frac{2}{\sqrt{2\pi}}\int_0^{+\infty}u^{2p}e^{\frac{1}{2}u^2}du$

Posons $t=\frac{u^2}{2}$, $dt=udu$

$$
u_{2p} = \frac{2}{\sqrt{2\pi}}\int_0^{+\infty}(2t)^pe^{-t}\frac{dt}{\sqrt{2t}}=\frac{2^p}{\sqrt{\pi}}\int_0^{+\infty}t^{p-\frac{1}{2}}e^{-t}dt = \frac{2^p}{\sqrt{\pi}}\Gamma(p+\frac{1}{2})\\
\text{Or } \Gamma(p+\frac{1}{2}) = \frac{1.3.5...(2p-1)}{2^p}\Gamma(\frac{1}{2}) \text{ et } \Gamma(\frac{1}{2})=\sqrt{\pi}\\
\text{Donc } u_{2p}=1.3.5....(2p-1)=\frac{(2p)!}{2^pp!}
$$

# Fonctions caractéristiques

<div class="alert alert-info" role="alert" markdown="1">
**Definition**: la fonction caractéristique d’une variable aléatoire réelle $X$ est la transformée de Fourier de sa loi de probabilité. Elle est notée $\phi_X(t)$ et on a:
$$
\phi_X(t)=E(e^{itX}) \text{ (} i \text{ complexe)}
$$
</div>

Si $X$ est une variable à densité ($X$ est une v.a continue de densité $f$) alors : 
$$
\phi_X(t) = \int_{\mathbb R}e^{itx}f(x)dx
$$

Si $X$ est une variable discrète alors sa fonction caractéristique est : 
$$
\phi_X(t)=\sum_ke^{itk}P(X=k)
$$

## Propriétés
1. $\phi_{\lambda x} = \phi_X(\lambda t)$, $\forall\lambda$ un scalaire
2. $\phi_{X+a}(t)=e^{ita}\phi_X(t)$, $\forall a$ un scalaire
3. Si $X$ est une variable aléatoire d’espérance $m$ et d’écart type $\sigma$ et $U = \frac{X-m}{\sigma}$

$$
\phi_{\frac{X-m}{\sigma}} = \phi_U(t) = e^{-\frac{itm}{\sigma}}\phi_X(\frac{t}{\sigma})
$$

### Remarque
La fonction caractéristique se prête bien aux additions de variables aléatoires indépendantes.

Si $X$ et $Y$ sont deux variables aléatoires indépendantes alors 
$$
\phi_{X+Y}(t) = \phi_X(t)\phi_Y(t)\\
\text{En effet } \phi_{X+Y}(t) = E(e^{it(X+Y)})=E(e^{itX}e^{itY})\\
\text{Or } X \text{ et } Y \text{ sont indépendantes } E(e^{itX}e^{itY}) = E(e^{itX})E(e^{itY})\\
\text{Donc } \phi_{X+Y}(t)=\phi_X(t)+\phi_Y(t)
$$

## Proposition
Soit $X$ une variable aléatoire de fonction de répartition $\phi_X(t)$.

On a $\phi_x(0)=1$ et $\frac{d^k\phi_X}{dt^k}(0)=\phi_X^{(k)}(0)=t^kE(X^k)$

### Démo
Supposons que $X$ est une variable continue de densité $f$

On a:

$$
\phi_X(t)=\int_{\mathbb R}e^{itx}f(x)dx\Rightarrow\phi_X(0)=\int_{\mathbb R}f(x)dx=1 \text{ (car f est une densité)}\\
\text{En dérivant } \phi_X(t) \text{ par rapport à t: } \phi_X'(t)=i\int_{\mathbb R}xe^{itx}f(x)dx\\
\text{Si } t=0: \phi_X'(t)i\int_{\mathbb R}xf(x)dx=iE(x)\\
\text{Si on dérive 2 fois, } \phi_X^{(2)}(t)=\int_{\mathbb R}(itx)^2e^{itx}f(x)dx\\
\text{En dérivant k fois par rapport à t: }\phi_X(t)^{k}(t)=\int_{\mathbb R}(ix)^ke^{itx}f(x)dx\\
\text{Donc } \phi_x^{(k)}(0)=(i^k)\int_{\mathbb R}x^kf(x)dx=i^kE(X^k),\forall k\in\mathbb N
$$

## Formule de Mac-Laurin
Si $\phi_X(t)$ est indéfiniment dérivable on a:

$$
\phi_X(t)=\sum_{k=0}^{+\infty}\frac{t^k}{k!}\phi_X^{(k)}(0)=\sum_{k=0}^{+\infty}\frac{t^k}{k!}i^kE(X^k)
$$

### Exemple 1
Soit X une variable aléatoire continue de densité: 

$$
f(x)=
\begin{cases}
    e^{-x} &\text{si } x\gt0\\
    0 &\text{sinon}
\end{cases}
$$

Déterminer la fonction caractéristique de $X$

<details markdown="1">
<summary>Solution</summary>

$$
\begin{aligned}
\phi_X(t) &= \int_{\mathbb R}e^{itx}f(x)dx=\int_{-\infty}^{+\infty}e^{itx}e^{-x}dx=\int_{0}^{+\infty}e^{-(1-it)x}dx\\
&= \int_{0}^{+\infty}e^{-(1-it)x}dx=\biggr[\frac{-e^{-(1-it)x}}{1-it}\biggr]_0^{+\infty}=\frac{1}{1-it}
\end{aligned}
$$

Car $-e^{-(1-it)x}=e^{-x}e^{itx}\to0$ lorsque $x\to+\infty$.

Puisque $e^{itx}$ est bornée de module 1 et $e^{-x}\to0$ quand $x\to+\infty$
</details>

### Exemple 2
Déterminer la fonction caractéristique de la loi de Bernoulli de paramètre $p$


<details markdown="1">
<summary>Solution</summary>

Soit $X$ une variable de Bernoulli 

$$
\begin{cases}
X=1 &\text{avec la probabilité }p\\
X=0 &\text{avec la probabilité }1-p
\end{cases}
$$

X étant discrète, donc sa fonction caractéristique est:

$$
\begin{aligned}
\phi_X(t)&=\sum_ke^{itk}P(X=k)=\sum_{k=0}^1e^{itk}P(X=k)=P(X=0)+e^{it}P(X=1)\\
&= 1-p+pe^{it}=q+pe^{it} \text{ avec } q=1-p
\end{aligned}
$$

</details>

# Convergences des suites de variables aléatoires

Une suite $(X_n)$ de variables aléatoires étant une suite de fonctions il existe diverses façons de définir la convergence de $(X_n)$ dont certaines jouent un grand rôle en statistiques.

## Convergence en probabilité
<div class="alert alert-info" role="alert" markdown="1">
**Definition**
La suite $(X_n)$ converge en probabilité vers une variable aléatoire $X$ si $\forall\varepsilon\gt0, \eta\gt0$ (arbitrairement petits) il existe un entier $n_0$ tel que $\forall n\gt n_0\Rightarrow P(\vert X_n-X\vert\gt\varepsilon)\to_{n\to+\infty}0$, c’est-à-dire $P(\vert X_n-X\vert\gt\varepsilon)\to_{n\to+\infty}0$.

On notera $(X_n)\to^PX$.
</div>

### Inégalité de Bienaymé-Tchebychev
<div class="alert alert-danger" role="alert" markdown="1">

$$
P(\vert X_n-E(X)\vert\gt\varepsilon)\lt\frac{V(X)}{\varepsilon^2},\forall\varepsilon\gt0
$$

</div>

### Remarque
Lorsque $E(X_n)\to_{n\to+\infty}a$, il suffit de montrer que $V(X_n)\to_{n\to+\infty}0$ pour établir la convergence en probabilité de la suite $(X_n)$ vers $a$.

En effet d’après Tchebychev: $P(\vert X_n-E(X_n)\vert\gt\varepsilon)\lt\frac{V(X)}{\varepsilon^2}\to0$\\
Donc en passant à la limite $\lim_{n\to+\infty}P(\vert X_n-a\vert\gt\varepsilon)=0,\forall\varepsilon\gt0$

## Convergence en moyenne quadratique
On suppose que $E(\vert X_n-X\vert^2)$ existe

<div class="alert alert-info" role="alert" markdown="1">
**Definition**
On dit qu’une suite de variables aléatoires $(X_n)$ converge en moyenne quadratique vers une variable $X$ si $E(\vert X_n-X\vert^2)\to_{n\to+\infty}0$

On notera $(X_n)\to^{m.q}X$
</div>

## Convergence en loi 
<div class="alert alert-info" role="alert" markdown="1">
**Definition**
La suite $(X_n)$ converge en loi vers la variable $X$ de fonction de répartition $F$ si en tout point de continuité de $F$ la suite $(X_n)$ des   fonctions de répartition des $(X_n)$ converge vers $F$.

C’est-à-dire $\lim_{n\to+\infty}F_n(x)=F(x)$ pour tout $x$ point de continuité de $F$.

On notera $(X_n)\to^LX$
</div>

### Remarque
Pour les variables discrètes, la convergence en loi est équivalente à

$$
\lim_{n\to+\infty}P(X_n=k)=P(X=k)
$$

### Théorème
<div class="alert alert-warning" role="alert" markdown="1">
Si la suite des fonctions caractéristiques $\phi_{X_n}(t)$ converge vers $\phi_X(t)$ alors $(X_n)\to^LX$
</div>

# Applications: Convergence en loi de la binomiale vers la loi Normale
## Théorème (Moivre-laplace)
<div class="alert alert-danger" role="alert" markdown="1">
Soit $(X_n)$ une suite de variables binomiales $\mathcal B(n,p)$ alors

$$
\frac{X_n-np}{\sqrt{npq}}\to^L\mathcal N(0,1) \text{ lorsque } n\to+\infty
$$

</div>

### Démonstration
La fonction caractéristique de la loi $\mathcal B(n,p)$ est:

$$
\phi_{X_n}(t)=(pe^{it}+1-p)^n \text{ donc celle de } Y_n=\frac{X_n-np}{\sqrt{npq}} \text{ est:}\\
\phi_{Y_n}(t) = (pe^{\frac{it}{\sqrt{npq}}}+1-p)^ne^{\frac{-itnp}{\sqrt{npq}}}\\
\ln(\phi_{Y_n}(t))=nLn(p(e^{\frac{it}{\sqrt{npq}}}-1)+1)-\frac{itnp}{\sqrt{npq}}
$$

On rappelle le développement limité de l’exponentielle à l’ordre 2

$$
e^x\simeq1+x+\frac{x^2}{2} \text{(au voisinage de 0)}\\
\ln(\phi_{Y_n}(t))\simeq n\ln(p(\frac{it}{\sqrt{npq}}-\frac{t^2}{2npq})+1)-\frac{itnp}{\sqrt{npq}}
$$

On rappelle $\ln(1+x)\simeq x-\frac{x^2}{2}$ (au voisinage de 0)

Donc:
$$
\begin{aligned}
\ln(\phi_{Y_n}(t))&\simeq n\biggr[\frac{pit}{\sqrt{npq}}-\frac{pt^2}{2npq}+\frac{p^2t^2}{2npq}\biggr]-\frac{itnp}{\sqrt{npq}}\\
&\simeq-\frac{t^2}{2q}+\frac{pt^2}{2q}=\frac{t^2}{2q}(p-1)=-\frac{t^2}{2}
\end{aligned}
$$

En composant par l’exponentielle:

<div class="alert alert-success" role="alert" markdown="1">
$$
\phi_{Y_n}(t)\simeq e^{-\frac{t^2}{2}}
$$

fonction caractéristique de la loi normale $\mathcal N(0,1)$
</div>

Conclusion $\frac{X_n-np}{\sqrt{npq}}\to^L\mathcal N(0,1)$

### Remarque
lorsque n est assez grand on peut donc approximer la loi Binomiale par la loi normale. On donne généralement comme condition $np$ et $nq\gt5$.

Il convient cependant  d’effectuer la correction de continuité : on obtient donc une valeur approchée de $P(X=x)$ par la surface sous la courbe de densité de la loi normale $\mathcal N(np,\sqrt{npq})$ comprise entre les droites d’abscisse $x-\frac{1}{2}$ et $x+\frac{1}{2}$

$$
P(X=x)\simeq P(x-\frac{1}{2}\lt X\lt x+\frac{1}{2})=P\biggr(\frac{x-\frac{1}{2}-np}{\sqrt{npq}}\lt \frac{X-np}{\sqrt{npq}}\lt \frac{x+\frac{1}{2}-np}{\sqrt{npq}}\biggr)\\
\text{Et } P(X\lt x)\simeq P\biggr(\frac{X-np}{\sqrt{npq}}\lt \frac{x+\frac{1}{2}-np}{\sqrt{npq}}\biggr)
$$

### Exemple
Soit X une variable binomiale $\mathcal B(n=40; p=0,3)$.

La valeur exacte pour $P(X=11)$ est $0,1319$.
La formule d’approximation : 
$$
P(X=11)\simeq P\biggr(\frac{11-\frac{1}{2}-12}{\sqrt{8,4}}\lt \frac{X-12}{\sqrt{8,4}}\lt \frac{11+\frac{1}{2}-12}{\sqrt{8,4}}\biggr)=P(-0,52\lt U\le-0,17)=0,131
$$

Avec $np=12$ et $npq=8,4$

Donc l’erreur est de moins de $1\%$

## Convergence en loi de la loi de Poisson vers la loi normale

<div class="alert alert-warning" role="alert" markdown="1">
**Theoreme**
Soit $(X_{\lambda})$ une suite de variables de Poisson de paramètre $\lambda$.

Si $\lambda\to+\infty$, $\frac{X_{\lambda}-\lambda}{\sqrt{\lambda}}\to^L\mathcal N(0,1)$
</div>

### Démonstration
on rappelle la fonction caractéristique de la loi de Poisson:

$$
\phi_{X_i}(t)=e^{\lambda e^{it}-\lambda}
$$

On rappelle aussi la formule $\phi_{\frac{X-m}{\sigma}}=e^{-\frac{it\lambda}{\sqrt{\lambda}}+\lambda+\frac{\lambda it}{\sqrt{\lambda}}-\frac{t^2}{2}-\lambda}=e^{-\frac{t^2}{2}}$

<div class="alert alert-success" role="alert" markdown="1">
On retrouve la fonction caractéristique de la loi normale centrée et réduite. 
</div>

Conclusion $\frac{X_{\lambda}-\lambda}{\sqrt{\lambda}}\to^L\mathcal N(0,1)$

## Théorème (Central-limite)
<div class="alert alert-danger" role="alert" markdown="1">
Soit $(X_n)$ une suite de variables aléatoires, indépendantes et de même loi d’espérance $m$ et d’écart-type $\sigma$ alors :

$$
\frac{X_1+X_2+....+X_n-nm}{\sigma\sqrt n}\to\mathcal N(0,1)
$$

</div>

### Démonstration

$$
\frac{X_1+X_2+....+X_n-nm}{\sigma\sqrt n}\to\mathcal N(0,1) = \sum_{i=1}^n\frac{X_i-m}{\sigma\sqrt n}
$$

Posons $Y_n=\sum_{i=1}^n\frac{X_i-m}{\sigma\sqrt n}$

$$
E(\frac{X_i-m}{\sigma\sqrt n})=\frac{E(X_i)-m}{\sigma\sqrt {n}}=0 \\
\text{et}\\
V(\frac{X_i-m}{\sigma\sqrt n})=\frac{1}{\sigma^2 n}V(X_i)=\frac{\sigma^2}{n\sigma^2}=\frac{1}{n}
$$

La fonction caractéristique de $Y_n=\sum_{i=1}^n\frac{X_i-m}{\sigma\sqrt{n}}$ est:

$$
\phi_{Y_n}(t) = \Pi_{i=1}^n\phi_{\frac{X_i-m}{\sigma\sqrt{n}}}(t)=\phi_{\frac{X_i-m}{\sigma\sqrt{n}}}(t)^n=(1-\frac{t^2}{2n}+o(\frac{1}{n^2}))^n
$$

On rappelle que $(1+\frac{x}{n})^n\to e^{x}$
Car $(1+\frac{x}{n})^n=e^{n\ln(1+\frac{x}{n})}\simeq e^{n\frac{x}{n}}=e^x$
Donc $\phi_{Y_n}(t)=(1-\frac{t^2}{2n}+o(\frac{1}{n^2}))^n\to e^{-\frac{t^2}{2}}$ lorsque $n\to+\infty$

# Estimateurs

<div class="alert alert-info" role="alert" markdown="1">
**Définition**
Soit $(X_1,X_2,...,X_n)$ un échantillon de $X$, c’est-à-dire une suite de variables aléatoires indépendantes et de même loi que $X$. La statistique $\bar X$ ou moyenne empirique de l’échantillon est:

$$
\bar X=\frac{1}{n}\sum_{i=1}^nX_i
$$

</div>


$$
E(\bar X)=\frac{1}{n}\sum_{i=1}^n E(X_i)=\frac{nm}{n}=m \text{ où } m=E(X)\\
V(\bar X)=\frac{1}{n^2}\sum_{i=1}^n V(X_i)=\frac{n\sigma^2}{n^2}=\frac{\sigma^2}{n}\to 0 \text{ lorsque } n\to+\infty
$$

Donc d’après Tchebychev $\bar X=\frac{1}{n}\sum_{i=1}^nX_i\to^Pm=E(X)$ quand $n\to+\infty$

<div class="alert alert-success" role="alert" markdown="1">
C’est la loi des grands nombres.
</div>