---
title:          "DLIM: Reseaux neuronaux convolutifs"
date:           2021-11-08 14:00
categories:     [Image S9, DLIM]
tags:           [Image, S9, DLIM]
math: true
---

Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/B1-YkiLwt)

# Un reseau de neurones convolutif

![](https://i.imgur.com/Gusjhh3.png)

## Le but est d'extraire les caracteristiques

![](https://i.imgur.com/HXXmFvh.jpg)

## Les formules de convolution

Continue 1D:

$$
(f * g)(x) = \int_{-\infty}^{+\infty}f(x-t)g(t)dt = \int_{-\infty}^{+\infty} f(t)g(x-t)dt
$$

Discrete 2D:

$$
(f*\omega)(x,y) = \sum_{dx=-a}^a\sum_{dy=-b}^b\omega(a + dx, b + dy)f(x + dx, y+dy)
$$

$f$ est l'aimeg, $\omega$ le noyau, son support est $[-a,a]\times[-b, b]$

Exemple de noyaux $\omega$ (WP Noyau_(traitement_d'image)):

![](https://i.imgur.com/X1325di.png)

# Conv2D

```python
x = kl.Conv2D(filters = 4, kernel_size=(5, 5))(x)
```

L'image d'entree a 3 canaux -> chaque filtre a $5\times5\times 3 + 1$ poids
L'image de sortie a 4 canaux, elle pert 4 pixels dans chaque direction

## En details + stride + padding = 'same'

```python
Conv2D(filters = 2, kernel_size = (3, 3), stride = (2, 2), padding = 'same')
```

![](https://i.imgur.com/do3CIuS.gif)

- Stride: une facon de reduire la taille d'une image
- padding = 'same': la sortie a la meme taille

## Convolution a trous

En anglais: *atrous convolution*

```python
Conv2D(32, kernel_size=3, dilatation_rate=(2, 2))
```

![](https://i.imgur.com/yDxMfxd.gif)

<div class="alert alert-success" role="alert" markdown="1">

Couvre la meme surface qu'un noyau $5\times 5$, ou que $2$ convolutions $3\times 3$ a la suite, mais pour un cout moins cher (en poids)

</div>

Ne reduit pas la taille de l'image (padding = `same`)

## Convolution separee 

- **spatiale**: une conv $2D\to1$ conv. $1D$
- **profondeur**: $N$ conv $2D$ sur $M$ couches $\to$ $M$ conv $2D$ puis $N$ conv $1D$

**Convolution separeee spatiale**

![](https://i.imgur.com/CiDOpZd.png)

En pratique on fait:

![](https://i.imgur.com/StH7rLK.png)

**Conv separee en profondeur** 

```python
kl.SeparableConv2D
```

Ici 3 couches:
- $3$ conv $2D$ + $4$ conv $1D$
- $4$ couches en sortie

Gain de calcul important
perte de representation $\to$ utilise

[MobileNet](https://arxiv.org/abs/1704.04861)

## La convolution transposee (ou deconvolution)

<div class="alert alert-info" role="alert" markdown="1">
*Convolution*: **concentre** en un pixel un bloc de pixel (fois un noyau)
</div>

<div class="alert alert-info" role="alert" markdown="1">
*Conv transposee*: **distribue** un pixel (fois un noyau) a un bloc de pixel
</div>

![](https://i.imgur.com/RBr2eiZ.png)


Mathematiquement les deux sont des convolutions mais la conv. transposee a pour but de simuler l'operation inverse de la conv

$$
\begin{aligned}
\text{propagation conv transposee} &\leftrightarrow \text{retro-propagation conv}\\
\text{retro-propagation conv. transposee} &\leftrightarrow\text{propagation conv.}
\end{aligned}
$$

## Trucs d'architecture

<div class="alert alert-danger" role="alert" markdown="1">
**Pooling**

```python
kl.MaxPooling2d(pool_size = (2, 2))
```
![](https://i.imgur.com/jiVaceA.png)

Si on veut augmenter le nombre de couches il faut diminuer la taille de l'image sinon BOOM

On veut une vision multi-echelle il faut diminuer la taille de l'image + ponts.

L'inverse du *pooling* est kl

</div>


<div class="alert alert-danger" role="alert" markdown="1">
**Ponts**

La grande astuce de ResNet qui leur a permis de tout gagner

![](https://i.imgur.com/geGwGQT.png)

![](https://i.imgur.com/gsMUa9w.png)

![](https://i.imgur.com/0JZRffW.png)
- vert $\to$
- rouge $\leftarrow$

Prog. et retro-prog.

Lors de la retropropagation l'erreur prend le pont et les convolutions $\to$ les premieres couches sont corrigees

</div>

<div class="alert alert-danger" role="alert" markdown="1">

**Dropout ou BatchNormalization**

Pas besoin de dropout si BatchNormalization

![](https://i.imgur.com/LKglSCh.png)

Evite que les poids importants en bloquent d'autres

![](https://i.imgur.com/a6ZPQiZ.png)

Apres convolution
Avant fonction d'activation
Reduit le besoin de normaliser les donnees

</div>

# Types de problemes en vision

Semantic segmentation

![](https://i.imgur.com/T8Yjc0Z.png)

![](https://i.imgur.com/Fe8XbHm.jpg)

- Classification
- Classification + localisation
- Object detection
- Instance segmentation
    - Celle qu'on va faire

## U-net (2015)

Separation semantique d'images medicales

![](https://i.imgur.com/TIXfKwb.png)

Multi-echelle

*Notre projet aujourd'hui !*

Copy & crops: ce sont des PONTS
- Ca sert a faire des concatenations

# Fonctions d'erreur pour la segmentation

Si chaque image de sortie represente les pixels appartenant a la classe $k$, alors on peut finir avec un `softmax`: $y+k = e^{z_k}/\sum_{i}e^{z_i}$

- Erreur quadratique `mse`: pente douce, pas d'information d'exclusion
- Entropie croisee: $E=-\sum_kt\log y_k+(1-t_k)\log(1-y_k)$
    - `binary_crossentropy` avec $t_k=0$ ou $1$
    - `categorical_crossentropy` avec resultats sous la forme $[0,0,..,1,..,0]$ pour indiquer la classe $k$
    - `sparse_categorical_crossentropy` avec les classes indiques par des entier

```python
y_true = [[1, 2], [0, 2]] #image 2x2 with 3 categories
y_pred = [[0.05, 0.95, 0], [0.1, .01, 0.8], #proba for each category
         [0.7, 0.2, 0.1], [0.2, 0.2, 0.6]] #for each pixel
loss = keras.losses.SparseCategoricalCrossentropy()
loss(y_true, y_pred).numpy()
```


<div class="alert alert-danger" role="alert" markdown="1">

**Focal loss**

$$
E_{FL} = -\sum_k t_k(1-y_k)^{\gamma}+(1-t_k)(1-y_k)^{\gamma}\log(1-y_k)
$$

Comme la pente du log est forte, elle favorise les cas simples a detecter. On peut ecraser la courbe de $(1-\gamma_k)$ pour aider à trouver les cas difficiles.

![](https://i.imgur.com/L6XTOML.png)

</div>

# Augmenter le nombre de donnees

Souvent c'est bien utile, en particulier lorsqu'on manque de donnees.

![](https://i.imgur.com/7dtm6dZ.png)

Parfois ca rend la tache plus difficile et ca ne marche pas.

```python
ImageDataGenerator
```