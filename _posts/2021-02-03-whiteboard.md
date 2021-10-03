---
title:          "Whiteboard in VR"
date:           2021-02-03 10:15
categories:     [Image S8, RVAU]
tags:           [Image, S8, RVAU]
math: true
description: Projet de Realite Virtuelle et AUgmentee
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/ry73wJ_lu)

> On va vous montrer un projet tout pourri!

Projet: whiteboard en VR

# Project goals
* Write on a whiteboard
* Implement mutliple tools
* Interact with multpile people with the whiteboard

# Features implemented
* Write on the whiteboard
    * Create a pen
    * Grab a pen
    * Detect collision between pen and whiteboard

# Problems encountered
* Difficulte avec textures
    * Detecte collision mais pas de texture
* Pas pu rajouter le multi
* Difficult test environment
    * Difficulty on Linux
    * Moving, could only work in the kitchen but had an occulus
    * 50cm space to test a VR game

> Pourquoi je suis penche ? Le cable etait pas assez long

> C'est parce que je sais pas dessiner que c'est moche - en dessinant un mouton

# Question
Est-ce qu'il y une sensation en ecrivant ?
> Non car la manette vibre en permanence

En terme de mutliplayer ?
> Utiliser Photon

Comment applique la texture ?
> Repere la collision et applique la texture en X,Y