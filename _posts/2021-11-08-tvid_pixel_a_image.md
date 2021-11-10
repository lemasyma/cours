---
title:          "TVID: Du pixel a l'ecran"
date:           2021-11-08 10:00
categories:     [Image S9, TVID]
tags:           [Image, S9, TVID]
math: true
---

Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/S1ZO1_LDt)

On va decouvrir les principes fondamentaux l'audio et la video numerique. 
- 20h dont 6 de TP
- TPs de 3h
- On va faire notre propre decodeur et afficheur video

Plusieurs parties:
- Fondamentaux de ce qu'est un pixel
    - Qu'est-ce que signifie les resolutions (pourquoi pas des multiples de 10 ? Pourquoi 1080i ? Pourquoi 16/9e ?)
- Structure d'une image video
- Cadences
    - Comment on fait pour afficher n'importe quel film a n'importe quelle taille vers n'importe quelle television ?
    - Comment on fait de l'adaptation de cadence ?
- Entrelacement
    - Ca nous pourri la tete depuis 70 ans
- Affichage
    - Comment trouver un mode commun d'affichage ?

<div class="alert alert-warning" role="alert" markdown="1">
Ce sont les prerequis pour la suite
</div>

La suite: standards de compression video

# Pixel

<div class="alert alert-info" role="alert" markdown="1">
C'est un **element d'une image**
</div>

![](https://i.imgur.com/E8mjnPa.gif)

Mais encore ?
- C'est un format
- Profondeur
    - Combien de bits par composants ?
- espace de couleur

## Pixel aspect ratio

Monde PC: PAR = 1:1
- Pixels carres

![](https://i.imgur.com/BCoe2bD.png)


Monde video: PAR >= 1
- Pixel rectangulaires

![](https://i.imgur.com/yAsLYU9.png)

![](https://i.imgur.com/XiAcE8S.png)

*Pourquoi ?*
> On tient ca de l'analogique: pas de resolution

- Analogique: pas de resolution
- Numerique: resolutions partout
- Besoin de correspondance numerique $\leftrightarrow$ analogique

<div class="alert alert-success" role="alert" markdown="1">

On arrive sur le **display aspect ration**: la resolution de sortie

$$
\color{red}{\text{PAR}\times\text{DIM} = \text{DAR}}
$$

</div>

*Est-ce qu'on a deja essaye de jouer un fichier VOG d'un DVD tout seul ?*
> L'image sera plus carree et deformee car on ne lit pas les metadata

## Color Space

Generateurs de graphismes RGB
- Ordis, smartphones, tablettes On Screen Display (OSDs)
    - On Screen Technique: superposition d'affichage comme l'affichage du numero de la chaine quand on zappe

*Pourquoi on affiche le nom de la chaine quand on zappe en numerique ?*
> En analogique, quand on zappait c'etait instantane car il suffisait de changer que quelques parametres pour changer de frequence sans pre-processing
> C'est juste pour **faire attendre les gens**, sinon on n'a qu'un ecran noir

*Pourquoi certaines box ont une mosaique avec plusieurs flux videos de differentes chaines ?*
> Car ce n'est pas fait par la box, ce sont des chaines mosaiques pre-composees par l'emetteur
> On utilise les metadatas pour choisir une chaine sur les mosaiques
> Certaines mosaiques ne permettent pas de selectionner de chaine

- ARGB, ABGR
    - A est le canal $\alpha$ (alpha)
    - ABGR est la representation d'Android
- BGRA, RGBA, ...

![](https://i.imgur.com/vSy6lav.gif)

Video: YUV
- Images et sequences animees
- Y: luminance
- U, V: Chrominance (aka Cb, Cr)
- Raisons historiques

*Est-ce que les premiers signaux analogiques pour la tele etaient en couleur ?*
> Bien sur que non

Vers les annees 50 on se dit que ca serait bien d'avoir la couleurs
> On va faire un truc degueulasse pour que ce soit retrocompatible avec les gens ayant une tele en noir et blanc

<div class="alert alert-danger" role="alert" markdown="1">
L'analogique est **la reponse de ce qu'on fait en numerique**.
</div>

Les US avaient NTC qui on cree un standard video de 480 lignes en noir et blanc qui est passe en couleurs en une nuit (et ca a marche !)

<div class="alert alert-warning" role="alert" markdown="1">
L'heritage de l'analogiqe nous enquiquine encore aujourd'hui
</div>

## Exemple RGB

![](https://i.imgur.com/RiljJnd.png)

*Qu'est-ce qu'on remarque ?*
> Le vert est predominant car il est predominant dans la nature
> Les humains ont un excellent pouvoir d'observation sur le vert (60-70% de notre champ de vision)
> On voit moins bien le rouge car c'est le sang et le feu (20-30% de notre champ de vision)
> On voit encore moins bien le bleu car on ne veut pas etre aveugle par le ciel

<div class="alert alert-success" role="alert" markdown="1">
La compression numerique va user et abuser de nos limitations de perception
</div>

## Exempe YUV

![](https://i.imgur.com/lPrpPld.png)

*Qu'est-ce qu'on remarque ?*
> Dans le V il y a tres peu de rouge, noye dans du gris

*Si on etait un algorithme, lesquels de ces images on trouverait plus facile a digerer que les autres ?*
> U et V ont une dynamique faible donc l'encodeur entropique va se regaler

![](https://i.imgur.com/MP5SlRe.png)

<div class="alert alert-danger" role="alert" markdown="1">
On va grignoter tout ce qui est possible pour faire des economies
</div>

## Formats

Format lineaire:
- Toute l'info est dans le pixel
- Profondeur: 8..16 bits/composantes
    - HDR: 10 bits
- 8 bpc: "True Color" 
    - Representation des pixels : ARGB, ARGB, ARGB...
- Exemple: #FF00FF00
    - C'est du vert
    - alpha opaque et vert a fond
- Exotiques: high colors

## Considerations systeme: True colors

*Combien ca coute ?*

*Que faut-il dans un systeme ?*
- Horloge Systeme
- CPU
- RAM
    - Efficacite
    - Bande passante (BW)
- BUS DMA
    - Direct Memory Access
    - Faire des transferts de donnees enorme sans utiliser un iota du processeur
    - Taille: combien de bytes au max il est capable de copier
    - BW: bande passante (nb bits/s capable de transferer)
- Modules hardware 
    - Carte video (GPU), carte son, etc
    - Autres modules d'affichage

### CCC Full Hd True Color ?

- Image fixe RGB $8bcp$ @ $1080p60$
- BW afficage: $1920 \times 1080 \times 60 \times 24 = 2,98 Gb/s$

Pour un systeme:
- Bus clock: $200$ MHz
- DRAM: DDR3 $12800$ ($8$ bytes / burst, classiquement)
    - $8$ bursts / clock
    - $\Rightarrow 64$ bytes / clock
    - $80\%$ d'efficacite
    - $\Rightarrow$ BW RAM $= 200M \times 32 = 6,4 Gb/s$
    - ~$3,88\%$ BW ram
    - ~$46\%$ BW bus
    - Juste pour afficher !
    - $\times 2$: NOK. Pas d'animation possible
- DMA: $64$ bits / clock (DMA++)
    - $\Rightarrow$ BW bus $=200M\times 64 = 12,8 Gb/s$
    - $\Rightarrow$~$3,88\%$ BW RAM
    - $\Rightarrow$~$23\%$ BW bus
    - $\Rightarrow$ Image animee jouable
    - $\Rightarrow$ Couteux

### CCC 4K ?

- Image fixe RGB 

TODO

## Pixels: formats

Format paletisse:
- Palette de couleur predeifinie
- Pixel = index couleur palette
- Profondeurs: 1, 2, 4, 8 bits / pixel

![](https://i.imgur.com/HdD0t8C.png)

![](https://i.imgur.com/UJzzSOv.png)

![](https://i.imgur.com/S0GOZZN.png)

![](https://i.imgur.com/SmfQD5v.png)

<div class="alert alert-success" role="alert" markdown="1">
**Tous** les OSDs sont paletises
</div>

## CCC Full HD palettise ?

- Image paletisee 256 couleurs

TODO

# Structure d'une image video

## Colorspace YUV

![](https://i.imgur.com/pqf4xcC.png)

## Sampling Mode

<div class="alert alert-info" role="alert" markdown="1">
**Sampling Mode**: sous-echantillonnage de la chrominance
</div>

*Qu'est-ce que ca veut dire ?*
> On va peut-etre enlever du U ou du V sur certains pixels car nos yeux ne peuvent pas le voir de toute facon
> Le fameux grignottage

- Seulement en color space YUV
- Oeil moins sensible a UV

Exemple:

![](https://i.imgur.com/U9VdBXw.png)

Sur la 2e image, on a commence a diviser l'echantillonnage

*Qu'est-ce qu'on observe ?*
> Il y a des bandes qui apparaissent a chaque bordures de couleurs
> *Elles se degeulent les unes sur les autres*
> Si on met une video youtube avec du rouge petant on aura le meme effet

<div class="alert alert-warning" role="alert" markdown="1">
Ca arrive surtout sur les cas extremes avec des transitions abruptes
</div>

On suppose 8 pixels:

![](https://i.imgur.com/yf2csMo.png)

Ils ont chacun leurs composantes

<div class="alert alert-info" role="alert" markdown="1">

**$4:4:4$**

Pour 4 pixels consecutifs (pas forcement en ligne mais aussi en carre) il y a 4 $U$ et 4 $V$

</div>

<div class="alert alert-info" role="alert" markdown="1">

$4:2:2$

Pour 4 pixels consecutifs, on n'en a que 2 qui contiennent de la chrominance

![](https://i.imgur.com/aODeAc3.png)

</div>

<div class="alert alert-success" role="alert" markdown="1">
On a litteralement decime une colonne de chroma sur 2
</div>

> Ce sont toutes les images JPEG

<div class="alert alert-info" role="alert" markdown="1">

**$4:2:0$ MPEG-1**

On a 6 composantes sur 8 bits au lieu de 12

Le calculateur fait la moyenne

![](https://i.imgur.com/72GU0oT.png)

</div>

<div class="alert alert-success" role="alert" markdown="1">
On a beaucoup economise juste en coupant la chroma une ligne sur 2 et un colonne sur 2
</div>

<div class="alert alert-info" role="alert" markdown="1">

**$4:2:0$ MPEG-2**

![](https://i.imgur.com/zvN5vjG.png)

</div>

<div class="alert alert-info" role="alert" markdown="1">

$4:1:1$

![](https://i.imgur.com/tguXBPK.png)

</div>

> Utilise par les Etats-Unis

Pendant notre enfance on avait les camescopes DV, en Europe ils sont en $4:2:2$ et aux US du $4:1:1$

<div class="alert alert-warning" role="alert" markdown="1">
Tous les CODECs aujourd'hui sont bases sur la perception visuelle
</div>

## Image planaire

- Heritage TV: Y avant UV
- PC: Images interleavees (ARGB, ARGB, ...)
- Video: Images planaires:
    - Buffers composantes separes
    - Luma: Y, Y, Y
    - Chroma: UV, UV, UV
    - Decouplage hardware / composantes

*Une image planaire, combien ca coute ?*

### CCC Full HD Planar $4:2:2$ ?

$1080p60$ YUV $4:2:2$ $8$ bits
- Luma: $1920\times 1080\times 60\times 8=\sim1 Gb/s$
- Chroma: $1920\times 1080\times 60\times 16 / 2=\sim1 Gb/s$

Pour un systeme:
- Bus clock: $200$ MHz
- DRAM: DDR3 $12800$ ($8$ bytes / burst, classiquement)
    - $8$ bursts / clock
    - $\Rightarrow 64$ bytes / clock
    - $80\%$ d'efficacite
    - $\Rightarrow$ BW RAM $=200M\times 64\times 8\times 0.8 = 81,92 Gb/s$
- Deux DMA 2 fois plus petits: $16$ bits / clock
    - $BW = 200 M \times 16 = 3,2 Gb/s/canal$
    - $2,5\%$ BW ram
    - $31\%$ BW par canal

<div class="alert alert-danger" role="alert" markdown="1">
On pas en YUV car **c'est le seul format qui nous permet de decimer le chroma** sans tout casser
</div>

### CCC Full HD Planar $4:2:0$ ?

$1080p60$ YUV $4:2:0$ $8$ bits $\gt90\%$ des fichiers video (TNT, SAT, YT, Netflix, ...)
- Luma: $1920\times 1080\times 60\times 8=\sim1 Gb/s$
- Chroma $1920\times1080\times60\times16\times\color{green}{4 = \sim 0,5Gb/s}$

Pour un systeme:
- Bus clock: $200$ MHz
- DRAM: DDR3 $12800$ ($8$ bytes / burst, classiquement)
    - $8$ bursts / clock
    - $\Rightarrow 64$ bytes / clock
    - $80\%$ d'efficacite
    - $\Rightarrow$ BW RAM $=200M\times 64\times 8\times 0.8 = 81,92 Gb/s$
- Deux DMA 2 fois plus petits: $16$ bits / clock
    - $BW = 200 M \times 16 = 3,2 Gb/s/canal$
    - $2,5\%$ BW ram
    - $\sim 31\%$ BW Y, $15\%$ BW UV

### CCC 4K Planar $4:2:0$ 10 bits ?

$2160p60$ YUV $4:2:0$ 10 bits: Netflix

- Deux DMA 64 bits / clock
- Hardware a 2 px / clock
    - BW = 200M x 64 = 12,8 Gb/s/canal
- 9% BW ram
- TODO

# Entrelacement / Desentrelacement

70 ans et toutes ses dents

Un peu d'histoire: les signaux videos ne sont pas tous faits de la meme maniere et ne sont pas fait comme on le pense.

Mais nous n'avons pas parle de la structure d'une image.

Il y a un peu moins d'un siecle, des ingenieurs se sont dit "On va transmettre de l'image analogique sur des tubes cathodiques".

Le principe d'un ecran cathodique est toujours le meme: on a une surface remplit de photophores qui emet de la lumiere quand elle se prend des electrons, elle met du temps a s'allumer et du temps a s'eteindre.

On s'est dit qu'on allait utiliser ces ecrans pour afficher des images.

*Pourquoi ecran cathodique ?*

Car les electrons sont generes par une cathode, et si on etait un peu trop pres de l'ecran on se prenait des rayons.

On ecrit notre image ligne a ligne a l'ecran et on obtient notre image.

**SAUF QUE**

On a remarque de 480 lignes c'est bien pour le format d'image. Mais si on envoie 480 lignes par image, 60 images par seconde, on a un signal beaucoup trop large.

Des ingenieurs se sont dit "Mais c'est pas un probleme, regardez le temps que prend mon ecran a s'eteindre" (c'est une gaussienne). Ces ingenieurs se sont dit "Je ne vais envoyer qu'une ligne sur 2 de chaque image et alterner entre lignes paires/impaires". 

<div class="alert alert-danger" role="alert" markdown="1">
C'est ca **l'entrelacement**
</div>

<div class="alert alert-warning" role="alert" markdown="1">
On a decime l'image spatialement.
</div>

<div class="alert alert-success" role="alert" markdown="1">
On a quasiment la meme qualite d'image
</div>

*Est-ce qu'on a vu que les tubes cathodiques scintillent ?*
> C'est lie du a l'entrelacement et alterner les images

Aujourd'hui on n'a que des ecrans plats avec des pixels avec une bonne reactivite (jusqu'a 140 Hz)

<div class="alert alert-danger" role="alert" markdown="1">
Mais ca nous pose des ENORMES problemes avec l'entrelacement
</div>

Sur nos ecrans actuels, chaque pixel a chacun sa vie.

On a un probleme de taille d'ecran, de pixels, de resolution, etc.

*Pourquoi garder l'entrelacement ?*
> Car il y a encore des pays qui utilisent des teles cathodiques

<div class="alert alert-success" role="alert" markdown="1">
Si c'est moins cher, on va le faire
</div>

> On paye cher apres car c'est a credit

## Un peu d'histoire

- 1941: standard NTSC ![](https://i.imgur.com/El1RSCa.png)
    - 6 MHz de bande passante
    - Dot crawl: information couleur mal filtree
    - 15730 ligne/s
    - 525 ligne/image
    - 15730 / 525 = 30 ips
        - OK pour films (24 ips)
        - NOK pour du direct

## Une idee simple

- 1 frame: 2 fields : pair/impair
- Captures a des instants differents

![](https://i.imgur.com/u2Jabvn.png)

![](https://i.imgur.com/fsXQ0IW.png)

TFF = Top filter (flag)

![](https://i.imgur.com/HTYg7zz.png)

BFF = Bottom filter (flag)

### Exemples

![](https://i.imgur.com/slzC3zi.png)

Une image entrelacee c'est une image avec des *dents*

<div class="alert alert-warning" role="alert" markdown="1">
Tous les flux de la TNT sont entrelaces et ne sont **pas en HD**

On en en 1440i50
</div>

<div class="alert alert-danger" role="alert" markdown="1">
Le numerique, c'est pas que c'est mieux, c'est que c'est moins cher
</div>

## Entrelacement

Avantages:
- Image fixe: resolution conservee
- Image mouvante: $2\times$ plus fluide
- BW inchangee
- Parfait pour un tube cathodique

Inconvenients:
- Resolution horizontales / 2 si mouvement
- Signaliser l'ordre des fields
- Scintillement
- Le futur devra faire avec...

![](https://i.imgur.com/R3wpcfh.gif)

## Exemple

![](https://i.imgur.com/9eGx8c8.png)

![](https://i.imgur.com/9Gocbz7.png)

![](https://i.imgur.com/VTIuImv.png)

<div class="alert alert-warning" role="alert" markdown="1">
En bas a droite l'objet bouge mais n'est pas entrelace
</div>

> Ce flux video donne des maux de tete aux ingenieurs
> Le OK ne bouge pas et ne doit pas etre entrelace
> Le logo en bas a droite est le logo corporate

<div class="alert alert-success" role="alert" markdown="1">
Il y a plusieurs entrelaceurs
</div>

Exemple: VLC

![](https://i.imgur.com/F8RB4yo.png)

*Ou est le K ?*
> On a pris que les lignes du haut et on a degage les lignes du bas
> C'est desentrelace comme un pied par le GPU

Plusieurs facons de desentrelace:
- Prendre que les lignes du dessus et upscale $\times 2$ en vertical