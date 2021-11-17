---
title:          "TVID: De l'image a l'ecran"
date:           2021-11-17 14:00
categories:     [Image S9, TVID]
tags:           [Image, S9, TVID]
math: true
---

Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/BJIwcdMdY)

# Cadences en pratique

<div class="alert alert-warning" role="alert" markdown="1">
On a des problemes de precisions
</div>

Tout est entier:
- PTS: temps image source
- STC: temps horloge affichage

Resolution d'increment: TIR
- TIR(PTS) = duree d'une seconde dans le flux video
- TIR(STC) = duree d'une seconde a l'affichage

Si TIR(PTS) non \% TIR(STC), probleme de $\color{red}{\text{fraction continue!}}$

## Exemple

TIR PTS = 90000 = 1 seconde

Supposons STC = timer hardware a 5 KHz
- TIR(STC) $=5000$

Pour un affichage a 50 fps:
- $\Delta STC=5000/50=100$ (TIR \%)

*Comment comparer STC avec TIR(STC) = 5000 vs PTS avec TIR(PTS) = 90000*

<div class="alert alert-success" role="alert" markdown="1">
Produit en croix
</div>

$$
STC' = STC \times TIR(PTS) / TIR(STC) = STC \times 18
$$

STC' comparable avec PTS

<div class="alert alert-warning" role="alert" markdown="1">
Mais jitter de STC multiplie par $18$
</div>

Adaptation source 59,97 ips -> affichage 60 ips
- Theoriquement: adaptation par repetition 1 image sur 1000
- En pratique: jitter PTS + jitter STC
    - Tremblement du criteres PTS - STC

# Bufferisation

On veut envoyer a l'affichage une image a l'heure !

On fait de la bufferisation pour les jeux CGI realtime

<div class="alert alert-info" role="alert" markdown="1">
**Bufferisation**: art de choisir l'image a afficher
</div>

<div class="alert alert-danger" role="alert" markdown="1">
Il faut qu'il y ait toujours une image a l'ecran
</div>

## Bufferisation non VSYNC

<div class="alert alert-info" role="alert" markdown="1">
Envoyer le backbuffer suivant des qu'il est pret
</div>

Avantages:
- Un seul backbuffer
- Rapide

Inconvenient:
- $\color{red}{\text{Tearing back/front}}$

![](https://i.imgur.com/7iBgIHD.png)

## Bufferisation VSYNC

<div class="alert alert-info" role="alert" markdown="1">
Permutter frontbuffer et back buffer
</div>

Avantages
- Pas de tearing

Inconvenient
- $\color{red}{\text{Producteur aussi leant que l'afficheur}}$

![](https://i.imgur.com/SCL6MJI.png)

<div class="alert alert-danger" role="alert" markdown="1">
Notre jeu/application va etre ralenti
</div>

> C'est le meme phenomene que celui du passage des jeux japonais aux consoles europeennes avec des jeux $20\%$ plus lent

## Bufferisation triple + VSYNC


<div class="alert alert-info" role="alert" markdown="1">
Deux backbuffers composes en alterance
</div>


- Au VSYNC: envoyer le backbuffer pret en front buffer
- Avantages
    - Pas de tearing
    - Decouplage cadence production vs affichage
- Inconvenients
    - $\color{red}{\text{Deux backbuffers}}$
    - $\color{red}{\text{CPU/GPU a donf}}$

![](https://i.imgur.com/ed7inHw.png)

# Comment afficher ?

*Comment cadrer l'image dans l'ecran ?*
- En frequence
- En phase

En frequence:
- Pulses verticaux: VSYNC
- Pulses horizontaux: HSYNC

En phase:
- Palliers avant/arriere

Pulses et palliers normalises

VGA, DVI, HDMI: Display Data Channel => Extended Display Identification Data

Xorg: "Modelines"

## Cadrage d'une image

![](https://i.imgur.com/Gw6g3gQ.png)

- Vertical blanking
- Horizontal blanking

### DVI/HDMI

![](https://i.imgur.com/zjrY10D.png)

## HDMI 3D

*Comment afficher des images 3D ?*

- Plusieurs formats 3D numeriques
- Dans tous les cas, pixel clock $\times 2$

Checkerboard (NVIDIA):
- VBlank + VSync
- HSyncs + Lignes de pixels OG/OD en quinconce
- Lignes deux fois plus larges

![](https://i.imgur.com/8IcUffb.png)

Frame pack (HDMI 1.4A)

![](https://i.imgur.com/ClQovQL.png)

![](https://i.imgur.com/ktT5ZZK.png)

## Analogique

![](https://i.imgur.com/VVMnsar.png)
