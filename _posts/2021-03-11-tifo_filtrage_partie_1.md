---
title:          "TIFO: Filtrage, partie 1"
date:           2021-03-11 15:00
categories:     [Image S8, TIFO]
tags:           [Image, TIFO, S8]
description: Filtrage, partie 1
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/H13CJ2vm_)

# Filtrage
- Domaines spatial et frequentiel
- Lissage, elimination du bruit
- Detection de bords/coins

# Quelques filtres classiques
- On s'appuie souvent sur le produit de convolution
    - Matrice avec des coefficients
- On va recalculer la valeur d'un pixel en fonction de son voisinage
    - Combinaison lineaire de tous les pixels voisins

![](https://i.imgur.com/b12LazZ.png)

# Lissage, debruitage
*Comment eliminer le bruit dans une image* ?

- Filtre moyenneur
    - Objectif: lisser l'image
        - Donne une impression de flou
    - Fonctionnement: on remplace la valeur d'un pixel par la moyenne des valeurs des pixels du voisinage
    - Noyau de convolution:

$$
\frac{1}{9}
\begin{bmatrix}
    1 & 1 & 1\\
    1 & 1 & 1\\
    1 & 1 & 1\\
\end{bmatrix}
$$

*Comment choisir la taille/forme du voisinage ?*
On reste generalement sur des voisinages carres par soucis de performance

## Resultats:
![](https://i.imgur.com/zAbB8u9.png)

![](https://i.imgur.com/VeJpVEO.png)
Un leger flou apparait.
 
Si on continue et qu'on augmente la taille du masque:
![](https://i.imgur.com/pK4lAYT.png)
Le lissage est *un peu trop fort* et on perd des details.

## Implementation
- Comment implementer un tel filtre ?
    - Double boucle
- Que faire sur la bordure
    - On ne traite pas les bords
    - Recalculer sur la bordure avec des coeffs differents
    - Dupliquer les dernieres et premieres lignes/colonne
    - Image periodique: chercher les valeurs sur une autre periode
    - $\Rightarrow$ il n'y a **pas** de bonnes reponses

## Amelioration?
- Au lieu de faire contribuer tous les pixels egalement, on peut privilegier les pixels proches du centre 
    - Filtre Gaussien

## Filtre Gaussien
- Objectif: lisser l'image
- Fonctionnement: on remplace la valeur d'un pixel par la moyenne ponderee des valeurs des pixels du voisinage
- Noyau de convolution: gaussienne
- Parametre/Taille du noyau ?

### Resultat
Comparaison ave le filtre moyenneur
![](https://i.imgur.com/AOfpH4d.png)
- Avantages/inconvenients ?
    - moins l'impression de flou
    - bonne amelioration

## Filtre Median
- Objectif: debruitage
- Fonctionnement: trier l'ensemble des valeurs des intensites des pixels sur un voisinage puis remplacer la valeur du pixel considere par la valeur mediane sur le voisinage

### Resultat
- Supprime facilement le bruit impulsionnel
- Preserve l'information de contour
- Est un peu lourd (tri)

![](https://i.imgur.com/0TnBTHw.png)
> Je suis pas du tout narcissique

On a completement enleve le bruit *"poivre et sel"* de la 2$^{\text{nde}}$ image

# Lissage
- Lissage (gaussien, moyenne...)
    - Degrade les frontieres
    - Solutions ?
        - Faire contribuer principalement les pixels qui ont une couleur proche de la couleur du pixel considere ou ponderer leur apport en fonction de leur couleur
        - Filtre de Nagao
        - ...

Filtre gaussien, resultats:
![](https://i.imgur.com/8XxAQ0f.png)

Gaussien selectif: seuil pour faire contribuer les pixel (si c'est inferieur, on les fait contribuer, sinon on les oublie).
- Permet de preserver les contours

<div class="alert alert-warning" role="alert" markdown="1">
Seuil a fixer
- S'il est trop tolerant: tend vers le gaussien normal
- Pas assez tolerant: reste sur l'image originale
</div>

## Nagao
- Filtre de Nagao
    - Tenir compte des regions?
    - Faire un median mais dans la region de variance faible

Au lieu de prendre un masque centre sur le pixel, on va regarder sur differents voisinages
![](https://i.imgur.com/5ntjuRp.png)

On calcule la variance a chaque zones rouges
- On calcule la moyenne sur le voisinage avec la variance la plus faible
    - On ne veut pas faire une moyenne a cheval sur un contour

### Resultats
![](https://i.imgur.com/ucWqvXy.png)
Nagao: on a fortement lisse l'image mais on a garde les contours

# Detection de bords
- Comment se caracterise un contour ?
- Comment trouver les contours ?
- Pourquoi trouver les contours ?

![](https://i.imgur.com/vNlCUYq.png)

![](https://i.imgur.com/DMoUJD5.png)

<div class="alert alert-info" role="alert" markdown="1">
Definir la notion de bord/contour
</div>
- Transition brutale (echelon)
    - En "escalier"
    - Dans la vraie vie, jamais aussi brutale

![](https://i.imgur.com/aY53lbS.png)

- Quelle operation realiser pour detecter ce type de motif?

![](https://i.imgur.com/dybTRHi.png)

<div class="alert alert-success" role="alert" markdown="1">
Calcul de la derivee ?

$$
\lim_{x_0\to x}\frac{f(x_0)-f(x)}{x_0-x}
$$

Si l'accroissement est plus fort en $y$ que en $x$, on calcul le coefficient directeur. Quand la porte est tres fort, on a un contour.
</div>

![](https://i.imgur.com/Jvpljnx.png)

$$
\frac{\delta f(x,y)}{\delta x} =
$$

![](https://i.imgur.com/6pLZ576.png)

$$
\frac{\delta f(x,y)}{\delta y} =
$$

![](https://i.imgur.com/RhNVFhg.png)

<div class="alert alert-warning" role="alert" markdown="1">
Vecteur directeur en tout point de la courbe
</div>

## Calcul de la derivee
En continu on a $\lim_{h\to 0}\frac{f(x + h) - f(x)}{h}$ et on veut calculer ca correctement en dirscret.

Profil:
![](https://i.imgur.com/xYvN1Zf.png)

Derivee:
![](https://i.imgur.com/6fxbqXs.png)

- recherche de maxima locaux ?

### Calcul de la derivee en 1 point x
- En continu: $\lim_{h\to 0}\frac{f(x + h) - f(x)}{h}$
    - En discret on a du mal a aller vers 0
    - En discret on a $\frac{f(x+1)-f(x)}{1}$
- Dans notre cas (discret)
    - $f'(x)=(f(x+1)-f(x))$ ou $\frac{1}{2}\times (f(x+1)-f(x-1))$
    - Masques: $[-1;1]$, $\frac{1}{2}[-1;0;1]$
    - Attention signal 2D

## Roberts
- Filtre de Roberts

$$
r(x,y) = \sqrt{(i(x,y)-i(x-1,y-1))^2} + \sqrt{(i(x,y-1)-i(x-1,y))^2}\\
r(x,y) = \vert i(x,y)-i(x-1,y-1)\vert + \vert i(x,y-1)-i(x-1,y)\vert
$$

<div class="alert alert-warning" role="alert" markdown="1">
Contours pas forcement nets
</div>

## Sobel, Prewitt
Filtres beaucoup plus communs.
Sobel:
![](https://i.imgur.com/t27HcMm.png)

![](https://i.imgur.com/HVkDsN3.png)

Prewitt:
![](https://i.imgur.com/Bowe9WT.png)

![](https://i.imgur.com/08vblZV.png)

*Pourquoi ces coefficients ?*
<div class="alert alert-success" role="alert" markdown="1">
On inclut le lissage
</div>

La difference:
- lisser par un filtre moyenneur / Sobel
- lisser par un filtre Gaussien / Prewitt

### Resultats
![](https://i.imgur.com/TLWs6Ik.png)

Sobel
![](https://i.imgur.com/YRUEmI5.png)

Prewitt
![](https://i.imgur.com/yQS7PcX.png)

$$
\frac{\delta f(x,y)}{\delta x}\\
\frac{\delta f(x,y)}{\delta y}
$$

On peut combiner les derivees:
1. calculer amplitude du gradient
2. calculer l'angle

$$
\sqrt{sx^2+sy^2}\\
tan^{-1}(\frac{sy}{sx})
$$

Informations sur l'orientation du gradient

*Comment recuperer les contours a partir de l'image du gradient ?*

On peut combiner les 2 images
![](https://i.imgur.com/X45iOoZ.png)

- Le vecteur gradient est orthogonal aux lignes de niveaux
- plus sa norme est grande plus la transition est forte
- On cherche une transition maximale

Differentes strategies pour recuperrer les contours:
- Seuillage
- Seuillage par hysteresis
    - On cherche un seuil pour un profil 
    - On garde tout au dessus du seuil et on jette tout en dessous
    - ![](https://i.imgur.com/b6vrWqu.png)
    - On inclut le motif a droite qu'on ne veut pas garder
    - Pour regler ce probleme on utilise 2 seuils 
        - un seuil haut
        - un seuil bas
    - On a une 1$^{ere}$ binarisation avec le seuil haut
        - On perd de l'info
        - On enleve le motif qu'on veut pas
    - Le seuil tolerant garde beaucoup plus d'infos
    - Hysteresis: on garde tous les resultats des seuils tolerant qui ont un contact avec le seuil haut
    - ![](https://i.imgur.comazO2iO.png)

- Recherche de lignes de crete

![](https://i.imgur.com/t0UFoPz.png)

<div class="alert alert-warning" role="alert" markdown="1">
Probleme:
- Contour ferme/contour ouvert ?
</div>

## Kirsch, Robinson
Kirsch and Robinson **Compass** Masks (Filtres de compas):

<div class="alert alert-info" role="alert" markdown="1">
On fait "tourner" le filtre.
</div>

![](https://i.imgur.com/8I91VMJ.png)

![](https://i.imgur.com/P5nRGY9.png)
> "Sobel que l'on fait tourner"


L'amplitude est donnee par la plus forte reponse.

L'orientation est deduite du masque qui a donne la plus forte reponse.

## Frei-Chen
Permet de trouver les gradients et d'autres motifs (lignes croises, point, etc.)

|Edge|Line||
|-|-|-|
|1.$$\frac{1}{2\sqrt 2}\begin{bmatrix}1&\sqrt2&1\\0&0&0\\-1&-\sqrt 2&-1\end{bmatrix}$$|5.$$\frac{1}{2}\begin{bmatrix}0&1&0\\-1&0&-1\\0&1&0\end{bmatrix}$$|9.$$\frac{1}{3}\begin{bmatrix}1&1&1\\1&1&1\\1&1&1\end{bmatrix}$$|
|2.$$\frac{1}{2\sqrt 2}\begin{bmatrix}1&0&-1\\\sqrt 2&0&-\sqrt 2\\1&0&-1\end{bmatrix}$$|6.$$\frac{1}{2}\begin{bmatrix}-1&0&1\\0&0&0\\1&0&-1\end{bmatrix}$$||
|3.$$\frac{1}{2\sqrt 2}\begin{bmatrix}0&-1&\sqrt 2\\1&0&-1\\-\sqrt 2&1&0\end{bmatrix}$$|7.$$\frac{1}{2}\begin{bmatrix}1&-2&1\\-2&4&-2\\1&-2&1\end{bmatrix}$$||
|4.$$\frac{1}{2\sqrt 2}\begin{bmatrix}-\sqrt 2&-1&0\\-1&0&1\\0&1&-\sqrt 2\end{bmatrix}$$|8.$$\frac{1}{2}\begin{bmatrix}-2&1&-2\\1&4&1\\-2&1&-2\end{bmatrix}$$||

9 masquent qui forment une base
- Chaque sous-famille est capable de detecter un motif localement

<div class="alert alert-info" role="alert" markdown="1">
La detectection se fait seulement avec:
$$
\frac{1}{2\sqrt 2}\begin{bmatrix}1&\sqrt2&1\\0&0&0\\-1&-\sqrt 2&-1\end{bmatrix}\text{ +rotations a }90^o\\
\theta=\arccos\biggr(\sqrt{\frac{\sum_{k=1}^4(W_k\times I)^2}{\sum_{k=1}^9(W_k\times I)^2}}\biggr)
$$

Plus $\theta$ est grand, moins la bordure est marquee ($\theta$ est entre 0 et $\pi$).
</div>

Avantages:
- Plus robuste a differents niveaux d'illumination
- Plus robuste car elimine les motifs lignes, points, etc. de la detection
- Peut etre utilise pour detecter les lignes en utilisant les masques 5 a 8 a la place des masques 1 a 4

## Le laplacien
Utilisation de la derivee seconde
- Un point de contour est un passage a zero de la derivee seconde

Derivee seconde:
$f$: ![](https://i.imgur.com/1W91uN4.png)

$f'$: ![](https://i.imgur.com/1yoxfj7.png)

$f''$: ![](https://i.imgur.com/rcLLSXg.png)

<div class="alert alert-danger" role="alert" markdown="1">
Un point de contour n'est rien d'autre qu'un passage de la derivee seconde par 0.
</div>

<div class="alert alert-info" role="alert" markdown="1">
Calcul du laplacien
- $f'(x)=f(x+1)-f(x)$
    - $\frac{f(x+1)-f(x)}{1}$
- $f''(x) = (x+1)-f'(x)$
- $f''(x = f(x+2)-f(x+1)-f(x+1)+f(x)$
</div>

<div class="alert alert-success" role="alert" markdown="1">
On obtient un masque simple:

$$
f''(X) = f(X+1)-2\times f(X)+f(X-1)
$$

![](https://i.imgur.com/pHNSBb6.png)

</div>

Si on veut detecter les contours, il faut chercher les passage par 0 du resultat:
![](https://i.imgur.com/vtfnVm3.png)

On a somme le masque horizontal et vertical

<div class="alert alert-warning" role="alert" markdown="1">
Les contours sont reperes par un changement de signe
</div>

On va plutot chercher un changement de signe (de forte amplitude)

![](https://i.imgur.com/sC3xk0e.png)
Si $E\gt0$ il faut un des $A,B,C$ ou $D\lt0$ et inversement si $E\lt 0$

- La calcul des derivees est approche au moyen de filtres
    - Simple et rapide
    - Inconvenients: approximation, sensibilite au bruit, en particulier le Laplacien $\rightarrow$ necessite de lisser le signal avant ou lors de la derivation
- Impact du lissage
    - Robustess au bruit
    - Delocalisation des points de contour
- Le Laplacien est sensible au bruit $\to$ sur-segmentation

Evaluation de la qualite de detection de contours:
- Bonne detection
- Bonne localisation
- Reponse unique

> Cf filtre de Canny/Deriche

# Detection de points d'interest
- Detection de coins
    - Comment se caracterise un coin ?
    - Comment trouver les coins ?
    - Pourquoi trouver les coins ?

<div class="alert alert-info" role="alert" markdown="1">
Coin = gradient fort dans 2 directions
</div>

![](https://i.imgur.com/K9aUWRu.png)

![](https://i.imgur.com/Tr3lDlR.png)

![](https://i.imgur.com/Mg64UFJ.png)

## Moravec
Pour chaque point:
1. On fait la somme $S$ des differences des intensites entre un voisinage centre sur le point et le voisinage decale
2. On reitere le calcul avec des decalages dans toutes les directions
3. Pour chaque point, on garde, parmi tous les decalages $i$ le resultat de $S_i$ qui a donne la plus faible valeur

![](https://i.imgur.com/rNTh3VB.png)

Moravec:
- Calcul d'un critere sur toute l'image

$$
c_{d_x,d_y}(x,y) = \sum_{i=-s...+s}\sum_{j=-s...+s}(I(x+i, y+j)-I(x+i+d_x,y+j+d_y))^2
$$

- On calcul un critere pour chaque point

$$
c(x,y)=\min_{d_x,d_y}(c_{d_x,d_y}(x,y))
$$

<div class="alert alert-success" role="alert" markdown="1">
Un coin est un maximum local de $c(x,y)$
</div>

Desavantages:
- Sensible au bruit (des petites imperfections peuvent etre prises pour des coins)
- Contours de certaines directions peuvent etre pris pour des coins (anisotrope car on considere que quelques directions)

## Harris
Revision du critere pour etre plus robuste

$$
c_{d_x,d_y}=\sum_{i=-s...+s}\sum_{j=-s...+s}w(i,j)(I(x+i,y+j)-I(x+i+d_x,y+j+d))^2\\
I(x+d_x,y+d_y)\simeq I(x,y)+d_x\biggr(\frac{\delta I(x,y)}{\delta x}\biggr)+d_y\biggr(\frac{\delta I(x,y)}{\delta y}\biggr)+...\\
c_{d_x,d_y}=\sum_{i=-s...+s}\sum_{j=-s...+s}w(i,j)\biggr(d_x\biggr(\frac{\delta I(x+i,y+j)}{\delta x}+d_y\frac{\delta I(x+i,y+j)}{\delta y}\biggr)\biggr)^2
$$

Critere:
$$
c_{d_x,d_y}=\sum_{i=-s...+s}\sum_{j=-s...+s}w(i,j)\biggr(d_x\frac{\delta I(x+i, y+j)}{\delta x}+d_y\frac{\delta I(x+i,y+j)}{\delta y}\biggr)^2\\
\biggr(d_x\frac{\delta I(x+i, y+j)}{\delta x}+d_y\frac{\delta I(x+i,y+j)}{\delta y}\biggr)^2
$$

$$
\biggr(d_x\frac{\delta I(x+i, y+j)}{\delta x}+d_y\frac{\delta I(x+i,y+j)}{\delta y}\biggr)^2 = (d_x,d_y)
\begin{pmatrix}
    (\frac{\delta I}{\delta x})^2 &(\frac{\delta I}{\delta x\delta y})\\
    (\frac{\delta I}{\delta x\delta y}) & (\frac{\delta I}{\delta y})^2
\end{pmatrix}
\begin{pmatrix}
d_x\\
d_y
\end{pmatrix}
$$

Ce qui donne:

$$
Ad+x^2+2Cd_xd_y+Bd_y^2\\
M=
\begin{pmatrix}
    A&C\\
    C&B
\end{pmatrix}=
\begin{pmatrix}
    (\frac{\delta I}{\delta x})^2 &(\frac{\delta I}{\delta x\delta y})\\
    (\frac{\delta I}{\delta x\delta y}) & (\frac{\delta I}{\delta y})^2
\end{pmatrix}
$$

- Avec $w$ une gaussienne

Nouveau critere H
- $H=det(M)-\alpha$ trace $(M)^2$
- $\lambda_1$ $\lambda_2$ les deux valeurs propres
    - $det(M)=\lambda_1\lambda_2$ et $trace(M)=\lambda_1+\lambda_2$
- $H=\lambda_1\lambda_2-\alpha(\lambda_1+\lambda_2)^2$
    - $H\lt0$ contour
    - $H\to0$ ras
    - $H\gt\gt0$ coin
- $\alpha$ grand $\Rightarrow$ $H$ diminue et le detecteur est moins sensible
- $\alpha$ petit $\Rightarrow$ $H$ diminue et le detecteur est plus sensible

## Achard, Bigorgne, Devars
- Detection basee sur le produit vectoriel
    - Pres d'un coin, la norme du produit vectoriel entre 2 vecteur gradient est grande
    - Dans une zone homogene elle est faible
        - La norme des vecteurs gradients est petite
    - Sur un contour elle est faibke aussi
        - L'angle frome entre 2 vecteurs gradients proches est petit 

<div class="alert alert-info" role="alert" markdown="1">
Pour chaque point $i$, avec un voisinage $V_i$, on determine un critere $k$:

$$
k=\sum_{j\in V_i}\Vert\overrightarrow{grad(P_i)}\Vert^2\Vert\overrightarrow{grad(P_j)}\Vert^2\sin^2(\widehat{grad(P_i),grad(P_j)})
$$
$$
\begin{aligned}
&I_x=\biggr(\frac{\delta I}{\delta x}\biggr) &\Vert\overrightarrow{grad(P)}\Vert^2=I_x^2+I_y^2\\
&\widehat{\sin(ox,grad(P)})=\frac{I_y}{\sqrt{I_x^2+I_y^2}} &\widehat{\cos(ox,grad(P)})=\frac{I_y}{\sqrt{I_x^2+I_y^2}}\\
&k=I_x^2<I_y^2>+I_y^2<I_x^2>-2I_xI_y<I_xI_y> &<I>I\times
\begin{pmatrix}
1&1&1\\
1&0&1\\
1&1&1
\end{pmatrix}
\end{aligned}
$$
</div>

## Resultats
Archard
![](https://i.imgur.com/vnTK2If.png)

# Amelioration de la nettete
## Laplacien
- Retour sur la derivee seconde (Laplacien)

$f$: ![](https://i.imgur.com/1W91uN4.png)

$f'$: ![](https://i.imgur.com/1yoxfj7.png)

$f''$: ![](https://i.imgur.com/rcLLSXg.png)

$$
f''(X) = f(X+1)-2\times f(X)+f(X-1)
$$

![](https://i.imgur.com/pHNSBb6.png)

### Renforcement de la nettete

![](https://i.imgur.com/ZHSFRm2.png)


$-f''$: ![](https://i.imgur.com/N6wZ2XG.png)
Ce qu'on ainerai c'est combine $f$ et $-f''$ pour ecarter les amplitudes des extremums avant et apres

![](https://i.imgur.com/5hkUJB7.png)

On prend $f$ et lui on lui retranche $k$ fois la derivee seconde pour accroitre le contraste locale

$f$: ![](https://i.imgur.com/qZhGawq.png)

$-kf''$: ![](https://i.imgur.com/2mtqQlr.png)


$f-kf''$: ![](https://i.imgur.com/OpBCIhY.png)

Masque pour le Laplacien
![](https://i.imgur.com/HoLsbCE.png)

<div class="alert alert-warning" role="alert" markdown="1">
Rajouter $+1$ au centre c'est comme rajouter l'image complete
</div>

## Resultats
- Augmente la nettete
- Renforce le bruit

![](https://i.imgur.com/j75XvRD.png)

![](https://i.imgur.com/oLrHetu.png)

C'est l'inverse de ce qu'on a fait au debut

# Conclusion
<div class="alert alert-danger" role="alert" markdown="1">
Tout ce qu'on a fait jusqu'a present est faux car on a pas pris en compte la correction gamma.
</div>