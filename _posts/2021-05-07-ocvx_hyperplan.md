---
title:          "OCVX: Hyperplan d'appui"
date:           2021-05-07 10:00
categories:     [Image S8, OCVX]
tags:           [Image, SCIA, OCVX, S8]
description: Hyperplan d'appui
---

Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/SydX3IWOd)

# Rappels
- Hyperplan d'appui a une partie $A$ de $\mathbb R^n$ en un point $p\in A$, est un hyperplan affine de $\mathbb R^n$ qui laisse $A$ dans un des deux demi-espaces definis par $H$

Etant donne un vecteur normal $\vec \nu$ definissant $H\in\mathbb R^n$ et $p$ un point dans $H\cap A$ on a

$$
\forall x\in A; <\vec\nu, x-p>\le 0
$$

![](https://i.imgur.com/MARQHLr.png)

- On a definit par ailleurs la notion de gradient d'une fonction differentiable $f:\mathbb R^n \to \mathbb R$ en un point $a$, determinee par la relation:

$$
\forall h\text{ assez petit}\\
f(a+b) = f(a) + \nabla f(a)^Th + \underbrace{\varepsilon(h)\Vert h\Vert}_{\varepsilon(h) \to 0 \\ h\to0}
$$

![](https://i.imgur.com/MHYc9iH.png)

# Plan du cours
<div class="alert alert-success" role="alert" markdown="1">
**Objectif d'aujourd'hui**
1. Etendre la notion de droite tangente au graphe d'une fonction $f:\mathbb R\to\mathbb R$
    1. Au cas des fonctions $\phi:\mathbb R^n\to\mathbb R$
    2. au cas des parties de $\mathbb R^n$ decrites comme courbes de niveaux de fonctions
2. Utiliser le point 1. pour obtenir une lieuristique, permettant de construire des methodes iteratives d'optimisation
</div>

1. Revoir la notion de droite tangente dans le cas $\mathbb R$ (une dimension)
    - $f:\mathbb R\to\mathbb R$
    - Graphe
2. On va definir une maniere de generaliser la notion de droite tangente
    - $f:\mathbb R\to\mathbb R$
    - Graphe
3. On adapte cette definition au cas de courbes de niveaux
    - $g:\mathbb R^2\to\mathbb R$
    - zeros de $g$ (courbes de niveau de $g$)
4. Conclusion pour le cas general
    - $\phi:\mathbb R^n\to\mathbb R$

# Espace tangent

Le gradient en dimension 1 correspond a la notion de derivee, qui permet de definir la notion de droite tangente au graphe d'une fonction en un point. Dans ce contexte, l'interpretation geometrique de la notion de gradient est connue. En particulier le fait que vous soyez croissants ou decroissant vous est donne par le signe de votre gradient; cela vous permet de savoir dans quelle direction aller si vous cherchez des points ou votre fonction a des plus petite ou plus grandes valeurs.

*Que signifie un nombre positif ou negatif pour un vecteur de $\mathbb R$ ?*
Si on est positif (resp. negatif), on est dans la moitie positive(resp. negative) de notre droite reelle.

![](https://i.imgur.com/TCRQgTl.png)
$$
Q: \min_{x\in\mathbb R}f(x)
$$
On cherche a minimiser la fonction $f$

Dans ce dessin, le signe de la derivee vous dit que si vous voulez chercher des points $x$ avec $f(x)\le f(a)$, il faut aller dans le sens oppose a $f'(a)$.

La droite $D_{f,p}$ est derivee parametriquement par 

$$
\begin{aligned}
\mathbb R&\to^{\lambda}\mathbb R^2\\
t&\mapsto (a+t, f'(a)t + f(a))\color{green}{= (a, f(a)) + t(1, f'(a))}\color{red}{=P}
\end{aligned}
$$

![](https://i.imgur.com/5ULPhtA.png)

On est en train de dire que $D_{f,p}$ est la droite passant par $p$, de direction $Vect\biggr((1,f'(a))\biggr)$

Cette notion de droite tangente ne semble pas, telle quelle, facilement generalisable au cas de fonctions de $\mathbb R^n\to\mathbb R$

<div class="alert alert-info" role="alert" markdown="1">
**Definition**
Soit $A$ une partie de $\mathbb R^n$, soit $p\in A$. On appelle $$\color{red}{\text{germe d'une courbe (derivable) } \gamma:\underbrace{]-\varepsilon,\varepsilon[}_{\varepsilon\gt0}\to A\text{ tel que }\gamma(0)=p}$$, la derivee de $\gamma$ en $0$
</div>

Cela correspond au vecteur vitesse en $p$ d'un point materiel passant par $p$ a l'instant 0, si $\gamma$ decrit la position de ce point en fonction du temps $t$.

![](https://i.imgur.com/b0idTMk.png)

<div class="alert alert-danger" role="alert" markdown="1">
L'ensemble des germes de courbes en $p$ definit un sous-espace vectoriel de $\mathbb R^n$. 
$\color{orange}{\text{On le note }T_{A,p}\text{, il s'appelle espace tangent a }A\text{ en }p}$.
</div>

*Que donne $\color{orange}{T_{A,p}}$ dans le cas du graphe de $f$?*

Si $A$ est $\Gamma_f$ (graphe de $f$) toute courbe passant par $p$ $\gamma:]-\varepsilon,\varepsilon[\to\Gamma_f$ est de la forme:

$$
\gamma(t) = \underbrace{(\psi(t), f(\psi(t)))}_{\color{orange}{\psi(t), \phi(t)}} \quad \text{pour }\psi:]-\varepsilon,\varepsilon[\to\mathbb R
$$
avec $\psi(0) = a$

Si $\gamma$ est derivable en 0:

$$
\gamma'(0) = (\psi'(0),\psi'(0)f'(a)) = \psi'(0)(1,f'(a))
$$

<div class="alert alert-success" role="alert" markdown="1">

$$
\Rightarrow \gamma'(0)\in Vect\biggr((1,f'(a))\biggr)\Rightarrow T_{A,p}\subseteq Vect\biggr((1,f'(a))\biggr)
$$

</div>

<div class="alert alert-danger" role="alert" markdown="1">
**Conclusion**

$$
T_{A,p} = Vect\biggr((1, f'(a))\biggr)
$$

autrement dit: $D_{f,p} = p + T_{A,p}$
</div>

<div class="alert alert-info" role="alert" markdown="1">
**Definition**
Etant donne une partie $A\subseteq\mathbb R^n$ et $p\in A$, on appelle espace tangent a $A$ en $p$ l'espace vectoriel $T_{A,p}$ compose des germes de courbes dans $A$ passant par $p$.
</div>

**Remarque:** Geometriquement, on represente souvent $p+T_{A,p}$ et non $T_{A,p}$

Notre prochaine etape est de reinterpreter $p+T_{A,p}$ de maniere implicite de facon a faire apparaitre la notion de gradient d'une fonction $\mathbb R^n\to\mathbb R$.

On a $D_{f,p}: (a,f(a)) + t(1,f'(a))$ pour $t\in\mathbb R$.

*Comment obtenir une ecriture implicite de $D_{f,p}$ ?*
Si $(x,y)\in D_{f,p}$ alors

$$
\begin{cases}
x = a + t\\
y = f(a) + f'(a)t
\end{cases}
\Leftrightarrow f'(a)(x-a) = y - f(a)
$$

## Questions
1. *Comment ecrit-on $\Gamma_f$ comme zeros d'une fonction ?*
2. *Quel est le gradient de cette fonction au point $p$ ?*
3. *Quel est $\perp$ de ce gradient au point $p$ ?*

### Premiere question
$\Gamma_f$ est zeros de la fonction:

$$
\begin{aligned}
\phi:\mathbb R^2&\to\mathbb R\\
(x,y) &\mapsto f(x)-y
\end{aligned}\\
\begin{aligned}
z(\phi) = \text{{}(x,y)\vert f(x)-y=0\text{}} &= \text{{}(x,y)\vert f(x)=y\text{}}\\
&= \text{{}(x,f(x))\vert x\in\mathbb R\text{}}\\
&= \Gamma_f
\end{aligned}
$$

### Deuxieme question

$$
\nabla\phi((a,f(a))) = \begin{pmatrix}\frac{\partial\phi}{\partial x}(a,f(a)) \\ \frac{\partial\phi}{\partial y}(a,f(a)) \end{pmatrix} = \begin{pmatrix}f'(a) \\ -1\end{pmatrix}\\
\phi(x,y) = f(x) - y
$$

Ce qui genere notre droite tangente c'est $(1, f'(a))$ et on a obtenu le vecteur $(f'(a), -1)$.

<div class="alert alert-success" role="alert" markdown="1">
On a obtenu un vecteur orthogonal a notre droite tangente
</div>

### Troisieme question

L'orthogonal a $\nabla\phi(p)$ au point $p$:

$$
\nabla\phi(p)^T
\begin{pmatrix}
x - a \\ y-f(a)
\end{pmatrix} =
\begin{pmatrix}
f'(a) \\ -1
\end{pmatrix}
\begin{pmatrix}
x - a \\ y - f(a)
\end{pmatrix} = f'(a)(x-a)- ( y - f(a))
$$

<div class="alert alert-success" role="alert" markdown="1">
$\perp\nabla\phi(p): f'(a)(x-a) = y-f(a)$ ($\perp$ passant par $p$)
</div>

*"Vectorialise"*: $f'(a)x = y \Leftrightarrow\nabla\phi(p)^T \begin{pmatrix}x \\ y\end{pmatrix} = 0$

<div class="alert alert-danger" role="alert" markdown="1">
$\nabla\phi(p)$ nous donne $T_{\Gamma_{f,p}}$, Autrement dit:

$$
D_{f,p}:p + \underbrace{\nabla\phi(p)^{\perp}}_{\color{orange}{T_{\Gamma_{f,p}}}}
$$
</div>

<div class="alert alert-info" role="alert" markdown="1">
**Prop**
Soit $f:\mathbb R^n\to\mathbb R$ une fonction differentiable en un point $p\in\mathcal C_{f,r}$. L'espace tangent a $\mathcal C_{f,r}$ au point $p$ est donne par l'hyperplan orthogonal ($\perp$) a $\nabla f(p)$.
</div>

## Question: *Calculer l'espace tangent au point $(1, 1)$ de $\mathcal C_{f,r}$ pour $$\begin{aligned}f:\mathbb R^2&\to\mathbb R \\ (x,y)&\mapsto x^2+y^2\end{aligned}$$*

$$
\begin{aligned}
\nabla f(x,y) = \begin{pmatrix}2x \\ 2y\end{pmatrix}; \quad \nabla f(1,1)^T\begin{pmatrix}x \\ y\end{pmatrix} &= 0\\
\Leftrightarrow 2x+2y &=0\\
\Leftrightarrow x+y&=0
\end{aligned}
$$

![](https://i.imgur.com/gerHRU3.png)

![](https://i.imgur.com/1O0np3R.png)


# Apport de la convexite

## Rappel
<div class="alert alert-info" role="alert" markdown="1">
Une fonction $f:\mathbb R^n\to\mathbb R$, differentiable, est convexe si $\forall x,y\in\mathbb R^n$

$$
f(y)- f(x) \ge\nabla f(x)^T(y-x)\qquad \text{(E)}
$$
</div>

## Hypothese

<div class="alert alert-danger" role="alert" markdown="1">
**Hypothese**
$f:\mathbb R^n\to\mathbb R$ une fonction convexe
</div>

Dans ce cas $\forall r\in\mathbb R$, $\mathcal C_{f\le r}$ est convexe $\subseteq\mathbb R^n$

![](https://i.imgur.com/YJrHOT4.png)

![](https://i.imgur.com/KeZxqwf.png)

Ici, $$\forall y\in\mathcal C_{f_1\le v}$$, $\nabla f(x)^T(y-a)\le0$. Donc $x+\nabla f(x)^{\perp}$ est un hyperplan d'appui a $$\mathcal C_{f_1\le v}$$

<div class="alert alert-success" role="alert" markdown="1">
Convexite: $f(y)-f(x)\ge\nabla f(x)^T(y-x)$
</div>

Donc le demi-espace positif est a exclure si l'on souhaite chercher un point $x^+$ tel que $f(x^+)\le f(x)$

<div class="alert alert-danger" role="alert" markdown="1">
On vient d'eliminier toute une partie de l'espace de nos recherches.
</div>

## Question: *Dans quelle direction chercher ?*
<div class="alert alert-info" role="alert" markdown="1">
**Prop**
Soit $f:U\subset\mathbb R^n\to\mathbb R$ une fonction differentiable. Soit $x\in\mathcal C_{f,r}$, si $\nabla f(x)\neq 0$ $\exists x^+=x+\Delta x$ tel que $f(x)\ge f(x^+)$ detour, par un deplacement $\Delta x$ a l'oppose de la direction de $\nabla f(x)$
</div>

## Remarques
1. On ne connait pas a priori l'amplitude par laquelle on doit additioner $\nabla f(x)$ a $x$, pour obtenir $x^+$
2. Ce resultat est vrai meme si $f$ n'est pas convexe, on ne garantit plus la recherche d'un minimum global

## Question: *Il se passe quoi si $\nabla f(x) = 0$ ?*


# Questions des eleves

J'ai pas compris la particule a une vitese constante sur x? Comment on défini la "vitesse"?

> Tu images que la courbe gamma représente le déplacement de la particule le long de la courbe A -> gamma(t) = abscisse de la particule le long de la courbe. Avec en t=0, ta particule qui passe par le point p
> 
> La vitesse instantanée = dérivée de la position. Vitesse instantanée de la particule en p = dérivée de gamma en 0
>
> Ta particule peut adopter plusieurs profils de vitesse le long de la courbe (accélérer, décélérer, etc), mais elle est contrainte de suivre le profile de la courbe
>
> Donc la valeur du vecteur vitesse gamma'(0) peut effectivement varier selon le profil de vitesse
> 
> Mais la direction de ce vecteur vitesse sera toujours la même, et c'est ce qui défini l'espace tangent (en dim 1)

Mais du coup on fait tout ça juste pour trouver un vecteur qui appartient a l'espace tangent?
> En fait cette idée est très générale, et indépendante de la dimension de l'espace dans lequel on travaille.
En dim 1, ça peut paraître un peu overkill de faire tout ça "juste" pour avoir la direction de la tangente.
Mais quand on va passer sur des dimensions supérieurs (donc des surfaces, etc), là tu auras plusieurs directions possibles de te balader sur la surface et d'approcher ton point p. Imagine $f(x,y) = x^2 + y^2$, donc une surface en forme de bol. En (0,0), tu as plusieurs directions pour approcher (0,0) en restant sur la surface. Pour chacune de ces courbes possibles, tu vas avoir un vecteur vitesse associé. Et c'est l'ensemble de ces vecteurs vitesse (enfin, l'espace généré par ces vecteurs vitesse) qui va définir le plan tangent

J'ai encore du mal à voir en quoi c'est différent d'une différentielle
> Il y a effectivement un lien entre les deux notions, mais ce ne sont pas du tout les mêmes objets : une différentielle est une application linéaire, un espace tangent est une sous-partie de ton espace de travail.