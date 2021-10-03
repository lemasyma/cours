---
title:          "PFEE ForEvent"
date:           2021-02-04 14:00
categories:     [Image S8, PFEE]
tags:           [Image, S8, PFEE]
math: true
description: Optimisation et développement de filtres graphiques avancés pour des team building et animations.
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/r1oFydYgu)

Par Alexandre Girard - Nassim Habib-Allah - Xavier Fichter

# ForEvent
* Agence d'animation evenementielle implantee a Paris et Bordeaux

# Etat de l'art
* App Ipad pour creer sa propre BD photos
* Dev en Swift
* Quelques secondes de calcul par image

# Objectifs
* Ameliorer le temps de traitement des images
* Ajout de nouveaux filtres
* **Creer une verion PC, portable sur un serveur**

# Fonctionnement du projet/filtres
* On utilise C++/OpenGL: GLFW et glad
* Combinaison de Vertex/Fragment Shader
* Chaque filtre est rendu dans un `FrameBuffer`

# Filtre Manga/Couleur
![](https://i.imgur.com/5j3nTbE.png)

# Filte Comics
![](https://i.imgur.com/G82NdFC.png)

# Deployer sur un serveur
1. Deployer avec docker et Serveur-X
    * Utiliser nvidia-docker-runtime et xvfb
    * Contrainte de la versio d'OpenGL
2. Deployer sans docker et Serveur-X
    * Utiliser EGL au lieu de GLFW
    * OpenGL moderne dispo
    * Rendu Headless

# API Web
* Une interface simple pour upload une image vers le serveur et choisir le filtre a appliquer
* Permet de telecharger l'image filtree

# Resultats
![](https://i.imgur.com/1ovDh8s.png)

Benchmark:
![](https://i.imgur.com/CFRwkEW.png)

# Ameliorations
* Faire de GPGPU $\rightarrow$ Compute Shader ou CUDA
* Reunir plus de filtres dans un shader

# Conclusion
Projet interessant, nouvel aspect de OpenGL et rendu sur serveur
![](https://i.imgur.com/HW4EaCk.png)

# Questions
## Guillaume Tochon
Pourquoi parti sur l'aspect rendu que traitement ?
> Pas pret a composer des filtres, besoin de connaissances en Swift: "Ouh la c'est quoi cette chose"

## Elody Puybareau
Sur la version comics, outils deja pret ou polarisation maison ?
> Filtre deja disponible sur l'application, portage PC, quelques types a changer/opti mais sinon filtres deja existants

## Eleves
Satisfait du rendu ?
> Bien-sur c'est style

Combien de temps ?
> Avril/Mai en fonction de si un virus ne bloque pas l'economie mondiale jusqu'a Fevrier

## ForEvent
Question pour les profs: comment se passe l'attribution des projets ?
> Proposition des sujets, repartis par groupe (1 groupe = un sujet), beaucoup de bataille pour obtenir un sujet mais surtout les etudiants choississent

# Retour de ForEvent
Experience nouvelle et positive, communication a ameliorer mais reussi a remplir les objectifs surtout que ralenti aussi a cause du corona, explorations a essayer mais manque de connaissance de la part de l'entreprise (ex: filtre peinture impressioniste)