---
title:          "QUI : La physique du qubit"
date:           2020-06-25 19:30
categories:     [S6, electif, QUI]
tags:           [S6, QUI, electif]
math: true
description: Premier exemple de support physique pour transporter l’information par un système quantique
---

Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/ryiMsAlCI)

# Generalites
## Informatique quantique

<div class="alert alert-danger" role="alert" markdown="1">
**L'informatique quantique** est l'utilisation des lois et proprietes de la *mecanique quantique* pour *encoder* et *tranposter* de l'information.
</div>

## Mecanique quantique

<div class="alert alert-danger" role="alert" markdown="1">
La **mecanique quantique** est une *theorie physique* pour decrire un systeme dont la taille est celle d'un atome ($10^{-10}m$) ou moindre.
</div>

<div class="alert alert-warning" role="alert" markdown="1">
Tout systeme est ultimement un **objet quantique**. La mecanique quantique doit permettre de retrouver les lois classiques.
</div>

## Qubits

<div class="alert alert-danger" role="alert" markdown="1">
Qubits (*Quantum bits*) : changer les *proprietes quantiques individuelles* d'une particule telle que son energie, sa polarisation, son "spin" pour encoder de l'information. C'est la plus petite quantite d'information que l'on peut transporter ou stocker dans un systeme quantique.
</div>

## Loi de Moore

<div class="alert alert-info" role="alert" markdown="1">
Le nombre de transistors garves sur une puce double tous les 18 mois environ.
</div>

D'apres cette loi, les dimensions d'un puce seront inferieures a 10 nm apres 2020. A cette echelle les proprietes quantiques des atomes et electrons vont devenir importantes.

## Avantages et inconvenients du calcul quantique
* Superposition
    * Un bit classique peut seulement prendre les valeurs 0 et 1
    * Un qubit peut prendre les valeurs 0 et 1 et toutes celles intermediaires
    * Un qubit est constitue d'une **superposition lineaire** des **etats quantiques** correspondant aux bits 0 et 1
        * cela decuple les capacites de calcul, le cryptage et de transport de l'information

* Intrication
    * 2 objets quantiques intriques bien que separes pas une distance arbitraire sont une seule et meme entite
    * on ne peut pas comprendre cette entite comme la reunion de 2 objets independants

* Parallelisme
    *  mise en oeuvre des proprietes de **superposition** et **d'intrication**
    *  permet a un ordinateur quantique de realiser plus d'operations qu'un ordinateur classique
    *  algoritmes quantiques
        *  algorithme de Shor
        *  algorithme de Grover

* Decoherence : **Obstacle majeur**
    * sensibilite a l'environnement
    * entraine une perte de relation de phase entre 2 etats quantiques
        * relation necessaire a la realisation d'un calcul quantique
    * interaction des qubits avec l'environnement qui brouille les superpositions lineaires


<div class="alert alert-warning" role="alert" markdown="1">
Un ordinateur quantique fiable doit etre parfaitement **isole**. Des codes d'erreur ont ete creer pour palier aux **defauts d'isolation**.
</div>

# Premier modele physique d'un qubit : le photon

<div class="alert alert-danger" role="alert" markdown="1">
La **polarisation du photon** sers a encoder de maniere quantique un qubit.
</div>

## Polarisation
La polarisation a ete mise en evidence avec un cristal **birefringent**, c.a.d. qui decompose la lumiere en deux rayons polarises dans des directions perpendiculaire alors que la lumiere incidente est **polarisee**.

<div class="alert alert-warning" role="alert" markdown="1">
Les vibrations lumineuses ont un caractere vectoriel.
</div>


### Une onde transverse

<div class="alert alert-info" role="alert" markdown="1">
Pour une orientation convenable, on observera une extinction d'un des deux rayons. C'est une **vibration transverse** (orthogonale) a la direction de propagation.
</div>

<div class="alert alert-success" role="alert" markdown="1">

Une onde scalaire se propageant au cours du temps selon la direction $O_z$ est decrite par:
$$
u(z,t) = u_o\cos(\omega t - kz)
$$

* $\omega = ck = \frac{2\pi}{T} = 2\pi f$ : frequence angulaire de la vibration ($s^{-1}$)
* $c$ : vitesse de la lumiere ($m.s^{-1}$)

<div class="alert alert-danger" role="alert" markdown="1">
On se place dans un plan fixe en $z = 0$ : 
$$
u(z = 0, t) = u(t) = u_0\cos(\omega t)
$$

</div>
</div>

### Vecteur polarisation

<div class="alert alert-info" role="alert" markdown="1">
Le modele de l'onde scalaire peut se generaliser aux 3 dimensions pour representer le vecteur **champ electrique** qui caracterise une onde lumineuse:
$$
\vec E = \vec E_0\cos(\omega t)
$$
</div>

<div class="alert alert-warning" role="alert" markdown="1">
**L'orientation de ce champ** est la **polarisation** de la lumiere.
</div>
La lumiere est percue comme un champ electromagnetique dont la **composante electrique** est orthogonale a sa direction de propagation.

<div class="alert alert-info" role="alert" markdown="1">
Pour decire l'orientation du champ electrique on a besoin d'un systeme d'axe $O_x$ et $O_y$. En posant $\Vert \vec E_0 \Vert = E_0$ : 
$$
\vec E = \begin{pmatrix} E_x \cr E_y \end{pmatrix} = E_x \vec u_x + E_y \vec u_y \Rightarrow \vec E = E_o\cos \theta \cos(\omega t)\vec u_x + E_0 \sin \theta\cos(\omega t)\vec u_y
$$

<div class="alert alert-warning" role="alert" markdown="1">
L'angle $\theta$ caracterise l'orientation de $\vec E$ dans $xOy$, c.a.d. la **polarisation**
</div>
</div>

L'intensite de l'onde lumineuse est proportionnelle au carre du champ electrique
$$
I \propto E_0^2
$$

<div class="alert alert-success" role="alert" markdown="1">
On introduit un vecteur unitaire, note $\hat{p}$ et appartenant au plan $xOy$ tel que:
$$
\hat{p} = \begin{pmatrix} \cos\theta \\ \sin\theta\end{pmatrix} \Rightarrow \vec E = E_0\cos(\omega t)\hat{p}
$$
* Si $\theta = 0$ : polarisation selon $O_x (\hat{p} = \vec u_x)$
* Si $\theta = \pi / 2$ : polarisation selon $O_y (\hat{p} = \vec u_y)$
</div>

## Changement et mesure de la polarisation de la lumiere
### Polariseur et analyseur
On utilise un systeme a 2 polarisateurs consecutifs pour changer et mesurer l'orientation du champ $\vec E$:
* polariseur "d'entree" : oriente la polarisation de la lumiere incidente selon un angle $\theta$ par rappor a $O_x$
* polariseur "de sortie" (**l'analyseur**) : possede un axe de polarisation faisant un angle $\alpha$ avec $Ox$

<div class="alert alert-info" role="alert" markdown="1">
On utilise un vecteur unitaire $\hat{n}$ pour decrire la polarisation de l'analyseur
$$
\hat{n} = \cos\alpha\vec u_x + \sin\alpha\vec u_y = \begin{pmatrix}\cos\alpha\\ \sin\alpha\end{pmatrix}
$$
</div>

![](https://i.imgur.com/Sg8B1XL.png)

### Loi de Malus

<div class="alert alert-warning" role="alert" markdown="1">
On doit determiner **l'orientation du champ electrique** $\vec E'$ pour mesurer la **polarisation** a la sortie de l'analyseur.
</div>

On projete $\vec E$ oriente selon $\hat{p}$ dans la direction $\hat{n}$
$$
\begin{aligned}
\vec E &= (\vec E \cdot\hat{n})\hat{n} \\
&= E_0\cos(\omega t)(\hat{p}\cdot\hat{n})\hat{n} \\
&= E_0\cos(\omega t)(\cos\theta\cos\alpha + \sin\theta\sin\alpha)\hat{n}\\
\vec E &= E_0\cos(\omega t)\cos(\theta - \alpha)\hat{n}
\end{aligned}
$$

<div class="alert alert-info" role="alert" markdown="1">
La loi de Malus est une loi classique pour l'**intensite a la sortie de l'analyser**:
$$
I' = I\cos^2(\alpha-\theta)
$$
</div>

### Type de polarisation

<div class="alert alert-warning" role="alert" markdown="1">
Pour une polarisation lineaire, les deux composantes de $\vec E$ ont la meme dependence par r

<div class="alert alert-info" role="alert" markdown="1">
Les composantes de $\vec E$ se notent avec une phase specifique a chacune qui peut etre differentes : 
$$
\begin{cases}
E_x = E_0\cos\theta\cos(\omega t - \delta_x) \\
E_y = E_0\cos\theta\cos(\omega t - \delta_y)
\end{cases}
$$
</div>
</div>

En fonction de la differnce de phase $\delta = \delta_x - \delta_y$:
* Si $\delta = 0$ ou $\delta = \pm\pi$ : **polarisation rectiligne**
    * $E_x$ et $E_y$ oscillent dans un plan fixe faisant un angle $\theta$ avec $Ox$
* Si $\theta = \pm\frac{\pi}{2}$ : **polarisation circulaire**
    * l'extremite du vecteur $\vec E$ decrit un cercle au cours du temps
* Si $\theta \not = p\frac{\pi}{2}$ avec $p \in \mathbb{Z}$ : **polarisation elliptique**
    * pas de relation particuliere entre les phases des composantes
    * l'extremite de $\vec E$ decrit une *ellipse*

![](https://i.imgur.com/T8kevgb.png)
<div class="alert alert-warning" role="alert" markdown="1">
On ne peut pas mesurer la phase individuelle d'une composante $\vec E$, seule $\delta$ est accessible. On peut imposer $\delta_x = 0$ en redefinissant l'origine des temps.
</div>

<div class="alert alert-info" role="alert" markdown="1">
Le champ electrique $\vec E$ peut aussi s'ecrire : 
$$
\vec E = E_0\textbf{Re}\biggr[e^{-i\omega t}\begin{pmatrix}\lambda \\ \mu\end{pmatrix}\biggr]\space \text{avec} \begin{pmatrix}\mu \\ \lambda\end{pmatrix} = \begin{pmatrix}\cos\theta e^{i\delta_x} \\ \sin\theta e^{i\delta_y}\end{pmatrix}
$$
* $\begin{pmatrix}\mu \\ \lambda\end{pmatrix}$ : polarisation
* $\mu,\lambda\in \mathbb{C}$
* $\vert\lambda\vert^2 + \vert\mu\vert^2 = 1$
</div>

## Approche quantique de la polarisation
En reduisant l'intensite lumineuse, on peut etudier la **polarisation rectiligne individuelle** de chaque photon constituant la lumiere.

<div class="alert alert-danger" role="alert" markdown="1">
La taille typique d'un photon est donnee par sa longueur d'onde de l'ordre du nanometre.
</div>

On detecte $N$ photons, si $N\to\infty$ on doit retrouver le comportement ondulatoire classique de la lumiere.
On prend une *lame birefringente* avec des photons incidents dont la polarisation *rectiligne* fait un angle $\theta$ avec $O_x$.
![](https://i.imgur.com/y37PXXL.png)

### Non simultaneite
Le faisceau est separe en des faisceaux d'intensite:
* $I\cos^2\theta$ polarise selon $O_x$
* $I\sin^2\theta$ polarise selon $O_y$

<div class="alert alert-success" role="alert" markdown="1">
Un photon est detecte soit en $D_x$ soit en $D_y$
</div>

<div class="alert alert-info" role="alert" markdown="1">
Pour mesurer la probabilite de detection d'un photon pour chaque detecteur:
$$
\textbf{P}_x = \cos^2\theta \space \textbf{et}\space \textbf{P}_y = \sin^2\theta
$$
</div>

Cette experience met en valeur **l'aspect corpulaire** de la lumiere.

### Recouvrement de la loi classique

<div class="alert alert-info" role="alert" markdown="1">
Si $N$ photons sont envoyes alors le nombre de photons detectes par chaque detecteur est :
$$
D_x:N_x\simeq N\cos^2\theta \space \textbf{et} \space D_y:N_y\simeq N\sin^2\theta
$$
</div>

On retrouve la loi de Malus lorsque $N\to\infty$.

### Nature probabiliste
Il est impossible de prevoir le chemin d'un photon, ce qui est en opposition avec le determinisme de la mecanique classique.

### Recombinaison de faisceau
On cherche a recombiner deux faisceaux, et retrouver la *loi de Malus* malgre la differentiation de chemin, par ce dispositif:
![](https://i.imgur.com/NBhfdTu.png)

On s'attend a une intensite de sortie proporionelle a $\textbf{P}_x$.
Le photons a 2 chemins possibles : 
* (E) : il traverse le polariseur avec une probabilite de $\cos^2\theta$, puis l'analyseur avec une probabilite de $\cos^2\theta$
    * la probabilite totale est $\cos^2\theta\cos^2\alpha$
* (O) : il traverse le polariseur avec une probabilite de $\sin^2\theta$, puis l'analyseur avec une probabilite de $\sin^2\theta$
    * la probabilite totale est $\sin^2\theta\sin^2\alpha$

<div class="alert alert-danger" role="alert" markdown="1">
La probabilite totale est : 
$$
\textbf{P}_{tot} = \cos^2\theta\cos^2\alpha + \sin^2\theta\sin^2\alpha \not = \cos^2(\theta - \alpha)
$$
Le raisonnement est **FAUX**.
</div>

### Amplitude de probabilite

<div class="alert alert-success" role="alert" markdown="1">
Pour retrouver la *loi de Malus*, il faut raisonner a partir de la notion d'**amplitude de probabilite** pour chaque chemin.
</div>

<div class="alert alert-info" role="alert" markdown="1">
Le module au carre de cette amplitude donne la probabilite: 
$$
\begin{matrix}
\textbf{a}(\theta\to x) = \cos \theta & \textbf{a}(\alpha\to x) = \cos \alpha\\
\textbf{a}(\theta\to y) = \sin \theta & \textbf{a}(\alpha\to y) = \sin \alpha
\end{matrix}
$$
* $\textbf{a}(\theta\to x)$ : amplitude assiociee a la probabilite de detecter un photon polarise selon $O_x$
</div>

<div class="alert alert-danger" role="alert" markdown="1">
L'amplitude totale de sortie s'obtient en **superposant** les amplitudes pour des chemins **indiscernables**:
$$
\textbf{P}_{tot} = \vert\textbf{a}_{tot}^2\vert = \cos^2(\theta - \alpha)
$$
Le raisonnement est **BON**.
</div>

### Discernabilite
Un photon ne fait aucune distinction entre les chemins (E) et (O), sinon la probabilite serait $\textbf{P}_{tot} = \cos^2\theta\cos^2\alpha + \sin^2\theta\sin^2\alpha \not = \cos^2(\theta - \alpha)$. C'est l'**indiscernabilite des chemins possibles**.

### Interpretation
On a 2 interpretations possibles:
1. Le photon emprunte 2 trajets a la fois
2. la question "*Quel trajet ?*" n'a aucun sens

<div class="alert alert-success" role="alert" markdown="1">
La deuxieme interpretation est preferable car il est impossiblde de differencier les chemins experimentalement.
</div>

<div class="alert alert-danger" role="alert" markdown="1">
La notion de trajectoire n'existe pas en physique quantique. Elle est remplacee par la notion de **probabilite de presence**.
</div>

<div class="alert alert-warning" role="alert" markdown="1">
Un photon ne peut prendre *physiquement* qu'un seul des 2 chemins.
</div>

# Application : La cryptographie quantique

On attribue arbitrairement : 
* **Valeur 1** : photon polarise par $O_x$
* **Valeur 0** : photon polarise par $O_y$

### Convention de communication

Si *Alice (A)* et *Bob (B)* echangent des informations sous forme quantique alors cela prend la forme d'une suite de photons polarises : 
$$
\text{y y x y x y y y x ...}
$$
*Bob* analyse la polarisation de l'information recue a l'aide d'une lame birefringente et en deduis le message de *Alice*
$$
\text{0 0 1 0 1 0 0 0 1 ...}
$$

### Possibilite d'ecoute

Pour intercepter le message, *Eve* va devoir mesurer la **polarisation quantique d'un des photons**, elle a $50%$ de chance de se tromper, puis doit renvoyer le photon a *Alice* et a $50%$ de chance de se tromper.
<div class="alert alert-warning" role="alert" markdown="1">
Si leur message a ete espionne, *Alice* et *Bob* peuvent constater une plu grande quantite d'erreurs.
</div>

## Protection de la cle publique
### Protection de la cle publique

<div class="alert alert-info" role="alert" markdown="1">
La cryptographie repose sur une **cle de chiffrage** (cle publique) connue seulement de l'expediteur et du destinataire.
</div>

Le temps de calcul est le principal obstacle pour dechiffrer le message

### Cryptographie quantique

Il s'agit de proteger la cle de chiffrage, tel que s'assure que la transmission d'une cle n'a pas ete espionee (*distribution quantique d'une cle*).

## Protocole BB84
### Choix de polarisation

1. On suppose qu'*Alice* peut envoyer 4 types de photons avec des *polarisations rectilignes* differentes:
![](https://i.imgur.com/ofMfmtT.png)
2. On peut regrouyper les polarisations en 2 ensembles differents:
![](https://i.imgur.com/3Mns6nc.png)

### Transmission

*Alice* choisit **au hasard** une des deux bases pour emettre / recevoir des photons

![](https://i.imgur.com/9MUmtSV.png)

Ces bases sont constituees par des systemes similaires a la **lame birefringente**.

Quand *Bob* recoit un photon, il choisit parmis ce bases **aleatoirement**. 
Il va ensuite analyser la polarisation du photon recu.

![](https://i.imgur.com/2v4Xpir.png)

### Reception
Parfois la base de reception de *Bob* $\mathfrak B_B$ n'est pas "alignee" avec la polarisation du photon recu, l'etat de polarisation est projete sur l'une des 2 directions de $\mathfrak B_B$.

### Comparaison
*Alice* rend **publique** sa base d'emission $\mathfrak B_A$ pour indiquer a *Bob* les photons recus dont la polarisation n'etait pas alignee.

<div class="alert alert-warning" role="alert" markdown="1">
Si $\mathfrak B_B \not = \mathfrak B_A$ il y a eu une projection, dans ce cas le photon recu est *rejete* et *Bob* conserve que les photons dont la $\mathfrak B_B$ etait en accord avec $\mathfrak B_A$.
</div>

<div class="alert alert-success" role="alert" markdown="1">
Dans le tableau la **cle conservee** ou **clee reconciliee** est $\text{0 1 0 1 ...}$
</div>

### Interception
Une personne souhaitant intercepter le message (*Eve*) doit **recevoir** d'*Alice* puis renvoyer a *Bob* chaque photon intercepte. 2 cas se presentent : 
1. La base $\mathfrak B_E$ de *Eve* est **alignee**
    * *Eve* a 0% de chances de se tromper
2. La base $\mathfrak B_E$ de *Eve* est **non-alignee**
    * *Eve* a 50% de chances de se tromper

### Non-clonage

Il est **impossible** pour *Eve* de proceder differemment, elle est obligee de projeter.

<div class="alert alert-danger" role="alert" markdown="1">
**Theoreme de non-clonage** : Il est impossible d'interagir avec un "*etat quantique*" sans le modifier, il ne peut pas etre clone.
</div>

<div class="alert alert-success" role="alert" markdown="1">
*Alice* et *Bob* peuvent detecter un eventuel espion avec une probabilite de $1-\frac{3}{4}^n$
</div>
