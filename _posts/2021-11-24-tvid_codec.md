---
title:          "TVID: Codec Video"
date:           2021-11-24 14:00
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

<div class="alert alert-info" role="alert" markdown="1">
Transport Stream
</div>

- Decoupage PES en paquets de 188 bits
- Multiplexage pour broadcast
- Packet Identifier (PID)
- Program Specific Information (PSI)
    - Program Allocation Table (PAT)
    - Program Management Table (PMT)
- Horloge: Program Clock Reference (PCR)

![](https://i.imgur.com/jZtY9E9.png)

![](https://i.imgur.com/a6bduYn.png)

## Demultiplexage MPEG2-TS

- PSI (PAT + PMTs) repetes regulierement
- Choix d'une chaine
    - Choix d'un PID de PMT and la PAT
    - Recuperation de la PMT correspondante
    - Filtrage des PIDs decrits dans la PMT
    - Assemblage PES correspondants
    - Extraction ES + PT
    - PTS : TS Image

## PCR

- Distinguer PCR de PTS
    - PTS: TS image
        - Cadence d'affichage des images
    - PCR: "heure de l'encodeur"
        - Synchronise le decodeur (STC) avec l'encodeur
        - En longevite (Heures)
        - Indispensable pour du streaming realtime (DVB-S/C/T)
        - Comparable a SCR pour un MPEG-PS (CVD, DVD)

## Streaming

- Streaming implique:
    - Producteur
    - Consommateur
    - Fifos
- Realtime implique:
    - Flux tendu
    - Fifo limitees (faible buffering)
    - Synchronisation producteur et consommateur
    
## STC VS PCR *FIGHT*

Pas de synchro STC $\leftrightarrow$ PCR ?
- STC $\gt$ PCR
    - Decodeur consomme **plus vite** que prevu
    - Que se passe-t-il ?
        - Drainage des FIFOs A/V
        - $\Rightarrow$ Video: saccades / ralentissements
        - $\Rightarrow$ Audio: micro-silences / repetitions
- STC $\lt$ PCR
    - Decodeur consomme **plus lentement** que prevu
    - Que se passe-t-il ?
        - Buffering limite $\Rightarrow$ blocage impossible
        - $\Rightarrow$ Depassement des FIFOs
        - $\Rightarrow$ Perte de paquets
        - $\Rightarrow$ Flux elementaires discontinus
        - $\Rightarrow$ Audio: blips, squeals, silences
        - $\Rightarrow$ Video: mosaiques, prediction surrealistes

## Synchronisation STC PCR

- Besoin d'asservir STC a PCR
- **VCXO: Voltage COntrol Xtal Oscillator**
    - Mesurer diff = STC - PCR
    - Asservir les cloks A/V correspondantes
    - Audio:
        - Reguler la vitess du decodeur
        - Controle du remplissage de la fifo de samples
    - Video
        - Reguler la vitesse du decodeur
        - Controle de la vitesse de production des pixels pour l'affichage
            - $\color{orange}{\text{Variations Pixel Clock de sortie}}$
            - $\color{orange}{\text{Tolerance en analogique ("effet de volant")}}$
            - $\color{red}{\text{TOUCHY en HDMI !}}$

# H.264 Le champion

## Objectifs

<div class="alert alert-info" role="alert" markdown="1">
Reprendre les applications de MPEG-2
</div>

Couvrir tous les nouveaux usages:
- Disques optiques avances (BD, HD-DVD)
- Streaming actif (VOD, VCONF)
- Enregistreurs embarques
- Stereoscopie

## Nouveautes

<div class="alert alert-success" role="alert" markdown="1">
Nouveau protocole: Network Abstraction Layer
</div>
- Limite les repetitions
- S'adapte aux moyens de transmission

<div class="alert alert-success" role="alert" markdown="1">
Nouveaux outils d'analyse d'image
</div>
- Macroblocs plus fins
- Predictions plus elaborees
- Filtrage a l'encodage des MV

<div class="alert alert-success" role="alert" markdown="1">
Nouveaux compresseurs entropiques
</div>
- CABAC:
    - Codage arithmetique binaire
    - Intervalles adaptatifs par modeles statistiques

![](https://i.imgur.com/sO7vQ5W.png)

- CAVLC
    - VLC type Huffman
    - Dictionnaire adapatatif par rapport aux blocs voisins

## Historique

- 1998: Initiative VCEG H26L
- 2001: MPEG + VCEG = Joint Video Team
- 2003: Finalisation premiere ebauche
- 2005: Fidelity Range Extension
    - $4:2:2$
    - $4:4:4$
    - bit depth > 8
- 2007: Scalable Video Coding
- 2009: Multiview Video Coding

## Arithmetique

- Integer DCT
    - Calculs entiers
    - Plus simples (que MPEG-2)
    - Entierements specifies
    - $\Rightarrow$ Reconstruction exacte

## NAL

<div class="alert alert-info" role="alert" markdown="1">
Network Abstrasction Layer
</div>

- NAL: Objets semantiques du flux video
- VCL: Video Coding Layer
    - NAL VCL: images, macroblocs, MVs, coefficients IDCT
    - NAL Non-VCL: parametres, metas
        - Changent rarement
    - Decouplage NAL vs mode d'envoi:
        - Byte-Stream : signalisation par *start codes* (~MPEG-2)
        - Packer-Transport
            - Pour reseaux (RTP)
            - Le protocole sous-jacent *sait* quel NAL il envoie/recoit

### Exemples

Quelques NAL
- IDR: Instant Decoder Refresh (VCL)
    - Contient seulement une nouvelle image
    - synchronisation du decodeur avec parsing minimal
    - Besoin prealable de metas non-VCL
- SPS: Sequence Parameter Set (non-VCL)
    - Profil, niveau, resolution, cadence
    - ~ MEPG-2 Sequence Header
- PPS: Picture Parameter Set
    - Codage entropique, mode de prediction, groupe et ordre des slices, filtrage de blocs

## En resume

![](https://i.imgur.com/TBlrTbs.png)

## ASO

<div class="alert alert-info" role="alert" markdown="1">
Arbitrary Slice Order
</div>
- Les slices peuvent etre envoyees dans le desordre
- + non continument dans le temps
- Avantages
    - Limite l'impact 

## FMO

<div class="alert alert-info" role="alert" markdown="1">
Flexible Macroblock Ordering
</div>

- Partition des MB par motifs
- Type 0: Interlaced: Lignes
- Type 1: Dispersed
    - En sequnces
- Type 3: Foreground: par zones (ROI)
- Explicitement par l'encodage

![](https://i.imgur.com/fRFinIK.png)

### Avantages

- Forme de segmentation
- Adaptation a la nature du contenu
- $\color{green}{\text{Resout des cas difficiles}}$
- $\color{green}{\text{Dispersion des impacts BER}}$

### Inconvenients

- Pas dans tous les profils

## Prediction Inter

Partitions de MB et sous-MB

![](https://i.imgur.com/7xXYXMx.png)

References multiples:
- 16 en theorie
- 5 a 6 en pratique
- $\color{green}{\Rightarrow\text{Moins de residus}}$
- Ponderations possibles (fdes)

![](https://i.imgur.com/yUqPHdW.png)

Motion Vectors au quart de pixel pres:

![](https://i.imgur.com/aztl4hs.png)

## Prediction Intra

- Prediction spatiale:
    - INTRA $4\times 4$
    - 9 directions de recherche
    - Pour sous-blocs $4\times 4$

![](https://i.imgur.com/R7h92Ws.png)

- INTRA $16\times 16$
    - Pour regions plus lisses / BF

![](https://i.imgur.com/mclaQUh.png)

## Filtrage in-loop

![](https://i.imgur.com/Kr1VvK5.png)

<div class="alert alert-info" role="alert" markdown="1">
In-loop deblocking filter
</div>
- Filtrage frontieres Luma $8\times 8$ ou $4\times 4$
- (resp. Chroma % sampling mode)
- $\color{red}{\text{Pendant l'encodage des MV}}$
- $\color{red}{\text{Obligatoire}}$
- Filtrage depend de la structure du bloc:
    - Plusieurs references ? F++
    - Frontieres intra et/ou inter ? F++
    - Frontieres de MB ? F++!!
    - Contours ? F--

### Avantages

- Encodeur et decodeur fournissent la meme image (pas un post)
- Meilleurs MV
    - $\color{green}{\Rightarrow \text{Residus --}}$
- $\color{green}{\text{Qualite perceptuelle +++}}$

![](https://i.imgur.com/4XBfeWe.png)

<div class="alert alert-warning" role="alert" markdown="1">
PSNR identique ?!
</div>

### Inconvenients

- $\color{red}{\text{Complexite}}$
- En baisse vu le benefice

## PAFF

<div class="alert alert-info" role="alert" markdown="1">
Picture Adaptative Frame/Field
</div>

Frame Mode (MPEG-2)

![](https://i.imgur.com/Pw0MmU7.png)

Field mode: l'un sous l'autre

![](https://i.imgur.com/WHY9pQy.png)

## MBAFF

<div class="alert alert-info" role="alert" markdown="1">
Macro Block Adaptative..
</div>

Paire de MBs: $16\times 32$
- Mode frame: $32$ lignes progressives
- Mode field: $2\times 16$ lignes entrelacees

![](https://i.imgur.com/MQlYNl3.png)

<div class="alert alert-danger" role="alert" markdown="1">
Entrelance par parties
</div>

### Avantages

- Integrite spatiale maximum
- Prediction MV TOP BOT possible pour une paire de MBs en mode field
    - $\color{green}{\text{Precision}++}$
- Pas de MV TOP BOT pour une paire de MBs en mode frame
    - $\color{green}{\text{Frugalite}++(16\%)}$
- Indices de mouvement
    - $\color{green}{\text{Desentrelacement}++}$ (c)

# H. 265 / HVEC

![](https://i.imgur.com/TV9GWoE.png)

## Objectifs

<div class="alert alert-info" role="alert" markdown="1">
Ceux de H. 264
</div>

- Debit /= 2
- Scalabilite des calculs
    - Simplification
    - Parallalisation
- 4K, 8K, 120 i/s
- Free Viewpoint (VR)

![](https://i.imgur.com/mGJqJEl.png)

- 10/12 bpc (HDR)
    - Simule la sensation d'eblouissement

![](https://i.imgur.com/WXwGPgD.png)

![](https://i.imgur.com/tLDWAkC.png)

## Historique

- 2007-2009: Rivalites MPEG - VCEG
    - Rivalites MPEG - VCEG
        - MPEG HPC : mauvais resultats
    - Union JVT VC
- 2010:
    - Janvier: Appel a propositions
    - Avril: tests, Nommage HEVC
    - Octobre: Premiere ebauche
- 2013:
    - Janvier: Ebauche finale
    - Avril: Standard ITU
- 2014:
    - Avril: Ebauche V2
        - MV-HEVC, Rext, Scalability
    - Octobre: V2 approuvee
- 2015:
    - Janvier: Publication officielle
    - Avril: V3 approuvee
        - Puis definition Screen Contents: ACT, AMVR, IntraBC, Palette
- 2016:
    - Juin: V4 refusee
    - Decembre: V4 approuvee (Extension Screen Contents)

## Principes

<div class="alert alert-info" role="alert" markdown="1">
Decouplage enCodage Prediction Transformation
</div>

- CTU: Coding Tree Unit
    - "Macrobloc" haut niveau
    - $16\times 16$, $32\times 32$, $64\times 64$

## CU

<div class="alert alert-info" role="alert" markdown="1">
Partition carree d'une CTU
</div>

![](https://i.imgur.com/kE5OEt8.png)

## PU

<div class="alert alert-info" role="alert" markdown="1">
Partition de la CU
</div>

<div class="alert alert-danger" role="alert" markdown="1">
Uniquement la prediction
</div>

![](https://i.imgur.com/jPrBX2g.png)

Intra:
- CU == PU
- Sauf au dernier

## TU

<div class="alert alert-info" role="alert" markdown="1">
Transformation Unit
</div>

- Parition de la CU

<div class="alert alert-danger" role="alert" markdown="1">
Uniquement les residus
</div>

- Independante de la partition PU

![](https://i.imgur.com/jPFMqB8.png)

Ressemble a ...



<div class="alert alert-danger" role="alert" markdown="1">

Une TU peut couvrir plusieurs PU

![](https://i.imgur.com/JFwYpF7.png)

</div>

<div class="alert alert-success" role="alert" markdown="1">
Ou une partie de PU

![](https://i.imgur.com/kSAvUyC.png)

</div>

<div class="alert alert-info" role="alert" markdown="1">
Ou plusieurs parties de PU
</div>

## Outils

- 33 Modes de prediction intra
    - 9 pour H.264
    - **Most Probable Modes**
        - Indexation dynamique
        - $\color{green}{\text{Moins de prefixe (2b vs 5b)}}$

![](https://i.imgur.com/Lz5vc4b.png)

- IDCT:
    - $4\times4$, $16\times 16$, etc.
    - ~IDST $4\times 4 possible$

## Slices et Tiles

- Slices
    - Comme H.264
        - Headers individuels
        - $\color{green}{\text{Limitations de l'erreur}}$
        - $\color{red}{\text{Jonctions imparfaites}}$

![](https://i.imgur.com/Fre9WlI.png)

- Tiles
    - Partition rectangulaire de l'image
    - Header/sequence
        - $\color{green}{\text{Decodage parallelisable}}$
        - $\color{green}{\text{ROI/VCONF}}$

![](https://i.imgur.com/aESkYjt.png)

- Slices in Tiles, Tiles in slices: Video Split

![](https://i.imgur.com/vk6KdUq.png)

- Wavefront parallel processing
    - Slices divisees en lignes de CTU
    - Pipeline multithreadable
    - $\color{green}{\text{Efficace}}$
    - $\color{red}{\text{Intensif}}$

![](https://i.imgur.com/r1UvHc9.png)

<div class="alert alert-danger" role="alert" markdown="1">
Strategie de parallelisation
</div>

## Filtrage

- Deblocking Filter
    - Plus simple que H.264
        - Grille $8\times 8$
        - $\color{green}{\text{Parallelisable}}$
- SAO: Sample Adaptative Offset
    - Filtre non-lineaire post-DBF
    - Reduit les distorsions locales
    - Categorie des samples selon voisinage
        - Moyenne, contour, min, max
    - LUT / index d'offset

<div class="alert alert-success" role="alert" markdown="1">
Reduction des effets d'aplats (banding)
</div>

![](https://i.imgur.com/OKpgLtz.png)

## SAO

Original:

![](https://i.imgur.com/oxMttpq.png)

$\color{red}{\text{SANS}}$

![](https://i.imgur.com/aGp2P38.png)

$\color{green}{\text{AVEC}}$

![](https://i.imgur.com/x7fXQhW.png)

# Epilogue

## Autres CODECS

- MPEG/VCEG/JVT: Versatile Video Codec
    - ITU Universite Industriels
    - Evolution de H.265
    - Debit $\sim 40\%$
    - Finalise 07/2020
    - Encodeurs dispo (09/2021)
    - Licences, royalties... comme HEVC
- Alliance for Open Media: AV1
    - Amazon, Google, Samsung, ARM
    - Temps d'encodage >>> VVC
    - S'ameliore avec ML (Google)
    - En deploiement:
        - Netflix: depuis 2018
        - Android TV 10: obligatoire
        - Twitch: 2022

## Evolution du marche

- Changer de code $\Rightarrow$ \$
    - Nouveau HW + SW
    - Nouvelle conso (W)
    - Nouvelles box utilisateur
- Bandes passantes plus importantes
    - Fibre, 4G, 5G, 802.11ax
    - $\Rightarrow$ taux de compression en second plan (cf H.264)
- Nouveau
    - Netflix, Hulu, Amazon, Apple TV...
    - Veulent le code "magique"
        - Pour toutes les box
        - Dont la licence est **la moins chere** (cf AV1)

## Evolution du streaming

- Trivia
    - $60\%$ du trafic internet
    - $\color{green}{\text{Netflix}: \sim\$ 2.25 B / an}$
    - 2018: +50\%, 2019: + 59\%, 2020: +47\%
    - **300 MT** $CO_2$/an (~Espagne)
    - $1\%$ des emissions $CO_2$ mondiales
    - Questions financieres et sociales evidentes