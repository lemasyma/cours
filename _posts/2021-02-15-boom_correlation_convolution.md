---
title:          "BOOM: La correlation et la convolution"
date:           2021-02-15 10:00
categories:     [Image S8, BOOM]
tags:           [Image, BOOM, S8]
description: La correlation et la convolution
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/rJkzI2wWu)

<div class="alert alert-warning" role="alert" markdown="1">
Les TD et TP ne sont pas notes et ont des corrections (a la fin de la semaine).
</div>

Typical reaction of an average EPITA students when he discovered that this cours was about the Fourier transform
![](https://i.imgur.com/xvRNzg1.png)

> L'ordi d'Elodie crash ? "*Mathématiques du "pas de signal"*"

# Piqure de rappel
On a entendu une *magnifique* note de piano puis une note de piano **bruitee**.
On va regarder les signaux:

![](https://i.imgur.com/LCWXlxW.png)

*Lequel est bruite et lequel n'est pas bruite ?*
![](https://i.imgur.com/Q1c0TRM.png)
 Resultat: celui de gauche.

<div class="alert alert-info" role="alert" markdown="1">
Oscillations rapides: hautes frequences.
</div>
Le signal de gauche c'est notre signal + un autre signal qui oscille tres vite. Le but c'est de reperer quelles frequencer enlever.

<div class="alert alert-info" role="alert" markdown="1">
Filtrage de signal: selection de certaines frequences ou suppression d'autres.
</div>

> Comme les chercheurs d'or: on met le sable dans le tamis et on tamise, les mailles laisse passer le sable et garde les pepites.

Dans ce cas, on supprime les hautes frequences (en theorie).

*D'ou peut venir le bruit ?*
Peut etre lie au capteur, s'applique aussi en Image, on a besoin de connaitre les bruits pour les enlever.

En pratique, toujours une petite correlation.

<div class="alert alert-danger" role="alert" markdown="1">
Quand on parle de mathematiques de signaux, on l'applique aussi a l'image car c'est un signal en 2D; le traitement d'image est une **sous-partie** du traitement du signal.
</div>

<div class="alert alert-warning" role="alert" markdown="1">
Les bibliotheques utilisees en python n'ont pas toutes la meme representation de l'image. Certaines bibliotheques transforment l'image en 1D et d'autres en 2D.
</div>

<div class="alert alert-info" role="alert" markdown="1">
Convolution en 1D sur du signal est + ou - la meme en 2D sur les images.
</div>

![](https://i.imgur.com/GvyFdgp.png)
A droite: transformee de Fourier du signal classique et a gauche signal bruite.

On a un "pate" en bas. Si on zoom:
![](https://i.imgur.com/Ejc0Q6n.png)

# Les signaux
*Qu'est-ce qu'un signal ?*
<div class="alert alert-info" role="alert" markdown="1">
Quelque chose qui evolue au cours du temps, qu'on peut mesurer (ex: la temperature; la mesure reguliere la transforme en signal, un electrocardiogramme...).
Un flux d'electron qu'on va mesurer.
</div>

## L'image
<div class="alert alert-danger" role="alert" markdown="1">
Une image est aussi un signal car il y a une mesure: **la mesure du nombres de photons qui arrivent**.
</div>
<div class="alert alert-warning" role="alert" markdown="1">
Les images en noir et blanc **n'existe pas**, ce sont des photos en niveaux de gris.
</div>
Prendre une photo avec un telephone: on a un capteur et plus un photon tape a un endroit plus le pixel sera blanc. Plus on laisse le capteur "ouvert", plus on capte de photons et l'image sera plus net.

## Le signal
*A quoi ca sert ?*
Verifier les risques d'incendie (temperature + humidite), le rechauffement climatique, etc.

<div class="alert alert-success" role="alert" markdown="1">
Les signaux sont utiles pour les statistiques
</div>

## Exemple: le radar
![](https://i.imgur.com/88ty69O.png)
<div class="alert alert-warning" role="alert" markdown="1">
Ne pas toucher a cette fenetre !
</div>

![](https://i.imgur.com/wN5yXHW.png)
Cas parfait: signal continu.

On envoie un signal et on compte le temps que ca prend pour revenir. 

<div class="alert alert-warning" role="alert" markdown="1">
Attention aux variations avec l'air, l'eau, le vide, etc.
</div>

Les chauves-souris le font "automatiqument" mais attention a l'effet Dopler: si une mouche bouge, la frequence renvoyee est modifiee.

### Premier probleme
Notre chauve-souris envoie un signal continu mais nos ordis ont pas une memoire infinie et le signal risque d'avoir du bruit a cause du capteur, numerisation, etc

<div class="alert alert-warning" role="alert" markdown="1">
On passe d'un monde analogique a numerique et il risque d'y avoir de la perte d'information $\rightarrow$ problemes d'effets de bords.
</div>

### Cas reel
On recupere un signal **decale** et **bruite**.
![](https://i.imgur.com/p5n3l6P.png)

### Les outils pour traiter ce signal: la **correlation**
* L'ensemble des signaux forment un **espace vectoriel**.
* La ressemblance = la correlation
* La norme = la distance

*La ressemblance est max quand ?*
Quand on a une superposition des deux signaux.

<div class="alert alert-success" role="alert" markdown="1">
On va "glisser" le signal de gauche sur celui de droite et calculer la ressemblance, cad la **correlation** ou une **integrale** (l'aire sous la courbe des 2 signaux).
</div>

Quand on va faire, on ne va pas avoir la correlation maximale theorique.

<div class="alert alert-info" role="alert" markdown="1">
Dans la correlation:
1. L'auto-correlation
    * Entre 2 signaux $x$ et $x$
    * Entre le meme signal sans **aucune** modification
    * Nous sert a definir l'espace des calculs qu'on va faire
3. L'inter-correlation
    * Entre 2 signaux $x$ et $y$
    * ![](https://i.imgur.com/dLRnWfZ.png)
</div>

Dans ce cas c'est **l'inter-correlation**.
![](https://i.imgur.com/9UEELjh.png)
Notre correlation est maximale en $-5$ car on a un decalage de $-5s$

### Recap sur le bruit
![](https://i.imgur.com/7iBez2I.png)

*Pourquoi on arrive quand meme a retrouver notre signal de base ?*
<div class="alert alert-success" role="alert" markdown="1">
La correlation entre le signal et le bruit est **nulle** car le bruit est non-correle.
</div>

# La correlation
## Definition
$$
\Gamma_{xx}(\tau) = \int_{\mathbb{R}}x(t)\overline{x(t-\tau)}dt = <x(t),x(t-\tau)>
$$
$\Gamma_{xx}(0)$ est maximale car *il n'y a pas de decalage*

$$
\begin{aligned}
&= <x(t), x(t)>\\
&= \int_{\mathbb{R}}|x(t)y|^2\\
&= ||x(t)||^2 = \text{ENERGIE du signal}
\end{aligned}
$$

## Proprietes
<div class="alert alert-info" role="alert" markdown="1">
Dans le cas des signaux reels, si $x$ est reel, l'auto-correlation est **paire**: $\Gamma_{xx}(-\tau) = \Gamma_{xx}(\tau)$
</div>

<div class="alert alert-danger" role="alert" markdown="1">
**Inter-correlation:**
$$
\Gamma_{xy}(\tau) = \int_{\mathbb{R}}x(t)\overline{y(t-\tau)}dt = <x(t),y(t-\tau)>
$$

C'est la formule qu'on utilisera.
</div>
L'inter-correlation est **nulle** si les signaux ne s'intersectent pas.

<div class="alert alert-warning" role="alert" markdown="1">
On prend un signal, on le fait glisser sur un autre et on calcul la **multiplication des aires sous la courbes** de l'intersection des 2.
</div>

## Cas du radar
On envoie $x(t)$ et on recupere $y = x(t-t_0) + \nu(t)$
- $\nu(t)$ : bruit
- $x(t-t_0)$ : signal retarde de $t_0$

Le bruit depend de $t$ et pas de $x$.

$$
\begin{aligned}
\Gamma_{xy}(\tau) = <x(t),y(t-\tau)> &= <x(t),\overbrace{x(t - (\tau + t_0) + \nu(t-\tau))}^{y(t-\tau)}>\\
&= <x(t), x(t - (\tau + t_0))> + \underbrace{<x(t),\nu(t-\tau)>}_{=0}\\
&= \Gamma{xx}(\tau-t_0)
\end{aligned}
$$

$\Gamma{xx}(\tau+t_0)$ est maximal en $0$:
$$
\tau + t_0 = 0 \Rightarrow \tau=-t_0
$$

Sur le notebook: les courbes ne sont pas arrondies, si on zoom dessus on pourrait voir des traits.

# La convolution
<div class="alert alert-warning" role="alert" markdown="1">
On va parler de convolution **continue**:
- En numerique: des sommes
- En analogique: des integrales
</div>

![](https://i.imgur.com/LR1sIhm.png)

Avec la convolution, possible de recuperer un signal debruite:
![](https://i.imgur.com/DgT0p9n.png)
On veut recuperer notre signal a partir du gros pate bleu.

<div class="alert alert-danger" role="alert" markdown="1">
La convolution est utilisee pour debruiter des signaux *tout le temps*.
</div>
C'est faisable avec la correlation mais plus chiant.

<div class="alert alert-warning" role="alert" markdown="1">
Convolution avec une image: probleme aux bords. La "fenetre glissante" passant sur une image risque de sortir du bord de l'image.
**Attention a comment on gere les bords**.
</div>

## Exemple
![](https://i.imgur.com/gIF2w6q.png)

## Definition
$$
(f*g)(t) = \int_{-\infty}^{+\infty}g(xg(t-x))dx = \int_{-\infty}^{+\infty}g(x)f(t-x)dx = (g*f)(t)
$$

Difference de la correlation:
- On ne prend pas le conjugue, $t-x$ inverse $g$
- Il n'y a pas de $t-\tau$

## Proprietes
- Element neutre de la convolution: le delta de Dirac

$$
f*g=g*f=f \Rightarrow g \equiv \delta:t\to
\begin{cases}
    0 & t\neq 0\\
    +\infty & t= 0
\end{cases}
\text{et}
\int_{\mathbb{R}}\delta(t)dt = 1
$$

![](https://i.imgur.com/FGYcgFm.png)

- Si $f$ et $g$ sont de meme parite: $f*g$ est **paire**.
- Si $f$ et $g$ sont de parite contraire: $f*g$ est **impaire**.
