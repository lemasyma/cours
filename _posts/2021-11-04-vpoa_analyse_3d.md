---
title:          "VPOA: Analyse de l'environnement 3D"
date:           2021-11-04 09:00
categories:     [Image S9, VPOA]
tags:           [Image, S9, VPOA]
math: true
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/rkmnVzWvt)

# Introduction

On sait obtenir de l'info en 3D sous la forme d'un nuage de points (sous forme de nuage de points, carte de disparite).

*Comment valoriser cette donnee ?*
> On peut se localiser
> Detection d'objets

- Visualisation 3D
- Reconstruction de modele 3D
- Building Information Modeling
- Clustering 3D
- Dimensionnement 3D
- Detection d'objets 3D
- Modele numerique de terrain
- Navigation autonome
- etc

*Comment passer d'un nuage de points a une donnee a valeur ajoutee ?*
- Analyse 3D
- Segementation
- Recalage


# Analyse de Surface et Reconstruction 3D

## Segmentation semantique

![](https://i.imgur.com/J6bqpe0.jpg)

<div class="alert alert-info" role="alert" markdown="1">
But: 
1. segmenter en temps reel tous les points
2. segmenter toutes les donnees accumulees
</div>

<div class="alert alert-success" role="alert" markdown="1">
Utile pour les vehicules autonomes
</div>

## Reconstruction 2D

Exemple de problematique en 2D:

![](https://i.imgur.com/4yN6gc5.png)

<div class="alert alert-warning" role="alert" markdown="1">
Dans la realite, le probleme n'est pas si simple

![](https://i.imgur.com/oRTrKoM.png)

</div>

### Extraction de la surface

- Discretisation Octree (1 point par cellule)

![](https://i.imgur.com/8uYVrOa.png)

- Calcul d'un champ de vecteurs

![](https://i.imgur.com/6jWNHUN.png)

- Calcul de la fonction indicatrice

![](https://i.imgur.com/R2VgmMb.png)

- Extraction de l'isosurface

![](https://i.imgur.com/g0T9prk.png)


## Reconstruction 3D

<div class="alert alert-success" role="alert" markdown="1">

En 3D, ca donne:

![](https://i.imgur.com/EKBavSc.png)

</div>

### Voxelisation

Differentes methodes de voxelisation

![](https://i.imgur.com/jkwk163.png)

### Maillage

Ensemble de sommets connectes

![](https://i.imgur.com/QGpjqMc.png)

## Analyse de surface

![](https://i.imgur.com/l4raMJT.png)

Calculs de normales par ACP:
- On cherche le meilleur plan approche dans le voisinage d'un point $X_{i0}$
    - Les points du voisinage sont notes $X_i$
- Equation d'un plan $n^tX=d, \Vert n\Vert =1$
- Distance signee d'un point au plan: $d(X_i, P) = n^tX_i-d$

![](https://i.imgur.com/1Ahgpob.png)

### Resolution

- Methode des moindres carres
- Resolution de l'equation de minimisation pour le plan

Fonction a minimiser: $f(n,d)=\sum_{i=1}^m(n^tX_i-d)^2$

On pose:
- Barycentre des points $G=\frac{1}{}$
- Matrice de covariance des points

TODO

Le meilleur plan approche est defini par:
- Normale $n_{min}$
    - Vecteur propre norme associe a la plus petite valeur propre de $M_{cov}$
    - NB: indetermine a un changement de sens pres
- Distance $d_{min}$
    - $d_{min}=n^tG$

<div class="alert alert-success" role="alert" markdown="1">
La solution fait appel a l'analyse des directions principales de la matrice de covariance: **Analyse en Composantes Principales (ACP)**
</div>

# Segmentation 3D

<div class="alert alert-info" role="alert" markdown="1">
**Definition**

*Subdiviser (partitionner)* le nuage de points 3D en sous-ensembles connexes correspondants a des modeles simples

![](https://i.imgur.com/UNzJxk1.png)

</div>

## Methodes de segmentation

![](https://i.imgur.com/jiDVe8U.png)

## Croissance de surface

<div class="alert alert-info" role="alert" markdown="1">
**Principe**

- A partir de "surfaces germes" ou "graines" (seed surfaces) dans le nuage de point
- Agregation progressive des points voisins appartenant a la meme surface

</div>

> **Remarque**: extension de l'algorithme "croissance de regions" pour les images

Pour chaque point, un calcul de la normale du plan dans un voisinage:

![](https://i.imgur.com/NbR8Oaq.png)

Critere d'agregation:
- Co-normalite: $\alpha = \arccos(n_1, n_2)\le \alpha_{seuil}$
    - Normales dans le meme sens
- Coplanarite: $d=\max(\vert r_{12}\cdot n_1\vert, \vert r_{12}\cdot n_2\vert) \le d_{seuil}$
    - Points sur le meme plan

![](https://i.imgur.com/MkGWlA1.png)

## Clustering

<div class="alert alert-info" role="alert" markdown="1">
**Definition**

Regroupement de donnees en paquets homogenes selon des caracteristiques commnunes

</div>

### DBSCAN

<div class="alert alert-info" role="alert" markdown="1">
C'est l'un des algorithme de clustering les plus repandus
</div>

Principe:
- Choix d'un point graine pour la region
- Identification des voisins du point
- Pour chaque point voisin
    - Si la densite locale de points est suffisante, ajout a la region
    - Sinon, labellisation en tant que bruit
- On continue jusqu'a ne plus pouvoir etendre la region

On peut jouer sur 2 parametres:
- Le rayon de recherche des voisins
- La quantite minimale de voisin ou densite

## RANSAC

<div class="alert alert-info" role="alert" markdown="1">
**RANdom SAmple Consensus**
</div>

Methode de vote sur des echantillons aleatoires de surfaces
- Echantillons calcules a partir du nombre minimal de points necessaires pour definir la surface(quorum)
- Vote: un TODO

Primitives geometriques et quorum de points:
- Droite: 
    - Quorum = 2 points non alignes
- Plan:
    - Quorum = 3 points $x_i$ non alignes
    - TODO

Vote:
- Nombre de points compris dans un espace a une certaine distance $\delta$ de la surface calculee

![](https://i.imgur.com/B0rYPno.png)

Probabilites:
- Hypotheses
    - Plusieurs surfaces possibles, points non bruites
    - $N$ points dans le nuage de points
    - $n$ points appartiennet a la surface recherchee
    - $q$ points pour definir la surface (quorum)
TODO

Nombre de tirages necessaires:
- Nombre de tirage aleatoires $T_{min}$ necessaires pour avoir une probabilite $p_t$ de trouver une surface d'au moins $n_{min}$ points

$$
T_{min} = \frac{\log(1-p_t)}{\log(1-(\frac{n_{min}}{N})^q)}
$$

- En supposant $n_{min}\lt\lt N:T_{min}\simeq \log(\frac{1}{1-p_t})$ TODO

## Hough 3D

Principe:
- Methode de vote dans l'espace dicre

TODO

Detection de droites

![](https://i.imgur.com/DdaIdw7.png)


TODO
Probleme

## Deep learning

![](https://i.imgur.com/qkNT4H6.png)

# Recalage 3D

Point Set Registration, Point Matching:
- Processus d'alignement de jeux de points TODO

## Iterative Closest Point

<div class="alert alert-info" role="alert" markdown="1">
**ICP**

Determination de la transformation rigide $(R,t)$ entre les deux nuages de points

</div>

Principe
- Appariement des points du nuage a recaler au point le plus proche dans l'autre nuage (approche de "nearest neighbor")
- Calcul de la transformation $(R,t)$ qui minimise la distance entre ces points

![](https://i.imgur.com/1QuMGjy.png)

### Calcul de la transformation $(R,t)$

Resolution par la methode des moindres carres:

On calcule:

$$
f(R,t) = \sum_{i=1}^n\Vert p_i-(R\cdot p_i'+t)\Vert^2\\
f:\begin{cases}
SE^3&\to \mathbb R^+\\
(R,t)&\mapsto f(R,t)
\end{cases}
$$

On cherche: $(R,t)$ tel que $(R, t)=\text{arg}\min_{R,t}f(R,t)$

Solution par decomposition

TODO

Resolution par Singular Value Decomposition (SVD)
- Entree: jeux de points $(P,P')$
- sortie: Matrice de rotation $R$, vecteur translation $t$
- Algorithme
    - Determiner les barycentres $p_m=\frac{1}{n}\sum_{i=1}^n$ et $p_m'$
    - Calculer la matrice $H$
    - Decomposer $H$ en valeurs singulieres $\exists(U, V, \Sigma)$ TODO
    - Calculer $R=VU^T$ et $t=p_m-p_m'$

Pseudo code ICP:

```
Recalage approximatif P'->P
Repeter:
    - Association de donnees P' -> P
    - Calcul de la transformation (R, t)
    - Application de la transformation au nuage de point P'
    - Calcul de la distance entre les nuages
Tant que:
    - Distance normalisee > seuil
    - Et nombre d'iterations < maximum d'iterations
```

Temps de calcul:
- Appariement en $O(n_1, n_2)$, le reste en $O(n_1 + n_2)$
- Acceptable pour les petits nuages de points, trop lent pour de gros nuages de points
- Necessite de sous-enchatilloner
- Possibilite d'acceleration avec ANN (Approximate Nearest Neighbor): $O(n_1\log(n_2))$

Approximate Nearest Neighbor (ANN)
- Principe
    - Pre-calcul d'un kd-tree pour partitionner l'espace
    - Recherche dichotomique avec distance seuil

![](https://i.imgur.com/dxLcs9v.png)


Variante ICP:
- Metrique point a plan (point to plane)
- Echantillonage: regulier, aleatoire, base sur les normales
- Rejection des outliers
- ...

![](https://i.imgur.com/HEr3LzD.png)

