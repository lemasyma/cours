---
title:          "TIFO: Introduction a la morphologie mathematique, partie 2"
date:           2021-04-02 9:00
categories:     [Image S8, TIFO]
tags:           [Image, TIFO, S8, morphologie mathematique, niveau de gris, minima, maxima, watershed]
math: true
description: Introduction a la morphologie mathematique, partie 2
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/rkxBXHEHO)

# Rappels
- erosion et dilatation
- z erosions de taille y = une erosion de taille $z\times y$
- z ouverture de taille y $\neq$ une ouverture de taille $z\times y$

![](https://i.imgur.com/YmqOXng.png)

## Niveau de gris
On peut voir l'erosion et la dilatation comme une etude des niveaux de gris presents dans une fenetre glissante representee par l'element structurant

![](https://i.imgur.com/in3p99j.png)

On regarde le ixel de l'origine de l'element structurant. On attribue le min ou max pour les pixels correspondants a l'element structurant de leurs niveaux de gris

![](https://i.imgur.com/CfS8Swb.png)

## Filtres alternes sequentiels

<div class="alert alert-info" role="alert" markdown="1">
Une repetetition des compositions (fermeture et ouverture) pour debruiter progressivemenent en perdant le moins d'infos possible
</div>

![](https://i.imgur.com/ozL9FlV.png)
![](https://i.imgur.com/GGpbZcg.png)

- alternes: on alterne les filtres
- sequentiel: on augmente la taille de l'element structurant au fur et a mesure

## *Top hat*
![](https://i.imgur.com/J6JQn8N.png)

![](https://i.imgur.com/UMvbHSw.png)

![](https://i.imgur.com/M7JGQWw.png)

## Exemple pas du tout scientifique
> J'ai pris Harry et je l'ai ouvert

Harry en gris - Harry en gris ouvert =
![](https://i.imgur.com/JdorL9s.png)
> Dindon is that you ??

La dinde a un niveau de gris d'ecart avec l'image originale

## Bilan
- Le nom "morphologie mathematiques" a ete choisi dans un bar
- Morpho = considerer les images commes des paysages ~~Minecraft~~
- Non-lineaire: insensible au contraste
- Erosion et dilatation sont amis pour la vie
- On peut selectionner des objets grace a leur forme/taille (geometrie)
- La morpho est tres utile pour le filtrage d'image
- LES DINDES ONT PRIS LE CONTROLE DU MONDE

# De nouveaux outils
## Retournons sur Harry et son patronus


![](https://i.imgur.com/JdorL9s.png)

On augmente la taille de l'element structurant = tout est plus visible (image incoming)

Simple dilatation
![](https://i.imgur.com/udh3KIl.png)

## Gradients morphologiques
Dinde binaire:
![](https://i.imgur.com/I3Facfv.png)

<div class="alert alert-warning" role="alert" markdown="1">
La dilatation va *"augmenter les bords"*
</div>

<div class="alert alert-danger" role="alert" markdown="1">
Soustraire les 2 images, c'est le **gradient externe**
</div>

Avec une erosion:
![](https://i.imgur.com/5FSsrB5.png)

<div class="alert alert-warning" role="alert" markdown="1">
L'erosion va *"grignoter les bords"*
</div>

<div class="alert alert-danger" role="alert" markdown="1">
C'est le **gradient interne**
</div>

En niveau de gris:
![](https://i.imgur.com/fzIi23h.png)

### Bilan du gradient

![](https://i.imgur.com/rEgW6Hn.png)
![](https://i.imgur.com/dcOzc3m.png)

<div class="alert alert-warning" role="alert" markdown="1">
Ces gradients se ressemblent beaucoup!
</div>

Il faut choisir le gradient au cas par cas.

## La squeletisation

<div class="alert alert-info" role="alert" markdown="1">
On va chercher le **squelette** de notre objet.
</div>

L'idee c'est de prendre la position des centres des boules max inclues dans l'objet etudie
- On fait grossir des boules au fur et a mesure (ray marching style)

![](https://i.imgur.com/EPXKQ5q.png)

<div class="alert alert-warning" role="alert" markdown="1">
A partir du moment ou l'objet touche le bord, ca fait n'importe quoi
</div>

## Carte des distance

<div class="alert alert-info" role="alert" markdown="1">
Attribuer a chaque pixel de l'ojet concerne sa distance au bord
</div>

![](https://i.imgur.com/8GyKCe6.png)

## Outil de segmentation: le Watershed

> Ou ligne de partage des eaux

![](https://i.imgur.com/3vzYvyy.png)

![](https://i.imgur.com/q0rzomN.png)

<div class="alert alert-info" role="alert" markdown="1">
On *"inonde"* les vallees (minima locaux) au fur et a mesure que l'on "monte" en niveau de gris.
</div>

- Quand 2 vallees se recontrent, cela cree une ligne qui est la limitation entre 2 objets.
- En fonction de l'implem, il faut des marqueurs ou non

<div class="alert alert-warning" role="alert" markdown="1">
Toujours lire la doc de la fonction de Watershed qu'on utilise
</div>

<div class="alert alert-warning" role="alert" markdown="1">
S'il n'y a pas de marqueurs et que l'image a beaucoup de minima locaux, on a une **sur-segmentation**
</div>

## Les minima/maxima locaux

<div class="alert alert-info" role="alert" markdown="1">
**Extrema local**: point ou groupe de point dont la valeur est extreme dans un voisinage donne
</div>

![](https://i.imgur.com/G7nUPmT.png)

### Les maxima locaux

On peut definir des profondeurs de maxima

![](https://i.imgur.com/JgMc9C5.png)

<div class="alert alert-info" role="alert" markdown="1">
On peut selectionner les maxima qui se "distinguent" vraiment du reste
</div>
- On calcule sa profondeur pour chaque maxima
    - Niveaux de gris necessaire pour qu'il n'y a plus de maxima
- On vide l'eau qui a inonde partout sous la courbe
    - On regarde quand les regions fusionnent

<div class="alert alert-success" role="alert" markdown="1">
C'est *l'inverse* du Watershed
</div>

## Reconstruction geodesique

<div class="alert alert-info" role="alert" markdown="1">
Recuperer uniquement certains objets a l'aide de marqueurs
</div>

![](https://i.imgur.com/aDBrVDY.png)

Implem: dilatations successives jusqu'a **idempotence**

## Bouchage de trous

![](https://i.imgur.comm3dUeA.png)

Rectangle rouge = marqueur du fond

## Elimination d'objets touchant les bords

![](https://i.imgur.com/biF5XGt.png)
