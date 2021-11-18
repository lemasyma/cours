---
title:          "IMED2: Reconstruction tomographique - quand rien n'est ideal"
date:           2021-11-17 10:00
categories:     [Image S9, IMED2]
tags:           [Image, S9, IMED2]
math: true
---

Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/H10hNcJ_t)

# Les hypotheses fortes de FBP

> Beaucoup trop ideal

- La ligne est supposee connue
    - Autrement dit: on a recupere $p$ dans $I=I_0e^{-p}$ .. ou plutot dans $I=\int I_0(E)e^{-p(E)}dE$
- Le detecteur n'a aucun defaut (la mesure est supposee parfaite)
    - Or un detecteur est loin d'etre parfait
- Un photon qui atteint le detecteur est un photon qui vient de la source
    - Or le rayonnement diffuse ne respecte pas cette hypothese
- L'objet est statique pendant l'acquisition
    - Or un patient respire, ses organes bougent, ses vaisseaux pulsent...
- L'objet est integralement vu sous toutes les angulations
    - Nous parlerons de ce sujet et d'autres sujets lies a l'echantillonnage au prochain cours !

<div class="alert alert-info" role="alert" markdown="1">
Problematiques de troncation
</div>

## Non-idealite du tube

![](https://i.imgur.com/Xo0pWLy.png)

<div class="alert alert-danger" role="alert" markdown="1">
Les basses energies sont absorbees en permier: a mesure qu'on traverse des epaisseurs de materiaux, le spectre se reduit vers les hautes energies: l'energie moyenne du spectre augmente, on appelle ce phenomene le durcisement du faisceau
</div>

## Non-idealite du detecteur

> Les problemes de la radiographie 2D... sont aussi les problemes de tomographie !
> 
![](https://i.imgur.com/HRcstpX.png)

![](https://i.imgur.com/7I7QglO.png)

- \+ spread dans le detecteur
- \+ Reponse differente en fonction de l'energie du photon
- \+ ...

*Comment on envisagerait de reparer ces artefacts circulaires ?*
> Changer de detecteur (mais c'est cher)
> Compenser le phenomene

*Avec quelle methode ?*

<div class="alert alert-success" role="alert" markdown="1">
Avec la transformee de *Hoff*
</div>

C'est une transformee qui detecte les lignes, utile dans la projection polaire

*Comment on recupere les nouvelles colonnes ?*
> On regarde le gradient

Quand on travaille dans le sinogram, toutes nos colonnes sont traitees de la meme facon.

On peut travailler dans 2 domaines:
1. Le domaine image
2. Dans le sinogramme
    - Besoin de plus de finesse mais detection plus robuste

$$
\begin{aligned}
\bar p &= -log(\frac{I}{I_0})\quad I = P+S\\
&= \log(I_0) - \log(P+S)\\
&= \log(I_0) - \log(P(I+\underbrace{\frac{S}{P}}_{\color{red}{\text{SPR} \\ \text{scatter-to-primaray} \\ \text{ratio}}}))
\end{aligned}
$$

<div class="alert alert-success" role="alert" markdown="1">

$$
\bar p = p_{\text{tree}} - \log(1+SPR)
$$

</div>


## Interactions avec la matieres et rayonnement diffuse

> Ennemi public numero 1 de la tomographie RX

![](https://i.imgur.com/iqWTSGp.png)

![](https://i.imgur.com/Ix0l4ik.png)

Rejection de diffuse:
1. Augmenter l'air gap
2. Reduire le champ de vue (collimation)
3. Inserer une grille anti-diffuse

![](https://i.imgur.com/AFgl8Uo.png)

C'est aussi un probleme en 2D:

![](https://i.imgur.com/FS79oRA.png)

*Est-ce que ca fait sens de forcer les contrastes en imagerie medicale ?*
> Oui !
> Il faut que le contraste de l'image global soit confortable

![](https://i.imgur.com/QFJy2c2.png)

*Comment fixer cette image ?*
> Estimer la non-uniformite

On a en non-uniformite pure:

![](https://i.imgur.com/E803qdK.png)

Si on applique la correction, on a:

![](https://i.imgur.com/1rLFlPA.png)

*Qu'est-ce qu'on a comme defaut ?*
> La forte surbrillance sur le bord
> L'arc de cercle
> Les niveaux de gris en bas de l'image sont un peu plus clairs, on a presque trop corrige notre image

<div class="alert alert-warning" role="alert" markdown="1">
Il faut faire attention avec ces methodes: ca peut etre pratique d'un POV visuel mais il ne faut pas creer de nouveaux artefacts
</div>

Plein de gens on travaille sur des methodes pour corriger ces artefacts, l'un est la **retroprojection differenciee**.

<div class="alert alert-success" role="alert" markdown="1">
Et ca, c'est magique !
</div>

![](https://i.imgur.com/T0I71hW.png)

<div class="alert alert-warning" role="alert" markdown="1">
On a l'impression que l'axe horizontale est privilegie
</div>

*Qu'est-ce qui nous donne une information ligne a ligne ?*

On est en train de dire que les lignes sont exactement les memes.

Comme algorithme, on prend notre projection, on prend la projection ligne a ligne et on retroprojecte ca

$$
p\to\delta_u p\to\boxed{DBP}\to\text{ligne}(i) = -2\pi \mathcal Hf[\text{row#}i]\\
\mathcal H[\mathcal H[f]] = -f
$$

Avec $\mathcal H$: transformee de Hilbert

Ici, elle est mal calculee: ![](https://i.imgur.com/rbyJtJZ.png)

Prenons par exemple la ligne $100$: on sait que notre objet est fini.

*Pourquoi c'est interessant ?*


Si notre objet est gros est qu'on a  qu'un champ de vue (notre objet depasse), on fait une retroprojection differenciee et on inverse toutes les lignes de notre vue.

<div class="alert alert-success" role="alert" markdown="1">
On arrivera a reconstruire notre vue, tant bien meme que l'objet est tronquee

![](https://i.imgur.com/2I80fiI.png)

</div>

## Mouvement et incoherence des donnees

> Catastrophique en image de bas de contrastes (tissus mous) comme en imagerie vasculaire

![](https://i.imgur.com/X6xidrx.png)

![](https://i.imgur.com/QkwlEyC.png)

![](https://i.imgur.com/UhCZ30z.png)
