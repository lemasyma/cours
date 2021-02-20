---
title:          "ISIM: Rappels"
date:           2021-02-18 9:00
categories:     [Image S8, ISIM]
tags:           [Image, ISIM, S8]
description: Rappels
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/SkrIFCi-d)

# Optique et image
<div class="alert alert-info" role="alert" markdown="1">
Pour synthetiser une image, il faut comprendre comme celle-ci se forme et est capturee.
</div>

![](https://i.imgur.com/t30MnYX.png)

Dans ce cas:
- Table
- Observateur (cam)
- Source lumineuse
    - rayons se propagent dans toutes les directions
    - eclaire la table
    - la table renvoie la lumiere qui est captee par l'observateur $\rightarrow$ source lumineuse secondaire

<div class="alert alert-warning" role="alert" markdown="1">
L'observateur ne peut pas faire de difference entre un objet qui emet de la lumiere et un objet qui le renvoie
</div>

## Qu'en est-il de la couleur ?
*Quelles sont les couleurs primaires ?*
- [ ] RGB
- [ ] RJB

*Comment ca se fait que je vois la nape bleue ?*
Dans les rayons lumineux il y a des longueurs d'ondes.

La table filtre les longueurs d'onde et renvoie les rayons qui correspondent au bleu.
![](https://i.imgur.com/Oagj1gl.png)

2 systemes:
- Source primaire: 
    - rajoute des couleurs 
    - RVB
        - couleurs primaires
    - $\Rightarrow$ **sysnthese additive**
- Objets qui renvoient la lumiere et en absorbe une partie: 
    - enleve de la couleur 
    - CMJ (Cyan, Magenta, Jaune)
        - complementaire aux couleurs primaires
    - $\Rightarrow$ **sysnthese soustractive**

![](https://i.imgur.com/wi6gKY7.png)

## Capture de l'image
Dans un appareil photo/oeil/camera:
- Chambre noire
- Pellicule/capteurs photosensibles
    - transforme la lumiere recue en energie
    - transforme la lumiere recue en teinte (ancien appareils photos)
- Point image
    - image envoyee
- Foyer
    - selectionne les rayons lumineux
- Plan image
    - image recue a l'envers

![](https://i.imgur.com/Kz05vu6.png)

### Caracteristiques
1. Zoomer ou dezoomer
    - En augmentant ou reduisant la distance focale
    - Zoomer: reduire le champ de vision (grande distance focale)
    - Dezoomer: augmenter le champ de vue (petite distance focale)
2. Ouvrir ou fermer le diaphragme
    - Si ouvre
        - Plus de foyer unique
        - Image devient flou
        - On reduit la zone de nettete
        - **Plus on ouvre le diaphragme, plus on reduit la profonder de champ**
    - Si reduit le diaphragme
        - Plus de profondeur de champ
        - Moins de lumiere
    - Varier la taille de diaphragme
        - Peut etre une contrainte
        - Rendre l'arriere-plan flou
        - Jouer avec dans les images de synthese

![](https://i.imgur.com/hc0hjAD.png)
<div class="alert alert-warning" role="alert" markdown="1">
Le foyer doit etre **avant** le plan image IRL, mais en virtuel il peut etre apres (cf. schema).
</div>

### Comment capturer l'image en pratique
<div class="alert alert-success" role="alert" markdown="1">
Dans l'appareil photo: matrice de capteurs photosensibles qui generent de l'energie quand ils sont frappes.
</div>

Image en niveau de gris:
![](https://i.imgur.com/38wbohl.png)

<div class="alert alert-info" role="alert" markdown="1">
Pour la couleur, pour chaque capteur photosensibles on met des filtres (ex: capturer que les longueurs d'onde qui capturent le vert).
</div>

*Probleme:* on connait l'intensite en tout point mais pas pour toutes les longueurs d'onde, il faut la deduire via les voisins.
![](https://i.imgur.com/T9yjwMH.png)

<div class="alert alert-danger" role="alert" markdown="1">
C'est le **patterne de Bayer**.
</div>
*Pourquoi ces couleurs ?*
> C'est les couleurs primaires RVB. Pourquoi RVB?

*Pourquoi plus de vert ?*
> Lie a la perception humaine, nos yeux sont plus sensibles au vert/jaune.

Pour un capteur virtuel, pour chacune des cellules on peut mesurer toutes les longueurs d'ondes pour RVB.

## Formation de l'image
<div class="alert alert-info" role="alert" markdown="1">
Les longeurs d'onde du spectre visible est une plage tres etroite.
![](https://i.imgur.com/siuzJLa.png)

</div>

### Pourquoi les couleurs primaires sont RVB ?
On a des capteurs dans nos yeux pour RVB.
![](https://i.imgur.com/VYjLxbv.png)

*Pourquoi on peut reconstituer toutes les couleurs a partir de RVB?*
> Si par exemple on voit une couleur jaune, nos capteurs vert et rouge sont stimules.
> ![](https://i.imgur.com/IQAE3Pl.png)

<div class="alert alert-warning" role="alert" markdown="1">
Dans les couleurs possibles il n'y a pas de blanc, ca arrive quand on stimule tous les capteurs en meme temps. De meme pour le magenta, qui arrive quand uniquement le cone vert n'est pas stimule.
</div>
<div class="alert alert-danger" role="alert" markdown="1">
Certaines couleurs *n'existent pas*, notre oeil nous donne une representation.
</div>

### Codage de la couleur
Modele RGB
- One code une couleur par la quantite de rouge, de vert et de bleu que contient cette couleur
    - Une couleur est alors un point du cube
- Modele directement lie a notre perception

![](https://i.imgur.com/I0Z1KQm.png)

Le modele RGB est **directement issue de notre perception des couleurs**.
![](https://i.imgur.com/l4zIhMb.png)

### Generation d'une image synthetique
<div class="alert alert-info" role="alert" markdown="1">
Simuler les phenomenes optiques qui conduisent a la formation de l'image.
</div>

# Geometrie Euclidienne
- Produit scalaire: forme nilineaire, symetrique, definie positive
- Espace pre-hilbertien $(E,\vert)$ reel
    - $E$: R-espace vectoriel
    - $\vert$: produit scalaire
- Espace euclidien
    - Espace pre-hilbertien reel de dimension finie
- Espace affine $\mathcal F$ de $E$ (e.v):
    - $\mathcal F$ s.e.v de $E$
    - Soit $A\in E, \forall x\in\mathcal F; A + x\in\mathcal F$
- Cas particuliers:
    - Dim 0 $\Rightarrow un point
    - Dim 1 $\Rightarrow$ une droite affine
    - Dim 2 $\Rightarrow$ un plan affine
- Repere cartesien de $\mathcal F : (O, B)$ avec $O$ un point de $\mathcal F$ et $B$ une famille de vecteurs de $\mathcal F$ formant une base de $\mathcal F$
- Soir $E$ un $\mathbb R$-espace vectoriel, une norme $N$ sur $E$ est une application de $E$ dans $\mathbb R$ tel que:
    - $\forall u\in E, N(u) ge 0$
    - $\forall u \in E, N(u) = 0 \Leftrightarrow u = 0$
    - $\forall (u,\lambda)\in (E\times\mathbb R), N(\lambda u) = \vert\lambda\vert N(u)$
    - $\forall(u,v)\in E^2,N(u+v)\le N(u)+N(v)$
- Definition associee au produit scalaire:
    - $N(u)=\sqrt{u\vert u}$: norme euclidienne
- Produit mixte:
    - $[u,v,w] = det(u,v,w)$
    - = (u\times v).w
    - Donne le volume du parallelepipede
- Produit vectoriel;
    - $x;[u,v,w] = x.w(x=u\times v)$
    - $\Vert u\times v\Vert$ aire du rectangle
    - $\frac{1}{2}\Vert u\times v\Vert$ aire du triangle
- Vecteurs et angles en euclidien
    - Produit scalaire: $u.v=\Vert u\Vert\Vert v\Vert\cos(u,v)$
    - Produit vectoriel: $u\times v = \Vert u\Vert\Vert v\Vert\sin(u,v)$
    - $u.v = 0 \Leftrightarrow u$ et $v$ ortho
    - $(u.v)^2 + (u\times v)^2 = \Vert u\Vert^2\Vert v\Vert^2$

## Equation de droites
- 2D
    - Cartesienne: $y=ax + b$
    - Implicite: $ax+by+c=0$
    - Parametrique: $A+\lambda\overrightarrow v$
- 3D
    - Cartesienne 
    - Implicite
    - Parametrique: $A+\lambda\overrightarrow v$

## Equation d'un plan
- 3D
    - Cartesienne: $ax+by+cz+d=0$
    - Implicite
    - Parametrique
        - Prendre un point du plan et donner 2 vecteurs qui vont definir une base
        - $A+\lambda_1\overrightarrow v_1\lambda_2\overrightarrow v_2$

## Equation d'un cercle/sphere
- 2D/3D
    - Cartesienne: $(x-a)^2+(y-b)^2+(z-c)^2 = r^2$
    - Implicite
    - Parametrique

## Determinant
- Utilite du determinant:
    - Equation de droite passant par ($x_1$, $y_1$) et $u(a,b)$
    $$
\begin{vmatrix}
    x-x_1 & a\\
    y-y_1 & b\\
    \end{vmatrix}
    = 0
    $$
    - Equation de droite passant par ($x_1$, $y_1$) et ($x_2$, $y_2$)
    $$
\begin{vmatrix}
    x-x_1 & x-x_2\\
    y-y_1 & y-y_2\\
    \end{vmatrix}
    = 0
    $$
- Idem pour l'equation d'un plan dans un espace 3D

## Intersection
### Intersection droite/plan
- Droite: $P+t\overrightarrow v$
- Plan: $ax+by+cz+d=0$ ou $\overrightarrow N.\overrightarrow X = d$
- $\overrightarrow N.(P+t\overrightarrow v) = d$
- $t_i = \frac{d-\overrightarrow N.P}{\overrightarrow N\overrightarrow v}$
    - Cas particulier si $d$ parallele au plan ($\overrightarrow N\overrightarrow v=0$)
- $I=P+t_i\overrightarrow v$

### Intersectoin droite/plan $\rightarrow$ droite\triangle
- Verifier que $I$ est dans le triangle $ABC$
    - Exprimer $I$ en fonction de $A$, $B$ et $C$
        - Les coordonnees barycentriques doivent etre toutes positives
    - Determiner les  de chaque cote du triangle
        - Determiner la positiom de $I$ vis a vis de chaque cote i.e $ax+by+c\lt0$ ou $ax+by+c\gt0$
    - Avec l'algorithme de Cyrus-Beck
    - En regardant l'orientation du sens de parcours

![](https://i.imgur.com/G5UZKWC.png)


### Intersection droite/sphere
- Calcul de l'intersection dans le repere local ou global ?
- Idem que pour le plan mais avec l'equation de la sphere. 3 cas possibles:
    1. Pas de solution (pas d'intersection)
    2. Solution double (la droite touche la surface de la sphere)
    3. Deux solutions distinctes (la droite traverse la sphere)
- Distance point/droite
    - $d(p, D) = \frac{\vert ax_p + by_p + c\vert}{\sqrt{(a^2 + b^2)}}$
    - $d(p, D) = \frac{\vert\overrightarrow{AM}.\overrightarrow n\vert}{\Vert n\Vert}$
- Distance point/plan
    - $d(p,P)=\frac{\vert ax_p+by_p+cz_p+d\vert}{\sqrt{(a^2+b^2+c^2)}}$
    - $d(p, P) = \frac{\vert\overrightarrow{AM}.\overrightarrow n\vert}{\Vert n\Vert}$
- Distance droite/droite $D_i(A_i, \overrightarrow{v_i})$
    - $d(D_1, D_2) = [\overrightarrow{A_1A_2}, \overrightarrow{v_1}, \overrightarrow{v_1}]/\Vert\overrightarrow{v_1}\overrightarrow{v_2}\Vert$
- Distance sphere/sphere

# Geometrie projective
- Geometrie euclidienne
    - Etude des formes des "objets"
    - Invariance par rotation, tranlsation, reflexion
- Geometrie projective
    - Etude des objets tel qu'ils sont vus
    - Perception des angles, des distances, du parallelisme distordu

Exemple avec des rails de train paralleles mais qui semblent se rejoindre au point de fuite:

> N'allez pas aller vous faire renverser par un train


![](https://i.imgur.com/emRimFP.png)

Dependant du point de vie, B est entre A et C ou A est entre B et C:
![](https://i.imgur.com/PToCKlZ.png)

## Projection sur le plan image
<div class="alert alert-info" role="alert" markdown="1">
On a juste a projeter les sommets d'une face
![](https://i.imgur.com/yx5sdlr.png)

</div>

Dans l'espace, on ne prend pas l'objet entier mais juste une face. On trace une droite qui passe par le foyer et le sommet, on note l'intersection avec le plan image ce qui nous donne sa projection.

![](https://i.imgur.com/DtOsnI5.png)

## Point de fuite
Si on a une droite qu'on veut projeter sur le plan image, on prend le plan forme par la droite et le plan qui inclut le foyer de projection. Si on fait une intersection de ce plan avec le plan image, c'est **exactement** la projection de la droite sur le plan image en accord avec le foyer.

<div class="alert alert-info" role="alert" markdown="1">
Si on fait de meme avec d'autres droites, elle convergeraient toutes vers un meme point: **la point de fuite**.
</div>

## Horizon
<div class="alert alert-info" role="alert" markdown="1">
Intersection du plan passant par le foyer et parallele au plan objet
![](https://i.imgur.com/yvlGlBE.png)

</div>

Tous les points de fuite de droites paralleles sont alignees sur le l'horizon
![](https://i.imgur.com/BkQKk0Y.png)

## Points a l'infini

On a l'ensemble de droites, si on les projettent on a undividuellement l'ensemble des points de la droite, avec **une image et un antecedent** sauf que si on prend une droit qui va suffisament loin on est **parallele au plan objet**.

<div class="alert alert-danger" role="alert" markdown="1">
Ce sont les **points a l'infini**.
</div>

On a le *corollere* dans l'autre sens: certains points appartiennent au plan parallele au plan image et passent par le foyer, ils ne peuvent pas etre projetes sur le plan image car leur droite ne coupe jamais le plan image.

<div class="alert alert-warning" role="alert" markdown="1">
On doit rajouter au plan objet et au plan image des points a l'infini.
</div>

![](https://i.imgur.com/k23QPyt.png)

<div class="alert alert-info" role="alert" markdown="1">
Un ensemble de droites paralleles convergent vers ce point a l'infini.
</div>

On peut representer le plan projectif par un disque, l'ensemble de paralleles est represente par une seule droite sur ce disque.
![](https://i.imgur.com/RUXKvZL.png)

<div class="alert alert-danger" role="alert" markdown="1">
Le point de fuite est le meme de chaque cote du plan image.
</div>
Pour le rajouter sur le disque, on doit le "plier" pour que les extremites se rejoignent.
![](https://i.imgur.com/iMjUT0L.png)

## Coordonnees homogenes
Dans le plan
- $RP^2$ est l'ensemble des triplets $[p] = [p_1, p_2, p_3]$ avec $(p1,p2,p3)$ dans $\mathbb R^3$ prive de $(0,0,0)$
- Deux points $p$ et $q$ sont egaux si et seulement si il existe un $k$ dans $R^*$ tel que:
    - $p_1=kq_1$ et $p_2 = kq_2$ et $p_3=kq_3$

Deux cas:
- $p_3 = 0$, $[p_1,p_2,p_3] = [p_1,p_2,0]\in RP^2$
- $p_3 \neq 0$, $[p_1,p_2,p_3] =[p_1/p_3,p_2/p_3,1]\in RP^2$

*Pourquoi s'embeter avec cette 3e coordonnes ?*
Si $p_3$ est a 0, on parle des points a l'infini.

<div class="alert alert-danger" role="alert" markdown="1">
Homogenes: peut representer les points euclidiens et les points ideaux.
$[a,b,0]:(a,b)$ donne la direction des points associes
</div>
Idem pour une droite projective et pour l'espace 3D.

## Transformation usuelles
Representation des transformations usuelles dans l'espace projectif
- Translation
- Echelle 
- Rotation
- Projection

Combinaison des transformations.

### Translation
- Euclidien: 
$$
P + 
\begin{pmatrix}
	t_x\\
	t_y
\end{pmatrix}
$$
- Coordonnees projective: on a une coordonnees de plus
$$
\begin{pmatrix}
    x + t_x\\
    y + t_y\\
    1
\end{pmatrix}=
\begin{pmatrix}
    1 & 0 & t_x\\
    0 & 1 & t_y\\
    0 & 0 & 1
\end{pmatrix}
\begin{pmatrix}
    X\\
    Y\\
    1
\end{pmatrix}
$$
<div class="alert alert-warning" role="alert" markdown="1">
La translation est passe d'une addition a une multiplication matriciel.
</div>

Si on passe en 3D, on a une matrice qui permet d'expliquer la translation en 3D:
$$
\begin{pmatrix}
    1 & 0 & 0 & t_x\\
    0 & 1 & 0 & t_y\\
    0 & 0 & 1 & t_z\\
    0 & 0 & 0 & 1
\end{pmatrix}
$$

Mise a l'echelle:
$$
\begin{pmatrix}
    S_x & 0 & 0 & 0\\
    0 & S_y & 0 & 0\\
    0 & 0 & S_z & 0\\
    0 & 0 & 0 & 1
\end{pmatrix}
$$

Rotation:
- Suivant un axe canonique:

$$
\begin{pmatrix}
    \cos & -\sin & 0 & 0\\
    \sin & \cos & 0 & 0\\
    0 & 0 & 1 & 0\\
    0 & 0 & 0 & 1
\end{pmatrix}
$$

- Suivant un axe quelconque:

$$
\begin{pmatrix}
    x^2(1 - \cos) + \cos & xy(1-\cos)-z\sin & xz(1-\cos) + y\sin & 0\\
    yx(1 - \cos) + z\sin & y^(1-\cos)+\cos & yz(1-\cos) - x\sin & 0\\
    xz(1 - \cos) + y\sin & yz(1-\cos)+x\sin & z^2(1-\cos) + \cos & 0\\
    0 & 0 & 0 & 1
\end{pmatrix}
$$

Modelisation des rotations:
<div class="alert alert-warning" role="alert" markdown="1">
L'ordre des rotations compte
</div>
- Specifier un ordre suivant les axes $O_x$, $O_y$ et $O_z$
- Specifier l'axe de rotation
- Utilisation des quternions
    - $Q=a+bi+cj+dk$
    - $a,b,c,d$ reels $\rightarrow$ $a$ partie reelle et $(b,c,d)$ partie imaginaire
    - $I^2=j^2=k^2=-1$
    - $i.j=k;j.k=i;k.i=j$
    - $j.i=-k;k.j=-i;i.k=-j$
    - Les quaternions unites (norme $(Q) = 1$) permettent une representation plus compacte de n'importe qu'elle rotation

## Combinaisom des transformations
<div class="alert alert-danger" role="alert" markdown="1">
On peut **pre-calculer** une matrice qui est **l'ensemble** des transformations.
</div>
Rajouter une coordonnees nous permet d'exprimer l'ensemble des transfomrations sous forme d'un produit matriciel.