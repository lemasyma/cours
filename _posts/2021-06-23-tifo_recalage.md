---
title:          "TIFO: Cours recalage"
date:           2021-06-23 9:00
categories:     [Image S8, TIFO]
tags:           [Image, TIFO, S8, recalage]
description: Recalage d'images
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/ByK2KPghO)

*Comment extraire une frequence cardiaque quand on a une oscillation ?*

<div class="alert alert-success" role="alert" markdown="1">
Stabiliser l'image
</div>

<div class="alert alert-warning" role="alert" markdown="1">
Quand on fait du recalage, on fait des estimations donc par moment l'image "vibre"
</div>

La video recalee est plus petite car on prend la plus grande translation de chaque cote.

# Context
## An example

![](https://i.imgur.com/4SPNP2p.png)
> Ptit poisson, grozyeux

## General principle

<div class="alert alert-info" role="alert" markdown="1">
**What is the transformation between 2 frames ?**
For 2 frames $I_2$ and $I_2$, Find $\mathcal T$ to minimize

$$
\mathcal V = Variance(I_1,\mathcal T(I_2))
$$
</div>

![](https://i.imgur.com/PyK8VxI.png)
> Hyper important de verifier 

### 2 frames

<div class="alert alert-info" role="alert" markdown="1">
The **reference frame** ($I_1$ in our presentation) is the frame we will not modify, considered as the "true" image
</div>

<div class="alert alert-info" role="alert" markdown="1">
The **studied frame** ($I_2$ in our presentation) is the frame we try to minimize $\mathcal V$
</div>

## Model

Choixe of the model to have the best estimation:
- Fourier domain
- Image
- Graph
- Multi-modality
    - Un peu complique

## Usual transformations
### Rigid transformation

<div class="alert alert-info" role="alert" markdown="1">
Transfo rigide: on ne change pas la structure (les distances) dans l'image
</div>

![](https://i.imgur.com/mmsfCLe.png)

![](https://i.imgur.com/eUyp3U1.png)

### Non-rigid transformation

![](https://i.imgur.com/TyLgGTV.png)

<div class="alert alert-warning" role="alert" markdown="1">
On ne veut surtout pas faire de transformation non-rigide
</div>

*Pourquoi ?*
On risque de creer des deformations locales (dans notre exemple: corriger le mouvement du coeur)

## Transformation estimation

Classical estimation for the entire image analysis:

$$
\mathcal T = (\mathcal R, T)
$$

with:

$$
\mathcal R=
\begin{pmatrix}
\alpha a &\alpha b\\
\alpha c&\alpha d
\end{pmatrix} = \alpha\mathcal R'\\
T=(d_x, d_y)
$$

Case of $\mathcal R$:

If there is a rotation:

$$
\mathcal R=
\begin{pmatrix}
\alpha \cos(\theta) &-\alpha \sin(\theta)\\
\alpha \sin(\theta)&\alpha \cos(\theta)
\end{pmatrix} = \alpha\mathcal R'
$$

$\alpha$ is the scale factor

$$
(I_2\mathcal R+T)-I_1 = min(\mathcal V)\\
S = \mathcal T(I_2)=(I_2\mathcal R + T)\\
\forall (x,y)\in I_2: S(x,y)=I_2(x',y')
$$

with the estimated $\mathcal R$ and $T$, $[x'\quad y']=[x\quad y]\mathcal R+T$

# Key-points
## Principle

<div class="alert alert-info" role="alert" markdown="1">
**Objectives**
- Points which are interesting $I_1$
- Find their equivalent in $I_2$
- Estimate the transform between the 2 sets of points

We want to solve

$$
P_2=P_2\times\mathcal R+\mathcal T
$$

Where $P_1$ and $P_2$ are the sets of points of the 2 frames we seek to match, $\mathcal R$ is the "rotation" matrix. $\mathcal T=(d_x, d_y)$ is the translation

![](https://i.imgur.com/zOWctul.png)

</div>

## The solution

![](https://i.imgur.com/eHWydO2.png)

<div class="alert alert-warning" role="alert" markdown="1">
En fonction de la version d'OpenCV il peut y avoir un soucis avec la matrice $\mathcal M$ (elle peut etre $3\times 3$ au lieu de $2\times 3$)
</div>

# Applications
- Sequence stabilization
- Reconstruction
- Optical flow
- Similarity
- Comparison (evolution of a tumor etc.)

# Recalage
## keuwa ?

Deux images $S$ et $C$: cherche $T$ tel que $T(S)$ ressemble a $C$

![](https://i.imgur.com/Zv11Wu0.png)

<div class="alert alert-warning" role="alert" markdown="1">
Les notations sont pourries ici
</div>

## Applications

<div class="alert alert-danger" role="alert" markdown="1">
Outil **fondamental** en analyse d'images medicales, mais pas uniquement
</div>
- Ou ailleurs en imagerie ?
- Creation d'images panoramiques
- Mosaiques
- Astronomie

![](https://i.imgur.com/4byUdS4.png)

![](https://i.imgur.com/X92xkOm.png)

<div class="alert alert-warning" role="alert" markdown="1">
On ne cherche pas sur toute l'image les points-cles, on se restreint a une certaine zone
</div>

# Systemes par mosaique

Ce type d'approche consiste a **construire les images panoramiques** a partir d'une **serie d'images** prises avec le meme systeme optique. On peut, par exemple, utiliser une camera en rotation autour de son centre optique

![](https://i.imgur.com/e80HkoG.jpg)

Evidemment, un nombre arbitraire d'images peut etre utilise

![](https://i.imgur.com/7TjXKPR.jpg)

# Exemples en imagerie medicale
## Recalage

<div class="alert alert-info" role="alert" markdown="1">
**Definition**
Consiste a trouver une transformation spatiale permettant d'aligner une image (source ou *flottante*) sur une autre (cible ou *reference*)
</div>

En anglais:
- Image registration
- Image matching

![](https://i.imgur.com/8Gls9lp.png)

Recalage monomodal ou multimodal:
- Monomodal: meme modalites
- Multimodale: modalites differentes

![](https://i.imgur.com/30MmL9b.png)

Recalage intra ou inter-sujets

![](https://i.imgur.com/PeiG4PG.png)

![](https://i.imgur.com/fkeKaqc.png)

## Exemples
### Intra-patient, mono-modalite

Exemple: evolution de lesions (images IRM d'un patient atteint de SEP a quelques mois d'intervalle)

![](https://i.imgur.com/TtkJtps.png)

![](https://i.imgur.com/x67f2gx.png)

<div class="alert alert-success" role="alert" markdown="1">
C'est flou !
</div>

![](https://i.imgur.com/doPu2tZ.png)

Pour trouver quelles sont les zones qui ont evolue

### Intra-patien, multi-modalite

Exemple: fusion d'informations provenant de 2 modalites differentes

![](https://i.imgur.com/VOFptBN.png)

![](https://i.imgur.com/5T5dAt7.png)

### Inter-patient, intra-modalite

Exemple: segmentation a partir d'un *atlas* anatomique

![](https://i.imgur.com/gcehBLd.png)

### Extension en 3D

![](https://i.imgur.com/I8qR34u.png)

# Recalage en imagerie medicale

Reconstruction d'un volume 3D
- A partir d'une serie de coupes 2D contigues (microscopie, epaisseur de coupe de 60nm environ)

![](https://i.imgur.com/fyowuWk.png)

![](https://i.imgur.com/vdGF95y.png)

Evolution temporelle

![](https://i.imgur.com/6Nh49NF.png)

![](https://i.imgur.com/aTQ2dhZ.png)
> Brain-shift

![](https://i.imgur.com/oLRITQ7.jpg)
> Developpement cerebral

Comparaison entre differents sujets:

![](https://i.imgur.com/juksUH9.png)

![](https://i.imgur.com/SSisOIm.png)

Fusion de modalite

![](https://i.imgur.com/xIfdwtU.png)

## Recap

![](https://i.imgur.com/1E716ks.png)

# Principe des methodes de recalage
## Critere de similarite

Supposons que l'on se donne un critere de similarite: $Simil(I, J)$ qui mesure la "*ressemblance*" entre 2 images $I$ et $J$

![](https://i.imgur.com/zvu11al.png)

![](https://i.imgur.com/d4VueAV.png)

On choisit egalement une famille de transformation $\mathcal F$

<div class="alert alert-info" role="alert" markdown="1">
Le probleme de recalage s'ecrit alors comme:

$$
argmin_{T\in\mathcal F} Simil(T(I), J)=?
$$
</div>

## Methode de recalage

- Structures (primitives) a mettre en correspondance
- Critere de similarite
- Transformation
- Optimisation

![](https://i.imgur.com/ila1UcT.png)

## Primitives geometriques

<div class="alert alert-info" role="alert" markdown="1">
Structures particulieres dans l'image
</div>
- Points, courbes, surfaces
- Extraits automatiquement ou manuellement

![](https://i.imgur.com/APR3XM8.png)

![](https://i.imgur.com/9yZhpYk.png)

![](https://i.imgur.com/xrGUz72.png)
> Detection des primitives: ici points de forte courbure

<div class="alert alert-info" role="alert" markdown="1">
- Primitives intrinseques
- Primitives extrinseques
</div>

## Primitives intrinseques
- Structurent intrinseques au patient
- Information pertinente presente dans les 2 jeus de donnees
    - Points
    - Courbes (contours)
    - Surfaces segmenteees
    - Volumes
- Points anatomiques
    - Identifies manuellement par l'operateur
    - Isole automatiquement

## Primitives extrinseques

Reperes externes, visibles dans les 2 modalites
- fixees au patient ou a la table d'examen
- Invasifs
    - Cadre stereitaxique
    - Vis dans la boite cranienne
- Non invasifs
    - Cadre non visse
    - Moule
    - Repere colles a la peau

### Avantages
- Permet de recaler des donnees tres differentes

### Inconvenients
- Les marqueurs doivent etre positionnes avant l'acquisition
- Le recalage retrospectif n'est pas possible

Autres reperes exterenes, contention

![](https://i.imgur.com/b027zcy.png)

![](https://i.imgur.com/4n6eBeZ.jpg)

On fait des moules du patient pour faire des recalages

# Primitives

<div class="alert alert-danger" role="alert" markdown="1">
Pas de structures particulieres: tous les voxels de l'image sont utilises
</div>

# Critere de similarite

![](https://i.imgur.com/Lcn0R2n.png)

## Dependance lineaire ou affine

![](https://i.imgur.com/PWUMRMg.png)

## Coefficient de correlation

![](https://i.imgur.com/yD8rwxo.png)

![](https://i.imgur.com/GOnMKHT.png)

![](https://i.imgur.com/W0AMK4q.png)

![](https://i.imgur.com/GkLU0j3.png)

![](https://i.imgur.com/g99z6sU.png)

## Histogramme conjoint

![](https://i.imgur.com/gWr4e2U.png)

![](https://i.imgur.com/L0h7lf8.png)

<div class="alert alert-success" role="alert" markdown="1">
Quand il est parfait, on a le meme nombre de points a la meme valeur
</div>

![](https://i.imgur.com/WbR6NwD.png)

*A quel histogramme correspond les images ?*
![](https://i.imgur.com/EsAHzWj.jpg)

<div class="alert alert-success" role="alert" markdown="1">
![](https://i.imgur.com/dv0hg2P.png)

</div>

## Conservation de l'intensite - SSD

![](https://i.imgur.com/BLdkB3t.png)

## Information mutuelle

![](https://i.imgur.com/IPB4amn.png)

### Exemples

![](https://i.imgur.com/KKlajro.png)

## Sommaire

![](https://i.imgur.com/UOFnf6M.png)

# Optimisation
## Approches geometriques

![](https://i.imgur.com/wUmTVcj.png)

# Evaluation
## Evaluation qualitative

![](https://i.imgur.com/F1uX5Xx.png)

## Evaluation semi-quantitative

![](https://i.imgur.com/IgOOxLL.png)

## Evaluation quantitative

![](https://i.imgur.com/ucAPoIY.png)
