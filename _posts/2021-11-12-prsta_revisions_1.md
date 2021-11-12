---
title:          "PRSTA: Revisions 1"
date:           2021-11-12 14:00
categories:     [Image S9, PRSTA]
tags:           [Image, S9, PRSTA]
math: true
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/B1MOKYFLY)

# Exercice 1

## Partie 1

<details markdown="1"><summary>Solution</summary>

Sous l'hypothese $H_0$,

$$
T = \sqrt{n} \frac{\bar X_n - m}{\sigma}\sim N(0,1)\\
t= \sqrt{10}\frac{0,48 - 0}{1}\simeq 1,55
$$

Zone de rejet:

$$
\color{red}{R=}\{T\gt q_{0,95}\}\\
\{T\gt1,64\}
$$

*Est-ce que $t$ appartient a notre zone de rejet ?*

$t\not\in \color{red}{R}$ $\color{red}{\text{donc}}$ l'hypothese $(H_0)$ n'est pas rejetee.

</details>

## Partie 2

<details markdown="1"><summary>Solution</summary>

$$
Z_n = \sqrt{n}\frac{\bar X_n - m_0}{\sqrt{S_n^2}}\sim T_{n-1}\\
S_n^2:= \frac{1}{n-1}\sum_{i=1}^n(X_i-\bar X_n)^2
$$

Ici,

$$
t = \sqrt{10}\frac{0,49 - 0}{1,96}\simeq 0,79
$$

Zone de rejet: on rejette **des 2 cotes**

$$
\{T\gt 2.26\}\cup\{T\lt \color{green}{-1,28}\}\\
R=\color{green}{\{T\gt q_{0,975}\}\cup\{T\lt q_{0,025}\}}
$$

*Pourquoi on n'a pas besoin d'utiliser Python ?*
> Car c'est symetrique

$\color{green}{\text{Pas}}$ de rejet car $\color{blue}{t\not\in R}$

</details>

## Partie 3

<details markdown="1"><summary>Solution</summary>

$$
T = (n-1)\frac{S_n^2}{\sigma_0^2}=\boxed{\frac{1}{\sigma^2_0}\sum_{i=1}^n(X_i-\bar X_n)^2}
$$

Sur l'echantillon,

$$
t\simeq \frac{1}{4}\times 34, 55 = 8,64
$$

$$
\begin{aligned}
&P(T\lt t)\quad\text{ou } T\sim\chi^2(9)\\
&= P(T\lt 8,64)\\
&\simeq 0,53\color{orange}{\gt 0,1}
\end{aligned}
$$

*Comment resonne-t-on avec la P-value ?*
> Il faut que la P-value soit superieure ou egale 

Donc l'hypotese $(H_0)$ n'est pas rejetee.

</details>

# Exercice 2

<details markdown="1"><summary>Solution</summary>

1.

Comme le parametres est $\frac{1}{\theta}$, on veut affirmer sur la duree de vie moyenne $\theta$ est $2$ ans, et on aura un probleme si jamais elle est inferieure car $E(\varepsilon(\frac{1}{2}))=2$

2.

$H_0$ rejetee si $T\lt 2$ avec $T:=\min_{1\le i\le n}X_i$

3.

$$
\begin{aligned}
F(x)&=\int_0^x\lambda e^{-\lambda t}dt\\
&= [-e^{\lambda y}]_0^x\\
&= -e^{-xt} + 1 = 1-e^{-xt}
\end{aligned}
$$

$$
\begin{aligned}
R(x) &= 1-F(x)\\
&=e^{-\lambda x}
\end{aligned}
$$

$$
\begin{aligned}
P(T&\gt x)\\
P(\min_{1\le i\le n}X_i&\gt x)\\
P(\bigcap_{i=1}^n\{X_i&\gt n\})
\end{aligned}
$$

Sous $H_0$:

$$
\begin{aligned}
P(T\gt x) &= \prod_{i=1}^nP(X_i\gt x)\\
&= P(X_1\gt x)^n\\
&= e^{-\frac{n}{\color{blue}{\theta}}x}
\end{aligned}
$$

<div class="alert alert-danger" role="alert" markdown="1">

$$
T\sim\varepsilon(\frac{n}{\color{blue}{\theta}})
$$

</div>

4.

$$
\begin{aligned}
P(T\lt 2) &= F(2)\\
&= 1-e^{-\frac{n}{2}\times 2}\\
&= \color{red}{1-e^{-n}}
\end{aligned}
$$

5.

$$
\begin{aligned}
\alpha &= P(\text{Rejeter }H_0\vert H_0\text{ vraie})\\
&= P(T\lt 2\vert \theta=2)\\
&= \color{red}{\boxed{1-e^{-n}}}
\end{aligned}\\
n = 10\\
\alpha\simeq = 0.9999
$$

6.

Rien qu'avec $n=10$, on a un $\alpha$ extremement eleve, la regle est donc ***NULLE***.

**Test GLR**

$$
\color{red}{H_0:\theta = 2\text{ contre } H_1:\theta\lt 2}
$$

$$
T=\frac{L(X_1,\dots, X_n,2)}{L(X_1,\dots, X_n,\hat\theta)}
$$

Soit:

$$
\color{red}{H_0:\frac{1}{\theta} = \frac{1}{2}\text{ contre } H_1:\frac{1}{\theta}\lt \frac{1}{2}}
$$

$$
\begin{aligned}
T&=\frac{L(X_1,\dots, X_n,\color{green}{\frac{1}{\bar X_n}})}{L(X_1,\dots, X_n,\frac{1}{2})}\\
&= \frac{\prod_{i=1}^n\color{green}{\frac{1}{\bar X_n}}e^{-\color{green}{\frac{1}{\bar X_n}} X_i}}{\prod_{i=1}^n\frac{1}{2}e^{-\frac{1}{2}X_i}}\\
&= (\color{green}{\frac{2}{\bar X_n}})^ne^{-\sum_{i=1}^n(\color{green}{\frac{1}{\bar X_n}}-\frac{1}{2})X_i}
\end{aligned}
$$

L'hypothese $(H_0)$ est rejetee si $T\gt S_{\alpha}$.

<div class="alert alert-success" role="alert" markdown="1">
Nous allons utiliser *Wilks*.
</div>

$$
\begin{aligned}
R&=2\ln(T)\\
&= 2n\ln(\color{green}{\frac{2}{\bar X_n}})-2\sum_{i=1}^n(\color{green}{\frac{1}{\bar X_n}}-\frac{1}{2})X_i\\
\end{aligned}
$$

Pour $n$ suffisamment grand:

$$
\{R\sim\chi^2(1)\}
$$

</details>

# Feuille 4 Exercice 4

<details markdown="1"><summary>Solution</summary>

$$
\color{green}{\boxed{T=\sum_{i=1}^nX_i^3}}
$$

$$
\color{green}{Y_{ii} = \frac{2}{\theta}X_i^3\sim X^2(2)}
$$

$$
\Rightarrow \frac{2}{\theta} T\sim \chi^2(2n)
$$

$$
\begin{aligned}
\alpha &=P(\text{Rejeter }H_0\vert H_0\text{ vraie})\\
&= P(T\gt S_{\alpha}\vert\theta = \theta_0)\\
&= P(\frac{2}{\theta_0}T\gt \frac{2}{\theta_0}S_{\alpha}\vert \theta=\theta_0)
\end{aligned}
$$

Sous $(H_0)$, $\color{red}{\frac{2}{\theta_0}T\sim\chi^2(2n)}$

$\color{green}{F_n \text{ est la fonction de repartition }\chi^2(2n)}$

$$
\alpha = P(W\gt \frac{2}{\theta_0}S_{\alpha})
$$

<div class="alert alert-danger" role="alert" markdown="1">

$$
\alpha = 1 -F_n(\frac{2}{\theta_0}S_{\alpha})
$$

</div>

$\color{red}{Donc}$

$$
1-\alpha = F_n(\frac{2}{\theta_0}S_{\alpha})
$$

<div class="alert alert-danger" role="alert" markdown="1">

$$
S_{\alpha} = \frac{\theta_0}{2}F_n^{-1}(1-\alpha)
$$

</div>

$$
\begin{aligned}
\color{red}{\beta} &= P(\text{Rejeter }H_1\vert H_1\text{vraie})\\
&= P(T\le S_{\alpha}\vert \theta=\theta_1)\\
&= P(\frac{2}{\theta_1}T\le \frac{2}{\theta_1}S_{\alpha}\vert \theta = \theta_1)
\end{aligned}
$$

$$
w_1 = \frac{2}{\theta_1}T\sim \chi^2(2n)
$$

<div class="alert alert-danger" role="alert" markdown="1">

$$
\beta = F_n(\frac{2}{\theta_1}S_{\alpha})
$$


$$
\color{green}{\beta = F_n\biggr(\frac{\theta_0}{\theta_1}F_n^{-1}(1-\alpha)\biggr)}
$$

</div>

Passons aux applications numeriques:

```python
scipy.stats.chi2.cdf(0.5 * scipy.stats.ppf(0.95, 30), 30)
```

```
0.14185880202947254
```

```python
scipy.stats.chi2.cdf(0.2 * scipy.stats.ppf(0.95, 60), 60)
```

```
1.6239064341119149e-09
```

```python
scipy.stats.chi2.cdf(0.5 * scipy.stats.ppf(0.99, 20), 20)
```

```
0.46403880816957155
```

```python
scipy.stats.chi2.cdf(0.2 * scipy.stats.ppf(0.99, 20), 20)
```

```
1.87204631776198e-08
```

```python
scipy.stats.chi2.cdf(1.0001 * scipy.stats.ppf(0.99, 20), 20)
```

```
0.9900104784496678
```

</details>
