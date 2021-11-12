---
title:          "VPOA: Detection et localisation"
date:           2021-11-05 09:00
categories:     [Image S9, VPOA]
tags:           [Image, S9, VPOA]
math: true
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/ryDODPGDK)

# Introduction 

*Qu'est-ce que la vision ?*
- Percevoir le monde
    - Compose d'objets
    - Structure en 3D
    - Efficacement interprete par l'Homme
- Receuil d'information
    - Ensemble de points
    - Information sur la lumiere
    - Quantite et contenu spectral
- Representation du monde reel
    - Les objets n'existent pas sur la retine
    - Processus visuel d'interpretation

Vision humaine
- **Extremement complexe**
- Active de nombreuses zones du cerveau
- Possede des capacites nombreuses et variees

Vision par ordinateur
- Bio inspiree ou non
- Production d'un modele algorithmique fonctionnellement similaire aux capacites du cerveau humain
- Reprosudit seulement un sous-ensemble de capacites

## Quelques termes

<div class="alert alert-info" role="alert" markdown="1">
**Traitement d'images**:
- manipulation dont l'entree et la sortie sont des images
- Aide l'humain ou la machine a examiner des images
</div>

<div class="alert alert-info" role="alert" markdown="1">

Analyse d'images: analyse ou l'entree est une image mais la sortie est une information

</div>

TODO

## Processus d'integration dans un systeme

![](https://i.imgur.com/B9vP5wM.png)

## Objectifs de la seance

- Trouver/extraire dans l'image des informations pertinentes pour TODO

### Detection Deep-learning

![](https://i.imgur.com/iY54sij.png)

> On a entraine le modele a detecter des voitures mais ca ne reconnais que l'avant des camions

### Detection et tracking

![](https://i.imgur.com/A7pJ63x.jpg)

# Geometrie projective

## Coordonnees homogenes

<div class="alert alert-info" role="alert" markdown="1">
Systeme de coordonnees pour la geometrie projective
</div>

Passer des coordonnees cartesiennes aux coordonnees homogenes:

$$
\begin{bmatrix}
x\\
y
\end{bmatrix} \Rightarrow
\begin{bmatrix}
x\\
y\\
1
\end{bmatrix}
$$

Passer des coordonnees homogenes aux coordonnees cartesiennes:

$$
\begin{bmatrix}
u\\
v\\
w
\end{bmatrix}=
\begin{bmatrix}
u / w\\
v / w\\
1
\end{bmatrix} \Rightarrow
\begin{bmatrix}
u / w\\
v /w
\end{bmatrix} =
\begin{bmatrix}
x\\
y
\end{bmatrix}
$$

![](https://i.imgur.com/u6CNtwy.png)

![](https://i.imgur.com/cSZsGnh.png)

![](https://i.imgur.com/aR3SU38.png)

Propriete homogene: $\bar x\sim\lambda \bar x, \forall \lambda\in\mathbb R, \lambda \neq =0$

Point a l'infini: 

$$
\bar x_{inf} = \begin{bmatrix}x \\ y \\0 \end{bmatrix}
$$

![](https://i.imgur.com/kzwe2kq.png)

## Modele du plan projectif

<div class="alert alert-info" role="alert" markdown="1">
Le plan projectif $P^2$ represente l'espace 3D sur un plan
</div>

Intrepretation geometrique de l'homographie

![](https://i.imgur.com/PeupaZz.png)

## Homographies

![](https://i.imgur.com/B7uW7aT.png)

### Estimation d'homographie

![](https://i.imgur.com/wWf5gMc.png)

Estimation par Direct Linear Transform

- Necessite au moins 4 points pour obtenir une solution exacte (2 equations par point et 8 inconnues)
- Etant donne $n\ge 4$, correspondances de points 2D, determiner $H$ tel que $\bar x_i'=H\bar x_i$

Algorithme:
- Pour chaque correspondance $\bar x_i\leftrightarrow \bar x_i'$ pour claculer $A_i$
- Assembler les matrices $A_i$ en une matrice $9\times 9$: $A$
- Calculer le SVD de $A$: $U\Sigma V$
- Solution pour $h$: derniere colonne de $V$
- Determiner $H$ a partir de $h$

![](https://i.imgur.com/JrKRkqE.png)


## Homographie et plan 3D

![](https://i.imgur.com/muiUmRQ.png)

Le passage de n'importe quel plan vers n'importe quel autre plan (y compris le plan image) est une homographie

![](https://i.imgur.com/iuhko5j.png)

# Extraction de caracteristiques locales

## Representation d'une image

$I(x, y)$: valeur d'un pixel

- Dans $\mathbb R$ en monochrome
- Dans $\mathbb R^3$ en couleurs

### Variations

- De luminosite globale: $I(x,y)\to I(x,y)+\alpha$
- De contraste: $I(x,y)\to\lambda I(x,y)$
- Par translation

## Comparaison de points

Trouver le point le plus similaire

![](https://i.imgur.com/TIuMbWD.png)

Stereo-vision: on suppose que les points similaires sont sur la meme ligne

![](https://i.imgur.com/SOmWfvj.png)

*Comment trouver des points facilement identifiables ?*
> Gradients
> Contours
> Etc

## Kernel

<div class="alert alert-info" role="alert" markdown="1">
Aussi appele noyau ou masque ou matrice de convolution
</div>

- Permet d'appliquer une operation a l'image
- Convolution:

![](https://i.imgur.com/BEBUXgp.png)

## Gradient 

<div class="alert alert-success" role="alert" markdown="1">
Va nous permettre d'obtenir une caracteristique de variabilite autour d'un point
</div>

En 1D:
![](https://i.imgur.com/mDCiKnB.png)

En 2D: Filtre de Sobel

![](https://i.imgur.com/AkWZgZz.png)

![](https://i.imgur.com/RT91Spq.png)

![](https://i.imgur.com/Norvcpq.png)

### Laplacien

Detection de contours

![](https://i.imgur.com/g7YZ4xd.png)

## Detection de coins

<div class="alert alert-info" role="alert" markdown="1">
Zones ou le gradient varie dans plusieurs directions
</div>

Detecteur de Harris:

![](https://i.imgur.com/nHRZMFX.png)

### Changement d'echelle

*Comment reconnaitre un point apres un changement d'echelle ?*

![](https://i.imgur.com/Vqw9JpI.png)

<div class="alert alert-success" role="alert" markdown="1">
Avec des descripteurs !
</div>

## Descripteur

- Moyen de decrire une zone locale de l'image
- Les "features" sont associees a des points localement distincts dans l'image
- Les descripteurs sont la signature de ces points

![](https://i.imgur.com/GaTjlU0.png)

### Differences de Gaussiennes

Detection de blobs par differences de Gaussiennes:

![](https://i.imgur.com/ngGG4El.png)

On soustrait l'image floutee a l'image normale

Invariance par changement d'echelle pour les differences de Gaussiennes:

![](https://i.imgur.com/oVczY6i.png)

### Descripteur SIFT

<div class="alert alert-info" role="alert" markdown="1">
Scale Invariant Feature Transform
</div>

Detection de blobs par la methode des differences de gaussienne

![](https://i.imgur.com/wPVNwyJ.png)

## Rotation

*Comment reconnaitre un point apres une rotation ?*

### Descripteur SIFT

Histogramme d'orientations du gradient

![](https://i.imgur.com/XOLda1b.png)

- Decoupage en $4\times 4$ fenetres
- Histogramme sur 8 directions

![](https://i.imgur.com/RuGMtQo.png)

Resume:

![](https://i.imgur.com/funLyNS.png)

- Identification/Matching des keypoints

![](https://i.imgur.com/nYLkqcf.png)

## Autres descripteurs

- MSER (Maximally Stabel Extremal Regions)
- SURF (Speeded Up Robust Features)
- ORB (Oriented FAST and Rotated BRIEF)
    - SIFT et SURF sont brevetes
    - OpenCV a invente ORB comme alternative open-source et gratuite
- BRIEF
- FAST
- KAZE
- etc

## Extraction de caracteristiques locales

*Comment valoriser l'information ?*
- Reconaissance/detection d'objets
- Estimation de la pose/localisation
    - De la projection d'objets 3D sur le plan Image
    - D'objets 3D dans le monde
    - De la camera dans le monde
- Estimation du mouvement

# Reconaissance d'objets

Objectifs:
- Detection d'instances d'objets par points d'interet
    - Transformee de Hough
    - RANSAC
- Detection de categories d'objets
    - Sac de mots visuels

![](https://i.imgur.com/ILLjg3c.png)

![](https://i.imgur.com/nvH682P.png)

## Transformee de Hough

A l'origine, detection de lignes droites:
- Chaque point votre pour "toutes" les lignes qui passent par lui
- Les votes sont accumules
- Un maximum local corresponds a des lignes candidates

![](https://i.imgur.com/hcSfnBE.png)

Possible probleme: trouver le maximum vrai
- Mean shift
- Gaussian convolution
- ...

![](https://i.imgur.com/BTxhMam.png)

Transformee de Hough generalisee
- Contour/forme arbitraire
    - Choix d'un point de reference our le contour (e.g. le centre)
    - Pour chaque point du contour, se rappeler de sa position par rapport au point de reference
    - Calcul de l'angle

## RANSAC

Cas de lignes
- Choix aleatoire de droites
- Vote base sur le nombre de points proches de la ligne
- todo

Amelioration
- Elimination de outliers par RANSAC
- Amelioration de l'estimation de RANSAC TODO

### Comparaison

![](https://i.imgur.com/vfwAGTw.png)

## Reconnaissance d'objets 3D

Base sur la detection de features
- 3 features minimum sont necessaires pour la reconnaissance

Reconnaissance d'objet 3D base sur la detection d'un modele 3D connu

![](https://i.imgur.com/Cwgmt5I.png)

## Mots visuels

Principe: extraction de features locales a partir d'un certain nombre d'images

![](https://i.imgur.com/0UOpkQy.png)

- Cartographie des descripteurs vers de mots visuels qui quantifient l'espace des features
- Le centre des clusters definissent les prototypes de mots

![](https://i.imgur.com/fftVGoo.png)

- Determination de quel mot doit etre assigne a chaque nouvelle region de l'image en trouvant le centre du cluster le plus proche

![](https://i.imgur.com/dVROtkP.png)

### Exemple

Chaque groupe de patch correspond a un meme mot visuel

![](https://i.imgur.com/ynnmD0x.png)

- Resumer une image entiere a partir de sa distribution de presence de mots
- Analogue a un sac de mots souvent utilise pour les documents de texte

![](https://i.imgur.com/RmeoXEY.png)

Creation d'un vocabulaire visuel:
- Repertorier un ensemble de mots visuels (~ dictionnaire)
- Differentes strategies
    - Apprentissage supervise
    - Deep learning
    - etc

Strategies d'echantillonnage:

![](https://i.imgur.com/ixWAtiB.png)

Arbre de vocabulaire:

![](https://i.imgur.com/iCpzPCg.png)

- Remplissage:

![](https://i.imgur.com/HEpcWhN.png)

![](https://i.imgur.com/bDsQ99t.png)

Probleme:
- certains mots visuels sont discriminants
- D'autres apparaissent dans de nombreuses images

Calcul d'un poids pour chaque mot visuel
- Le poid correspond a la quantite d'info esperee 
- Normalisation des histogrammes en fonction de ce poids

# Estimation du mouvement

## Objectifs

- Detection/ Estimation du mouvement dans la scene
    - Du au mouvement de la cmaera
    - Mouvement des objets
- Perception du mouvement apparent
    - Champs des vecteurs de deplacement
    - Flux optique

## Flux optique

Difficultes de l'estimation du flux optique
- Ambiguites

![](https://i.imgur.com/jceMWVx.png)

- Premiere image: deplacement de drone, champ de vecteurs = deplacement des pixels
- Si on aune voiture qui se rapproche de nous, on peut segementer la voiture du reste de l'image a partir de champs de vecteurs

Interpretation du flux:

![](https://i.imgur.com/RUSDZIj.png)

Vitesse:
- La camera se deplace a une vitesse $(X', Y', Z')$ par rapport a la scene
- Si on derive les equations de perspective on a donc:

![](https://i.imgur.com/ufEgE5x.png)

### Interpretation du flux

Translation pure selon $X$ (ou $Y$)

![](https://i.imgur.com/SAjpekQ.png)

Translation pure selon $Z$:

![](https://i.imgur.com/7KY4y9P.png)

Cas general:
- Donne la direction du deplacement
- Mouvement $(X', Y', Z')$
- Soit $[X_0, Y_0, Z_0]^T$ un point de la scene, apres un temps $t$, il est projete sur l'image au point $[u_t, v_t]^t$ avec:

![](https://i.imgur.com/oZhsKcm.png)


Temps avant collision:
- Mesure de la taille d''un element $\lambda = f\frac{\Lambda}{z}$

![](https://i.imgur.com/mJblqFp.png)

## Bundle adjustment

- Nous avons pour l'instant uniquement utilise des paires d'image pour obtenir une information de profondeur
- Dans le cas general, il est possible d'utiliser $N\gt 2$ images/cameras

![](https://i.imgur.com/8LGDpMS.jpg)

<div class="alert alert-info" role="alert" markdown="1">
Le Bundle (block) adjustment ou ajustement de faisceaux en bloc, est une methode de resolution au sens des moindres carres les coordonnees 3D des points et aligner les images

Plusieurs images sont corrigees "en bloc"
</div>

Principe:
- Demarrer avec une approximation initiale
- Projeter les points 3D sur les plans images des cameras
- Comparaison avec la mesure
- Ajustement pour minimiser l'erreur

<div class="alert alert-warning" role="alert" markdown="1">

Le BA est une approche non-lineaire de resolution par moindres carres:
- $\bar x_{ij} + \hat e_{x_{ij}} = \lambda_{ij}P_{ij}\bar X_i$
- Avec $\hat e_{x_{ij}}$ l'erreur de mesure du point $\bar X_i$
- $i l'indice du point, $j$ l'indice de la camera

</div>

Elimination du facteur d'echelle:
- $\bar x_{ij} + \hat e_{x_{ij}} = \frac{P_{1:2_{ij}}\bar X_i}{P_{3_{ij}}\bar X_i}$
- Resolution par SVD

## Odometrie Visuelle

<div class="alert alert-info" role="alert" markdown="1">
Estimation du mouvement de la camera par rapport au monde
</div>

Necessaire a de nombreuses applications
- Pas de GPS
    - Genre sur Mars
- IMU et/ou odometrie des roues insuffisants
    - On va mettre des encodeurs sur les roues et lire de combien s'est deplace la roue

Odometrie:
- Estimation du mouvement base sur le modele cinematique
- Extansion a la vision

Triangulation
- Permet de connaitre la position 3D d'un point

![](https://i.imgur.com/vrUQGxx.png)

<div class="alert alert-danger" role="alert" markdown="1">

Principe:
- Trouver des correspondances de points entre 2 images successives: utilisation de descripteurs
- Si le monde est statique et les points bien apparies alors on peut estimer la transformation $(R,t)$ a partir des parametres extrinseque
- Probleme de minimisation de l'erreur de reprojection
    - Necessite d'une bonne calibration

</div>

<div class="alert alert-warning" role="alert" markdown="1">

Peu robuste aux rotations pures
- On compense ave l'IMU et l'odometrie des roues

</div>

Pseudo code:

```
Capturer l'image I_k
Calculer les correspondannce entre I_k-1 et I_k
Calcul de la matrice essentielle E et que p^TEp' = 0
Decomposition de E en R_k et t_k par SVD
Calcul du modele 3D (coordonnees des points de correspondance)
Redimensionnement de t_k pour prendre en compte l'echelle
    Attention ! p^TEp' = 0 <=> lambda p^TEp'=0
k = k + 1
```

## SLAM

<div class="alert alert-info" role="alert" markdown="1">
Simultaneous Localization and Mapping
</div>

- Si une carte est fournie, possibilite de se localiser dans cette carte uniquement
- Si une position est fournie, possibilite de creer une carte de l'environnement
- Le SLAM est l'estimation conjointe d'une carte de l'environnement et de la position de la camera dans cette carte
- Necessaire des qu'un robot doit explorer un environnement totalement ou partiellement inconnu
- Amelioration de l'odometrie visuelle
- On sauvegarde les coordonnees des points 3D extraits et de leurs caracteristiques locales
- Creation d'une carte de features 3D

![](https://i.imgur.com/FLT34Uv.png)

3 categories principales de methodes pour l'estimation de l'etat:
- Extended Kalman Filter
- Particle Filter
- Least Squares => Graph-based SLAM

Graph-based SLAM
- Utilisation d'un graphe pour representer les variables et les relations entre ces variables
- Pose Graph: contient uniquement les positions
- Factor Graph: contient des facteurs reliant les differentes variables

Pose Graph:
- Chaque noeud represente une pose
- Les liaisons entre ces noeuds contiennent leur relation spatiale
- L'optimisation essaye de trouver la position optimale d'un noeud qui minimise l'erreur introduite dans les liaisons

![](https://i.imgur.com/Fu6J4Sf.png)

*Quels sont les avantages ?*
- Meilleure estimation des coordonnees 3D des points/features
- Fermeture de boucles (Loop-closure)
- Plus robuste face aux rotations pures

![](https://i.imgur.com/i5zUBRl.png)
