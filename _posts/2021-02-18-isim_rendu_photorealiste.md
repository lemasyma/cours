---
title:          "ISIM: Rendu photorealiste"
date:           2021-02-18 11:00
categories:     [Image S8, ISIM]
tags:           [Image, ISIM, S8]
description: Rendu photorealiste
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/B1ArmjAZd)

# Rendu photorealiste
- Objectif
    - Generation d'images realistes
    - Contrainte de temps faible
- Strategies:
    - *Object-based rendering algorithms*
        - Illumination globale calculee independamment du point de vue
    - *Image-based rendering algorithms*
        - Illumination calculee partiellement, en fonction du point de vue
    - *Deterministic rendering algorithms*
    - *Monte Carlo rendering algorithms*

Les algorithmes qu'on va voir:
- *Raytracing*
- *Path Tracing* et *Bidirectional Path Tracing*
- ...
- *Radiosity*
- *Photon map*
- ...

## Formation de l'image
![](https://i.imgur.com/YDac3hp.png)

Capture de l'image:
![](https://i.imgur.com/ThOipDA.png)

Modele stenope:
![](https://i.imgur.com/UxIqt6u.png)

Capture de l'image (capteur CCD, CMOS)
![](https://i.imgur.com/oU3fnMK.png)

Dans notre cas nous pouvons faire passer des rayons avec differentes longueurs d'onde par le meme point

- On peut facilement modeliser la camera
- Il faut reussir a modeliser l'eclairage
    - Idee: "suivre" les rayons lumineux pour trouver le chemin parcouru depuis la source jusqu'a l'oeil
    - Principe: Lancer une "infinite" de rayons depuis la source pour esperer trouver ceux qui frappent l'oeil de l'observateur


    ![](https://i.imgur.com/u5AIs7n.png)

<div class="alert alert-danger" role="alert" markdown="1">
**C'est tres lourd!**
</div>

# *Raytracing*
- Historique
    - 68, Appel (du *raycasting*?)
    - 80, Whitted (ajoute les effets optiques: reflexion, transparence...)
- Principe
    - Idee de base: Difficile de suivre tous les rayons partant de la source en revanche il est possible d'estimer le chemin inverse
    - Faire le chemin inverse pour trouver les objets "vus"

    ![](https://i.imgur.com/QCgbVmI.png)
    - Pour chaque objet vu, on peut estimer une approximation de l'eclairage local

    ![](https://i.imgur.com/xZfqw1g.png)
    - Approximation de 2 types de contributions:
        - la partie diffuse
        - la partie speculaire
    
    ![](https://i.imgur.com/dmhqtns.png)

<div class="alert alert-danger" role="alert" markdown="1">
Calcul de l'illumination locale:
- Composante diffuse
- Composante speculaire
- Apport des sources primaires
- Apport des sources secondaires
</div>

<div class="alert alert-info" role="alert" markdown="1">
Sources primaires:
- Lumieres ponctuelles
- Spots
- Lumieres directionnelles
- Objets lumineux

![](https://i.imgur.com/8RtKZJs.png)
</div>

<div class="alert alert-info" role="alert" markdown="1">
Sources secondaires:
- Les autres objets eclaires
</div>

<div class="alert alert-danger" role="alert" markdown="1">
Modele local:
![](https://i.imgur.com/NCy2shH.png)
</div>

## La composante diffuse
- La propriete de diffusion de la surface est $k_d$
- La couleur de la surface est $C$

![](https://i.imgur.com/F0xmhP3.png)

Voila ce que ca donne:
![](https://i.imgur.com/R8QpXSW.png)

> "Mais vous avez triche monsieur il y a des ombres !"

<div class="alert alert-success" role="alert" markdown="1">
C'est faux, il faut regarder l'effet de degrade: c'est la lumiere diffusante.
</div>

## La composante speculaire
- La propriete de reflexion de la surface est $k_s$
- L'intensite de la lumiere depend de l'angle fait par $S$ et $L$

![](https://i.imgur.com/0y7v1Bz.png)

On a en resultat:
![](https://i.imgur.com/oZRUdW9.png)

<div class="alert alert-success" role="alert" markdown="1">
La lumiere est blanche donc on a un reflet blanc sur les objets.
</div>

Il y a un coefficient de brillance, la tache speculaire est plus ou moins piquee (ex: la lumiere dans les yeux des gens)

![](https://i.imgur.com/j2o2suO.png)

<div class="alert alert-info" role="alert" markdown="1">
![](https://i.imgur.com/fMvghzU.png)
- Les "$k_d$" incluent la couleur ![](https://i.imgur.com/9vH2NkM.png)

- Il faut sommer toutes les sources lumineuse $i$...
</div>

Resultat:
![](https://i.imgur.com/H1yvpLh.png)

> Encore une fois je triche comme un arracheur de dent car je n'ai pas explique comment avoir l'ombre, normalement ca devrait etre le degrade du bleu.

*Est-ce qu'on peut affiner ce modele ?*
- On peut ajouter un coeff d'attenuation $f(d)$ ($d$ $\rightarrow$ distance)
    - Estimer que ce n'est pas un rayon qui repart mais un cone ![](https://i.imgur.com/LkIoVPi.png)
    - $f(d) = 1/d$
    - $f(d) = 1/d^2$
    - $f(d) = 1/(d + k)$
    - ...

*Quel modele de couleur prendre ?*
Une synthese additive RVB.

## Algorithme
### Etape 1: Prise en compte des sources primaires
Pour l'ensemble des points de l''image:
1. Calculer le vecteur directeur du rayon lumineux $v$ partant de l'observateur
2. Chercher les intersections de ce rayon lumineux avec l'integralite des objets de la scene et garder le plus proche
3. Calculer le niveau d'eclairement au point d'intersection en sommant l'apport diffus et speculaire pour chaque source lumineuse

<div class="alert alert-warning" role="alert" markdown="1">
Problemes:
- Ne tient pas compte des sources lumineuses secondaire
- Ne gere pas les **ombres**
</div>

### Prise en compte des sources secondaires:
![](https://i.imgur.com/0Li6M3O.png)

On ne considere pas tous les points de toutes les surfaces de l'espace, par contre on va aller explorer la direction du rayon rebondissant sur la table.
Pour y arriver, on calcule l'illumination au point sur la table, rien nous empeche de "relancer" un rayon et voir quel objet on intersecte. Une fois qu'on l'intersecte, on calcul l'illumination au point.

<div class="alert alert-danger" role="alert" markdown="1">
C'est du **cast ray**.
</div>

![](https://i.imgur.com/bmVzbc7.png)
> La reponse "lancer plus de rayon" ca fonctionne.

### Etape 2: Prise en compte des sources primaitres et certaines sources secondaire
Pour l'ensemble des points de l'image:
1. Calculer le vecteur directeur du rayon lumineux $v$ partant de l'observateur
2. Chercher les intersections de ce rayon lumineux avec l'integralite des objets de la scene et garder le plus proche
3. Relancer un rayon dans la direction de $S$ puis calculer le niveau d'eclairement recursivement
4. Calculer le niveau d'eclairement au point d'intersection en sommant l'apport diffus et speculaire pour chaque source lumineuse ainsi que l'eclairement dans la direction de $S$

### Etape 3: Prise en compte de l'ombre
Pour l'ensemble des rayons que l'on "lance" vers les sources primaires, il faut chercher si un objet de la scene ne s'est pas insere entre le point considere et la source. Pour cela, il faut a nouveau calculer l'intersection du rayon avec l'ensemble des objets de la scene et prendre le plus proche.

### Resultats
![](https://i.imgur.com/xmqQygZ.png)

> Je triche plus (ou quasiment plus)

![](https://i.imgur.com/16q30Sm.png)
> Je triche j'ai pas du tout parle de texture et d'anti-aliasing

<div class="alert alert-info" role="alert" markdown="1">
- L'algorithme du *raytracing* est un processus simple, recursif
- Il faut etre capable, pour chaque objet, de calculer la normale en chaque point
- Il faut reflechir a la condition d'arret
</div>

## Avantages
- Algorithme simple et rapide a mettre en oeuvre
- Genere des images honorables
- ...

## Inconvenients
- Temps de calcul un peu eleve
- Pas de gestion de la profondeur de champ et autres effets
- Mauvaise gestion des ombres (frontieres trop brutales)
- Sources secondaire pas suffisamment prises en compte (eclairage indirect incorrect)
- Objets transparents
- "*Alisaing*"
- ...


# Les problemes du *Raytracing*
## Probleme de l'*aliasing*
<div class="alert alert-warning" role="alert" markdown="1">
**Probleme**: si on lance un rayon c'est *touche* ou pas *touche* alors que ca devrait etre la *proportion* de chaque.
![](https://i.imgur.com/ygeEvTt.png)

</div>

On risque aussi de louper les petits objets.

### Solution
<div class="alert alert-success" role="alert" markdown="1">
On lance plus de rayons (*cast ray*)!
</div>
- Sur-echantillonage
    - Lancer plusieurs rayons pour chaque pixel
        - De maniere organisee
        - Au hasard
    - Lancer plusieurs rayons pour chaque pixel ou le gradient est eleve
        - Bon resultats mais peut etre tres lent
- Post-filtrage
    - Resultat moyen mais tres rapide

### Resultats 
Avec anti-alisaing sur toute l'image (50 rays/pixel)
temps: de l'ordre de 7-8 secondes
![](https://i.imgur.com/P9rcCEk.png)

Anti-aliasing sur les zones de gradient eleve (50 rays/pixel)
Temps: l'ordre de la seconde
![](https://i.imgur.com/9nV5KXr.png)

## Probleme du temps de calcul
<div class="alert alert-success" role="alert" markdown="1">
On lance plus de rayons (*cast ray*)!
</div>
Solutions:
- Volumes englobants
- Projection sur un plan/partition de l'espace
- Pre-trier les objets?
- Calcul parallele
- Utilisation d'OpenGL
- ...

## Probleme des objets transparents
Solutions:
- Comme nous avons relance le rayon reflechi, il faut "suivre" le rayon refracte
    - Loi de la refraction
- Tenir compte du rayon refracte pour l'illumination locale: $I=I_d+I_s+I_s+k_tT$

### Milieux transparents:
- Loi de la refraction (Snell Descartes): $n_1\sin i_1 = n_2\sin i_2$
![](https://i.imgur.com/7qJMKya.png)

### Surfaces translucides:
- Distribution probabiliste
![](https://i.imgur.com/Jo7fLhV.png)

### Calcul de l'ombre
<div class="alert alert-success" role="alert" markdown="1">
Solution approchee:
Ne pas devier le rayon mais filtrer les longueurs d'ondes
![](https://i.imgur.com/OGzeRRk.png)

</div>

## Probleme de l'eclairage indirect
Si on va sous notre bureau, d'apres nos calculs il devrait faire totalement noir alors que ce n'est pas le cas avec l'eclairage indirect.
![](https://i.imgur.com/2fMo5eh.png)

### Solution
- Ajouter une lumiere ambiante: $I=k_a*I_a+I_d+I_r+I_t$
- Solution vraiment approximative

Resultats:
![](https://i.imgur.com/oAKQQvQ.png)

## Probleme de l'ombre
On lance un rayon pour savoir si on est eclaire mais ca donne une reponse binaire, c'est comme considerer la source comme **ponctuelle**.
<div class="alert alert-warning" role="alert" markdown="1">
Notre source lumineuse **n'est pas ponctuelle**.
</div>
*Quel est la proportion de notre source ?*
*Comment faire pour avoir des ombres plus douces ?*

### Solution
<div class="alert alert-success" role="alert" markdown="1">
Cast ray !
</div>
- Ne plus considerer une lumiere comme ponctuelle
    - Probleme de temps de calcul

# Bilan
## Avantages
- Algorithme tres simple
- Donne des images honorables

## Des problemes majeurs persistent
- Les sources secondaires ne sont pas suffisamment bien geres
- Les objets transparents non plus

## Amelioration
- Raytracing distrubue (84)
    - Sur-echantillonnage pour simuler
    - les ombres douces
    - la profondeur de champ
    - ...
    - Ne regle pas le probleme de l'apport de la diffusion des sources secondaires
    - Quantite de calcul enorme

## Conclusion
- Algorithme simple
- Necessite beaucoup d'ameliorations pour avoir des images photorealistes