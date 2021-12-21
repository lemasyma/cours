---
title:          "OPEL : Seance de revisions"
date:           2020-07-03 10:00
categories:     [S6, Shannon, OPEL]
tags:           [S6, OPEL, Shannon]
math: true
---

Lien de la [note Hackmd](https://hackmd.io/BWw0eORLSUqrEqAayXwoJw)

# Calculer les integrales doubles
<div class="alert alert-info" role="alert" markdown="1">
On fixe une integrale et on calcule l'autre.
</div>
## Premier exo
$I = \iint_D x^2 dxdy, \space\text{ou } D=\lbrace(x,y)\in\mathbb{R}^2, x\le1, \space y\ge0,\text{ et } y\le x\rbrace$
On trouve d'abord les bornes, on fixe $x$ et on regarde les variations de $y$. Comme $x\le1$ et $x\ge y^2$, $x$ est positif et varie entre 0 et 1. Donc on fixe $x\in[0, 1]$, on integre par rapport a $y$ positif et $y\le\sqrt{x}$, $y$ varie de 0 a $\sqrt x$. 
$$
\begin{aligned}
I &= \int^{x=1}_{x=0}x^2\biggr(\int_{y=0}^{y=\sqrt{\sqrt{x}}}dy\biggr) dx\\
&= \int^{1}_{0}x^2\sqrt{x}dx\\
&= \int^{1}_{0}x^{\frac{5}{2}}dx = \biggr[\frac{2}{7}x^{\frac{7}{2}}\biggr]^{1}_{0}\\
&= \frac{2}{7}
\end{aligned}
$$

## Deuxieme exo
$J = \iint_D x^2dxdy, \space\text{ou } D=\lbrace(x,y)\in\mathbb{R}^2, \frac{x^2}{a^2}+\frac{y^2}{b^2}\le1\rbrace$
Cette integrale nous rappelle **l'interieur d'un ellipse.**
![](https://i.imgur.com/hd09yRM.png)
Meme technique, on fixe $x$ et on regarde les variations de $y$.

### Premiere partie
Quand on trace une ellipse, $x$ varie entre $-a$ et $a$. Pour trouver les variations de $y$, on fixe $x$ puis on isole $y$, $y$ va dependre de $x$ en fonction de la trajectoire de l'ellipse. On obtient deux branches: une branche positif et une branche negatif en bas. 
$$
\frac{x^2}{a^2}+\frac{y^2}{b^2}\le1 
\Rightarrow -b\frac{\sqrt1 - x^2}{a^2} \le y\le +b\frac{\sqrt1 - x^2}{a^2}
$$
$y$ varie de $-b\frac{\sqrt1 - x^2}{a^2}$ a $+b\frac{\sqrt1 - x^2}{a^2}$.

### Deuxieme partie
Cette integrale est plus dur car on a une racine carree, cela peut s'apparenter a un changement de variable.
$$
\begin{aligned}
J &= \int_{-a}^{a}x^2\biggr(\int_{-b\frac{\sqrt1 - x^2}{a^2}}^{+b\frac{\sqrt1 - x^2}{a^2}}dy\biggr)dx\\
J &= 2b\int_{-a}^{a}x^2\sqrt{1-\frac{x^2}{a^2}}dx \\
&\text{On utilise la parite, tous les x sont au carre.}\\ 
&\text{On fait donc deux fois l'integrale de 0 a a}\\
J &= 4b\int_0^{a}x^2\sqrt{1-\frac{x^2}{a^2}}dx
\end{aligned}
$$
On pose $x = a\cos(t)$ pour se debarasser de la racine carre. L'astuce est de faire apparaitre une fonction trigonometrique pour obtenir $1-\cos^2\Rightarrow\sin^2$, $x = a\cos(t)\Rightarrow dx=-a\sin(t)dt$
<div class="alert alert-warning" role="alert" markdown="1">
Il y a un changement de bornes. $0 = acos(t)\Rightarrow\frac{\pi}{2}$ et $x =a, \cos(t) = 1\Rightarrow t=0$
</div>
$$
\begin{aligned}
J &= 4b\int_{\frac{\pi}{2}}^0 a^2\cos^2(t)\vert\sin(t)\vert(-a\sin(t)dt)\\
 &= 4ba^3\int^{\frac{\pi}{2}}_0\cos^2(t)\sin^2(t)dt\space\text{Attention! les bornes ont ete permuttees}\\
 &= ba^3\int^{\frac{\pi}{2}}_0\biggr(\sin(2t)\biggr)^2dt=ba^3\int^{\frac{\pi}{2}}_0\biggr(\frac{1-\cos(4t)}{2}\biggr)dt\space\text{car}\space\sin(2t) = 2\sin(t)\cos(t)\\
 &= \frac{ba^3}{2}\biggr[-\frac{\sin(4t)}{4} + t\biggr]^{\frac{\pi}{2}}_0 = \frac{a^3b\pi}{4}
\end{aligned}
$$
<div class="alert alert-danger" role="alert" markdown="1">
Si la fonction etait impair le resultat serait 0 car $\int_{-a}^a = 0$
</div>

## Troisieme exo
$K = \iint_D\cos(x^2+y^2) dxdy, \space\text{ou } D=\text{Disque de centre O et de rayon R}$
<div class="alert alert-info" role="alert" markdown="1">
Faites un changement de variable en polaire.
</div>
On pose $x = r\cos(\theta)$ et $y = r\sin(\theta)$. On est sur un disque de centre $O$ et de rayon $R$. L'angle polaire $\theta$ varie de $0$ a $2\pi$ et r varie de $0$ a $R$.
Posons $\begin{cases}x = r\cos(\theta)\\y = r\sin(\theta)\end{cases}$.
$$
\begin{aligned}
K &= \int^{\theta=2\pi}_{\theta=0}\int^{r = R}_{r=0}cos(r^2)rdrd\theta\space\text{car c'est le Jacobien}\\
&= \int^{2\pi}_{0}d\theta\int^{R}_{r=0}r\cos(r^2)dr\\
&= 2\pi\biggr[\frac{1}{2}\sin(r^2)\biggr]=\pi\sin(r^2)
\end{aligned}
$$

## Quatrieme exo
$I' = \iint_D\frac{dxdy}{(1+x^2)(1+y^2)}, \space\text{ou } D=0\le y\le x\le 1$
$x$ varie de $0$ a $1$ et $y$ varie de $0$ a $x$. Le domaine est un **triangle**. Si $y = x$ c'est la bissetrice.
![](https://i.imgur.com/YX09GD4.png)
$$
\begin{aligned}
I' &= \iint_D\frac{dxdy}{(1+x^2)(1+y^2)}\\
&= \int^{x=1}_{x=0}\int^{y=x}_{y=0}\frac{dxdy}{(1+x^2)(1+y^2)}\\
&= \int^{1}_{0}\frac{dx}{1+x^2}\int^{y=x}_{y=0}\frac{dy}{1+y^2}\\
&= \int^{1}_{0}\frac{\arctan(x)}{1+x^2}\\
&= \biggr[\frac{1}{2}(\arctan(x))^2\biggr]^1_0 = \frac{1}{2}(\frac{\pi}{4})^2 = \frac{\pi^2}{32}
\end{aligned}
$$

## Cinquieme exo
$J' = \iint_D\frac{dxdy}{(1+x^2+y^2)^2}, \space\text{ou } D=\lbrace(x,y)\in\mathbb(R), \space \vert x\vert\le x^2+y^2\le 1\rbrace$
On a l'interieur d'un disque de centre $O$ et de rayon 1.
* Si $x\ge0$
    * $\vert x\vert = x \le x^2 + y^2$
    * $x^2 - x + y^2 ge 0 \Rightarrow \biggr(x - \frac{1}{2}\biggr)^2 + y^2\ge\frac{1}{4}$
* Si $x\lt0$
    * $\vert x\vert = x \le x^2 + y^2\Rightarrow\biggr(x+\frac{1}{2}^2\biggr) + y^2 \ge \frac{1}{4}$
$D$ est la partie du disque de centre $O$ et de rayon $1$, exterieure au disque de centre $\Omega(\frac{1}{2}, 0)$ et de rayon $R=\frac{1}{2}$ et au disque de centre $\Omega^1(-\frac{1}{2}, 0)$ et $R=\frac{1}{2}$
![](https://i.imgur.com/AAL7Ydv.png)
$$
D = D_1U D_2U D_3U D_4
$$
D et la fonction $f(x, y)$ sont invariantes dans les symetrie par rapport aux axes.

# Determiner les extremes des fonctions suivantes
## Premier exo
$f(x,y) = -x^2y+\frac{1}{2}y^2+y$
On determine les points critiques: $\vec{grad}f=\vec 0$
$$
\Rightarrow
\begin{cases}
\frac{\partial f}{\partial x} = -2xy = 0 \Leftarrow x= 0\space\text{ou}\space y=0\\
\frac{\partial f}{\partial y} = -x^2+y+1=0
\end{cases}
$$
* si $x=0\Rightarrow y+1=0\Rightarrow y=-1$
* si $y=0\Rightarrow x^2+1\Rightarrow x=\pm1$
Donc il existe 3 points critiques: $M_1(0,-1)$, $M_2(-1,0)$ et $M_3(1,0)$.
La matrice Hessienne:
$$
\nabla^2f(x,y)=
\begin{pmatrix}
-2y & -2x\\
-2x & 1
\end{pmatrix}
$$
Nature des points critiques:
$$
\nabla^2f(x,y)=
\begin{pmatrix}
2 & 0\\
0 & 1
\end{pmatrix}
$$
$r=2$, $t=1$, $s=0$
$s^2-rt=-2\lt0$ et $r=2\gt0\Rightarrow M_1(0,-1)$ est un **minimum local**.
$$
\nabla^2f(M_2) = 
\begin{pmatrix}
0 & 2\\
2&1
\end{pmatrix}\\
$$
$s^2-rt=4-gt0\Rightarrow M_2(-1, 0)$ est un point.
$$
\nabla^2f(M_3) = 
\begin{pmatrix}
0 & -2\\
-2 & 1
\end{pmatrix}\\
$$
$s^2-rt=4-gt0\Rightarrow M_3(1, 0)$ est un point.
## Deuxieme exo
$f(x, y) = (x^2+y^2)e^{-x}$
## Troisieme exo
$f(x,y)=e^{x+y}-x^2-y$
## Quatrieme exo
$f(x,y,z) = z^2+xyz^2+xy$