---
title:          "PFEE GE Healthcare: Deep Learning Inpainting"
date:           2021-02-04 15:30
categories:     [Image S8, PFEE]
tags:           [Image, S8, PFEE]
description: Complétion (inpainting) par deep learning dans les séquences d'images rayons X.
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/BksdVYKxO)

# How to get a volume ?
* Turn around the patient
* X ray acquisition in different angles

# Artifacts
Different types of artefact:
* Motion artifact
* Metal artifact
* Ring artifacts (detector)

# State of the art
* Where
    * Correction applied on volumes

# Inpainting
* Fill selected image area
* Requires having the mask of the missing parts

# Methods
## Interpolation 2D

Interpolation algorithm from skimage to create a basline:
* Nearest neighbor
* Linear

## U-NET 2D
![](https://i.imgur.com/TBfxv5y.png)

# Improvements ?
* Conv2D/3D do not consider the mask
* Losses (MSE/MAE) do not consider the mask

# Partial convolution
* Presented by Nvidia in 2018
* Mask area is much less visible and overall results are improves

## Keras ?
![](https://i.imgur.com/ounf4JU.png)

![](https://i.imgur.com/668yjMK.png)

# Loss improvement
* Using a train VGG
    * deep learning classifier
    * Layers used: 3rd, 6th and 10th

# Data
![](https://i.imgur.com/4e1iHYJ.png)

# Experiments
## Goal
* 2D
    * Perfomance machine learning
    * Added value

* 3D 
    * Adding temporal gives best results
    * Can we be more memory efficient using patches ?

# Evaluation method
* Quantitative evaluation
* MSE
* MAE
* SSIM
    * Structural similarity
* PSNR
    * Peak To Signal Noise Ratio
    * More quantitative than qualitative
* Quality eval
    * Eval by human eye

# Results
![](https://i.imgur.com/Ajf6f9u.png)

## Qualitative 2D
![](https://i.imgur.com/mvqmHVf.png)
![](https://i.imgur.com/JxxAUOR.png)

### Ribs reconstruction
![](https://i.imgur.com/5fbsShk.png)

## Qualitative 2D+T
![](https://i.imgur.com/N21dNdF.png)

## Analysis
* Machine learning can be used for this task
* PConv and VGG loss are the best improvements

# Conclusion
* Implementation of PConv2D and PConv3D
* Promising resultls
* Kickstarted GE exploration and gave them insights on their future work
* Had fun with advance machine learning

# Questions
## Guillaume Tochon
Le papier a ete utilise sur des images de scan ?
> Non sur des images naturelles

Expliquer 'smoothing loss'
> Dilatation verticale et horizontale des resultats

## Elodie Puybareau
Generation des artefacts: probleme avec modele 2D+T, pourquoi blanc alors que modele 2D noir ?
> Les modeles 2D sont aussi blanc sur les images

## Eleves
Exemple d'applications concretes ?
> Application de corrections permet d'avoir des images pouvant etre travaillees pour un medecin
![](https://i.imgur.com/zaTwI6a.png)

Genration des artefacts aleatoires ?
> Oui pour la position et rotation en 3D mais sinon non, pas de perte de temps a generer de la donnee

Tester avec des formes differentes ?
> Oui avec des coins et des aiguilles

Generer un nombre infini de donnees, probleme de fit ?
> Oui

Interpolation lineaire plus simple ?
> Oui mais beaucoup de stries et n'arrive pas a reconstruire certaines parties

# Retour GE Healthcare
Bonne organisation, bon avancement des projets mais baisse d'activite lors d'examens, groupe autonome