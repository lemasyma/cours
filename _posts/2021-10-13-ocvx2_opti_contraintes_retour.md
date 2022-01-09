---
title:          "OCVX2 : Le retour de l'optimisation avec contraintes"
date:           2021-10-13 14:00
categories:     [Image S9, OCVX2]
tags:           [Image, SCIA, S9, OCVX2]
math: true
---

Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/HJi55S4SK)


<div class="alert alert-danger" role="alert" markdown="1">
**But**

Resoudre:

$$
\begin{matrix}
(OPT)&\text{minimiser } f(x)& \\
\text{tel que} &g_i(x)\le0&i=1,\dots,m\\
&h_j(x)=0&j=1,\dots,p
\end{matrix}
$$

</div>

Avec $f, g_i$ convexes et $h_j$ affines

$p^{\*}=$ valeur optimale $=f(x^{\*})$ point optimal avec

$$
\begin{aligned}
f:\mathbb R^n&\to\mathbb R\\
x&\mapsto f(x)
\end{aligned}
$$

$x$ est admissible ssi il verifie les contraintes

<div class="alert alert-info" role="alert" markdown="1">
Lagrangien de (OPT):

$$
\begin{aligned}
\mathscr L:\mathbb R^n\times\mathbb R^m\times\mathbb R^p&\to\mathbb R\\
(x,\alpha,\beta)&\mapsto\mathscr L(x,\alpha,\beta)=f(x)+\sum_{i=1}^n\alpha_ig_i(x)+\sum_{j=i}^p\beta_jh_j(x)
\end{aligned}\\
\begin{aligned}
\alpha\in\mathbb R^m\\
\beta\in\mathbb R^p
\end{aligned}\biggr\}\text{variables duales/multiplicateurs de Lagrange}
$$

</div>

# Fonction primale et probleme primal

Fonction objective primale:

$$
\theta_p(x)=\max_{\alpha,\beta \\ \alpha\ge0\Leftrightarrow \alpha_i\ge0\forall i}\mathscr L(x,\alpha,\beta)
$$

et probleme primal $(Q)$ $$\min_x\theta_p(x)$$
- $x$ est primal admissible ssi $g_i(x)\le0$ $\forall i$ $h_j(x)=0$ $\forall j$
- $x^{\*}$ primal optimal et $p^{\*}=\theta_p(x^{\*})$ valeur optimale

Dans le cas ou on a une seule contrainte $g(x)\le0$ et une seule contrainte $h(x)=0$

$$
\mathscr L(x,\alpha,\beta)=f(x)+\alpha g(x)+\beta h(x)\\
\begin{aligned}
\underbrace{\theta_p(x)}_{\text{fonction convexe}}&=\max_{\alpha,\beta \\ \alpha\ge 0}\mathscr L(x,\alpha,\beta)\\
&=\max_{\alpha, \beta \\ \alpha\ge 0}[f(x)+\alpha g(x)+\beta h(x)]\\
&= f(x) + \max_{\alpha,\beta \\ \alpha\ge0}[\alpha g(x)+\beta h(x)]
\end{aligned}
$$

| $g(x)\gt0\to\alpha=+\infty$ | $h(x)\neq0, \beta=signe(h(x))\infty$ |
|:---------------------------:|:------------------------------:|
|    $g(x)\le0\to\alpha=0$    |  $h(x)=0,$ peu importe $\beta$  |

$$
\theta_p(x)=f(x)+\begin{cases}
0 &\text{si } g(x)\le0 \text{ et } h(x)=0\\
+\infty &\text{sinon}
\end{cases}\\
\Leftrightarrow x\text{ primal admissible}
$$

$y=x^2$:

![](https://i.imgur.com/d4s9kVn.png)

$$
\begin{aligned}
\min f(x)&=\infty^2\\
x+1&\le0
\end{aligned}
$$

![](https://i.imgur.com/mKhRA1z.png)

$\color{red}{\boxed{}}$ : lieu des points primaux admissible

# Fonction duale et probleme dual

Fonction objective duale $$\theta_D(\alpha,\beta)=\min_x\mathscr L(x,\alpha,\beta)$$

et probleme dual $$(D) \max_{\alpha,\beta \\ \alpha\ge0}\theta_D(\alpha,\beta)$$

<div class="alert alert-success" role="alert" markdown="1">
$(\alpha, \beta)$ dual admissible ssi $\alpha\le0$ ($\alpha_i\ge0$ $\forall i$)
</div>

$(\alpha^{\*}, \beta^{\*})$ dual optimal ssi solution de $(D)$ et $d^{\*}=\theta_D(\alpha^{\*},\beta^{\*})$

$$
\begin{aligned}
\underbrace{\theta_D(\alpha,\beta)}_{\text{fonction concave}} &=\min_x\mathscr L(x,\alpha,\beta)\\
&= \min_x[\underbrace{f(x)+\alpha g(x)+\beta h(x)}_{\text{affine (a } x \text{) fixe relativement a }\alpha\text{ et }\beta\text{ et }\min(\text{fcts concaves}) = \text{fct concave}}]
\end{aligned}
$$

<div class="alert alert-info" role="alert" markdown="1">
**Lemme**

Si $$(\alpha,\beta) \\ \alpha\ge0$$ dual admissible, $\theta_D(\alpha,\beta)\le p^{\*}$

</div>

### Preuve

$$
\begin{aligned}
\theta_D(\alpha, \beta) &=\min_x\mathscr L(x, \alpha, \beta)\\
&\le\mathscr L(x^*,\alpha,\beta)=f(x^*)+\underbrace{\overbrace{\alpha}^{\ge0}\overbrace{g(x^*)}^{\le0}}_{\le0} + \overbrace{\beta h(x^*)}^{=0}\quad\begin{matrix}\text{avec }x^*\text{ primal optimal} \\ \to g(x^*)\le0\text{ et } h(x^*)=0\end{matrix}\\
&\le f(x^*)=p^*
\end{aligned}
$$

<div class="alert alert-danger" role="alert" markdown="1">
Toutes les valeurs du probleme dual minorent la valeur optimale du probleme primal
</div>

Probleme dual $$\to\max_{\alpha,\beta \\ \alpha\ge0}\theta_D(\alpha,\beta)=d^*\le p^*\to p^*-d^*\ge0$$ **saut de dualite**

<div class="alert alert-info" role="alert" markdown="1">
C'est le **principe de dualite faible**: vrai pour tout probleme primal et dual
</div>

On aimerait ici que le saut de dualite $p^\*-d^\*$ soit egaux a $0\to p^\*=d^\*$

<div class="alert alert-success" role="alert" markdown="1">
On peut resoudre le primal en resolvant le dual
</div>

On a cherche les conditions ("qualifications de contraintes") pour que $p^\*=d^\*$.

Dans le cas ou tout est convexe:

<div class="alert alert-info" role="alert" markdown="1">
**Condition de Slater**
Le saut de dualite est nul s'il existe un $\tilde x$ qui est *srictement admissible* $(g(\tilde x)\lt0)\Leftrightarrow$ l'ensemble admissible doit avoir un point interieur
</div>

<div class="alert alert-info" role="alert" markdown="1">
**Lemme** *(complementarite)*
Si la dualite forte est verifiee, on a $\boxed{\alpha^{\*}g(x^{\*})=0}$

> Si on a plusieurs contraintes, $\alpha^{\*}_ig_i(x^{\*})=0$ $\forall i$

</div>

### Preuve

Dualite forte: 

$$
\begin{aligned}
p^{*}=d^{*}&=\theta_D(\alpha^{*},\beta^{*})\\
&= \min_x\mathscr L(x,\alpha^{*},\beta^{*})\\
&\le\mathscr L(x^*,\alpha^*\beta^*)=\underbrace{f(x^*)}_{p^*}+\underbrace{\overbrace{\alpha^*}^{\ge0}\overbrace{g(x^*)}^{\le0}}_{\le0}+\overbrace{\beta^*\underbrace{h(x^*)}_{=0}}^{=0}
\end{aligned}\\
p^*\le p^*+\underbrace{\alpha^*}_{\le0}\to\alpha^*+g(x^*)=0\\
\begin{cases}
\alpha^*\gt0&\to g(x^*)=0\\
g(x^*)\lt0&\to\alpha^*=0
\end{cases}
$$

# Conditions de Karush-Kuhn-Tucker (KKT pour les intimes)

<div class="alert alert-info" role="alert" markdown="1">
**Conditions KKT**

Conditions necessaires pour la resolution de (OPT):

$$
\begin{matrix}
(OPT)&\text{minimiser } f(x)& \\
\text{tel que} &g_i(x)\le0&i=1,\dots,m\\
&h_j(x)=0&j=1,\dots,p
\end{matrix}
$$

</div>

Soient $x^{\*}\in\mathbb R^n$, $\alpha^{\*}\in\mathbb R^m$ et $\beta^{\*}\in\mathbb R^p$ satisfait les conditions:

1. Stationnarite de $\mathscr L$: $$\nabla_x\mathscr L(x^*,\alpha^*,\beta^*)=\nabla_x f(x^*)+\sum_{i=1}^n\alpha_i^*\nabla g_i(x^*)+\sum_{j=1}^p\beta_j^*\nabla_x h(x^*)=0$$
2. Admissibilite primale: $g_i(x^{\*})\le0$ $\forall i$ et $h_j(x^{\*})=0$ $\forall j$
3. Admissibilite duale: $\alpha_i^{\*}\ge0$ $\forall i$
4. Complementarite: $\alpha_i^{\*}g_i(x^{\*})=0$ $\forall i$

Alors $x^{\*}$ est optimal pour le probleme primal, et $(\alpha^{\*}, \beta^{\*})$ optimal pour le dual.

Si de plus la dualite forte est verifiee, alors n'importe quelles solutions du primal et du dual verifient $1)-4)$

## En pratique

*Comment on s'en sort ?*
1. On ecrit le Lagrangien $\mathscr L(x,\alpha,\beta)$ et on calcule $\nabla_x\mathscr L(x,\alpha,\beta)$
2. On utilise la stationnarite $\nabla_x\mathscr L(x,\alpha,\beta)=0$ pour trouver une relation entre $x$ et $\alpha/\beta$
3. On remplace $x$ par $\alpha/\beta$ dans le Lagrangien $\to$ ecrire la fonction objective duale
4. On resout le dual, eventuellement en se servant de la complementarite


# Exemple

$$
\begin{aligned}
\min_{x\in\mathbb R^2}&\frac{1}{2}(x_1^2+x_2^2)\\
\text{tel que }&\underbrace{x_1-2x_2+2}_{g(x_1,x_2)}\le0
\end{aligned}
$$

1. $$\mathscr L(x,x_2,\alpha_2)=\frac{1}{2}(x_1^2+x_2^2)+\alpha(x_1-2x_2+2)$$
2. $$\begin{aligned}\nabla_x\mathscr L = 0 &\to \frac{\partial\mathscr L}{\partial x_1}=x_1+\alpha=0\to x_1=-\alpha \\ &\frac{\partial \mathscr L}{\partial x_2} = x_2-2\alpha=0\to x_2=2\alpha\end{aligned}$$
3. $$\begin{aligned}\mathscr L(\alpha)(\equiv\theta_D(\alpha))&=\frac{1}{2}\biggr((-\alpha^2)+(2\alpha)^2\biggr) + \alpha(-\alpha-4\alpha+2) \\ &= \frac{5}{2}\alpha^2-5\alpha^2+2\alpha \\ &=-\frac{5}{2}\alpha^2+2\alpha\end{aligned}$$
4. On resout

$$
\begin{aligned}
\max_{\alpha\ge0}\theta_{D}(\alpha)\to\nabla_{\alpha}\theta_D(\alpha)&=-5\alpha+2 = 0 \\
\alpha^*&=\frac{2}{5}\to x_1^*=-\frac{2}{5}\text{ et } x_2^*=\frac{4}{5}
\end{aligned}
$$
