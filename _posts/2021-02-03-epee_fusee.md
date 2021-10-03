---
title:          "Epee et fusee"
date:           2021-02-03 12:15
categories:     [Image S8, RVAU]
tags:           [Image, S8, RVAU]
math: true
description: Projet de Realite Virtuelle et AUgmentee
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/rJQArWOl_)

> Qu'est-ce qui se passe si on fusionne une epee et une fusee ?

Jeu d'epee ou les joueurs peuvent se deplacer

# Le reseau
* Defini la structure du code
* Photon Unity Network
* Synchronisation du minimum
    * Pas ouf de synchoniser tout
    * Synchro les animations

# Personnage 3D
* Modele 3D et animations
    * Si le joueur bouge sa main dans le jeu, tout le monde doit le voir
* Hit Box par membre du corps (tete, torse...)
* Metaphore du corps du joueur

# Modele camera
* Retranscrire les deplacements reels du joueur dans le jeu
* Le personnage est la camera
* Le corps du personnage suit la camera

# Les fusees
* Une fusee par main (activable par le joueur)
* Changement de velocite du personnage selon orientation de la main
* Deplacement tridimensionnel
* Permet un deplacement assez fun
* Ne cause pas la nausee

# Les armes
* Abstraction: support de plusieurs armes (et bouclier)
* Detection des collisions avec les personnages
* Systeme d'energe: solution pour gerer les collisions entre les armes

# Changement d'arme
* Propre a chaque main
* Changement enclenche par: main derriere la nuque
* Calcul par rapport a la position du joueur

# Environnement 3D
* Objectif: vertigineux, theme urbain
* Probleme: souvent trop lourd pour le Quest
* Solution: texture basse qualite

# Questions
Le mouvement des personnages synchro sur le reseau ?
> Ce qu'on synchro c'est la target d'origine et sa rotation, on synch la tranlsation

Degats de chutes ?
> Non pas implem

Faire des deplacements dans une zone de non gravite ?
> Manque l'aspect de retomber facilement

Quelles interactions PC ?
> Pas d'interaction PC, la vue sert de debuggueur