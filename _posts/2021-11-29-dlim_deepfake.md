---
title:          "IMED2: 3D/3D registration with labeled atlas"
date:           2021-11-26 9:00
categories:     [Image S9, IMED2]
tags:           [Image, S9, IMED2]
math: true
---

# DPH and TURP treatment

![](https://i.imgur.com/2Yo0onS.png)

## The endo-vascular treatment for BPH

![](https://i.imgur.com/6zvJDsc.png)

*C'est quoi le challenge ?*

<div class="alert alert-warning" role="alert" markdown="1">
La prostate a BEAUCOUP de variantes anatomiques
</div>

![](https://i.imgur.com/60NNHTo.jpg)

La variante anatomique la moins embetante est la C. Meme si on bouche les vaisseaux, les os ne risque pas de se necroser.

La plus compliquer est la B car le point de bifurcation est proche des arteres et du penis, boucher les vaisseaux pourrait tout niquer.

Quand on fait un volume rendering, on voit *ca*:

![](https://i.imgur.com/tRwUssu.jpg)

## From CBCT to clinical information

![](https://i.imgur.com/cI5MPOJ.png)

Une fois sur le *centerline*, on peut labeliser les vaisseaux a la main, en fonction de si c'est des vaisseaux d'interets ou non.

*Pourquoi on n'essaierai pas de faire ca automatiquement ?*

![](https://i.imgur.com/zEGJ2RU.png)

![](https://i.imgur.com/OzLt3c6.png)

On a essaye dans un premier temps de classifier les arteres: on fait une boule autour de la prostate et on regarde

![](https://i.imgur.com/zDUFia4.png)

<div class="alert alert-warning" role="alert" markdown="1">
Mais ca ne marche pas pour regarder tous les vaisseaux autours
</div>

## State of the art on vessel classification

![](https://i.imgur.com/l4uQ6Zg.png)

> Pour tester les classifier, on ouvre scikit et on teste tous les classifiers a la main

# Vascular tree labeling as a classification problem on subtrees

## Overview

1. Compute descriptors
2. Predict a lable
3. Branch label assignment

## Tackle a machine learning problem

> A best practice proposal inspired from different courses

- Data splitting
    - To ensure statistical relevance of the results
- Metric definition
    - To compare algorithms and evaluate performances
- Define metrics targets
    - Human level
    - Dumb algorithm
    - State of the art
- Data preprocessing
    - Explore, 
    - outlier removal, 
    - feature engineering normalization
- Model selection
    - Identify relevant models to test
- Hyper-parameter tuning
    - Either panda or caviar
- Iterate
    - Evaluate the model
    - Learn from failure
    - Augment data

## Large Diffeomorphic Deformations Metric Mapping

![](https://i.imgur.com/GWESNDn.png)

### Compute the registration

*Pourquoi utiliser ca ?*
1. Utiliser une deformation tres non-rigide
2. On a besoin de statistiques

![](https://i.imgur.com/K3Lw0YQ.png)

## Toward atlas building

![](https://i.imgur.com/glx1nQt.png)
