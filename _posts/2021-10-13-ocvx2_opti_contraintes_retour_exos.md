---
title:          "OCVX2 : Le retour de l'optimisation avec contraintes - Exercices"
date:           2021-10-13 16:00
categories:     [Image S9, OCVX2]
tags:           [Image, SCIA, S9, OCVX2]
math: true
---

Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/BJpLlvVrY)

# Exercice 1

$$
\begin{aligned}
\min f(x,y)&=2x+y\\
\text{tel que }3x^2+y^2&\le4
\end{aligned}
$$

<details markdown="1"><summary>Solution</summary>

$$
\begin{aligned}
3x^2+y^2&\le4\\
3x^2+y^2-4&\le0\\
g(x,y)&=3x^2+y^2-4
\end{aligned}\\
\mathscr L(x,y,\alpha)=2x+y+\alpha(3x^2+y^2-4)\\
\begin{cases}
\frac{\partial\mathscr L}{\partial x}=2+6\alpha x=0&\to x=-\frac{1}{3\alpha}\\
\frac{\partial \mathscr L}{\partial y}=1+2\alpha y=0&\to y=-\frac{1}{2\alpha}
\end{cases}\\
\begin{aligned}
\mathscr L(\equiv \theta_D(\alpha))&=2(-\frac{1}{3\alpha})+(-\frac{1}{2\alpha}) + \alpha(3(-\frac{1}{3\alpha})^2 + (-\frac{1}{2\alpha})^2 - 4)\\
&= -\frac{2}{3\alpha}-\frac{1}{2\alpha}+\alpha(\frac{1}{3\alpha^2}+\frac{1}{4\alpha^2}-4)\\
&= -\frac{1}{3\alpha}-\frac{1}{2\alpha}+\frac{1}{3\alpha}+\frac{1}{4\alpha}-4\alpha\\
&= -\frac{1}{3\alpha}-\frac{1}{4\alpha}-4\alpha\\
&= -\frac{7}{12\alpha}-4\alpha
\end{aligned}\\
\begin{aligned}
\nabla_{\alpha}\theta_D(\alpha)&=\frac{7}{12\alpha^2}=0\\
&=\frac{7}{12\alpha^2}=4\\
&=\frac{1}{4}\frac{7}{12}=\alpha^2\\
\alpha&=\frac{1}{2}\sqrt{\frac{7}{12}}=\frac{1}{4}\sqrt{\frac{7}{3}}
\end{aligned}
$$


Autre methode, en utilisant la complementarite:

$$
\begin{aligned}
\alpha^*g(x^*,y^*)&=0\\
\alpha^*=(3(-\frac{1}{3\alpha^*})+(-\frac{1}{2\alpha^*})^2)&=0\\
\alpha^*(\frac{1}{3\alpha^{*^2}}+\frac{1}{4\alpha^{*^2}}-4)&=0\\
\frac{1}{3\alpha^*}+\frac{1}{4\alpha^*}-4\alpha^*&=0\\
\frac{7}{12\alpha^*}&=4\alpha^*\\
\frac{1}{4}\frac{7}{12}&=\alpha^{*2}\\
\alpha^*&=\frac{1}{4}\sqrt{\frac{7}{3}}
\end{aligned}
$$

</details>

# Exercice 2

$$
\begin{aligned}
\min_{x\in\mathbb R^3}&\frac{1}{2}(x_1^2+x^2_2+x_3^2)\\
\text{tel que } &x_1+x_2+2x_3-1=0\\
&x_1+4x_2+2x_3-3=0
\end{aligned}
$$

Sous forme matricielle: 

$$
\boxed{\begin{aligned}
\min &\frac{1}{2}x^Tx\\
\text{tel que } &Ax-b =0
\end{aligned}
}\\
x=\begin{pmatrix}x_1 \\ x_2 \\ x_3\end{pmatrix}\\
A=\begin{pmatrix}1&1&2 \\ 1&4&2\end{pmatrix}\\
b=\begin{pmatrix}1 \\ _3\end{pmatrix}\\
$$

<details markdown="1"><summary>Solution</summary>

$X=\{S_1,\dots,S_N\}$ avec proba discrete $p_i=\mathbb P(X=S_i)$ et $\sum_{i=1}^Np_i=1$.

<div class="alert alert-info" role="alert" markdown="1">

**Entropie de Shannon**

$$
H(\mathbb P=(p_1,\dots,p_n))=-\sum_{i=1}^Np_i\log_2(p_i)\\
\log_2(x)=\frac{\ln(x)}{\ln(2)}
$$

</div>

La distribution qui maximise l'entropie est la distribution uniforme.

On cherche a maximiser 

$$
H(x)=-\sum_{i=1}^nx_i\log_2(x_i)\quad\text{pour }x=\begin{pmatrix}x_1 \\ \vdots \\ x_n\end{pmatrix}\in\mathbb R^2\\
\text{tel que} \sum_{i=1}^nx_i=1\\
$$

On cherche a minimiser

$$
-H(x)=\sum_{i=1}^nx_i\log_2(x_i)\\
\text{tel que }\sum_{i=1}^nx_i-1=0\\
\to h(x)=\sum_{i=1}^nx_i-1\quad\text{affine}\\
\begin{aligned}
\mathscr L(x,\beta)&=-H(x)+\beta h(x)\\
&= \sum_{i=1}^nx_i\log_2(x_i)+\beta(\sum_{i=1}^nx_i-1)
\end{aligned}\\
\begin{aligned}
\nabla_x\mathscr L(x,\beta)=0&\Leftrightarrow\forall i,\begin{cases}
\frac{\partial \mathscr L}{\partial x_i}=0\\
\frac{\partial\mathscr L}{\partial x_i}=\frac{\partial}{\partial x_i}(x_i\log_2(x_i))+\beta\\
\end{cases}\\
&\Leftrightarrow\begin{cases}
\frac{d}{dx}(x\log_2 x)=\log_2x+x\frac{d}{dx}\log_2x\\
\frac{d}{dx}\log_2x=\frac{d}{dx}\frac{\ln(x)}{\ln(2)}=\frac{1}{x\ln(2)}
\end{cases}
\end{aligned}\\
\begin{aligned}
\frac{\partial \mathscr L}{\partial x_i}&=\frac{\partial}{\partial x_i}(x_i\log_2(x_i))+\beta\\
&=\log_2(x_i)+x_i\frac{1}{x_i\ln(2)}+\beta\\
&=\frac{\ln(x_i)+1}{\ln(2)}+\beta=0
\end{aligned}\\
\begin{aligned}
\frac{\ln x_i+1}{\ln 2}&=-\beta\\
\ln x_i+1&=-\beta\ln 2\\
\ln x_i &= -\beta\ln(2)-1\\
x_i&=e^{-(\beta\ln 2+1)}\quad\forall i
\end{aligned}
$$

Avec la contrainte:

$$
\begin{aligned}
\sum_{i=1}^nx_i&=1\\
\sum_{i=1}e^{-(\beta\ln2+1)}&=1\\
ne^{-(\beta)}\\
ne^{-(\eta\ln 2+1)}&=1\\
\underbrace{e^{-(\beta\ln 2+1)}}_{x_i}&=\frac{1}{n}
\end{aligned}
$$

La distribution qui maximise l'entropie est donc $x_i=\frac{1}{n}$ $\forall i=1\dots n$ $\equiv$ distribution uniforme

</details>
