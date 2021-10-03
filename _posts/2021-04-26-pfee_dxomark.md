---
title:          "PFEE - Sujet 7: DXOMARK - Custom QT Video Player"
date:           2021-04-26 16:00
categories:     [Image S8, PFEE]
tags:           [Image, S8, PFEE]
math: true
description: Custom QT Video Player
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/BJFNvHNDu)

# Introduction
Laurent Chanas
- Product owner
- Partie creation/suivie des mesures

Claudio
- Ingenieur traitement d'image

Loris
- Software developer pour l'equipe Analyzer
- Integration traitement d'image

## A reference for the press and the industry
![](https://i.imgur.com/eQgVHCC.png)
- Score DXOMARK de la camera lors de l'annonce d'un nouveau smartphone
- Grande expertise en traitement d'image

## Renowned for camera tests and scores for 12 years, DXOMARK also tests audio and display
![](https://i.imgur.com/fxAmv0U.png)

# Analyzer, the measurement reference solution

<div class="alert alert-info" role="alert" markdown="1">
**The reference** for reliable image quality evaluation and optimization
</div>

## A turn-key and modular solution
![](https://i.imgur.com/5RHGzX8.png)

![](https://i.imgur.com/aKUou0m.jpg)
Analyse la photo de l'appareil photo pour trouver des defauts

## Easy-to-use software
![](https://i.imgur.com/5hhucR1.png)
- Un peu old school

## Analyzer, a standards compliant solution
![](https://i.imgur.com/vBLPjSV.png)

<div class="alert alert-warning" role="alert" markdown="1">
Important que tous les produits suivent les normes
</div>

## L'equipe
![](https://i.imgur.com/tPGodU4.png)
1. Une equipe hardware
2. Une equipe traitement d'image/software

<div class="alert alert-info" role="alert" markdown="1">
Suivi hebdomadaire
</div>

# Le projet
## Contexte du projet
![](https://i.imgur.com/k6CTze4.png)

Aujourd'hui, il y a plusieurs facon de decoder une video. Il faut determiner la librairie qui correspond

## L'existant
Inspiration d'un logiciel existant
![](https://i.imgur.com/aVmnHdP.png)

<div class="alert alert-danger" role="alert" markdown="1">
Le logiciel doit utiliser du GPU
</div>

## Description du projet
![](https://i.imgur.com/fN2IFqA.png)

<div class="alert alert-success" role="alert" markdown="1">
Les demo seront toujours en Python, en utilisant la partie cree en C++
</div>

Il faut qu'il y ait quelque chose d'aboutit a chaque fin de mois, faire une demonstration de quelque chose de fonctionnelle

## Organisation du projet
![](https://i.imgur.com/uxCropc.png)

*Pourquoi utiliser du Python ?*
Beaucoup de mesures dev en Python

# Questions
Le projet est que pour les etudiants ou il y a une equipe ?
> Que les etudiants

Les attentes: quelles attentes en terme de temps pour un lecteur en C++?
> On ne nous demande pas de refaire un decodeur video, on utilisera FFMPEG, bonnes inspirations sur des projets existants.