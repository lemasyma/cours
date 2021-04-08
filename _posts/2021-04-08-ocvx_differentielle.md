---
title:          "OCVX: Norme"
date:           2021-04-08 10:00
categories:     [Image S8, OCVX]
tags:           [Image, SCIA, OCVX, S8]
description: Norme
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/r1ZRdN3S_)

---
lang: fr
---

# OCVX : Différentiabilité et différentielle en un point

Bienvenue dans le merveilleux monde de la differentielle <3

<div class="alert alert-danger" role="alert" markdown="1">
**BUT**: Etudier les extrema d'une fonction convexe
</div>

# Exemple

$$
f(x) = ax^2+bx+c\quad a\gt 0
$$

![](https://i.imgur.com/sdhYEVG.png)

<div class="alert alert-success" role="alert" markdown="1">
On derive $f$, $f'(x)=2ax+b$

On cherche $x^*$ tel que $f'(x^*)=0$
</div>

$$
f'(x^*) = 0 = 2ax^*+b
$$

Point optimal:
$$
x^*=-\frac{b}{2a}
$$

Valeur optimale:
$$
\begin{aligned}
f^*=f(x^*)&=a(-\frac{b}{2a})^2+b(-\frac{b}{2a})+c\\
&=\frac{b^2}{4a}-\frac{b^2}{2a}+c\\
&=-\frac{b^2}{4a}+c
\end{aligned}
$$

<div class="alert alert-warning" role="alert" markdown="1">
$$
f^*=\min_{x\in\mathbb R}f(x)\\
x^*=argmin_{x\in\mathbb R}f(x)
$$
</div>

On a envie de faire pareil pour $$\begin{aligned}f:\mathbb R^n&\to\mathbb R \\ x=(x_1,x_2,...,x_n)&\mapsto f(x) \end{aligned}$$

<div class="alert alert-danger" role="alert" markdown="1">
On a besoin de generaliser la notion de derive pour des fonctions de plusieurs variables.
</div>

# Rappel
On dit que $f:\mathbb R\to\mathbb R$ est *derivable* en $x_0$ ssi $$\lim_{x\to x_0}\frac{f(x)-f(x_0)}{x-x_0}$$ existe et est finie.

Si c'est le cas, $$f'(x_0)=\lim_{x\to x_0}\frac{f(x)-f(x_0)}{x-x_0}$$ est le nombre derive de $f$ en $x_0$.

![](https://i.imgur.com/YFFOJLA.png)

$f'(x_0)\equiv$ pente de la tangente au point $(x_0,f(x_0))$.

<div class="alert alert-info" role="alert" markdown="1">
**Equation de la tangente:** Elle passe par le point $(x_0,f(x_0))$ et $\vec u=(1,f(x_0))$ est un vecteur directeur
$$
\rightarrow y=f(x_0)+(x-x_0)f'(x_0)
$$
</div>

<div class="alert alert-success" role="alert" markdown="1">
*Si $f$ est convexe* $\rightarrow$ le graphe de $f$ est toujours au dessus de la tangente, quelque soit le point ou on trace la tangente
$$
\forall x_0\in\mathbb R,\quad f(x)\ge f(x_0)+(x-x_0)f'(x_0)
$$

**C'est la caracterisation a l'ordre 1 de la convexite**.
</div>

On peut reecrire le nombre derive comme $$f'(x_0)=\lim_{h\to 0}\frac{f(x_0+h)-f(x_0)}{h}$$ en posant $h=x-x_0$

<div class="alert alert-info" role="alert" markdown="1">
**Petit rappel**: On dit que $f\theta_{a}(g)$ s'il existe $\varepsilon:\mathbb R\to\mathbb R$ avec $\varepsilon(x)\to_{x\to a}0$ et $f(x)=g(x)\varepsilon(x),x\in \mathcal V(a)$

$$
\begin{aligned}
\frac{f(x)}{g(x)}&\to_{x\to a}0\\
\lim_{h\to0}\frac{f(x_0+h)-f(x_0)}{h} = f'(x_0) &\Leftrightarrow \lim_{h\to0}\frac{f(x_0+h)-f(x_0)-hf'(x_0)}{h} = 0\\
&\Leftrightarrow f(x_0+h)-f(x_0)-hf'(x_0)=\begin{cases}
\theta_a(h)\\
h\varepsilon(h)
\end{cases}\\
&\Leftrightarrow\underbrace{\color{red}{f(x_0+h)=f(x_0)+\overbrace{hf'(x_0)}^{h\to hf'(x_0)\text{ lineaire en }h}+h\varepsilon(x)}}_{\text{DL a l'ordre 1 en 0}}
\end{aligned}
$$
</div>

# *Comment generaliser la notion de derivee pour $f:\mathbb R^n\to\mathbb R$ ?*

*En quoi c'est faux ?*
$$
\lim_{x\to x_0}\frac{f(x)-f(x_0)}{\underbrace{x-x_0}_{\in\mathbb R^n}} = \lim_{h\to 0}\frac{f(x)-f(x_0)}{\underbrace{x-x_0}_{\in\mathbb R^n}}
$$

<div class="alert alert-danger" role="alert" markdown="1">
**On divise par des vecteurs !**

~~Wait that's illegal~~
</div>

<div class="alert alert-success" role="alert" markdown="1">
On pourrait regarder axe par axe (coordonnee par coordonnee) $\Rightarrow$ **derivees partielles**
</div>

<div class="alert alert-info" role="alert" markdown="1">
**Definition**: Si la fonction $\phi:t\mapsto f(x_1,...,x_k+t,...,x_n)$ est derivable en $0$, on dit que la $k^e$ derivee partielle de $f$ existe en $x=(x_1,...,x_n)$, et $\phi'(0)=\frac{\delta f}{\delta x_k}(x)$ (*se note $\delta_nf(x)$*)
</div>

$$
\phi(t) = f(x_1,...,x_k+t,...,x_n) = f(x+t(0,...0,1,0,...0))
$$

On regarde ce qu'il se passe pour la $k^e$ coordonnee en "bloquant" les autres.

Pour $f:\mathbb R\to\mathbb R$, $f'(x_0)$ existe $\Leftrightarrow$ $f$ derivable en $x_0$ $\Rightarrow$ f continue en $x_0$

<div class="alert alert-warning" role="alert" markdown="1">
Manque de bol, l'existence des derivees partielles en un point donne $\not\Rightarrow$ continuite de $f$
</div>

## Exemple

$$
\begin{aligned}
f:\mathbb R^2&\to\mathbb R\\
(x,y)&\mapsto\begin{cases}
\frac{xy}{x^2+y^2} &(x,y)\neq(0,0)\\
0 &(x,y)=(0,0)
\end{cases}
\end{aligned}
$$

On va regarder $$\begin{aligned}\phi_x:t&\to f((0,0)+t(1,0)) \\ \phi_x(t)&=f(t,0)=0\forall t \\ &\rightarrow\phi_x'(0)=0\frac{\delta f}{\delta x}(0,0)\end{aligned}$$

Idem pour $y$
$$
\begin{aligned}
\phi_y:t&\to f((0,0)+t(0,1)) = f(0,t)=0\forall t\\
&\rightarrow \phi_y'(0)=0=\frac{\delta f}{\delta y}(0,0)
\end{aligned}
$$

<div class="alert alert-warning" role="alert" markdown="1">
$\frac{\delta f}{\delta x}$ et $\frac{\delta f}{\delta y}$ existent en $(0,0)$, mais $f$ n'est pas continue
</div>


## Derivee directionnelle
<div class="alert alert-info" role="alert" markdown="1">
On peut generaliser la notion de derivee en un vecteur
$\rightarrow$ On dit que $f$ est derivable en $x_0$ selon un vecteur $v\in\mathbb R^n\setminus\{0\}$ si la fonction $\phi:t\mapsto f(x_0+tv)$ est derivable en $0$. On note $\phi'(0)=\lim_{t\to0}\frac{f(x_0+tv)-f(x_0)}{t} = \color{red}{D_vf(x_0)}$


$$
\frac{\delta f}{\delta x_i}(x_0)=D_{e_i}f(x_0)
$$
</div>

## Exemple

$$
\begin{aligned}
f:\mathbb R^2&\to\mathbb R\\
(x,y)&\mapsto x^2+y^2
\end{aligned}
$$

*Que vaut la derivee selon $v=(2,0)$ et $x_0=(1,0)$ ?*

$$
\begin{aligned}
\phi:t\to f(x_0+tv) &= f((1,0)+t(2,0))\\
&= f(1+2t,0)\\
&= (1+2t)^2+0^2\\
&= 4t^2+4t+1
\end{aligned}\\
\rightarrow\phi(t) = 4t^2+4t+1\rightarrow \phi'(t)=8t+4\rightarrow phi'(0)=D_vf(x_0)=4\\
\text{Et } D_{e_1}=\frac{\delta f}{\delta x}(x_0) = 2\\
\begin{cases}
    D_{(2,0)}f(x_0)=4\\
    D_{(1,0)}f(x_0)=\frac{\delta f}{\delta x}(x_0)=2
\end{cases}
\text{D'une maniere generale, } D_{\alpha v}f(x_0)=\alpha D_v f(x_0)
$$

Si $\Vert v\Vert=1\rightarrow$ derivee en $x_0$ en vecteur $v$ $\equiv$ derivee directionnelle en $x_0$ selon $v$

## *Est-ce que les derivees directionnelles sont la solution ?*

*Est-ce que l'existence des derivees directionnelles en $x_0$ selon tout vecteur $v\in\mathbb R^n\setminus\{0\}$ garantit la continuite ?*

<div class="alert alert-warning" role="alert" markdown="1">
Nope, toujours pas.
</div>

## Exemple

$$
\begin{aligned}
f:\mathbb R^2&\to\mathbb R\\
(x,y)&\mapsto\begin{cases}
\frac{y^2}{x} &x\neq0\\
y &x=0
\end{cases}
\end{aligned}
$$

En $(0,0)$ selon $v=(v_1,v_2)\neq\{(0,0)\}$

$$
\begin{aligned}
\phi:t&\to f(x_0+tv)=f((0,0)+t(v_1,v_2)) = f(tv_1,tv_2)\\
\phi(t)&=\begin{cases}
\frac{(tv_2)^2}{tv_1} &v_1\neq0\\
tv_2 &v_1=0
\end{cases}\\
\phi(t)&=\begin{cases}
t\frac{v_2^2}{v_1} &v\neq 0\\
tv_2 &v_1=0
\end{cases}\\
\phi'(t)&=\begin{cases}
\frac{v_2^2}{v_1} &v_1\neq0\\
v_2 &v_1=0
\end{cases}\\
\phi'(0)&=\begin{cases}
\frac{v_2^2}{v_1} &v_1\neq0\\
v_2 &v_1=0
\end{cases}
\rightarrow\text{ existe }\forall v\in\mathbb R^2\setminus\{0\}
\end{aligned}
$$

<div class="alert alert-success" role="alert" markdown="1">
$f$ admet une derivee en $0$ quelque soit le vecteur $v\in\mathbb R^2\setminus\{0\}$
</div>

<div class="alert alert-danger" role="alert" markdown="1">
Pourant, $f$ n'est **pas** continue en $(0,0)$.
</div>

Si on regarde le parametrage $\psi:t\to(t^2,t)$

$$
f\circ\psi(t)=f(\psi(t)) = f(t^2,t)=\begin{cases}
\frac{t^2}{t^2} &t\neq0\\
0 &t=0
\end{cases}
$$
$\rightarrow$ $f\circ\psi$ n'est **pas** continue en $0$
$\rightarrow$ $f$ n'est **pas** continue en 0

# Nouvelle approche

On va changer l'angle d'attaque
Pour $f:\mathbb R\to\mathbb R$, on a vu: $f$ derivable en $x_0$ $$\begin{aligned}&\Leftrightarrow \lim_{h\to0}\frac{f(x_0+h)-f(x_0)}{h} \\ &\Leftrightarrow f(x_0+h)=\underbrace{f(x_0)}_{\text{la variable c'est }h}+\underbrace{hf'(x_0)}_{\text{fonction lineaire par rapport a }h}+\underbrace{\theta_a(h)}_{h\varepsilon(h)}\end{aligned}$$ 

<div class="alert alert-info" role="alert" markdown="1">
**Definition**: On dit que $f$ est **differentiable** en $x_0$ s'il existe une application lineaire $$\underbrace{d_{x_0}f}_{\text{se note aussi }df(x_0), df_{x_0}}:\mathbb R^n\to\mathbb R$$ telle que 

$$
\color{red}{f(x_0)+d_{x_0}f(h)+\underbrace{\theta_a(\Vert h\Vert)}_{\Vert h\Vert\varepsilon(h)}}
$$
</div>

Pour $f:\mathbb R\to\mathbb R$, $f$ derivable en $x_0$ $\Leftrightarrow$ $f(x_0+h)=f(x_0) + \underbrace{hf'(x_0)}_{d_{x_0}f\text{ avec } d_{x_0}f:h\to hf'(X_0)} + h\varepsilon(h)$

<div class="alert alert-success" role="alert" markdown="1">
$d_{x_0}f$ s'appelle la differentielle de $f$ en $x_0$
</div>

<div class="alert alert-warning" role="alert" markdown="1">
differentielle = application lineaire = fonction $\neq$ $f'(x_0)$ = valeur
</div>

<div class="alert alert-info" role="alert" markdown="1">
**Proposition**: Si $f$ est differentiable en $x_0$, $f$ est continue en $x_0$
*preuve $\rightarrow$ admise*
</div>

## Exemple
$$
\begin{aligned}
f:\mathbb R&\to\mathbb R\\
x&\mapsto x^2
\end{aligned}
$$

En $x_0$

$$
f(x_0+h)=(x_0)^2=\underbrace{x_0^2}_{f(x_0)}+\overbrace{2hx_0}^{\text{fonction lineaire par rapport a }h \\ \rightarrow d_{x_0}f(h)=2hx_0 \\ \rightarrow d_{x_0}h\mapsto\underbrace{2x_0h}_{f(x_0)}}+\underbrace{h^2}_{\theta_a(h)\to\frac{h^2}{h}=h\to_{h\to0}0}\\
$$

$$
\begin{aligned}
f:\mathbb R^n&\to\mathbb R\\
x&\mapsto x^Tx
\end{aligned}
$$

En $x_0$:

$$
\begin{aligned}
f(x_0+h)&=(x_0+h)^T(x_0+h) = x_0^Tx_0+x_0^Th+\underbrace{h^Tx_0}_{(h^Tx_0)^T=x_0^Th}+h^Th\\
&= \underbrace{x_0^Tx_0}_{f(x_0)} + 2x_0^Th+\underbrace{h^Th}_{\theta_a(\Vert h\Vert)}
\end{aligned}\\
h^Th=<h,h>=\Vert h\Vert^2\\
\frac{h^Th}{\Vert h\Vert}=\frac{\Vert h\Vert^2}{\Vert h\Vert}=\Vert h\Vert\to_{h\to0}0
$$

Et $2x_0^Th$ est lineaire $\color{red}{(2x_0^T(h_1+\lambda h_2))=2x_0^Th_1+2\lambda x_0^Th}$

<div class="alert alert-info" role="alert" markdown="1">
**Propriete**: Si $f$ differentielle en $x_0$, alors f admet des derivees selon tout vecteur $h\in\mathbb R^n\setminus\{0\}$ et $D_hf(x_0)=d_{x_0}f(h)$
</div>

## Lien entre differentielle et vecteur gradient
f differentielle en $x_0$, $f$ admet des derivees selon tout vecteur $h\in\mathbb R^n\setminus\{0\}$, en particulier selon les vecteurs de la base canonique $(e_1,...,e_n)$
$\rightarrow$ toutes les derivees partielles $\frac{\delta f}{\delta x}(x_0)$ existent

$$
h\in\mathbb R^n\\
h=\begin{pmatrix}
h_1\\
\vdots\\
h_n
\end{pmatrix}\quad h=\sum_{i=1}^nh_ie_i\\
\begin{aligned}
d_{x_0}f(h) &= d_{x_0}f(\sum_{i=1}^nh_ie_i) \begin{cases}
h_i\in\mathbb R\forall i\\
e_i\in\mathbb R^n
\end{cases}\quad f\text{ lineaire } f(\lambda x+\mu y) = \lambda f(x) + \mu f(y)\\
&= \sum_{i=1}^nh_id_{x_0}f(e_i)\\
&= \sum_{i=1}^nh_iD_{e_i}f(x_0) = \sum_{i=1}^nh_i\frac{\delta f}{\delta x_i}(x_0)
\end{aligned}
$$

<div class="alert alert-info" role="alert" markdown="1">
**Definition**: On appelle vecteur gradient de $f$ en $x_0$ 
$$
\nabla_{x_0}f=\nabla f(x_0)=\begin{pmatrix}
\frac{\delta f}{\delta x_i}(x_0)\\
\vdots\\
\frac{\delta f}{\delta x_n}(x_0)
\end{pmatrix}
$$
</div>

$$
\begin{aligned}
d_{x_0}f(h) &= \sum_{i=1}^nh_i\frac{\delta f}{\delta x_i}(x_0) =  (\underbrace{\frac{\delta f}{\delta x_1}(x_0),...,\frac{\delta f}{\delta x_n}(x_0)}_{\nabla_{x_0}f^T})\begin{pmatrix} h_1 \\ \vdots \\ h_n \end{pmatrix}\\
&=\nabla_{x_0}f^Th=<\nabla_{x_0},h>
\end{aligned}
$$

$f$ differentielle en $x_0$, $d_{x_0}=<\nabla_{x_0}f,h>=\nabla_{x_0}f^Th$

<div class="alert alert-danger" role="alert" markdown="1">
La differentielle est donc

$$
d_{x_0}f:h\mapsto<\nabla_{x_0}f,h>=\nabla_{x_0}f^Th
$$
</div>

## *Comment s'etend la differentielle pour $$\begin{aligned}f:\mathbb R^n&\to\mathbb R^p \\ x=(x_1,...,x_n)&\mapsto f(x) = (f_1(x_1,...,x_n),...,f_p(x_1,...,x_n))\end{aligned}$$*

$$
\begin{aligned}
f:\mathbb R&\rightarrow \mathbb R^3\\
x&\mapsto(2x, x^2, 3x+2)
\end{aligned}
$$

$f$ differentiable en $x_0$ $\Leftrightarrow$ $f_1,...,f_p$ sont differentiables en $x_0$

$$
\begin{aligned}
f(x_0+h)&=\begin{pmatrix} f_1(x_0+h) \\ \vdots \\ f_p(x_0+h) \end{pmatrix}\\
&= \begin{pmatrix}
f_1(x_0) + d_{x_0}f_1(h)+\theta_a(\Vert h\Vert)\\
\vdots \\
f_p(x_0) + d_{x_0}f_p(h)+\theta_a(\Vert h\Vert)
\end{pmatrix}\\
&= \underbrace{\begin{pmatrix}
f_1(x_0)\\
\vdots\\
f_p(x_0)
\end{pmatrix}}_{f(x_0)} + 
\underbrace{\begin{pmatrix}
d_{x_0}f_1(h)\\
\vdots\\
d_{x_0}f_p(h)
\end{pmatrix}}_{?} + \underbrace{\theta(\Vert h\Vert)}_{\in\mathbb R^p}
\end{aligned}
$$

Les $f_i, i = 1,...,p$ sont des fonctions differentiables de $\mathbb R^n\to\mathbb R$

$$
d_{x_0}f_i(h) = <\nabla_{x_0}f_i,h> = \nabla_{x_0}f_i^Th=\biggr(\frac{\delta f_1}{\delta x_1}(x_0),...,\frac{\delta f_n}{\delta x_n}(x_0)\biggr)h\\
\begin{pmatrix}d_{x_0}f_1(h) \\ \vdots \\ d_{x_0}f_p(h) \end{pmatrix}_{\mathbb R^p} = \begin{pmatrix}\nabla_{x_0}f_1^Th \\ \vdots \\ \nabla_{x_0}f_p^Th \end{pmatrix}_{\mathbb R^p} = \begin{pmatrix} (\frac{\delta f_1}{\delta x_1},...,\frac{\delta f_1}{\delta x_n})h \\ \vdots \\ (\frac{\delta f_p}{\delta x_1},...,\frac{\delta f_p}{\delta x_n})h \end{pmatrix}_{\mathbb R^p} = \underbrace{\begin{bmatrix} \frac{\delta f_1}{\delta x_1},...,\frac{\delta f_1}{\delta x_n} \\ \vdots \\ \frac{\delta f_p}{\delta x_1},...,\frac{\delta f_p}{\delta x_n} \end{bmatrix}_{\mathbb R^{p\times n}}}_{\text{matrice jacobienne}}h_{\mathbb R^n}
$$

<div class="alert alert-danger" role="alert" markdown="1">
Pour une fonction $f:\mathbb R^n\to\mathbb R^p$, on appelle **matrice jacobienne** en $x_0$, et on note $Jac_{x_0}f$, la matrice des derivees partielles $[Jac_{x_0}f]_{ij}=\frac{\delta f_i}{\delta x_j}$ 
</div>

$$\color{red}{d_{x_0}f(h) = Jac_{x_0}f\times h}$$  La differentielle de $f:\mathbb R^n\to\mathbb R^p$ en $x_0$ est l'applicatio lineaire $d_{x_0}f:h\mapsto Jac_{x_0}f\times h$
$f$ differentielle en $x_0$, $f(x_0+h)=f(x_0)+\underbrace{d_{x_0}}_{d_{x_0}f\text{ application lineaire}}+\theta_a(\Vert h\Vert)$

1. $$\begin{aligned} f:\mathbb R&\rightarrow \mathbb R^3\\ d_{x_0}f:h&\mapsto hf'(x_0) \end{aligned} $$
2. $$\begin{aligned} f:\mathbb R^n&\rightarrow \mathbb R\\ d_{x_0}f:h&\mapsto <\nabla_{x_0}f, h>=\nabla_{x_0}f^Th \end{aligned}$$
3. $$\begin{aligned} f:\mathbb R^n&\rightarrow \mathbb R^p\\ d_{x_0}f:h&\mapsto Jac_{x_0}f\times h \end{aligned}$$