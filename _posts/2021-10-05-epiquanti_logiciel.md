---
title:          "EPIQUANTI : Partie logiciel"
date:           2021-10-05 14:00
categories:     [tronc commun S9, EPIQUANTI]
tags:           [tronc commun, EPIQUANTI, S9]
math: true
description: Partie logiciel
---

Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/SJRoAnFEt)

Lien du [livre du prof](https://www.oezratty.net/wordpress/2021/understanding-quantum-technologies-2021/)

# Registers 
 
| **n bits register**                      | **n qubits register**                         |
| ---------------------------------------- | --------------------------------------------- |
| $\color{red}{2^n\text{ possible states } \textbf{once at a time}}$ | $\color{green}{ 2^n \text{possible states }\textbf{linearly superposed}}$ |
| evaluable                                                          | partially evaluable                           |
| independant copies                                                 | no copies                                     |
| individually erasable                                              | non individualy erasable                      |
| non destructive readout                                            | value changed after readout                   |
| deterministic                                                      | probabilistic                                 |

# Gates

## Classical logic gates

![](https://i.imgur.com/D2uCweD.png)

Irreversible gates:
- NAND
- NOR
- AND
- OR

*Quelle est leur consequence ?*
> Comme on perd un bit, on a une **perte d'energie**
> Decouverte par *Rolf Landauer*

<div class="alert alert-success" role="alert" markdown="1">
Des gens travaillent aujourd'hui pour creer une informatique classique sans perte d'energie
</div>

## Quantum gates

<div class="alert alert-info" role="alert" markdown="1">
Matrix based reversible **unitary transformations**
</div>

![](https://i.imgur.com/QddSjHl.png)
- NOT: rotation $X$
- Rotation $Y$

$$
\begin{bmatrix}
0&-i\\
i&0
\end{bmatrix}
$$

- Pauli-Z: rotation $Z$
- Hadamard: superposition

### Porte CNOT

<div class="alert alert-info" role="alert" markdown="1">
On va changer la valeur d'un qubit en fonction d'un autre

![](https://i.imgur.com/mQz42Js.png)

</div>

*Mathematiquement, a quoi ca ressemble ?*

$$
\begin{bmatrix}
1&0&0&0\\
0&1&0&0\\
0&0&0&1\\
0&0&1&0
\end{bmatrix}
$$

![](https://i.imgur.com/2BSkpZE.png)

*Si on intrique des qubits a des portes a 2 qubits, est-ce que ca reste ?*
> Oui

## C2NOT

![](https://i.imgur.com/9vIlFMQ.png)

$$
\begin{bmatrix}
1&0&0&0&0&0&0&0\\
0&1&0&0&0&0&0&0\\
0&0&1&0&0&0&0&0\\
0&0&0&1&0&0&0&0\\
0&0&0&0&1&0&0&0\\
0&0&0&0&0&1&0&0\\
0&0&0&0&0&0&0&1\\
0&0&0&0&0&0&1&0
\end{bmatrix}
$$

## SWAP

![](https://i.imgur.com/cAxqf6h.png)

$$
\begin{bmatrix}
1&0&0&0\\
0&0&1&0\\
0&1&0&0\\
0&0&0&1
\end{bmatrix}
$$

## Fredkin

<div class="alert alert-info" role="alert" markdown="1">
Conditional SWAP
</div>

![](https://i.imgur.com/FIvsp0Y.png)

$$
\begin{bmatrix}
1&0&0&0&0&0&0&0\\
0&1&0&0&0&0&0&0\\
0&0&1&0&0&0&0&0\\
0&0&0&1&0&0&0&0\\
0&0&0&0&1&0&0&0\\
0&0&0&0&0&0&1&0\\
0&0&0&0&0&1&0&0\\
0&0&0&0&0&0&0&1\\
\end{bmatrix}
$$

## Single qubit operations visualization

![](https://i.imgur.com/fW0h0fw.gif)


## CNOT gate effect

$$
\begin{matrix}
\color{blue}{\text{control qubit}} &&\color{blue}{\text{tensor product of control and target qubits before CNOT}}\\
\alpha_1\vert0\rangle &&\alpha_1\alpha_1\vert00\rangle+\alpha_1\beta_2\vert01\rangle + \alpha_2\beta_1\vert10\rangle+\beta_1\beta_2\vert11\rangle\\
\bigotimes&\Rightarrow&\text{CNOT}\\
\alpha_2\vert0\rangle+\beta_2\vert1\rangle&&\alpha_1\alpha_1\vert00\rangle+\alpha_1\beta_2\vert01\rangle + \alpha_2\beta_1\vert11\rangle+\beta_1\beta_2\vert10\rangle\\
\color{blue}{\text{target qubit}}&&\color{blue}{\text{control and target qubits state after CNOT}}\\
\color{blue}{\text{control qubit is }\vert0\rangle}\\
\alpha_1=1&&\alpha_2\vert00\rangle+\beta_2\vert01\rangle\\
&\Rightarrow&\text{CNOT}\\
\beta_1=0&&\alpha_2\vert00\rangle+\beta_2\vert01\rangle\\
\end{matrix}
$$

<div class="alert alert-info" role="alert" markdown="1">
CNOT is not changing the qubit
</div>

## The EPR pair entanglemet building block

Put control qubit into superposition state, then future gates act on 2 states simultaneously

$$
\frac{\vert0\rangle+\vert1\rangle}{\sqrt 2}
$$

![](https://i.imgur.com/U6hQUlf.png) $$\biggr\}\frac{\vert00\rangle+\vert11\rangle}{\sqrt{2}}$$

Subsenquently, flipping a qubit in an entangled state modifies all of tis components

## Control-U gate

On prend une porte U qui est une porte arbitraire

![](https://i.imgur.com/PYYoF2m.png)

$$
\begin{bmatrix}
1&\dots&\dots&\dots\\
\dots&1&\dots&\dots\\
\dots&\dots&U_{11}&U_{12}\\
\dots&\dots&U_{21}&U_{22}
\end{bmatrix}
$$

# Qubit lifecycle

- Initialization
    - $\vert0\rangle$
- Hadamard gate
    - $\frac{\vert0\rangle + \vert1\rangle}{\sqrt{2}}$
- Other gate
    - aubit vector turning around in Bloch sphere
- Measurement
    - Measurement returns $\vert 0\rangle$ qith a probability $\alpha^2$ depending on the qubit state, then qubit state becomes $\vert0\rangle$
    - Measurement returns $\vert1\rangle$ with a probability $\beta^2$

# Universal gates sets

<div class="alert alert-info" role="alert" markdown="1">
**Jeu de portes universel**
Jeu de portes *simples* qu'on peut combiner pour recreer toutes les transformations unitaires
</div>

> Ex: CNOT peut etre recree avec HZH
> Three CNOT gates: one SWAP gate

<div class="alert alert-danger" role="alert" markdown="1">
**Universal quantum computing** requires a T gate ($\frac{\pi}{4}$ rotation)
</div>

## Getting confused with phase rotations

- One round = $2\pi$
- $S=$ one quarter round $=\frac{\pi}{2}$
- $T=$ one eight roung

## Solovay-Kitaev theorem

<div class="alert alert-info" role="alert" markdown="1">
**Theorem**

Any desired gate can be approximated by a sequence of gates from an universal gates set.

A quantum circuit of $m$ constant-qubit gates can be approximated to $\varepsilon$ error by a quantum circuit of $O(m\log^c(\frac{m}{\varepsilon}))$ gates from a desired finite universal gate set with $c=3,97$

For example, creating a $R_{15}$ gate requires $127$ H/Z/T gates
</div>

## In other words

<div class="alert alert-success" role="alert" markdown="1">
On veut appliquer a $n$ qubits n'importe quelle operation generique $U$, on enchaine une serie de transformations unitaires.
</div>

# $SU(2^n)$ - Space of unitaries on $n$ qubits

<div class="alert alert-info" role="alert" markdown="1">
Espace contenant toutes les transformations
</div>

![](https://i.imgur.com/NTCjIQu.png)

# On reversibility

<div class="alert alert-info" role="alert" markdown="1">
**All quantum gates are mathematically reversible**, this is a property of the matrix linear transformations
</div>

<div class="alert alert-danger" role="alert" markdown="1">
We could theortically run an algorithm and rewinf it entirely to return to the initial state, which could help recover port of the energy spent in the system
</div>

On a practical basis:
- The gates are not physically and thermodynamically reversible due to some irreversible processes like micro-wave generations and DACs (digital analog converters)
- The whole digital process taking place before micro-wave generation and after their readout conversion back to digital could be implemented in classical adiabatic\thermodynamically reversible fashion
- Currently being investigated at Sandia Labs, Wisconsin University and with SeeQC

![](https://i.imgur.com/onkL3T5.png)

# Inputs and outputs

![](https://i.imgur.com/1SeTmqH.png)

## Probabilistic or deterministic readouts ?

<div class="alert alert-info" role="alert" markdown="1">
A single qubit measurement is probabilistic, ie: a qubit registered after a Hadamard gate applied to all qubits is a simple random numbers generator
</div>

On a practical basis:
- the algorithm is executed many times, up to 8000 for IBM Q Experience
- an average of qubits results is computed, producing a real number
- the averahed result is theoratically deterministic
- modulo the error generated by noise and decoherence

# Basis, pure and mixed states

![](https://i.imgur.com/rHcKh3T.png)

## Examples

![](https://i.imgur.com/z70JJHi.png)

> *Normalement vous avez rien compris*
> [name=Olivier Ezratty] [time=Tue, Oct 5, 2021 3:55 PM] [color=#907bf7]

![](https://i.imgur.com/TzGs5Aw.png)

<div class="alert alert-success" role="alert" markdown="1">
L'origine aleatoire du photon provient de la physique classique et non quantique
</div>

## Single qubit mixed state

![](https://i.imgur.com/Mhd7O1E.png)

# Toying with density matrices

![](https://i.imgur.com/fEpnGpS.png)

# Qubits measurement

<div class="alert alert-info" role="alert" markdown="1">
**Measurement** is using a collection ${M_m}$ of operators acting on the measured system state space $\vert\psi\rangle$, with probability of $m$ being:

$$
p(m)=\langle\psi\vert M_m^✝M+m\vert\psi\rangle
$$

</div>

System state after measurement becomes:

$$
\frac{M_m\vert\psi\rangle}{\sqrt{\langle\psi\vert M_m^✝M+m\vert\psi\rangle}}
$$

with: 

$$
\sum_mM_m^✝M+m=1
$$

## Various qubits measurement methods

![](https://i.imgur.com/ucEpkHD.png)

# Computing semantics summary

![](https://i.imgur.com/6F6xAjC.png)

# 5 DiVienzo criteria (IBM, 2000)

![](https://i.imgur.com/SuKkNyW.png)

## Main qubit types

![](https://i.imgur.com/5LfK2lw.png)

# From lab to packaged computers

Les ordinateurs quantiques actuels d'IBM:

![](https://i.imgur.com/ourihch.png)

L'ordinateur version commerciale:

![](https://i.imgur.com/TGDouPp.png)
> Il y a un cube derriere qui contient l'ordinateur

IBM pense atteindre $1000$ qubits d'ici 2 ans, mais ca a pas trop l'air possible car au-dessus de $28$ qubits il y a une enorme perte de qualite.

## Inside a typical quantum computer

![](https://i.imgur.com/JLlYQaX.png)


En resume: 4 composantes

Avec des atomes froids, on n'aurait pas des compresseurs mais des pompes a ultra-vide.

## Chez Google

![](https://i.imgur.com/DJlYR8A.jpg)

*Pourquoi les fils tournent ?*
> Pour passer plus de temps dans le froid ?

<div class="alert alert-success" role="alert" markdown="1">
Systeme de **dilatation thermique** du au changement de temperature hardcore
- Refroidit: contracte
- Rechauffement: dilate
</div>

*Pourquoi plusieurs etages ?*
> On est a $300K$ a l'exterieur, on veut minimiser plusieurs poches
> Chaque etage = une temperature
> Chaque disque a une taille plus petite en descendant les etages, pour faire passer le moins de chaleur possible
> Chaque etage est isole de celui au-dessus
> Les fils sont des attenuateurs de puissance mais ils generent de la chaleur

<div class="alert alert-success" role="alert" markdown="1">
C'est l'isolation thermique
</div>

## Quantum computer architecture

![](https://i.imgur.com/iy4vWcY.png)

## Physical layout example

![](https://i.imgur.com/TND8OMC.png)

![](https://i.imgur.com/DzcqICU.png)

# Error correction

<div class="alert alert-danger" role="alert" markdown="1">
Each quantum gate and readout generate significant errors
</div>

Coming form decoherence generated by:
- flip, phase and leakage error
- calibration errors
- thermal noise
- electric and magnetic noise
- gravity
- radioactivty
- vacuum quantum fluctuations
- cosmical rays

<div class="alert alert-warning" role="alert" markdown="1">
It accumulates with the number of quantum gates and qubits
</div>

![](https://i.imgur.com/43XcjSf.png)

## QEC zoo

![](https://i.imgur.com/YVbY7p2.png)
