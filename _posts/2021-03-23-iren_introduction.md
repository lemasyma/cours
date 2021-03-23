---
title:          "IREN: Retropropagation du gradient"
date:           2021-03-23 11:00
categories:     [Image S8, IREN]
tags:           [Image, Sante, IREN, S8, réseaux neuronnaux]
description: Retropropagation du gradient
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/HkbsAQDN_)

[Index du cours](http://www.ricou.eu.org/irenotes_rn.html)

# Rétropropagation du gradient

![](https://i.imgur.com/1iJPfKY.png)
Fonction logistique

Calculons l’influence du poids $w_{2,2}^2$ sur l'erreur quadratique $E:\frac{\delta E}{\delta w_{2,2}^2}$

La derivee partielle de $y$ par rapport a $z$ est $y(1-y)$

<div class="alert alert-warning" role="alert" markdown="1">
On note t (*truth*) la vraie valeur avec l'erreur quadratique
</div>

[Correction](http://www.ricou.eu.org/irenotes_rn.html#R%C3%A9tropropagation%20du%20gradient)

## Que vaut le gradient de $E :\nabla E$?
*Qu'est-ce qu'on modifie pour arriver au bon resultat ?*
Les poids, on a 18 poids donc $\nabla E$ est a dimension 18.

$$
\forall \text{ layer }l, W^l\leftarrow W^l-\eta\nabla E(W^l)
$$

## Pourquoi ce titre ?
On fait une propagation a l'envers, *"retropropagation"* pour remonter l'erreur 

# La methode du gradient
Le but est de trouver le vecteur $w$ qui minimise notre erreur $E$

![](https://i.imgur.com/W9U5i9B.png)

Avec un $w_0$ choisi, l'algorithme de descente du gradient est:

$$
w_{t+1}=w_t-\eta\nabla E(W_t)
$$

jusuq'a atteindre un seuil choisi

# Representation graphique
Cas simple: l'erreur est une fonction convexe.

Si on modifie les cas apres chaque donnees, on risque d'osciller
![](https://i.imgur.com/YSjVzEC.png)

<div class="alert alert-success" role="alert" markdown="1">
travailler par paquet de données. $\rightarrow$ Notion de batch
</div>

Lorsque l’elliptiques est allongée, son gradient est quasiment orthogonal à son axe long ce qui n’est pas du tout la bonne direction vers le minimum.

![](https://i.imgur.com/V3yVlGn.png)

<div class="alert alert-success" role="alert" markdown="1">
la convergence sera longue
</div>

# Travail sur les donnees
## Jouer sur l'echelle

$$
y=w_0i_0+w_1i_1\\
E=(y-t)^2
$$

![](https://i.imgur.com/rLnghJw.png)

Soit comme jeux de donnees:

$$
\begin{aligned}
&\begin{matrix}
0,1&10&\rightarrow&2\\
0,1&-10&\rightarrow&2\\
\end{matrix}
&\begin{matrix}
1&1&\rightarrow&2\\
1&-1&\rightarrow&2\\
\end{matrix}
\end{aligned}
$$

La fonction d’erreur correspondante a la forme suivante:
![](https://i.imgur.com/ZTxEV9K.png)

<div class="alert alert-danger" role="alert" markdown="1">
**normaliser** les données pour éviter des fonctions d’erreur écrasées
</div>

## Translation

$$
y=w_0i_0+w_1i_1\\
E=(y-t)^2
$$

![](https://i.imgur.com/Nq7NsDR.png)

Soit comme jeux de donnees:

$$
\begin{aligned}
&\begin{matrix}
101&101&\rightarrow&2\\
101&99&\rightarrow&0\\
\end{matrix}
&\begin{matrix}
1&1&\rightarrow&2\\
1&-1&\rightarrow&0\\
\end{matrix}
\end{aligned}
$$

L’erreur correspondante aux jeux de données a la forme suivante:

![](https://i.imgur.com/unZQvRv.png)

<div class="alert alert-danger" role="alert" markdown="1">
**centrer** les données pour éviter des fonctions d’erreur écrasées.
</div>

# Les minimums locaux
Une fonction d'erreur n'est pas forcement elliptique, il faut s'attendre a avoir des minimums locaux.
![](https://i.imgur.com/uByhkaS.png)

Le point de convergence dépend du point de départ d’où le risque de finir
dans un minimum local.

> Si on lance une bille, en fonction de la ou elle se trouve elle fini dans un minimum local

*Comment sortir d’un minimum local pour rejoindre un minimum global ?*

# Les solveurs
Pour contrer ces differents problemes, on a differents solveurs

## Moment et Nesterov
On donne une inertie $\alpha$ a la methode:
![](https://i.imgur.com/40xM4zO.png)

On ne calcule pas le gradient au poids des poids, mais aux poids modifies.
Nesterov propose de travailler sur les données mise à jour:
![](https://i.imgur.com/4gzOtxK.png)

![](https://i.imgur.com/56Prtas.png)

![](https://i.imgur.com/FUX1fRY.png)

Ca peut aider a "sortir" des trous et reduire les oscillations

> Si notre bille s'approche d'un trou, on lui dira "Non va pas par la, fait demi-tour"

## RMSprop
Le coef d'apprentissage $\eta$ influence beaucoup la convergence.

On peux choisir autant de $\eta_i$ que de parametres existants: $\eta_i=\varepsilon\mu_i\frac{\delta E}{\delta \omega_i}$

Avec:
![](https://i.imgur.comnkhdGr.png)

Ca marche mal avec les "*mini-batches*"
- $9\frac{\delta E}{\delta \omega_i}$ de $0,1$ suivi d'une de $-0,9$ devrait faire du surplace, mais pas avec cette methode

On prefere moyenner les gradients dans le temps, l'algorithme est:
![](https://i.imgur.com/aqeMBq3.png)

## Adagrad
On cherche le **w** aui minimise $E$, donc $\nabla E(w)=0$

Au pas de temps $t$, on est au point $w_t$, on cherche $\delta w$ tel que $\nabla E(w-t+\delta w)=0$ donc avec un developpement limite:

![](https://i.imgur.com/f19tbNy.png)

Avec $\nabla^2E$ la matrice hessienne de $E$.
L'algorithme iteratif est:
![](https://i.imgur.com/LVUWV3S.png)

Calculer l'inverse de la matrice essienne est trop couteux, on va chercher quelque chose qui lui ressemble, $V_t$ pour Adagrad:
![](https://i.imgur.com/YcuNNbc.png)

## Exemple de convergence
Regardons à quelle vitesse convergent différentes méthodes suivant la forme
de la fonction d’erreur.

[An overview of gradient descent optimization algorithms](https://ruder.io/optimizing-gradient-descent/)

# Trois types de reseaux neuronaux
Quelques exemples de reseaux neuronaux:
- reseau simple pour separer des donnees
    - Qui a le cancer, qui ne l'a pas
- reseau recursif pour faire des additions
- reseau de convolution pour comprendre une image

![](https://i.imgur.com/qyJp6Mn.png)

*Une idée pour séparer les données sur deux cercles?*

## Separation
Relu defini un demi-plan, on va utiliser 6 Relu $(\nearrow)$ pour faire un cercle grossier et une sigmoide $(\rightsquigarrow)$ pour separer les 2 cercles

![](https://i.imgur.comh4Y0PC.png)

## Recursif
![](https://i.imgur.com/otGKR1v.png)

On veut calculer $0101011+1001110$, on fait comme un addition a la main

<div class="alert alert-danger" role="alert" markdown="1">
On a besoin d'avoir des retenues (si on a $1+1$ par exemple), c'est un reseau a **memoire**.
</div>

Les cellules grises sont la memoire, cad les retenues, des operations precedentes.

<div class="alert alert-warning" role="alert" markdown="1">
Ces reseau sont compliques a faire converger, il faut que la memoire fonctionne correctement.
</div>

## Convolution
<div class="alert alert-success" role="alert" markdown="1">
Les *Convolution Neural network* sont la grande reussite du *deep learning*.
</div>

Le but est de travailler sur des images pour en extraire ses caracteristiques

![](https://i.imgur.com/zojnP0V.png)

En entrée nous avons une image $N \times N \times 3$ (en RGB) dont nous diminuonsla surface à chaque couche du réseau pour augmenter sa profondeur.

À la fin on peut voir l’image comme un vecteur de caractéristiques.

Ensuite (pas sur le dessin) on peut utiliser un réseau neuronal classique pour classer l’image.

### Les convolutions
![](https://i.imgur.com/rcyq7eD.png)

<div class="alert alert-info" role="alert" markdown="1">
Un filtre est un masque d'une certaine taille dont on a donné une valeur pour chacune des couches
</div>

On fait la somme de tous les poids $\times$ toutes les valeurs et on travaille un pixel sur 2.

<div class="alert alert-warning" role="alert" markdown="1">
La taille des filtres est le nombre de canaux de l'image de depart.
</div>

*Chacun des 5 filtres aura combien de canal ?*
2 car l'image d'arrivee a 2 canaux

### Diminuer la surface
L'exemple précédent saute un pas (travailler un pixel sur 2), qui réduit la surface. Si on a pas de saut de plus de filtre $\rightarrow$ le nombre de données EXPLOSE.

<div class="alert alert-info" role="alert" markdown="1">
**pooling**: On réduit la surface de l'image au fur et a mesure qu'on augmente sa profondeur.
</div>

![](https://i.imgur.com/KSvGeGT.png)

Le choix du maximum est le plus utilisé. On pourrait faire une moyenne mais cela risque de réduire le contraste de l’image.

### Le Net 5
Le premier CNN, qui a bien fonctionné, pour lire les codes postaux sur les enveloppes, développé en 90 par Yann Le Cun

![](https://i.imgur.com/VCiBbFU.png)

### Evolution des CNN

Les reseaux augmentent en précision, taille et nombre d'opérations.

![](https://i.imgur.com/insDjYW.png)

De plus en plus compliqué:

![](https://i.imgur.com/ImdxGGX.png)

On rajoute des trucs pour améliorer les résultats (ou converger).

L'idée est de reprendre des données antérieures pour ne pas trop oublier. Le saut correspond à l’opération:

$$
y=F(x,w)+x
$$

# Kaggle
Le [Kaggle](https://www.kaggle.com/oricou/code) d'Olivier Ricou