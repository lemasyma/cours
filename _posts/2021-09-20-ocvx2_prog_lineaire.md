---
title:          "OCVX2: Programme Lineaires"
date:           2021-09-20 10:00
categories:     [Image S9, OCVX2]
tags:           [Image, SCIA, S9, OCVX2]
math: true
description: Programme Lineaires
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/ryqrFeUXF)

# OCVX2: Programme Lineaires

Quelques changements par rapport a ce qui etait prevu
> OCVX le retour
> OCVX qui ne va pas se passer comme prevu

Bashar doit reprendre une partie du boulot de Corinne, pour pas qu'il creve il ne fera pas OCVX2 et Guillaume fera tout $\to$ OCVX2 allege :(
- On verra les bases
- Pas de TP
    - Ex: pas de TP sur l'implem d'un SVM
- Mais on aura tout le reste
- Evaluation: partiel
    - Essaiera de le caler premiere quinzaine de Novembre
- Semaine prochaine: pas de cours jusqu'a 19h

<div class="alert alert-danger" role="alert" markdown="1">

**Programme lineaire**

On cherche a minimiser $f_0(x)$ $x\in\mathbb R^n$ tel que $f_i(x)\le 0$ avec $i=1,\dots,p$, $f_0, f_i$ $(i=1,\dots,p)$ fonctions affine. On note ce probleme $P_1$.

$$
\begin{matrix}
\text{minimiser}&f_0(x)&x\in\mathbb R^n\\
\text{tel que}&f_i(x)\le 0&f_0,f_i&\text{fonctions affines}\\
&i=1,\dots,p
\end{matrix}
$$

</div>

# Exercice 1

Soit $A_u$ le lieu de $\mathbb R^2$ decrit par les contraintes

$$
A_u\begin{cases}
-x+2y&\le -1\\
x+y&\le 1
\end{cases}
$$

Et $A_b$ le lieu decrit par les contraintes de $A_u$ auxquelles on ajoute $x-3y\le 6$

On va se donner un espace
- $$A_u=\biggr\{(x,y)\in\mathbb R^2\text{ tq } \begin{aligned} -x+2y &\le 1&(D_1) \\ x+y&\le1&(D_2) \end{aligned}\biggr\}$$
- $$A_b=A_u\cap\{(x,y)\in\mathbb R^2\text{ tq } \underbrace{x-3y\le 6}_{(D_3)}\}$$

1. Etudier le programme lineaire de lieu admissible $A_u$ et minimisant $y$. Que se passe-t-il si on remplace $y$ par $-y$ ?
2. A-t-on toujours une valeur minimale pour un programme lineaire ayant pour lieu admissible $A_b$ ?
3. Etudier le programme lineaire de lieu admissible $A_b$ et minimisant $x+y$. Effectuer cette meme etude pour la fonction objectif $-x-y$

<details markdown="1"><summary>Solution</summary>

## Question 1

$$
\text{min } f_0(x,y)=y\quad x\in A_u
$$

$$
(D_1): -x+2y+1=0
$$

<div class="alert alert-info" role="alert" markdown="1">

*Comment obtenir le vecteur directeur ?*

$$
ax+by+c=0\\
\vec u=\binom{-b}{a}\\
$$

</div>

<div class="alert alert-info" role="alert" markdown="1">

*Comment obtenir le vecteur normal ?*

$$
ax+by+c=0\\
\vec n=\binom{a}{b}\\
$$

</div>

Donc:
$$
(D_1):\begin{cases}
\vec u_1 = \binom{-2}{-1}\\
\vec n_1 = \binom{-1}{2}
\end{cases}\\
(1,0)\in(D_1)
$$

On obtient graphiquement:

![](https://i.imgur.com/epelXyC.png)

Maintenant avec le vecteur normal:

![](https://i.imgur.com/olBYzva.png)

*Dans quel demi-espace sommes nous ?*
> Le demi-espace positif est du cote du vecteur normal et le demi-espace negatif est de l'autre

On s'interesse a $-x+2y+1\le0$ donc on s'interesse au demi-espace negatif car la contrainte est $-x+2y\le 1\Rightarrow -x+2y-1\le 0$.

![](https://i.imgur.com/fKAW3i1.png)

On fait la meme procedure pour $(D_2)$:

$$
(D_2):x+y-1=0\\
\vec u_2 = \binom{-1}{1}\\\
\vec n_2 = \binom{1}{1}\\
(1,0)\in(D_2)
$$

![](https://i.imgur.com/boDrJb5.png)

<div class="alert alert-success" role="alert" markdown="1">
On cherche notre programme lineaire sur l'intersection de ces 2 contraintes

![](https://i.imgur.com/49bi2JG.png)

</div>

<div class="alert alert-success" role="alert" markdown="1">

On cherche a minimiser $y$, on part donc "vers le bas". Notre lieu admissible n'est pas borne vers le bas donc dans ce cas, la valeur optimale est $-\infty$.

</div>

$$
(P_2): \text{min }-y\\
(x,y)\in A_u
$$

On veut minimiser $-y$ donc on veut maximiser $y$.

$$
(x^+,y^+)=(1,0)\quad\text{et}\quad f_0(x^+,y^+)=0
$$

## Question 2

On va faire exactement pareil en etudiant $(D_3): x-3y-6=0$

$$
\vec u_3=\binom{3}{1}\\
\vec n_3=\binom{1}{-3}\\
(0,-2)\in(D_3)
$$

![](https://i.imgur.com/gyxU0hd.png)

En intersection de ces 3 contraintes:

![](https://i.imgur.com/XfBmele.png)

*Est-ce qu'on programme lineaire a toujours une valeur minimale sur $A_b$ ?*
> Oui car le lieu admissible $A_b$ est borne

## Question 3

$(P_3)$: minimiser $f_0(x,y)=x+y, (x,y)\in A_b$

$1^{ere}$ etape: on trace une ligne de niveau

<div class="alert alert-info" role="alert" markdown="1">
**Rappel**

$$
\mathcal C_0(f_0)=\{(x,y)\in\mathbb R^2, 
\begin{aligned} 
f_0(x,y)&=0 \\ 
x+y&=0 
\end{aligned}\}
$$

</div>

$$
\vec u_0 = \binom{-1}{1}\\
\vec n_0 = \binom{1}{1}\\
(0,0)\in\mathcal C_0 (f_0)
$$

![](https://i.imgur.com/2CPTW30.png)

On a defini le **gradient** de notre fonction, on descend a l'oppose de notre vecteur normal pour trouver la solution.

<div class="alert alert-warning" role="alert" markdown="1">
On fait une descente de gradient
</div>

<div class="alert alert-success" role="alert" markdown="1">

Graphiquement, la solution est l'intersection de la droite $(D_1)$ et la droite $(D_3)$.

</div>

Pour determiner les coordonnees de ce point, il doit verifier les equations des 2 droites:

$$
\begin{aligned}
&\begin{cases}
-x^*+2y^*+1 = 0\\
x^*-3y^*-6=0
\end{cases}\\
&\Leftrightarrow\begin{cases}
y^*=-5\\
x^*=-9
\end{cases}
\end{aligned}
$$

<div class="alert alert-success" role="alert" markdown="1">
- Point optimal 

$$
p^{*} = (-9,-5)
$$

- Valeur optimale: 

$$
\begin{aligned} 
f_0^*&=f_0(x^*,y^*) \\ 
&= x^*+y^* \\ 
&=-14 
\end{aligned}
$$
</div>

</details>

# Exercice 2

Donnez un exemple de programme lineaire:

## Non borne

<details markdown="1"><summary>Solution</summary>

$$
\text{min}_{(x,y)\in A_u} y
$$

</details>

## De lieu admissible non borne mais de solution finie

<details markdown="1"><summary>Solution</summary>

$$
\text{max}_{(x,y)\in A_u} y
$$

</details>

## Ayant une infinite de solutions/points optimaux

<details markdown="1"><summary>Solution</summary>

$$
\text{max}_{(x,y)\in A_b} x+y
$$

</details>

## Ayant une unique solution

<details markdown="1"><summary>Solution</summary>

$$
\text{min}_{(x,y)\in A_b}
$$

</details>

# Exercice 3

On considere le programme lineaire suivant

$$
\begin{matrix}
\text{(P)}&\text{minimiser}&f_0(x,y)=3x+2y\\
&\text{sujet a}&x-y\le 0\\
&&4x-y\ge 1\\
&&-x-y\ge-5
\end{matrix}
$$

1. Representer le lieu admissible de $(P)$ dans le plan euclidien
2. Tracer $\mathcal C_6(f_0)$ la courbe de niveau $6$ de la focntion objectif de $(P)$. Indiquer les demi-espcaes positifs et negatif definis par $\mathcal C_6(f_0)$. Dans quelle direction translater $\mathcal C_6(f_0)$ afin de minimiser $f_0$ ?
3. Tracer la courbe de niveau qui realise le minimum de $(P)$ et calculer l'unique point optimal de $(P)$. Quelle est la valeur optimale de $(P)$ ?

<div class="alert alert-info" role="alert" markdown="1">
**Methode**

1. Lieu admissible
2. Courbe de niveau de $f_0$
3. Point optimal (geometriquement)
4. Point optimal (analytiquement)
5. Valeur optimale

</div>

<details markdown="1"><summary>Solution</summary>

## Question 1

![](https://i.imgur.com/O5kp4xu.png)

## Question 2

![](https://i.imgur.com/jUgiNpZ.png)

On cherche a minimiser, on translate dans la direction opposee au vecteur normal.

![](https://i.imgur.com/PE9lEIz.png)

## Question 3

$$
p^{*}\in(D_1)\cap(D_2)\\
p^{*}=\biggr(\frac{1}{3},\frac{1}{3}\biggr)\\
f_0^{*}=f_0(x^*,y^*)=\color{red}{\frac{5}{9}}
$$

*Comment on trouve la courbe de niveau 6 ?*

$$
\begin{aligned}
C_6(f_0)=\{(x,y)\in\mathbb R^2, f_0(x,y)&=6\}\\
3x+2y&=6\\
3x+2y&=0
\end{aligned}
$$

</details>

# Exercice 4

On considere le programme lineaire suivant

$$
\begin{matrix}
\text{(P_2)}&\text{minimiser}&f_0(x,y)=x+2y\\
&\text{sujet a}&-1\le x\le 1\\
&&-1\le y\le 1\\
\end{matrix}
$$

Resoudre $(P_2)$ en suivant la demarche precedente

<details markdown="1"><summary>Solution</summary>

Sujet a 

$$
\begin{aligned}
\begin{aligned}
x&\le1\\
-x&\le1
\end{aligned}\Biggr\} \vert x\vert\le1\\
\begin{aligned}
y&\le1\\
-y&\le1
\end{aligned}\Biggr\}\vert y\vert\le 1
\end{aligned}\Biggr\}\Vert\binom{x}{y}\Vert_{\infty}\le1
$$

![](https://i.imgur.com/DTgvV3E.png)

$$
p^*=(-1,-1)\\
f_0^*=-3
$$

</details>
