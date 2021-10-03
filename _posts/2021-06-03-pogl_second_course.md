---
title:          "POGL: Second class"
date:           2021-06-02 14:00
categories:     [Image S8, POGL]
tags:           [Image, POGL, S8]
math: true
description: Second class
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/rkKwUBU5O)

# Frame buffer object

![](https://i.imgur.com/HxYPpVQ.png)

![](https://i.imgur.com/LBfzkKw.png)

Quand on veut faire un rendu de l'offscreen rendering:

![](https://i.imgur.com/bIiEf61.png)

Calcul final au dernier moment
- Avantage: ce calcul n'est pas faut pour les points qui ne sont pas visibles

![](https://i.imgur.com/T7A53gr.png)
On va faire un rendu par buffer qui n'est pas visible
- un pour la couleur
- un pour la profondeur
- etc

En tout les points du quadrilateres du rendu on a les couleurs, normales, etc. et on peut en deduire les combinaisons pour le calcul effectif de l'illumination

<div class="alert alert-warning" role="alert" markdown="1">
Les combinaisons sont calculees une seule fois pour les points visibles sur un quadrilatere
</div>

> C'est utilise dans les jeux videos pour economiser du temps

## Off-screen rendering

On a besoin de pouvoir ecrire pour notre premier rendu similutanement la profondeur, couleur, etc. Pour cela on defini plusieurs variables out dans notre shader (Multi-Render target)

![](https://i.imgur.com/Bpzjhzd.png)

# Depth shadow maps

1. Avant de faire le rendu final, pour savoir quels sont les objets visibles, on fait le rendu depuis la source lumineuse ![](https://i.imgur.com/Dl5WDbI.png)
2. Faire le rendu en tenant compte de parties visibles ou pas depuis la source lumineuse

## Initialise *FBO*

![](https://i.imgur.com/FlT5R26.png)

## Rendu depuis la source lumineuse

![](https://i.imgur.com/euMih06.png)

## Rendu depuis la camera

![](https://i.imgur.com/G7hMbXF.png)

## Vertex shader

![](https://i.imgur.comR95DKT.png)

## Fragment shader

![](https://i.imgur.com/N0AlAv8.png)

## Resultats

![](https://i.imgur.com/O4PESdq.png)

On a le z-buffer depuis la source lumineuse

![](https://i.imgur.com/SJxyWHd.png)

> On s'attendait a un super resultat mais la partie pas a l'ombre a mal rendue

*Pourquoi ?*

Quand on fait le rendu, on discretise la scene: peut-etre que quand on verifie un pixel on est trop a droite ou trop a gauche, donc des pixels sont consideres a l'ombre alors qui ne le sont pas.

### Solution: ajout d'un biais

![](https://i.imgur.com/8qgYiRi.png)

<div class="alert alert-warning" role="alert" markdown="1">

Ce biais n'est pas facile a fixer car depend de notre scene, sa taille, la taille des objets, etc.

</div>

![](https://i.imgur.com/NSaX7iG.png)
> Le lapin profite du soleil avant d'avoir trop chaud

# Second depth shadow map

<div class="alert alert-info" role="alert" markdown="1">
Faire le rendu de la scene depuis la lumiere en regardant les faces arrieres des objets

![](https://i.imgur.com/d7vJmDW.png)

</div>
> On inverse le backface culling

<div class="alert alert-success" role="alert" markdown="1">
On n'a plus besoin du biais
</div>
> Le biais est toutefois plus facile a mettre

## Resultats

![](https://i.imgur.com/yUUn9xV.png)
> Il n'y a ni anti-aliasing, ni ombres douces

On n'a plus d'artefacts et on a un rendu temps reel qui fonctionne tres bien.

Pour aller plus loin:
- `sampler2DShadow`/`textureProj()`
- soft shadow map
- etc.

# Rendu final


## Frame buffer objects

On a plusieurs images, a t-1, t et t+1 (par exemple)

- Rendu d'une position dans une texture/un render buffer
- Accumulation dans une texutre (Type `float` sinon les valeurs sont *clampees*) ![](https://i.imgur.com/9hc3D0b.png)
- Copies dans l'image finale

Nous en train de courir vers le lapin, ca donne : ![](https://i.imgur.com/HzQ5d4w.png)
> Au lieu de faire un rendu, on en fait 3


## Post processing

On a un quadrilatere affiche dont on peut modifier la texture comme on souhaite.

### Rendu dans une texture
On deforme l'image

![](https://i.imgur.com/Bs9a2p2.png)
> Notre lapin a trouve des champignons, les a mange mais c'etait des champignons hallucinogenes

# OpenGL
## *Object Picking*

<div class="alert alert-info" role="alert" markdown="1">
L'idee: on va faire un rendu intermediaire off-screen, on associe a chaque objet un **identificateurs** dans les FBOs
</div>

## Le brouillard

![](https://i.imgur.com/i2YsFIQ.png)

<div class="alert alert-info" role="alert" markdown="1">
**Objectif**
Modifier la couleur en fonction de la distance
- choisir la fonction
</div>

![](https://i.imgur.com/ZHuXLq2.png)

![](https://i.imgur.com/93OJZuH.png)
> On retrouve notre lapin perdu dans le brouillard

## Moteur de particules
Systemes a base de particules
- Permet de modeliser des elements difficiles a modeliser avec des solides classiques ou des surfaces
    - feu
    - fumee
    - etc

Fonctionnement
- Caracteristiques
    - position
    - couleur
    - taille
    - forme
    - ...
- Lois
    - creation
    - destruction
- Regles (Evolution)
    - Modifications des caracteristiques

### Le feu
Utilisation de particules
- Creation
    - Plusieurs centaines
    - Apparaissent dans une zone precise
    - Avec une couleur proche du blanc
- Forme
    - Point
    - Sphere
- Evolution
    - Changement de couleur
    - Deplacement vers le haut avec perturbations
- Destruction
    - Atteint la couleur noir

Evolution: changement de couleur

![](https://i.imgur.com/5g4i3fg.png)

Resultat:
![](https://i.imgur.com/K6WZ6rZ.png)

Si on est flemmards:
- utilisation d'un billboard
- Affichage d'un feu en 2D

### Etinceles/feu d'artifice/explosion

Resultat:
![](https://i.imgur.com/bRfnlXj.png)

C'est les memes regles que pour le feu

![](https://i.imgur.com/gvotV1O.png)

![](https://i.imgur.com/BzTVnde.jpg)

On fait des bulles qui grossissent de plus en plus

![](https://i.imgur.com/oahoC2A.png)

## Billboard
Utilisation d'un Billboard

## Conclusion
Les effets intermediares qu'on peut faire pour le rendu final.