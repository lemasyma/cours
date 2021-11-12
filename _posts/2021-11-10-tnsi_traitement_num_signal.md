---
title:          "TNSI: Traitement numerique du signal"
date:           2021-11-10 09:00
categories:     [Image S9, TNSI]
tags:           [Image, S9, TNSI]
math: true
---

Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/BJxQ-Ztvt)

# Presentation

Parcours:
- Ingenieur topographe - INSA
- These en traitement du signal et de l'image - Telecom

Ingenieur Chercheur a EDF R&D (Saclay)
- Groupe realite virtuelle et visualisation scientifique (avec Arnaud MAS)
- Numerisation et apprentissage statistique (image et 3D)

## Groupe Realite Virtuelle Visualisation Scientifique

- Aider l'exploitant des sites de production nucleaire a decider lors des phases de preparation et de realisation des arretes de tranche
- Aider

## OCR pour les plans techniques

![](https://i.imgur.com/rroAJpP.png)

## La reconnaissance de forme dans les images

![](https://i.imgur.com/IZye8az.jpg)

Segmentation semantique: deux reseau
- Segmentation pixelique
- Segmentation semantique pour classifier les pixels de l'image

![](https://i.imgur.com/lq7hSnj.png)

## La reconnaissance de forme *dans les nuages de points*

![](https://i.imgur.com/kAh6IEB.jpg)
> Donnees DP2D FES2
> Local R250
> 280 millions de points

Actuellement: manuel
- Segmentation en petit nuage de points + ajustement de forme

# Traitement numerique du signal

<div class="alert alert-info" role="alert" markdown="1">
**Definition**

Representation de la variation d'un phenomene physique

</div>

> Exemples
> Evolution de la temperature ou de la pression dans le temps

<div class="alert alert-info" role="alert" markdown="1">
**Definition**

Transcrire numeriquement (i.e. des donnees) un signal continu (monde reel)

</div>

On veut passer du monde continu au monde discret

![](https://i.imgur.com/cklHObs.png)

*Comment on fait le passage du continu au discret ?*
> On va faire un echantillonage en temps et en amplitude

*Quelle est la precision de cette discretisation ?*
> On utilise le theoreme de Shannon

En resume: on prend notre signal, on compare dans chaque base de fonction a quel point notre signal ressemble et on va pouvoir voir a quel point notre signal est haute frequence et basse frequence.

![](https://i.imgur.com/TvaWcT2.png)

<div class="alert alert-danger" role="alert" markdown="1">
Avec les transformee de Fourier, on veut passer en temporel **sans perdre d'information**
</div>

## Theoreme d'interpolation

<div class="alert alert-info" role="alert" markdown="1">
Decoule du theoreme de Shannon
</div>

On utilise un *sinus cardinal*

Le theoreme de Shannon nous dit qu'on a un signal continu:

$$
x(t) = \sum_{n=-\infty}^{+\infty}x[n]\underbrace{\frac{\sin\biggr(\frac{\pi(\overbrace{t-\color{red}{nT_e}}^{\text{translation}})}{\underbrace{\color{red}{T_e}}_{\text{echelle}}}\biggr)}{\frac{\pi(t-nT_e)}{T_e}}}_{\color{red}{sinc}}
$$

![](https://i.imgur.com/xPCan8j.png)

## Exercice

$$
x(t) = \sin(10t) + 2\sin(2t) + \sin(5t) - 3\sin(\frac{t}{2})\\
t = [-2, 2]\to 400
$$

1. Normaliser et centrer
2. $T_e=0.1$
3. Interpoler avec $sinc$

On reprendre notre figure

![](https://i.imgur.com/rWmIKr9.png)

On prend des echantillons a intervalles regulire

![](https://i.imgur.com/ZdBEWja.png)

On va sommer les sinus cardinaux:

![](https://i.imgur.com/1FBfJc8.png)

Ca va nous permettre de reconstruire notre signal:

![](https://i.imgur.com/fplEQWb.png)

*Quel est l'interet du sinus cardinal ?*
> On peut utiliser n'importe quelle interpolation, mais le sinus cardinal est le meilleur

## Quantification

<div class="alert alert-info" role="alert" markdown="1">
**Quantification scalaire**: arrondir a l'entier le plus proche
</div>

![](https://i.imgur.com/FPDCbTe.png)

- $x$: amplitude des valeurs
- $q(x)$: valeur de quantification

## Traitement

*Comment on debruite un signal ?*
> Convolution avec une fonction gaussienne ?
> Convolution avec une porte ?
> Non local means ? (c'est un flou gaussien ou un flou uniforme)

On a un signal avec un flou gaussien:

![](https://i.imgur.com/4EWwML3.png)

<div class="alert alert-success" role="alert" markdown="1">
On fait une convolution avec une porte
</div>

## En resume

- Comment echantilloner et reconstruire un signal
- Comment analyser un signal
- Comment filtrer une partie de l'information d'un signal

# Transformee de Fourier

1. Rappel rapide
2. Analyser harmonique
    1. Decomposition en serie de Fourier
    2. Discrete Time Fourier Transform (DTFT)
        - Tf a temps discret
    3. Discrete Fourier Transform (DFT)
        - TF discrete
    4. Continuous Fourier Transform (CFT)
    5. Fast Fourier Transform (FFT)

## Produit scalaire

*Comment est-ce qu'on calcule un produit scalaire ?*

$$
\langle x, y\rangle = \sum_{n=-\infty}^{+\infty}x[n]y[n]^*\\
\langle x, y\rangle = \int_{-\infty}^{+\infty}x(t)y^*(t)dt
$$

<div class="alert alert-warning" role="alert" markdown="1">
Avec Fourier, on est en complexes
</div>

$$
\Vert x\Vert^2 = \langle x,x\rangle = \sum_{n=-\infty}^{+\infty}\vert x[n]\vert
$$

## Decomposition/reconstruction

Soit $$\{f_n\}_{n\in\mathbb N}\to$$ base orthogonale.

$$
\langle f_n,f_p\rangle = 0\quad n\neq p
$$

$\exists$ une suite $\lambda[n]$ telle que $\lim_{N\to+\infty}\Vert x-\sum\lambda[n]f_n\Vert = 0$

$$
x=\sum_{n=0}^{+\infty}\lambda_n f_n\quad\text{avec }\lambda_n = \frac{\langle x,f_n\rangle}{\Vert f_n\Vert^2}
$$

## Exercice

$$
x = \sin(2\pi t) + 2\sin(3\times 2\pi t) - 3\sin(5\times 2\pi t) + \sin(7\times 2\pi t)\\
t = [0,1]
$$

1. 
    - Tracer $x$ avec 1000 echantillons
    - Decomposition de $x$ avec $$\{\sin(n\cdot 2\pi t)\}_{n\in N}\to$$ $N = [0,...,5]$ ou $N = [0,...,20]$
        - Verifier l'orthogonalite
    - Tracer les coefficients
    - Reconstruction
2. Si on ajoute une phase au sinus ?
    - Idem