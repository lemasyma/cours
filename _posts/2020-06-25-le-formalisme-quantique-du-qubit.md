---
title:          "QUI : Le formalisme quantique du qubit"
date:           2020-06-25 20:00
categories:     [S6, electif, QUI]
tags:           [S6, QUI, electif]
math: true
description: Formalisme et notions fondamentales de la mécanique quantique
---

Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/SyQQ08G0U)

# La notion d'etat quantique
## Espace des etats
### Espace lineaire
<div class="alert alert-info" role="alert" markdown="1">
Les etats purs sont la polarisation en selon $O_x$ et $O_y$
</div>

Pour decrire la polarisation d'un photon on utilise un *espace lineaire*, un *espace vectoriel de dimension finie* $\mathcal H$ dont les **vecteurs de base** correspondent aux *etats purs*.

On associe la base $\{\vert x\rangle, \vert y\rangle\}$ a $O_x$ et $O_y$.
<div class="alert alert-danger" role="alert" markdown="1">
Un **etat de polarisation** $\{\vert\Phi\rangle\}$ correspond a un **vecteur appartenant a** $\mathcal H$ : 
$$
\vert\Phi\rangle = \lambda\vert x\rangle + \mu\vert y\rangle
$$
</div>
<div class="alert alert-warning" role="alert" markdown="1">
On utilise la *notation de Dirac*.
</div>
### Etat de polarisation
Il existe differents types de polarisation pouvant etre representes par un **vecteur complexe**.
<div class="alert alert-danger" role="alert" markdown="1">
$\mathcal H$ est un *espace vectoriel complexe de dimension 2*
</div>
<div class="alert alert-info" role="alert" markdown="1">
Cela permet de prendre le conjugue d'un vecteur:
$$
\overline{\vert\Phi\rangle} = \langle\Phi\vert = \bar\lambda\langle x\vert + \bar\mu\langle y\vert
$$
* $\bar\lambda, \bar\mu$ : conjugues de $\lambda,\mu$
</div>

### Produit scalaire
<div class="alert alert-info" role="alert" markdown="1">
On peut ecrire une **amplitude de probabilite** comme un **produit scalaire**:
$$
\langle\Psi\vert\Phi\rangle = \biggr(\bar\nu\langle x\vert + \bar\sigma\langle y\vert\biggr) + \biggr(\lambda\vert x\rangle + \mu\vert y\rangle\biggr) = \bar\nu\lambda\langle x\vert x\rangle + \bar\sigma\mu\langle y\vert y\rangle
$$
* $\vert\Psi\rangle = \nu\vert x\rangle + \sigma\vert y\rangle$
</div>
Les vecteurs de bases sont **orthogonaux** entre eux et sont de norme unitaire:
$$
\begin{matrix}
\langle x\vert x\rangle = \langle y\vert y\rangle = 1 & \text{et} & \langle x\vert y\rangle = \langle y\vert x\rangle = 0
\end{matrix}
$$
<div class="alert alert-success" role="alert" markdown="1">
On a donc:
$$
\langle \Psi\vert \Phi\rangle = \bar\nu\lambda + \bar\sigma\mu = \overline{\langle \Phi\vert \Psi\rangle}
$$
</div>
### Norme
<div class="alert alert-info" role="alert" markdown="1">
La norme au carre d'un vecteur $\vert\Phi\rangle$ s'ecrit comme le produit scalaire de $\vert\Psi\rangle$ avec son conjugue $\langle\Phi\vert$:
$$
\Vert\Phi\Vert^2 = \langle\Phi\vert\Phi\rangle = \vert\lambda\vert^2 + \vert\mu\vert^2
$$
</div>
Un etat physique represente par un vecteur doit etre normalise : 
$$
\Vert\Phi\Vert^2 = \langle\Phi\vert\Phi\rangle = \vert\lambda\vert^2 + \vert\mu\vert^2 = 1
$$
### Espace de Hilbert
<div class="alert alert-danger" role="alert" markdown="1">
Un **espace de Hilbert** $\mathcal H$ est un espace vectoriel complexe *pas forcement de dimension finie* muni d'un produit scalaire; introduisant une *norme*, et complet.
</div>
## Amplitude et probabilite
### Calcul d'amplitude
Les **etats de polarisation** sont rpz par des *vecteurs unitaires* dans $\mathcal H$.
<div class="alert alert-info" role="alert" markdown="1">
Un etat de polarisation *rectiligne* ou *lineare* selon $\theta$, note $\vert\theta\rangle$ s'ecrit:
$$
\vert\theta\rangle = \cos\theta\vert x\rangle + \sin\theta\vert y\rangle
$$
</div>
On peut calculer l'amplitude de probabilite en utilisant la notation de Dirac pour qu'un photo polarise suivant $\theta$ traverse un polariseur oriente suivant $\alpha$:
$$
\begin{aligned}
\textbf{a}(\theta\to\alpha) &= \langle\alpha\vert\theta\rangle \\
&= \biggr(\cos\alpha \langle x\vert + \sin\alpha \langle y\vert\biggr)\biggr(\cos\theta \vert x\rangle + \sin\theta \vert y\rangle\biggr) \\
&= \cos\alpha\cos\theta + \sin\alpha\sin\theta\\
&= \cos(\theta - \alpha)
\end{aligned}
$$
### Probabilite
<div class="alert alert-info" role="alert" markdown="1">
Suite au calcul precedent, la **probabilite de traverser l'analyseur** (probabilite de mesurer un photon polarisation selon $\alpha$) est:
$$
\textbf{P}(\theta\to\alpha) = \cos^2(\theta - \alpha) = \vert\langle\alpha\vert\theta\rangle\vert^2
$$
</div>
La probabilite de trouver un etat $\vert\Phi\rangle$ dans un autre etat $\vert\Psi\rangle$ s'exprime selon:
$$
\begin{matrix}
\textbf{a}(\Phi\to\Psi) = \langle\Psi\vert\Phi\rangle & \textbf{et} & \textbf{P}(\Phi\to\Psi) = \vert\langle\Psi\vert\Phi\rangle\vert^2
\end{matrix}
$$
## La mesure quantique
On reprend le systeme de *polariseur/analyseur* avec l'analyseur oriente selon $O_x$. Le polariseur ($\textbf{P}$) va prepare l'etat quantique puis l'analyseur ($\textbf{A}$) va tester sa *polarisation*.
$\textbf{P}_s$ est la **probabilite de sortie** du photon de ($\textbf{A}$):
1. ($\textbf{P}$) est selon $O_x$ : $\textbf{P}_s = 100\%\Rightarrow\text{Resultat : 1}$
2. ($\textbf{P}$) est selon $O_y$ : $\textbf{P}_s = 0\% \Rightarrow\text{Resultat : 0}$
### Polarisation arbitraire
<div class="alert alert-info" role="alert" markdown="1">
Supposons que le polariseur est oriente selon la direction $\theta$ ou sa **direction orthogonale** $\theta_{\bot}$, on peut construire un **systeme orthonorme** de vecteur de base $\{\vert\theta\rangle, \vert\theta_{\bot}\rangle\}$ a partir de la base $\{\vert x\rangle, \vert y\rangle\}$:
$$
\begin{matrix}
\vert\theta\rangle = \cos\theta\vert x\rangle + \sin\theta\vert y\rangle & \textbf{et} & \vert\theta_{\bot}\rangle = -\sin\theta\vert x\rangle + \cos\theta\vert y\rangle
\end{matrix}
$$
</div>
Le **polariseur** prepare le photon dans l'etat $\vert\theta\rangle$, on a donc:
$$
\textbf{P}_s = \cos^2\theta
$$
<div class="alert alert-warning" role="alert" markdown="1">
Apres le passage du photon dans l'analyseur, son etat $\vert\theta\rangle$ devient $\vert x\rangle$.
</div>
<div class="alert alert-danger" role="alert" markdown="1">
La mesure modifie (ou perturbe) l'etat de polarisation.
</div>
### Difference entre mesure classique et quantique
Il y a une **difference de principe** entre la mesure en *physique classique* et la mesure en *physique quantique*:
* Cas classique: la quantite physique *preexiste* a la mesure
    * Si une voiture est contolee a $180km.h^{-1}$, cette vitesse preexistait avant la mesure
* Cas quantique: l'etat de polarisation $\vert\theta\rangle$ n'*existait pas* avant d'etre mesure.
<div class="alert alert-success" role="alert" markdown="1">
Si on prend l'exemple de la voiture dans une **version quantique**, son *etat de vitesse* serait donne par la superposition d'un etat a $120km.h^{-1}$ et d'un autre a $180km.h^{-1}$.
</div>
# La notion d'operateur
*Comment un etat quantique peut se transformer sous l'effet d'operateurs de la forme de matrices de dimensions 2?*
### Principes
On peut formuler 2 principes a partir de l'analyse de la structure mathematique:
1. L'*etat physique* d'un systeme quantique est rpz par un vecteur $\vert\Phi\rangle$ appartenant a $\mathcal H$. $\vert\Phi\rangle$ est unitaire ($\Vert\Phi\Vert^2 = 1$) et est un *vecteur d'etat* du systeme quantique.
2. Soient $\vert\Psi\rangle$ et $\vert\Phi\rangle$ 2 etats physiques. L'**amplitude de probabilite** de trouver $Phi$ dans $Psi$ est $\textbf{a}(\Phi\to\Psi) = \langle\Phi\vert\Psi\rangle$. La probabilite pour $\Phi$ de reussir le test $\Psi$ est:
$$
\textbf{P}(\Phi\to\Psi)=\vert a(\Phi\to\Psi)\vert^2 = \vert\langle\Psi\vert\Phi\rangle\vert^2
$$

<div class="alert alert-warning" role="alert" markdown="1">
Pour realiser le test on doit *preparer* le systeme dans l'etat $\vert\Phi\rangle$ puis on va tester le systeme qui va le mettre dans l'etat $\vert\Psi\rangle$.
</div>
## Operateur de projection
### Mesure et projection
Dans le test precedent on a fait une projection orthognale sur $\vert\Psi\rangle$