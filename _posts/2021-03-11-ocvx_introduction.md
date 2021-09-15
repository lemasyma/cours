---
title:          "OCVX: Introduction"
date:           2021-03-11 13:00
categories:     [Image S8, OCVX]
tags:           [Image, SCIA, OCVX, S8]
description: Introduction
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/SyU52FvX_)

# Introduction
L’optimisation fait partie des missions historiques de l’ingénierie. Elle naît avec l’ère industrielle: une fois un concept élaboré il s’agit de réduire les coups, minimiser les risques de défauts de livraisons ou étendre le scope d’action ...

Les techniques mathématiques qui permettent de résoudre une partie de ces problèmes d’optimisation balayent un large spectre des thématiques mathématiques que vous avez pu aborder jusque là; l’algèbre linéaire, le calcul différentielle et un peu de géométrie. Le cours d’OCVX a pour objectif de vous donner le bon degré de confort pour manipuler ces techniques.

## De quoi on parle ?
Voici quelques exemples qu’on pourrait croiser lorsqu’on s’intéresse à l’optimisation.
- Chercher le plus court/rapide chemin entre deux coordonnées GPS.
- Décider des meilleures routes aériennes qui minimisent le prix d’approvisionnement en kérosène.
- Identifier des images d’IRM qui correspondent à des malformations du cerveau.
- Chercher des patterns dans la population d’étudiants intégrants Epita
- Décider d’achat/vente d’assets prenant en compte l’historique disponible.

# Probleme d'optimisation
## Definition formelle
On écrit en général un problème d’optimisation $(P)$ sous la forme standard

$$
\begin{aligned}
&\text{minimiser} &f_0(x) &\\
&\text{sujet a } &f_i(x)\le0, &\forall i\in\text{{}1,...,p\text{}}\\
& &h_j(x)=0, &\forall i\in\text{{}1,...,m\text{}}
\end{aligned}
$$

où $f_0$, les $f_i$ et les $h_j$ sont des applications de $\mathbb R^n$ vers R. La fonction $f_0$ est dite ***fonction objectif*** ; suivant le contexte ce sera une fonction de ***coût*** ou ***d’erreur***. Les inégalités sont qualifiées de ***contraintes d’inégalités*** et les égalités de ***contraintes d’égalités***.

<div class="alert alert-warning" role="alert" markdown="1">
**Tentative**
Vous pouvez chercher à formuler les problèmes énumérés sous forme d’un problème d’optimisation, ce n’est pas toujours évident.
</div>


Un probleme d'optimisation du type de $(P)$ est dit
- differentiable si toutes les fonctions en jeux le sont;
- ***non-contraint*** s'il n'a aucune contraintes d'inegalites ou egalites
- ***convexe*** si l'ensemble des fonctions en jeu sont convexes, les contraintes d'egalites etant de plus affines

Sous la première hypothèse on a une série d’outils mathématiques qui nous permettront d’apporter un éclairage riche sur $(P)$. Si l’on rajoute la seconde on est en mesure de construire des procédés itératifs efficaces en état de *résoudre* ces problèmes. La dernière nous garantie de trouver *la* solution optimale.


<div class="alert alert-danger" role="alert" markdown="1">
**Fake news**
Les éléments en italiques sont là pour marquer le fait que nos assertions à ce stade sont encore un peu fausses. L’image est un peu moins idyllique.
</div>

## Lexique
Étant donné un problème d’optimisation $(P)$ on appelle:
- ***point admissible*** de $(P)$ tout point de $R^n$ satisfaisant toutes les contraintes. L’ensemble de tous les points admissibles est appelé **lieu admissible** de $(P)$.
- ***valeur objectif*** d’un point admissible la valeur que prend la fonction objectif en celui-ci.
- ***valeur optimale*** de $(P)$ la meilleure borne inférieure sur la fonction objectif.
- ***point optimal*** de $(P)$ tout point admissible dont la valeur objectif est la valeur optimale.

## Premieres remarques qualitatives
Comme est le cas de tout système d’équations, il est utile de se poser le type de questions suivantes:
- y a-t-il au moins une solution?
- s’il y a au moins une solution combien?
- peut-on toujours décrire l’ensemble des solutions?
- y a-t-il moyen d’approcher des solutions?

<div class="alert alert-warning" role="alert" markdown="1">
**Question**
Chercher un problème d’optimisation qui:
- a un lieu admissible est vide;
- a plus d’un seul point optimal;
- n’a pas de valeur optimale mais a un lieu admissible non vide \;
- a une valeur optimale mais pas de point optimal.
</div>

# Cadre de la premiere UE d'OCVX
## Contours du cours
On se limite au cours du premier semestre de majeure au cas des problèmes d’optimisations ***sans contraintes***.
- C’est un cadre suffisant pour les premières applications des techniques d’optimisations à un premier niveau de ML ; il recouvre le cas des différentes régressions, de l’entraînement d’un réseau de neurones ainsi que les cas des algos de classification standards
- Il représente un premier niveau à atteindre qui permet de fixer votre attitude vis-à-vis d’un problème d’optimisation, sans s’encombrer de concepts plus abstraits à concevoir.
- Il ne recouvre pas le cas des Support Vector Machines

# Regression mon amie
## Map Fitting
<div class="alert alert-info" role="alert" markdown="1">
Une famille différentiable d’applications $f_{\alpha} : \mathbb R^n \to \mathbb R$ indexées par $\alpha\in \mathbb R^k$ est une famille de fonctions pour laquelle l’application $\phi : \mathbb R^k \times\mathbb R^n → \mathbb R$ qui envoie $(\alpha, x)$ sur $f_{\alpha}(x)$ est différentiable.

</div>

<div class="alert alert-danger" role="alert" markdown="1">
On considère un ensemble de couples $(X_i, y_i) \in\mathbb R^n \times\mathbb R$ pour $i \in \text{{}1, . . . , p\text{}}$ et une famille différentiable d’applications $\text{{}f_{\alpha}\text{}},\alpha\in\mathbb R^k$ . Le problème de *map fitting* relatif aux données précédentes consiste à trouver les meilleurs paramètres $\alpha^*$ tels que $f_{\alpha^*}$ approche au mieux *(pour une métrique pré-choisie)* a les $(X_i, y_i)$.

</div>

## La regression lineaire
Le plus simple des problèmes de *map fitting* est celui de la régression linéaire. Dans le cas de dimension 1 (on cherche à approcher une fonction de $\mathbb R$ dans $\mathbb R$) il se décline comme ceci:
- la famille différentiable à laquelle on s’intéresse est indexées par $\mathbb R^2$: $f_{\alpha}(x)=\alpha_1x+\alpha_0$ pour $\alpha=(\alpha_0,\alpha_1)$
- la métrique standard utilisée est la ***MSE*** pour ***Mean Square Error*** donnée pour un $f_{\alpha}$ par

$$
\mathcal E(\alpha) = \sum_{i=1}^p\frac{1}{p}(f_{\alpha}(x_i)-y_i)^2
$$

c’est une estimation moyenne de la variance des prédictions de $f_{\alpha}$

<div class="alert alert-success" role="alert" markdown="1">
Le but est de trouver un paramètre $\alpha=(\alpha_0,\alpha_1)$ tel que $\mathcal E(\alpha)$ est minimal, autrement dit de résoudre le problème d’optimisation sans contraintes **minimiser $\mathcal E(\alpha)$**.
</div>

Le problème de régression linéaire a une solution ***analytique***; càd une solution donnée par une expression explicite en fonction des entrées.

Cette solution implique cependant l’inversion d’une matrice de taille équivalent à celle des données en entrée. Chose particulièrement coûteuse.

# Empathie machine
## Approximation séquentielle

Il est rare qu’un problème d’optimisation ait une solution analytique. Même quand cela est le cas il est souvent plus efficace de chercher une solution approchée.

Un processus itératif qui résout un problème d’optimisation $(P)$ est
1. un choix initial d’un point de départ (de préférence) admissible $x_0$ ;
2. un processus itératif qui construit un point admissible $x_{n+1}$ à partir de $x_n$ et de données locales ayant une valeur objectif plus petite que celle de $x_n$.

Cette démarche ne nous offre en général qu’une approximation d’une solution. Elle a cependant l’avantage de pouvoir se dérouler en temps raisonnable. Il faut par ailleurs prendre en compte que l’implémentation des flottants en machines nous contraint déjà à approcher les grandeurs qu’on manipule.

# Acquis d'apprentissages vises (AAVs)
- ***Savoirs***
    - Identifier les éléments composants un problème d’optimisation et des éléments nécessaires à son étude qualitative
    - Cartographier les outils à disposition pour résoudre un problème d’optimisation et les hyperparamètres qui déclinent et gouvernent ceux-ci.
    - Décrire le domaine de validité d’un algorithme.
- ***Savoir-faire*** 
    - Implémenter des algorithmes standards d’optimisation sans contraintes
    - Effectuer des analyses comparatives entre des différentes algorithmes d’optimisation sans contraintes
    - Reconnaître les problèmes liés aux approximations numériques qui apparaissent dans toute implémentation.
- ***Attitude*** - Analyse de risque
    - Vivre par le moto : ***Un*** test n’est pas une ***statistique*** et une ***statistique*** ne vient pas sans ***variabilité***.

# Contenus notionnels
1. Pré-requis techniques
    - Des éléments de géométries
        - Interprétation géométrique du produit scalaire
        - Courbes de niveau et epigraphes de fonctions.
        - Parties et fonctions convexese en dimension finie.
    - Des éléments de topologie
        - Comment calculer des distances et définir des voisinanges dans $\mathbb R^n$
        - Approcher et comparer des fonctions à plusieurs variables.
    - Des éléments de calcul différentiel
        - Approcher localement une fonction multivariées par une fonction affine.
        - Écriture en base ; jacobienne et gradient.
        - Interprétation géométrique du gradient
        - Approximation locale de second ordre : la hessienne
2. Étude qualitative des problèmes d’optimisation.
    - Le lieu critique d’une fonction objectif.
    - Apport de la convexité au contexte de l’optimisation.
    - Études du cas quadratique.
3. Méthodes de résolutions itératives.
    - Descentes de gradients et Méthodes de Newton

# Evaluation
Deux modes d’évaluations vont intéragir dans le cadre de ce cours
1. Des évaluations formatives via moodle, ce qui est suffisant pour garantir le fait que vous consacrez suffisamment de temps à comprendre les éléments de cours et l’assimiler. Une évaluation formative est notée de manière binaire : 0% de la note si l’étudiant n’y participe pas sérieusement et 100% sinon.
2. Des évaluations sommatives comptabilisées de manière classique. Elle seront composées
    - d’une évaluation intermédiaire qui prendra la forme d’un devoir sur table, celui-ci vise à garantir votre capacité à formuler un raisonnement géométrique / différentiel concernant les problématiques d’optimisation
    - d’une évaluation TP afin d’avoir un regard sur l’ensemble des éléments que vous aurez pu mobiliser pour atteindre les objectifs de cours.

Les évaluations formatives comptent pour 20% de la note finale. On attend de vous de faire preuve ***d’autonomie*** lors du suivi de ce cours.

# Moodle
L’ensemble des contenus de cours, d’annonces, de bibliographies de travail à rendre et des tests d’évaluation seront disponibles sur un cours moodle auquels vous serez inscrit bientôt.