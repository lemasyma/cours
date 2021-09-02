---
title:          "CMKV: Introduction"
date:           2021-09-02 14:00
categories:     [Image S9, CMKV]
tags:           [Image, S9, CMKV, sudoku, pastis]
description: Champs de Markov - Introduction
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/B1wT64CbF)

# Introduction

<div class="alert alert-info" role="alert" markdown="1">
**Definition**
Statistiques: comptage et representation de donnees
</div>

<div class="alert alert-info" role="alert" markdown="1">
**Definition**
Probabilite: phenomene dont on extrait un modele
</div>

# Optimisation combinatoire

On a une grille, on veut la remplir pour que ca devienne un echequier via un algorithme

![](https://i.imgur.com/IKGiBmp.png)

<div class="alert alert-info" role="alert" markdown="1">
*Est-ce que notre algo est deterministe ?*
Oui, car on a toujours le meme resultat avec la meme entree.
</div>

Si la couleur d'une case est aleatoire, l'algo n'est plus deterministe.

<div class="alert alert-info" role="alert" markdown="1">
**Definition**
Un algo est stochastique si **a l'interieur** il y a de l'aleatoire

```python=
# algo
rand()
#algo
```
</div>

<div class="alert alert-warning" role="alert" markdown="1">
L'aleatoire provient de l'entree
</div>

Il existe des programmes *stochastisques* **et** *deterministes*.

![](https://i.imgur.com/ndpLLoZ.gif)

*`rand()` est-il deterministe ?*
> Oui. C'est dingue, hein ?

$$
\Omega=\{A,B,C,D\}\\
\begin{cases}
P(A)\in[0,1], \text{idem pour } B,C\text{ et } D\\
P(A)+P(B)+P(C)+P(D) = 1
\end{cases}
$$

![](https://i.imgur.com/4HVO1ZS.png)

## Exemple
Nous sommes une population, on mesure la probabilite d'avoir 20 ans.

$$
\underbrace{P(20)}_{P(A)}=0.36
$$

![](https://i.imgur.com/c80RkoI.png)

Maintenant avec la meteo:

$$
\Omega=\{\text{beau},\text{pluie},\text{couvert}\}\\
\begin{cases}
P(\text{beau}) = 0.51\\
P(\text{pluie}) = 0.01\\
P(\text{couvert}) = 1 - 0.21 - 0.01
\end{cases}
$$

Faire action avec la proba $P$

![](https://i.imgur.com/o1FQYZM.png)

$$
P(\varnothing)=P(1)=P(2)=...=\frac{1}{\text{RANDMAX}}
$$

Retour sur la meteo:

$$
\begin{cases}
P(\text{beau}) = 0.3\\
P(\text{pluie}) = 0.5\\
P(\text{couvert}) = 0.2
\end{cases}
$$

![](https://i.imgur.com/52irfS0.png)

<div class="alert alert-warning" role="alert" markdown="1">
Le probleme: certaines variables aleatoires ne sont pas independante (salaire, categorie pro, etc.)
</div>

# SUDOKU

On doit ecrire un programme qui resout le sudoku

||1|||
|-|-|-|-|
|||2||
|||3||
|2|||$\square$|

On a $$4^{12}=16,7M$$ de valeur possibles.

On va ***bruteforce***, cad visiter plein de chemins possibles pour remplir. Les $16$ millions de possibilites de remplissage vont baisser mais vont rester elevees.

<div class="alert alert-warning" role="alert" markdown="1">
La resolution prend du temps :(
</div>

Mais, au lieu de faire un algo bete, on fait quoi ?

<div class="alert alert-danger" role="alert" markdown="1">
On rentre dans un ***probleme d'optimisation combinatoire***.
</div>
> On enumerait les nombres de remplissage possible

*Mais pourquoi un probleme d'optimisation ?*

On obtient un espace a 12 axes, la solution est quelque part dans l'espace

![](https://i.imgur.com/9YmRtnu.png)

<div class="alert alert-success" role="alert" markdown="1">
On cherche le minimum ou le maximum de la fonction

$$
x_{\text{sol}}=\text{arg min}_xf(x)
$$
</div>

Ah et evidemment pas moyen que ce soit une fonction convexe.

Pour les gens du fond:

![](https://i.imgur.com/4OtOUhP.gif)

### Resolution de Sudoku

|.|.|.|.|
|-|-|-|-|
|.|2|3|.|
|1|.|.|.|
|.|.|.|4|

$$
P(\begin{matrix}
\begin{vmatrix}
3 &1\\
4&2
\end{vmatrix}
&\begin{vmatrix}
4 &2\\
3&1
\end{vmatrix}\\
\begin{vmatrix}
1 &4\\
2&3
\end{vmatrix}
&\begin{vmatrix}
2 &3\\
1&4
\end{vmatrix}\\
\end{matrix}) = \frac{1}{4^{12}}\\
P(\begin{matrix}
\begin{vmatrix}
1 &1\\
1&2
\end{vmatrix}
&\begin{vmatrix}
1 &1\\
1&1
\end{vmatrix}\\
\begin{vmatrix}
1 &1\\
1&1
\end{vmatrix}
&\begin{vmatrix}
1 &1\\
1&4
\end{vmatrix}\\
\end{matrix}) = \frac{1}{4^{12}}
$$

<div class="alert alert-warning" role="alert" markdown="1">
Quand on ne sait pas, on fait de **l'equiprobable**
</div>

Mais on sait, c'est un *sudoku*:

$$
P(\begin{matrix}
\begin{vmatrix}
3 &1\\
4&2
\end{vmatrix}
&\begin{vmatrix}
4 &2\\
3&1
\end{vmatrix}\\
\begin{vmatrix}
1 &4\\
2&3
\end{vmatrix}
&\begin{vmatrix}
2 &3\\
1&4
\end{vmatrix}\\
\end{matrix}) = 1\\
P(\begin{matrix}
\begin{vmatrix}
1 &1\\
1&2
\end{vmatrix}
&\begin{vmatrix}
1 &1\\
1&1
\end{vmatrix}\\
\begin{vmatrix}
1 &1\\
1&1
\end{vmatrix}
&\begin{vmatrix}
1 &1\\
1&4
\end{vmatrix}\\
\end{matrix}) = \varnothing
$$

<div class="alert alert-success" role="alert" markdown="1">

$$
P(x_{\text{sol}})=1\\
\forall x\neq x_{\text{sol}}, P(x)=0
$$

<div class="alert alert-danger" role="alert" markdown="1">
On peut pas juste ecrire notre solution comme ca...
</div>

</div>

> "Certaines solutions sont plus *vraies* que d'autres"
> Le camarade qui a dit un truc important

<div class="alert alert-danger" role="alert" markdown="1">

Par "vrai", on veut dire proche de la solution $\equiv$ ***peu d'erreur***

</div>

$$
P(\begin{matrix}
\begin{vmatrix}
3 &1\\
4&2
\end{vmatrix}
&\begin{vmatrix}
4 &2\\
3&1
\end{vmatrix}\\
\begin{vmatrix}
1 &4\\
2&3
\end{vmatrix}
&\begin{vmatrix}
2 &3\\
1&4
\end{vmatrix}\\
\end{matrix}) = 0.00001\\
P(\begin{matrix}
\begin{vmatrix}
1 &1\\
1&2
\end{vmatrix}
&\begin{vmatrix}
1 &1\\
1&1
\end{vmatrix}\\
\begin{vmatrix}
1 &1\\
1&1
\end{vmatrix}
&\begin{vmatrix}
1 &1\\
1&4
\end{vmatrix}\\
\end{matrix}) = 0.0\dots 01
$$

![](https://i.imgur.com/f4wFBXE.png)

<div class="alert alert-success" role="alert" markdown="1">
La prob est plus elevees que le reste
</div>

# La meteo de Gulli
$$
\begin{matrix}
P(A&\cap&B)\\
\text{beau} &&\text{Londres}\\
\text{temps} = \{\text{pourri, ...}\} &&\text{lieu} = \{\text{Londres, Paris, ...}\}
\end{matrix}
$$

- $T$ VA pour rpz le temps
- $P(T=\text{beau})=0.6$, $P(T=\text{pourri})=0.1$, ...

$$
\color{red}{\boxed{P(T=t)}}
$$

- $V$ vecteur aleatoire, $$V=(V_1,...,V_n)$$, $$V_i$$ var aleatoire

$$
P(T=t\color{red}{\underbrace{,}_{\text{et}}}L=l)\color{green}{\equiv f(t,l)\in]\varnothing,1]}
\begin{cases}
t\in\{\text{beau, pourri,}\dots\}\\
l\in\{\text{Londres, Paris,}\dots\}
\end{cases}
$$

$$
P(A\cap B)=P(A)+P(B)-P(A\cup B)\\
\bar A+\cap + \cap + \bar B-\bar A-\cap -\bar B
$$

## Exemple

$W$ weather, $L$ location, $N$ thune de Xavier NIEL.

$P(W=w,L=l)\equiv$ proba qu'il fasse $$\color{red}{\underbrace{\boxed{\text{w a l}}}_{\text{beau a Londres}}}$$

$$
\begin{aligned}
P(A\cap B)&=P(A\vert B).P(B) \\
= P(B\cap A) &= P(B\vert A).P(A)\\
&\Rightarrow P(A\vert B)=\frac{P(A\cap B)}{P(B)}
\end{aligned}
$$

![](https://i.imgur.com/JUpxkkU.png)

$$
\begin{aligned}
x_{\text{sol}}=\text{arg max}_x P(X=x&\vert Y=y)\\
&\downarrow
\end{aligned}\\
\frac{\overbrace{P(Y=y\vert X=x)}^{\color{blue}{f(x,y)}}.P(X=x)}{\underbrace{P(Y=y)}_{\color{red}{\text{terme constant}}}}\\
\underbrace{L(X=x\vert Y=y)}_{\color{green}{\text{VRAISEMBLANCE}}}.\underbrace{P(X=x)}_{\color{green}{\text{A PRIORI}}})
$$

# Retour au SUDOKU

$$
y=\begin{matrix}
\begin{vmatrix}
y_1 &\\
&1
\end{vmatrix}
&\begin{vmatrix}
 &\\
2&x_p
\end{vmatrix}\\
\begin{vmatrix}
3 &\\
&
\end{vmatrix}
&\begin{vmatrix}
 &\\
&4
\end{vmatrix}\\
\end{matrix}\\
y=(0,0,0,0,0,\color{red}{1},\color{green}{2},0,\color{blue}{3},0,0,0,0,0,0,\color{orange}{4})\\
y=(y_1,...,y_{15})\\
y_6=1\\
x=(x_1,x_2,x_3,x_4,x_6,\color{red}{0},\color{green}{0},x_p,\color{blue}{0},\dots)\\
x'=(1,1,1,1,1,\color{red}{0},\color{green}{0},1,\color{blue}{0},\dots)
$$

En solution:

$$
\color{green}{P(}x'\color{green}{)}= \begin{matrix}
\begin{vmatrix}
1 &1\\
1&0
\end{vmatrix}
&\begin{vmatrix}
1&1\\
0&1
\end{vmatrix}\\
\begin{vmatrix}
0&1\\
1&1
\end{vmatrix}
&\begin{vmatrix}
1&1\\
0&1
\end{vmatrix}\\
\end{matrix}\color{green}{=?}\\
\color{green}{P(}x''\color{green}{)}= \begin{matrix}
\begin{vmatrix}
1&2\\
3&0
\end{vmatrix}
&\begin{vmatrix}
3&4\\
0&1
\end{vmatrix}\\
\begin{vmatrix}
0&1\\
4&3
\end{vmatrix}
&\begin{vmatrix}
4&3\\
2&0
\end{vmatrix}\\
\end{matrix}\color{green}{=?}\\
$$

# Recap

$$
\color{red}{
P_{\color{pink}{T}}(X=x)=\frac{1}{Z}e^{\frac{-U(x)}{\color{pink}{T}}}\quad(z=\sum_xe^{-U(x)})
}\\
\color{green}{
P_{\color{pink}{T}}(X=x_{\text{sol}})\gt P_{\color{pink}{T}}(X=x)\quad\forall x\neq x_{\text{sol}}
}\\
\color{blue}{
P(X=x_{\text{sol}}) = 0.000001\quad\text{ECHANTILLONEUR }\bullet\to x\text{ suivant }P(x)
}\\
\color{pink}{
\lim_{T\to0^+}P_T=\begin{cases}
\color{green}{P_{\color{pink}{0}}(X=x_{\text{sol}})=1}\\
\color{green}{P_{\color{pink}{0}}(X=x_{\text{sol}})=\varnothing}&\text{sinon}
\end{cases}
}
$$