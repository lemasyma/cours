---
title:          "ISIM: Les textures"
date:           2021-03-08 11:00
categories:     [Image S8, ISIM]
tags:           [Image, ISIM, S8]
description: Les textures
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/BJT3ierQ_)

# Les textures
- Objectifs
    - Ajouter du realisme
    - Simplifier la modelisation des secenes
    - Simuler l'eclairage
- Applications
    - Algorithmes temps reels
    - Algorithmes photorealistes
- Types:
    - Textures procedurales
    - Textures plaquees
    - Effet de volume
    - Eclairage

# Les couleurs
- Associer une couleur par face
    - Effet de volume donee par l'illumination
        - Gouraud
        - Phong
- Associer une couleur par sommet
    - interpolation
- Indiquer les proprietes des materiaux
    - diffusion
    - specularite

# Les textures plaquees
- "Mapper" un bitmap sur un polygone
    - Realise
    - Consommation memoire elevee
- Comment plaquer une texture?
    - Sur un plan $\to$ facile
    - Sur une surface quelconque >
        - Trouver une fonction
        - Plaquer la texture suivant un projection simple
            - Plan
            - Sphere
            - Cylindre
            - Cube
            - ...
        - *Conformal map*
- Projection:
    - planar
    - cylindrical
    - spherical
    - triplanar

![](https://i.imgur.com/YHfuC6u.png)

- On cree un plan qu'on projette sur le theiere
- On cree un cyclindre qu'on projette sur le theiere
- On cree une sphere qu'on projette sur le theiere

Projections:
- triplanar
    - On le projette en fonction de la normale du point qu'on considere
    - Permet de dissocier les textures en fonction de l'orientation

![](https://i.imgur.com/uMtJpuj.png)

<div class="alert alert-warning" role="alert" markdown="1">
Pour un personnage (ou objet complexe), on ne trouvera pas de fonction intermediaire.
</div>
Association texture $\leftrightarrow$ model
- On decoupe soi-meme sont modele
- Voir quel est le mapping entre le modele decoupe et aplatit et le bitmap qu'on veut mapper

![](https://i.imgur.com/xI9m93P.png)
Possible d'avoir un decoupage plus "intelligent".

- *Conformal map*

![](https://i.imgur.com/Flmejhk.png)

## Origine du *Bitmap*
- Image (photo)

![](https://i.imgur.com/yTmTHZp.png)

*Est-ce qu'on peut faire des photos ou des dessins ?*
On peut peindre "comme un artiste" les surfaces 3D
![](https://i.imgur.com/dvsiCoC.png)

- Resultat d'un rendu (*render to texture*)
    - Surfaces reflechissantes

![](https://i.imgur.com/8FRHnq9.png)
> Ca va ? Pas trop le mal de mer maintenant ?


Dans ce cas on map 6 textures sur la sphere
- Change quand on bouge la camera
- Pour le rendu final on a 6 rendus intermediaires

## "Mapper" un bitmap sur un polygone
![](https://i.imgur.com/RnoootV.png)
- Interpolation dependante du $z$
- Repetition de la texture si non compris entre 0 et 1

### Textures repetitives
![](https://i.imgur.com/lutFT8R.png)

*Qu'est-ce qui se passe quand on veut faire un mur de brique ?*
- Motif repetitif
- On prend un motif qu'on duplique

|Avantages|Inconvenients|
|-|-|
|Economise de l'espace|Le motif peut devenir visible|

![](https://i.imgur.com/YpqipW0.jpg)

Pour reduire les inconvenients:
- Prendre des *patches* plus petits
- Prendre des motifs differents

![](https://i.imgur.com9xfw4e.png)

<div class="alert alert-warning" role="alert" markdown="1">
Ce n'est qu'une facon de repousser le probleme
</div>

## Mipmap
> Si on a notre mur qu'on voit de loin, plein d'artefacts apparaissent

- Le but du MIP est d'eviter la pixelisation lorsqu'on s'eloigne d'une texture
    - Le niveau de detail des textures est adapte a la distance de l'objet
    - Souvant supporte nativement par les moteurs graphiques

![](https://i.imgur.com/u0QoVOy.jpg)

- Lissage
    - Mip mapping: niveau de detail (LOD)
    - Point sampling: texel le plus proche
    - Bilineaire: interpolation sur 4 texels
    - Trilineaire: interpolation inter-LOD
    - Anisotropique: prise en compte des effets d'angle (32 texels)

![](https://i.imgur.com/KSmWmtn.png)

# Textures procedurales
- Texture generee
    - Avantages:
        - Economie de memoire
        - Pas de repetition dans le motif
        - Possibilite d'avoir une texture 3D
        - ...
- Effets classique:
    - Damier,
    - Rayures,
    - ...

![](https://i.imgur.com/YQ6ZM7h.png)

![](https://i.imgur.com/ImsycN8.png)
> Je vous ai fait une espece de bronze ou je ne-sais-quoi

- Generation de bruit pour simuler l'aspect de certains elements
    - Bruit structure

![](https://i.imgur.com/iH0kYt5.png)

## Bruit de Perlin

<div class="alert alert-info" role="alert" markdown="1">
Afin de donner une impression d'organisation, seul un sous enesemble de points est genere aleatoirement. Le reste des points es calcule par interpolation.
</div>

Ajout d'autres frequences:
- $bruit(i,x)=p^{(i-1)}.bruit(2^{(i-1)},x)$
- Parametres: pas, persistance et nombre d'octaves
- Resultat:
    - Somme de l'ensemble des $bruit(i,x)$

![](https://i.imgur.com/Xte6vUp.png)
- 1 octave $p=0.5$
- On interpole (interpolation lineaire)
- On prend un autre echantillonage et on interpole avec cette autre matrice $\Leftrightarrow$ 2 tirages aleatoires donc 2$^{eme}$ octave


![](https://i.imgur.com/mhaBfZy.png)
- 2 octaves $p=0.5$

![](https://i.imgur.com/9q26QWz.png)

- 5 octaves $p=0.5$

![](https://i.imgur.com/zEwTNYn.png)

- 5 octaves $p=0.8$

![](https://i.imgur.com/EDeFZHw.png)

- 5 octaves $p=0.2$

Applications:
- fumee
    - Interpolation du balanc $\to$ noir

![](https://i.imgur.com/SY1BtBV.png)

- cieluages
    - En dessous d'un certain seuil: Interpolation du gris bleu $\to$ bleu
    - Au dessus d'un certain seuil: bleu

![](https://i.imgur.com/Xn5V9Qu.png)
- bois
    - En dessous d'un certain seuil, marron fonce
    - En dessous d'un certain seuil, marron clair
    - Entre les deux, interpolation

![](https://i.imgur.com/tU1eU7D.png)
- psycho...

![](https://i.imgur.com/m3po5XW.png)
> A force de jouer avec les couleurs j'ai un peu craque

- marbre
    - $n = 1-\sqrt{\vert\sin(2\pi v)\vert}$
    - Interpolation linaire du gris vers le noir en fonction de $n$

![](https://i.imgur.com/1K4faMk.png)

- Generation possible en 3D

![](https://i.imgur.com/ZvGkNnR.png)

# Usage des textures
## *Billboard*
- Element toujours face a l'observateur sur lequel est plaque une texture
- Permet de simuler un objet/phenomene complique simplement a l'aide d'une texture:
    - Arbre
    - Feu
    - ...

![](https://i.imgur.com/VODGjNO.png)

# Environnement

<div class="alert alert-info" role="alert" markdown="1">
On peut s'enfermer dans un objet pour avoir notre environnement
</div>

- *Equirectangular*
    - Une seule texture pour l'ensemble de l'environnement
- *Cubemap*
    - *Skybox*
    - On enferme notre personnage dans un cube
    - Meme resolution pour tous les points
    - Mettre 6 cameras qui prennent $90^o$ dans une direction 
    ![](https://i.imgur.com/BYu081a.png)


![](https://i.imgur.com/RZEMdvM.png)

![](https://i.imgur.com/xzMTIZ1.png)
> In-theiere stellar

# Texture particuliere
## Objets transparents
- Rendu type *raytracing*
    - Loi de Snell-Descartes
- Rendu par projection *openGL*
    - Pas de deviation de rayon
    - Rend tous les objets qui ne sont pas transparents
    - On verrouille le z-buffer en ecriture avant de dessiner tous les objets transparents
    - Objets transparents: melanger la couleur de ce qui a deja ete dessine avec l'objet transparent

# Textures
## Effet de volume
- Perturbation des normales
    - *Bump mapping* (Blinn)
    - Permet de faire apparaitre des variation sur la surface

![](https://i.imgur.com/QwFOFQ2.png)

![](https://i.imgur.com/wcmY10o.png)
> Realise avec blender
> (C'est une mure en haut a droite)

*Comment voir que c'est bien juste la perturbation de normale ?*

<div class="alert alert-success" role="alert" markdown="1">
Si on trace les contour, on voit bien qu'ils sont lissent et qu'ils ne vont pas dans les creux de la mure.
</div>

![](https://i.imgur.com/K73NjQS.png)

Pour aller plus loin:
- Parallax mapping
- Relief mapping

## Ameliorations
<div class="alert alert-info" role="alert" markdown="1">
La texture permet d'ajouter du realisme et evite de modeliser les details d'une surface. Toutefois le resultat est un peu plat.

![](https://i.imgur.com/FscD9RH.png)

</div>

Initialement, on plaque un *bitmap*

![](https://i.imgur.com/owUoHlY.png)
- Ne pas considerer seulement le *bitmap*
- Ajout d'informations:


### 1. Deformations locales
- Height map
    - Carte d'elevation
    - Normales deduites en faisant une derivee partielle
- Normal map
- Diminue le niveau de details (polygones)
- Stocke dans une image

![](https://i.imgur.com/qx2JQhq.png)

![](https://i.imgur.com/EkvGUZz.png)

*Bitmap*:
![](https://i.imgur.com/1UpLHUs.png)

*Bitmap + bump mapping*:
![](https://i.imgur.com/tEOXVjP.png)
- Tache d'illumination a disparue

### 2. Proprietes locales
Ex: specularite

![](https://i.imgur.com/pxeZwOq.png)

*Bitmap + bump mapping +* modifications speculaires
![](https://i.imgur.com/7fW4HKZ.png)

## Conclusions
- Participe au realimse
- Permet la simplification des modeles
- Permet de simuler certains objets/phenomenes difficiles