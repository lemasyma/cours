---
title:          "Obstacles"
date:           2021-02-03 11:15
categories:     [Image S8, RVAU]
tags:           [Image, S8, RVAU]
description: Projet de Realite Virtuelle et AUgmentee
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/r1omYgdxu)

Par Amelie, Alexandre, Bruno

# Sujet: un jeu collaboratif
2 joueurs: un avec un casque VR, l'autre PC
But:
* Le joueur VR doit finir le niveau
* Le joueur PC doit l'en empecher, en utilisant la map

# Map
3 zones
* Attente (spawn): choix des armes
* Combat
* Fin

# Joueur PC
* Empecher le joeur VR de finir le niveau
* Faisant spawn des ennemis sur la map
* Accelerer la vitesse des plateformes

# Joueur VR
* Deplacement avec Joystick
* Rotation en bougeant la tete
* Se defendre avec une arme

# Combat
* Les ennemis peuvent lancer des boules de feu
* Le joueur VR perd des PV s'il se fait toucher ou touche une ennemi
* Tirer sur une boule de feu permet de la detruire, meme avec un coup de sabre laser

# Fin de la partie
* Le joueur VR a passe la porte de fin de niveau $\rightarrow$ joueur VR gagne
* Le temps imparti $\rightarrow$ joueur PC gagne
* Le joueur VR tombe $\rightarrow$ joueur PC gagne

# Problemes rencontres
* Le reseau
    * Mirror
    * Le spawn des joueurs sur la scene et leurs gameobjects
    * La synchro (objets, ennemis, etc.)

# Questions
Pertinant que les ennemis et boules de feus synchro ?
> Sans la synchro, le joueur PC ne verrait pas la vraie scene

Boule de feu instantiee sur le network ou chez le client ?
> Avec Photon: utilise photon view, de meme que les ennemis

Comment sont gerer les deplacement ?
> OVR Controller

Interaction entre les 2 joueurs: comment le joueur PC voit le joueur VR ?
> Le joueur PC a une camera fixe et le joueur VR est rpz par un cube sur son ecran.