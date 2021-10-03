---
title:          "TIFO: Codage, partie 2 - Histogramme"
date:           2021-02-19 10:00
categories:     [Image S8, TIFO]
tags:           [Image, TIFO, S8]
math: true
description: Codage, partie 2 - Histogramme
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/rJ8B9TJz_)

# Analyse globale de l'image
## Histogramme
- Recense les occurrences de chaque couleur
- Donne une information globale sur l'image
- Permet la realisation de petits traitement globaux
- Peut etre calcule sur une image en couleur

![](https://i.imgur.com/BTsOQQk.png)

![](https://i.imgur.com/bUY9J7T.png)

- Calcul de l'histogramme
- Code:

``` cpp
histogramme: tableau initalise a 0
image: l'image sour forme d'un vecteur

for (offset = 0; offset < sx*sy; ++offset)
    histogramme[image[offset]]++
```

### Quels information peut apport l'histogramme
- Si une image est sur-exposee ![](https://i.imgur.com/jchzgqG.png)
- Si une image est sous-exposee ![](https://i.imgur.com/C8IQzSb.png)
- Si une image manque de contraste

# Applications
## Amelioration du contraste
Application: modification du contraste a l'aide de l'histogramme

![](https://i.imgur.com/g7sEUnm.png)

Correction de l'histogramme:
![](https://i.imgur.com/SIDHXuo.png)

- Etirement
    - $[min, max] \to [0, \text{borne_sup}]$
    - Fonction de correction: $f(x) = ax + b$
        - $a = \frac{b_{sup} - b_{inf}}{max - min}$
        - $b = b_{inf} - ax$ 
        - Generalement $b_{inf} = 0$

![](https://i.imgur.com/ogMjzJb.png)

- Etirement du resultat
    - J'ai bien augmente le contraste
    - J'ai detruit une partie de l'information
        - On a sature des pixels, effacant des details

![](https://i.imgur.com/ZMRQtCe.png)

## Amelioration de l'image
Application: modification du contraste a l'aide de l'histogramme

``` cpp
image: l'image sous forme d'un vecteur

for (offset = 0; offset < sx*sy; ++offset)
    image[offset] = f(image[offset])
```
Tout depend du choix de f
- Fonction $\log$
    - si $x\neq 0$, $f(x)=\frac{\ln(x)}{\ln{max}}*max$
    - si $x=0$, $f(x) = 0$
    - L'intervalle des zones sombres est augmentee
- Fonction $\exp$
    - L'intervalle des zones claires est augmentee
    - L'image est assombrie
    - Attention aux plages de valeurs (exp(255)...)

![](https://i.imgur.com/wThTrOu.png)

## Modification des couleurs de l'image
Application: calcul du negatif
- Fonction de correction: $f(x) = b_{sup} - x$

![](https://i.imgur.com/z0Lbhiu.png)

## Amelioration du contraste
Application: amelioration du contraste a l'aide de l'histogramme cumule
- Calcul de l'histogramme cumule
$$
\begin{cases}
    hc(x) = hc(x-1) + h(x) &\text{pour } x\gt 0\\
    hc(x) = h(x) &\text{pour } x = 0
\end{cases}
$$
![](https://i.imgur.com/6OLCvuR.png)
- Essayer d'uniformiser la repartition des niveaux de gris dans l'histogramme
- Cela revient a essayer de rendre l'histogramme cumule lineaire
    - $f(x) = b_{sup} * \frac{hc(x)}{nb_{pix}}$

Resultat:
![](https://i.imgur.com/DuLObSy.png)

# Histogramme et images couleurs
- Differentes manieres de calculer
    - Globale ![](https://i.imgur.com/T1KqeNj.png)
    - Par plan ![](https://i.imgur.com/DCGhLI9.png)
- Traitements:
    - Independamment sur chaque canal
    - Changement d'espace et traitement uniquement dans le plan L ou V

# Applications
## Amelioration du contraste
- Egalisation d'histogramme de couleur
    - Effectuer l'egalisation sur chaque canal ?
        - Donne de mauvais resultats en general (modification des couleurs) ![](https://i.imgur.com/wpKaa81.png)
    - Solution:
        - Changer d'espace de representation
    - Utilisation de HSV ?
        - Egalisation uniquement sur la valeur

![](https://i.imgur.com/WIMwuLM.png)

## Amelioration de l'image
Specification d'histogramme
- Imposer la forme de l'histogramme
    - (comme pour l'egalisation qui donne un histogramme plat)

## Indexation
- Distance entre histogrammes
    - Comparaison d'images
    - Segmentation automatique en plan de sequences
        - Difference entre images consecutives
- Distances
    - Bin-by-bin distances
        - Distances de Hellinger ~~Bhattacharyya~~
        - ...
    - Cross-bin distances
        - Earth Mover's Distance
        - ...

## Diminution du nombre de couleurs
- Pourquoi diminuer le nombre de couleurs?
    - Simplifier l'image
    - Diminuer l'espace necessaire de stockage
    - Focaliser sur les elements qui nous interessent
    - Effet artisitique
- Pourquoi plus precsiement passer de la couleur aux niveaux de gris ?
    - Traitement de la couleur pas toujours aisee
        - Plusieurs canaux
        - Pas vraiment de relation d'ordre utilisable avec la couleur
- Pourquoi plus precisement passer en noir et blanc ?
    - Focaliser sur les elements qui nous interessent 
        - Separation fond/forme (O.C.R., ...)

### Objectif
<div class="alert alert-info" role="alert" markdown="1">
Reduire le nombre de couleurs utilisees tout en conservant le plus possible une image proche de l'originale
</div>

![](https://i.imgur.com/JfOXmJO.png)

![](https://i.imgur.com/sj7LIm8.png)

### Algorithme
- Mediane cut
    - Basee sur l'etude de l'histogramme
- Diffusion de l'erreur
    - Adoucit certaines erreurs pour la visualisation

#### *Median cut algorithm*
- Reduction du nombre de couleurs
    1. Construction de l'histogramme des couleurs
    2. Elimination des extremites vides
    3. Decoupage du prallelepipede restant en 2 sous-blocs contenant autant de points
    4. Pour chaque sous bloc, recommencer jusqu'a avoir autant de sous blocs que de couleurs souhaitees
    5. Trouver pour chaque partie, une couleur representante

![](https://i.imgur.com/RiHCIYa.png)

#### Diffusion de l'erreur
Le but est de compenser l'erreur commise sur un pixel en propageant cette erreur sur les pixels voisins

$$
\text{FloydSteinberg:}\\
\begin{matrix}
    12 & 15 & 18 & 67 & 68 & ...\\
    67 & 25 & 26 & 57 & 89 & ...\\
\end{matrix}
$$
Ex: on fait une erreur en substituant le 12 par son representant, on propage la difference entre 12 et son representant sur son voisin 15

1. On remplace la couleur du pixel considere par le representant
$$
\text{FloydSteinberg:}\\
\begin{matrix}
     & 15 & 18 & 67 & 68 & ...\\
    67 & 25 & 26 & 57 & 89 & ...\\
\end{matrix}
$$
$$
\begin{matrix}
     & 21 & 18 & 67 & 68 & ...\\
    67 & 25 & 26 & 57 & 89 & ...\\
\end{matrix}
$$
2. On calcul l'erreur commise par cette substitution en faisant la difference entre la vraie couleur et la couleur de remplacement: on trouve une erreur pour chaque canal.
$$
+6
$$
3. On repartie l'erreur estimee sur les pixels voisins
    - Les voisins en haut et a droite participent plus que les voisins en diagonales

|  | $X$| $-7$ |...|
| -------- | -------- | -------- |----|
| $-3$    | $-5$  | $-1$ |...|

$$
\text{FloydSteinberg:}\\
\underline{
\begin{matrix}
     & 21 & 11 & 67 & 68 & ...\\
    64 & 20 & 25 & 57 & 89 & ...\\
\end{matrix}}
$$

<div class="alert alert-info" role="alert" markdown="1">
Ce dernier tableau etait recommande par **FloydSteinberg** pour la propagation de l'erreur.

||X| 7/16|
|-|-|-|
|3/16|5/16|1/16|

</div>

Resultats:
![](https://i.imgur.com/AfcFqMe.png)

![](https://i.imgur.com/4L0eNhB.png)

### Passage en noir et blanc (binarisation)
Binarisation: 
- Separation fond/forme

Seuil global:
- Utilisation de l'histograme
    - On suppose l'histogramme bi-modal (1 mod pour le fond et 1 pour la forme)
    - Trouver le niveau de gris a la jonction entre les 2


Seuil global - resultats:
![](https://i.imgur.com/14q535g.png)

![](https://i.imgur.com/JLsMGiM.png)

Seuil global - un algorithme simple:
1. Supposons un seuil T initial
2. Calculons les moyennes m1 et m2 des ensembles des pixels d'intensite inferieure a T et superieur ou egale a T respectivement
3. Corriger T avec $T = \frac{m_1 + m_2}{2}$
4. Si $T \gt \Delta T$ continuer en 2

Seuil global - Le critere d'Otsu
- On cherche 2 classes
    - Minimiser la variance intra-classe
    - Maximisier la variance inter-classe
- $m_1(k)$ et $m_2(k)$ les moyennes des 2 classes formees par le seuil k
- $m_g$ la moyenne
- $p_1(k)$ et $p_2(k)$ les probabilites d'occurrence des 2 classes formees par le seuil k
- Maximiser la variance inter-classe:
    - $\sigma(k)^2=P_1(k)(m_1(k)-m_g)^2 + P_2(k)(m_2(k)-m_g)^2$
    - Or $P_1(k)m_1(k) + P_2(k)m_2(k) = m_g$ et $P_1(k) + P_2(k) = 1$
    - $\sigma(k)^2 = P_1(k)P_2(k)(m_1(k) - m_2(k))^2 = \frac{(m_gP_1(k)-m_1(k))^2}{P_1(k)(1-P_1(k))}$
        - Reviens a chercher le k dans l'intervale ou $P_1(k)(1-P_1(k))\neq 0$ rel que $\sigma(k)^2$ est le maximum (si plusieurs max, faire la moyenne)

<div class="alert alert-info" role="alert" markdown="1">
Seuil global
- Rapide et simple
- **Se calcul directement sur l'hisotgramme**
- Dans la pratique pas toujours efficace selon le contexte

</div>

#### Resultats
Original:
![](https://i.imgur.com/gufrwAs.png)

Otsu:
![](https://i.imgur.com/jQph8Jz.png)
