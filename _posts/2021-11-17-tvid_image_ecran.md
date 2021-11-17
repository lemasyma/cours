---
title:          "TVID: La video numerique en pratique"
date:           2021-11-17 14:00
categories:     [Image S9, TVID]
tags:           [Image, S9, TVID]
math: true
---

Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/r14LNrFvY)

![](https://i.imgur.com/gA1JHpC.png)

# Film et entrelacement

- Film = 24P, NTSC = 60I
- Comment passer un film a la tele ?
    - 2:3 pulldown
    - 4 frames, 10 fields
    - A: TFF + RFF
    - B: BFF
    - C: BFF + RFF
    - D: TFF

![](https://i.imgur.com/WPSTWyx.png)

<div class="alert alert-success" role="alert" markdown="1">
Voila comment on envoie des films a la tele Americaine (*tele-cine*)
</div>

> Et oui, on repete des films !

# Desentrelacement

- Reconstruire les lignes manquantes
- Plusieurs approches
- Toutes inexactes
- Complexite variable
- En pratique: efficacite / cout

![](https://i.imgur.com/dtTFi3P.png)

<div class="alert alert-warning" role="alert" markdown="1">
Ce n'est pas qu'on ne sait pas faire, c'est qu'on fait pour un budget
</div>

*Desentrelacer, comment ca marche, combien ca coute ?*

## Methode

- Ne rien faire

<div class="alert alert-danger" role="alert" markdown="1">
C'est indadmissible
</div>

- Weave
    - Lire une frame (a)
    - \$$=1:1$ (a)
- Skip field
    - Lire $2\times$ le meme field (a)
    - Si field bottom $\to$ aligner frame (b)

### Alignement

Image entrelacee 4:2:0 MPEG-2

![](https://i.imgur.com/7YuBYry.png)

![](https://i.imgur.com/n9z4w3a.png)

On doit *upscaler* verticalement pour skip field

### Upscaling

<div class="alert alert-info" role="alert" markdown="1">
**Definition**

Agrandir une image source a faible resolution
</div>

<div class="alert alert-warning" role="alert" markdown="1">
On cree des pixels
</div>

#### Upscaling NN: **Nearest Neighbour / Plus proche voisin**
- Repeter le pixel voisin

![](https://i.imgur.com/bO0lGRg.png)

> Utiliser dans la Super Nintendo ou la Neo Geo

Avantages:
- Rapide
- Gratuit

Probleme:
- $\color{red}{\text{Moche}}$


#### Upscaling BF (Bilinear Filtering)

- Interpolation lineaire 2D
- Trois interpolations 1D
    - entre $P_{00}$ et $P_{10}$: $Q_0$

TODO

![](https://i.imgur.com/2AyG2pH.png)

Avantages:
- Acceptable
- Pas cher

Probleme:
- Pas pour les gros ratios (SD $\Rightarrow$ 4K)

![](https://i.imgur.com/w41eRst.png)

#### Upscaling B-Spline

- Plusieurs polynome
- Points de passage pour les pixels en 2D
- B-Spline: Contrainte de continuite entres les polynomes

![](https://i.imgur.com/OgqvT2y.png)

Tres souvent: B-Splines cubiques

![](https://i.imgur.com/Ie3Cdg2.png)

C'est flou, mais c'est acceptable
- SD $\to$ 4K: OK

Problemes:
- Cher
- Risque (ringing)

Le resultat est tres inegal.

<div class="alert alert-danger" role="alert" markdown="1">
Il n'y a aucune strategie *parfaite*
</div>

Le coup de skip field c'est \$ $= 1:1(a) + \text{filtrage}(b) + \text{upscale}(c)$

- Bobbing:
    - Lire chaque field 1/1 (a)
    - Si field bottom $\to$ aligner frame (b)
    - Upscaler verticalement $\times 2$ ( c )
    - Cout $=1:1(a) + \text{filtrage}(b) + \text{upscale}(c)$
- Blending (Microsoft)
    - Lire une paire de fields (a)
    - Aligner fields bottom (b)
    - Upscaler verticalement $\times 2$ ( c )
    - Cout $=2:1(a) + 2\times \text{filtrage}(b) + 2\times\text{upscale}(c) + \text{mixage}(d)$
- $\color{red}{\text{Adaptative (Spatial, MoComp)}}$
    - Desentrelaceur intelligent

![](https://i.imgur.com/4sCxUEv.gif)

### Adaptatif spatial pur

- Plusieur fields: B0, T1, B1
- Decoupes en zones de pixels: $Z_i$
- Pour chaque $Z_i$
    - "difference" entre $B1$ et $B0$ (parite)
    - $E_i\sim = Z_i(B1) - Z_i(B0)$
    - $E_i\gt$ seuil: $Z_i$ "en mouvement"
        - Pixels $Z_i(T1)$ bobbes
    - Sinon $Z_i$ "statique"
        - Pixels $Z_i(T1)$ weaves avec $Z_i(B0)$
    - Avantages
        - Si mouvement: $Z_i(T1)$ desentrelacee
        - Sinon $Z_i(T1)$ pleine resolution
        - Rendu acceptable
    - Inconvenients
        - Certains mouvements indetectables (translation, recouvrements)
- \$ $=3:1+\text{differenciateur} + \text{bob} + \text{multiplexeur}$

Amelioration
- 4 fields
- $E_i = \max(Z_i(B1) - Z_i(B0))$, $Z_i(T1) - Z_i(T0)$
- Meilleure detection de "mouvement"
- \$ $=4:1+2\times\text{differenciateur} + \text{bob} +\text{multiplexeur}$

Adaptatif temporel:
- Spatial + estimateurs de mouvements convolutifs
- FIR / Turbo
- Cuisine secrete brevetee (Faroudja)
- Plus beau
- ***BEAUCOUP PLUS CHER***

## Exemples

![](https://i.imgur.com/eCa0fpn.png)

# Cadence image

- US: 1953: NTSC en couleur
- Interference image/son a 60 ips

<div class="alert alert-success" role="alert" markdown="1">
**Solution**: changer la frequence image
</div>

- $\times 1000/1001$
    - 60 ips $\Rightarrow$ 59,94 ips
    - 30 ips $\Rightarrow$ 29,97 ips
    - 24 ips $\Rightarrow$ 23,978 ips
- Transparent, economique **penible**
- "Modes TV", "Modes PC"

Image animee: quelle frequence choisir ?

- Cinema
    - Muer: 16 ips
    - Parlant: 24 ips
- TV
    - Synchro cameras et TVs
    - "Horloge commune" ?
    - Frequence secteur !
    - US, JP: 60 ips
    - EMEA: 50 ips

## Cadence US

US: $60$ ips
- $60 \Rightarrow 30$: sauter 1 image sur 2
- $30 \Rightarrow 60$: repeter 1 image sur 2
- $24 \Rightarrow 30$: repeter 1 image sur 5
- $59,97 \Rightarrow 60$: repeter 1 image sur 1000
- $60 \Rightarrow 59,97$: sauter 1 image sur 1000
- $29,97 \Rightarrow 60$: repeter 1 image sur 2 *et 1 fois sur 1000*

## Cadence EU

EU: $50$ ips
- $60 \Rightarrow 50$: sauter 1 image sur 6
- $50 \Rightarrow 60$: repeter 1 image sur 5
- $24\Rightarrow25$: repeter 1 image sur 24 ?
    - NON! accelerer $25/24$: $+4\%$
    - $2m20s/h$
    - $+1$ demi-ton

> Mega drive: toute la logique etait conditionnee par l'horloge video
> Certains jeux etaient ralentis en Europe pour le passage $60Hz\to50 Hz$
> Perte de $20\%$ de vitesse !

- $30 \Rightarrow 50$: rapport 5/3. Repeter $2\times$ fois la 3e image ?
    - $1$ $2$ $3$ $\color{orange}{3}$ $\color{red}{3}$
    - Pourquoi on veut pas faire ca ? Parce que c'est saccade
    - On fait: $1$ $\color{orange}{1}$ $2$ $\color{orange}{2}$ $3$
    - Plus homogene $\Rightarrow$ resultat plus fluide

## Cadences en pratique

Tout est entier:
- PTS: temps image source
- STC: temps horloge affichage

Resolution d'increment: TIR
- TIR(PTS) = duree d'une seconde dans le flux video
- TIR(STC) = duree d'une seconde a l'affichage

Si TIR(PTS) non $\%$ TIR(STC) probleme de $\color{red}{\text{fraction continue !}}$

### Exemple

TIR PTS = 90000 = 1 secnode

![](https://i.imgur.com/1KqjrRh.png)

<div class="alert alert-danger" role="alert" markdown="1">
La FC fait apparaitre de la gigue, aka JITTER
</div>

![](https://i.imgur.com/V04xFz1.png)
