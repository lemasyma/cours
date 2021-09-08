---
title:          "CMKV: Metropolis-Hastings et recuit simule"
date:           2021-09-08 14:00
categories:     [Image S9, CMKV]
tags:           [Image, S9, CMKV, sudoku, pastis]
description: Champs de Markov - Metropolis-Hastings et recuit simule
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/SyseY7IfF)

# Rappels
$P(X=x)$ => variable aleatoire
- $x$: ne pas lister toutes les valeurs possibles pour $X$

$$
P(X=x\underbrace{,}_{\text{et}} Z=z)
$$

On le notait $\cap$ au lycee

$$
P(A\cap B) = P(A).P(B)
$$

<div class="alert alert-info" role="alert" markdown="1">
- $X = (X_1,\dots,X_n)$ est un vecteur aleatoire
- $x = (x_1,\dots,x_n)$ est une realisation
</div>

## Sudoku

Il existe une solution dediee mais on ne la connait pas

|$\color{red}{x_1}$|$\color{red}{x_2}$|||
|-|-|-|-|
|$\color{red}{x_4}$|$2\color{green}{\rightarrow y_1}$|||
|||||
|||||

$$
P(\begin{vmatrix}1\vert&1 \\ 1\vert&\end{vmatrix}) = ?
\begin{cases}
x_1 =1\\
x_2=1\\
x_4=1
\end{cases}
$$

Dans ce cas, on ne regard que 3 realisations et on va les evaluer


$$
P(\begin{vmatrix}1\vert&1 \\ 3\vert&\end{vmatrix}) = ?
\begin{cases}
x_1 =1\\
x_2=1\\
x_4=3
\end{cases}\\
P(\begin{vmatrix}1\vert&3 \\ 4\vert&\end{vmatrix}) = ?
\begin{cases}
x_1 =1\\
x_2=3\\
x_4=4
\end{cases}\\
P(\begin{vmatrix}3\vert&1 \\ 4\vert&\end{vmatrix}) = ?
\begin{cases}
x_1 =3\\
x_2=1\\
x_4=4
\end{cases}\\
P(\begin{vmatrix}1\vert&1 \\ 1\vert&\end{vmatrix})\color{green}{\lt}P(\begin{vmatrix}1\vert&1 \\ 3\vert&\end{vmatrix})\color{green}{\lt}P(\begin{vmatrix}1\vert&3 \\ 4\vert&\end{vmatrix})\color{green}{=}P(\begin{vmatrix}3\vert&1 \\ 4\vert&\end{vmatrix})\\
\color{red}{\boxed{L(X=x\vert Y=y) = P(Y=y\vert X=x)}}\\
$$

On veut reecrire $f(x,y)=\cos(x)\sin(\frac{1}{y})$ en $g(y,x)$

$$
g(a,b)=\cos(b)\sin(\frac{1}{a})
$$

Retour au sudoku: on sait parler des probas et des vraisemblances

<div class="alert alert-success" role="alert" markdown="1">
On lit les donnees a un espace de recherche
</div>

Pour avoir des vraisemblances:

$$
\begin{aligned}
&L(\begin{vmatrix}1\vert&1 \\ 1\vert&\color{red}{2}\end{vmatrix})\color{red}{}
&L(\begin{vmatrix}1\vert&1 \\ 3\vert&\color{red}{2}\end{vmatrix})\color{red}{}
&L(\begin{vmatrix}1\vert&3 \\ 4\vert&\color{red}{2}\end{vmatrix})\color{red}{=}
&L(\begin{vmatrix}3\vert&1 \\ 4\vert&\color{red}{2}\end{vmatrix})\\
&\overbrace{L(\begin{vmatrix}2\vert&1 \\ 1\vert&\color{red}{2}\end{vmatrix})}^{\downarrow}&\uparrow&&
\end{aligned}
$$

<div class="alert alert-info" role="alert" markdown="1">
**Rappel : Bayes**
$$
\begin{aligned}
x_{\text{sol}} = \text{arg max}_x&\underbrace{P(X=x\vert Y=y)}\\
&=\color{blue}{\frac{L(X=\boxed{x}\vert Y=y)P(X=\boxed{x})}{P(Y=y)}}
\end{aligned}
$$
</div>

## La meteo de Gulli
Le retour de `rand()`

$$
\begin{cases}
P(\text{beau}) = 0.5 &\color{red}{\varnothing}\\
P(\text{pourri}) = 0.3 &\color{red}{1}\\
P(\text{couvert}) = 0.2 &\color{red}{2}
\end{cases} \leftarrow P(T=t)\quad t\in{\text{\{beau}}, \text{pourri}, \text{couvert\}}
$$

|$0||`RANDMAX`|
|-|-|-|
|$\varnothing\dots\varnothing$|$1\vert\color{red}{1}\dots1$|$2\dots2$|

<div class="alert alert-danger" role="alert" markdown="1">
C'est pareil pour le sudoku: **tout depend de tout**
</div>

On va voir comment calculer des probas ou les variables ne sont **pas** independantes

$$
\begin{aligned}
y&\rightarrow\\
u&\rightarrow
\end{aligned}
\bigcirc\rightarrow x_{\text{sol}} = \text{arg max}_xP(X=x\vert Y=y)
$$

$$
\begin{cases}
P(\text{beau}) = 0.4 \\
P(\text{pluie}) = 0.1 \\
P(\text{couvert}) = 0.2 \\
P(\text{orage}) = 0.2 \\
P(\text{neige}) = 0.2
\end{cases}\\
\color{red}{x_{sol} = beau}
$$

On a un *echantilloneur:*

$$
P\rightarrow \bigcirc \rightarrow x
$$

<div class="alert alert-warning" role="alert" markdown="1">
Il y a plus de chances que l'echantilloneur ne nous donne **pas** la bonne solution
</div>

# Hypothese

$$
U\to P?\\
\text{hypothese}: \not\exists x, P(x)=\varnothing\\
P(X=x)=\boxed{\color{red}{\frac{1}{Z}}e^{-U(x\color{green}{,y})}}\Rightarrow U(x)=-\log(Z.\underbrace{P(X=x)}_{\color{red}{\text{ouf}\neq\varnothing}})\\
\sum_xP(X=x)=1\Rightarrow Z=\sum_xe^{-U(x)}\gt\varnothing\text{ une constante}
$$ 

# Un algo: Metropolis-Hastings

Il a ete invente en meme temps par 2 chercheurs

$$
x^{(0)} = \begin{vmatrix}
1&1\\
1&\not 2
\end{vmatrix} = \color{red}{\begin{pmatrix}
1\\
2\\
1
\end{pmatrix}}\\
x^{(1)} = \begin{vmatrix}
2&1\\
3&\not 2
\end{vmatrix} = \color{red}{\begin{pmatrix}
2\\
1\\
3
\end{pmatrix}}\\
\vdots\\
x^{(t)}=
\begin{vmatrix}
\bullet&\bullet\\
\bullet& \bullet
\end{vmatrix}
$$

<div class="alert alert-info" role="alert" markdown="1">
**Initialisation:**
1. $x^{(0)}$ tire aleatoirement avec loi uniforme
2. $t\leftarrow\varnothing$
3. Repeter jusqu'a l'infini (un algo... a l'infini)

![](https://i.imgur.com/YMmYgR5.png)
> On fait juste un tres grand nombre d'iterations

**Repeter jusqu'a l'infini:**
- $$x_{\text{rand}}$$ tire avec loi uniforme
- $$P_{\text{trans}} = \frac{P(X=x_{\text{candidat}})}{P(X=x^{(t)})}$$
- Si $$P_{\text{trans}}\gt 1\color{red}{\Leftrightarrow P(X=x_{\text{candidat}})\gt P(X=x^{(t)})}$$
- Alors $$x^{(t+1)}\leftarrow x_{\text{candidat}}\color{green}{\equiv\text{ MIEUX = ON GARDE}}$$
- Sinon on fait $$\color{green}{\boxed{x^{(t+1)}\leftarrow x_{\text{candidat}}}}\color{red}{\Leftrightarrow P(x_{\text{candidat}})\lt P(x^{(t)})}$$ avec la proba $$P_{\text{trans}}\le 1$$
    - Sinon $x^{(t+1)}\leftarrow x^{(t)}$
- $t\leftarrow t+1$
</div>

*Quel est cet algo ?*

<div class="alert alert-success" role="alert" markdown="1">
C'est un **algorithme de descente**
</div>

Cet algo est tel que la fonction $P(x^{(t+1)})\ge P(x^{(t)})$, quand $t$ augmente, $P(x^{(t)})$ augmente aussi.

<div class="alert alert-warning" role="alert" markdown="1">
C'est un optimiseur **hyper sous-efficace**
</div>
> Surtout compare a des algos de descente

## Exemple

![](https://i.imgur.com/W8GTSO6.png)

$0$|`RANDMAX`|
|-|-|
$1\dots\color{green}{\boxed{1}}1$|$0\dots0$|

$$
i_{\text{trans}} = 0.8 \times \text{RANDMAX}
$$

- Si `rand()` $$\lt P_{\text{trans}}\times$$ `RANDMAX`
    - $x^{(t+1)}\leftarrow x_{\text{candidat}}$
- Sinon $x^{(t+1)}\leftarrow x^{(t)}$

$$
\begin{aligned}
P(X=x) &= \frac{1}{Z}e^{-U(x)}\\
P_{\text{trans}} &= \frac{\not{\frac{1}{Z}}e^{-U(x_{\text{candidat}})}}{\not{\frac{1}{Z}}e^{-U(x^{(t)})}}\\
&= e^{-(\underbrace{U(x_{\text{candidat}}) - U(x^{(t)})}_{\color{red}{\Delta U}})}
\end{aligned}
$$

# Recuit simule

Comme les forgerons qui chauffe la lame d'une epee, qui la mette dans l'eau le temps de manger, la rechauffe en revenant et la laisse refroidir lentement a l'air libre apres avoir ete formee
- Apres avoir ete dans l'eau, l'epee est cassante
- On atteint l'etat le plus stable possible en lassant refroidir lentement, l'epee est la plus solide possible

<div class="alert alert-info" role="alert" markdown="1">
C'est un etat de basse energie qui pourrait etre trouve dans la nature
</div>

## Algorithme

<div class="alert alert-info" role="alert" markdown="1">
**Initialisation**
1. $T^{(\varnothing)}\leftarrow$ elevee
2. On repete:
    - $\not P\to P_{T^{(t)}}$
    - $T^{(t+1)}\simeq T^{(t)-}$
    - $t\leftarrow t+1$
</div>

$$
P_{\color{red}{T}}(X=x) = \frac{1}{Z_{\color{red}{T}}}e^{-U(x)}\\
P(X=x)\propto e^{-U(x)}\\
P_{\color{red}{T}}(X=x)\propto e^{-\frac{U(x)}{T}}\\
U_T(x)=\frac{U(x)}{T}
$$

## Exemples d'utilisation

- On prend une image en niveau de gris qu'on stylise
- On prend une image qu'on veut binariser, avec le moins de regions blanchesoires possibles mais les plus grandes possibles

*Est-ce qu'on a la meilleure solution ?*
> On en a pas la moindre idee

## Retour sur l'algo

<div class="alert alert-info" role="alert" markdown="1">
**Initialisation:**
1. ~~$\not x^{(0)}$ tire aleatoirement~~ (avec loi uniforme)
2. $t\leftarrow\varnothing$ $\quad\color{blue}{T^{(0)}\leftarrow \text{elevee}}$
3. Repeter jusqu'a l'infini (un algo... a l'infini)

**Repeter jusqu'a l'infini:**
- $$x_{\text{rand}}$$ tire avec loi uniforme
- $$P_{\text{trans}} = \frac{P_{\color{blue}{T}}(X=x_{\text{candidat}})}{P_{\color{blue}{T}}(X=x^{(t)})}=e^{\frac{-(U(x_{\text{candidat}}-U(x^{(t)})))}{\color{blue}{T^{(t)}}}}$$
- Si $$P_{\text{trans}}\gt 1$$
- Alors $$x^{(t+1)}\leftarrow x_{\text{candidat}}\color{green}{\equiv\text{ MIEUX = ON GARDE}}$$
- Sinon on fait $$\color{green}{\boxed{x^{(t+1)}\leftarrow x_{\text{candidat}}}}$$ avec la proba $$P_{\text{trans}}\le 1$$
    - Sinon $x^{(t+1)}\leftarrow x^{(t)}$
- $\color{blue}{T^{(t+1)}\leftarrow\propto T^{(t)}\text{ ou } \propto=1^{-}}$ 
- $t\leftarrow t+1$
</div>

Si on fait un tirage aleatoire, *est-ce que c'est intelligent de mettre que des $1$ dans une grille vide d'un sudoku ?*
> Non, c'est la meme proba de mettre des $1$ que n'importe quel autre chiffre

|$\color{blue}{1}$|$\color{blue}{1}$|$\color{blue}{1}$|$\color{blue}{2}$|
|-|-|-|-|
|$\color{blue}{2}$|$\boxed{2}$|$\boxed{3}$|$\color{blue}{2}$|
|$\color{blue}{3}$|$\color{blue}{3}$|$\color{blue}{3}$|$\boxed{4}$|
|$\boxed{1}$|$\color{blue}{4}$|$\color{blue}{4}$|$\color{blue}{4}$|

*C'est quoi l'interet de ce tirage "moins con"? (et pas du tout aleatoire)*
> On peut changer $x^{(t)}$ aleatoirement (en echangeant des cases par exemples)

|$\color{blue}{1}$|$\color{blue}{1}$|$\color{blue}{1}$|$\color{red}{\boxed{3}}$|
|-|-|-|-|
|$\color{blue}{2}$|$\boxed{2}$|$\boxed{3}$|$\color{blue}{2}$|
|$\color{blue}{3}$|$\color{red}{\boxed{2}}$|$\color{blue}{3}$|$\boxed{4}$|
|$\boxed{1}$|$\color{blue}{4}$|$\color{blue}{4}$|$\color{blue}{4}$|

<div class="alert alert-success" role="alert" markdown="1">
On met de l'intelligence dans cet algo qui a vraiment besoin d'etre aleatoire
</div>

$$
P_{T\to+\infty}(X=x)=\frac{1}{Z}e^{-\frac{U(x)}{T}}\\
\color{red}{P_{+\infty}(x) = \frac{1}{Z}}\quad\text{uniforme}\\
\color{green}{P_1(x)=P(x)\\
P_0(x)=\varnothing\quad\forall x}
$$

<div class="alert alert-warning" role="alert" markdown="1">
Ce n'est pas une loi de probabilite car la somme des probas $=0$
</div>

On va determiner la loi de probas autrement, en regardant par exemple un ratio:

$$
\frac{P_T(X=x_{\text{solution}})}{P_T(X=x)}=e^{\boxed{\frac{-(\overbrace{U(x)-U(x_{\text{solution}})}^{\color{red}{\text{positif}}})}{T\color{green}{\to 0^+}}}}_{\color{blue}{\to-\infty}}\to 0^+\\
\frac{P_0(x\neq x_{\text{solution}})}{P_0(x_{\text{solution}})} = \varnothing\\
\begin{cases}
\forall x\neq x_{\text{solution}}, P_0(x)=\varnothing\\
P_0(x_{\text{solution}}) = 1
\end{cases}
$$

![](https://i.imgur.com/OdWzH55.png)

$$
\downarrow\\
P_0(x)=\begin{cases}
1&\text{si } x=x_{\text{solution}}\\
\varnothing &\text{sinon}
\end{cases}
$$