---
title:          "VPOA: Perception 3D"
date:           2021-11-03 09:00
categories:     [Image S9, VPOA]
tags:           [Image, S9, VPOA]
math: true
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/HywOSpyDK)

# Introduction

## Magellium

- Observation de la terre
    - Analyse et traitement de donnees satelittes
- Geo-information
- Imagerie et Applications
    - Essayer d'extraire de la donnee image
- Infrastructure logicielle

L'entreprise:
- 248 employes
- 2 sites

### Offres et marche

![](https://i.imgur.com/SPLD1G7.png)

### Imagerie & applications

Activites
- Image & video
- Lidar & 3D
- Robotique

Offre
- Transfert de technologies
- Conception, systeme de perception
- Dev logiciel

### Positionnement

![](https://i.imgur.com/0yFT5qq.png)

<div class="alert alert-warning" role="alert" markdown="1">
Ce n'est **pas** de la sous-traitance
</div>

### Technos cles

- Capteurs 2D & 3D
- Detection et reconnaissance d'objets
- Localisation et navifation
- Technos informatiques avancees

### Synthese

![](https://i.imgur.com/dAIU8P3.png)

## Metier et projets

Responsable technique
- Definition des architectures et algos
- Encadrement technique des equipes
- Echange clients et/ou partenaires

Thematiques
- Computer vision
- Robotique d'exploration planetaire
- Robotique orbitale

Autres
- Labo vision
- Deep learning

### Projet H-20

<div class="alert alert-info" role="alert" markdown="1">
Projets finances par la comission europeenne
</div>

![](https://i.imgur.com/p8ooAQK.png)

![](https://i.imgur.com/ssnNccL.png)

> Autonomous Decision Making

![](https://i.imgur.com/TbfuFxf.png)

Assemblage de structures en orbite comme des telescopes

![](https://i.imgur.com/YLBui8h.png)

Suite de ADE

![](https://i.imgur.com/OK7jBMd.png)

T0: en mois

Beaucoup implique au CNES

![](https://i.imgur.com/k2Mr6Kw.png)

Robot Simple Fetch Rover (SFR)

![](https://i.imgur.com/umXGZGk.jpg)

MMT2 pour Thales

![](https://i.imgur.com/HPiLd8Q.png)

## Computer vision

*Comment les eleves decrivent le computer vision ?*
![](https://i.imgur.com/c3P72nO.png)

> "Un truc de GISTRE"

<div class="alert alert-info" role="alert" markdown="1">
**Definition**
Un domaine inter-disciplinaire pour permettre a une machine d'analyser, traiter et comprendre une representation de l'environnement obtenue par un systeme d'acquisition.

Cette branhe de l'intelligence artificielle implique le developpement d'algorithmes permettant l'automatisation de taches que le systeme visuel humain peut realiser.

![](https://i.imgur.com/XKdmUo4.png)

</div>


# Introduction

*Qu'est-ce que la perception ?*
> Une representation de la realite

On va *estimer* des choses
- proprietes geometriques
- proprietes semantiques
    - Ce qui concerne le sens/la signification

*Que peut-on obtenir ?*
- Reconstruction 3D
- Interpretation semantique
- Interpretation d'image

## De l'objet a l'observation

![](https://i.imgur.com/JYDpH54.png)

### De l'observation a l'objet

Ce qu'on veut faire en computer vision

![](https://i.imgur.com/EXZNYmp.png)

# Systemes d'acquisition 3D

![](https://i.imgur.com/7vK5yB9.png)

## Tomographie numerique

Rayons X
- Principe de l'IRM
- Superposition de coupes 2D successives

![](https://i.imgur.com/JoLM3fd.png)

### Telemetrie par temps de vol

Envoi d'une impulsion pulsee
- Lumineuse classique: camera ToF

### Lidar ToF

![](https://i.imgur.com/KwfH0Js.png)

*Comment on voit derriere l'objet ?*
> On ne peut pas voir derriere les objets
> On devine en utilisant des donnees autour et on interpole

### Telemetrie par decalage de phase

Envoi d'une impulsion modulee
- Lumineuse classique: Camera SWIR a modulation de phase
- Lumineurse Laser: LIDAR
- Ultrasonore: SONAR
- Ondes Radio: RADAR

Mesure du decalage de la phase

![](https://i.imgur.com/vNixvVB.png)

<div class="alert alert-warning" role="alert" markdown="1">
Il faut utiliser des longueurs d'ondes adaptees aux utilisations qu'on veut en faire
</div>

![](https://i.imgur.com/N79nglw.png)

![](https://i.imgur.com/dj1izcm.png)

> C'est comme ca qu'on se fait flasher sur l'autoroute

### Triangulation

Principe utilise par les geometres, le GPS...

![](https://i.imgur.com/ZAice7u.png)

### Triangulation active

Pointeur laser
- Un rayon laser est envoye vers l'objet a mesurer
- La lumiere diffusee est observee par une camera
- On peut en deduire la profondeur du point

Laser ligne, profilometrie
- Une image saisie donne une ligne de points
- Un unique balayage suffit pour assurer la couverture de la surface

Lumiere structuree
- Projection d'un motif connu
- Appariement pixels/motif

![](https://i.imgur.com/TICe8eB.png)

![](https://i.imgur.com/H84qqgA.png)

## Cameras

Avantages:
- Pas de contact
- Peu onereux
- Robuste (~pas de piece mobile, pas d'interferences...)
- Facilite d'acquisition de grandes quantites de donnees
- Couverture dense
- Grande variete de distances
- Possibilite d'obtenir de l'information 2D et 3D
- Pas besoin d'eclairage specifique
    - Technique passive
- Informatino geometrique mais aussi semantique, interpretation de l'image
- Donnee directement interpretable par l'Homme

Inconvenients:
- Besoin de lumiere
- Occlusions
- Perte d'information
    - Une image est une projection du monde 3D sur un plan 2D
- Difficulte de l'appariement des pixels
- Precision relativement faible

## Mono-vision passive

- Utilisation d'image 2D pour avoir un rendu 3D

## Stereo-vision

- Vision d'une meme scene depuis 2 endroits legerements decales l'un par rapport a l'autre
- Principe de la perception 3D chez l'Homme

## Precision et etalonnage

- Les points 3D sont des mesures geometriques obtenues par des principes physique (lumiere, contact, etc.) et mecaniques
- Les erreurs systematiques de mesure peuvent etre ameliorees par calibrage/etalonnage

![](https://i.imgur.com/AFqTNao.png)

# Modelisation de la camera

## Geometrie optique

Postulats:
- La propagation de la lumiere est decrite par des rayons lumineux provenant d'une source de lumiere
- Un rayon lumineur suis une ligne droite dans un milieu homogene
- A l'intersection entre 2 milieux homogenes, la lumiere est reflehie ou refractee
- Le chemin parcouru par un rayon lumineux et reversible
- L'intersection de rayons lumineux est sans effets

## Modelisation de la camera

- Capteur uniquement

![](https://i.imgur.com/LgTaSIp.png)

*Comment eviter ca ?*
> On met une lentille :) (Theotime)

- Pinhole/stenope

![](https://i.imgur.com/beQfhzx.png)

<div class="alert alert-info" role="alert" markdown="1">
C'est le **modele stenope**

![](https://i.imgur.com/QIFDCeo.png)

</div>

## Distance focale

![](https://i.imgur.com/3VHVbhw.png)

## Ouverture

![](https://i.imgur.com/UWMAarU.png)

<div class="alert alert-danger" role="alert" markdown="1">
Reduction de la taille de l'ouverture
- Amelioration de la nettete
- Reduction de la luminosite

![](https://i.imgur.com/WKaRkPz.png)

</div>

<div class="alert alert-info" role="alert" markdown="1">
**Problematique du computer vision**: choisir la bonne ouverture
</div>

## Lumiere

- Sans lumiere, pas d'image (pas de bras pas de chocolats)
- L'illumination de la scene a une influence importante sur le processus d'acquisition
- Controler l'illumination est un concept clef
- GLobalement possible de controler l'illuminatino dans l'industrie
- Difficile a impossible en milieu exterieur

<div class="alert alert-warning" role="alert" markdown="1">

Il faut si possible controle l'illumination

</div>

- Sinon, agir sur les parametres physiques de la camera
    - Vitesse d'obturation
    - Ouverture
- Petite vitesse d'obturation et/ou grande vitesse de l'objet $\Rightarrow$ attention au flou de mouvement
- Logiciel d'auto-exposition
- Cameras "global shutter" plutot que "rolling shutter"

![](https://i.imgur.com/xgMpgbr.png)

## Lentilles

- Utilisation d'une lentille pour concentrer la lumiere sur le plan image
    - Amelioration de la luminosite
    - Amelioration de la nettete

## Distance focale

<div class="alert alert-info" role="alert" markdown="1">
La distance entre la lentille et le point ou tous les rayons lumineux convergent
</div>

## Focus

<div class="alert alert-warning" role="alert" markdown="1">
Les objets sont correctement projetes sur le plan image uniquement lorsqu'ils sont a une certaine distance de la lentille/lorsque le capteur est a une certaine distance de la lentille
</div>

## Distance de focus

![](https://i.imgur.com/mUpYbdy.png)

## Hyperfocale

<div class="alert alert-info" role="alert" markdown="1">
**Definition**

Distance minimum a laquelle il est possible de faire la mise au point tout en gardant les objets situes a l'infini avec une nettete acceptable

> Depend de la distance focale et de l'ouverture

![](https://i.imgur.com/Jj4tZTn.png)

</div>

## Validite du modele stenope

On peut assimilier une camera munie d'une lentille a une camera stenope si:
- On considere uniquement le rayon lumineux central
- On suppose que la mise au point est faite
- On considere que la distance de focus de la camera avec lentille est equivalenete a la distance focale de la camera stenope
- On neglige ou corrige les distortions induites par la lentille
- On ajoute un systeme d'ouverture pour limiter les erreurs

## Distortions

<div class="alert alert-danger" role="alert" markdown="1">

Probleme des lentilles
- Distortion radiale ![](https://i.imgur.com/nlkzrl8.png)
    - Distortion en moustache mais tres rare
- Distortion tangentielle ![](https://i.imgur.com/mBUM34z.png)
    - La distortion est plus importante pour les rayons qui passent pres du bord de la lentille
- Astigmatisme ![](https://i.imgur.com/HEsmIgt.png)
    - La distance focale est differente selon l'axe $X$ et l'axe $Y$ car la lentille n'est pas parfaitement circulaire

</div>

## Abberations

Probleme des lentilles
- Aberration chromatique ![](https://i.imgur.com/MwKUfWp.png)
- Aberration comatique ![](https://i.imgur.com/KRhsXLR.png)
    - S'observe notemment sur les telescopes

## Malformation capteur

Probleme du capteur
- Asymetrie des pixels ou "skewness"
- Souvent negligeable sur les cameras modernes

![](https://i.imgur.com/SLUUR90.png)


## Bruit

Probleme du capteur
- Bruit lie a l'electronique
- Bruit lie a la discretisation des mesures (seulement 255 valeurs possibles)

![](https://i.imgur.com/eZJKSkQ.png)

![](https://i.imgur.com/KoEKHEc.png)

## Geometrie optique

![](https://i.imgur.com/TFosGRf.png)

## Systeme d'equation

![](https://i.imgur.com/sP734Pj.png)

## Centre optique

<div class="alert alert-danger" role="alert" markdown="1">
Le capteur et la lentille ne sont pas parfaitement alignes $\Rightarrow$ decalage entre le centre optique et le centre de l'image
</div>

Le point/pixel de coordonnees $(0,0)$ dans l'image correspond au coin superieur gauche

<div class="alert alert-success" role="alert" markdown="1">
On applique une tranlsation permettant de passer au centre optique $(0,0)$ de l'image
</div>

## Parametres intrinseques

![](https://i.imgur.com/IokVlCL.png)

<div class="alert alert-danger" role="alert" markdown="1">
Retenir: matrice intrinseque
</div>

3D vers image 2D:

$$
\begin{bmatrix}
u\\
v\\
1
\end{bmatrix}\sim K
\begin{bmatrix}
X\\
Y\\
Z
\end{bmatrix}\quad\text{Equivalent a un facteur d'echelle pres}
$$

$$
\exists\lambda\text{ tq }\lambda\begin{bmatrix}
u\\
v\\
1
\end{bmatrix} = K
\begin{bmatrix}
X\\
Y\\
Z
\end{bmatrix}
$$

![](https://i.imgur.com/PQYUIwW.png)

<div class="alert alert-danger" role="alert" markdown="1">
Les coordonnees du monde ne sont pas necesairement les memes que les coordonnees de la camera

![](https://i.imgur.com/gqymEcD.png)

</div>

Il faut convertir du systeme de cooordonnees du monde vers le system de coorodnnnees de la camera

$$
\begin{bmatrix}
X_c\\
Y_c\\
Z_c
\end{bmatrix}=R\cdot
\begin{bmatrix}
X\\
Y\\
Z
\end{bmatrix} + t
$$

- $R$ une matrice de rotation $3\times 3$
- $t$ un vecteur translation

![](https://i.imgur.com/Htiosuo.png)

## Du monde a l'image

![](https://i.imgur.com/jaMGKpl.png)

### Estimation de la matrice camera

- $P$ une matrice $3\times 4\Rightarrow 12$ inconnues
    - $P\sim K\cdot[R\vert t]$
    - On peut decomposer en $P=[\vert P_1\vert P_2]$
    - $P_1=K\cdot R$ matrice $3times 3$
    - $P_2=k\cdot t$ vecteur $3\times 1$
- Resectioning:
    - On estime $P$ a partir de parires $\bar x$ et $\bar X$ connues
    
### Estimation de la matrice intrinseque

Plane-based calibration
- On realise l'acquisition de multiple images d'une surface plane (e.g. damier)

![](https://i.imgur.com/iMbOWLI.png)

<div class="alert alert-success" role="alert" markdown="1">
Cela permet de fixer $Z=0$ pour tous les points du plan observe
</div>

![](https://i.imgur.com/b21EehJ.png)

On a donc:

$$
\begin{bmatrix}
u\\
v\\
1
\end{bmatrix}\sim K\begin{bmatrix}r_1&r_2&t\end{bmatrix}
\begin{bmatrix}
X\\
Y\\
1
\end{bmatrix}=H
\begin{bmatrix}
X\\
Y\\
1
\end{bmatrix}
$$

<div class="alert alert-success" role="alert" markdown="1">
A l'aide de ces equations et de la conaissance du plan observe, il est possible de determiner $K$

![](https://i.imgur.com/gd0MlmU.png)

</div>

## Parametres de distorsion

- Il est possible d'estimer des aprametres caraterisant les distortions radiales et tangentielles
- Plusieurs modeles de distorsion existent, notamment le modele polynomial de Brown-Conrady

![](https://i.imgur.com/GEgOarI.png)

## Modele complet

![](https://i.imgur.com/ExFHiww.png)

## Comment realiser une bonne calibration ?

- La cible doit etre parfaitement plane
- Les motifs de type cercles asymetrqiues donnent de meilleurs resultats
- La distance entre les points doit etre mesuree precisement
- Il faut correctement definir le nombre de lignes/colonnes de la cible

![](https://i.imgur.com/yRH9O7L.png)

![](https://i.imgur.com/uC4L24n.png)

## Controler l'environnement de calibration

- Pas de sources de lumiere directe
- Pas d'autres cible/motifs similaires visible
- Pas de relets
- Controle de l'exposition

![](https://i.imgur.com/ld2F51d.png)

![](https://i.imgur.com/egTKDPm.png)

![](https://i.imgur.com/on9D9kU.png)

![](https://i.imgur.com/729RDI0.png)

<div class="alert alert-warning" role="alert" markdown="1">
Il faut toujours calibrer **sur site**
</div>

## Procedure de calibration

<div class="alert alert-info" role="alert" markdown="1">
- Mettre la camera dans une position fixe
- Acquerir 9 images a la distance de travail la plus proche
- Recommecer pour la distance de travail moyenne
- Acquerir 8 images avec des inclinaisons differentes de la cible
- Acquerir 5 a 10 images supplementaires avec des angles "aleatoires"
- Essayer d'avoir une distribution homogene des points dans le plan image

![](https://i.imgur.com/ykGzyyf.png)

</div>

# Stereovision

## Triangulation

![](https://i.imgur.com/vTeFtb1.png)

## Geometrie epipolaire

![](https://i.imgur.com/434Z48b.png)

## Lignes epipolaires

![](https://i.imgur.com/AleIWzO.png)

## Matrice essentielle $E$

![](https://i.imgur.com/Om5m8ee.png)

## Matrice fondamentale $F$

![](https://i.imgur.com/XYbrN3T.png)

## Rectification

Le fait de rendre 2 images "paralleles"
- Rend la triangulation facile
- Facilite l'appariement

![](https://i.imgur.com/Bgum11M.png)

## Appariement de points

- Trouver les coordonnees en pixel d'un point 3D dans le plan image des 2 cameras
- Les points images sont sur la meme ligne lorsque les images sont rectifiees

![](https://i.imgur.com/1pxOTGT.png)

## Plans image paralelles

![](https://i.imgur.com/IFzUGuK.png)

<div class="alert alert-info" role="alert" markdown="1">
**Disparite**
Distance en pixels qui separe la projection d'un meme point sur les images des 2 cameras

![](https://i.imgur.com/9YFfwSz.png)

</div>

### Calcul de la profondeur

![](https://i.imgur.com/DHKN49A.png)

## Image de disparite/clarte de profondeur

![](https://i.imgur.com/PprUnqm.png)

## Calcul des coordonnees 3D

![](https://i.imgur.com/4k9rZg8.png)

## Methodes de correlation

*Comment faire pour trouver les points correspondants ?*

![](https://i.imgur.com/LNfIVKz.png)

De facon naive, recherche identique mais on peut avoir des pixels qui ont la meme valeurs et avoir des faux positifs -> selection d'une fenetre

![](https://i.imgur.com/Rr66P7l.png)

- pick a window $W$ around $\bar p = (\bar u, \bar v)$
- build vector $w$
- Slide the window $w$ along $v=\bar V$ in image 2 and compute $w'(u)$ for each $u$
- Compute the dot product $w^Tw'(u)$

<div class="alert alert-warning" role="alert" markdown="1">
C'est sensible aux differences d'exposition
</div>

<div class="alert alert-success" role="alert" markdown="1">
On fait de la **normalized crossed-correlation**

![](https://i.imgur.com/SxAJVq7.png)

</div>

On peut faire varier la taille de la fenetre

Petite fenetre:
- + Plus de details
- - Plus de bruit

![](https://i.imgur.com/NNObSwE.png)

## Problemes de la stero-vision

![](https://i.imgur.com/1gq0rjp.png)

## Occlusions

![](https://i.imgur.com/dSeWBsZ.jpg)

## Problemes de la stereo vision

- Regions homogenes et/ou peu texturees

![](https://i.imgur.com/ZjzLZQM.png)

- Patterns repetitifs

![](https://i.imgur.com/gLi1DB7.png)

## Influence de la baseline 

- Petite baseline, petit $\frac{B}{Z}$

![](https://i.imgur.com/g1jApn7.png)

- Grande baseline, grand $\frac{B}{Z}$

![](https://i.imgur.com/6BQrSBC.png)

## Disparite entiere

<div class="alert alert-warning" role="alert" markdown="1">
Le processus de stereo-correlation permet uniquement de calculer des valeurs entieres de disparite

> Il est necessaire de raliser une interpolation pour lisser les disparite

</div>

Exemples ans interpolation sous-pixellique:

![](https://i.imgur.com/HyMTihN.png)

<div class="alert alert-success" role="alert" markdown="1">
Une fonction d'interpolation sous-pixellique doit etre implementee
</div>

La fonction de disparite est estimee en appliquant une fonction de la forme:

$$
d_{subpix} = d_{int} + f(s_{left}, s_{med}, s_{right})
$$

avec $s$ les scores de correlation

On peut simpifier la formulation de cette fonction:

$$
d_{subpix}=\begin{cases}
d_{int} - 0.5 + f(\frac{l_d}{r_d}) &\text{if } l_d\le r_d\\
d_{int} + 0.5 + f(\frac{r_d}{l_d}) &\text{otherwise}
\end{cases}
$$

L'utilisation d'une fonction d'interpolation sous-pixellique a pour effet d'introduire de petites erreurs sous la forme d'une sinusoide

![](https://i.imgur.com/74mfR2W.png)

Meme si cet effet est difficilement visible sur la carte de disaprtie, il apparait clairement sur la reprojection 3D:

![](https://i.imgur.com/1Hh9rRT.png)

## Deep learning

Reseaux de neurones convolutifs:

![](https://i.imgur.com/YpNu4EJ.png)

[Etat de l'art](http://vision/middlebury.edu/stereo)

![](https://i.imgur.com/1nvcyuj.png)
