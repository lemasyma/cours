---
title:          "OCVX: Differentielles (le retour)"
date:           2021-04-12 10:00
categories:     [Image S8, OCVX]
tags:           [Image, SCIA, OCVX, S8]
description: Differentielles (le retour)
---

Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/ryJGRObI_)

# La differentielle en TOP-DOWN
La semaine derniere, vous avez cherche a generaliser la notion de derivabilite d'une fonction $\phi:\mathbb R\to\mathbb R$ a celle de differentiabilite d'une fonction $f:\mathbb R^n\to\mathbb R$.

Le point de vue aborde: on sait deriver le long d'un vecteur $v\in\mathbb R^n$, cad qu'on sait deriver la fonction

$$
t\mapsto f(\overbrace{a}^{\text{le pt qu'on} \\ \text{cherche a deriver}}+tv)
$$

A partir de la on cherche a construire un objet multidimensional qui va remplacer la derivee dans le cas unidimensionnel.

On sait deriver une fonction de $\mathbb R\to\mathbb R$ 
$\to$ On sait donc deriver une fonction de $\mathbb R^n\to\mathbb R$ le long d'un vecteur $v$ (en particulier le long des axes).
$\to$ On regroupe les derivees le long des axes dans un objet qu'on appelle le gradient
$\to$ Definition de la differentielle en un point

<div class="alert alert-danger" role="alert" markdown="1">
C'est la demarche BOTTOM-UP
</div>

## Aujourd'hui
On va generaliser la notion de derivabilite d'une fonction de $\mathbb R\to\mathbb R$ a l'aide des normes sur $\mathbb R^n$
$\to$ Analyser "*l'objet differentiel*" qu'on obtient et decrire une partie des proprietes qu'il a
$\to$ retrouver les derivees partielles comme ecriture en coordonnnees de la differentielle en un point

<div class="alert alert-danger" role="alert" markdown="1">
C'est la demarche TOP-DOWN
</div>

# Rappel sur $\mathbb R$

<div class="alert alert-info" role="alert" markdown="1">
Etant donne une fonction $\phi:\mathbb R\to\mathbb R$ on dit que $\phi$ est derivable en $a\in\mathbb R$ si $$\lim_{h\to a}\frac{\phi(a+h)-\phi(a)}{h}$$ existe. Dans ce cas cette limite est appelee le nombre derivee de $\phi$ en $a$ et on le note $\phi'(a)$
</div>

## De maniere equivalente
<div class="alert alert-success" role="alert" markdown="1">
$\phi$ est derivable en $a$ s'il existe un nombre reel $\alpha$ tel que pour $h$ assez petit (h proche de 0)

$$
\phi(a+h)=\phi(a)+\alpha h + h\underbrace{\varepsilon(h)}_{\begin{aligned}\varepsilon(h)&\to0\\h&\mapsto0\end{aligned}}
$$

Dans ce cas $\alpha$ est le nombre derivee de $\phi$ en $a$ et on le note $\phi'(a)$
</div>

<div class="alert alert-info" role="alert" markdown="1">
Dans $\mathbb R$: si $\phi$ est derivable en $a$ alors

$$
\forall h\text{ assez petit}\quad \phi(a+h)=\phi(a)+\phi'(a)h+h\varepsilon(h)
$$
</div>

# Proposition d'extension au cas d'une fonction $f:\mathbb R^n\to\mathbb R$
f est differentiable en $a$ si

$$
\forall \underbrace{h}_{\in\mathbb R^n}\underbrace{\text{ assez petit}}_{\exists\eta\gt0\text{ tq }h\in\mathcal B(0,\eta)}\quad f(a+h)=f(a) +\overbrace{\lambda_a(h)}^{\text{lineaire en }h}+ \Vert h\Vert\overbrace{\underbrace{\varepsilon(h)}_{\begin{aligned}\varepsilon:\mathbb R^n&\to\mathbb R \\ \varepsilon(h)&\to0\\h&\mapsto0\end{aligned}}}^{\text{pas lineaire en }h}
$$

$h$ varie de tel sorte a ce qu'on reste dans la boule $\mathcal B(0,\eta)$
![](https://i.imgur.com/KVZ6sPS.png)

<div class="alert alert-info" role="alert" markdown="1">
**Definition**: une fonction $f:\mathbb R^n\to\mathbb R$ est differentiable en un point $a\in\mathbb R^n$ s'il existe une application lineaire $\lambda_a:\mathbb R^n\to\mathbb R$ telle que

$$
\forall h\text{ assez petit}:\quad f(a+h)=f(a)+\lambda_a(h)+\Vert h\Vert\underbrace{\varepsilon(h)}_{\begin{aligned}\varepsilon(h)&\to0\\h&\mapsto0\end{aligned}}\quad\color{orange}{(D_1)}
$$
</div>

<div class="alert alert-warning" role="alert" markdown="1">
On ne precise pas la norme car elles sont equivalentes.
</div>

Question: *Pour $f$ donne, combien y a-t-il d'applications lineaires qui satisfait $\color{orange}{D_1}$ ?*
Il n'y a qi'une seule, qu'on appelle la differentielle en $a$.

<div class="alert alert-info" role="alert" markdown="1">
**Lemme**: Si $\lambda_a$ existe, elle est unique.
</div>

## Preuve
On suppose qu'il existe 2 applications lineaires $\lambda_a$ et $\mu_a$ qui satisfont $\color{orange}{(D_1)}$, cad

$$
\begin{aligned}
\forall h\text{ assez petit}:\quad f(a+h)&=f(a)+\lambda_a(h)+\Vert h\Vert\varepsilon_1(h)\\
-f(a+h)&=f(a)+\mu_a(h)+\Vert h\Vert\varepsilon_2(h)\\
\overbrace{\underbrace{(\lambda_a-\mu_a)}_{\text{Une app lineaire en }h}}^{\text{On va montrer que} \\ \text{c'est l'app lineaire nulle}}(h)&=\Vert h\Vert(\underbrace{\varepsilon_1(h)-\varepsilon_2(h)}_{\begin{aligned}\varepsilon:\mathbb R^n&\to\mathbb R \\ \varepsilon(h)&\to0\\h&\mapsto0\end{aligned}})
\end{aligned}
$$

On est dans la situation suivante:

$$
\forall h\in\mathcal B(0,\eta)\text{ pour }\eta\gt0\quad\underbrace{\psi}_{\text{lineaire}}(h)=\Vert h\Vert\underbrace{\varepsilon(h)}_{\begin{aligned} \varepsilon(h)&\to0\\h&\mapsto0\end{aligned}}
$$

### Demonstration: Ma $\psi$ est nulle
On va prendre un vecteur $$\overbrace{v\in\mathbb R^n}^{\Vert v\Vert=1}$$, soit $t\in]-\eta,\eta[$ (donc $tv\in\mathcal B(0,\eta)$)

On a: 

$$
\begin{aligned}
\psi(tv)=\Vert tv\Vert\varepsilon(tv)&\Leftrightarrow t\psi(v)=\Vert t\Vert\Vert v\Vert\varepsilon(tv)\\
&\Leftrightarrow signe(t)\frac{\psi(v)}{\Vert v\Vert}=\varepsilon(tv)
\end{aligned}
$$

Si on se limite a $t\in[0,\eta[$, on a $\frac{\psi(v)}{\Vert v\Vert}=\varepsilon(tv)$

Dans la relation

$$
\forall t\in[0,\eta]\quad \frac{\psi(v)}{\underbrace{\Vert v\Vert}_{\text{constant}}}=\underbrace{\varepsilon(tv)}_{\begin{aligned}\varepsilon(tv)&\to0\\t&\mapsto0\end{aligned}}\\
\Rightarrow\psi(v)=0
$$

Etant donne un vecteur $v\in\mathbb R^n$, $\Vert v\Vert=1$, $\psi(v)=0$.
En particulier, $\forall i\in\text{{}1,...,n\text{}}$; $\psi(e_i)=0$
Donc la matrice de $\psi$ dans la base canonique est nulle, i.e. $\psi = 0$
<div class="alert alert-success" role="alert" markdown="1">
Donc $\lambda_a=\mu_a$
</div>

<div class="alert alert-info" role="alert" markdown="1">
**Definition**: On appelle differentielle de $f:\mathbb R^n\to\mathbb R$ au point $a$, l'unique application lineaire (si elle existe) qui satisfait:

$$
\color{orange}{D_{abs}}: \quad f(a+h)=f(a)+Df(a)(h)+\Vert h\Vert\underbrace{\varepsilon(h)}_{\begin{aligned}\varepsilon(h)&\to0\\h&\mapsto0\end{aligned}}
$$
</div>

Dans ce contexte, $Df(a)$ a une matrice dans la base canonique de taille $(1,n)$

## Exemple
1.On note $$\begin{aligned}f:\mathbb R^n&\to\mathbb R \\ h&\to \underbrace{A}_{A\text{ est une matrice ligne}}h+n\end{aligned}$$ 

$$
\begin{aligned}
f(a+h)&=A(a+h)+b\\
&= Aa + Ah +b\\
&=(\underbrace{Aa+b})+Ah\\
&=f(a) + \underbrace{Ah}_{\text{lineaire en }h} + \underbrace{o}_{\Vert h\Vert\varepsilon(h) \\ \varepsilon \text{ est nul la}}
\end{aligned}
$$

D'apres la definition:

$$
Df(a)(h) = Ah\\
Df(a):h\to Ah
$$

2.
$$
f:\mathbb R^n\to\mathbb R\\
x\to x^Tx\\
\begin{aligned}
f(a+h)&=(a+h)^T(a+h)\\
&=aTa+h^Ta+a^Th+\overbrace{h^Th}^{\Vert h\Vert_2\Vert h\Vert_2}\\
&=f(a) +\underbrace{2a^Th}_{\text{lineaire en }h} +\Vert h\Vert \varepsilon(h)
\end{aligned}\\
$$

<div class="alert alert-info" role="alert" markdown="1">
**Definition (rappel)**:

$$
\Vert h\Vert_2+\sqrt{h^Th}
$$
</div>

**Remarque**: $h^Ta\in\mathbb R$, $(h^Ta)^T=h^Ta\Rightarrow a^Th^{T^T}=a^Th$ car ce sont des **reels**.

<div class="alert alert-success" role="alert" markdown="1">
Donc $Df(a):h\to2a^Th$
</div>

Dans le cas $n=1$

$$
\begin{aligned}
f:x&\to x^2\\
D f(a):h&\mapsto Df(a)(h)\\
f'(a)&=2a
\end{aligned}
$$

## Proprietes usuelles
Les proprietes usuelles de derivabilites et de calcul des derivees s'etend au cas des fonctions de $\mathbb R^n\to\mathbb R$. Soient $f,g:\mathbb R^n\to\mathbb R$ et $a\in\mathbb R^n$, on suppose $f,g$ differentiable en $a$.

$$
\begin{aligned}
\forall h\text{ AP}\quad f(a+h)&=f(a)+D f(a)(h)+\Vert h\Vert\varepsilon_1(h)\\
g(a+h)&=f(a)+D g(a)(h)+\Vert h\Vert\varepsilon_2(h)\\
(+):(f+g)(a+h)&=(f+g)(a)+(\underbrace{D f(a)+D g(a)}_{\text{lineaire en }h})(h)+\Vert h\Vert (\underbrace{\varepsilon_1(h)+\varepsilon_2(h)}_{\varepsilon(h)})
\end{aligned}
$$

<div class="alert alert-danger" role="alert" markdown="1">
$$
D(f+g)(a)=D f(a)+D g(a)
$$
</div>

$$
(\times):(fg)(a+h)=(fg)(a) + f(a)D g(a)(h)+g(a)D f(a)(h)\\
+D f(a)(h)D g(a)(h)+\\
\Vert h\Vert\varepsilon_1(h)D g(a)(h) + \Vert h\Vert\varepsilon_2(h)D f(a)(h) +\\
\Vert h\Vert^2\varepsilon_1(h)\varepsilon_2(h) + \Vert h\Vert(\varepsilon_1(h)g(a) + \varepsilon_2(h)f(a))\\
\color{red}{D(fg)(a)=f(a)D g(a)+g(a)D f(a)}\\
\color{orange}{D (fg)(a):h\to f(a)D g(a)(h) + g(a)D f(a)(h)}
$$

## Matrice ligne
La differentielle de $f:\mathbb R^n\to\mathbb R$ en $a$ quand elle existe est une matrice ligne: *comment en decrire les coeffs ?*

<div class="alert alert-info" role="alert" markdown="1">
**Definition**(temporaire): Quand $f$ est differentiable au point $a$ on appelle gradient de $f$ en $a$ le vecteur $v$ (colonne) $\nabla f(a)$ dont la transposee est la marice de $Df(a)$ dans les bases canoniques
</div>

On a donc: pour tout $h$ assez petit

$$
f(a+h)=f(a)+\nabla f(a)^Th+\Vert h\Vert \underbrace{\varepsilon(h)}_{\begin{aligned}\varepsilon(h)&\to0\\h&\mapsto0\end{aligned}}
$$

On est interesse par calculer $\nabla f(a)^Te_i$ $\forall i\in\text{{}1,...,n\text{}}$

Soit $t\in\mathbb R$

$$
f(a+t_{e_i})=f(a)+\nabla f(a)^T(te_i)+\Vert te_i\Vert\varepsilon(te_i)\\
\Leftrightarrow f(a+t_{e_i})-f(a)=t\nabla f(a)^Te_i+\Vert te_i\Vert\varepsilon(te_i)\\
\frac{\Leftrightarrow f(a+t_{e_i})-f(a)}{t}=\nabla f(a)^Te_i+\Vert e_i\Vert\varepsilon'(te_i)\quad t\neq0\\
\Leftrightarrow\nabla f(a)^Te_i=\underbrace{\frac{f(a+te_i)}{t}}_{\to_{t\to 0}\delta e_if(a)=\frac{\delta}{\delta x_i}f(a)}-\underbrace{\Vert e_i\Vert\varepsilon'(te_i)}_{t\to0 \\ \to 0}
$$

En prenant la limite on vient de constater (avec la definition temporaire de $\nabla f(a)$) que $\nabla f(a)^Te_i=\frac{\delta}{\delta x_i}f(a)$

Cad que la ieme coordonnee de votre gradient c'est la derivee partielle par rapport a $x_i$

<div class="alert alert-info" role="alert" markdown="1">
**Defintion**: Le gradient d'une fonctino $f$ en un point $a\in\mathbb R^n$ c'est le vecteur $v$ des derivees partielles: 

$$
\nabla f(a)=\biggr(\frac{\delta f}{\delta x_i}(a)\biggr)_{1\le i\le n}
$$

</div>

<div class="alert alert-danger" role="alert" markdown="1">
Les definitions "temporaire" et definitives de gradient ne sont pas equivalentes: on peut admettre des derivees partielles sans etre differentiable
</div>

<div class="alert alert-info" role="alert" markdown="1">
**Prop**: Si une fonction $f:\mathbb R^n\to\mathbb R$ admet un gradient en un point $a$, et si $x\to\nabla f(x)$ est **continue** au voisinage de $a$, alors $f$ est differentiable en $a$, cad qu'on peut ecrire

$$
\forall h \text{ assez petit}\\
f(a+h)=f(a)+\nabla f(a)^Th+o_a(h)
$$
</div>

**Remarque**: si $f$ est differentiable en $a$:

$$
\underbrace{\delta_v f(a)}_{\color{red}{\text{derivee directionnelle de } f\\ \text{en } a \text{ le long de } v}}=\nabla f(a)^Tv
$$

# Derivee d'une composee
Pour parler de composee on va generaliser un petit peu le cadre avec lequel on a travaille jusque la.
On s'interesse donc aux fonctions

$$
f:\mathbb R^n\to\mathbb R^n
$$

On note $f_1,...,f_n$ les fonctions coordonnees de $f$, $f=(f_1,...,f_n)$

## Exemple

$$
\begin{aligned}
g:\mathbb R^2&\to\mathbb R^3\\
(x,y)&\mapsto \begin{pmatrix}\cos(xy) \\ x^2+y \\ 2y\end{pmatrix}\\
g_1:\mathbb R^2&\to\mathbb R\\
(x,y)&\mapsto \cos(xy)\\
g_2:\mathbb R^2&\to\mathbb R\\
(x,y)&\mapsto x^2+y\\
g_3:\mathbb R^2&\to\mathbb R\\
(x,y)&\mapsto 2y\\
\end{aligned}
$$

Une fonction $f:\mathbb R^n\to\mathbb R^m$ va etre dite differentielle si on a une ecriture:

$$
f(a+h)=f(a)+\underbrace{Df(a)}_{\text{differentielle de } f\\ \text{en } a,\text{de matrice}\\ \text{dans les bases canoniques}\\ \text{de taille: }(m,n)}(h)+\underbrace{\Vert h\Vert}_{\text{une norme sur }\mathbb R^n}\underbrace{\varepsilon(h)}_{\begin{aligned}\varepsilon:\mathbb R^n&\to\mathbb R^m \\ \varepsilon(h)&\to0\\h&\mapsto0\end{aligned}}
$$

<div class="alert alert-success" role="alert" markdown="1">

La matrice de $\lambda f(a)$ dans les bases canoniques est appellee la **jacobienne** de $f$ en $a$.

$$
J_f(a)=\begin{pmatrix}
\frac{\delta f_1(a)}{\delta x_1}&\dots &\frac{\delta f_1(a)}{\delta x_n}\\
\vdots&\ddots&\vdots\\
\frac{\delta f_m(a)}{\delta x_1}&\dots &\frac{\delta f_m(a)}{\delta x_n}\\
\end{pmatrix}\\
=\begin{pmatrix}
\nabla f_1(a)^T\\
\vdots\\
\nabla f_m(a)^T
\end{pmatrix}\\
= (\nabla f_1(a),...,\nabla f_m(a))^T\\
$$
</div>

Pour $f:\mathbb R^n\to\mathbb R^m$ si on est differentiable en $a\in\mathbb R^n$
On a $\forall h$ AP:

$$
f(a+h)=f(a)+J_{f}(a)h+o_a(h)
$$

## Question:
Soit $f,g$, $f:\mathbb R^n\to\mathbb R^m$, $g:\mathbb R^m\to\mathbb R^p$, si $f$ et $g$ sont differentiable respectivement $f$ en $a$ et $g$ en $b=f(a)$ alors

$$
D(g\circ f)(a)=D g(\color{red}{f(a)})\circ D f(\color{red}{a})
$$

Matriciellement: 

$$
J_{g\circ f}(a) = J_g(f(a))\times J_f(a)
$$
