---
title:          "TIFO: Le bruit"
date:           2021-03-11 16:00
categories:     [Image S8, TIFO]
tags:           [Image, TIFO, S8]
description: Le bruit
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/B1A2futQO)

# Modelisation
Amelioration vs restauration:
- Amelioration: on ne sait pas ou on va
- Restauration: on a un modele que l'on souhaite atteindre

Modele de degradatation (dans le domaine spatial)
- $I_{\text{deg}}=h*I_{\text{ori}} + n$
    - $h\to$ la degradation (optique, flou...)
    - $n\to$ le bruit

# Le bruit
<div class="alert alert-info" role="alert" markdown="1">

$$
I_{\text{deg}} = h*I_{\text{ori}} + n
$$
</div>
On regarde $n$.

Genant pour le cote esthetique que pour les traitements $\Rightarrow$ Il faut donc reduire ce bruit

- Reduction de bruit
    - Estimation ?
        - Connaissances a priori ou pas
    - Reduction
        - Sans degrader le signal...

## Bruit additif
On considere souvent ici le bruit additif

Fonction de repartition peut varier:
- Gaussienne, (impulsion) periodique

## Estimation
Soit le capteur est connu:
- Photos d'une zone bien homogene dans de bonnes conditions d'eclairement

Soit le capteur pas connu:
- Analyse de quelques zones

### Exemple
![](https://i.imgur.com/JWqXa9Z.png)

![](https://i.imgur.com/WveTZMB.png)
On cherche dans les zones les plus homogenes l'ecart-type des valeurs.

## Reduction
Revisite des filtres classiques
- Mean filter
    - Arithmetic mean
    - Geometric mean
    - Harmonic mean
    - ...
- Median + variantes
    - Midpoint, alpha-trimmed
- Adaptative
    - Gaussien selectif
    - ...

Approche par ondelette
- l'image $f(n)$ est bruite par $q(n)$
    - $g(n)=f(n)+q(n)$
- L'estimation de la correction
    - $F_c=W^{-1}T_{\lambda}Wg$
    - $T_{\lambda}p(y)=p(y)$ si $\vert p(y)\vert\gt\lambda$, $0$ sinon
    - $T_{\lambda}p(y)=p(\lambda)\pm\lambda$ si $\vert p(y)\vert \gt \lambda$, $0$ sinon

![](https://i.imgur.com/J9nsXKg.jpg)

Resultat:
![](https://i.imgur.com/3CMeUYu.jpg)

- ToS (Tree of Shape)
    - Bruit = feuilles dans l'arbre
    - Couper les feuilles de l'arbre pour affiner le resultat
- NLMeans
    - Au lieu de faire la moyenne sur un voisinage, on cherche des patchs ressemblants

![](https://i.imgur.com/DrZb1ic.png)

Resultats:
![](https://i.imgur.com/5bFTIaI.jpg)
On a une image a laquelle on rajoute du bruit et qu'on debruite avec NLMeans

### Degradation periodiques
![](https://i.imgur.com/NMdUp9X.png)
> Moi devant les cours de TIFO quand je me dit que je reviserai plus tard

Spectre (eclairci):
![](https://i.imgur.com/UJUaDvo.png)

On a des taches aux coins qui apparaissent.

*Definition du filtre dans le domaine frequentiel:*
On fait un rejecteur (on met a 0 des frequences precises dans le spectre)
![](https://i.imgur.com/fi2LXzW.png)
> Fait un peu grossierement

On multiplie le spectre et l'image obtenue par le filtre, supprimant theoriquement l'origine des degradations periodiques:
![](https://i.imgur.com/sHWB6tY.png)

Resultat:
![](https://i.imgur.com/afvmGff.png)

Si on fait la difference entre l'image d'origine et debruitee:
![](https://i.imgur.com/xREJlLG.png)

# La partie convolutionnelle
- Le bruit: $I_{\text{deg}} = h*I_{\text{ori}} + n$
    - On regarde $h$
    - Degradations convolutionnelles comme du flou de bouge
- Reduction $\Leftrightarrow$ deconvolution
    - Blind deconvolution: Seul $I_{\text{deg}}$ connu
    - Non-Blind deconvolution: $I_{\text{deg}}$ et $h$ sont connnus

Degradation:
- $g=h*f+n$

Passage en frequentiel:
- $G(u,v)=H(u,v)F(u,v)+N(u,v)$
    - $h\to$ point spread function (PSF)

Estimation de $F$ (l'image non bruitee)
- On a envie de dire: $g=h*f$ d'ou une solution "facile"
    - $F_e(u,v)=\frac{G(u,v)}{H(u,v)}$
- Toutefois, il y a le bruit additif
    - $F_e(u,v)=F(u,v)+\frac{N(u,v)}{H(u,v)}$
    - Quand $H\to0$, $\frac{N}{H}\to+\infty$ $\Rightarrow$ limiter le support

<div class="alert alert-success" role="alert" markdown="1">
Solution:

$$
F_e(u,v)=F(u,v)+\frac{N(u,v)}{H(u,v)}
$$

</div>
- $h/H$ connu ou pas?

## Filtre de Wiener
- Mean square error entre $f$ et $f_e$: $e=E[(f-f_e)^2]$
- On cherche $W$ tel que:
    - $\frac{1}{NM}E[\vert F-F_e\vert^2]$ soit $\min$
    - $F_e=WG=WHF+WN$
    - $F-F_e=(1-WH)F-WN$
    - $e=\frac{1}{NM}\sum\sum\vert (1-WH)F-WN\vert^2$
- Expression en frequentiel de $f_e$ (en fonction de $H$) en derivant e en fonction de $W$

$$
F_e = \biggr[\frac{1}{H}\frac{\vert H\vert^2}{\vert H\vert^2+\frac{\vert N\vert^2}{\vert F\vert^2}}\biggr]G
$$

<div class="alert alert-info" role="alert" markdown="1">
Filtre de Wiener:

$$
w = \biggr[\frac{H^c}{\vert H\vert^2+\underbrace{\frac{\vert N\vert^2}{\vert F\vert^2}}}_{=K}\biggr]
$$

</div>

Probleme: $\frac{\vert N\vert^2}{\vert F\vert^2}$ pas connu $\rightarrow$ mais considere constant $K$

# Degradation
- *Comment determiner $H$ ?*
    - Faire une image d'une impulsion $\to$ determine entierement $H$
    - Analyser une image et essayer de determiner sur des frontieres ou des impulsions la reponse $H$
    - Modeliser la degradation (flou de bouger...)

$\to$ Tres difficile la plupart du temps

# Quantification des resultats
- Rapport signal sur bruit SNR
    - $\sum\vert F(u,v)\vert^2\sum\vert N(u,v)\vert^2$
- Mean Square Error MSE entre l'image et l'estimation
    - $\frac{1}{N}\sum (f(x,y)-f_e(x,y))^2$
    - Note: SNR=$\sum\frac{(fe(x,y)^2)}{MSE}$

# Conclusion
- Restauration, amelioration
    - Difficile dans le cas general