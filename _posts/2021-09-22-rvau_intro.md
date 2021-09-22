---
title:          "RVAU: Introduction a la Realite Virtuelle"
date:           2021-09-22 10:00
categories:     [Image S9, RVAU]
tags:           [Image, S9, RVAU]
description: Introduction a la Realite Virtuelle
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/rknFhLOQF)

# Realite virtuelle

*C'est quoi ?*

<div class="alert alert-info" role="alert" markdown="1">
C'est toutes les technologies utilisees pour immerser un humain dans un monde virtuel
</div>
> Contrairement au cinema, on est acteur

![](https://i.imgur.com/XbrCkfY.png)

Terme introduit par Jaron Lanier en 1988
> Maybe we should go over what Virtual Reality is. We are speaking about a technology that uses computerized clothing to synthesize shared reality.

## Une definition

> *"La realite virtuelle est un domaine scientifique et technique, exploitant l'informatique et des interfaces comportementales en vue de simuler dans un monde virtuel le comportement d'entite 3D, qui sont en interaction en temps reel entre elles et avec un ou des utilisateurs en immersion pseudo-naturelle par l'intermediaire de canaux sensori-moteurs"*
> P. Fuchs, Le traite de la realite virtuelle vol. 1

<div class="alert alert-warning" role="alert" markdown="1">
C'est un univers 100% virtuel
</div>

![](https://i.imgur.com/4eDHmKp.jpg)

## Realite augmentee

Il faut la distinguer par rapport a la VR

<div class="alert alert-info" role="alert" markdown="1">
Le but est d'incruster sur le monde reel des elements du monde virtuel
</div>

## Realite mixte

Un continuu, d'experiences sensorielles

![](https://i.imgur.com/3IeE6Bh.png)

![](https://i.imgur.com/3zDqVmy.png)

# Historique

- Stereoscope ![](https://i.imgur.com/qzMou02.png)
    - Premiere forme de la VR d'aujourd'hui
    - C'etait pour les images fixes
- Sensorama (1962) ![](https://i.imgur.com/qg0wn0a.png)
- The ultimate display (1965)
    - Premiere reference a la VR
    - Pas une invention, une vision du futur de l'informatique
- The sword of Damocles (1968) ![](https://i.imgur.com/HMEGrao.png)
    - Le premier casque VR
    - Tellement lourd qu'il devait etre accroche au plafond
- GROPE Haptic display (1967-1988) ![](https://i.imgur.com/DZNFmOe.jpg)
    - Simule le toucher
- Dataglove ![](https://i.imgur.com/yw2V10i.jpg)
- Vived ![](https://i.imgur.com/xxrVNyL.jpg)
    - Combinait l'affichage avec des gants
    - Avec commandes vocales
- EyePhone (1989) ![](https://i.imgur.com/pLXfoQJ.jpg)
    - Premier iPhone
    - Coutait 10k\$
- View (1990) ![](https://i.imgur.com/3DqJJLw.png)
- Cave (1992)
    - Dispositif different
    - Immersion avec des projecteurs
- SPIDAR (1992) ![](https://i.imgur.com/Q6jy2iD.png)
    - Genere un retour de force
    - Genre bague reliee a un fil
- Flock of Birds (1992) ![](https://i.imgur.com/oQICeCb.png)
- Casque pour le jeu video (90's) ![](https://i.imgur.com/JD3UOKI.png)
    - Technologie encore balbutiante
- Annees 2000-2010 ![](https://i.imgur.com/OZKMpzb.jpg)
    - Casque de l'ordre de 20k\$
    - Plus grosse resolution: 6 millions de pixels par oeil
    - Par comparaison: 1er occulus, 500k pixels par oeil
    - Cave de Renault
        - 5 faces
        - $2\times4k$ par face
        - Plusieurs millions d'euros
- Haption Virtuose 6D (2001)
- Depuis 2010 ![](https://i.imgur.com/IfUyb4c.png)
- Leap motion (2013) ![](https://i.imgur.com/D0JAOxq.png)

# Caracteristiques de RV

## Immersion

<div class="alert alert-info" role="alert" markdown="1">
Mesure selon laquelle le peripherique de RV est capable de remplacer les stimulations sensorielles du monde reel par celui du monde virtuel

![](https://i.imgur.com/D3oliA7.png)

</div>
> Pour chacun de nos sens, la simulation est *panoramique*

<div class="alert alert-warning" role="alert" markdown="1">
Un appareil qui peut en simuler un autre est plus immersif que ce dernier
</div>
> Un casque peut simuler un ecran de PC, il est plus immersif

## Presence

<div class="alert alert-info" role="alert" markdown="1">
Le sentiment d'etre present dans l'environnement virtuel

![](https://i.imgur.com/1RyhI5H.png)

</div>
> Sur l'image a droite, pour passer de droite a gauche, tout le monde a fait le tour du trou au lieu de passer par-dessus (alors que le sol est en-dessous, il n'allait pas tomber)

# Affichage pour la realite virtuelle

## Peripherique d'affichage

![](https://i.imgur.com/3hrBgtL.jpg)
- En haut a droite: workbench
    - Ecran 3D avec dispositif d'interactions
    - Possibilite d'interagir avec une maquette
    - Donne une zone de travail

## Rendu 3D

- Model au monde: ![](https://i.imgur.com/iO0RJqf.png)
- Projection: ![](https://i.imgur.com/S3hEmX6.png)
- Pyramide de vue: ![](https://i.imgur.com/xrDzPRG.png)
    - Near clipping: distance minimale pour voir les objets
    - Far clipping: distance max
- Z-Buffer ![](https://i.imgur.com/uOmJjsk.png)
- Shaders ![](https://i.imgur.com/K7Pb1gn.png)

## Stereoscopie

![](https://i.imgur.com/1czPwn3.png)
> Bawi on veut de la 3D

<div class="alert alert-warning" role="alert" markdown="1">
On a dans notre monde virtuel 2 cameras
</div>

Plusieurs facons de le faire:
- Anaglyphe ![](https://i.imgur.com/4oFCaCX.png)
    - Filtre de couleurs
    - Une couleur par oeil
    - pb: rendu des couleurs fausse
    - Ce n'est pas du tout utilise pour la RV
- Stereoscopie active ![](https://i.imgur.com/9UO6IFn.png)
    - Besoin d'electricite
    - Va occulter chaque verre l'un apres l'autre en permanence
    - Pour du 60 fps, on va faire du 120 fps et afficher une fois pour l'oeil droit et une fois pour l'oeil gauche
- Seteroscopie passive ![](https://i.imgur.com/PybgeoZ.png)
    - Lunettes beaucoup plus legeres
    - Filtres polarisants
    - 2 projecteurs differents
    - Certains rayons pour l'oeil gauche, d'autre pour l'oeil droit

Ecrans auto-stereoscopiques
![](https://i.imgur.com/BOzajBz.png)

![](https://i.imgur.com/op0nWun.png)

<div class="alert alert-info" role="alert" markdown="1">
Ce sont des ecrans qui n'ont pas besoin de lunettes pour etre vus en 3D
</div>

Inconvenients: 
- ca reduit la resolution de l'ecran par 2
- Il suffit de se deplacer un peu pour que la 3D saute

<div class="alert alert-success" role="alert" markdown="1">
C'est utilise pour la 3DS :0
</div>

### Dans un casque de RV

![](https://i.imgur.com/yt3fEZ9.png)
- On applique une correction avec les lentilles pour l'effet vignette

## Calibration

![](https://i.imgur.com/eUkDRAl.png)
- Probleme pour les caves
- Les images doivent etre coherentes et geometriquement justes

# Interactions pour la RV

## Peripheriques d'interaction

![](https://i.imgur.com/ZHPdouO.png)

## Metaphores d'interaction

<div class="alert alert-info" role="alert" markdown="1">
**Metaphore**
> *Au lieu d'exploiter un comportement sensori-moteur et acquis de la personne, nous lui proposons, visuellement en general, une TODO*
</div>

*Manipuler un objet ?*
> Utiliser une manette, un pointeur, etc.

<div class="alert alert-success" role="alert" markdown="1">
Utiliser une *main virtuelle*

![](https://i.imgur.com/CtA13M9.gif)

![](https://i.imgur.com/In2MscK.gif)

</div>

### Co-localisation

<div class="alert alert-info" role="alert" markdown="1">
Que la main virtuelle apparaisse a l'endroit de notre main reelle

![](https://i.imgur.com/lwWO4hd.png)

</div>

![](https://i.imgur.com/WKnCkGH.png)

### Gestes

![](https://i.imgur.comnJUIFv.png)

### Gizmos

<div class="alert alert-info" role="alert" markdown="1">
Des "poignees" utilisees pour deplacer les objets dans le monde virtuel

![](https://i.imgur.com/VgbtudY.png)

</div>

### Rayon

<div class="alert alert-info" role="alert" markdown="1">
Comme un rayon laser, on vise un objet pour interagir avec

![](https://i.imgur.com/Xh8kiJl.png)

> Portal-gun style
</div>

### Tactile

![](https://i.imgur.com/mt9eTq7.png)

### Controles de l'application

![](https://i.imgur.com/zdv5jJV.gif)

![](https://i.imgur.com/49Bm4aR.gif)

## Metaphores de navigation

*Comment se deplacer dans l'environnement virtuel ?*
> On pointe et on se teleporte
> Un utilise un joystick
> Un tapis roulant dans toutes les directions

### Room scale

![](https://i.imgur.com/jR4JW9b.png)
- Beaucoup utilise par les casques
- Utilise par HTC vive

### Deplacement continu

![](https://i.imgur.com/GFVEz68.png)

### Teleportation libre

![](https://i.imgur.com/ksOlgUO.png)

### Teleportation point a point

![](https://i.imgur.com/ZtYYYbw.jpg)

### Materiel dedie

![](https://i.imgur.com/CmZOy3E.png)

### Monde en miniature

![](https://i.imgur.com/8r2wtqj.png)

### Redirected walking

On tourne legerement l'environnement virtuel, pour faire un mouvement courbe IRL en allant tout droit IVL

![](https://i.imgur.com/rHb7JJY.png)

![](https://i.imgur.com/JylEZyb.png)

# Realite augmentee

Le but est d'incruster des elements virtuel au monde reel.

*Mais comment ?*

- Vue indirecte (*video see-through*) ![](https://i.imgur.com/PeuTtDS.png)
    - Aka pokemon go
- Vue indirecte (optical see-through) ![](https://i.imgur.com/y8oRHWY.png) ![](https://i.imgur.com/3ZUZYSC.png)
    - Donne l'impression que l'objet virtuel est reel
- Projection dans l'environnement ![](https://i.imgur.com/LVdCfhb.png) 
    - Dans le cas d'une voiture ![](https://i.imgur.com/ZjItvnV.png)

## Nouveaux peripheriques de realite augmentee

![](https://i.imgur.com/ZmEV2vL.jpg)
- Hololens

<div class="alert alert-success" role="alert" markdown="1">
Ces peripheriques peuvent embarquer differents capteurs
</div>

![](https://i.imgur.com/dsEmIUw.gif)
