---
title:          "TIFO: Codage, partie 1: couleurs et representations"
date:           2021-02-19 9:00
categories:     [Image S8, TIFO]
tags:           [Image, TIFO, S8]
description: Codage, partie 1: couleurs et representations
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/HkY00xJM_)

# Codage des couleurs
## Le modele RGB/RVB
Espace RGB/RVB (Red-Green-Blue)
- One code une couleur par un triplet representant la quantite de rouge, de vert et bleu de la couleur
- Une couleur est un point du cube:
    - L'origine du repere $(0,0,0)$: le noir
    - L'opposee: $(1,1,1)$ le blanc
    - Chaque axe code une couleur primaire (R,G,B)

![](https://i.imgur.com/zrEepyG.png)

### Decomposition d'une image suivant les 3 axes:
![](https://i.imgur.com/IV7RgsS.png) 

![](https://i.imgur.com/dUegR2M.png)

Sur une image reelle:
![](https://i.imgur.com/WDvbStb.png)

<div class="alert alert-info" role="alert" markdown="1">
Le modele RGB
- Modele base sur la perception humaine (couleurs primaires en synthese additive)
- Pas toujours intuitif pour selectionner une couleur
- Tres repandu
</div>

## Le model HLS
L'espace **HLS (Hue, Lightness, Saturation)**
<div class="alert alert-info" role="alert" markdown="1">
On code une couleur par 3 composantes: teinte, luminance et saturation. L'espace ressemble a 2 cones que l'on a joint par leurs bases. Une couleur est un point de cet espace
</div>
- Teinte
    - C'est l'angle sur le disque
        - $0^o$ rouge
        - $60^o$ jaune
        - $120^o$ vert
        - $180^o$ cyan
        - $240^o$ bleu
        - $300^o$ magenta
- Luminance
    - La luminance est la hauteur dans le cone
- Saturation
    - La saturation ("purete de la couleur") est la distance au centre du disque

![](https://i.imgur.com/HL0yA4L.png)

### Decomposition suivant les 3 axes:
![](https://i.imgur.com/79Owa9V.png)

![](https://i.imgur.com/Ms2tTOo.png)

Sur une image reelle:
![](https://i.imgur.com/0W3wAZH.png)

### La saturation
> J'ai un p'tit singe ici:


![](https://i.imgur.com/PRIQoLy.jpg)

- Modele intuitif pour "*choisir une couleur*".
<div class="alert alert-warning" role="alert" markdown="1">
L'utilisation de la teinte est interessante toutefois, sur des saturations faibles, la teinte n'a plus vraiment de signification
</div>
- Beaucoup de variantes (HSV...)

## Le modele ~~YMCA~~ CMY 
L'espace CMY (couleurs primaires en syntese soustractive)
- Mieux adpate pour les peripheriques d'impression
- Beaucoup de variantes

<div class="alert alert-warning" role="alert" markdown="1">
En image on l'utilise quasiment jamais.
</div>

## Codage d'un niveau de gris
*Comment coder un niveau de gris ?*
- Une seule composante qui code la luminance
- Une convention possible:
    - Composante nulle $\rightarrow$ pas de lumiere (noir)
    - Composante au maximum $\rightarrow$ maximum de lumiere (blanc)
    - Un niveau de gris quelconque = un point de l'axe:

![](https://i.imgur.com/FYjeWDl.png)
    
## Autres espaces
Il existe d'autres espaces de representation
- YIQ
    - NTSC 1953
    - Facilite la transmission et la compatibilite de l'image tant pour un ecran couleur que un ecran noir et blanc
    - Y donne la luminance
- Lab
    - La distance entre 2 couleurs dans cet espace est representative de la difference percue visuellement entre les 2 couleurs
- XYZ
- YCbCr
- ...

# Conversions entre espaces de couleurs
## RGB $\leftrightarrow$ HLS
- H$[0^o, 360^o]$ L$[0,1]$ S$[0,1]$
    - Teinte
        - Estime en fonction de 2 bornes min et max ![](https://i.imgur.com/EiISSgA.png)
- Pour L $\le 0,5$
    - Saturation
        - Joue sur l'ecartement min $\leftrightarrow$ max sur la teinte
        - Si S $=0$, min $=$ max $=$ L
        - Donc max $=$ ($1$ + S)L et min $=$ ($1$ - S)L
        ![](https://i.imgur.com/u5TH6Ja.png)
- Pour L $\ge 0,5$
    - Meme raisonnment

## RGB $\leftrightarrow$ YIQ
Le passage de l'un a l'autre est simple:

$$
\begin{pmatrix}
    Y\\
    I\\
    Q
\end{pmatrix}=
\begin{pmatrix}
    0.30 & 0.59 & 0.11\\
    0.60 & -0.28 & -0.32\\
    0.21 & -0.52 & 0.31
\end{pmatrix}
\begin{pmatrix}
    R\\
    G\\
    B
\end{pmatrix}
$$

## RGB $\leftrightarrow$ CMY
- Les couleurs primaires de l'espaces CMY sont les couleurs complementaires des couleurs primaires de l'espace RGB
- La conversion est donc simple:
    - $R = 1 - C$
    - $G = 1 - M$
    - $B = 1 - Y$

![](https://i.imgur.com/R5meCzf.png)

## RGB $\leftrightarrow$ niveaux de gris
- Idee simple et intuitive:
    - $L = (r + v + b)/3$
- Amelioration
    - $L = 0.299r + 0,587v + 0,114b$
- Pourquoi la premiere idee est-elle fausse ?
    - Car nos yeux percoivent certaines couleurs mieux que d'autres (cf. la seconde formule)
- Peut-on faire l'inverse (passer du niveau de gris a la couleur ?)
    - Non bien-sur: projection, on passe d'un image 3D a 2D, on a perdu de l'info
    - Avec des regles on peut se donner une colorisation de l'espace (teinte sepia, vert comme une camera de surveillance, etc.) mais **on ne retrouvera pas la couleur d'origine**

## RGB $\leftrightarrow$ noir et blanc
- Est-il possible de passer a une image noir et blanc ?
    - Utile pour traiter les images "trop" riches
    - On binarise l'image
    - *Qu'est-ce qu'on veut extraire de l'image ?*
- Y a t il un interet a passer a une image en noir et blanc ?

## Codage des couleurs
Il existe differents espaces pour la representation des couleurs
- Il faut etre capable de choisir le bon, en fonction de l'objectif recherche
- Etre capable, dans la mesure du possible de passer de l'un a l'autre

# Codage de l'image
## Representation d'une image couleur
Codage d'une image par une matrice:
- L'image est une fonction discrete 2D, elle est souvent codee par une matric
- Pour une image codee en RGB, un point de l'image = un triplet (r,g,b) de valeurs dans la matrics
- Un point de l'image = un pixel. Que signifie pixel ?
    - Picture element

![](https://i.imgur.com/PHxVo6m.png)

## Representation d'une image en niveaux de gris
Codage d'une image par une matrice:
- L'image est une fonction discrete 2D, elle est souvent codee par une matrice
- Pour une image codee en niveaux de gris, un point de l'image = une valeur dans la matrice codant la luminance

![](https://i.imgur.com/k5cxJor.png)

## Acces aux pixels
- Comment coder cette image en memoire ?
    - Matrice ? Vecteur ?
- Comment acceder a un point de cette image ?
- Comment acceder a ses voisins ? 
- Comment parcourir l'image ?


![](https://i.imgur.com/DwVDzec.png)
``` cpp
for (i = 0; i < sx; i++)
    for (j = 0; j < sy; j++)
        offset = i + j * sx
```
``` cpp
for (j = 0; i < sy; j++)
    for (i = 0; j < sx; i++)
        offset = i + j * sx
```
``` cpp
for (offset = 0; offset < sx * sy; ++offset)
```
- Utiliser un iterateur ?

## Resolution/Echantillonage
- Discretisation spatiale (resolution)

![](https://i.imgur.com/Zolw9eM.png)

- Echantillonage (amplitude)

![](https://i.imgur.com/89PRtaB.jpg)

## Nombre de couleurs - Echantillonnage
Codage par palette (couleurs indexees)

| Bit(s) par pixel | Couleurs | 
| -------- | -------- | 
| 1 bpp    | ???     | 
| 2 bpp    | ???     | 
| 4 bpp    | ???     | 
| 6 bpp    | ???     | 
| 8 bpp    | ???     | 

Codage sans palette

| Bits par pixel | Couleurs | Bits par canaux |
| -------- | -------- | -------- |
| 16 bpp | ? | ? |
| 24 bpp | ? | ? |
| 32 bpp | ? | ? |

## Representation de l'image
Un moyen classique de representer une image est d'utiliser une matrice. Y a t il d'autres approches ?
- Arbres (max tree, min tree, tree of shape)
- Graphes
- ...

Maillage
- On choisit intuitivement un maillage ~~carre~~ mais cela peut-il presenter des inconvenients ?
- Y a t il d'autres maillages possibles ?

## Topologie
Choix de la connexite des pixels

4-connexe:
- Voisins en haut, en bas, a gauche, a droite
- Pas lies aux voisins en diagonale
- Plusieurs regions

![](https://i.imgur.com/KwU8LD2.png)

8-connexe:
- Une seule region
![](https://i.imgur.com/lB2UnpX.png)

- Cela pose un probleme de topologie:

![](https://i.imgur.com/s3yJpIw.png)

![](https://i.imgur.com/vXYhJgS.png)

- Si le fond est 8-connexe (en noir), la forme (en blanc) est 4-connexe
- Si le fond est 4-connexe (en noir), la forme (en blanc) est 8-connexe
- Contradiciton avec le theoreme de Jordan
- Que faire ?
    - Vivre avec
    - Changer la forme de pixels
    - Intercaler des frontieres entre les pixels
    - ...

### Changer la forme de pixels:
![](https://i.imgur.com/S9s7Sxw.png)

Codage en memoire:
![](https://i.imgur.com/HuOWWvi.png)


Pour:
- Plus de probleme de connexite
- Plus de probleme de distance
    - Tout le monde est a la meme distance

Contre:
- Gestion de la memoire
    - Inteprete chaque ligne de la matrice comme ayant un decalage *offset*

### Intercaler des frontieres entre les pixels
Les frontieres sont determinees par les *inter-pixels*
![](https://i.imgur.com/ZOprlnX.png)

![](https://i.imgur.com/Sdrsk47.png)

### Exemple d'arbre: Max tree
A chaque fois qu'on a 2 regions qui se separent, on cree des branches
![](https://i.imgur.com/IxO2ni4.png)


## Stockage/Transfer
- Differents formats:
    - JPEG, TIFF, PNM, PNG, BMP, GIF, TGA
- Choix en fonction de criteres
    - Avec ou sans compression (avec ou sans perte)
    - Avec ou sans couleur
    - Avec ou sans palette
    - Une seule image ou plusieurs
    - Optimise pour une architecture ? (Ex. BMP sauvegarde a l'envers)
    - Libre ou pas (Ex. GIF et Compuserve)

### Exemple
- Format PNM
    - PBM: noir et blanc
    - PGM: niveaux de gris
    - PPM: couleurs
- 2 variantes
    - PNM
    - TGA
- Format tres simple (extrait de spec)

![](https://i.imgur.com/b9B0dVp.png)

# Application
- On a vu pas mal de choses sur la formation d'une image
- On va l'appliquer
    - en changeant les couleurs ou l'illumination d'une image
    - en changeant l'organisation spatiale des pixels de l'image
    - en combinant des changements dans le couleurs et dans l'organisation spatiale des pixels

## Changement d'illumination
En tous points de la scene, la reponse du capteur est donne par:
$L(x,y) = \int E(x,y,\lambda)S(x,y,\lambda)R(\lambda)d\lambda$
- Avec
    - $E(x,y)$ l'eclairage
    - $S(x,y,\lambda)$ la reflectance de la surface (fonction de la longueur d'onde $\lambda$)
    - $R(\lambda)$ la sensitivite du capteur qui (pour simplifier est supposse repondre a une seule longueur d'onde: $R(\lambda) = \sigma(\lambda-\lambda_k)$)
On a donc: $L(x,y) = E(x,y)S(x,y,\lambda_k)$

La meme image prise avec 2 niveaux d'illuminations differents:
- $L1(x,y) = E_1(x,y)S(x,y,\lambda_k)$
- $L2(x,y) = E_2(x,y)S(x,y,\lambda_k)$

Donc:
- $L2(x,y) = (E_2(x,y)/E_1(x,y))*L1(x,y)$

Et donc:
- **$L2(x,y)=C*L1(x,y)$**

<div class="alert alert-success" role="alert" markdown="1">
Pour changer l'illumination il faut donc multiplier les valeurs des pixels par une constante (et non additionner/soustraire par une constante comme c'est usuellement fait)
</div>

## Correction d'illumination non uniforme
- Soit une image acquise $I_1$ avec un eclairage non uniforme
- $I_1(x,y)=S(x,y,\lambda_k)E(x,y)$

![](https://i.imgur.com/uLcwNzh.png)

- Soit l'image du fond $I_f$
- $I_f(x,y)=F(x,y,\lambda_k)E(x,y)$

![](https://i.imgur.com/Z4NIvg1.png)

### La soustraction des deux donne:

$$
I_1(x,y)-I_f(x,y) = [S(x,y,\lambda_k)-F(x,y,\lambda_k)]E(x,y)
$$
![](https://i.imgur.com/VApsjT6.png)

### Le ratio des 2 donne:

$$
\frac{I_1(x,y)}{I_f(x,y)} = \frac{S(x,y,\lambda_k)}{F(x,y,\lambda_k)}
$$
![](https://i.imgur.com/aVq3M9A.png)

### Difference vs Ratio
![](https://i.imgur.com/rfn1zih.png)

## Modification des couleurs de l'image
- Application : effet artistique $\rightarrow$ effet sepia
    - On associe a un niveau de luminance une couleur

![](https://i.imgur.com/rfIJnPk.png)

$$
\begin{pmatrix}
    r\\
    g\\
    b
\end{pmatrix}=
\begin{pmatrix}
    0,784 & 0 & 0\\
    0 & 0,588 & 0\\
    0 & 0 & 0,391
\end{pmatrix}
\begin{pmatrix}
    l\\
    l\\
    l
\end{pmatrix}
$$

Resultat:
![](https://i.imgur.com/uZx8NHd.png)

## Modification de l'organisation spatiale des pixels
Application: effets artistiques
- $image\_resultat(x,y) = image\_origin(g(x,y), h(x,y))$
    - Les fonctions $g$ et $h$ ne tiennent pas forcement compte de la valeur du pixel
- Rotation - cisaillement
![](https://i.imgur.com/q6npf2K.jpg)
- Etirement - retrecissement
![](https://i.imgur.com/FajJpsd.jpg)
- Ondulations
- Spirale
- Tranlations aleatoires
- ...
    
![](https://i.imgur.com/lfXcuXH.png)

![](https://i.imgur.com/wwg3153.png)
> La 2e image c'est quand on me chatouille le cou

<div class="alert alert-danger" role="alert" markdown="1">
$image\_resultat(x,y) = image\_origin(g(x,y), h(x,y))$
La transformation doit etre appliquee dans ce sens !
</div>

# Application: le morphing d'images
## Modification des couleurs et de l'organisation spatiale des pixels
- Application: le morhping
    - Vu la structure d'une image, il est possible d'appliquer des operateurs sur ces images
    - Exemple: la moyenne ![](https://i.imgur.com/tOLACWk.png)
    - En combinant
        - Une moyenne ponderee des images (dont les poids evoluent au cours du temps)
        - Un champ de vecteur de translation

# Problemes de precision
- Sur les fonctions colorimetriques
- Sur les transformations spatiales

## La correction gamma
Retour sur la perception
- La perception de l'oeil est logarithmique ![](https://i.imgur.com/RGuhlgk.png) 
- La repartition des niveaux d'energie n'est donc pas lineaire mais exponentielle

![](https://i.imgur.com/lvhzezp.png)

<div class="alert alert-danger" role="alert" markdown="1">
Tous les calculs fait jusqu'a present sont **completement faux** car 50% du signal n'est pas a la moitie du niveau de gris (128) mais a 186.
</div>
$$
r = \frac{number}{255}^{gamma}\\
gamma = 2.2
$$
- Les niveaux de gris ne sont que des numeros, faire des operations (moyenne, addition, application de filtres, interpolation...) n'a pas vraiment de sens
- Dans la pratique, on omet souvent la correction gamma lors des etapes de filtrages
    - C'est faux
- Il y a un compromis entre precision du resultat et vitesse

Retour sur le passage de la couleur en niveuax de gris
- Espace CIE XYZ 1931
    - $R'= r/255 V' = v/255 B' = b/255$
    - $Rsrvb = [(R'+0.055)/1.055]^{2.4}$
    - $Vsrvb = [(V'+0.055)/1.055]^{2.4}$
    - $Bsrvb = [(B'+0.055)/1.055]^{2.4}$

$$
\begin{pmatrix}
    X\\
    Y\\
    Z
\end{pmatrix}=
\begin{pmatrix}
    0,4124 & 0,3576 & 0,1805\\
    0,2126 & 0,7152 & 0,0722\\
    0,0193 & 0,1192 & 0,9505
\end{pmatrix}
\begin{pmatrix}
    Rsrvb\\
    Vsrvb\\
    Bsrvb
\end{pmatrix}
$$
- $Y$ donne la luminance

## L'interpolation
- Que faire lorsque l'on doit "chercher" la valeur d'un pixel mais que l'on ne tombe pas precisement sur un pixel ?
    - 1er solution (rapide): prendre la du pixel le plus proche ![](https://i.imgur.com/bavt9yR.png)
    - 2nd solution: Faire une interpolation bi-lineaire ![](https://i.imgur.com/ebNQsiB.png)

Peut-on faire mieux ?
- Interpolation bicubique
    - Utilise 4 points (calcul de la derivee) ![](https://i.imgur.com/dKybTVd.png)

### Interpolation bicubique
![](https://i.imgur.com/CmdOiGN.png)

$$
f(x) = ax^3+bx^2+cx+d\\
f'(x)=3ax^2+2bx+c
$$

On connait les valeurs pour $x=-1$, $x=0$, $x=1$ et $x=2$
$$
f(-1)=p0, f(0)=p1 \text{ et } f(2)=p3\\
f'(0)=(p2-p0)/2 \text{ et } f'(1)=(p3=p1)/2
$$

Mais aussi
$$
f(0) = d\\
f(1) = a+b+c+d
$$

$$
f'(0) = c\\
f'(1) = 3a+2b+c
$$

On peut donc en conclure que les coefficients a,b,c,d du ploynome et donc interpoler les valeurs intermediaires du signal entre 0 et 1.
![](https://i.imgur.com/UvTPioQ.png)

Artefact:
![](https://i.imgur.com/uZaB0gA.png)

### Autres interpolation
- Il existe d'autres methodes d'interpolation
- Pour faire le choix de l'interpolation, il faut faire un compromis entre vitess et qualite

![](https://i.imgur.com/dFMrb9W.jpg)

# Conclusion
- Codage de l'image et de la couleur
    - Espaces de couleurs, passage d'un espace a l'autre
- Applications
    - Effet sepia
    - Transformation artistiques
    - Morphing
- Correction gamma
- Interpolation