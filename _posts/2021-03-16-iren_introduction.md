---
title:          "IREN: Introduction aux réseaux neuronnaux "
date:           2021-03-16 11:00
categories:     [Image S8, IREN]
tags:           [Image, Sante, IREN, S8, réseaux neuronnaux]
description: Introduction aux réseaux neuronnaux
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/H1k6jb07d)

[Index du cours](http://www.ricou.eu.org/iren/notes_rn.html)
# Un neurone

![](https://i.imgur.com/9EFBuRe.png)
- On reflechis selon les impulsions electriques dans notre cerveau
- Il y a des seuils pour les impulsions electriques

![](https://i.imgur.com/giplUbM.png)
- Poid: $w_0$
- Energie de la part du voisin: $x_0$
- Si on a une mauvaise "connexion", on recoit pas ou peu les informations des voisins
- On a une fonction d'activation $f$ (seuil) pour savoir si on ressort du neurone
- A la sortie on a une combinaison lineaire de l'entree de base
    - La fonction d'activation *casse* la linearite
    - Les problemes ne se reglent pas lineairement a chaque fois

## Les maths d'un neurone
1. $z=b+\sum_iw_ix_i$
2. $y=\sigma(z)$

avec
- les $i$ entrees $x_i$
- $b$ le biais
- $w_i$ les poids
- $\sigma$ la fonction d'activation

![](https://i.imgur.com/MpH4FwW.png)

- ReLU:
    - cancer ? $2,5$ en reponse
- Logistique (sigmoide)
    - vrai ou faux
- Tangente hyperbolique
    - Varie de $-1$ a $1$
    - Choisi entre vrai ou faux

# Un premier reseau neuronal
![](https://i.imgur.com/9L6XulL.png)

Évaluer les couples d’entrée $(1,1)$, $(0,1)$, $(1,0)$ et $(0,0)$ avec $\sigma$ une logistique

- $(0,0) = 0$

# Construction d'un reseau neuronal
Pour construire un réseau neuronal par apprentissage supervisé il faut : 
- un grand jeu de données étiquetées par la sortie voulue
- définir l’architecture du réseau avec
    - le nombre de couches
    - les types de couches
    - le nombre de nœuds par couche
    - les fonctions d’activations
    - les connexions inter-couches
    - toutes astuces qui fonctionnent
- une fonction d’erreur pour guider la correction sur les poids
- une méthode pour faire converger le réseau (trouver les bons poids)

> En cas de problème, on sacrifie un poulet.

# Les donnees
Les données doivent être
- très nombreuses (assez pour définir toutes les inconnues du réseau)
- de bonne qualité (pour ne pas tromper le réseau)

*On appronfondira avec des exemples et l’utilisation de Pandas pour nettoyer les données.*

![](https://i.imgur.com/6DgeOCy.png)
Est-ce un champignon ? Précision suivant la qualité des étiquettes.

# L’architecture du réseau
C’est la partie tactique et artistique.

*L’étude des différents réseaux n’entre pas dans le cadre de ce cours d’introduction. On se limitera à quelques réseaux lors des TP.*

![](https://i.imgur.com/2dWzDxd.png)

# La fonction d’erreur
La fonction d’erreur indique de combien le réseau s’est trompé par rapport à
la vérité terrain ($y$ vs $t$). Elle doit
- être dérivable
- correspondre au problème traité

Cette fonction est aussi appelée fonction de coût (*cost function* ou *loss function* en anglais).

## Exemple
- L’erreur quadratique $E = (y − t)^2$
- $E = \log(\cosh(y − t))$ quadratique puis linéaire lorsque l’écart croît
- L’entropie croisée pour des probabilités (valeurs entre $0$ et $1$)

$$
E=-\sum_kt_k\log(y_k)+(1-t_k)\log(1-y_k)
$$

# Une méthode pour trouver les bons poids
Comment l’erreur nous guide pour trouver les poids ?

## Exemple
Vous êtes le directeur et tous les jours vous invitez votre équipe à déjeuner. Il y a le choix entre le plat A, B ou C. Vous payez chaque jour l’addition.

![](https://i.imgur.com/Ymi0H3z.png)

Avec les données $[(5,3,2), 114]$, $[(6,2,2), 108]$, $[(3,4,5), 147]$ qui correspondent aux quantités de chaque plat et au prix global, déduire le prix de chaque plat par une méthode d’apprentissage

### *Que proposez-vous ?*
C'est une equations a 3 inconnues mais on veut faire apprendre au reseau de neurones.

Supposons qu'on met tous les prix a 10euros et qu'au lieu de payer 100euros pour 10 plats, on paye 114euros.
Reflechir comme un reseau neuronal:
- On augmente tous les prix
- On augment les poids en fonction du nombre de fois ou un plat a ete prit
    - On fait un pourcentage $\rightarrow$ $50%$
        - La somme de tous les $i$ divise par $i_0$

### Utilisons l’erreur pour corriger les poids
L’algorithme consiste à trouver les $w_i$ qui minimisent l’erreur : 
1. On initialise les poids à une valeur probable (disons 10 pour tous)
2. On corrige les poids au prorata de leur part dans l’erreur $E = y − t$ : 

$$
w_j = w_j − \eta d_j
$$
- $d_j = \frac{E\times i_j}{\sum_ki_k}$
- $\eta$ petit pour éviter de sur-corriger

Déroulons l’algorithme avec $\eta = \frac{1}{10}$:
- $[(5,3,2), 114]$ Notre prix estimé est de 100.
    - $d_0=\frac{(y-t)\times i_0}{10} = -7.0$ donc $w_0=10+0.70=10.7$
    - $d_1=\frac{(y-t)\times i_1}{10} = -4.2$ donc $w_0=10+0.42=10.42$
    - $d_2=\frac{(y-t)\times i_2}{10} = -2.8$ donc $w_0=10+0.28=10.28$
- $[(6,2,2), 108]$ Notre prix estimé est de 105.6 et on obtient
    - $w_0=10.84$, $w_1=10.46$ et $w_2=10.33$
- $[(3,4,5), 147]$ Notre prix estimé est de 126.04 et on obtient
    - $w_0=11.37$, $w_1=11.16$ et $w_2=11.20$

On peut rejouer les données jusqu’à converger
- la convergence peut être longue avec un petit $\eta$
- cela peut diverger avec un trop grand $\eta$

<div class="alert alert-danger" role="alert" markdown="1">
$$
\frac{E\times i_j}{\sum_k i_k} = \alpha\frac{\delta(y-t)^2}{\delta w_j}
$$
derivee partielle par rapport a $w_j$
</div>

# Rétropropagation du gradient

![](https://i.imgur.com/1iJPfKY.png)
Fonction logistique

Calculons l’influence du poids $w_{2,2}^2$ sur l'erreur quadratique $E:\frac{\delta E}{\delta w_{2,2}^2}$

La derivee partielle de $y$ par rapport a $z$ est $y(1-y)$

> C'est $e^x$ qui se balade. Il croise $2$ tout panique qui lui dit "Derivee me court apres!" et part en courant pendant que $e^x$ se marre. Ensuite $e^x$ tombe sur un gars qui cherche quelqu'un, et le gars lui demande "T'as pas peur de moi ?", $e^x$ repond "Bah non pourquoi?", le gars lui repond "Bah parce que je suis $\frac{d}{dy}$"

## Que vaut le gradient de $E :\nabla E$?

## Pourquoi ce titre ?