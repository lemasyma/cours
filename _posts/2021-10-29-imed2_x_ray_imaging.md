---
title:          "IMED2: X-Ray Imaging"
date:           2021-10-29 09:00
categories:     [Image S9, IMED2]
tags:           [Image, S9, IMED2]
math: true
---

Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/BJZYe7YIt)

# Principe physiques de la radiologie numerique

> Rappels

- kVp
- mA
- Temps d'exposition

![](https://i.imgur.com/Ruwqtce.png)

Adaptation du faisceau:
- Filtration uniforme (Cu)
- Lames de collimation

![](https://i.imgur.com/98yidG6.png)

Interactions avec la matiere:
- Diffusion elastique
- Diffusion inelastique
- Effet photoelectrique

# Les chaines images selon les modalites

> Quelques exemples

![](https://i.imgur.com/zEp6reJ.png)

![](https://i.imgur.com/xTd0yJb.png)

![](https://i.imgur.com/AlzLNSn.png)

![](https://i.imgur.com/CZU1RHq.png)

# Qu'est-ce qu'une "bonne" image ?

## Tout depend de la tache

On a 3 choses tres importantes:
- bruit ![](https://i.imgur.com/7lkD2Xr.png)
- nettete
    - Resolution spatiale
    - ![](https://i.imgur.com/2QiUPkx.png)
- contraste 
    - Contraste-to-noise ratio ![](https://i.imgur.com/zuRKj3f.png)

## Bonne image a rayons X ?

> Ca depend encore de la tache

<div class="alert alert-info" role="alert" markdown="1">
Differentiation de matieres

![](https://i.imgur.com/LtIeTG1.png)

</div>

![](https://i.imgur.com/04O1QIc.png)

<div class="alert alert-success" role="alert" markdown="1">
Pas d'artefacts (e.g., halos pres des contours, lignes, colonnes, mouvement, flou...)
</div>

> Si on a un halo autout d'un implant, on a un peu de jeu autour
> Il faut certainement rajouter quelque chose pour reparer ca
> Ca peut etre tres dangereux (patient fragile, agee, etc.)

# Zoom sur la chaine de traitement numerique

> L'image qu'on voit est loin d'etre l'image qu'on mesure

![](https://i.imgur.com/Sxvec36.png)

Sur la premiere image on a une ligne au centre

![](https://i.imgur.com/036ogcj.png)

# Qualite Image et tache clinique

- Qui est mon patient ?
    - Un gamin
    - Un adulte
    - Une personne agee
- Pour quel acte vient-il ?
    - Un suivi de scoliose / un bilan general de posture
    - Un depistage de cancer du sein
    - Une ablation de tumeur hepatique

<div class="alert alert-warning" role="alert" markdown="1">
Selon les cas, le besoin en qualite image et la *tolerance en terme d'irradtion* serra differente
</div>

- Un principe historique: **ALARA** (*As Low As Reasonnably Achievable*)
- Un acronyme qui a tendance a etre remplace par **ALADA** (*As Low As Diagnostically Achievable*)

Du coup il y a des guidelines:

![](https://i.imgur.com/BwtK7to.png)

## Controle automatique de l'exposition

> AEC: la technologie de tous les appareils modernes d'imagerie RX

<div class="alert alert-info" role="alert" markdown="1">
"*Automatic Exposure Control (AEC) is an X-ray exposure termination device*"
- Wikipedia

![](https://i.imgur.com/DHZ3bf0.png)

</div>

![](https://i.imgur.com/5QUL3yJ.png)

![](https://i.imgur.com/bzirPQ5.png)

## Radiographie conventionnelle

> Une technique aussi vieille que les rayons X

![](https://i.imgur.com/ldn4ylf.png)

On faisait du *stitching*, mais on avait des problemes de deformation geometriques

## EOS/EOSedge et l'imagerie orthopedique 

![](https://i.imgur.com/EoO52xY.png)

[Video de presentation](https://youtu.be/B1DojRTcTQ8)

## Pathologies en orthopedie

![](https://i.imgur.com/bZFI23o.jpg)

- Diagnostic, correction & suivi de scolioses
    - Chirurgie: tiges et vis
- Implants (hanches, genou)
- Osteoporose
- Polyarthrite

