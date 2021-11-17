---
title:          "TVID: Codec Video"
date:           2021-11-17 15:00
categories:     [Image S9, TVID]
tags:           [Image, S9, TVID]
math: true
---

Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/SyJcKtGuK)

# Que faire ?

Identifier les repetitions
- Spatiales
- Temporelles

![](https://i.imgur.com/R0kOUcz.png)

Optimiser leur codage de rouce

Dessiner le moins possible

![](https://i.imgur.com/IyHuuC5.gif)

> 2x les memes dessins pour chaque oeil

<div class="alert alert-success" role="alert" markdown="1">
On va decimer ce qui n'est pas important
</div>
- Spatialement ?
- Temporellement ?

Detruire selectivement:
- En fonction de l'application: TV, DVD/BD, streaming
- Compromis qualite <=> debit

Compression entropique (compromis qualite)
- Huffman (CAVLC)
- Arithmetique (CABAC)

# Codec Image

## JPEG

<div class="alert alert-info" role="alert" markdown="1">
Le veteran: Join Photographic Experts Group (1992)
</div>

- Limitations de la vision humaine
    - HF
    - Chroma
- Decoupage en blocs $8\times 8$
- Transformation DCT
- Quantification des coefficients
- Lecture Zig-Zag
- Huffman

<div class="alert alert-info" role="alert" markdown="1">
- Decoupage en blocs $8\times 8$
- Transformation DCT
- Quantification des coefficients

![](https://i.imgur.com/dbpjLD2.png)

</div>

### Exemple

![](https://i.imgur.com/NPagM5d.png)

![](https://i.imgur.com/BXdTX1i.png)

Bloc DCT

![](https://i.imgur.com/WEWBaza.png)

Parcours Zig zag

![](https://i.imgur.com/gIJVe9j.png)

- Codage RLE: paires {Valeur, Nombre}
- $79; 0; -2; \{-1;3\}; \{0;2\}; -1;$ EOB
- Image animee:
    - Motion JPEG
    - DV

# Codec Video

## MPEG-1

> Le pere fondateur

- Motion Pictures Experts Group (1993)
- Base sur JPEDG et H.261 (NetMeeting, PSX FMV)

> CF. JDG *les jeux FMVs*

- Support:
    - Stockage numerique: VCD
    - Reseaux fiables
- En pratique
    - $352\times 240$ ("NTSC") / $352\times288$ ("PAL")
    - 30 i/s
    - YUV $4:2:0$ MPEG-1
    - $1, 5 Mbs$

![](https://i.imgur.com/x8OoEYx.png)

## Blocs, Macroblocs

- Bloc: matrice de pixels $8\times 8$
- Aggregation en macroblocs
    - MB-Luma: 4 blocs $\times 8=16\times 16$
    - MB-Chroma: $1$ bloc U $8\times 8$ + 1 bloc V $8\times 8$
    - => 1Mb complet = 4 blocs de Luma + 2 blocs Chroma

![](https://i.imgur.com/p9mH2uV.png)

## Slices

- Suite de macroblcos
- Sans recouvrement
- => Partition de l'image

![](https://i.imgur.com/vcv0TWV.png)

![](https://i.imgur.com/E3KmhGN.png)

- Multiusage
    - Facteur de quantification individuel
    - Synchronisation (*start* codes)

## Pictures

- Suite de slices
- *Start code*
- Prediction full / half pel
- Types: I, B, P, D


# "Intra": I

- Quasi-JPEG
- Reference: elle-meme
- Quantification par defaut ("intra") surchargeable
- Macroblocs intra, codage
    - DC: DPCM
    - AC: Huffman

## Difference entre images

![](https://i.imgur.com/jmp45Yb.png)

> Le lapin apparait d'une image a l'autres

Image 1
- Traitement par blocs
- Recherche de mouvement
- Calcul des residus

![](https://i.imgur.com/zlGBbMf.png)

![](https://i.imgur.com/0rvtArT.png)

Image 2
- Vecteurs de mouvement (pixel, demi-pixel)
    - balle
- Residus
    - Lapins
    - Yeux
- Quantification nonintra
    - *uniforme*

## Exemple: Big Buck Bunny

![](https://i.imgur.com/LyKm3VJ.png)

## Vecteurs de mouvements

![](https://i.imgur.com/6c07Dmh.png)

# Prediction IP

On a des images qui dependent les unes des autres

![](https://i.imgur.com/aJ2oLqW.png)

Avantages:
- Debit(P) < Debit(i)
- Aucune latence

Inconvenients:
- Decoder une P => conserver la I et les P precedents
- Prediction + quantification => $\color{red}{\text{propagation d'erreur}}$

## Prediction IBP

![](https://i.imgur.com/dWRk3P5.png)

Avantages
- Debit(B) << Debit(P)
- "Lisse les erreurs" entre I et P
- B bidirectionnelle => moyenne des reconstructions

Inconvenients:
- Decoder une B: garder les I et P apparentees $\color{red}{\Rightarrow RAM}$
- Ordre de decodage $\neq$ ordre affichage
- $\Rightarrow$ Latence
- Zapper: besoin d'intercaler des $I$ frequemment
- $\Rightarrow$ "Group Of Pictures"

![](https://i.imgur.com/hasDw2t.png)

- Suite d'image avec au moins une $I$
- Parametres:
    - $M$: distance entre une $I$ et une $P$
    - $N$: distance entre deux $I$

## Ordre affichage vs decodage

- DO: Display Order - CO: Coding Order
- A cause des B, $CO\neq DO$
- Supposons ces images en DO:

![](https://i.imgur.com/96dBVdH.png)

- L'ordre des GOP correspondant est (en CO):

![](https://i.imgur.com/bfgvjT3.png)

![](https://i.imgur.com/iuCBJeh.png)

## Sequence Header

- Resolution
- PAR
- Frame rate

## En resume

![](https://i.imgur.com/ZG4NWwc.png)

### Encodeur MPEG-1

![](https://i.imgur.com/lUH47ho.png)

# Convoyer du son et de la video en meme temps

## MPEG Program stream

- Fichier composite contenat:
    - 1+ flux audio elementaire
    - 1+ flux video elementaire

## MPEG PES

<div class="alert alert-info" role="alert" markdown="1">
Packetized Elementary Stream
</div>

![](https://i.imgur.com/QdhRn5f.png)


PES:

![](https://i.imgur.com/cDyVntx.png)

- Flux elementaire decoupe
- Stream ID
- $\color{red}{PTS/DTS}$
- CRC

## MPEG Program Stream

- Sequence:
    - Pack header
        - System Clock Reference
        - = Horloge createur PS (pour synchro PTS)
    - Pack: Suite de PES

![](https://i.imgur.com/YEy7K5m.png)

- Convient pour un support fiable (VCD, DVD)
- Pas adapte a la diffusion de chaines de TV (broadcast)
    - Peu resistant au BER
    - Une seule base de temps (SCR)

# MPEG-2: Le premier codec video

- Objectif: polyvalence applicative
    - Broadcast DTV SD, HD (DVB, ATSC)
    - Home video (DVD, PVR)
    - Videoconf
- Differences avec MPEG-1
    - Profils et niveaux (7)
    - Entrelacement
    - Scalabilite (pseudo-HLS)
    - Plusieurs vues

## Profils et niveaux MPEG-2

![](https://i.imgur.com/4RPvPBw.png)

- SDTV, DVD, MP@ML
- SDTV Studio: HP@ML
- HDTV: MP@H14

## Entrelacement MPEG-2

- Frame entrelacee

![](https://i.imgur.com/3YjL9wj.png)

- \+ Topness bit
- Field individuels

![](https://i.imgur.com/pZRyeDL.png)

> C'etait bizarre et ca fait chier

![](https://i.imgur.com/RLUs5N6.png)

- Ordre arbitraire
- Peu commode

## Codecs et applications

![](https://i.imgur.com/GVXtmqb.png)

# Convoyer plusieurs chaines: MPEG-2 Transport Stream

- Decoupage PES en paquets de 188 bits
- Multiplexage pour broadcast
- Packet IDentifier (PID)
- Program Specific Information (PSI)
    - Program Allocation Table (PAT)
    - Program Management Table (PMT)
- Horloge: Program Clock Reference (PCR)

## MPEG-2 TS

![](https://i.imgur.com/jZtY9E9.png)

![](https://i.imgur.com/a6bduYn.png)

## Demultiplexage MPEG2-TS

- PSI (PAT + PMTs) repetes regulierement
- Choix d'une chaine
    - Choix d'un PID de PMT and la PAT

## PCR

- Distinguer PCR de PTS
    - PTS: TS image
        - Cadence d'affichage des images
    - PCR: "heure de l'encodeur"
        - Synchronise le decodeur (STC) avec l'encodeur
        - En longevite (Heures)
        - Indispensable pour du streaming realtime (DVB-S/C/T)
        - Comparable a SCR pour un MPEG-PS (CVD, DVD)
