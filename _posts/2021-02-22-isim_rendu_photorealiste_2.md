---
title:          "ISIM: Rendu photorealiste 2"
date:           2021-02-22 11:00
categories:     [Image S8, ISIM]
tags:           [Image, ISIM, S8]
description: Rendu photorealiste
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/rkloGbZzd)

# La Radiosite
On essaye d'estimer la "*radiosite*" de chaque element de la scene, c'est a dire la quantite d'energie de chaque element emet...

- B_i$ la radiosite de la surface $i$
- $E_i$ la quantite de lumiere emise par la surface $i$
- $P_i$ la fraction de lumiere incidente qui est reflechie par la surface $i$
- $F_{ij}$ la fraction de lumiere quittant la surface $i$ et atteignant la surface $j$

$$
B_i = E_i + P_i\sum_i(F_{ij}B_j)
$$

Calcul des $F_{ij}$ par hemi-cubes
![](https://i.imgur.com/QgIzg0e.png)
On projet un triangle, la partie bleue est la projection de ce triangle.
<div class="alert alert-success" role="alert" markdown="1">
Cela nous donne le niveau d'energie recue par "petits carres".
</div>

![](https://i.imgur.com/APbob5E.png)

<div class="alert alert-warning" role="alert" markdown="1">
Ne permet pas directement de calculer une vue de la scene mais simplement l'illumination globale
</div>
- Avantages:
    - Prend mieux en compte les sources secondaires
    - Calculee une fois pour toutes
- Inconvenients
    - Tient compte de la diffusion
    - Assez lourd
    - Obligation d'avoir un maillage (il faut discretiser les surfaces)
    - Objets transparents ?

# *Photon map*
<div class="alert alert-info" role="alert" markdown="1">
- Pre-calcul de l'illumination de la scene
- Lancement des rayons lumineux depuis les sources et calcul des accumulations des photons
</div>
- Avantages:
    - Permet de modeliser plus proprement les sources secondaires, les ombres portees (...) et surtout les objets transparents (caustiques)
        - Faire des ombres correctes sous les objets transparents
- Inconvenients
    - Calculs
    - Complexite
    - Penible a coder

Resultats: video manquante :(

Ameliorations:
- Projection Maps
- Visual importance map (3-pass Technique)
- Shadow photons
- ...

# *Path Tracing/Bidirectional Path Tracing*
- Modelisation des proprietes de reflexion des surfaces: (Bidirectional reflectance distribution function BRDF) (idem pour la transmission)
    - Si on a une surface et qu'on lance un laser, qu'elle est l'energie ressortante en fonction de l'angle d'incidence?
- Solution pour resoudre l'illumination

<div class="alert alert-info" role="alert" markdown="1">
BRDF: Biderectional reflectance distribution function (Reflectivite bidirectionnelle)
![](https://i.imgur.com/iz40gTo.png)
</div>
Conservative:
$$
\int f_r(x,\theta,\theta_o)L_{input}(x, \theta_i)\vert\theta_i.N_x\vert\delta w_0\le 1
$$
Reciprocite de Helmholtz:
$$
f_r(x, \theta_i, \theta_o) = f_r(x,\theta_o^{-1}, \theta_i^{-1})
$$

- Mesuree
    - Goniophotometer
    - ...
- Modele
    - Blinn-Phong
    - Cook-Torrance
    - GGX
    - ...

Principe du rendu:
![](https://i.imgur.com/vgBHuLT.png)

![](https://i.imgur.com/e460Nwq.png)

## *Path Tracing*
- Avantages:
    - Rendu realiste
    - Convient bien aux scenes d'exterieurs
    - Prend bien en compte l'apport des autres objets
    - Rend les caustiques
    - Possibilite de modeliser les effets (profondeur de champ...)
- Inconvenients:
    - len
    - bruite (Il faut bcp d'iterations pour converger)
    - difficile pour scenes avec des petites sources lumineuse (ou sources cachees)

## Bidirection Path Tracing
<div class="alert alert-success" role="alert" markdown="1">
Amelioration du calcul du rendu
- Lancement des rayons depuis l'observateur et depuis les sources
</div>

![](https://i.imgur.comcO43q6.png)
Avantages:
- Facilite la recherche du chemin vers la source lumineuse
- Permet de modeliser les petites sources lumineuses

# *PBGI*: Point-Based Global Illumination
- Tres peu enseigne
- Beaucoup utilise dans l'industrie du cinema
    - *Monster Academy*: 1er long-metrage en raytracing
    - *La-haut*: utiliser PBGI
    - *SFX de Pirates des Caraibes* avec PBGI

<div class="alert alert-info" role="alert" markdown="1">
Methode pour estimer l'illumination globales
</div>
- Avantages:
    - Rapide
    - Image non bruitee (*pas d'artefacts temporel*)
- Inconvenients
    - Pas aussi precis que le *raytracing*
    - Difficile de gerer les effets miroir

<div class="alert alert-success" role="alert" markdown="1">
Approximation de la scene par nuage de points
- Un point - un disque de couleur
- Calcul de l'illumination direct de la scene

![](https://i.imgur.com/PTti6X4.png)

</div>
- Approximation de la scene par nuage de points
    - Un point = un disque de couleur
    - Calcul de l'illumination directe de la scene

![](https://i.imgur.com/Pue2PMH.png)
<div class="alert alert-danger" role="alert" markdown="1">
**Regroupement des points**
</div>
Calcul de l'illumiantion globale
- Calcul de la contribution des points sur un disque
    - Pour les points eloignes
        - Utilisation du cluster
    - Pour les points proches
        - Raytracing
    - Pour les autres points
        - Utilisation directe du disque

![](https://i.imgur.comFbMjm5.png)



# Bilan et remarques
## Rendus
Rendu simple
![](https://i.imgur.com/IRWfVp1.png)


Rendu simple avec anti-aliasing
![](https://i.imgur.com/EuVak4o.png)

Rendu avec la radiosite
![](https://i.imgur.com/DpeSYc3.png)

Rendu avec les photons
![](https://i.imgur.com/gf5sKoA.png)

Rendu avec la radiosite et les photons
![](https://i.imgur.com/X29fpso.png)


Rendu avec anti-aliasing
![](https://i.imgur.com/ei34Jje.png)

## Bilan
- Raytracing
    - Calcul de l'illumination en fonction d'un point de vue
    - Calcul l'illumination approximatif : gère mal les objets transparents, les lumières secondaires, les ombres portées...
    - On peut combiner cet algorithme avec des techniques de calcul d'illumination globale pour palier à ces problèmes
- Radiosity
    - Calcul l'illumination globale
    - Gère que la diffusion mais améliore l'apport des lumières secondaires
- PhotonMap
    - Calcul l'illumination globale
    - Plus diffcile à mettre en ÷uvre (implémentation, artéfacts...)
    - Gère bien les objets transparents (caustiques) et éventuellement les ombres portées et les sources secondaires
- PathTracing
    - Gère bien les objets transparents, les lumières secondaires, les ombres portées
    - Calcul très long
    - Risque d'apparition de bruit
- PBGI

## Remarques sur l'implementation
- Doit être bien réfléchie
- Parallélisation possible
- Utilisation du GPU possible
- ...

## Modelisation
Pour chaque "forme" il faut être capable de:
- calculer la normale en chaque point
- calculer l'intersection avec une droite,
- éventuellement calculer les coordonnées de la texture

*Calcul des intersections : dans le repère monde ou le repère
objet ?*

## Pour aller plus loin
- Textures
- Autres effets (Brouillard, Bleu atmosphérique, ...)
- ...
- génération d'anaglyphes (cyan et rouge (espacement $\frac{1}{30} ∗ f$ ))

![](https://i.imgur.com/oNNnUh8.png)

# Post scriptum
## Raycasting
<div class="alert alert-info" role="alert" markdown="1">
*Principe*: On ne lance que les rayons depuis l'observateur et on ne calcul
pas les rebonds...
</div>
*(Raytracing est une extension du raycasting ?)*

Wolfstein:
- On lance des rayons dans le plan!

![](https://i.imgur.com/4XDr8cR.png)

![](https://i.imgur.com/fnRUjtf.png)

La longueur du rayon permet de conclure sur la hauteur du mur
- 1 rayon donne 1 colonne de l'image + gestion des objets

Avanatages:
- Algorithme rapide

<div class="alert alert-warning" role="alert" markdown="1">
On est loin du rendu photoréaliste...
</div>