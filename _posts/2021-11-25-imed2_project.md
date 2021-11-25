---
title:          "IMED2: Project"
date:           2021-11-25 11:00
categories:     [Image S9, IMED2]
tags:           [Image, S9, IMED2]
math: true
---

Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/B1xHaAn_F)

# Part 1
## Retinal fundus image segmentation

![](https://i.imgur.com/jYTbkNu.png)

## Iterative Closest Point - ICP

![](https://i.imgur.com/6IVRysx.png)

Quand on itere, on reste bloques sur des minimums local

En remplacant points par courbes:

![](https://i.imgur.com/PScgsbe.png)

On construit un ensemble de courbes problables et on associe ces courbes probables

![](https://i.imgur.com/d6SNtCv.png)

Ca marche pas car on recale un objet 3D sur un objet 2D

![](https://i.imgur.com/wpcnOWY.png)

# Part 2

## Iterative Closest Point Registration

[Vedo](https://github.com/marcomusy/vedo)
[ICP](https://github.com/ClayFlanningan/icp)

![](https://i.imgur.com/Ge2l95H.png)

![](https://i.imgur.com/Jrn80tD.png)

# Project part 3

## Mosaicking application

[CVRL](https://projects.ics.forth.gr/cvrl/fire/)

![](https://i.imgur.com/aCe6CeB.png)

<div class="alert alert-danger" role="alert" markdown="1">
A la fin, **ca ne marchera pas**
</div>

Mais c'est pas grave, on aura essaye :)

## Pathology evolution

[CVRL](https://projects.ics.forth.gr/cvrl/fire/)

![](https://i.imgur.com/0rISO0w.png)

![](https://i.imgur.com/CvdxnQk.png)

<div class="alert alert-info" role="alert" markdown="1">
On fait un suivi temporel d'une pathologie
</div>
