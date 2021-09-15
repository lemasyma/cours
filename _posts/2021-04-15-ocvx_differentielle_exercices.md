---
title:          "OCVX: TD Differentielle"
date:           2021-04-15 10:00
categories:     [Image S8, OCVX]
tags:           [Image, SCIA, OCVX, S8]
description: TD Differentielle
---

Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/HkCxmdrLu)

# OCVX: TD Differentielle

<div class="alert alert-success" role="alert" markdown="1">
*But de la seance:* comprendre les differentielles
</div>

# Rappels
<div class="alert alert-info" role="alert" markdown="1">
**Definition premiere de la differentielle**
Une fonction $$\begin{aligned}f:\mathbb R^n&\to\mathbb R^n \\ x=(x_1,...,x_n)&\mapsto (f_1(x),...,f_n(x))\end{aligned}$$ est differentiable en un point $x_0$ si on peut ecrire 

$$
f(x_0+h)=f(x_0)+\color{red}{d_{x_0}f(h)}+\Vert h\Vert\varepsilon(h)
$$

$d_{x_0}f:h\mapsto d_{x_0}f(h)$ est une application lineaire: $d_{x_0}f(h_1+\lambda h_2)=d_{x_0}f(h_1)+\lambda d_{x_0}f(h_2)$
</div>

**Notation**: $d_{x_0}f$ / $df_{x_0} / Df(x_0)$

## $1^{ere}$ maniere de calculer la differentielle

$1^{ere}$ maniere de calculer la differentielle en $x_0$ de $f$: ecrire et lineariser $$f(x_0+h)=f(x_0)+d_{x_0}f(h)+\underbrace{\Vert h\Vert\varepsilon(h)}_{\mathcal O_o(h)}$$

## $2^{ere}$ maniere de calculer la differentielle
Si 
1.
$$
\begin{aligned} 
f:\mathbb R&\to\mathbb R \\ 
d_{x_0}f:h&\mapsto hf'(x_0)\\ 
\end{aligned}
$$

2.
$$
\begin{aligned} 
f:\mathbb R^n&\to\mathbb R \\ 
d_{x_0}f:h&\mapsto <\nabla_{x_0}f, h> = \nabla_xf^Th\\ 
\end{aligned}\\
\nabla_{x_0}f=\begin{pmatrix} \frac{\partial f}{\partial x_1}(x_0) \\ \vdots \\ \frac{\partial f}{\partial x_n}(x_0) \end{pmatrix}
$$

3.
$$
\begin{aligned} 
f:\mathbb R^n&\to\mathbb R^m \\ 
d_{x_0}f:h&\mapsto Jac_{x_0}f\times h\\ 
\end{aligned}\\
Jac_{x_0}f=\text{matrice jacobienne}\\
[Jac_{x_0}f]_{ij} = \frac{\partial f_i}{\partial x_j}(x_0)\\
Jac_{x_0}f=\begin{bmatrix}
\frac{\partial f_1}{\partial x_1}(x_0) & \dots & \frac{\partial f_1}{\partial x_n}(x_0)\\
\vdots & \ddots &\vdots\\
\frac{\partial f_n}{\partial x_1}(x_0) & \dots & \frac{\partial f_m}{\partial x_n}(x_0)\\
\end{bmatrix} = \begin{pmatrix}\nabla_{x_0}f_i^T \\ \vdots \\ \nabla_{x_0}f_m^T\end{pmatrix}
$$

<div class="alert alert-success" role="alert" markdown="1">
$f$ differentiable $\Rightarrow$ existence et continuite des $\frac{\partial f}{\partial x_i}$
</div>

<div class="alert alert-danger" role="alert" markdown="1">
Existence et continuite des $\frac{\partial f_i}{\partial x_j}$ $\Rightarrow$ $f$ differentiable
</div>

## Exemple

$$
f:(x,y)\mapsto \frac{xy}{x^2+y^2}\quad (x,y)\neq(0,0); 0\quad(x,y) = 0\\
f:(x,y)\mapsto \frac{xy}{\sqrt{x^2+y^2}}\quad (x,y)\neq(0,0); 0\quad(x,y) = 0
$$

<div class="alert alert-warning" role="alert" markdown="1">
Fonction ou ca se passe mal
</div>

## Differentielle de 2 fonctions
<div class="alert alert-info" role="alert" markdown="1">
**Rappel**
Pour des fonctions $f,g:\mathbb R\to\mathbb R$
- $(f+\lambda g)'=f'+\lambda g'$
- $(fg)'=f'g+g'f$
- $(f\circ g)'(x)=f'(g(x))\times g'(x)$

Pour la differentielle:
- $d_x(f+\lambda g)=d_xf+\lambda d_xg$
- $d_x(fg)=g(x)d_xf+f(x)d_xg$
- $d_x<f,g>=<d_xf,g(x)> + <f(x),d_xg>$ $\to$ pas ouf comme ecriture
    - $d_x<f,g>:f\mapsto <d_xf(h),g(x)> + <f(x),d_xg(h)>$
- $d_xg\circ f=d_{g(x)}f\circ d_xg$ $\to$ pas ouf comme ecriture
    - $$\begin{aligned} d_xg\circ f:h&\mapsto d_{g(x)}f\circ d_xg(h) \\ &=d_{g_x}f(d_xg(h)) \end{aligned}$$
</div>

# Exercices

## Exercice de cours
Differentielle de $$\begin{aligned}f:\mathbb R&\to\mathbb R \\ x&\mapsto \frac{\sin(x)}{x^2+1}\end{aligned}$$ en tout point $x$

<details markdown="1">
<summary>Solution</summary>

<div class="alert alert-info" role="alert" markdown="1">
**Rappel**

$$
\biggr(\frac{u(x)}{v(x)}\biggr)' = \frac{u'(x)v(x)-u(x)v'(x)}{v^2(x)}
$$
</div>

*Seconde methode:*
<div class="alert alert-danger" role="alert" markdown="1">
**Moyen memo technique**
- si(mple) $\to$ $\cos$
- co(mplique) $\to$ $-\sin$
</div>

$$
\begin{aligned}
f'(x) & =\frac{\cos(x)(x^2+1)-\sin(x)2x}{(x^2+1)^2}\\
&=\frac{(x^2+1)\cos(x)-2x\sin(x)}{(x^2+1)^2}
\end{aligned}\\
d_xf:h\mapsto hf'(x)
$$

*Premiere methode* (**mode bourrin**):
$$
f(x+h)=\frac{\sin(x+h)}{(x+h)^2+1}=\frac{\sin(x)\cos(h)+\cos(x)\sin(h)}{x^2+2xh+h^2+1}\\
\underbrace{\frac{\sin(x)\cos(h)}{(x^2+1)(1+\frac{2x}{x^2+1}h+\frac{h^2}{x^2+1})}}_{\text{premier terme}} + \underbrace{\frac{\cos(x)\sin(h)}{(x^2+1)(1+\frac{2x}{x^2+1}h+\underbrace{\frac{h^2}{x^2+1}}_{\mathcal o(h)})}}_{\text{second terme}}\\
\begin{aligned}
\text{Second terme }=&\frac{\cos(x)\sin(h)}{x^2+1}\underbrace{\frac{1}{(x^2+1)(1+\frac{2x}{x^2+1}h+o(h))}}_{1-\frac{2xh}{x^2+1}+o(h)}\quad\color{red}{\frac{1}{1+u}\sim 1-u+o(u)}\\
&\frac{\cos(x)\sin(h)}{x^2+1}\biggr(1-\frac{2xh}{x^2+1}+o(h)\biggr)\quad\color{red}{\sin(u)\sim u+o(u)}\\
&\frac{\cos(x)(h+o(h))}{x^2+1}\biggr(1-\frac{2xh}{x^2+1}+o(h)\biggr)\\
&= \frac{\cos(x)(h+o(h))}{x^2+1}-\underbrace{\frac{2xh}{x^2+1}\frac{\cos(x)(h+o(h))}{x^2+1}}_{o(h)}+o(h)\\
&= h\frac{\cos(x)}{x^2+1}+o(h)
\end{aligned}
$$

C'est que le second terme, on fait pas le premier parce qu'on a pas envie de crever.

</details>

## Exercice 2-37

<details markdown="1">
<summary>Solution</summary>
1.

$$
\begin{aligned}
f:\mathbb R^n&\to\mathbb R^m &A\in\mathcal M_{m,n}(\mathbb R)\\
x&\mapsto Ax+b &b\in\mathbb R^m
\end{aligned}\\
f(x+h)=A(x+h)+b=\underbrace{Ax+b}_{f(x)} + \underbrace{Ah}_{\text{lineaire en }h}\\
\begin{aligned}
d_xf:h&\mapsto Ah\\
d_xf(h)&=Jac_xf\times h
\end{aligned}
\biggr\text{\}} Jac_xf=A
$$

2.

$$
\begin{aligned}
f:\mathbb R^n&\to\mathbb R \quad A\in\mathcal M_{n}(\mathbb R) \text{ symetrique}\\
x&\mapsto x^TAx
\end{aligned}\\
\begin{aligned}
f(x+h)&=(x+h)^TA(x+h)\\
&= \underbrace{x^TAx}_{f(x)} + \underbrace{x^TAh}_{\in\mathbb R} + \underbrace{h^TAx}_{\in\mathbb R} + \underbrace{h^TAh}_{= (h^TAx)^T=x^TA^Th=x^TAh}\\
&= f(x) + \underbrace{2x^TAh}_{d_xf(h)}+\underbrace{hTAh}_{o(h)}
\end{aligned}\\
\begin{aligned}
d_xf:h&\mapsto 2x^TAh\\
d_xf(h)&=2x^TAh = <\nabla_xf,h> = \nabla_xf^Th\\
&\to \nabla_xf^T=2x^TA\\
&\to \nabla_xf = 2A^Tx
\end{aligned}\\
$$

3.

$$
\begin{aligned}
f:\mathcal M_n(\mathbb R)&\to\mathbb R\\
X&\mapsto tr^2(X)
\end{aligned}\\
\begin{aligned}
f(X+H) &= tr^2(X+H) = (tr(X+H))^2 = (tr(X)+tr(H))^2\\
&= \underbrace{tr^2(X)}_{f(X)} + \underbrace{2tr(X)tr(H)}_{d_Xf(H)}+\underbrace{tr^2(H)}_{o(h)}
\end{aligned}\\
\begin{aligned}
d_Xf:H&\mapsto 2tr(X)tr(H)\\
d_Xf(H)&=\nabla_Xf^TH=2tr(X)tr(H)
\end{aligned}
$$

4.

$$
\begin{aligned}
f:\mathcal M_n(\mathbb R)&\to M_n(\mathbb R)\\
B&\mapsto tr(AB)B
\end{aligned}\\
\begin{aligned}
f(B+H)&= tr(A(B+H))(B+H) = tr(AB+AH)(B+H)\\
&= \underbrace{tr(AB)B}_{f(B)} + \underbrace{tr(AB)H + tr(AH)B}_{d_Bf(H)} + \underbrace{tr(AH)H}_{o(h)}
\end{aligned}\\
\begin{aligned}
d_Bf:H&\mapsto tr(AB)H + tr(AH)B\\
d_Bf(H)&=Jac_B(f)\times H
\end{aligned}
$$

</details>

## Exercice 2-38

<details markdown="1">
<summary>Solution</summary>

$$
\begin{aligned}
f:\mathbb R^n&\to\mathbb R^n &A\in\mathcal M_n(\mathbb R\\
X&\mapsto <\color{blue}{\underbrace{AX+b}_{f_1(X)}}, \color{red}{\underbrace{tr(A)X}_{f_2(X)}}> &b\in\mathbb R^n
\end{aligned}
$$

<div class="alert alert-info" role="alert" markdown="1">
**Rappel**

$$
d_x<f,g>:h\mapsto<d_xf(h),g(x)> + <f(x),d_xg(h)>
$$
</div>

$$
d_xf_1:h\mapsto \color{green}{Ah}\\
f_2(x+h) = tr(A)(x+h)=tr(A)x+\underbrace{tr(A)h}_{d_xf_2:h\mapsto \color{orange}{tr(A)h}}
$$

Donc:

$$
\begin{aligned}
d_xf:h\mapsto d_x<f_1,f_2>(h)&= <\color{green}{d_xf_1(h)},\color{red}{f_2(x)}> + <\color{blue}{f_1(x)},\color{orange}{d_xf_2(h)}>\\
&= <Ah,tr(A)x> + <Ax+b,tr(A)h>
\end{aligned}\\
d_xf:h\mapsto <Ah,tr(A)x> + <Ax+b,tr(A)h>
$$

</details>

## Exercice 2-39

<details markdown="1">
<summary>Solution</summary>

1.

$$
\begin{aligned}
g:\mathbb R^n&\to \mathbb R\\
x&\mapsto \frac{1}{x^Tx+1}
\end{aligned}\\
$$

<div class="alert alert-info" role="alert" markdown="1">
**Rappel**

$$
d_xf\circ g = d_{g(x)}f\circ d_xg\\
d_xf\circ g(h) = d_{g(x)}f(d_xg(h))
$$
</div>

$$
g(x) = b\circ a(x)\\
\begin{aligned}
a:\mathbb R^n&\to \mathbb R\\
x&\mapsto x^Tx+1\\
d_xa:h&\mapsto 2x^Th 
\end{aligned}\\
\begin{aligned}
b:\mathbb R&\to \mathbb R\\
x&\mapsto \frac{1}{x}\\
d_xb:h&\mapsto hb'(x) = -\frac{1}{x^2}h 
\end{aligned}\\
d_xb(h) = -\frac{1}{x^2}h \quad d_xa(h)=2x^Th\\
\begin{aligned}
d_xb\circ a(h)&=d_{a(x)}b(\underbrace{d_xa(h)}_{y})\\
&= d_{a(x)}b(y)\\
&= -\frac{1}{(a(x))^2}y\\
&= -\frac{1}{(x^Tx+1)^2}y\\
&= -\frac{1}{(x^Tx+1)^2}2x^Th\\
\to d_xg:h&\mapsto-\frac{2x^Th}{(x^tx+1)^2}\equiv \biggr(\frac{1}{u(x)}\biggr)' = -\frac{u'(x)}{u(x)}
\end{aligned}
$$

2.

$$
\begin{aligned}
f:\mathbb R^n&\to \mathbb R\\
x&\mapsto \cos^2(x^TAx)
\end{aligned}\\
f(x) = b\circ a(x)\\
\begin{aligned}
a:\mathbb R^n&\to \mathbb R\\
x&\mapsto x^TAx\\
d_xa:h&\mapsto 2x^TAh\\
b:\mathbb R&\to \mathbb R\\
x&\mapsto \cos^2(x)\\
d_xb:h&\mapsto hb'(x) = -2\cos(x)\sin(x)h = -sin(2x)h
\end{aligned}\\
\begin{aligned}
d_xf(h) = d_xb\circ a(h) = d_{a(x)}b(\underbrace{d_xa(h)}_{y}) = d_{a(x)}b(y) &= -\sin(2a(x))y\\
&= -\sin(2x^TAx)y\\
&= -\sin(2x^TAx)2x^TAh
\end{aligned}
$$

</details>

## Exercice 3-42
*On calcule un gradient ou une jacobienne ?*

<details markdown="1">
<summary>Solution</summary>

1. Gradient
2. Jacobienne
3. Jacobienne
4. Gradient
5. Gradient
6. Gradient

</details>

## Exercice 3-43

$f:\mathbb R^3\to\mathbb R$ differentiable en tout point de $\mathbb R^3$

Soit $$\begin{aligned} g:\mathbb R^3&\to\mathbb R \\ (x,y,z)&\mapsto f(x-y,y-z,z-x) \end{aligned}$$

Montrer que 

$$
\frac{\partial g}{\partial x}(\alpha) + \frac{\partial g}{\partial y}(\alpha) + \frac{\partial g}{\partial z}(\alpha) = 0 \quad\forall \alpha=(a,b,c)\in\mathbb R^3
$$

<details markdown="1">
<summary>Solution</summary>

$$
\begin{aligned}
g(x,y,z) &=f(x-y,y-z,z-x)\\
&=f\circ u(x,y,z)
\end{aligned}
$$

avec $$\begin{aligned} u:\mathbb R^3&\to\mathbb R^3 \\ (x,y,z)&\mapsto (x-y,y-z,z-x) \end{aligned}$$

On vient de voir que 

$$
d_{\alpha}g:h\mapsto d_{\alpha} f\circ u(h)=\underbrace{d_{u(\alpha)}f(d_{\alpha}u(h))}_{Jac_{\alpha}g\times h=Jac_{u(\alpha)}f\times Jac_{\alpha}u\times h\mapsto Jac_{\alpha}g=Jac_{\underbrace{u(\alpha)}_{\beta\in\mathbb R^3=u(\alpha)}}f\times Jac_{\alpha}(u)}\\
u(x,y,z)=(\overbrace{x-y}^{u_1}, \overbrace{y-z}^{u_2}, \overbrace{z-x}^{u_3})\\
Jac_{(x,y,z)}u=\begin{bmatrix} \frac{\partial u_i}{\partial x_j} \end{bmatrix} = \begin{bmatrix} 1 &-1&0 \\ 0 & 1 &-1 \\ -1&0&1 \end{bmatrix}\\
\begin{aligned}
Jac_{\beta}f&=\nabla_{\beta}f^T\\
&= (\frac{\partial f}{\partial x}(\beta), \frac{\partial f}{\partial y}(\beta), \frac{\partial f}{\partial z}(\beta))\\
Jac_{\alpha}g&=\nabla_{\alpha}g^T \\
&=(\frac{\partial g}{\partial x}(\alpha), \frac{\partial g}{\partial y}(\alpha), \frac{\partial g}{\partial z}(\alpha))\\
\nabla_{\alpha}g^T&=\nabla_{\beta}f^T
\begin{bmatrix}
1 &-1 & 0\\
0 & 1 &-1\\
-1 & 0 & 1
\end{bmatrix}\\
&= (\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z})
\begin{bmatrix}
1 &-1 & 0\\
0 & 1 &-1\\
-1 & 0 & 1
\end{bmatrix}\\
&= (\frac{\partial f}{\partial x} - \frac{\partial f}{\partial z}, \frac{\partial f}{\partial y} - \frac{\partial f}{\partial x}, \frac{\partial f}{\partial z}- \frac{\partial f}{\partial y})\\
&= \frac{\partial g}{\partial x} + \frac{\partial g}{\partial y} + \frac{\partial g}{\partial z} = 0
\end{aligned}
$$

</details>