---
title:          "ISIM: Rendu temps reel"
date:           2021-03-08 9:00
categories:     [Image S8, ISIM]
tags:           [Image, ISIM, S8, clipping, backface culling, polygone, eclairage]
math: true
description: Rendu temps reel
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/Bkqe98XXd)

# Le rendu
Rendu temps reel vs Rendu photorealiste
- Rendu photorealiste:
    - Objectif:
        - Generation d'images realistes
        - Contrainte de temps faible
    - Strategies
        - Object-based rendering algorithms
            - Illumination globale calculee independamment du point de vue
        - Image-based rendering algorithms
            - Illumination calculee partiellement, en fonction du point de vue
        - Deterministic rendering algorithms
        - Monte Carlo rendering algorithms
- Rendu temps reel
    - Objectif:
        - Generation rapide d'images

# Le rendu temps reel

## Principe general
- Modelisation des objets dans un repere local
- Modelisation de la scene dans un repere global
- Projection de la scene sur le plan image
    - passage repere global au repere camera
    - projection sur le plan image (+dessin 2D)

![](https://i.imgur.com/2CFenpr.png)

<div class="alert alert-info" role="alert" markdown="1">
Pour faire le rendu:
- camera qui possede son propre repere
- les objets sont exprimes dans le repere lies a la scene 
    - on les change de repere et on les exprimes dans le repere lie a la camera
    - on peut maintenant les projeter sur le plan image.

</div>

![](https://i.imgur.com/Xg3HArf.png)

# Algorithmes 3D fondamentaux
Projection des objets sur le plan image:
![](https://i.imgur.com/dD8eMVP.png)

*Comment projeter un objet sur le plan image ? Plusieurs objets ?*

<div class="alert alert-warning" role="alert" markdown="1">
Il faut identifier les problemes!
</div>
- Comment determiner les sommets/face non visibles ?
- Comment determiner les objets caches (ou partiellement caches ?)
- Comment determiner les objets qui sont hors champ (ou partiellement hors champ/derrrier le plan image) ?
- Comment determiner les objets qui sont derriere le plan image ou partiellement visible ?

Afin de les resoudre et:
- avoir une projection correcte
- etre efficace


## *Clipping*
- *Comment determiner les objets qui sont hors champ (ou partiellement hors champ/derrrier le plan image) ?*
- *Comment determiner les objets qui sont derriere le plan image ou partiellement visible ?*

<div class="alert alert-success" role="alert" markdown="1">
- Estimation de la positiopn d'une face par rapport aux plans
- Elimination des faces a l'exterieur
- Decoupage des polygones a cheval (equations parametriques)

![](https://i.imgur.com/HTp00Rx.png)

</div>

## *Backface culling* 
*Comment determiner les faces non visibles ?*
- Enumerer les sommets toujours dans le meme sens
![](https://i.imgur.com/6H07o4V.png)
- Determiner l'orientation de la face par rapport a l'axe optique:
    - Calculer le vecteur normal a la surface (produit vectoriel)
    - Determiner l'angle entre le vecteur normal a la surface et le vecteur directeur de l'axe optique (produit scalaire)

![](https://i.imgur.com/fVwg0bI.png)


## *Comment determiner les objets caches ou partiellement caches ?*
- Trier les objets et les dessiner dans l'ordre
![](https://i.imgur.com/o6Iawzs.png)
- Comment determiner cet ordre ?
    - Utiliser le centre de gravite
    - Ne fonctionne pas dans tous les cas !

![](https://i.imgur.com/fgKDSud.png)


<div class="alert alert-warning" role="alert" markdown="1">
Si on dessine du plus pres au plus loin au lieu de par-dessus, on peut etre plus rapide.
</div>

<div class="alert alert-success" role="alert" markdown="1">
Utilisation d'un arbre B.S.P. (Binary Space Partitionning Tree)
</div>
- Chaque noeud represente un hyperplan (deduit d'une face F)
- Le 1$^{er}$ fils contient les faces du demi-espace derriere F et le second fils contient les faces du demi-espaces devant F
- Lorsque l'hyperplan intersecte une face, la face est coupee en 2
![](https://i.imgur.com/JPnZa5K.png)
- On peut deduire un ordre de parcours des polygones pour les dessiner du plus eloigne au plus proche
- idem, du plus proche au plus eloigne

Efficacite:
- Compromis entre arbre equilibre et nombre de polygones (fragmentation des polygones)

## *Z-buffer*
*Comment determiner les objets caches ou partiellement caches ?*
Utilisation du Z-buffer
- Sauvegarde de la profondeur pour chaque pixel dessine ![](https://i.imgur.com/Nm79CFs.png)

|Avantages|Inconvenients|
|-|-|
|Simple|Oblige a projeter l'ensemble des polygones|
||Probleme de resolution lors de l'encodage du Z|

## Projection
Une fois que l'on a elimine les elements hors champ de la camera, les elements qui ne sont pas de face
- On projette les sommets et on dessine (et rempli) le polygone en tenant compte de la profondeur

$$
\begin{aligned}
&p_i=\frac{fp}{z} &(1)
\end{aligned}
$$

![](https://i.imgur.com/IC6sMTA.png)

# Algorithmes 2D fondamentaux
## Remplissage de polygones
- Suivant la projection des polygones, il faut dessiner/remplir le polygone
    - Determiner si une partie n'est pas visibile
    - Determiner la couleur et l'eclairage
        - Eventuellement plaquer une texture
    - ...
- Les donnees sont la liste des sommets


Depend de plusieurs choses:
- Triangle de polygone
    - Triangle ?
    - Convexe ?
    - Quelconque...?
- Donnees:
    - Liste de sommet
- Approches:
    - Triangulation
    - Remplissage direct
    - Inondation

<div class="alert alert-info" role="alert" markdown="1">
Algorithme:
- Parcourir toutes les arretes de haut en bas et remplir horizontalement

![](https://i.imgur.com/fTkNRbM.png)

</div>

### Algorithme
1. Trier les sommets pour definir les section ![](https://i.imgur.com/2uQzfZU.png)
    - Ordre de remplissage
2. Determiner les arretes actives (dans la section) ![](https://i.imgur.com/wXKrujD.png)
    - A chaque transition, il faut remettre a jour la liste des arretes actives ![](https://i.imgur.com/PtRSMwt.png) 
        - On arrive a une frontiere de section
        - On regarde le sommet suivant
        - Il faut desactiver l'arrete actuelle et activer la suivante ![](https://i.imgur.com/7AZjK0T.png)
3. A chaque niveau il faut tracer des segments horizontaux ![](https://i.imgur.com/TgYSxIv.png)
    - On obtient des points d'intersection avec chaque arrete
    - On les trie horizontalement pas ordre croissant

<div class="alert alert-warning" role="alert" markdown="1">
Il faut etre prudent car en arrivant a un niveau une arrete peut etre ignoree.
![](https://i.imgur.com/h9jB29a.png)
</div>

- Simplification pour les polygones convexes (ou meme dans le cas du triangle)
    - Se restreindre a des cas plus simples

![](https://i.imgur.com/Smh1SM5.png)

## Trace de segments
- Trace rapide de segments
    - Affichage de segments
    - Suivi des arretes activer
- Comment faire ?

Algorithme naif:
- Repose sur l'utilisation des nombres a virgule flottante (un peu lent)

``` cpp
for (x = 1; ...;) {
    y = ax + b
    plot(x,y)
}
```

Critiquons ce bout de code: c'est pas ouf
- Si on parcourt les x et qu'on veut dessiner les y
    - Matrice de pixel
    - Si coeff faible (ex: 1), on avance lentement
    - Si on a `a = 4`, pente tellement forte qu'on a des discontinuite dans le trace du segment 

![](https://i.imgur.com/6rc4c5P.png)

*Est-ce qu mon algo est bien ?*
- `a` est un ratio donc `float`
- multiplication $\rightarrow$ beaucoup de calculs
- **Le resultat est un `float` avec une multiplication et addition**

### Autre solution: Bresenham (65?)
Uniquement avec des additions d'entiers
![](https://i.imgur.com/BjdSd9C.png)

Critere:
- $y=mx+p$ avec $m=\frac{d_y}{d_x}$
- $D=d1-d2=(m(x_p+1)+p+y_p)-(y_p+1-m(x_p+1)+p)$
- $D=d1-d2=2d_y(x_p+1)-2d_xy_p-d_x+2d_xp$
- $D\lt0\Rightarrow(x_{p+1}, y_p)$ inc: $2d_y$
- $D\gt0\Rightarrow(x_{p+1},y_{p+1})$ inc: $2d_y-2d_x$

![](https://i.imgur.com/I2qaZBq.png)

<div class="alert alert-warning" role="alert" markdown="1">
Probleme d'*aliasing*.
</div>

## Trace de cercle
Algorithme naif
- Repose sur l'utilisation des nombres a virgule flottante `float` (un peu lent)
- Utilisation des symetries
- Precalcule des fonctions trigos

Algorithme de Bresenham
- Meme esprit que pour les segments

Critere:
- $D(P) = x^2 + y^2 - r^2$
- $D(A) = (x+1)^2 + y^2-r^2$
- $D(B) = (x+1)^2+(y-1)^2-r^2$
- $S=D(A)+D(B)$
- $S\ge0\Rightarrow B$
- $S\lt0\Rightarrow A$
- Calcul de S incremental

![](https://i.imgur.com/pZS1QvC.png)

## *Clipping*
Une fois qu'on a projete le polygone, on l'a clipe mais on peut aussi le projeter et le fenetrer.

Meme s'il est possible de fenetrer les polygones dans l'espace, on peut aussi le faire dans le plan (apres projection)
- Fenetrage rectangulaire de segments:
    - Cohen-sutherland
- Fenetrage d'un polygone a partir des segments:
    - Weiler-Atherton

### Fenetrage rectangulaire de segments
Cohen-sutherland
- Pour fenetrer il faut des criteres simples et rapides
- Fenetre de vue: 4 frontieres dans le plan
- Code associe a la position relative du point dans le plan
- Attribue a chaque sommet un code a 4bits
    - Chaque bit representant la position relative du point par rapport a la frontiere

![](https://i.imgur.com/fRpodPT.png)
- Les points a l'interieur de l'image on tous leurs bits a 0
- Les points a l'exterieur ont au moins un bit a 1

![](https://i.imgur.com/OvsDA0p.png)
- Pour savoir si une arrete est completement visible, on fait un ou logique entre le code du premier et deuxieme sommet
    - Si le resultat = 0, l'arrete est entierement visible

![](https://i.imgur.com/cR23pKe.png)
- Pour savoir si une arrete est visible quand ses sommets sont hors de l'image, on fait un et logique
    - Si resultat = 0, l'arrete est potentiellement visible
    - Sinon, probablement hors de l'image

### Weiler-Artherton
![](https://i.imgur.com/VHH4uGr.png)
Polygone projete sur l'image:
- Partie a l'interieur
- Partie a l'exterieur

On prend notre polygone et fenetre de vue et on y insere tous nos points d'intersection:
![](https://i.imgur.com/zChLRcl.png)
- Ex: AB1, 1 sommet supplementaire, on l'insere
- Obtient 2 nouveaux polygones

*Comment trouver le polygone resultat de la fenetre de vue ?*
- Partir d'un point dun polygone depuis la fenetre de vue
- Parcours les arretes
- A point d'intersection, change de polygone (polygone $\leftrightarrow$ quadrilatere)

![](https://i.imgur.com/8ocZk1u.png)

<div class="alert alert-warning" role="alert" markdown="1">
1. Toujours partir d'un point in l'interieur de la fenetre sinon on tourne en rond. S'il n'y a pas de point du polygone a l'interieur de l'image, commencer par une intersection
2. Avoir parcouru tous les points du polygone dans la fenetre

![](https://i.imgur.com/ecWfak4.png)

</div>

### Cyrus-Beck
Fenetrage entre 2 polygones
- Cyrus-Beck (Pour deux polygones convexes)

Connaitre la position d'un point $Q$ par rapport a un cote de la fenetre ?

![](https://i.imgur.com/4Jinb1I.png)

$$
\begin{align}
&I(Q) = (Q-P).n
\begin{cases}
&= 0\\
&\lt0\\
&\gt0
\end{cases}
&(2)
\end{align}
$$

Fenetrage d'un segment ?
![](https://i.imgur.com/oXX7gQn.png)
- $L(t)=A+(B-A)t$
- $I(Q)=(Q-P).n$
- $I(L(T)) = (L(T)-P).n$
- Intersection
    - $(L(t)-P).n = 0\Leftrightarrow t = \frac{(A-P).n}{A-B.n}$
- $D=(B-A)$
    - Cas 1: $D.N\lt0\Rightarrow t=t_{\text{sup}}$
    - Cas 2: $D.N=0$
    - Cas 3: $D.N\gt0\Rightarrow t=t_{inf}$
- On recommence pour tout les segments de la fenetre
    - puis si $t_{\text{inf}}\gt t_{\text{sup}}$ segment non visible
    - sinon segment compris entre $[t_{\text{inf}}..t_{\text{sup}}]$

![](https://i.imgur.com/IWx1wM7.png)

Polygones non convexe
- Decoupage en polygones convexes
- Triangulation de Delaunay

## Retour sur le *clipping*
Application de Cohen-Sutherland sur la pyramide 3D
![](https://i.imgur.com/ImIDHXi.png)
- Peut appliquer l'algo en 3D
    - Au lieu de 4 codes on en a 6

## Determination de la couleur des pixels durant le remplissage
Remplissage en fonction de:
- La couleur de la face ?
- L'eclairage ?

## Eclairage
Determination de la couleur
- Modele de Lambert
    - $I_d = k\times \frac{N.L}{\Vert N\Vert.\Vert L\Vert}$
    - Meme niveau d'eclairement pour un polygone donne
        - Un peu moche d'avoir des polygones uniformes
        - Impression polygones plats

![](https://i.imgur.com/w4vtLYY.png)

- Modele de Gourand
    - Essayer de *lisser* le polygone
    - On calcule l'illumination a chaque extremite du polygone
    - Interpoler l'illumination
    - Repeter l'interpolation pour tous les points de la surface
    - Utile quand on a beaucoup de points sur la surface

![](https://i.imgur.com/6Oj5FJG.png)

> Anecdote: Sur les verisons ancienne de OpenGL, c'etait soit Lambert soit Gourand. Fabrizio voulait avoir une lampe torche pour son 1$^{er}$ projet OpenGL, des qu'un spot illumine un angle ca eclaire beaucoup plus que si on eclaire plus le centre
> ![](https://i.imgur.com/Fb9Rymt.png)

- Modele de Phong
    - On interpole la normale en tous les points du polygone suivant les arretes
    - Beaucoup plus de calcul
    - Marche mieux

<div class="alert alert-warning" role="alert" markdown="1">
Attention au calcul des normales
![](https://i.imgur.com/uKBVTwy.png)

![](https://i.imgur.com/Mbz3kb4.png)
Echnatilloner suffisemment la surface ou bien placer la normale
</div>

On approxime une surface ronde par des polygones. Si on calcule Lambert, on espere que l'interpolation represente la normale **reelle** a la surface. **L'aclairage donne l'impression de volume**.
![](https://i.imgur.com/ZwxeNwO.png)
Pour chaque sommet du maillage, on stoque la normale.

## Resultats
![](https://i.imgur.com/hBvYHGs.png)

La difference entre Phong et Gouraud se creuse lorsque le modele est pauvre
![](https://i.imgur.com/Ul8zFrX.png)

## *lightmap*
Eclairages plus evolues
![](https://i.imgur.com/rXRwkLF.png)

On peut afficher des eclairages pre-calcules (du moment qu'il n'y a pas trop d'illumination)
![](https://i.imgur.com/gX34wei.png)
Permet de donner pas mal de realisme en temps reel

# Conclusion
- Beaucoup d'algorithmes
- Implementes dans les moteurs
    - A connaitre pour inter-agir avec ces moteurs
- De nouvelles technologies emergent (RTX...)