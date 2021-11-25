---
title:          "IMED2: Registration in medical imaging"
date:           2021-11-25 9:00
categories:     [Image S9, IMED2]
tags:           [Image, S9, IMED2]
math: true
---

Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/H10hNcJ_t)

<div class="alert alert-info" role="alert" markdown="1">
Cours de recalage d'image !
</div>

# GE Healthcare

*Qu'est-ce que c'est ?*

![](https://i.imgur.com/T7nYjNF.png)

> Un scanner !
> Mais c'est une question piege, c'est dur de savoir

![](https://i.imgur.com/DDyHAF4.png)

> Pour les echographie

![](https://i.imgur.com/8AhFYUg.png)

> Une radio dernier cri
> C'est portable, utile quand le patient ne peux pas etre bouge

## GE Healthcare in Buc

![](https://i.imgur.com/kiARd7k.png)

> Pour les mamographies

*Pourquoi on compresse le sein ?*
> Pour avoir moins de matiere a traverser

Les seins ont des tissus qui se superposent et qui sont super durs a analyser

Avant, on compressait le sein pour l'empecher de bouger, maintenant c'est parce qu'on fait de la 3D du sein

![](https://i.imgur.com/0pcKvWy.png)

<div class="alert alert-info" role="alert" markdown="1">
**AW**: station de revue dediee
</div>

## Le prof @ Healthcare

These sur:
- Le coeur
- Recalage

![](https://i.imgur.com/b6QNG2S.png)

> Ceci n'est pas un foie

## Ingenieur de recherche @ GE

1. Identification d'un besoin/manque/innovation repondant a un besoin clinique
2. Transformer la problematique clinique en un ensemble de problematiques techniques
3. Etude biblio sur les differents sujets techniques et identification des solutions les plus prometteuses
4. Preuve de concept technique et evaluation de la capacite de la solution technique a resoudre le probleme clinique
5. Rendre robuste la preuve de concept a l'ensemble des conditions d'utilisation potentielles
6. Etablissement d'une strategie de verification et de validation de la technique
7. Support pour le lancement du produit, la generation d'evidence clinique et gestion de potentiels problemes

# 3D/2D registration of coronary arteries

## Coronary artery disease

![](https://i.imgur.com/lpjKVkL.png)

On peut avoir une artere avec une section bien moins importante
- Si le sang passe moins bien, les tissus qui se nourrit par cette artere seront beaucoup moins nourris
- Douleur a l'effort, etc.

Souvent, quand on a des douleurs a la poitrine apres l'effort, c'est le *premier symptome*: on a un vaisseau bouche

Sur l'image a droite, il y a une partie qui est compressee
- Si c'est une artere du coeur, on peut faire un infarctus

<div class="alert alert-info" role="alert" markdown="1">
Infarctus: le but est de retructurer les vaisseaux coronaires pour continuer a avoir du sang

> C'est pas forcement une mauvaise chose !
</div>

## Coronary artery bypass surgery

1. General anesthesia
2. Extract small artery/vein from leg or arm
3. Open rib-cage
4. Heart stopping
5. On-pump
6. Link aorta to occlusion distality
7. Off-pump + restart the heart
8. ~3 to 6 hours
9. ~1 to 2 weeks of hospitalization

![](https://i.imgur.com/bpjJBqb.png)

## Percutaneous coronary intervention

<div class="alert alert-success" role="alert" markdown="1">
Le genre d'operation qu'on fait plus aujourd'hui car moins couteux
</div>

*C'est quoi la difference entre les veines et les arteres ?*
> Les arteres envoient le sang depuis le coeur, ce sont des muscles qui pulsent au meme niveau que le coeur
> Si on se prend un coup et qu'on a un bleu, une veine a pete mes les arteres sont tranquilles
> Les veines le ramene et ne sont plus un muscle

![](https://i.imgur.com/GvfmKb0.png)

On amene un catether pour aller jusqu'a l'artere bouchee, on met un "balon" pour eviter que l'artere se rebouche

*Comment on gonfle le balon ?*

<div class="alert alert-danger" role="alert" markdown="1">
Il ne faut **JAMAIS** avoir de l'air dans les arteres

> C'est pour ca qu'on vide une seringue de quelques goutes, pour eviter les bulles d'air

</div>

<div class="alert alert-warning" role="alert" markdown="1">
L'air peut faire un caillot sanguin
</div>

<div class="alert alert-success" role="alert" markdown="1">
On gonfle le balon avec une solution saline, aka de l'eau
</div>

![](https://i.imgur.com/1itARsq.png)

> La machine pour visualiser l'interieur du patient

*Mais et en termes de rayons X ?*
> As Low As Reasonably Possible
> Aussi les patients sont deja malades, certes on augmente le risque de cancer mais aussi les chances de survies

*Et pour les medecins alors ?*
> Chaque medecin porte un tablier de plomb

![](https://i.imgur.com/cBa7Co6.jpg)

> Il y a egalement une vitre plombee (cf a tige au milieu finissant par un cercle)

<div class="alert alert-danger" role="alert" markdown="1">
Il y a beaucoup de choses auxquelles ont ne pense pas en tant qu'ingenieur dans nos locaux (la vitre prenant de la place, le nombre de personnes dans la salle, les moniteurs un peu partout, etc.)
</div>

![](https://i.imgur.com/wgFWykL.png)

*Pourquoi dans une video, les vaisseaux apparaissent et disparaissent ?*
> C'est en fonction de la solution pour les faire ressortir

<div class="alert alert-success" role="alert" markdown="1">
On injecte un *produit de contraste* (le metal le moins nocif, l'iode)
</div>

![](https://i.imgur.com/p1bwfvd.png)

*Le guide sort du vaisseau ?*

<div class="alert alert-danger" role="alert" markdown="1">
Quand ca arrive, c'est la merde.
</div>

> Dans ce cas, le vaisseau est **completement bouche**
> On creuse dans tous ce qui est bouche, et comme le sang ne passe pas, il n'y a pas de produit de contraste

*Il y a des methodes non-intrusives pour voir les veines ?*
> L'echo doppler
> Le scanner

![](https://i.imgur.com/Y5OqRka.png)


<div class="alert alert-info" role="alert" markdown="1">
Ce vaisseau est **l'aorte**

![](https://i.imgur.com/cycfBoY.png)

</div>

## Potential applications for enhanced visualization

<div class="alert alert-success" role="alert" markdown="1">
On va fusionner un objet 3D avec la surface 2D pour se reperer

![](https://i.imgur.com/Ml2MP56.png)

</div>

Mais tres gagdet et medecins pas fans :(

<div class="alert alert-success" role="alert" markdown="1">
Proposition plus simple: on segemente l'artere, on extrait la ligne centrale et on la "deplie", on peut visualiser ou on se situe

![](https://i.imgur.com/Znx2IJW.png)

</div>

Point de vue ingenieur: "Mais ca ressemble a ca non ?"

![](https://i.imgur.com/aZ3FDXv.png)

Point de vue medecin: "OH WOW TROP BIEN !"

# The registration problem

On veut *bouger* un truc en 3D pour le repositionner et le superposer de facon nickel.

![](https://i.imgur.com/GLY4qfD.png)

Aim at compensating:
- No link between imaging systems ![](https://i.imgur.com/rotA5kO.png)
- Patient motion
    - Position on the table
    - Repiratory motion
    - Beating heart

## General registration probleme

On a 2 objets:
- bleu
- rouge

On a une fonction de distance qui estime notre recalage, et on veut minimiser cette valeur

<div class="alert alert-danger" role="alert" markdown="1">
Avec une mamographie:

![](https://i.imgur.com/oh02eIV.png)
</div>

![](https://i.imgur.com/rie0vKX.png)


## The 3D/2D registration problem

![](https://i.imgur.com/KrKcdzS.png)

<div class="alert alert-warning" role="alert" markdown="1">
Difficulties due to vessels projection
</div>

![](https://i.imgur.com/UhlF0e8.png)

- "fake" bifurcations
- "late" bifurcations detection
    - On peut confondre 2 vaisseaux et detecter la difference tard
- projective foreshortening (self-superimposition)

## 2D vasculature extraction

*Combien de temps ca met a calculer ?*

<div class="alert alert-warning" role="alert" markdown="1">
Des plombes
</div>

![](https://i.imgur.com/Y3SyQT4.png)

![](https://i.imgur.com/q1iQCZJ.png)

*Et si on veut segmenter cette image ?*
> Detecter des frontieres


*Et pourquoi pas juste un seuillage ?*
> Ca peut etre trop simple pour que ca marche

<div class="alert alert-warning" role="alert" markdown="1">
Le niveau de gris des veines peut etre confondu avec celui du foie
</div>

On fait du pre-traitement: **remove background**

![](https://i.imgur.com/H8bfwJh.png)

<div class="alert alert-success" role="alert" markdown="1">
On utilise de la **morpho math**

![](https://i.imgur.com/nEUBaPA.png)

</div>

![](https://i.imgur.com/bYGXIqM.png)


<div class="alert alert-warning" role="alert" markdown="1">
On prend que les vaisceaux principaux (hysteresis thresholding)

![](https://i.imgur.com/qikP6dS.png)

</div>

Si ton montre ca a des gens: "C'est de la merde" (*mais c'est pas si pire*)

Avec la reconnexion:

![](https://i.imgur.com/ZIy9d5Y.png)

![](https://i.imgur.com/dPA3cvh.png)

## A qui appartiennent les donnees ?

Le patient ne peux pas faire l'image sans l'hopital et l'hopital ne peux pas faire sans le patient

<div class="alert alert-warning" role="alert" markdown="1">
Mais si c'est des organes, pas moyen de reconnaitre le patient
</div>

*Anonymiser les donnees ?*
> Possible de desanonymiser