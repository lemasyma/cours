---
title:          "ISIM: La modelisation"
date:           2021-03-11 9:00
categories:     [Image S8, ISIM]
tags:           [Image, ISIM, S8, maillage, surface, polygone, animation]
math: true
description: La modelisation
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/Sk1TyUPm_)

# Modelisation
- Rendu temps reel
    - Mailages/polygones
- Rendu photorealiste (algorithme type *raytracing*)
    - Maillages/polygones
    - Mathematiques
- Animation
    - Modeles physiques

Chaque objet est decrit par une formule mathematiques
- Tres compact et bien adapte pour les algorithmes type *raytracing*
- Formule compliquee ou impossible a determiner pour la plupart des objets

Formes de bases - primitives 2D/3D
- Sphere
- Cylindre
- Cube
- Plan
- Tore
- ...

# Maillage
Construction d'objets par assemblage de polygones
- Bonne modelisation des objets avec peu de courbes (architecture...)
- Peu compacte mais facile manipuler

## Representation
- Polygone utilise:
    - Majoritairement le triangle
        - Facilite le traitement (remplissage...)
- Representation en interne
    - Liste de coordonnees de sommets par polygone
        - *Duplication* des sommets communs a plusieurs polygones
        - Pas de connaissance de la topologie
    - Liste de sommets puis liste d'indice par polygone
        - Gain de place
        - Reduction de la quantite d'information
        - Pas de connaissance de la topologie

## Triangulation de Delauny
<div class="alert alert-info" role="alert" markdown="1">
Cas pour quand le maillage n'est pas en triangle.
</div>

Diagramme de Voronoi
- $vor(p) = \{x\in E;\forall qd(x,p)\le d(x,q)\}$

![](https://i.imgur.com/HU9lPVg.png)

## *Mesh Refinement*

<div class="alert alert-warning" role="alert" markdown="1">
On veut appauvrir le maillage quand il est loin et l'enrichir quand il est pres.
</div>

Adaptive mesh refinement
- *Depth tagging*

# Modelisation surfacique
## Surfaces de Bezier
Bezier (1960 - *Renault*)
- Courbes de Bezier
- Surfaces de Bezier

> Ces courbes ont ete mises en place pour representer les carosseries de voitures

### Courbes de Bezier
<div class="alert alert-info" role="alert" markdown="1">
**Courbes de Bezier**: definir une courbe passant par 2 points:
</div>
- Lissage lineaire
    - $P_1t+P_2(1-t)$ avec $0\le t\le1$
    - Si plus de points: continu par morceau

![](https://i.imgur.com/vv7KpQO.png)

- Lissage polynomial
    - $x(t) = Q(t) = a_3t^3+a_2t^2+a_1t+a_0$
    - $y(t) = R(t) = b_3t^3+b_2t^2+b_1t+b_0$
    - Pour garder la derivabilite en $P_1$ et $P_2$:
        - $Q'(t) = 3a_3t^3+2a_2t+a_1$
        - Idem pour $y(t)$
    - Il faut trouver les $a_i$ et les $b_i$
- On va utiliser:
    - $x(0)=xP_1$
    - $x(1)=xP_2$
    - $x'(0) = x'P_1$
    - $x'(1)=x'P_2$
- Ce qui donne:
    - $x(t)=(2t^3-3t^2+1)xP_1+(-2t^3+3^2)xP_2+(t^3-2t^2+1)x'P_1+(t^3-t^2)x'P_2$
    - Idem pour $y(t)$
- Comment avoir les
    - $x'(0)=x'P_1$
    - $x'(1)=x'P_2$

<div class="alert alert-danger" role="alert" markdown="1">
Ajout de points de controles $D_n$ pour determiner la derivee localement.
![](https://i.imgur.com/7lfKfXU.png)

![](https://i.imgur.com/fawfaDf.png)

</div>
Les vecteurs tangents sont deduits par $3(D_1-P_1)$

<div class="alert alert-success" role="alert" markdown="1">
Cela donne:

$$
xP_1(1-t)^3+xD_1(3t(1-t)^2)+xD_23t^2(1-t)+xP_2t^3
$$

![](https://i.imgur.com/7WVrpFx.png)

</div>
On peut chainer et rajouter des morceaux pour agrandir la courbe.

Resultats:
![](https://i.imgur.com/tYSV3bA.png)

![](https://i.imgur.com/skBMlqc.png)

> La texture est d'ailleurs procedurale

Pour definir une courbe plus complexe:
- Augementer le degre
    - La modification d'un point de controle perturbe toute la courbe
- Joindre plusieurs courbes de Bezier

Pour appliquer des transformations affines:
- Applique les transformations affines aux points de controle

### Surfaces de Bezier
Par extension: surfaces de Bezier
- 4 points de controle en 2D, 16 points de controle en 3D
- Joindre plusieurs surfaces de Bezier

# Lissage de polygones
## Surface de subdivision
Differents algorithmes: Algorithme de catmull-Clark, Doo-sabin.
Un exemple en 2D:
- Diviser chaque segment en 3 parties egales
- joindre les divisions successives
- Recommencer jusqu'au niveau lissage desire

![](https://i.imgur.com/WDkVcmN.png)
> A faire en 3D

## Algorithme de Catmull-Clark
Exemple:
![](https://i.imgur.com/LXFxHfh.png)

![](https://i.imgur.com/J70tDVJ.png)

![](https://i.imgur.com/NUA9zHr.png)

![](https://i.imgur.com/fgl4o99.png)

![](https://i.imgur.com/yh6nEhB.png)

> Est-ce qu'on peut dire que c'est fait... a la main ?

# Modelisation par assemblage
## *C.S.G.*
<div class="alert alert-info" role="alert" markdown="1">
*C.S.G.: Constructive Solid Geometry*
</div>
Combiner des briques de base (solides) par des operations:
- Union
- Intersection
- Difference

Union:
![](https://i.imgur.com/AcP96zw.png)

Intersection:
![](https://i.imgur.com/ccDW72C.png)

![](https://i.imgur.com/mLZPAYS.png)

Difference:
![](https://i.imgur.com/qz4duXo.png)

![](https://i.imgur.com/G13F5Bk.png)

Representation sous forme d'arbre:
![](https://i.imgur.com/AKXwxav.png)
- Fonction implicite d'un solide: $F(x,y,z)$
    - $F(x,y,z)\lt0$ interieur
    - $F(x,y,z)=0$ surface
    - $F(x,y,z)\gt0$ exterieur
- Pour le calcul des C.S.G.: $-1;0;1$
    - $F_{A\cap B}(p) = \max(F_A(p),F_B(p))$
    - $F_{A\cup B}(p) = \min(F_A(p),F_B(p))$
    - $F_{A-B}(p) = \max(F_A(p),-F_B(p))$

# Modelisation par revolution
<div class="alert alert-info" role="alert" markdown="1">
L'objet est construit par la rotation d'une forme autour d'un axe de revolution
- Fonction d'un angle
- Fonction d'un pas d'echantillonnage
</div>

Trace du contour:
![](https://i.imgur.com/YdMcR7f.png)

![](https://i.imgur.com/QLsu02a.png)
L'axe de revolution se situe au centre (axe vert et axe rouge)

![](https://i.imgur.com/qy3aNlE.png)

![](https://i.imgur.com/6Pmgdy5.png)
> On se rend compte que le Graal n'est rien d'autre qu'une fulte a champagne

![](https://i.imgur.com/cpwSguI.png)

Autres exemples:
![](https://i.imgur.com/5KmFG1Q.png)
> La boule de bowling presente des C.S.G.

![](https://i.imgur.com/4vojKjk.png)

# Modelisation par extrusion
- L'objet est construit par une surface suivant une trajectoire
- Le chemin peut etre plus ou moins complique

![](https://i.imgur.com/M0MPpxo.png)
> C'est peut-etre une etoile de mer mais je la fait sortir de terre

Retour a la main de tout a l'heure:
![](https://i.imgur.com/uZE2Qx1.png)

![](https://i.imgur.com/Z9f6KKW.png)

# Cartes d'altitudes
Permet generalement de representer les terrains:
- Construction:
    - Iterative
    - ...

![](https://i.imgur.com/fypc4KA.png)

Exemple:
![](https://i.imgur.com/iFZD6kA.png)
> Is this minecraft

# Blobs/Metaballs
<div class="alert alert-info" role="alert" markdown="1">
Representation d'un objet par iosurface
</div>

Imaginons qu'on met une source d'energie qui chauffe:
![](https://i.imgur.com/jY1Dw4U.png)

![](https://i.imgur.com/qEVqPBz.png)

*Qu'est-ce qui se passe si on a 2 points d'energie qui se rapprochent ?*
![](https://i.imgur.com/aNxdZ8v.png)

![](https://i.imgur.com/QNbLBKY.png)

On obtient une courbe car les valeurs se *somment*.

<div class="alert alert-success" role="alert" markdown="1">
On peut utiliser cette courbe pour modeliser des formes arrondies.

</div>

## En 2D:
![](https://i.imgur.com/8MIDgeW.png)

![](https://i.imgur.com/19Bqj8A.png)

![](https://i.imgur.com/ueIIQn4.png)

## En 3D:
![](https://i.imgur.com/be5dDls.png)
![](https://i.imgur.com/vimt9wM.png)

![](https://i.imgur.com/cCnZNgr.png)
> J'ai fait un petit objet, je sais pas ce que c'est.
> *Hand-spinner?*

On peut faire des gouttes de mercure qui s'attachent ensemble.

<div class="alert alert-warning" role="alert" markdown="1">
Le point d'energie n'est pas forcement ponctuel, ca peut un un plan, un cylindre, etc.
</div>

![](https://i.imgur.com/prDc8dl.png)
> On un un p'tit.. p'tit cheval

- Rendu
    - En raytracing, evaluation le lonf du rayon
    - Algorithme des "*marching cubes*"
    - Particules
    - Attention au calcul des normales
- Modelisation
    - Eau
    - ...

# Modelisation de la vegetation
## Graftales
Modelisation desplantes
- L-Systems (Lindenmayer, 1968)
    - Similaire a une grammaire
    - souvent utilise pour modeliser la vegetation (mais pas seulement)

![](https://i.imgur.com/4VS7S2W.png)
> Y'a un super cours de theorie des langages donne par Jonathan Fabrizio

On par de l'axiome et on applique la regle de production
- On divise le 1$^{er}$ segment en 3 sous-segments
    - On rajoute 2 segments inclines
- On repete a chaque etape 

![](https://i.imgur.com/qjtTeDs.png)

<div class="alert alert-warning" role="alert" markdown="1">
On a besoin de differentes regles d'evolutions (branches, couleurs, etc.). Le plus dur c'est de **definir** la grammaire de base.
</div>

# Acquisition
> Comment font-ils pour faire des modeles aussi beau ?

Scan 3D

Pour le monde de Nemo:
![](https://i.imgur.com/BjyS8Ya.png)
On a un *vrai* artiste qui fait un *vrai* modele

![](https://i.imgur.com/DX61ptX.png)
Suite au scan 3D du modele

![](https://i.imgur.com/DPxQ6es.png)

![](https://i.imgur.com/52qZJrv.png)

Pour Avatar:
![](https://i.imgur.com/gpvmTyX.png)

<div class="alert alert-info" role="alert" markdown="1">
Cette pratique est assez courante.
</div>

D'autres artistes scultent directement le modele numerique.

Sculpture 3D:
![](https://i.imgur.com/mOaAHyT.png)

# Codage des Formes/Maillages
- Aretes aillees
- *B-rep*
- *Array of vertex*
    - Enregistrer tous les sommets et leurs proprietes
    - Pas tres compact
- *Array of indexes*
    - Lister les sommets et leur caracteristiques
    - Tablea d'addressage indexe

![](https://i.imgur.com/IMplrN1.png)

![](https://i.imgur.com/CKmNBcY.png)

Dans cette exemple: le sommet 1 est enregistre plusieurs fois, on a pas a enregistrer ses caracteristiques a chaque fois, on fait un addressage indexe.


<div class="alert alert-warning" role="alert" markdown="1">
Ne mache pas toujours, les proprietes peuvent varier d'un meme sommet en fonction du polygone auquel il est rattache.
</div>

## Aretes ailles
Une arete:
- une orientation
    - Sommet de depart et d'arrivee
    - On les memorise selon un ordre
- deux faces
- deux sommets
- quatre aretes
    - Le sommet actuel y est toujours lie si elles existent

![](https://i.imgur.com/KD5ff6H.png)

## *Boundary Representation B-Rep*
<div class="alert alert-info" role="alert" markdown="1">
Un solide est modelise par les elements exterieurs.
</div>
- Cela donne une surface fermee
    - Ensemble de : 
        - Faces, aretes et sommets + relations topologiques 
    - Les faces ne doivent pas s'intersecter ailleurs que sur des aretes explicites (de la B-REP)
    - Les afces doivent separer l'interieur de l'exterieur du solide
- Redondance des donnees $\to$ risque d'incoherence

# Modelisation d'une scene
Deformation/Mouvements/Objets articules
- Representation hierarchique
    - Systeme de pile de matrices

![](https://i.imgur.com/Lj0GzwI.png)

## Deformations libres
On veut contorsionner un objet mais ses morceaux doivent restes coherents.
- Une solution: faire un volume de Bezier et modifier les points de controle
    - Solution simple
    - Pas la plus efficace

![](https://i.imgur.com/lumbFW1.png)

# Animation
<div class="alert alert-info" role="alert" markdown="1">
Generation de toutes les images qui composent l'animations
</div>
- Il faut donc modeliser les transformations
    - Deplacements
    - Deformations
    - Changement de couleur
    - ...
- Equation de mouvement
    - Definitions des positions et orientations - trajectoire a suivre
- Position cle et interpolation
    - Specification que de quelques positions puis interpolation automatique pour generer les positions intermediaires (pas facile de respecter toutes les contraintes)
- Modele physique
    - Donne du realisme au mouvement

![](https://i.imgur.com/5RHCBB7.png)
- L'ordinateur calcul les positions intermediaires
- L'animateur fait les images "cles" de l'animation

## Positions cles
![](https://i.imgur.com/DeYYg2Q.png)
> Celle de droite c'est quand Fabrizio va voir mon raytracer

## Vitesse du mouvement
![](https://i.imgur.com/6haQMJz.png)
Il faut gere l'acceleration du mouvement entre 2 positions cles
- Un mouvement lineaire n'est pas realiste
- Il y a du travail sur l'expression du visage

## Le monde de Nemo
Filmer des poissons reels pendant tres longtemps et reproduire le mouvement
![](https://i.imgur.com/P8tJ4n8.png)

![](https://i.imgur.com/lWb0DFN.png)

## Animations difficiles
Animation de personnages
- Definition de l'animation complete du personnage
    - Difficile et consommation memoire trop elevee
- Definition d'un "squelette" et d'une "peau"
    - Le mouvement est specifie uniquement pour le squelette
    - Gain de place

Retournons sur la main:
![](https://i.imgur.com/IGDsy3z.png)
On a rajoute un squelette, si on veut bouger la main, on bouge le squelette.
> Le squelette de la main est anatomiquement faux

- Definition d'un "squelette"
    - Le corps humain comporte environ 200 os
    - Environ une centaine d'articulations
    - assemblage de segments rigides
        - Structure arborescente hierarchique
        - Rotation avec ajout de contraintes
    - Cinematique inverse
        - Trouver la bonne position
    - Le deplacement des os entraine le deplacement de la peau

![](https://i.imgur.com/7yp7ggR.png)
- La peau
    - Cylindres
    - Maillages ou surfaces (Splines...)
        - Attachement de chaque point a un os
        - Ponderation de l'attachement d'un point aux os voisins ![](https://i.imgur.com/KGnwFLY.png)
    - Modeles de muscles
        - Modelisation par blobs et surfaces implicites
            - Dans l'ensemble ce type de modeles n'est plus trop utilise
        - Modelisation des muscles par des ressorts ![](https://i.imgur.com/tNSz2GE.png)
    - Modelisation par particules hierarchiques
        - Noyau: lie au reste du modele
        - Derme: deformation del'objet
        - Epiderme: cohesion et surface + interaction et collisions avec le rest du monde

$\to$ Diminution de la complexite
- Interaction uniquement avec la couche voisine
- Interaction avec l'exterieur geree au niveau de l'epiderme
    - diminution du nombre de particules
    - diminution de la quantite de calculs

![](https://i.imgur.com/wwDg1tP.png)

- Problemes de jointures
    - Augmentation du maillage aux jointures
    - Ajout d'os dans l'articulation
    - Ajout de contraintes: section minimal autour de chaque os..
    - Lissage des ponderations des contributions des os sur l'enrobage

## Animation de visages
Quelques positions modelisees
- Normal, souriatn..
- Calcul automartique des transitions (*morphing*)

Temps reel: *Blend shape*
- Position neutre
- Codage des deltas pour arriver a une position particuliere

## *Motion capture*
![](https://i.imgur.com/E7rl5Zb.png)
- Realisme important
- Des acteurs vont jouer la scene
    - Jouent dans un hangar dans lequel ils sont geolocalises
    - Ils auraient pu se peindre le visage en bleu mais ils ont pas oses
    - Au moins ils ont des p'tites oreilles
- Camera: geolocalisee

Mapping:
![](https://i.imgur.com/72CIxGx.png)

![](https://i.imgur.com/ynvMunz.png)

![](https://i.imgur.com/6tbGdv1.jpg)
> C'est pendant l'entrainement, pas le hangar

Mouvement du visage:
![](https://i.imgur.com/oPqosCh.jpg)

Une grosse bete va manger des chevaux:
![](https://i.imgur.com/TfGQtsu.png)
![](https://i.imgur.com/CP67jYJ.jpg)

On va caller des modeles 3D de chevaux qui se feront manger
![](https://i.imgur.com/WSYeUT5.png)

Fonctionne de la meme facon que le motion capture avec les humains:
![](https://i.imgur.comEPdygP.png)
![](https://i.imgur.com/FtTV9sj.png)


> Pas tous les filmes utilisent le motion capture, comme Ratatouille

## Tissus et vetements
Modeles masses-ressorts
- Maillage de Provot
    - On met des "masses"
    - Ajout de ressorts pour le cisaillement et la courbure
        - Indique les contraintes physiques entre chacune des masses

![](https://i.imgur.com/YJk6fnE.png)

Collisions et autocollisions
- Beaucoup de calculs
    - division de l'espace et volumes englobants
- Autocollisions
    - Eviter que le tissus passe au travers de lui-meme en se repliant

# Conclusions
- Modelisatione et animation