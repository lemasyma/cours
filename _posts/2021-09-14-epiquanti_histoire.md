---
title:          "EPIQUANTI : Histoire et fondamentaux de la physique quantique"
date:           2021-09-14 9:00
categories:     [tronc commun S9, EPIQUANTI]
tags:           [tronc commun, EPIQUANTI, S9]
description: Histoire et fondamentaux de la physique quantique
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/BJLHdapGt)

# Agenda

1. Histoire et fondamentaux de la physique quantique
2. Fondmentaux des qubits avec elements mathematiques
3. Ingenierie du calcul quantique
4. Architecture d'un ordinateur quanitque et technologies habilitantes
5. Differents types de qubits et de calculateurs quantiques
6. Algorithmie quantique - David Herrera-Marti
7. Outils de developpement
8. CAs d'usage metiers et offres clouds - Olivier ezratty avec Georges Usbelger
9. Telecommunications et cryptographie quantique - Eleni Diamanti
10. Questions societales, fausse sciences et fact-checking - Fanny Bouton et Olivier Ezratty
11. Ecosysteme du marche, startup et opportunites - Christophe Jurczak

# Evaluation

- $50\%$: QCM a la fin
- $50\%$: participation active et exercices avec David Herrera-Marti

# Background

- CentraleSupelec 1982-1985
- Sogitec 1985-1989
    - Informatique applique a l'image (art graphique)
- Microsoft 1990-2005
    - Pour l'experience dev
    - A lance des programmes d'accompagnement de startup

> "Je me presente comme un troubadour, un saltimbanque"

- Publie depuis 15 ans des livres

## On quantum tech

- Est tombe dans le quantique il y a $\sim 10$ans
- *Comprendre l'informatique quantique*, $3^e$ edition, ebook gratuit de 684 pages septembre 2020
    - Un peu le syllabus du cours
    - La $4^e$ edition sors dans quelques jours (et en anglais !)
- Alain Aspect
    - A decouvert l'informatique quantique
- Podcasts
    - Quantum: podcast de l'actualite quanitque
    - Decode quantum: les entretiens du quantique

Dans la science fiction:
![](https://i.imgur.com/yiQIJOU.jpg)

![](https://i.imgur.com/z8nVtLj.jpg)

![](https://i.imgur.com/g8tgjJy.jpg)

> Y'a plein de mondes paralleles partout :)

![](https://i.imgur.com/YAZniDp.gif)

> Dans la physique quantique y'a de la teleportation

## Quantique ou pas ?

Les quantum dots ?

![](https://i.imgur.com/gSM71BC.png)

> Oui ! Alors que ca existe depuis longtemps
> C'est une technique qui modifie la frequence d'un photon pour en changer sa couleur en couleur primaire

Fireforx quantum
> Non c'est que le nom

Samsung quantum
> Oui et non (ah ca c'est bien quantique)
> Oui car n'importe quel modele de processeur aujourd'hui a des transistors utilisant des phenomenes quantiques
> Non car ca n'utilise par le quantique de $2^e$ generation

Qubole quantum ?
> Non


Finish quantum max?
> Non

## What is to be "quantum" ?

> Une forme finie qui ne peut pas etre divisee ?
> Meh, tu peux pas avoir un demi-bac

<div class="alert alert-success" role="alert" markdown="1">
C'est lie aux proprietes de la matiere
</div>

> Taille et/ou energie inferieure a un certain ?
> Oui

<div class="alert alert-danger" role="alert" markdown="1">
Une propriete importante: **la dualite des particules**: une bivalence de comportement (onde ET particules)
</div>

# Un peu d'histoire

## Conference de Solvay
![](https://i.imgur.com/W2tUwGF.png)
> A eu lieu a Bruxelles, Belgique

Cette photo marque la fin de la periode mettant en place les bases de la physique quantique.

*Pourquoi Einstein a recu un prix nobel ?*
> Grace a l'effet photoelectrique et NON la theorie de la relativite
> Ce papier est l'un des fondement de la physique quantique, et l'a fait a 26 ans

*Qui a recu 2 prix Nobel ?*
> Marie Curie, qui est la seule personne a avoir recu $2$ prix nobels dans $2$ domaines differents

## Precursors

Un grand nombre de travaux du $19^e$ siecle ont ete les bases de la physique quantique:
- Thomas Young
- William Rowan Hamilton
- Niels Henrik Abel
- Charles Hermite
- James Clerck Maxwell
- Ludwig Boltzmann
- Henri Poincare
- David Hilbert
- Pieter Zeeman
- Hendrik Lorentz

Young's slit experiment - 1806
![](https://i.imgur.com/cpsv0GR.png)

Maxwell electro-magnetic waves - 1865
![](https://i.imgur.com/ZBkpbDd.png)

Zeeman effect - 1896
![](https://i.imgur.com/kWNBeek.png)

## Founders

- Max Planck
- Emmy Noether
- Albert Einstein
- etc.

## Quantum physics beginnings

$1^{er}$ date: decouverte - $2^e$ date: prix nobel

- $1900-1918$: Max Planck
    - black body radiation energy quanta ![](https://i.imgur.com/I4Pf37k.png)
        - Un four
        - Une etoile
        - etc.
    - Planck constant
- $1905-1921$: Albert Einstein
    - photoeletric effect ![](https://i.imgur.com/a9iMoG5.png)
- $1913-1922$: Niels Bohr
    - hydrogen atom model ![](https://i.imgur.com/VhEIwSF.png)
- $1922-1944$: Stern-Gerlach experiment
    - atoms angular momentum ![](https://i.imgur.com/N2CmAXg.png)
    - experimentaliste

<div class="alert alert-warning" role="alert" markdown="1">
On a majoritairement des **theoriciens** et non **exerimentalistes**
</div>

- $1924-1929$: Louis de Broglie
    - wave-particle duality ![](https://i.imgur.com/EfJKrUg.jpg)
- $1924-1945$: Wolfgang Pauli
    - exclusion particle
- $1925$: Uhlenbeck-Goudsmith
    - Electron spin
- $1926-1933$: Erwin Schrodinger
    - wave function $$ih\frac{\partial \Psi(x,t)}{\partial t} = H\Psi(x,t)$$
- $1926-1954$: Max Born
    - quantume probability
- $1927-1932$: Werner Heisenberg
    - indertemination
- $1935$
    - Einstein, Podolski, Rosen: EPR paradox
    - Erwin Schrodinger: C H A T ![](https://i.imgur.com/wiLU0ni.png)
        - papier sur l'intrication quantique
        - il n'y a que 9 lignes sur le chat
- $1937$: Etore Majorana 
    - fermion: particule sans masse

<div class="alert alert-warning" role="alert" markdown="1">
Il manque au moins $50$ personnes dans cette chronologie
</div>

### How old were they ?

- Einseiberg: $24$ ans
- Einstein: $26$ ans
- Schrodinger: $39$ ans
- Planck: $42$ ans

# Quantum physics basics
## Physics domain classification

![](https://i.imgur.com/Ut4q6vn.png)

<div class="alert alert-success" role="alert" markdown="1">
Tout ca forme la **theorie du tout**
</div>
> Souvent les physicien faisant ca sont mono-maniaques

## From macro to nano physics

![](https://i.imgur.com/PM2Mnti.png)

## Quantum physics $101$

<div class="alert alert-info" role="alert" markdown="1">
**Qu'est-ce qui est quantique ?**
- Quantification
- Particules massives et non-massives $\to$ dualite particule/onde
- Superposition des etats
- L'intrication
    - Consequence de la superposition
- L'indetermination: $$\Delta x\Delta p\ge \frac{h}{4\pi}$$
- La mesure quantique
    - Quand on a nos etats superposes: on mesure et on obtient une des valeurs et non la superposition
- L'effet tunnel
- Non-clonage
    - Theoreme demontre a partir des postulats de la physiques quantique qui peuvent etre faux un jour
</div>
> Ecouter de la musique est une addition d'ondes

<div class="alert alert-warning" role="alert" markdown="1">
La teleportation c'est mort :(
</div>
> Le theoreme de non-clonage n'est pas invalide par la teleportation de Start Trek

## Quantification

<div class="alert alert-info" role="alert" markdown="1">
Quantization = discountinued nanoscopic properties of nanoscale amtter and light
</div>

$$
B(\lambda, T) = \frac{2hc^2}{\lambda^5}\frac{1}{e^{\frac{hc}{\lambda k_BT}}-1}\quad\text{Planck law}
$$

![](https://i.imgur.com/5c8oYP0.png)

<div class="alert alert-danger" role="alert" markdown="1">
**Rayleigh-Jeans law**
"Ultraviolet catastrophe" spectrum prediction in classical theory

$$
B_{\lambda}(T)=\frac{2ck_BT}{\lambda^4}
$$

</div>

### Black Body Radiaton

- $\lambda_{max}$: *peak wavelength*
    - Wien's displacement law - 1893

$$
\lambda_{max} = \frac{2898}{T}
$$

### Light Spectrum

- Continous spectrum
    - Sun, black body
- Absorption spectrum
    - cold gas illuminated from behind by continuous spectrum
- Emission spectrum
    - by rarified hot gas

## Quantification
- atoms et ions ![](https://i.imgur.com/6vNOZZe.png)
- electrons
    - autour de leur noyau
    - $n =$ principal
    - $I =$ angulaire
    - $m=$ moment magnetique
    - $s=$ spin
- photons
    - polarization
    - longueur d'onde
    - phase
    - number
        - photon de meme frequence et onde quantique qui peuvent s'additionner
        - ca creer un GROS photon $\to$ etat de *Fock*
    - orbital angular momentum

<div class="alert alert-success" role="alert" markdown="1">
used to create qubits with distincts states and at the particle scale (atoms, electrons, photons)
</div>

## Dualite onde-particule

![](https://i.imgur.com/uN8V5xT.png)
- Interference observed with photons
- photons acting as particle

![](https://i.imgur.com/cpsv0GR.png)
- interferences observed with electrons

$$
\text{particle energy}\to E=h\nu \leftarrow \text{wave frequency}\\
\text{particle momentum}\to p=\frac{h}{\lambda}
\begin{aligned}
\leftarrow\text{Planck constant}\\ 
\leftarrow\text{wavelength}
\end{aligned}
$$

### Young slit experiment details

![](https://i.imgur.com/eE58cOt.png)

## Schrodinger's equation

$$
\begin{aligned}
i\hbar\overbrace{\frac{\partial\Psi(x,t)}{\partial t}}^{\text{total energy}}=-&\underbrace{\frac{\hbar^2}{2m}\overbrace{\frac{\partial^2\Psi(x,t)}{\partial x^2}}^{\text{kinetic energy}}+\overbrace{V(x)\Psi(x,t)}^{\text{potential energy}}}_{}\\
&\hat H=-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}+V(x)\quad\text{Hamiltonian}
\end{aligned}
$$

- $i$: $i^2=-1$
- $m$: particle mass
- $\hbar=\frac{h}{2\pi}$: constante de Dirac
- $\Psi$: l'inconnue de l'equation de Schrodinger
    - Probabilite de trouver une particule massive a un endroit $x$ et un temps $t$
    - La derivee dans le temps est l'energie de la particule
- Hamiltonian: function applicable to the particle wave function to evaluate its total energy

### Constraints

$$
z = a+ib\quad\vert z\vert=\sqrt{a^2+b^2}
$$
Complex number module

$$
\vert\Psi(x,t)\vert^2
$$
Wave function module square

$$
\int^{+\infty}_{-\infty} \vert\Psi(x,t)\vert^2 dx =1
$$
Integral of the probability to find the particle in any position equals one

## Indetermination

$$
\Delta x\Delta p\ge\frac{h}{4\pi}
$$
- $\Delta x$: location precision
- $\Delta p$: momentum precision
- $h$: Planck constant

At a nanoscopic scale, the pseed and position measurement precision are the antinomic, the greater one is, the smaller is the other

<div class="alert alert-info" role="alert" markdown="1">
**Heisenberg microscope thought experiment**: a photon sent on the electron will hcnage its trajectory and measurement
</div>

<div class="alert alert-warning" role="alert" markdown="1">
Derivation: at a nanoscopic scale, measurement apparatus impacts measurement output
</div>

<div class="alert alert-success" role="alert" markdown="1">
- Used in "squeezing" like with photons to increse one precision against the other
- Quantum sensing to increase measurement precision
- Also indirectly explains quantum
</div>

### Planck time, distance and mass

Shortest time measurement
$$
\text{Planck time}\quad t_p=\sqrt{\frac{\hbar G}{c^5}}=\frac{l_p}{c}
$$

Shortest distance measurement
$$
\text{Planck distance}\quad l_p=\sqrt{\frac{\hbar G}{c^3}}
$$

Maximal mass of an elementary particle
- Sinon ca fait un trou noir
$$
\text{Planck mass}\quad m_p=\sqrt{\frac{\hbar c}{G}}
$$

## Quantum physics postulates

1. Quantum state
    - The state of the quantum mechanical system is completely specified by a psi wave function $\psi(x,y,z,t)$ returning a complex number value that depends on the coordinates of the particle and on time, also denoted a ket: $\vert\psi\rangle$ in Dirac's notation
3. Physical quantities
    - A physical quantity is evaluated with an observable operator acting on the $\vert\psi\rangle$ wave function, the observable is an Hermitian matrix, with real eigenvalues
5. Measurement
    - The only values that can be measured are the eignevalues of the observable, it's always a real number. When the spectrum of the observable is discrete, the results are quantized
7. Born rule
    - Defnes the expectation values and probabilities for $\vert\psi\rangle$ properties
9. State collapse
    - After measurement, the wave function $\vert\psi\rangle$ becomes the eigenvector corresponding to the eigenvalue obtained, the state of $\vert\psi\rangle$ is irreversibly changed unless
11. Time evolution

## State superposition

<div class="alert alert-info" role="alert" markdown="1">
Quantum objects can be in superposed states
</div>
- Consequence wave-particle duality
- Since the Schrodinger wave equation is linear, any linear combination of solutions is also a solution
- qubit example: $\vert\psi\rangle=\alpha\vert 0\rangle+\beta\vert 1\rangle$
- corresponds to a linear superposition of $\vert 0\rangle$ et $\vert 1\rangle$ with complex amplitude

![](https://i.imgur.com/dxsZVAv.png)

## Intrication

<div class="alert alert-info" role="alert" markdown="1">
2 quantum particles, particularly photons, can be prepred in a state that is correlated even at a long distance
</div>

![](https://i.imgur.com/c0nt4wD.png)

### Some applications

- Teleportation
- Algorithme
- Cryptographie
- Communication quantique
- etc.

## State reduction and measurement

- Before measurement, quantums are in a superposed state
    - 2 levelss quantum state $\vert\psi\rangle=\alpha\vert0\rangle+\beta\vert1\rangle$
    - $\alpha^2+\beta^2=1$
- Quantum state readout
    - $\vert\psi\rangle=\vert0\rangle$ $\vert\alpha^2\vert$ probability to get $\vert0\rangle$
    - $\vert\psi\rangle=\vert1\rangle$ $\vert\beta\vert^2$ probability to get $\vert1\rangle$
- Another measurement will yield the same result
    - $\frac{1}{\sqrt{2}}\vert0\rangle+\frac{1}{\sqrt{2}}\vert1\rangle$
    - $50\%\to\vert0\rangle\to$ measurement $100\%\to\vert0\rangle$
    - $50\%\to\vert1\rangle\to$ measurement $100\%\to\vert1\rangle$

Also quantum decoherence is progressively disturbing superposition and entanglement, like being a "partial measurement" from the environmnent

<div class="alert alert-success" role="alert" markdown="1">
- qubits measurements is done only at the end of computing
- cannot measure a qubit state in the middle of an algorithm to do some
</div>

## Photons primer

One photon
- wavelength/frequency
- right/left polarization = spin angular momentum $+\hbar$ or $-\hbar$
- vector direction in space
- massless
- no electric charge

- Photon wavenumber

$$
k=\frac{2\pi}{\lambda}
$$

- Photon mode
    - Orhtogonal solutions of the EM wave equations
- Glauber state

$$
\vert a\rangle=e^{-\frac{1}{2}\vert\alpha_i\vert^2}\sum_{n=0}^{+\infty}\frac{\alpha_i^2}{\sqrt{n!}}\vert n_i\rangle
$$

- Fock state
    - Tensor product of groups of photons of the modes $k_j$

$$
\vert n_{k_0}\rangle\circ\dots\circ\vert n_{k_n}\rangle
$$

## Fourier transforms

$$
\hat f(\xi) = \int_{-\infty}^{+\infty}f(x)e^{-2\pi ix\xi}dx\quad\text{Fourier transform}\\
f(x) = \int_{-\infty}^{+\infty} \hat f(\xi)e^{2\pi ix\xi}dx\quad\text{inversion Fourier transform}
$$

## Classical, semi-classical and non classical forms of lights and photons

- Sun and blackbody light
    - single mode laser coherent light
    - gaussian wave packet
    - entangled photons
    - photon squeezed state
- Photon number
    - Photon number superposition
    - Antibunching
    - non gaussian states

## Doppler effect
![](https://i.imgur.com/x4JeRG6.png)

## Superconductivity

Some materials have 0 resistivity below a threshold temperature 

![](https://i.imgur.com/dl4e9fu.png)

![](https://i.imgur.com/NQbWVG5.png)

## Superfluidity

At a very low temperature, helium 3 and 4 become superfluid and have no viscosity

![](https://i.imgur.com/qP1AJC8.png)

## Bose-Einstein condensated

![](https://i.imgur.com/zyRQAUV.png)
