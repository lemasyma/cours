---
title:          "ASE2: Convergence et estimation - Exercices, suite"
date:           2021-03-03 9:00
categories:     [tronc commun S8, ASE2]
tags:           [tronc commun, ASE2, S8]
description: Suite des exercices sur la convergence et estimation
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/HJqkMkTM_)

# Exercice 3
Soit $X$ une VA de densite $f(x) = e^{-x-e^{-x}}$ $\forall x\in\mathbb R$.

1. Determiner la fonction de repartition de $X$
2. Soit $Y=e^{-x}$, determiner la fonction de repartition de $Y$, puis sa densite
3. Calculer $E(Y)$, $V(Y)$
4. Soit $(Y_1,..., Y_n)$ un echantillon de $Y$, cad $(Y_i), 1\le i\le n$ sont alors des VA independantes et de meme loi que $Y$. On pose $\overline{Y_{n}} = \frac{1}{n}\sum_{i=1}^kY_i$
    1. Montrer que $\overline{Y_n}\to_{n\to+\infty}^P1$
    2. Montrer que $\overline{Y_n}\to_{n\to+\infty}^{m.q}1$

<details markdown="1">
<summary>Solution</summary>

1. $F(x) = P(X\lt x) = \int_{-\infty}^xf(t)dt$ $\forall x\in\mathbb R$

$$
\begin{aligned}
F(x) &= \int_{-\infty}^xe^{-t}\times e^{-e^{-t}}\\
&= \biggr[e^{-e^{-t}}\biggr]_{-\infty}^x = e^{-e^{-x}} \text{ car } (e^{-e^{-t}})' = e^{-t}e^{-e^{-t}}\\
&= e^{-e^{-x}}
\end{aligned}
$$

2. $Y = e^{-X}$, Soit $G(y)$ la fonction de repartition de $Y$. $Y$ etant positive donc $G(y) = P(Y\lt y) = 0$ pour $y\le 0$.

Pour $y\gt 0$:

$$
\begin{aligned}
G(y) &= P(Y\lt y) = P(e^{-X}\lt y) = P(-X\lt \ln(y))\\
&= P(X\gt-\ln(y)) = 1 - F(-\ln(y))\\
&= 1 - e^{-y}\\
\text{Donc } G(y) &=
\begin{cases}
    0 &y\le 0\\
    1-e^{-y} &y\gt 0
\end{cases}
\end{aligned}
$$

La densite de $Y = e^{-X}$ est:

$$
g(y) = G'(y) =
\begin{cases}
    0 &y\le 0\\
    e^{-y} &y\gt 0
\end{cases}
$$

3. $E(Y) = \int_{\mathbb R}yg(y)dy = \int_{-\infty}^{+\infty}ye^{-y}dy$

On integre par parties:
$$
\begin{cases}
    v = y &v'=1\\
    u' = e^{-y} &u = e^{-y}
\end{cases}\\
\begin{aligned}
E(Y) = \underbrace{\biggr[-ye^{-y}\biggr]_0^{+\infty}}_{_{y\to+\infty}\to0} - \int_0^{+\infty}(-e^{-y})dy &= \int_0^{+\infty}e^{-y}dy\\
&= \biggr[-e^{-y}\biggr]_0^{+\infty} = 1
\end{aligned}\\
V(Y) = E(Y^2) - E^2(Y)\\
E(Y^2) = \int_0^{+\infty}y^2e^{-y}dy\\
\text{Integration par parties:}
\begin{cases}
    v = y^2 &v'=2y\\
    u'=e^{-y} &u=-e^{-y}
\end{cases}\\
\begin{aligned}
E(Y^2) &=\int_0^{+\infty}Y^2e^{-y}dy = \underbrace{\biggr[-y^2e^{-y}\biggr]_0^{+\infty}}_{_{y\to+\infty}\to0}-\int_0^{+\infty}2y(-e^{-y})dy\\
&= 2\int_0^{+\infty}ye^{-y}dy = 2E(Y) = 1\\
\text{Donc: } V(Y) &= 2 - 1 = 1
\end{aligned}
$$

4. 1. $\overline{Y_n}=\frac{1}{n}\sum_{i=1}^{n}Y_i$, $(Y_i)_{1\le i\le n}$ idependantes et de meme loi que $Y$.

$$
\begin{aligned}
E(\overline{Y_n}) &= \frac{1}{n}\sum_{i=1}^nE(Y_i) = \frac{1}{n}\sum_{i=1}^n1 = \frac{n}{n} = 1\\
V(\overline{Y_n}) &= \frac{1}{n^2}\sum_{i=1}^nV(Y_i)= \frac{n}{n^2} = \frac{1}{n}
\end{aligned}
$$

En utilisant Tchebychev:
$$
\begin{aligned}
\forall\varepsilon\gt0, &P(\vert\overline{Y_n}-E(\overline{Y_n})\vert \gt\varepsilon)\lt\frac{V(\overline{Y_n})}{\varepsilon^2}\\
\Rightarrow &P(\vert\overline{Y_n}-1)\vert \gt\varepsilon)\lt\frac{1}{n\varepsilon^2}\to_{n\to+\infty}0\\
\text{Donc: } &\overline{Y_n}\to_{n\to+\infty}^P1
\end{aligned}
$$

4. 2. Montrons que $\overline{Y_n}\to_{n\to+\infty}^{m.q}1$

$$
\begin{aligned}
E(\vert\overline{Y_n}-1)\vert^2) &= E(\vert\overline{Y_n}-E(\overline{Y_n})\vert^2)\\
&=V(\overline{Y_n}) = \frac{1}{n}\to_{n\to+\infty}0\\
\text{Donc: } \overline{Y_n}&\to_{n\to+\infty}^{m.q}1
\end{aligned}
$$

</details>

# Exercice 4
Soit $X$ une VA de loi $\gamma_p$, $(p\in\mathbb N^*)$
1. Determiner la fonction caracteristique de $X$
2. En deduire celle de $\frac{X-p}{\sqrt{p}}$
3. Montrer que $\frac{X-p}{\sqrt{p}}\to_{p\to+\infty}^LN(0,1)$

<details markdown="1">
<summary>Solution</summary>

1. $X$ suit la  loi $\gamma_p$ (gamma). Sa densite est $f(x) = \frac{1}{\Gamma(p)}e^{-x}x^{p-1}$

Donc:

$$
\begin{aligned}
\phi_X(t) &= \frac{1}{\Gamma(p)}\int_0^{+\infty}e^{itx}e^{-x}x^{p-1}dx\\
&=\frac{1}{\Gamma(p)}\int_0^{+\infty}e^{(it-1)x}x^{p-1}dx\\
\text{Posons: } I_{p-1}&=\int_0^{+\infty}e^{(it-1)x}x^{p-1}dx\\
I_0 &= \int_0^{+\infty}e^{(it-1)x}dx = \biggr[\frac{e^{(it-1)x}}{it-1}\biggr]_0^{+\infty} = -\frac{1}{it-1}\\
\text{Car: } e^{(it-1)x} &= e^{itx}.e^{-x}\to_{x\to+\infty}0 \text{ puisque }\vert e^{itx}\vert = 1\text{ (bornee) }\\
I_{p-1} &= \int_0^{+\infty}e^{(it-1)x}x^{p-1}dx\\
\end{aligned}\\
\text{Integration par parties:}
\begin{cases}
    v = x^{p-1} &v'=(p-1)x^{p-2}\\
    u'=e^{(it-1)x} &u=\frac{1}{it-1}e^{(it-1)x}
\end{cases}\\
\begin{aligned}
I_{p-1}&=\underbrace{\biggr[\frac{e^{(it-1)x}}{it-1}x^{p-1}\biggr]_0^{+\infty}}_{\to_{x\to+\infty}0} - \frac{p-1}{it-1}\int_0^{+\infty}e^{(it-1)x}x^{p-2}dx\\
\text{Car: } \underbrace{e^{itx}}_{\text{bornee}, \vert e^{itx}\vert = 1}&e^{-x}x^{p-1}\to_{x\to+\infty}0\\
I_{p_1} &= -\frac{p-1}{it-1}I_{p-2}\text{ } \forall p\ge 2\\
I_{p-2} &= -\frac{p-2}{it-1}I_{p-3}\\
&.\\
&.\\
&.\\
I_2 &= -\frac{2}{it-1}I_1\\
I_2 &= -\frac{2}{it-1}I_1\\
\end{aligned}
$$

En faisant le produit:

$$
\begin{aligned}
I_{p-1} &= \frac{(-1)^{p-1}(p-1)!}{(it-1)^p}I_0\\
&= \frac{(-1)^p(p-1)!}{(it-1)^p}\\
\phi_X(t) &= \frac{1}{\Gamma(p)}I_{p-1}=\frac{(-1)^p}{(it-1)^p} \\
&= (1-it)^{-p}
\end{aligned}
$$

2. On veut la fonction caracteristique de $\frac{X-p}{\sqrt{p}}$. Or, d'apres le cours:

$$
\phi_{\frac{X-m}{\delta}}(t) = e^{\frac{itm}{\delta}}\phi_X(\frac{t}{\delta})
$$

Ici $m=p$ et $\delta=\sqrt{p}$

Donc:

$$
\begin{aligned}
\phi_{\frac{X-p}{\sqrt{p}}} &= e^{-\frac{itp}{\sqrt{p}}}\phi_X(\frac{t}{\sqrt{p}})\\
\Rightarrow \phi_{\frac{X-p}{\sqrt{p}}} &= e^{-\frac{itp}{\sqrt{p}}}(1-\frac{it}{\sqrt{p}})^{-p}
\end{aligned}
$$

3. Montrons que $\frac{X-p}{\sqrt{p}}\to_{p\to+\infty}^LN(0,1)$

$$
\ln(\phi_{\frac{X-p}{\sqrt{p}}}) = -\frac{itp}{\sqrt{p}}-p\ln(1-\frac{it}{\sqrt{p}})
$$

Or $\ln(1+x)\sim x-\frac{x^2}{2}$ au voisinage de 0.

Donc:

$$
\begin{aligned}
\ln(\phi_{\frac{X-p}{\sqrt{p}}})&\simeq-\frac{itp}{\sqrt{p}}-p(-\frac{it}{\sqrt{p}} + \frac{t^2}{2p}) \text{ pour p au voisinage de } +\infty\\
&\simeq -\frac{itp}{\sqrt{p}}+\frac{itp}{\sqrt{p}}+\frac{t^2}{2} = \frac{t^2}{2} \text{ pour p au voisinage de } +\infty\\
\Rightarrow \phi_{\frac{X-p}{\sqrt{p}}}&\simeq e^{-\frac{t^2}{2}} \text{ : fonction caracteristique de } N(0,1)
\end{aligned}
$$

Conclusion: $\frac{X-p}{\sqrt{p}}\to_{p\to+\infty}^LN(0,1)$

</details>
