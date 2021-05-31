---
title:          "VTK-ITK: Traitement d'Image avec ITK"
date:           2021-05-31 10:00
categories:     [Image S8, MLRF]
tags:           [Image, MLRF, S8, couple]
description: Traitement d'Image avec ITK
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/Sk30HGfqd)

# Insight Toolkit (ITK)
- Open source
- Ecrite en C++
- Existe depuis 2000
- Environ 267 developpeurs
- Plus de 500k telechargements
- Investissement de la part du NIH: ~14M
- Algorithmes de traitement d'image seulement
- Pas de UI ou visualisation
- [www.itk.org](https://www.itk.org)

<div class="alert alert-warning" role="alert" markdown="1">
A chaque fois qu'on utilise une bibliotheque open source. il faut le mentionner
</div>

3 grandes famille de modalites:
- IRM
    - Rapide et non nocif (a notre connaissance)
    - On voit tres bien la matiere blanche/grise du cerveau
- Scanner
    - CB scanner, radio (rayons X)
    - Attentions aux rayons X
    - On voit tres biens les os
- Ultrasons
    - Si on attend un enfant par exemple
    - Non nocifs a notre connaissance MAIS besoin de signer pour une echographie une decharge (au cas ou)

## Visible human

Un condamne a mort aux US a donne son corps a la science
- A ete scanner en HD avec les rayons X (apres sa mort)
- Son corps a ete congele et decoupe en tranche
- Chaque tranche a ete photographiee

![](https://i.imgur.com/EAzYYMc.png)
> Vraie tranche d'Humain

<div class="alert alert-warning" role="alert" markdown="1">
Projet tres controverse
</div>

**MAIS**
- Tout le monde a acces aux images
- Tres utile pour la science
- 500 Go (pour les annees 2000, quantite enorme de donnees)

## Pourquoi CMAKE a ete cree
- Utilisation des images ci-dessus par tout le monde
- Chacun fait son algo dans son coin
- Gouvernement US a voulu tout centraliser "visible human toolkit" (aujourd'hui ITK)

<div class="alert alert-info" role="alert" markdown="1">
**ITK**
Boite a outils d'algorithmes de traitement d'image
</div>

<div class="alert alert-danger" role="alert" markdown="1">
Il n'y a **pas** d'outils de visualisation/interface graphique dans ITK
</div>
Ca reste une boite a outils et c'est pour que ce soit **portable**

## Developpeurs initiaux d'ITK

![](https://i.imgur.com/WSnWYG7.png)

Combinaison industriels/academique

# Traitement d'image
## Segmentation

![](https://i.imgur.com/7sw6FVX.png)

![](https://i.imgur.com/miUFhsx.png)

Aujourd'hui, le traitement d'image sert a **ameliorer** le traitement d'image.

*Pourquoi extraire la taille des ventricules ?*
![](https://i.imgur.com/2GyoaNC.png)

La taille des ventricules c'est important
- Lie a l'autisme
    - Evolution de la taille des ventricules: predire l'autisme rapidement chez l'enfant
    - Verifier que les ventricules grandissent correctement

<div class="alert alert-success" role="alert" markdown="1">
Plus tot on arrive a diagnostique, plus tot on arrive a traiter
</div>

> Exemple d'une tumeur: permet de detecter la tumeur + pour le traitement pour l'enlever

## Recalage

![](https://i.imgur.com/5vOnIgf.png)
> Le probleme, c'est que le patient est vivant

# Integrer ITK dans une application

![](https://i.imgur.com/fxkhZpu.png)
> On ne va pas fair d'interface graphique pendant le TP

## Generic programming

<div class="alert alert-info" role="alert" markdown="1">
ITK utilise beaucoup les template et est tres tres generique
</div>
<div class="alert alert-warning" role="alert" markdown="1">
Ca le rend un peu dur a utiliser
</div>
- La STL en C++
- Abstraction des types et actions

![](https://i.imgur.com/CzpTkAO.png)

## C++
- Utilisation de namespaces
- Utilisaiton de smart pointers
    - Propre pointeurs de ITK
- Gestion des exceptions

## Python Types

![](https://i.imgur.com/hTiqrCx.png)

Il faut connaitre le type de pixel sur lequel on travaille

## Streaming

<div class="alert alert-info" role="alert" markdown="1">
ITK permet de traiter des images qui ne rentrent pas en memoire
</div>

![](https://i.imgur.com/PSYE9LQ.png)

Le streaming d'ITK partitionne notre grille et applique nos filtres

![](https://i.imgur.com/QKVIdJE.png)

<div class="alert alert-warning" role="alert" markdown="1">
Si on a besoin de quelque chose (bordure, etc) coupe par un filtre
</div>
- En maillage: les **ghost cells**
- Similaire en ITK

> Exemple: convolution sur chaque partie partitionnee mais bordure coupee entre 2 

*Quelle taille pour une image d'un scanner ?*
Entre 10 et 25 Mo (meme decompresse, rentre largement en memoire)

<div class="alert alert-success" role="alert" markdown="1">
Nos donnees nous appartiennent, les hopitaux sont obliges de nous donner nos scanner/IRM etc.
</div>

### Pour le TP
<div class="alert alert-danger" role="alert" markdown="1">
On va travailler en TP sur DICOM
</div>
- Pas en 3D

## Gestion de la memoire
![](https://i.imgur.com/RfTHOfb.png)

## Pipeline de traitement

Un filtre prend une image en entree et une autre en sortie

![](https://i.imgur.com/v8LWQ5c.png)

On combine les filtres entre eux

![](https://i.imgur.com/LtGjaQl.png)

En tant que traiteur d'image, soit:
- On creer un nouveau filtre
- On utilise ce qui existe deja et on combine les filtres

# Segmentation
## Comment segmenter cette tumeur ?

![](https://i.imgur.com/eVS4CT9.png)
> La tranche est a l'envers car le patient est sur le dos

## Confidence Connected

![](https://i.imgur.com/WRR9Zgc.png)

On defini un point (un germe)

![](https://i.imgur.com/CuTCsmS.png)
> On agrandit le point
<div class="alert alert-info" role="alert" markdown="1">
Croissance de region
</div>

*Qu'est-ce qui est problematique sur ce genre d'algo ?*
Le `seed point` a ete mis a la main
- Pour un point ca va
- Mais pour + (genre 15) c'est plus dur

## Connected Threshold

![](https://i.imgur.com/RP1lqBn.png)
> A nous de definir upper bound et lower bound

## Isolated connected

Demande 2 seeds (un germe a l'exterieur et un a l'interieur)
- Calcul la moyenne 

![](https://i.imgur.com/5d6kbPI.png)

*Quelle methode est la meilleure ?*
Tout depend de notre image, ce que veut le practicien, etc.

## Watershed concept

<div class="alert alert-info" role="alert" markdown="1">
Algo qui prend en consideration les intensites mais aussi les contours
</div>

![](https://i.imgur.com/r80n8zc.png)

![](https://i.imgur.com/d0nA5uE.png)

<div class="alert alert-warning" role="alert" markdown="1">
ITK ne gere pas le streaming sur les algos iteratifs
</div>

## Shape detection

![](https://i.imgur.com/lcPrpzv.png)

![](https://i.imgur.com/GNsKIyf.png)

# Recalage

<div class="alert alert-info" role="alert" markdown="1">
Mise en correspondance d'images afin de pouvoir agreger leurs informations
</div>

![](https://i.imgur.com/BMDj7iU.png)

Exactement le meme cas pour les scanners

![](https://i.imgur.com/Bb9NHbp.png)
> La machine a gauche vaut ~60M d'euros

Si on veut combiner des scanners Rayons X et IRM, il faut faire du recalage
- Sauf dans le scanner PET-CT

![](https://i.imgur.com/88Tradi.png)

Recalage d'une eclipse de Lune (fait a la main sur PowerPoint par Julien Jommier)
![](https://i.imgur.com/NBSpq9z.png)

![](https://i.imgur.com/A3lDZHu.png)

## Composants du recalage
- Transformation
    - Si on a 2 images, comment est-ce qu'on transforme une image qui boufe pour l'aligner avec une autre image ?
- Metrique (de mise en correspondances)
    - Quand est-ce qu'on est alignes ou non
- Optimiseur
    - Descente de gradient

![](https://i.imgur.com/gTVGOgH.png)

![](https://i.imgur.com/iGSvNJJ.png)

## Transformation

- Translations (deplacements)
    - conserve distances et angles orientes
    - 2 parametres
- Rotations (isometrie)
    - conserve distances et angles
- Homotheties (similitude)
    - conserve les rapports entre les distances
- Affinites
    - conserve le parallelisme
    - 6 parametres
- Non-lineaires

## Transformations

![](https://i.imgur.com/rN67gES.png)

### Affine

![](https://i.imgur.com/lml7Yl9.png)

### Quelle tranformation ?

![](https://i.imgur.com/HANbgrb.png)

![](https://i.imgur.com/ZU9L0iu.png)

*Quelle transformation a ete faite sur cette image ?*

Homothetie avec juste un parametre

### Transformations Non-Lineaires

![](https://i.imgur.com/iGnQShn.png)

- Transformations elastiques ou non-rigides
- Exemples:
    - B-Splines (Combinaison lineaire de Spline)
    - Thin-plate splines

![](https://i.imgur.com/5t1y3xd.png)

## Metrique

<div class="alert alert-info" role="alert" markdown="1">
Mesures de similarite(s) entre la cible fixe et la source en mouvement
</div>

- Recalage iconique
    - Somme des differences au carre
    - Coefficient de correlation

### SSD

![](https://i.imgur.com/Zf8tVhf.png)

<div class="alert alert-warning" role="alert" markdown="1">
**Probleme**
Les 2 images doivent avoir la meme intensite (relation lineaire)
</div>

### Cross-Correlation

<div class="alert alert-info" role="alert" markdown="1">
Convolution sans inverser le signal
![](https://i.imgur.com/HoychQZ.png)

</div>

- $\bar f=$ moyenne de $f$
- $\sigma f=$ ecart type de $f$
- Relation affine entre les intensites

### Information mutuelle
- Issue de la theorie de l'information
- Relation statistique entre les intensites des 2 images
- Densite conjointe de probabilite des niveaux de gris
- Calcul d'un histogramme conjoint
- Mesure d'entropie


Histogramme conjoint:
![](https://i.imgur.com/YfsQALV.png)

<div class="alert alert-info" role="alert" markdown="1">
**Entropie**
Ou est presente l'information dans notre volume
</div>
- Tres serree: peu d'entropie
- Un peu partout: beaucoup d'entropie

![](https://i.imgur.com/QAfgwa9.png)

On a 2 images qui ont bouge, l'histogramme commence a etre diffus:
![](https://i.imgur.com/efvyIqO.png)

![](https://i.imgur.com/Q7VKH67.png)

Soit $g(x,y)$ la valeur de l'histogramme conjoint au point [x,y]:
![](https://i.imgur.com/bQ7qglv.png)

![](https://i.imgur.com/j4oR6u0.png)

Si on a 2 images alignees (meme patient):

![](https://i.imgur.com/yBWBfqZ.png)

## Optimiseur
- Descente de gradient
- Gradient conjugue
- Algo genetiques
- Powell
- LBFGS

## Interpolateur

![](https://i.imgur.com/g1MD5Qx.png)

<div class="alert alert-danger" role="alert" markdown="1">
![](https://i.imgur.com/uKGxwdK.png)

</div>

![](https://i.imgur.com/0cbCVsT.png)

![](https://i.imgur.com/zAXdKtM.png)

![](https://i.imgur.com/JlQ989t.png)

# Quiz
## Premiere question
On a 2 images du meme patient

![](https://i.imgur.com/g9iMQiM.png)

## Deuxieme question
![](https://i.imgur.com/JftyvQy.png)

- [ ] a) 2.0
- [X] b) 1.0
- [ ] c) 0.5

<div class="alert alert-success" role="alert" markdown="1">
Toujours reflechir dans le domaine physique, le patient a toujours le meme cerveau
</div>