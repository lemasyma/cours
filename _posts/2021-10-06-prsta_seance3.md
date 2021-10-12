---
title:          "PRSTA: Seance 3"
date:           2021-10-06 14:00
categories:     [Image S9, PRSTA]
tags:           [Image, S9, PRSTA]
math: true
description: Seance 3
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/HkthlqbHK)

# Exemple

1. $H_0:m=m_0$ contre $H_1:m=m_1$ ou $X$ suit une loi $\mathcal N(m,1)$ et $m_0\le m_1$
2. A. N.: $m_0=1$ et $m_1=2$
3. Calculer $\alpha$
4. Calculer $\beta$

<details markdown="1"><summary>Solution</summary>

Determiner la statistique de NP

$$
\begin{aligned}
\frac{L(X_1,\dots,X_n,2)}{L(X_1,\dots,X_n,1)} &= \frac{\Pi_{i=1}^n\frac{1}{\sqrt{2\pi}}e^{-\frac{(X_i-2)^2}{2}}}{\Pi_{i=1}^n\frac{1}{\sqrt{2\pi}}e^{-\frac{(X_i-1)^2}{2}}}\\
&= e^{\frac{1}{2}[-\sum X_i^2-4X_i+4+\sum X_i^2-2X_i+1]}\\
&= e^{\frac{1}{2}\sum_{i=1}^n(1X_i-3)}\\
&=e^{\sum_{i=1}^nX_i}\times \underbrace{e^{-\frac{3n}{2}}}_{\color{red}{c}}
\end{aligned}
$$


Passons au log

$$
\log(T)=\sum_{i=1}^nX_i+\log(\color{red}{c})
$$

L'hypothese $H_0$ est rejetee lorsque

$$
\begin{aligned}
T&\gt S_{\alpha}\\
\log(T)&\gt\log(S_{\alpha})\\
\sum X_i+\log(c)&\gt\log(S_{\alpha})\\
\end{aligned}\\
\color{red}{\boxed{\sum X_i\gt\log(S_\alpha)-\log(c)}}\\
\sum X_i\gt C_{\alpha}
$$

On veut calculer $\alpha$:

$$
\begin{aligned}
\alpha &= P(\text{rejeter } H_0\vert H_0\text{ vraie})\\
&= P(\sum X_i\gt C_{\alpha}\vert m=1)
\end{aligned}
$$

On veut se ramener a la loi centree-reduite:

$$
\begin{aligned}
\alpha&=P(\underbrace{\frac{\sum X_i}{n}}_{\color{green}{\bar X_n}}\gt\frac{C_{\alpha}}{n}\vert m=1)\\
&= P(\bar X_n\gt\frac{C_{\alpha}}{n}\vert m=1)\\
&= P(\sqrt{n}(\bar X_n-1)\gt\frac{\sqrt{n}(C_{\alpha}-1)}{n})
\end{aligned}
$$

Sous l'hypothese $H_0$: $Z_n=\sqrt{n}(\bar X_n-1)\sim\mathcal N(0,1)$

*Par definition, qu'est-ce que ce nombre ? On rejette combien a droite ?*
> C'est un **quantile** au niveau $1-\alpha$

$$
\sqrt{n}(\frac{C_{\alpha}}{n}-1)=Z_{1-\alpha}
$$

ou $Z_{1-\alpha}$ designe le quantile de $\mathcal N(0,1)$ au niveau $1-\alpha$.

Maintenant on veut exprimer $\beta$.

*De quoi on a besoin pour determiner $\beta$ ?*

$$
\begin{aligned}
\beta &= P(\text{Accepter } H_0\vert H_1\text{ vraie})\\
&= P(\sum X_i\le C_{\alpha}\vert m=2)
\end{aligned}
$$

On veut exprimer $C_{\alpha}$ en fonction de $Z_{1-\alpha}$.

$$
\begin{aligned}
\sqrt{n}(\frac{C_{\alpha}}{n}-1)&=Z_{1-\alpha}\\
\frac{C_{alpha}}{n}-1&=\frac{Z_{1-\alpha}}{\sqrt{n}}\\
\frac{C_{\alpha}}{n}=\frac{Z_{1-\alpha}}{\sqrt{n}}+1\\
\end{aligned}\\
\color{red}{\boxed{C_{\alpha}=n\biggr(\frac{Z_{1-\alpha}}{\sqrt{n}}+1\biggr)=\sqrt{n}Z_{1-\alpha}+n}}
$$

Avant de continuer, essayons de trouver $C_{\alpha}$ dans le cas ou $\alpha=1\%$ et dans le cas ou $\alpha=5\%$

Avant de calculer $\beta$, on trouve les $C_{\alpha}$.

$$
\begin{matrix}
\alpha=5\%&C_{\alpha}=1,64\sqrt{n}+n\\
\alpha=1\%&C_{\alpha}=2,33\sqrt{n}+n
\end{matrix}
$$

Si $n=100$, $\alpha=1\%$, alors $C_{\alpha}=123,3$ et pour $\alpha=5\%$, $C_{\alpha}=116,4$.

Maintenant on peut calculer $\beta$.

$$
\begin{aligned}
\beta&=P(\text{Ne pas rejeter } H_0\vert H_0\vert \text{ fausse})\\
&=P(\sum X_i\lt C_{\alpha}\vert m=2)\\
&=P(\bar X_n\lt\frac{C_{\alpha}}{n}\vert m=2)\\
&=P(\sqrt{n}(\bar X_n-2)\lt\sqrt{n}(\frac{C_{\alpha}}{n}-2)\vert m=2)\\
\end{aligned}
$$

Sous l'hypothese $(H_1)$

$$
Z_n=\sqrt{n}(\bar X_n-2)\sim\mathcal N(0,1)\\
\color{red}{\boxed{\beta=P(Z_n\lt\sqrt{n}(\frac{C_\alpha}{n}-2))}}
$$

Pour $\alpha=5\%$ et $n=100$:

$$
\begin{aligned}
\sqrt{n}(\frac{C_{\alpha}}{n}-2)&=10(1,164-2)\\
&=-8,36
\end{aligned}\\
\beta=P(Z_n\lt-8,36)=3\times10^{-17}
$$

```python
scipy.stats.norm.cdf(-8.36)
```
- `norm`: loi normale
- `cdf`: cumulative distribution function

*Pourquoi $\beta$ est aussi petit ?*
> Parce que $\alpha$ est tres grand par rapport a $n$

Faisons la meme chose pour $n=25$ et $\alpha=1\%$

</details>

# Test du rapport de vraisemblance generalise (GLR)

<div class="alert alert-danger" role="alert" markdown="1">
- $H_0:\theta\in A$ contre $H_1:\theta\in B$
- $T=\frac{L(X_1,\dots,X_n\hat\theta_1^{MV})}{L(X_1,\dots,X_n\hat\theta_0^{MV})}$
- $T=\frac{\sup_{\theta\in B}L(X_1,\dots,X_n\theta)}{\sup_{\theta\in A}L(X_1,\dots,X_n\theta)}$
- Rejet de $(H_0)$ ssi $T\gt S_{\alpha}$ ou $S_{\alpha}$ est un seuil qui depend du niveau de confiance de $\alpha$
</div>

*Comment on le traduit ?*
> $H_0:m\in\{0\}$
> $H_1:m\in\mathbb R\setminus\{0\}$

# Test de comparaison de 2 moyennes

- Deux populations
- Deux echantillons independants suffisamment grand $(X_1,\dots,X_{n_1})$ et $(Y_1,\dots,Y_{n_1})$
- Statistique

$$
Z=\frac{\bar X_{n_1}-\bar Y_{n_2}}{\sqrt{(\frac{S^2_{n+1}}{n_1}+\frac{S^2_{n_2}}{n_2})}}
$$

- $H_0:m_1=m_2$ contre $H_1:m_1\neq m_2$
- $H_0:m_1=m_2$ contre $H_1:m_1\gt m_2$
- $H_0:m_1=m_2$ contre $H_1:m_1\lt m_2$

# Principe de Neyman Pearson

<div class="alert alert-info" role="alert" markdown="1">
1. Determination d'un model statistique
2. Determination d'hypotheses
3. Determination d'une statistique de test
4. Determination de la forme de la region critique
5. Determination des valeurs critiques
6. Conclusion: rejet ou non de l'hypothese
7. Calcul de la puissance du test
</div>

## Hypotheses simples

- $H_0:\theta=\theta_0$
- $H_1:\theta=\theta_1$

# Exemple

## Premier exemple
La variable aleatoire $X$ suit une loi $\mathcal N(m,1)$. Nous voulons tester $H_0:m=0$ contre $H_1:m\neq0$

<details markdown="1"><summary>Solution</summary>
*Qu'est-ce que le maximum de vraisemblance ?*
> C'est ce qui maximise la fonction de vraisemblance en fonction de $\theta$

*Maximum de vraisemblance pour une loi normale ?*

$$
L(x_1,\dots,x_n,m)=\Pi_{i=1}^n\frac{1}{\sqrt{2\pi}}e^{-\frac{(x_i-m)^2}{2}}
$$

Il n'y a pas de $\sigma$ car $\sigma=1$

$$
L(x_1,\dots,x_n,m)=\Pi_{i=1}^n\frac{1}{\color{red}{\sigma}\sqrt{2\pi}}e^{-\frac{(x_i-m)^2}{2\color{red}{\sigma^2}}}
$$

On a une fonction $f\Rightarrow\log(f')$?

Prenons un exemple:

$$
\begin{aligned}
f(x) &= x^2-2x\\
f'(x)&=2x-2\\
\log(f'(x))&=\log(2x-2)\\
\log(f'(x))=0&\Leftrightarrow2x-2=1\\
&\Leftrightarrow \color{red}{\boxed{x=\frac{3}{2}}}\\
\end{aligned}\\
\begin{aligned}
f(x)&=x^2-2x\\
\log(f(x))&=\log(x^2-2x)\\
(\log(f(x)))'&=\frac{2x-2}{x^2-1}\\
(\log(f(x)))'=0&\Leftrightarrow\color{red}{\boxed{x=1}}
\end{aligned}
$$

<div class="alert alert-danger" role="alert" markdown="1">
Ce n'est pas le meme resultat
</div>

La formule du maximum de vraisemblance est:

$$
T=\frac{L(X_1,\dots,X_n,\hat\theta)}{L(X_1,\dots,X_n,\theta_0)}
$$

Avec $\hat\theta$ l'estimateur du maximum de vraisemblance de $\theta$.

On cherche $\bar X$.

$$
\begin{aligned}
T&=\frac{L(X_1,\dots,X_n,\bar X)}{L(X_1,\dots,X_n,0)}\quad \text{car }m=0\\
&= e^{-\frac{1}{2}[\sum_{i=1}^n(X_i-\bar X)^2-\sum_{i=1}^nX_i^2]}\\
&=e^{-\frac{1}{2}[e\sum_{i=1}^nX_i+n\bar X^2]}\\
&=e^{-\sum_{i=1}^nX_i-\frac{n}{2}\bar X^2}
\end{aligned}\\
\log(T)=-\sum X_i-\frac{n}{2}\bar X^2
$$

$(H_0)$ rejetee $\color{red}{si}$ $T\gt S_{\alpha}$

$$
\begin{aligned}
\log(T)&\gt\log(S_{\alpha})\\
-\sum X_i-\frac{n\bar X^2}{2}&\gt \log(S_{\alpha})\\
\sum_{i=1}^nX_i+\frac{n\bar X^2}{2}&\lt\log(S_{\alpha})
\end{aligned}
$$

<div class="alert alert-info" role="alert" markdown="1">
**Proposition**
Sous des hypotheses techniques, en notant $\hat\theta_n$ l'estimateur du maximum de vraisemblance.

$\sqrt{nI(\theta_0(\hat\theta_n\theta_0))}$ converge en loi vers $\mathcal N(0,1)$

Nous dirons que l'estimateur du maximum de vraisemblance est normal asymptotiquement efficace ou NAE.
</div>

Nous supposerons que les hypotheses techniques evoquees sont verifiees.

<div class="alert alert-info" role="alert" markdown="1">
**Theoreme de Wilks**
Sous l'hypothese $H_0$, $R_n:=2\log(T_n)$ converge en loi vers une loi $\chi^2(1)$
</div>

En revenant a nos calculs:

$$
2\biggr(\sum_{i=1}^nX_i+n\bar X^2\biggr)\sim\chi^2(1)
$$
</details>

## Second exemple

- La variable aleatoire $X$ suit une loi $\varepsilon(\lambda)$
- $H_0:\lambda=1$ contre $H_1:\lambda\gt1$
