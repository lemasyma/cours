---
title:          "CMKV: Introduction aux Chaines de Markov"
date:           2021-09-15 14:00
categories:     [Image S9, CMKV]
tags:           [Image, SCIA, S9, CMKV, sudoku, pastis]
description: Champs de Markov - Introduction aux Chaines de Markov
math:            true
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/BJ8UMD1XY)

> Savoir echantilloner c'est bien mais on veut optimiser

# Rappels

<div class="alert alert-info" role="alert" markdown="1">
Quand on a une loi de proba $P(x)$

$$
\begin{aligned}
P(X&=x)\to P_{\underbrace{T}_{\text{temperature}}}(X=x)=\frac{1}{Z_T}e^{-\frac{U(x)}{T}}\\
&\downarrow\\
P(X=x)&=\frac{1}{Z}e^{-U(x)}
\end{aligned}
$$

</div>

$$
\color{red}{
\lim_{T\to+\infty}P_T=P_{\text{uniF}}\\
\lim_{T\to0^+} P_T=P_0\\
P_0(X=x)\begin{cases}
1 &\text{si } x=x_{\text{solution}}\\
\varnothing &\text{sinon}
\end{cases}
}
$$

## Marche aleatoire
<div class="alert alert-warning" role="alert" markdown="1">
Notre echantillonneur va realiser une **marche aleatoire**
</div>

*Comment on affecte $x^{(t+1)}$ a partir du $x$ courant ?*

<div class="alert alert-info" role="alert" markdown="1">

On a un échantiolloneur Metropolis-Hastings:
- $x^{(0)}\leftarrow \text{aléatoire}$
- Boucle:
    - On se trouve un $x_{\text{candidat}}$
    - $x^{(t+1)}\leftarrow$ soit $x^{(t)}$ soit $x_{\text{candidat}}$ $\to\color{red}{\text{dépend de }} P_{\color{blue}{T^{(t)}}}(X=x)$
    - $\color{blue}{T^{(t+1)}\leftarrow\underbrace{\alpha}_{\equiv 1^-} T^{(t)}}$
    - $t\leftarrow t+1$


<div class="alert alert-warning" role="alert" markdown="1">
C'est un algo de *recuit simulé*
> Alterner entre cycle de refroidissement lent et réchauffement pour un métal
</div>

</div>

*C'est quoi un algo brute force ?*
> C'est un algo qui va explorer tout l'espace pour trouver la solution

<div class="alert alert-success" role="alert" markdown="1">
On cherche le **minimum energetique**
</div>

|$\color{red}{\{2,4\}}$|$\color{red}{\{2,3,4\}}$|||
|-|-|-|-|
||$\boxed{1}$|$\boxed{2}$||
|||||
|$\boxed{3}$|||$\boxed{4}$|

D'apres le dernier cours, si on regarde l'echantilloneur, il y a une possibilite de faire un echantillonneur tres simple mais *sous-optimal*

<div class="alert alert-info" role="alert" markdown="1">

$$
\color{red}{\forall t, u(x^{(t+1)})\le u(x^{(t)})}
$$

loop:
- $x_{\text{candidat}}\leftarrow$ aleatoire
- si $x_{\text{candidat}}$ ameliore
    - on le garde comme $x^{(t+1)}$
</div>

![](https://i.imgur.com/QFgeGa7.png)
*Combien de temps ca va prendre pour atteindre la solution ?*
> On peut viser la fin de l'univers apres l'extinction des hommes

<div class="alert alert-warning" role="alert" markdown="1">
Au final, le tirage aleatoire est **moins efficace que le bruteforce**
</div>
> C'est con hein ?

# Backtracking

On va toujours empiler les boucles. Par exemple:
- On met $1$ dans la premiere case, sauf que ce n'est pas possible donc on break
- On met $2$ a la place
- On fait pareil pour la $2^e$ case, $1$ et $2$ ne sont pas possibles donc on met $3$
- On fait pareil pour la $3^e$ case, on met $4$
- $\vdots$
- On arrive a un blocage !

|$2$|$3$|$4$|$1$|
|-|-|-|-|
|$4$|$\boxed{1}$|$\boxed{2}$|$3$|
|$1$|$2$|$3$||
|$\boxed{3}$|||$\boxed{4}$|

*Mais ou est-ce qu'on s'est trompe ??*
- On backtrack et on change nos valeurs
- $1$, $2$, $3$ et $4$ ne sont pas possibles donc on supprime la valeur et on revient a la case precedente
- On change $2$, $3$ c'est pas possible donc on met $4$
 
|$2$|$3$|$4$|$1$|
|-|-|-|-|
|$4$|$\boxed{1}$|$\boxed{2}$|$3$|
|$1$|$4$|||
|$\boxed{3}$|||$\boxed{4}$|

Pour resoudre le sudoku, imaginons d'avoir une fonction $U$ a 16 variables:

$$
U(\begin{matrix}
\boxed{}&\boxed{}&\boxed{}&\boxed{}\\
\boxed{}&\boxed{}&\boxed{}&\boxed{}\\
\boxed{}&\boxed{}&\boxed{}&\boxed{}\\
\boxed{}&\boxed{}&\boxed{}&\boxed{}\\
\end{matrix})
$$

|$\{2, 4\}$||||
|-|-|-|-|
||$\boxed{1}$|$\boxed{2}$||
|||||
|$\boxed{3}$|||$\boxed{4}$|

<div class="alert alert-warning" role="alert" markdown="1">
Ici on reduit l'espace des possibilites
</div>

En premiere iteration:
$$
U(\begin{matrix}
\boxed{1}&\boxed{1}&\boxed{1}&\boxed{1}\\
\boxed{1}&\boxed{1}&\boxed{1}&\boxed{1}\\
\boxed{1}&\boxed{1}&\boxed{1}&\boxed{1}\\
\boxed{1}&\boxed{1}&\boxed{1}&\boxed{1}\\
\end{matrix})\\
\vdots\\
U(\begin{matrix}
\boxed{1}&\boxed{1}&\boxed{1}&\boxed{1}\\
\boxed{1}&\boxed{1}&\boxed{1}&\boxed{1}\\
\boxed{1}&\boxed{1}&\boxed{1}&\boxed{1}\\
\boxed{1}&\boxed{2}&\boxed{1,2,3,4}&\boxed{1,2,3,4}\\
\end{matrix})\\
$$

<div class="alert alert-success" role="alert" markdown="1">
On obtient un arbre des possibilites

![](https://i.imgur.com/h2u4Nji.png)

</div>
- Bruteforce: parcours en largeur
- Backtrack: parcours en longueur

<div class="alert alert-danger" role="alert" markdown="1">
Il y a des problemes ou **on ne peut pas backtracker**
</div>

# Autre methode

On se donne une fonction $U_1(x)$

![](https://i.imgur.com/Hzsb1Is.png)

$$
P(X=x)=\frac{1}{Z}e^{-U(x)}\\
\downarrow +T\\
P_T(X=x)=\frac{1}{Z_T}e^{-\underbrace{\frac{U(x)}{T}}_{\color{red}{U_T(x)}}}
$$

<div class="alert alert-warning" role="alert" markdown="1">
On va chercher le $x$ qui **maximisme**
</div>

![](https://i.imgur.com/vavFypp.png)

On a un *espace discret*.

<div class="alert alert-success" role="alert" markdown="1">
On chercher le $\color{green}{P_{\infty}}$ qui a la meme aire que notre fonction $\color{blue}{P(X=x)}$

![](https://i.imgur.com/B7hYdqN.png)

</div>

On dessine $\color{blue}{P(5)}$

![](https://i.imgur.com/jDn2PKL.png)

On dessine $\color{black}{P(1)}$

![](https://i.imgur.com/aSPkien.png)

$$
\vdots
$$

![](https://i.imgur.com/ROkquo0.png)

Imaginons qu'on a une bille. Il ne faut pas qu'elle se fasse coincer dans un minimum local et elle se deplace de proches en proches.

![](https://i.imgur.com/M7HD5Uu.gif)

<div class="alert alert-success" role="alert" markdown="1">
La bille aura de plus en plus de mal a "remonter" du creux et va se retrouver "coincee" dans le creux contenant la solution
</div>

*Quel est le cout pour aller d'une position a une autre ?*
![](https://i.imgur.com/pRUhpfx.png)

> Dans ce cas la bille doit avoir assez d'energie pour remonter la pente

# Ratio

$$
P(X_{t+1}=x_{t+1}\vert X_t=x_t)=\text{ratio}\\
X_t\color{green}{\text{ influence }} X_{t+1}\\
X_{t+1}\color{red}{\text{ depend de }} X_t
$$

<div class="alert alert-info" role="alert" markdown="1">
Si on a $P(A=a\vert B=b,C=c)$, $B$ et $C$ influencent $A$.
</div>

$$
\color{green}{X_0\to X_1\dots X_{t-2}\to X_{t-1}\to} \overbrace{X_t\to X_{t+1}}^{\text{modele}}\color{green}{\to X_{t+2}}
$$

## La meteo de Gulli

En supposant qu'on soit a Paris:

$$
\color{green}{
P(X_{t+1}=\text{pourri}) = 0.6\\
P(X_{t+1}=\text{pourri}) = 0.4
}
$$

|$x_{t+1}$ \ $x_t$|beau|pourri|total|
|-|-|-|-|
|beau|$\color{red}{0.4}$|$\color{red}{0.2}$|$\color{green}{0.6}$|
|pourri|$\color{red}{0.1}$|$\color{red}{0.3}$|$\color{green}{0.4}$|

$$
\color{green}{X_0\to X_1\dots X_{t-2}\to X_{t-1}\to} \overbrace{X_t\to X_{t+1}}^{\text{modele}}\color{green}{\to X_{t+2}}\\
\color{red}{
x_{t-2}\leftarrow x_{t-1}\overbrace{\leftarrow}^{\text{dependance}} x_t\overbrace{\leftarrow}^{\text{dependance}} ?x_{t+1}}
$$

*Le modele ne semble pas simpliste ?*
> On est influence que par le temps d'avant d'une facon directe

<div class="alert alert-warning" role="alert" markdown="1">
Le temps de demain depend du temps qu'il fait aujourd'hui mais egalement du temps d'hier
</div>

<div class="alert alert-success" role="alert" markdown="1">
Le tableau devient **3D**
</div>

On a defini:

$$
P(X_{t+1}=x_{t+1}\vert X_{t-1}=x_{t-1}, X_t=x_t)
$$

On a decide d'ignorer le temps d'avant avant-hier, et la journee encore avant, etc.

<div class="alert alert-danger" role="alert" markdown="1">
Le modele le plus **general** pour connaitre le temps de demain est:

$$
P(X_{t+1}=x_{t+1}\vert X_t=x_t, X_{t-1}=x_{t-1},\dots, X_0=x_0)\quad\text{(tous les jours)}
$$

</div>

$$
P(\underbrace{X_{t+1}}_{\color{green}{\text{var. alea}}}=x_{t+1}\vert X_t=x_t, X_{t-1}=x_{t-1},\underbrace{\dots, X_0=x_0}_{\color{green}{\text{independante de}}})
$$

<div class="alert alert-danger" role="alert" markdown="1">
On a ecrit des **dependances indirectes** qui ne vont pas etre modelisees

$$
\color{green}{X_0\to X_1\dots X_{t-2}\to X_{t-1}\to} \overbrace{X_t\to X_{t+1}}^{\text{modele}}\color{green}{\to X_{t+2}}
$$

- En vert: dependances indirectes

**C'est une *chaine de Markov***

</div>

Prenons une chaine de niveau $2$:

$$
\color{green}{\underbrace{X_{t-4}}_{\to \color{black}{X_{t-2}}}\to \underbrace{X_{t-3}}}_{\color{black}{\to X_t}}\to \underbrace{X_{t-2}}_{\to X_t}\color{green}{\to} X_{t-1}\to X_t
$$

Prenons une image en niveaux de gris:

![](https://i.imgur.com/pkLSxTq.png)

$$
X=(X_1,\dots,X_{\underbrace{N}_{\text{pixel}}})\\
x = (x_1,\dots,x_N)\\
U_L(x_i, y_i)=\begin{cases}
y_i &\text{si } x_i=\text{noir}\\
1-y_i&\text{sinon}
\end{cases}
$$

![](https://i.imgur.com/gT1kzxs.png)

$$
\begin{aligned}
\color{blue}{U_{\text{prior}}(x_i,x_{i-l},x_{i-1},x_{i+1},x_{i+l})}&=\sum_{v}\vert x_i-x_{iv}\vert\\
&=\sum_{v}\delta_{x_i\neq x_{iv}}
\end{aligned}
$$

<div class="alert alert-info" role="alert" markdown="1">
**Qu'est-ce qu'un champ de Markov ?**
Un modele graphique avec des fleches $A- B$ ($A$ et $B$ sont dependantes mutuellement)
</div>

<div class="alert alert-warning" role="alert" markdown="1">
On veut que notre graphe soit le plus **incomplet possible**
</div>
> cad avoir le moins de variables possibles

$$
P(X_{t+1}=x_{t+1}\vert \{X_u=x_u\}_{u\le t})=-(\{X_u=x_u\}_{u\in[t-h,t]})\\
$$

<div class="alert alert-info" role="alert" markdown="1">
**Propriete Markovienne**

$$
P(X_i=x_i\vert \{X_j=x_j\}_{[1,N]\setminus {i}}) = P(X_i=x_i\vert \{X_j=x_j\}_{\text{ ou } j\in V(i)})
$$

</div>