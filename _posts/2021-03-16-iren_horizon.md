---
title:          "IREN: Tour d'horizon"
date:           2021-03-16 10:00
categories:     [Image S8, IREN]
tags:           [Image, Sante, IREN, S8]
description: Tour d'horizon
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/SkZAGl0Xu)

Note: projet en binome

[Index du cours](http://www.ricou.eu.org/iren/notes_rn.html)
# Cas d'utilisation
- Pub ciblee
- Recommendations (Netflix)
- Description (d'une image pour les personnes malvoyantes)
- Securite
- Diagnostique (traitement d'image medicale)
    - Ex: creation d'une IA qui detecte le cancer et a commence a detecter le cancer chez des personnes ou les medecins n'avaient rien trouve et les medecins ont decouvert des nouveaux marqueurs du cancer
- Jeux (bot pour les echecs)
    - Jeu de go: trop complexe pour tester toutes les possibilites
        - IA developpee qui s'est averee tres creative
- Majordome (Alexa, Google Home)
- Le telephone

# Historique
> L'IA n'est pas l'oeuf

![](https://i.imgur.com/2Pv3VJ7.png)
Les hivers ont bloque l'IA avant qu'elle redemarre

## Les hivers
![](https://i.imgur.com/lbqTCs8.png)
La renaissance est dues au triptique **données, hardware, théorie.**

Aujourd'hui: 3$^{\text{eme}}$ phase: **l'espoir**
- l'IA va regler tous les problemes du monde

<div class="alert alert-danger" role="alert" markdown="1">
L'IA est une *copie* du cerveau humain (au moins le principe de base)
</div>
Quand un enfant apprend, il a un flux de donnees continu (vue, ouie, etc.)

- Les GPUs ont evolues, developpe un parallelisme de choses a faire
- La theorie: comprehension globale et trucs locaux qui permet de tout faire marcher
    - On n'a **PAS** de base robuste
    - > Ca marche mais on sait pas pourquoi

# Plus gros c'est mieux

![](https://i.imgur.com/bPbcGNw.png)
Besoin de calculs pour l’entrainement et taille des réseaux

<div class="alert alert-warning" role="alert" markdown="1">
Plus notre reseau est gros, plus on a besoin de donnees
</div>

On peut reduire les reseaux de neurones, si une connection entre 2 neurones est trop faible on la supprime.

# Exemple d'une voiture autonome
ResNEt-50 a besoin de $7,72$ G operations pour traiter une image $255\times 255$
- $230$ Gops pour $30$ fps
- $9,4$ Tops pour du HD
- $338$ Topes pour $12$ cameras et $3$ couleurs par camera

Nvidia A100
1. Peak rates = GPU boost clock
2. Effective | using Sparsity

![](https://i.imgur.com/lO3o9qI.png)
Tensor core: extensions de Nvidia pour gerer Tensorflow (par supposition du prof)

# Les leaders
Les leaders les plusvisible sont
- Google (Tensorflow, Keras, DeepMind)
- Facebook (Torch, PyTorch)
- Microsoft (CNTK)
- IBM (Watson)
- Baidu

et bien sûr le principal fabriquant : NVidia (Cuda, CuDNN)

<div class="alert alert-info" role="alert" markdown="1">
**Ce qu'on voit moins**
A coté de ceux qui participent activement à la recherche et au
développement des outils, il y a ceux qui l’utilisent en interne.
- Amazon (Alexa, Amaxon Go)
- Apple
- Les constructeurs automobiles (Tesla, Uber, t o u s)
- tout ceux qui font du conseil (Netflix, Expedia...), de la pub (Criteo)
- plein de startups
</div>

# Types d'apprentissage
![](https://i.imgur.com/ts41OCQ.png)

## Apprentissage supervise
- On a un jeu d'image et on sait que l'image 4 c'est une forme
- On montre l'image au reseau (qui sortira une reponse au pif vu qu'il ne sait rien pour l'instant)
- On corrige le reseaux en donnant la reponse
- Le reseaux changent les poids des connexions pour s'adpater

### Exemple: le spam
On recoit un nouveau mail et le reseau de neurones determine si c'est un spam ou non, on le corrige s'il a faux
![](https://i.imgur.com/uzjNnPk.png)

|Regression|Classification|
|-|-|
|Moindres carres|SVM|
|Regression polynomiale|Regression logistique, arbre de decisions|
|Reseau neuronal|Reseau neuronal|

La revolution vient des reseaux neuronaux:
- Mur
- Demande des quantites enormes de donnees etiquettees
- Pas toujours simple à faire marcher
- De plus en plus complexe
- Produit des résultats remarquables en
    - traitement d’image
    - traitement de la parole

## Apprentissage non supervise
- classer des classes qu'on ne connait pas $\rightarrow$ **clustering**

![](https://i.imgur.com/DoyJvvD.png)
- $K$-moyennes, ACP, des reseaux de neurones
- Difficile d'en mesurer l'efficacite (besoin de juges humains)
- Usage limite mais en progres

<div class="alert alert-warning" role="alert" markdown="1">
Probleme: ne sait pas si ce qu'il a fait est ok ou non
- Ex; s'il classe par couluer au lieu de forme
- Besoin d'humains pour juger

</div>

## Apprentissage par renforcement
Lie aux jeux videos

![](https://i.imgur.com/tWW4n1D.png)
- Rules of the fame are unknown
- Learn directly from interactive game-play
    - Le jeu informe si on gagne ou perd
- Pick actions on joystick, see pixels and scores

### Points clefs du renforcement
- Pas de superviseur qui connait la solution, seulement une note
- Le retour d'information est decale (pas immediat)
- La notion de temps est importante $\rightarrow$ Systeme dynamique
- L'agent qui note a un impact sur la suite des donnees qu'on va recevoir

![](https://i.imgur.com/mM2eGBi.png)

# Test
Quel type d’apprentissage ?
- [Comparaison de CNN pour la vision sur route](http://www.ricou.eu.org/iren/iren/videos/YOLOv2_vs_YOLOv3_vs_Mask_RCNN_vs_Deeplab_Xception.mp4) - 2018
    - Apprentissage renforce (et pas supervise)
- [Appel au téléphone - Google](http://www.ricou.eu.org/iren/iren/videos/Google_Duplex.mp4) – 2018
    - Un "majordome" prend RDV
    - Plusieurs techniques en meme temps
    - Essentiellement du supervisé
- DeepMind StarCraft II [combat](http://www.ricou.eu.org/iren/iren/videos/DeepMind_StarCradtII_figth.mp4) et [explications](http://www.ricou.eu.org/iren/iren/videos/Deepmind-StarcradtII_explanation.mp4) - 2019
    - L'IA Deepmind Starcraft joue et controles ses persos (les bleus) contre un humain (les rouges)
    - L'IA ne joue pas plus vite que l'humain (elle a une limite)
    - Apprentissage renforce
- [Helicopter - Stanford Univ.](http://www.ricou.eu.org/iren/iren/videos/helicopter.mp4) – 2008
    - Apprentissage renforcé
    - On fait un dessin dans le ciel et on dit a l'IA de suivre le dessin le mieux possible
- [Mélodie travaillée - Music VAE](http://www.ricou.eu.org/iren/iren/videos/melody.mp4) - 2018
    - Non supervisé
    - Capable d'extraire des carateristiques
    - Creer un vecteur de la musique initiale et finale
    - Creer des etapes intermediaires en "interpolant"
        - Re-genere des vecteurs
        - Recommence depuis la creation de vecteurs
- Débat : L’État doit-il financer les écoles pre-maternelle ? (3 à 4 ans)
    - [Non – Harish Natarajan](http://www.ricou.eu.org/iren/iren/videos/Debater_Harish_Natarajan.mp4)
    - [Oui – IBM Debater](http://www.ricou.eu.org/iren/iren/videos/Debater_IBM.mp4)
    - IA IBM (en vente)
    - Comme Google
    - Essentiellement du supervisé
        - Techniques en plus pour la comprehension de texte 
- Un [duo](http://www.ricou.eu.org/iren/iren/videos/DeepFake_Macron_Castex.mkv) et [l’artiste caché](http://www.ricou.eu.org/iren/iren/videos/DeepFake_Macron_Castex_video_originale.mkv) (2019 pour la méthode)
    - Non supervisé
    - On decompose en vecteurs le visage de Macron et celui de l'artiste original
    - Les mouvements de l'artistes original se font sur le visage de Macron
        - Classifie les sourcils, la bouche, etc.

# De AlphaGo a MuZero

Bonus: [Film sur AlphaGo](https://youtu.be/WXuK6gekU1Y)

![](https://i.imgur.com/RC2jusf.png)
- A massacre des professionnels
- > C'est comme si nous on voyait le jeu en 2D et AlphaGo en 3D, on est aveugle en comparaison

MuZero:
- Ne donne plus rien (pas de regles, donnees, etc.)
- Seulement si gagner ou perdu

# Usage futur des differents types d'apprentissage

![](https://i.imgur.com/kuuq3RE.png)

Le monde académique/internet et industriel sont différents.

## Transfer ML
On prend un reseau qui fonctionne deja dans un cas et on l'adapte pour fonctionner dans un autre cas
- Effacer les dernieres couches 
    - Detecter des objets/formes complexes (ex: une petite fille joue au balon)
- Garder les premieres couches
    - Detecter des formes de bases

![](https://i.imgur.com/QTYshgx.png)
Ainsi il est tout à fait possible d’utiliser un réseau neuronal entrainé pour une tâche A pour initier l’entrainement du réseau d’une tâche B proche.

# IBM IA pour l'industrie
- IBM Watson Recruitement une aide a l'embauche pour les entreprises
- Watson solution pour la vente
- Watson Assistant pour le marketing
- [Watson Decision Plateform pour l’agriculture](http://www.ricou.eu.org/iren/iren/videos/Watson_agriculture.mp4)
- IBM Equipement Maintenance Assistant pour améliorer la qualité et réduire la maintenance
- IBM Watson Supply Chain Insights

[Site IBM AI For Industries](https://www.ibm.com/watson/ai-for-industries/)