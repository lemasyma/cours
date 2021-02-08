---
title:          "PFEE Mihaly"
date:           2021-02-04 14:45
categories:     [Image S8, PFEE]
tags:           [Image, S8, PFEE]
description: Génération automatique de maquettes 3D.
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/rkCGd_tld)

Prototypage d'un voxeliseur avec VTK

# Mihaly
* Startup d'impression 3D
* Nouvelle tech d'impression qui permet d'avoir du texturing et de la couleur
* Precision a l'echelle du micrometre
* Creation de l'application et du pipeline de traitements des objets a imprimer

<div class="alert alert-danger" role="alert" markdown="1">

**Problematique**:
* Impression 2.5D/3D dans un espace reduit
* Incapacite de creer des structures de soutien pour les objets flottants
* Opti de l'utilisation de materiaux colorises
* Gros volume de donnees (scan de plusieurs millions de vertices)

</div>

# Premieres approches
2 solutions possible:
1. Voxeliser
    * Decouper la partie externe du volume
    * Imprimer cette couche et reassembler le modele creux
2. Voxeliser
    * Decouper le volume en sous-volumes
    * Imprimer et reassembler


# Premieres iterations
* Utilisation de notre propre voxeliseur a partir de bibliotheques qu'on adapte

Grand tournant:
* Decouverte VTK

# Outils
* VTK
    * On a eu un cours
    * Visualisation et interactions integrees
    * Gestion 
* PyQT
    * Package python
    * Simplifie utilisation
* Blender
    * rapide mais mauvais sur les grosses donnees
    * Meshlab meilleur pour les gros sets

# Pipeline
* Entree: modele 3D (OBJ)

# Sorties attendues
Plein de formats differents : utilise OBJ et XML

# Resultat
![](https://i.imgur.com/M0aaItg.png)

# Problemes
VTK:
* Pas de doc
* Peu d'exemples et pas dans tous les langages
* Import `vtkmodules.all`

# Conclusion
* Gerer les fichiers de facon plus propre
* Trouver un moyen de generer un bitmap de maniere intelligente
* Automatiser de plus en plus la segmentation en sous-volumes
* Comprendre VTK

# Questions
## Guillaume Tochon
Comment a ete decoupe le travail ?
> Avant VTK, probleme de restreindre le sujet et VTK probleme de l'engine

Quels cours on ete utiles ?
> VTK tres utile meme si le cours est leger

Impression 2.5D ?
> Pour des scans de tableau, seulement une face compte

## Elody Puybareau
Est-ce que le projet vous a plu ?
> Oui meme si beaucoup de galeres, on pu voir l'imprimante 3D de $3m^2$

## Eleves
Pourquoi le screenshot du tableau ?
> Tableau: fichier de 1,6Go, seule solution de screen le tableau pour avoir la texture

# Retour de Mihaly
2-3 precisions sur la machine: 9 tetes avec des micro-buses qui lache du polymere sur $3m^2$ donc beaucoup de donnees, galere car confinement, retour tres positif