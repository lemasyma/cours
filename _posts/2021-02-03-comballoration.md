---
title:          "Comballoration"
date:           2021-02-03 9:00
categories:     [Image S8, RVAU]
tags:           [Image, S8, RVAU]
description: Projet de Realite Virtuelle et AUgmentee
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/SJj5uRDxu)

Video de demonstration: duel 1v1 en VR avec des armes (epee, pistolet, assiettes, etc.)
> Le but est tout simple: c'est de le tuer

# Contexte
* Projet de Realite Virtuelle et AUgmentee
* Necessite d'avoir de la **collaboration**, aka pas de solo
* Dernier projet a Epita

# Sujet choisi
* Jeu de combat
* 1v1 Gare du Nord
* Collaboration

# Composants de base
* Le paquet OVR
    * Gestion de base du casque VR
    * Gestion de base des manettes Occulus
* Le paquet Mirror
    * Gestion de reseau
    * Copie de Unet, API reseau de Unity

# Fonctionnement
* Pour les armes:
    * Reprise du fonctionnement du TP
    * INtroduction de *Commands*
* Pour la camera VR:
    * Reprise du TP
    * Ajout d'un script pour l'initialisation du multi

# Boucles de jeu principales
* Pas de PVs
* Emphase sur la vitesse pour attraper l'epee ou le pistolet
* Des qu'un joueur se fait toucher: MORT

# Difficultes
* La camera
    * Reprendre le TP correctement
    * Avoir la camera au bon endroit
    * Synchro de la camera et bugs mix VR/Network
* Le reseau
    * Synchro des positions
    * Gestions d'autorite avec Mirror

# Tentatives ratees
* Robot Kyle avec des animations
    * Bug de reseau, etc...
* VR Rig
    * Perso 3D
* Notre propre mesh de personnage (blender et unity voulaient pas)
* Ajout de joueurs (sur tel par exemple)

# Outils
* Polybrush
* LowPOly

# Conclusion
* Projet ultra fun
* Necessite de recruter des cobayes pour les tests (Nausee, etc.)
* Bonne decouverte de Unity (admissions paralleles)

> Press F to pay respect at Robot Kyle

# Questions
Projets de combien de temps ?
> Fait la semaine derriere

Immobile ou on peut se deplacer ?
> On peut se deplacer mais certainement mort instant

Fonctionne sur casque autre que Occulus ?
> Utilisation de OVR, jamais pose la question vu que le but est de le faire en Quest

Creation des contenus 3D?
> Recuperation d'assets + assemblage des scenes a la main.

Organisation du travail ?
> Occulus maison, 1 s'occupe des scenes et les 2 autres le reste, beaucoup de pair programming