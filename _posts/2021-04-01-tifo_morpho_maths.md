---
title:          "TIFO: Introduction a la morphologie mathematique"
date:           2021-04-01 14:00
categories:     [Image S8, TIFO]
tags:           [Image, TIFO, S8, morphologie mathematique, dilatation, erosion, ouverture, fermeture, composition, connexe]
math: true
description: Introduction a la morphologie mathematique
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/ryxvuEmr_)

> Par Elodie cette fois

- TP en Python (wouhou!)
- Evaluation: commun avec IMED

# Plan du cours
Y'en a pas
![](https://i.imgur.com/gg2soyR.png)

# But du cours
- Savoir ce qu'est la morphologie mathematiques
- Comprendre son interet
- Acquerir les bases de la morphologie mathematiques

<div class="alert alert-success" role="alert" markdown="1">
Savoir utiliser les outils de morphologie mathematique pour traiter divers probleme de traitement d'image.
</div>

> On fait mieux que des reseaux de neurones ! (environ)

# Qu'est-ce que c'est ?
## Histoire
Invention francaise (cocorico)
Nee en 1964 a MINES PariTech (ENSMP a Fontainebleau) par Georges Matheron
> Le nom morphologie mathematiques est ete choisi... dans un bar

- 1982: publication du livre Serra en Anglais
- 1987: premiers articles dnas **IEEE PAMI**
    - faire en sorte que la morphologie mathematiques soit reconnue mondialement

<div class="alert alert-success" role="alert" markdown="1">
Depuis, elle est utilisee dans le monde entier
</div>
- Conference internationale tous les 2 ans
- Journal specialise

## STOOOP
On va parler d'OpenCV

<div class="alert alert-warning" role="alert" markdown="1">
Attention a OpenCV
</div>
> C'est genial et horrible en meme temps

- Pour importer OpenCV1: `import cv`
- Pour importer OpenCV2: `import cv2`
- Pour importer OpenCV3: `import cv2`
    - wot
- RGB devient BGR
- xyz? non zyx...

## Retour a qu'est-ce que c'est

Une image devient une fonction

<div class="alert alert-danger" role="alert" markdown="1">
On considere l'image comme un paysage ! (un peu comme Minecraft)
![](https://i.imgur.com/6rpceHY.png)

</div>

## En quelques mots

<div class="alert alert-info" role="alert" markdown="1">
- La morpho maths fait partie de la categorie de traitement d'image non lineaire
- Toutes les parties de l'image ne vont pas reagir de la meme maniere a l'application d'outils de morpho maths
- Permet d'etre beaucoup plus generique et efficace
    - En particulier: on est invariant au contraste
</div>

# La base des bases
## Concept de base: l'ordre

On doit pouvoir etbalir une relation d'ordre entre chaque element considere (pixels, groupes de pixels,etc.)

<div class="alert alert-danger" role="alert" markdown="1">
![](https://i.imgur.com/uiHjV2c.png)

</div>

## Le treillis
Structure de bases: **treillis complet**
- structure ordonee

![](https://i.imgur.com/zFYxhCN.png)

## La connexite
<div class="alert alert-info" role="alert" markdown="1">
La **connexite**, c'est le **voisinage des pixels**
</div>
Tous les voisins qu'on considere comme connectes.

![](https://i.imgur.com/qgQXFLw.png)

En 3D: connexite 6, 18, 26
- Voir a quoi ca correspond: imaginer un Rubik's cube

## Composante connexe

<div class="alert alert-info" role="alert" markdown="1">
Ensembles de pixels connectes
</div>

![](https://i.imgur.com/Wf0nazC.png)

## Operateurs en morpho maths
### Proprietes
Soit $\Omega$ un operateur morpho, $x$ et $y$ deux parties de treillis
- $x\le y\Rightarrow\Omega(x)\le\Omega(y)$ *Croissance*
- $x\le\Omega(x)$ ou $\Omega(x)\le x$ *Extensivite ou Anti-Extensivite*
- $\Omega(\Omega(x))=\Omega(x)$ *Idempotence*


![](https://i.imgur.com/ZkmjwLY.png)

## Elements structurants

<div class="alert alert-info" role="alert" markdown="1">
On veut comparer ce qu'on veut traiter avec un objet de geometrie connue: *element structurant*
</div>

- forme connue
- taille connue
- origine

![](https://i.imgur.com/9QdAXmA.png)

# Operateurs
## L'erosion
> Rappel: on est dans un paysage

![](https://i.imgur.com/p0fkpPJ.png)

On considere une image binaire avec un fond noir et un objet blanc.

<div class="alert alert-success" role="alert" markdown="1">
L'erosion va venir "grignoter" l'objet blanc!
</div>

On considere un element structurant $B_z$, avec une origine $z$. L'erosion est definie par:

$$
\epsilon(X)_B=\{z/B_z\in X\}
$$

Une [video](https://www.youtube.com/watch?v=b5lgnNEzGeU) pour mieux comprendre

## La dilatation
![](https://i.imgur.com/EtPlKAy.png)

En prenant les memes notations et ca devient:
$$
\delta(X)_B=\{z/B_z\cap X\neq\emptyset \}
$$

Une [video](https://www.youtube.com/watch?v=3IJ8RFtlDLY) pour mieux comprendre

## Bilan
![](https://i.imgur.com/jwqMdwl.png)

Erosion: 
- agrandit les trous
- deconnecte les objets
- "augment le noir"

Dilatation: 
- rempli les trous 
- connecte les objets
- "augment le blanc"


La forme de l'element structurant va "selectionner" les formes qu'on garde $\rightarrow$ on filtre en fonction de la taille/forme
<div class="alert alert-warning" role="alert" markdown="1">
La croissance n'est valables que si les elemens structurants sont identiques
</div>

# Associer et composer
## Premiere composition

Que se passe-t-il si on fait une erosion suivi d'une dilatation ?

$$
\gamma(X)=\delta_B(\epsilon_B(X))
$$

![](https://i.imgur.com/wXq0NFp.png)

<div class="alert alert-danger" role="alert" markdown="1">
Il s'agit d'une **ouverture**
</div>

## Deuxieme composition
Que se passe-t-il si on fait une dilatation suivi d'une erosion ?

$$
\phi(X)=\epsilon_B(\delta_B(X))
$$

![](https://i.imgur.com/jUZNDdM.png)

<div class="alert alert-danger" role="alert" markdown="1">
Il s'agit d'une **fermeture**
</div>

## L'ouverture et la fermeture
Ce sont des outils tres puissants en morpho

<div class="alert alert-info" role="alert" markdown="1">
Ils permettent de garder les objets plus grands que l'element structurant
</div>

![](https://i.imgur.com/sLazIUn.png)

<div class="alert alert-success" role="alert" markdown="1">
Ideales dans des problemes de filtrage/debruitage!
</div>