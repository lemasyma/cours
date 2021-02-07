---
title:          "PFEE GE Healthcare 2"
date:           2021-02-04 16:15
categories:     [Image S8, PFEE]
tags:           [Image, S8, PFEE]
description: Synthèse et recalage par deep learning d’images radiographiques de l’abdomen et du thorax.
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/ByQTRFKg_)

# Probleme
* La fluoroscopie ne montre pas toutes les informations
* Injection cause des contrastes

# Solutions
Scanner preoperatoire 2-3 mois en amont

## Pendant l'operation
Fusion manuelle des 2 modalites
![](https://i.imgur.com/ppzMEj1.png)

## En resume
* Premiere donnee: image 2D (fluoroscopie)
* Seconde donnee: volume 3D (scanner CT)

# But du projet 
Automatisation de ce processus

## But de l'agent
![](https://i.imgur.com/WgbpGSh.png)

# Generation de donnees
## Recherches de donnees publiques
Fichiers .DICOM
* Ensemble de coupes d'un patient donne

## Generation de donnees
Pour un scanner donne:
* Reconstruction volume 3D
* Generation de projection

Pour une projection:
* Generation de *patches*

Donnees 2D uniquement
Notre projet: recalage 2D/2D afin de se concentrer sur la mise en place d'une architecture globales

# Apprentissage par renforcement
* Trouver la meilleure sequence d'actions permettant d'aligner 2 images
* Un agent artificiel apprend la meilleure *strategie*

## Q-learning
* But de l'agent de trouver la *policy*
* La notion de *q-value* renvoie a la recompense obtenue sur le long terme

## Apprentissage par renforcement supervise
q-values deja calculees avant l'apprentissage
* On va faire une regressions entre q-value et output du reseau
* Permet d'avoir une convergence plus stable

## Role du reseau de neurones
* Determiner action optimale pour chaque etat
* Estimer les q-values pour chaque paire etat/action
![](https://i.imgur.com/zmoF2MA.png)
* Le reseau prend un etat en entree et retourne les q-vqlues pour chaque action

## Pre-traitement
* Patch normalise entre 0 et 1

![](https://i.imgur.com/WtRNDm5.png)

## Phase d'entrainement
![](https://i.imgur.com/Bq8dOV8.png)

## Obtention des images a chaque etape d'inference
* Choisi action parmi 6 pour q-value maximale
* Applique l'action

# Resultats
![](https://i.imgur.com/NZ0WcGG.png)

![](https://i.imgur.com/KB5VlPV.png)

## Reduction de la dimension du probleme
![](https://i.imgur.com/2xLtkkE.png)

# Conclusion
Ce que le projet nous a apporte
* Montee en competences
* Recalage d'image
* Imagerie medicale

Ce que le projet a apporte a GE
* Meilleure connaissance des bases de donees publiques
* Premiere approche de l'apprentissage par renforcement

# Questions
## Guillaume Tochon
C'est quoi `epsilon policy` ?
> Fonction qui permet de diriger exploration et exploitation

## Elodie Puybareau
Le temps de traitement sur une image ?
> Relativement instantanee

# Retours GE Healthcare
Retour globalement positif, resultat fonctionnel