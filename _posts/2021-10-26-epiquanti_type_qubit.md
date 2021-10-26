---
title:          "EPIQUANTI : Types de Qubits"
date:           2021-10-26 14:00
categories:     [tronc commun S9, EPIQUANTI]
tags:           [tronc commun, EPIQUANTI, S9]
math: true
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/SJwq0DBLF)

Lien du [livre du prof](https://www.oezratty.net/wordpress/2021/understanding-quantum-technologies-2021/)

[Slide du cours](https://www.oezratty.net/Files/Work/Olivier%20Ezratty%20Quantique%20EPITA%204%20Oct2021.pdf)

![](https://i.imgur.com/k5BEC4V.png)

# Quantum anneleaing

$$
\mathcal H_p =
\sum_{i=0}^Nh_i\sigma_i^Z+\sum_{i,j=0}^NJ_{ij}\sigma_i^Z\sigma_j^Z
$$

## Jargon

![](https://i.imgur.com/PkKCAx2.png)

## D Wave

**Super conducting quantum annealing**

15 ans d'avance sur la creation de ses machines

<div class="alert alert-info" role="alert" markdown="1">
- **Spin up** qubit $\vert\uparrow\rangle$
- **Spin up** qubit $\vert\downarrow\rangle$
</div>


![](https://i.imgur.com/4eQlkKP.png)

## Quantum annealing and ising model

$$
\mathcal H_p =\sum_{i=0}^Nh_i\sigma_i^Z+\sum_{i\lt j}^NJ_{ij}\sigma_i^Z\sigma_j^Z
$$

- $\mathcal H_p$: system hamiltonian
- $h_i$: energy difference between 2 states of qubits i
- $v_i$: vertices containing qubit i
- $J_{ij}$: coupling between vertices $v_i$ et $v_j$ with close i and j
- $E$: edge, connecting qubits

### Computing process

![](https://i.imgur.com/cjq7gqG.png)

Starts with converting the probleme into a Ising model or QUBO (Quadratic Unconstrained Binary Optimization)
1. Initialization of qubits states to $\vert\uparrow\rangle$ or $\vert\downarrow\rangle$
2. Setting qubits bias levels $h_i$
3. Slowly growing $J_{ij}$ coupling
4. System converging to minimal $\mathcal H_p$
5. Readout $\vert\uparrow\rangle$ or $\vert\downarrow\rangle$ states for all qubits, giving the solution to the problem of finding the energy minimum for $H_p$

![](https://i.imgur.com/vQYXO3r.png)

![](https://i.imgur.com/CWaI0tZ.png)

<div class="alert alert-info" role="alert" markdown="1">
Le **chimera** est la facon dont les qubits sont relies entre eux physiquement dans le processeur
</div>

![](https://i.imgur.com/aOg5Q3q.png)

## Algorithms

![](https://i.imgur.com/QAoZyMS.png)

## Pegasus / Advantage 2020 generation

**5436 qubits**

Each qubits is connected to 15 neighbour qubits through 37440 couplers, from 6 per qubit in previous generations.

Qubits are operating at 15,8 mK

<div class="alert alert-warning" role="alert" markdown="1">
One order of magnitude improvement in time spent solving problems vs D-Wave 2000Q launched in 2017
</div>

![](https://i.imgur.com/hrLGdBE.png)

*Pourquoi c'est plus dur de rajouter de nouveaux qubits ?*
> C'est plus dur a intriquer

![](https://i.imgur.com/3wjFQkZ.png)

# Superconducting qubits

![](https://i.imgur.com/A2WFYZd.png)

![](https://i.imgur.com/lRXxKiB.png)

## Qubits operating temperatures rationale

*Pourquoi est-ce qu'on doit les refroidir ces qubits ?*
> On veut eviter la decoherence des qubits mais pas que
> Les micro-ondes qu'on envoie sur les qubits sont conditionnees par le niveau d'energie
> On refroidit pour que le bruit ambiant soit inferieur a la puissance des micro-ondes

![](https://i.imgur.com/eaq0wBv.png)

## 5 Superconducting qubits lab configuraiton

![](https://i.imgur.com/B3GxRKK.png)

![](https://i.imgur.com/sza72i8.png)

![](https://i.imgur.com/vVZIBUA.png)

## IBM
![](https://i.imgur.com/cpqpkYX.png)

### Roadmap

![](https://i.imgur.com/y7CYcIP.png)

## Google

![](https://i.imgur.com/vjO4JTK.png)

![](https://i.imgur.com/JqH5Cue.png)

## Google’s 1 million physical qubits plan

![](https://i.imgur.com/caWPPRm.png)

> C'est quoi la consommation energetique ? - Theotime

## Alice & Bob

<div class="alert alert-info" role="alert" markdown="1">
French startup created by Théau Peronnin and Raphaël
Lescanne, from ENS
</div>
> with the help from Benjamin Huard (ENS Lyon), Zaki
Leghtas (ENS Paris), Mazyar Mirrahmi (Inria), Philippe
Campagne-Ibarcq (Inria) and Emmanuel Flurin (CEA)

- use cat-qubits based on two photons coupling in a cavity to increase reliability of superconducting qubits
- qubit information comes from measuring cavity photon number parity without measuring photon number
- expect to build a logical superconducting qubit with only 30 cat-qubits instead of 10 000 classical superconducting qubits
- significantly reduce the burden to create a LSQ FTQC (large scale quantum / fault tolerant quantum computer)
- plan to produce a first processor with logical qubits by 2023

![](https://i.imgur.com/MsKnRkz.png)

## Amazon

<div class="alert alert-info" role="alert" markdown="1">
Amazon announced in december 2020 it will build its own quantum computers using cat-qubits superconducting, in a 118 pages theoretical paper
</div>

> it plans to use surface codes QEC

it’s partnering with Caltech (incl John Preskill), Yale (Devoret/Schoelkopf teams)
and other universities


![](https://i.imgur.com/yvc4HPK.png)


## Summary

![](https://i.imgur.com/GEGffb8.png)

# Electron spins qubits

## Different electron spins qubit platforms

![](https://i.imgur.com/D26tTbo.png)

## How to detect a single charge?

![](https://i.imgur.com/4iyFLfK.png)

## How to manipulate a single spin?

![](https://i.imgur.com/bfdPQ5m.png)

## How to realize a two-qubit gate?

![](https://i.imgur.com/8XZi2K5.png)

## State of the art of two qubit gates

![](https://i.imgur.com/NR74HTt.png)

![](https://i.imgur.com/bhcdTse.png)

planar systems with a huge number of electrodes to:
- define the reservoirs - source and drain
- control the height of the barrier between quantum dots
- define the depth of the quantum well
- manipulate the qubits
- read out the qubits

## Toward a scalable platform

![](https://i.imgur.com/dXe8tBm.png)

## C12 Quantum Electronic

<div class="alert alert-info" role="alert" markdown="1">
french startup created by Matthieu and Pierre Desjardins with the help from Taki Kontos (LPENS) electron spins qubits trapped in carbon nanotubes 5 qubits demonstrator planned for 2021/2022
</div>

![](https://i.imgur.com/OmjRcwg.png)

![](https://i.imgur.com/lNIfJfk.png)

## Summary

![](https://i.imgur.com/fprBrnn.png)

# NV centers qubits

![](https://i.imgur.com/gjs7Ixy.png)

![](https://i.imgur.com/qEQPQ1J.png)

## NV centers implementation and controls

![](https://i.imgur.com/cxBnSIv.png)

## Quantum brillance

<div class="alert alert-info" role="alert" markdown="1">
Australian startup
- ambiant temperature qubits
- 5 NV centers qubits demonstrated in 2021
- they plan to scale > 50 qubits in 2022
- fits on a desktop computer form factor
</div>

![](https://i.imgur.com/wfcCLiV.png)

![](https://i.imgur.com/8Ytm7N2.png)

## qubits NV centers

![](https://i.imgur.com/XbGDbGn.png)

# Topologic qubits

## The topological qubit bit

Chez microsoft:

![](https://i.imgur.com/upmmPlO.png)

![](https://i.imgur.com/ZSmBaN1.png)

- better stability qubits
- low decoherence noise
- few errors
- long coherence time
- high gate speed

<div class="alert alert-danger" role="alert" markdown="1">
- nothing demonstrated so far
- no prototype
- different algorithms
</div>

![](https://i.imgur.com/rIdgkvg.png)

## Majorana fermions summary

![](https://i.imgur.com/RF4MlIC.png)

# Trapped ions qubits

![](https://i.imgur.com/V5EMN6I.png)

## IonQ

<div class="alert alert-info" role="alert" markdown="1">
La boite la plus calee et ayant recu le plus de fonds: \$$82$M en 2015

Maryland and Duke Universities spin-off launched by Christopher Monroe
</div>

![](https://i.imgur.com/y6PM1mX.png)

![](https://i.imgur.com/VIGrNO2.png)



| $\color{green}{\text{pros}}$ | $\color{red}{\text{cons}}$
| -------- | -------- |
| laser controlled gates     | slow gates     |
| $32$ qubits with a large quantum volume of $2^{22}$ reached in 2020|not easy to scale, planning to network several tiny units (above)
|long coherence time and good qubits fidelity||
|excellent qubit connectivity thanks to phonons||
|available on Microsoft and Amazon cloud services||

<div class="alert alert-warning" role="alert" markdown="1">
IPO planned in 2021
</div>


## Honeywell

<div class="alert alert-info" role="alert" markdown="1">
- 2D trapped ions announced in march 2020
- 4 qubits in march 2020
- 6 qubits in june 2020
- 10 qubits in septembre 2020
</div>

<div class="alert alert-success" role="alert" markdown="1">
Better scalability project
</div>

![](https://i.imgur.com/kYSdj6t.png)

![](https://i.imgur.com/6NSvdyx.png)

## Trapped ions qubits summary

![](https://i.imgur.com/xmWeX3O.png)

# Cold atoms qubits

## Cold atoms and Rydberg states

![](https://i.imgur.com/QhcyPpW.png)

<div class="alert alert-info" role="alert" markdown="1">
**Etat de Rydberg**: etat tres energisant
</div>

![](https://i.imgur.com/njxk4RF.png)

## Cold atoms qubits summary

![](https://i.imgur.com/cuWAYqb.png)

# Photon qubits

## Photons qubits types and tools

Qubits

![](https://i.imgur.com/5X6YHJs.png)

Instrumentation

![](https://i.imgur.com/K5mGnA7.png)

![](https://i.imgur.com/B8xhKVN.png)

![](https://i.imgur.com/WYValTN.png)

## Quantum dot photon source

![](https://i.imgur.com/mTipAA9.png)

## Quantum dot photon source

![](https://i.imgur.com/T9zNNaR.png)

![](https://i.imgur.com/Ee9NG0U.png)

## DV and CV photon qubits

![](https://i.imgur.com/1MWcx7e.png)

![](https://i.imgur.com/WWdPXA6.png)

## Photons qubits summary

![](https://i.imgur.com/RKN20cQ.png)

![](https://i.imgur.com/TScqDFm.png)
