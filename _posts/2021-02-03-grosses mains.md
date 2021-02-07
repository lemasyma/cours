---
title:          "Le Projet Grosses Mains"
date:           2021-02-03 10:00
categories:     [Image S8, RVAU]
tags:           [Image, S8, RVAU]
description: Projet de Realite Virtuelle et AUgmentee
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/ByzSVy_gd)

Un jeu triple A

# Concept
* Coop VR/PC
* Platformer
* Object displacement
* Mutliple scales

# VR Player
* Capacity to grab objects in environment
* Creation of passage

# Interactable
* Can grab a plank

# Keyboard/mouse player
* Input System Manager
* Cimemachine Camera
    * Handles Mouse input
* Define movement direction according to the camera vectors
* Handles rotation and animations
* Add jump and gravity

# Network handling
* Photon
    * Photon view: dire au perso ou il est pour le netowrk
    * Character follow: permet au personnage network de suivre le perso client
* Verifier que perso network bien instancie

# Level Design
* The floor is lava
* Movable objects to help the player go through the level

# Question
Pourquoi photon pour la partie reseau ?
> Le plus simple a utiliser, a la base serveur dedier mais Photon bien plus simple et moins de temps

Quel casque ?
> Occulus quest, dans la video 2 joueurs sur Quests car autant de joueurs VR + PC possible

Comment la cooperation se fait entre 2 joueurs en VR ?
> Ne peuvent pas interagir, uniquement pour la video demo

Pour les animations du perso PC, comment ?
> Tout ete fourni avec le personnage (assets)