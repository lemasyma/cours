---
title:          "PFEE Vesselness Covid"
date:           2021-02-01 16:00
categories:     [Image S8, PFEE]
tags:           [Image, S8, PFEE]
math: true
description:  Segmentation de vaisseaux sanguins pour diagnostic de coronavirus.
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/H1t1q9Beu)

Sous la supervision d'Odyssee Merveille
Par Camille, Rene-Louis, Salome et Sophie

<div class="alert alert-success" role="alert">
Analyse des consequences du Covid dans les vaisseaux sanguins.
</div>

# Vesselness
Algo se basant sur les structures tubulaires des vaisseaux sanguins
![](https://i.imgur.com/ftoegvy.png)

# RORPO
* Tool using mathetical morpholy to segment vessels
* characterizing the curvilinear structures
* detecting these strcutures by countin th number of high responses of an oriented filter, the path operators

![](https://i.imgur.com/f7ACBrt.png)
Une reponse indique le rayon et l'autre le chemin du vaisceau

# But et problematique du PFEE
* Peut-on utiliser RORPO pour analyser les differences entre patient sain et pattient atteint ?
* Ces differences nous permettent-elles de determiner l'avancement de la maladie ?
![](https://i.imgur.com/7m5ekej.png)

# La pipeline
* Segmentation via RORPO
* Extraction de donnees/metriques
* Visualisation des metriques
* Analyse des resultats

# Timeline du projet
![](https://i.imgur.com/KWl6XtW.png)

# Prise en main de nouveaux outils
* Slicer: tres utilise dans l'imagerie medicale
![](https://i.imgur.com/uPVOca3.png)
* HPC avec qsub

# Metriques
1. Valider les hypotheses: dilatation du reseaux vasculaire + lesions
2. Certaines metriques moins pertinentes que d'autres mais sont garder car on connait mal cette maladie

Segmentation des vaisseaux:
![](https://i.imgur.com/NKCPqqi.png)

## Metriques quantitatives
* Nombre de composantes connexes
* Nombre de Voxels labellises

## Des donnees par label
Metriques par label, cad par composante connexe
![](https://i.imgur.com/T9WzDzf.png)
Pas eu le temps de recuperer un outils

## Un maximum de minimum
On travail sur les rayons des composantes connexe

Par element connexe, on calcul le rayon minimum et on en retire:
* le min des min
* la moyenne des min
* le maximum des min
* un histogramme des min

## Un maximum de maximum
Par element connexe, on calcul le rayon minimum et on en retire:
* le min des max
* la moyenne des max
* le maximum des max
* un histogramme des max

## La moyenne, une donnee controversee
* le min des moyennes
* la moyenne des moyennes
* le maximum des moyennes

* Manque de sens theorique si mauvaise segmentation. Mais cette perte de sens ne serait pas exploitable ?
* Devrion nous pas nous tourner vers une moyenne pondere par la taille des vaisseaux ?

# Des metriques pour le futur
* des moyennes ponderees
* Volume du reseau vasculaire relativement au volume des poumons
* Volune des composantes connexes
* Remplacer les metriques par label par des metriques par embranchement grace a un algorithme de transformation en graphe

# Presentation du Dataset
* Donnees confidientielles
* Patients + ou - atteints

![](https://i.imgur.com/pwBpebF.png)
Nombre de composantes connexe augmente avec la severite du 

![](https://i.imgur.com/vosFTo9.png)
Uniforme chez les patients les plus atteints, mais besoin de plus de donnees pour en tirer une conclusion

## Rayon moyen
![](https://i.imgur.com/l6K8Hlh.png)
Extremum toujours patient severement atteint

## Recap
![](https://i.imgur.com/BWFDL5G.png)
Augmentation du nombre de voxel pour une taille de poumon qui n'augmente pas chez les patients atteints.

# Conclusion a partir des resultats
* Les metriques sont a adpate
* Pas de resultats concluant

# Pour la suite
* Ajouter de nouvelles metriques
* Plus grand dataset

# Questions
## Elody Puybareau
RORPO ne fait directement de segmentation: quelle est la brique rajoutee pour la segmentation ?
> Commencer par utiliser RORPO, stagiaire de Odyssee a cree la brique en plus qui a ete reprise pour ce PFEE

Utilisation des output du stagiaire ?
> Faire une pipeline qui prend tout en compte mais algorithme lourd donc division des taches

<div class="alert alert-danger" role="alert" markdown="1">
Utilistion de Matplotlib: attention car segmentation binaire mais 3 couleurs a cause de Matplotlib qui en melange pour les objets fins $$\rightarrow$$ ne jamais faire confiance a Matplotlib et son interpolation
</div>
## Guillaume Tochon
Base de donnees restreinte, dur d'en tirer des estimateurs fiable et representatif: pertinent de montrer des histogramme ? Coefficient de correlation plus pertinents ?
> Outils pour la posterite car le projet va etre repris, pas vraiment pense a un autre indicateur, but de faire l'analyse de donnees que d'en tirer des conclusions

Vous etes satisfait du travail fourni ?
> Bien aime avoir plus de temps pour travailler, dommage de pas avoir plus de temps pour PFEE, assez content du projet. A la fin du projet proche d'avoir une demarche scientifique complet, manque de temps. Frustration a cause de blocages sur sujets techniques.

Quels sont les cours qui ont ete le plus utile?
> IMED, IMED2 utile mais arrive un peu tard $\rightarrow$ PFEE utile pour IMED2

Repartition du travail?
> Pair programming, rotations 2 par 2

## Question etudiants
Tres peu de resultats: comment faire dans ce cas?
> On peut esperer en avoir plus, tres complique de recuperer des donnees surtout venant de l'hopital. On ne peut pas en tirer de conclusion.

Si vous aviez plus de donnees, comment aurai ete la fin du projet?
> Beaucoup de recul sur les patients, reflexion sur les resultats mais pas sure de comment conclure.

## Odyssee
Idee de ce PFEE: degrossir la pipeline globale, des etudiants qui travaille sur le pipeline complet, avoir des resultats concrets.
Une fois qu'on a le pipeline complet, on a une vision plus globale et on se rend compte de ce qui bloque, ils ont eu une tres bonne demarche sur le projet. Beaucoup de contraintes: l'accessibilite des donnees, acces moyens de calcul, etc.
Pipeline develope qui va etre tres util et repris par la suite.