---
title:          "Conference Google: Construire des solutions plus intelligentes sans expertise en machine learning"
date:           2021-04-20 14:00
categories:     [Image S8, conference]
tags:           [Image, conference, S8]
math: true
description:    Construire des solutions plus intelligentes sans expertise en machine learning
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/rJm6fBnI_)

<div class="alert alert-danger" role="alert" markdown="1">
Sans expertise en ML != Sans ML
</div>

# Intro
## Who are we ?
Laurent Picard
- Developer advocate - Google Cloud
- Ebook pioner

> Any sufficiently advanced **technology** is indistiguishable from **magic**
> - Arthur C. Clarke

## What is machine learning ?
![](https://i.imgur.com/lpGWT4z.png)

## Why is machine learning now possible ?
![](https://i.imgur.com/ci0TukS.png)

## Three ways we can benefit from ML today
![](https://i.imgur.com/FuCrXlK.png)

<div class="alert alert-success" role="alert" markdown="1">
Ne reiventez pas la roue !
</div>

Nouveau champ: auto-ML
- on peut construire nos propres models sans expertise

![](https://i.imgur.com/PTYocuO.png)

# Machine learning API

## Ready-to-use models
![](https://i.imgur.com/rOzhFDz.png)

## Vision API
Computer vision before ML:

![](https://i.imgur.com/NoXDADf.jpg)

Landmark detection:
![](https://i.imgur.com/xMR5E4Z.png)

<div class="alert alert-success" role="alert" markdown="1">
Capable de determiner ou a ete prise la photo (quel endroit)
</div>
La photo originale a ete modifiee (symetrie horizontale)
- Toujours capable de determiner l'origine de la photo

Object detection:
![](https://i.imgur.com/pjgxXAb.png)

Face detection:
![](https://i.imgur.com/qeGT6ZB.png)

Vue 3D de Gollum donc pas un vrai visage humain (mais marche quand meme !)

Text detection:
![](https://i.imgur.com/hham3wz.png)

Meme avec une legere rotation, on detecte toujours le texte

![](https://i.imgur.com/tnac3J6.png)
Detecte egalement l'ecriture manuscrite (quelques erreurs)

Web entity detection and image matching:
![](https://i.imgur.com/bSXJCUJ.png)
La photo ci-dessus de Tolkien est totalement inedite pour l'API utilisee, capable de reconnaitre Tolkien + determiner que l'origine est un journal espagnol

### OSS Client libraries
![](https://i.imgur.com/lWJ11Dk.png)

Librairies clientes en open-source sur GitHub dans plusieurs langages.

## Video Intelligence API
Demo:
![](https://i.imgur.com/tfKKlhk.png)

### OSS Client libraries
![](https://i.imgur.com/gFjPfCd.png)

## Natural Language API
Analyze text with a simple request

Syntax analysis:
![](https://i.imgur.com/Gb79GFy.png)

Entity detection
![](https://i.imgur.com/To5KzpB.png)

Content classification
![](https://i.imgur.com/QXbZ2CR.png)
![](https://i.imgur.com/eZpVNXK.png)

Sentiment analysis:
![](https://i.imgur.com/YIO7A3t.png)

<div class="alert alert-warning" role="alert" markdown="1">
Le ML se plante totalement sur la detection du sarcasme.
</div>

## Translation API
![](https://i.imgur.com/cWMb1Ki.png)

<div class="alert alert-info" role="alert" markdown="1">
Google Translate par exemple!
</div>

<div class="alert alert-success" role="alert" markdown="1">
On peut les ameliorer regulierement en fournissant de plus en plus d'exemples et de contre-exemples.
</div>

## Speech-to-Text API
Convert text to speech in 120 languages with a simple request.

![](https://i.imgur.com/Jxwuvun.png)

<div class="alert alert-info" role="alert" markdown="1">
Fonctionne en temps reel.
</div>
> Ex: il y a quelques annees repeter a un bot en appelant une banque "Je veux un conseiller" en esperant qu'il comprenne.

Consequence sympa des reseaux neuronaux: aujourd'hui les speech-to-text API sont resistants aux bruits car ils apprennent a partir de vrais echantillon.

Speech timestamps:
Search for text within your audio
![](https://i.imgur.com/bHDpSvV.png)

### OSS Client libraries
![](https://i.imgur.com/AP5wSbZ.png)

## Text-to-speech (TTS) API
Generate natural speech with a simple request

### WaveNet natural voices, par Deepmind
![](https://i.imgur.com/0Z1tibl.png)

<div class="alert alert-info" role="alert" markdown="1">
C'est le modele le plus avance de tous, qui reproduit le mieux une voix humaine.
</div>

Demo: "Quelle est la temperature a Paris ?" avec un accent anglais
![](https://i.imgur.com/ALUCg7v.png)
*Tadaaaaaa*

### OSS Client libraries
![](https://i.imgur.com/734kpwS.png)

Tuto pour generer des voix

# AutoML
Build your custom model with no expertise

## Generic results with the Vision API
![](https://i.imgur.com/M0C8N9F.png)

### Cloud AutoML
![](https://i.imgur.com/fRMAEe6.png)

Demo:
![](https://i.imgur.com/oU6hUD7.png)

Utilisation de ~250 images en moyennes

![](https://i.imgur.com/5rGoy3f.png)
> "Juste" 3h de calculs.

![](https://i.imgur.com/1NnDeq5.png)

## Auto-generate a custom model from your data
![](https://i.imgur.com/VbvaQOR.png)

## Unified in AI Platform
![](https://i.imgur.com/aDLrmZj.png)

## Demo
### Evaluation
![](https://i.imgur.com/h9Wk4sc.png)

## Transfert learning
![](https://i.imgur.com/NVBsl8I.png)

## Hyperparameter tuning
![](https://i.imgur.com/OJsFiyb.png)

# Conlusion
## How can I build smarter solutions ?
![](https://i.imgur.com/YtbrTOX.png)

## Liens utiles
→ [Présentation](https://bit.ly/slides-mlmagic)
→ [BD Google AI](https://bit.ly/ml-comic)
→ [ML codelabs](https://bit.ly/ml-codelabs)