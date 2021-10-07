---
title:          "EPIQUANTI : Qubits"
date:           2021-09-28 14:00
categories:     [tronc commun S9, EPIQUANTI]
tags:           [tronc commun, EPIQUANTI, S9]
math: true
description: Qubits
---

Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/SkrIHYx4t)

Lien du [livre du prof](https://www.oezratty.net/wordpress/2021/understanding-quantum-technologies-2021/)

# Grotrian diagram

![](https://i.imgur.com/WAzXA3j.png)

## Quantum vacuum fluctuations

According to quantum field theory and Heisenberg principle, vacuum contains harmonic oscillators with zero-point energy

$$
E=\frac{1}{2}hv\\
\Delta E\cdot\Delta t\ge\frac{h}{2}
$$

with electrons/positrons spontaneously cretaed and annilihating, creating photons

![](https://i.imgur.com/iNILAUH.png)
> Feynmann diagram

<div class="alert alert-info" role="alert" markdown="1">
**Lamb shift** *(1947)*
Energy shift observed between 2 levels hyperfine structure in hydrogen atom, explained by quantum vacuum fluctations impacting electrons
</div>

Casimir effect (1997)
![](https://i.imgur.com/PB376OX.png)

# Comparing classical and quantum physics

![](https://i.imgur.com/ixKLeYe.png)

# Quantum myths: History

*Einstein was wrong about quantum mechanics*
> He was a key founder of quantum physics with the photoeletric effect explanation and many other works; he asked the right questions about entanglement in 1935 which are still debated

*Werner Heisenberg created his indeterminacy inequality*
> It was created by Earle Hesse Kennard in 1927 and Hermann Weyl in 1928

*Erwin Schrodinger's cat is both dead and alive*
> He wanted to explain that the wave-particle duality didn't work at macro scale, thus the cat can't be both dead and alive. End of story, but I can elaborate. It's a matter of uncertainty origin.

*Richard Feynmann invented the concept of quantum computing*
> He imagined in 1981 the concept of quantum simulation of quantum physics phenomenon but, before, Yuri Manin invented in 1980 the concept of gate based quantum computing.

*Young's slit experiment was done with electrons in 1927*
> Peux pas lire ptdr

## What happened during WWII ?

> La bombe atomique

La physique atomique est un champ different de la physique quantique mais on peut expliquer la desintegration du noyau d'uranium par la physique quantique.

<div class="alert alert-warning" role="alert" markdown="1">
Les gens faisant de la physique quantique sont passes sur la physique nucleaire, il y a eu un trou dans la phyisque quantique
</div>

## Post-WWII

- 1946-1952: Felix Bloc
    - Sphere ![](https://i.imgur.com/dzmvu3W.png)
- 1947-1956: William Shockley John Bardeen Walter Brattain
    - Transistors
- 1957: John Bardeen, Leon Cooper, John RObert Schrieffer
    - Superconductivity
- 1953
    - 1960: Gordon Gould, Theodore Maiman, Nikolay Basov
    - 1964: Alexander Prokhorov
    - 1964: Charles Hard Townes
- 1962-1973: Brian Josephson
    - Josephson effect
- 1964: John Stewart Bell
    - Bell inaqualities and test
- 1970: Dieter Zeh
    - Quantum decoherence
- 1980: Yuri Manin
    - Quantum computing
- 1980: Tommaso Toffoli
    - Toffoli gate
- 1981: Richard Feynman
    - Quantum simulator
- 1982: Alain Aspect

## $1^{st}$ and $2^{nd}$ quantum revolutions

<div class="alert alert-info" role="alert" markdown="1">
Manipulating groups of quantum particles ($1947-\*$)
> Photons, electrons and atoms interactions
</div>
- Transistors
- Lasers
- GPS
- Photovoltaic cell
- Atom clocks
- Medical imaging
- Digital photography
- LCD TV quantum dots

<div class="alert alert-info" role="alert" markdown="1">
Manipulating superposition and entanglement and/or individual particles ($1982-\*$)
</div>
- Quantum computing
- Quantum telecommunications
- Quantum cryptography
- Quantum sensing

## Second quantum revolution

- 1991: Anton Zellinger
    - Neutrons duality
- 1992: Arthur Ekert
    - QKD
- 1993: Umesh Vazirani
    - Quantum complexity
- 1992:
    - Serge Haroche
        - Quantum decoherence
    - Juan Cirac and Peter Zoller
        - Trapped ions qubits
    - Edward Farhi
        - Adiabatic quantum computing
    - David DiVincenzo
        - Criterium
- 1997: Nicolas Gisin
    - Non locality
- 1997 & 2002: Daniel Esteve
    - Superconducting qubits
- 2001: Hans Briegel
    - MBQC
- 2011: John Preskill
    - Quantum supremacy concept
- 2012: D-Wave One
    - First quantum annealing commercial computer
- 2016: IBM Q
    - First cloud based quantum computer

# Quantum sensing

> On n'en parlera quasiment pas du tout

- lasers and frequency combs
    - clocks
    - Spectrographs
    - ultra-sound mikes
- entengled photons
    - radars
    - ultra-sensing imaging
- cold atoms

## Capteurs quantiques

- Nami
- Entanglement
- iXblue

# Classical computing state of the art and limitations

## Moore's law: *dead or alive ?*

C'est un papier ecrit par Gordon Moore. Il fait en observation empirique:

<div class="alert alert-danger" role="alert" markdown="1">

Faire croitre le nombre de transistors dans une puce de maniere exonentielle

![](https://i.imgur.com/SpOyygL.png)

</div>
> Ce n'est pas une loi mathematique ou physique

Cela mettait la pression sur les constructeurs comme Intel.

<div class="alert alert-warning" role="alert" markdown="1">
Elle est applicable aux:
- processeurs
- supercalculateurs
- espaces de stockage
</div>

*En quoi la loi de Moore s'est arretee ?*
> La puissance d'horloges n'a pas augmente exponentiellement depuis plus de 15 ans

<div class="alert alert-success" role="alert" markdown="1">
C'est lie a la fin de *l'echelle de Dennard* en 2006

![](https://i.imgur.com/uD4xsE1.png)

</div>
L'energie utilisee a explose.

*Pourquoi ?*
> A cause de fuites sur les transistors

<div class="alert alert-warning" role="alert" markdown="1">
Ca a fini sur le **dark silicon**
</div>
A cause de ce mecanisme, on ne peut pas utiliser toute la surface d'un processeur de serveur sinon il va fondre.

*Comment on fait pour tout utiliser en entier ?*
> Avec un isolant ?
> Avec un refroidissement ?

## CMOS technical challenges

- Extreme ultra violet (EUV)
    - for $\le10$ nm density
- Heat barrier
    - processor clocks

# Quantum computing
# Promis and use cases

Probleme intractable: probleme dont le temps de calcul va augmenter de maniere exponentielle avec sa taille.

<div class="alert alert-info" role="alert" markdown="1">
**Promesse**
Certains problemes intractables vont etre solvable dans un temps humainement raisonable.
</div>
- Transports et logisitiques
- Healthcare
- Energy and materials
- Finance and insurance
- Defense

# Difference Bits and Qubits

![](https://i.imgur.com/dEY5zW9.jpg)

## From quantum physics to qubits

- wave function
    - describes particles properties
    - probabilities
- quantization
    - discrete levels of wave functions, like energy, polarity, spin
- superposition
    - linear combination of quantized states
- entanglement
    - quantum objects correlated states, consequence of linear superposition of multiple quantum objects

<div class="alert alert-warning" role="alert" markdown="1">

wave function & quantization: 2 levels of quantum objects
</div>

## From computing to measurement

- Quantum gates
    - actions on qubits and their superposed states


![](https://i.imgur.com/3NhuTgA.png)


Computational basis state vector:

$$
\begin{matrix}
\text{complex amplitude} &\text{of all combinations of } 0 \text{ and } 1\\
\begin{bmatrix}
\alpha_1\\
\vdots\\
\alpha_2N
\end{bmatrix} &\begin{matrix}
\vert 00\dots00\rangle\\
\vdots\\
\vert 10\dots01\rangle\\
\vdots\\
\vert 11\dots11\rangle
\end{matrix}
\end{matrix}
$$

- $N$ qubits registers
    - information in $2^N$ superposed state

<div class="alert alert-danger" role="alert" markdown="1">
Qubits can't be independently copied 
</div>

$$
\sum_{i=1}^{2^N}\alpha_i^2=1
$$

handles $2^{N+1}-1$ real numbers

- measurement
    - Ends superposition and entanglement
- outputs
    - $N$ probabilistic classical bits
- computing
    - has to be run many times and results average

## Adressing the noise challenge

- decoherence
    - progressively ends superposition and entanglement
    - coherence times between $100\mu s$ and a couple seconds
- errors
    - significant during computing
    - $0.1\%$ to $8\%$ error rates per gate and for qubits readouts
- erros correction
    - requires a very large number of additional qubits
    - $1-100$ to $1-10000$ ratio between logical and physical qubits
- scalability challenges
    - aulity qubits, cabling, control electronics, cryogenics abd energetics engineering

<div class="alert alert-success" role="alert" markdown="1">
Distributed quantum computing ?
</div>

## Complex numbers and phase

- $r$: amplitude, modulus, norm
- $\theta$: phase angle

Euler formula:

$$
e^{i\theta}=\cos\theta+\sin\theta
$$

Phase angles add up

## qubit Bloch sphere representation

![](https://i.imgur.com/Wh71oh4.png)

<div class="alert alert-danger" role="alert" markdown="1">
Opposite vectors in sphere are mathematically orthogonal
</div>

$\alpha$ and $\beta$ are complex numbers altitudes:

$$
\vert\Psi\rangle=\alpha\vert0\rangle+\beta\vert1\rangle
$$

Probabilities and Born normalization constraint:
$$
\alpha+\beta=1
$$

Using polar coordinates $\theta$ and $\phi$ and no global phase:
$$
\vert\Psi\rangle=\cos\frac{\theta}{2}\vert0\rangle+\sin\frac{\theta}{2}e^{i\phi}\vert1\rangle
$$

Euler formula:
$$
e^{i\phi}=\cos\phi+i\sin\phi
$$

Alternate "symetric" version with a global phase of $e^{-\frac{i\phi}{2}}$
$$
\vert\Psi\rangle=\cos\frac{\theta}{2}e^{\frac{-i\phi}{2}}\vert0\rangle+\sin\frac{\theta}{2}e^{\frac{i\phi}{2}}\vert1\rangle
$$

The global phase doen't change the probabilities $\vert\alpha\vert^2$ and $\vert\beta\vert^2$ for measurement

## Other representations

Poincare's sphere:
![](https://i.imgur.com/i80h3wU.png)

# Linear algebra 101

$$
f(\lambda)
$$

Vectors Dirac notation:

$$
\vert\Psi\rangle = \begin{bmatrix}\alpha \\ \beta\end{bmatrix} \quad\Psi\text{ ket}\\
\bar\alpha =\alpha*\quad\langle\Psi\vert=[\bar\alpha,\bar\beta]\quad\psi\text{ bra}
$$

Bra-ket:

$$
\langle\Psi_1\vert\Psi_2\rangle=[\bar\alpha_1,\beta_1]\times\begin{bmatrix}\alpha_2 \\ \beta_2\end{bmatrix}
$$

## How to read that ?

$$
\langle\Psi\vert A\vert\phi\rangle
$$
Average valye in $\Psi$ of the value

$$
A^{✞}=(A^T)*
\underbrace{A^*}_{\text{matrix conjugate}}+\overbrace{A^T}^{\text{matrix transpose}}\Rightarrow \begin{bmatrix}a &b \\ c&d \end{bmatrix}^✞
$$

$$
\vert\Psi\rangle = \bigotimes_{n=1}^N\vert i\rangle
$$