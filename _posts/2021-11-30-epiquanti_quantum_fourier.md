---
title:          "DLIM: Deepfake"
date:           2021-11-29 14:00
categories:     [Image S9, DLIM]
tags:           [Image, S9, DLIM]
math: true
---

Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/Bkh1-8MYF)

# Deepfake

Les GAN permettent de creer de faux surprenat avec des reseaux profonds (d'ou *Deepfakes*)
- Creation de visage (StyleGAN) ![](https://i.imgur.com/IbMcGmR.png)
- Fausse video comme celle de [Poutine soulignant la faiblesse des democraties](https://youtu.be/sbFHhpYU15w)

## Autoencoders

<div class="alert alert-info" role="alert" markdown="1">
Avant les GAN il y a eu les autoencodeurs qui ne demandent pas de verite terrain
</div>

![](https://i.imgur.com/IPpGxM8.png)

Les resultats sont moyens

![](https://i.imgur.com/USNs8FD.png)

## U-net

<div class="alert alert-info" role="alert" markdown="1">
U-net est une sorte d'autoencodeur avec une verite terrain et des ponts
</div>

![](https://i.imgur.com/VLI4MzU.png)

## Autoencodeur variationel (VAE)

On decoupe l'espace latent en sa moyenne et son ecart-type

![](https://i.imgur.com/NIX9qzr.png)

Pour construire ce reseau on definit 2 fonctions d'erreur:
- Distance image d'arrivee/image de depart (*cf* autoencodeur)
- Divergence de Kullback-Leibler entre le vecteur de l'espace latent et une gaussienne type: $KL(N(\mu, \sigma), N(0,I))$

$$
E=\alpha E_{reconstruction} + \beta[\text{mean}^2 + \text{std_deriv}^2 - \log (\text{std_deriv}^2)-1]
$$

## VAE - generation

<div class="alert alert-info" role="alert" markdown="1">
On peut créer de nouvelles images en gardant la moyenne et en modulant l’écart type $z=\mu+\varepsilon\sigma$
</div>

Avec les chiffres manuscrits et un espace latent a 2 dimensions $[\mu, \sigma]$ on a:

![](https://i.imgur.com/Dsivdsn.png)

[Exemple de Keras](https://keras.io/examples/generative/vae/)

# Vector Quantised-Variational AutoEncoder (VQ-VAE)

On fabrique une collection de valeurs de vecteurs latents (*embedding space*). Une valeur est un vecteur lorsque le vecteur latent est en 3D

Si la sortie de l'encodeur est de $32\times 32\times 50$ alors la collection a des vecteurs de dimension $50$.

On traduit la sortie de l'encodeur en prenant pour chaque valeur, la plus proche dans la collection

![](https://i.imgur.com/ZUF0W9Y.png)

## VQ-VAE Compression

![](https://i.imgur.com/BI494c2.png)

Un facteur de compression de $42$:
- L'image d'origine a $128\times128\times 3\times 8$ bits
- L'image est encodee avec $32\times32\times9$ bits ($521$ valeurs possibles)
- (il faut aussi stocker la collection de valeurs soit $512\times D$)

On peut entrainer un classifieur sur les images $32\times 32\times 1$, ca marche

## VQ-VAE-2 - Multi-echelle

![](https://i.imgur.com/0FqjEWA.png)

# GAN

<div class="alert alert-info" role="alert" markdown="1">
Un Generative Adversarial Network (GAN) est un autoencodeur avec un **discriminateur** qui indique si le resultat est un vrai ou faux

![](https://i.imgur.com/w4PY46X.png)

</div>

L'erreur du discriminateur permet qu'il se corrige (minimise l'erreur) et que le generateur se corrige (maximise l'erreur du discriminateur)

## Conditional GAN

<div class="alert alert-info" role="alert" markdown="1">
Le principe est d'enrichier un GAN en ajoutant des informations supplementaires (la classe de l'image par ex.) en entree du generateur et du discriminateur

![](https://i.imgur.com/TM8yxrE.png)

</div>

<div class="alert alert-success" role="alert" markdown="1">
On a ainsi des images plus realistes en sortie
</div>

## Pix2Pix

C'est un GAN conditionel

![](https://i.imgur.com/64eapce.png)

Le generateur est un reseau en U et le discriminateur un classifieur CNN adapte.

On peut ainsi generer des images a partir de dessins.

# Cycle GAN

*Peut-on faire de l'auto-apprentissage (sans verite terrain) avec un GAN ?*

Si le but est de passer d'un type d'image a un autre, c'est possible.
Pour cela on utilise 2 generateurs, $G$ et $F$, et 2 discriminateurs, $DX$ et $DY$
- $G$ fabrique une image de type $Y$ a partir d'une image de type $X$
- $F$ fabrique une image de type $X$ a partir d'une image de type $Y$
- $DX$ indique si l'image donnee est vraie ou a ete generee par $F$
- $DY$ indique si l'image donnee est vraie ou a ete generee par $G$

![](https://i.imgur.com/kJdVWwj.png)

## Applications

![](https://i.imgur.com/0JsEQel.png)

# StyleGAN

![](https://i.imgur.com/CnNihr6.png)

## Melange de style

Avec 2 vecteurs de l'espace latent on peut melanger $2$ visage en injectant le 1er jusqu'a une couche dans la synthese, puis le second

![](https://i.imgur.com/DiVS1JF.png)

Plus on injecte tard le 2e, moins l'impact est important (seulement les hautes frequences)

## Vers le visage moyen

Lorsqu'on est dans l'espace $\mathcal W$ avec une valeur latente $w$ on peut interpler le visage moyen $\bar w$

$$
w=\bar w+\psi(w-\bar w)
$$

![](https://i.imgur.com/d5YVMmr.png)
