---
title:          "PROC : Seance de revisions"
date:           2020-07-03 14:00
categories:     [S6, tronc commun, PROC]
tags:           [S6, PROC, tronc commun]
math: true
description: 
---

Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/Skh83HCAI)

# Calculer la densite
Etant donnee $f$, est-ce une densite ? Si oui, $P(\text{X}\le3)$ ?
* Verifier que la $f \ge 0$ et $\int^{+\infty}_{-\infty} = 1$

# Calculer avec la densite
Etant donnee $f$ densite, calculer $E(\text{X})$, $Var({\text{X}})$
* $E(\text{X}) = \int^{+\infty}_{-\infty}xf(x)dx$
* $Var(\text{X}) = \int^{+\infty}_{-\infty}\biggr(x-E(x)\biggr)^2f(x)dx=\int^{+\infty}_{-\infty}x^2f(x)dx - \biggr(E(x)\biggr)^2$
    
# X et Y independants, calculer la densite
$\text{X}$ et $\text{Y}$ independants, densite $f$ et $g$. Densite de $\text{X} + \text{Y}$ ?
* $h(x) = \int^{+\infty}_{-\infty}f(x - y)g(y)dy$
     
# Calculer la densite de $\alpha\text{X} + \beta$
Densite de $\alpha\text{X} + \beta$. Densite de $\text{X}$ : $f$. Il faut passer par la fonction de repartition.
* $F(X) = P(\text{X}\le x) = \int^{+\infty}_{-\infty}f(t)dt$
* $f(x) = F'(x)$
* Soit $\text{Y} = \alpha\text{X} + \beta$, $g$ sa densite
    * $G(x) = P(\text{Y}\le x) = P(\alpha\text{X} + \beta\le x)$

## Premier Cas
Si $\alpha\gt 0, G(x) = P(\alpha\text{X} + \beta\le x) = P(\text{X}\le\frac{x-\beta}{\alpha}) = F(\frac{x-\beta}{\alpha})$
En derivant $G'(x) = \frac{1}{\alpha}F'(\frac{x-\beta}{\alpha})$

## Second Cas
Si $\alpha\lt 0, G(x) = P(\alpha\text{X}+\beta\lt x) = P(\text{X}\ge\frac{x-\beta}{\alpha}) = 1 - \frac{1}{\alpha}F'(\frac{x-\beta}{\alpha})$
En derivant $G'(x) = -\frac{1}{\alpha}F'(\frac{x-\beta}{\alpha}) \Rightarrow g(x) = -\frac{x-\beta}{\alpha}f(\frac{x-\beta}{\alpha})$

# Convergence en probabilite
## Definition
<div class="alert alert-danger" role="alert" markdown="1">
$\vert X_n\vert$ converge en probabilite vers $\text{Y}$ si $\forall\epsilon\gt0, P(\vert\text{X} - \text{Y}\vert\gt\epsilon)\to_{n\to\infty}0$
</div>
## Rappel
<div class="alert alert-info" role="alert" markdown="1">
$$
\int_1^{+\infty}\frac{1}{x^{\alpha}}dx
\begin{cases}
    \text{converge si et seulement si} & \alpha\gt1\\
    \text{diverge si et seulement si} & \alpha\le1
\end{cases}
$$
$$
\int_0^{1}\frac{1}{x^{\alpha}}dx
\begin{cases}
    \text{converge si et seulement si} & \alpha\lt1\\
    \text{diverge si et seulement si} & \alpha\ge1
\end{cases}
$$
</div>
Primitive de $\frac{1}{x^\alpha}$:
$$
\begin{aligned}
x^{-\alpha} &= f(x)\\
F(x) &= \frac{1}{-\alpha+1}x^{-\alpha+1}
\end{aligned}
$$
## Cas particulier
<div class="alert alert-warning" role="alert" markdown="1">
On tire $X_1, X_2,..., X_n$ independemment distribuee et on definit la moyenne $\bar X_n = \frac{X_1 + ... + X_n}{N}$
$$
\begin{aligned}
E(\bar X_n) &= E(X_1)\\
Var(\bar X_n) &= \frac{1}{n}Var(X_1)\\
\sigma(\bar X_n) &= \sqrt{Var(\bar X_n)}\\
\text{Car}\space E(\bar X_n) &= \frac{1}{n}(E(X_1) + ... + E(X_n)) \\ 
&= E(X_1)\\
Var(\bar X_n) &= \frac{1}{n^2}(Var(X_1) + ... + Var(X_n))\\
&= \frac{nVar(X_1)}{n^2} = \frac{Var(X_1)}{n}
\end{aligned}
$$
</div>
## Inégalité de Tchebychev
<div class="alert alert-info" role="alert" markdown="1">
$$
\begin{aligned}
\forall\epsilon\gt0, P(\vert\bar X_n - E(X_n)\vert\ge\epsilon) &\le \frac{Var(\bar X_n)}{\epsilon^2}\\
&\le\frac{Var(X_1)}{n\epsilon^2}\to_{n\to\infty}0
\end{aligned}
$$
Donc $P(\vert\bar X_n - E(X_n)\vert\gt\epsilon)\to_{n\to\infty}0$
</div>

## Theoreme central limite

* $X_1, X_2, ..., X_n$
* $\bar X_n = \frac{X_1 + ... + X_n}{n}$
On a vu que $E(\bar X_n) = E(X_1)$ et que $Var(\bar X_n) = \frac{1}{n}Var(X_1)$

<div class="alert alert-danger" role="alert" markdown="1">
$$
Z_n = \frac{\bar X_n - E(\bar X_n)}{\sigma(\bar X_n)}\to Z
$$
Ou $Z$ a une distribution normal centre reduite: $Z\rightsquigarrow N(0,1)$
</div>

<div class="alert alert-warning" role="alert" markdown="1">
$$E(Z_n) = 0 \space\text{et}\space Var(Z_n) = 1$$
</div>

On a $\forall[a,b]\subset\mathbb{R}$,
$$
P(Z_n\in[a,b])\to_{n\to\infty}P(Z\in[a,b])
$$

# Exercice typique
## Premier exercice

Soient $X_1, ..., X_n$ independemment distribuee avec $E(X_1) = 3$, $Var(X_1) = 4$ et $\bar X_n = \frac{X_1 + ... + X_n}{n}$. Trouver n tel que $P(\vert\bar X_n - 3\vert \ge 1)\le 5\%$.

<details markdown="1"><summary>Solution</summary>
:warning: Si $Z\to N(0,1)$, $P(-1,96\le Z\le1,96) = 95\%$
1 est pris au hasar mais pas 3, c'est l'esperance.
Ici, on definit 
$$
\begin{aligned}
Z_n &= \frac{\bar X_n - E(\bar X_n)}{\sigma(\bar X_n)}\\
&= \frac{\bar X_n - 3}{\sqrt{\frac{4}{n}}}\\
&= \frac{\bar X_n - 3}{\frac{2}{\sqrt n}}
\end{aligned}
$$
Si n est grand:
$$
P\Biggr(-1,96\le\frac{\bar X_n - 3}{\frac{2}{\sqrt n}} \le 1,96\Biggr) = 95\%\\
P\Biggr(\Biggr\vert\frac{\bar X_n - 3}{\frac{2}{\sqrt n}}\Biggr\vert \le 1,96\Biggr) = 95\%\\
P\Biggr(\vert\bar X_n - 3\vert \le \frac{1,96 * 2}{\sqrt n}\Biggr) = 95%\\
P\Biggr(\vert\bar X_n - 3\vert \ge \frac{3,92}{\sqrt n}\Biggr) = 5\%
$$
* Si $\frac{3,92}{\sqrt n} = 1$, on a:
$$P(\vert\bar X_n - 3\vert\ge 1) = 5\%$$
* Si $\frac{3,92}{\sqrt n} \ge n_0$ avec $n_0 = 3,92^2$ valeur minimale de n, on a:
$$
P(\vert\bar X_n - 3\vert\ge 1) \ge P(\vert\bar X_n - 3\vert\ge \frac{3,92}{\sqrt n}) \le 5\%
$$
</details>
## Deuxieme exercice
On achete une machine. $P_{\text{Machine defectueuse}} = 2\%$. On achete $n$ machines. Pour $i\in [1, n]$
$$
X_i =
\begin{cases}
      1 & \text{si defectueuse}\\
      0 & \text{sinon}
\end{cases}
$$
et $\bar X_n = \frac{X_1 + ... + X_n}{n}$

On sait que $\bar X_n\to_{\text{prob}}2\%$. Trouver $n_0$ tel que $\forall n\ge n_0$, $P(0,01\le\bar X_n\le 0,03) \ge 95\%$. 

<details markdown="1"><summary>Solution</summary>
Autrement dit, 
$$
\begin{aligned}
P(\vert\bar X_n - 0,02\vert\le0,01)&\ge95\%\\
\text{donc}\space P(\vert\bar X_n - 0,02\vert\ge0,01)&\le5\%
\end{aligned}
$$
$$
X_i =
\begin{cases}
      1 & \text{avec proba}\space p = 0,02\\
      0 & \text{avec proba}\space 1-p
\end{cases}\\
E(X_i) = 0*(1-p)+ 1\ast p = p\\
\begin{aligned}
Var(X_i) &= E\biggr((X_i-E(X))^2\biggr)\\
&= E\biggr((X_i - p)^2\biggr) = p(1-p) = 0,02 * 0,98
\end{aligned}
$$
Pour $\bar X_n$:
$$
\begin{aligned}
E(\bar X_n) = E(X_1) = p\\
Var(\bar X_n) = \frac{1}{n}Var(X_1) = \frac{p(1-p)}{p}
\end{aligned}
$$
On pose:
$$
Z_n = \frac{\bar X_n \ E(\bar X_n)}{\sigma{\bar X_n}} = \frac{\bar X_n - p}{\sqrt{\frac{p(1 - p)}{n}}}
$$

On a donc:
$$
\begin{aligned}
P(\vert Z_n\vert\ge 1,96) &= 5\%\\
P(\biggr\vert \frac{\bar X_n - p}{\sqrt{\frac{p(1-p)}{n}}}\biggr\vert\ge 1,96) &= 5\%\\
P(\vert \bar X_n - p\vert\ge 1,96\sqrt{\frac{p(1-p)}{n}}) &= 5\%\\
\end{aligned}
$$
Si $n$ tel que $1,96\sqrt{\frac{p(1-p)}{n}} \le 0.01$, on a $P(\vert X_n - p\vert\ge 0,01)\le5\%$
</details>

## Troisieme exercice
Soit $f(x) = ...$. 
* Si vous pensez que $f$ est une densite, entrer $P(X\le3)$
* Sinon rentrer $-1$

<details markdown="1"><summary>Solution</summary>
:abc: Discussion sur les integrales impropres.
Il faut verifier que $\int_{-\infty}^{\infty}f(x)dx = 1$. Si $f$ est non-nulle sur une partie infinie de $\mathbb{R}$, il faut discuter de la nature de l'integrale. Soit elle est:
* **divergente** et $f$ n'est *pas une densite*
* **convergente** et verifier que l'integrale vaut 1 et que $f$ est positive

</details>
# Exemples
## Exemple 1
$$
f(x) =
\begin{cases}
    0 & \text{si}\space x\le1\\
    \frac{1}{x} & \text{si}\space x\gt1
\end{cases}
$$
![](https://i.imgur.com/MpL0WRX.png)
<details markdown="1"><summary>Solution</summary>
$$
\int^{+\infty}_{-\infty}f(x)dx = \int^{+\infty}_{1}\frac{1}{x}dx
$$
L'integrale est divergente donc $f$ n'est pas une densite.
</details>

### Exemple 2
$$
f(x) =
\begin{cases}
    0 & \text{sur}\space ]-\infty, 1]\\
    \frac{1}{x^{10}} & \text{sur}\space ]1, +\infty[
\end{cases}
$$
![](https://i.imgur.com/zA4HewC.png)

<details markdown="1"><summary>Solution</summary>
$$
\begin{aligned}
\int^{+\infty}_{-\infty}f(x)dx &= \int^{+\infty}_{1}\frac{1}{x^{10}}\space\text{avec}\space
x^{-10}\to\text{primitive:}\space\frac{1}{-10 + 1x^{^-10+1}}\\
&=\biggr[-\frac{1}{9}\ast\frac{1}{x^9}\biggr]^{+\infty}_{1}\\
&=0-(-\frac{1}{9}) \\
&= \frac{1}{9}
\end{aligned}
$$
$f$ n'est pas une densite.
</details>

## Exemple 3
$$
f(x) =
\begin{cases}
    0 & \text{si}\space x\le1\\
    \frac{9}{x^{10}} & \text{si}\space x\gt 1
\end{cases}
$$
* f est une densite (cf exo ci-dessus)
* $P(X\le3)$? $E(X)$? $Var(X)$?

<details markdown="1"><summary>Solution</summary>
1. $P(X\le3)$?
$$
\begin{aligned}
P(X\le3) &= \int^{3}_{-\infty}f(x)dx\\
&=\int^3_1\frac{9}{x^{10}}dx \space\text{avec}\space
\frac{9}{x^{10}}\to\text{primitive:}-\frac{1}{x^{9}}\\
&=\biggr[-\frac{1}{x^{9}}\biggr]_1^3 = -\frac{1}{3^9} + \frac{1}{1^9} = 1 - \frac{1}{3^9}
\end{aligned}
$$
2. $E(X)$?
$$
\begin{aligned}
E(X) &= \int^{+\infty}_{-\infty}xf(x)dx\\
&= \int^{+\infty}_{1}\frac{9x}{x^{10}}dx\\
&= \int^{+\infty}_{1}\frac{1}{x^{9}}dx \space\text{avec}\space x^{-9}\to\text{primitive:}\frac{1}{-9+1}x^{-9+1} = -\frac{1}{8}x^{-8}\\
&= 9\biggr[-\frac{1}{8}x^{-8}\biggr]_1^{+\infty}\\\
&= 9[-0+\frac{1}{8}] = \frac{9}{8}
\end{aligned}
$$
3. $Var(X)$?
$$
\begin{aligned}
Var(X) &= \int^{+\infty}_{-\infty}(x-\frac{9}{8})^2f(x)dx\\
&= E(X^2) - (E(X))^2\\
&= \int^{+\infty}_{-\infty}x^2f(x)dx - (\frac{9}{8})^2
\end{aligned}
$$
$$
\int^{+\infty}_{-\infty}x^2f(x)dx = \int^{+\infty}_{1}x^2\frac{x9}{x^{10}}dx \space\text{avec}\space x^{-8}\to\text{primitive:}\frac{1}{-8+1}x^{-8+1}=-\frac{1}{7}x^{-7}
$$
$$
E(X^2) = 9\biggr[-\frac{1}{7x^7}\biggr]_{1}^{+\infty} = 9\biggr(-0+\frac{1}{7}\biggr)
$$
$$
Var(X) = \frac{9}{7} - \frac{9}{8}^2
$$
</details>

# Densite de $X + Y$ quand $X$ et $Y$ independants
* $X$: densite $f$
* $Y$: densite $g$
* $Z = X + Y$: densite $h
    * $h$ est la **convolution** de $f$ et $g$
$$
h(x) = \int^{+\infty}_{-\infty}f(x-y)g(y)dy
$$

## Exemple de distribution uniforme
* $X\rightsquigarrow\mathcal{U}([1, 2])$
* $Y\rightsquigarrow\mathcal{U}([4, 5])$
![](https://i.imgur.com/SEc7KGo.png)
$f(x)g(y)\not = 0 \Leftrightarrow x\in[1,2]\space\text{et}\space y\in[4,5]$
$$
h(x) = \int^{+\infty}_{-\infty}f(y)h(x - y)dy = \int^{+\infty}_{-\infty}f(x-y)g(y)dy
$$
Soit $x_0$ fixe, on calcule $h(x_0) = \int^{+\infty}_{-\infty}f(x_0-y)g(y)dy$.
$$
\begin{aligned}
f(x_0-y)g(y) \not= 0 &\Leftrightarrow 
\begin{cases}
1\le x_0-y\le2\\
4\le y\le 5
\end{cases}\\
&\Leftrightarrow 
\begin{cases}
\begin{aligned}
x_0 -2\le\space &y\le x_0 - 1\\
4\le\space &y\le 5
\end{aligned}
\end{cases}
\end{aligned}
$$

<div class="alert alert-info" role="alert" markdown="1">
Vert: $x_0 -2\le\space y\le x_0 - 1$
Rouge $4\le\space y\le 5$
</div>

* Cas $x_0 - 1\lt4$ ($x_0 \lt 5$): ![](https://i.imgur.com/2654bF8.png)
    * Pas de $y$ qui convient
    * $h(x_0)=\int^{+\infty}_{-\infty}0dx=0$
* Cas $5\le x_0 - 2$ ($x_0\ge7$): ![](https://i.imgur.com/jw0HK8Q.png)
    * Pas d'intersection
    * $h(x_0) = 0$
* Cas $4\le x_0 - 2\le5\le x_0 - 1$: ![](https://i.imgur.com/lFdCw9C.png)
    * $h(x_0) = \int_{x_0 -2}^5 1\ast1dx=[x]_{x_0 -2}^5 = 5-(x_0 - 2) = 7 - x_0$
* Cas $x_0-2\le4\le x_0 -1\le5$ ($5\le x\le6$): ![](https://i.imgur.com/FEL9oOa.png)
    * $h(x_0) = \int_4^{x_0-1}1dy = [y]_4^{x_0-1} = x_0 - 1 - 4 = x_0 - 5$
    
Finalement:
* $x\in[5,6]$, $h(x_0) = x_0 - 5$
* $x\in[6,7]$, $h(x_0) = 7 - x_0$
* Ailleurs, $h(x_0)=0$