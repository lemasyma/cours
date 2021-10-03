---
title:          "PFEE RORPO"
date:           2021-02-01 15:30
categories:     [Image S8, PFEE]
tags:           [Image, S8, PFEE]
math: true
description: Implémentation C++ et Python et intégration à une bibliothèque de traitement d'images
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/SkZNb5HgO)

# RORPO
* By Odyssee Merveille

## Mathematical morphology
The basic operators:
* Erosion
* Dilation
* Opening
* Closing

![](https://i.imgur.com/DVijXm7.png)

## How it works
* Relies on path operators

![](https://i.imgur.com/dP3IomE.png)

# C++ directional features
![](https://i.imgur.com/zqPCZX8.png)

RORPO: recuperer des features directionnelles, objets tubulaires
Dans l'exemple: indiquer vecteur directionel

1. Pointwise Rank Filter
2. Find orientation of interest
3. Combine orientations

![](https://i.imgur.com/7WmNmHE.png)
Dans l'exemple: la separation qui minimise le mieux la formule est la bleue

## Implementation
Parametres optionel:
![](https://i.imgur.com/TY0pMNp.png)

Iterer pixels image:
![](https://i.imgur.com/MRxuc61.png)

Chercher la bonne separation des groupes:
![](https://i.imgur.com/gVeg2By.png)

Combiner orientations sur un meme vecteur:
![](https://i.imgur.com/tWHogvQ.png)

# PyRORPO 
## Python module
Librairie entierement en C++ pour Python
Methods:
* RORPO
* RORPO_multiscale
![](https://i.imgur.com/esyU3Bp.png)

Bindings libs:
* Ctypes
* CFFI
* Boost::Python

Why pybind11:
* Focus on C++
* Use of c++ to specify the module
* Simple to use

## Bindings
![](https://i.imgur.com/uOJPohD.png)
A droite: definir la methode de notre module python $\rightarrow$ mapping de notre fonction chapeau

![](https://i.imgur.com/Y0zXtIc.png)
`BINDING_OF_TYPE`: defini tous nos bindings a chaque ligne

## Documentation
The documentation on how to create shared library, import shared module in python, on each available function

# New options for C++ progran
* uint8: convert image in uint8
![](https://i.imgur.com/pWSpfHz.png)
* normalize: input mage normalized
![](https://i.imgur.com/F4hkd40.png)

# Tests
* pytest
* virtualenv integretaion machine

Tests:
* Float/double input image
* Input image containging negative values
* uint8 option
* windows option

# Isotropic images
Isotropy is uniformity in all orientations
Use of:
`itk::ResampleImageFilter<TInputImage, TOutputImage, TInterpolarPrecisionType, TTransformationPrecisionType>`
![](https://i.imgur.com/6hVZpBb.png)

![](https://i.imgur.com/RCkIXd7.png)

# Encountered difficulties
* Creation of a PIP package
    * Pas forcement de documentation: package en C++ pour python
    * Package pas installable et distribuables sur differentes plateformes
* Isotropic images

# Questions

## Guillaume Tochon
Package pip manquant mais hors ca est-ce que le produit est considere fini ?
> Pour les features implementees, le produit est termine, est fonctionel et fonctionne comme planifie au debut

Applications concretes de tout ca?
> Non, hors celle de Odyssee. Odyssee a fourni des images synthetiques pour tester le programme et verifier que les resultats marchaient.

Quels ont ete les cours suivis dans la majeur les plus utiles ?
> Le cours TK et morpho de maths

## Elody Puybareau
Question sur RORPO:
1. Vous avez montre l'exemple avec un nifty, marche que sur nifty ou d'autres types d'image?
> Ca marche sur d'autres type d'image, marche sur n'importe quel type d'image. Le "load to numpy" n'est qu'un exemple
2. Comment vous gerer la conversation en uint8? Par exemple les donnees medicales sont souvent en 16bits, regarde en details les histoire de dynamique ?
> Gerer automatiquement: lorsqu'on recoit des images de type uint16, directement gerer par RORPO

Comment a ete decoupe le travail en equipe ? Tous ensembles, separes les differentes taches, etc. ?
> Separer les differentes taches

Pression de faire des points avec Odyssee qui a permis d'avancer ou auto-motive ?
> Lorsqu'on a plusieurs projets en simultanes, oui les reunions avec Odyssee permette de progresser regulierement. Repartir bredouille d'une reunion permet de se motiver pour la fois d'apres.

## Eleves
Qu'est-ce qui a bloque le developpement du package pip?
> Que ce soit pas du full python, pas de facon propre de bind une librairie en C++

## Odyssee
Ressenti et travail fourni: projet long a demarrer au debut mais pas mal de background pour comprendre RORPO, beaucoup de code pas forcement hype propre a prendre en main et aussi beaucoup de projets en parallele.
Gael et Anna ont propose des solutions satisfaisantes pour le binding, Anna a meme trouve des bugs dans le code original.
Le binding en python est suffisant et librairie deja en cours d'utilisation et au final tres satisfaite du travail.
Travail pas tres axe recherche mais plus dev et amelioration.