---
title:          "EPIQUANTI : Noisy Intermediate-Scale Quantum (NISQ) Computing"
date:           2021-11-30 16:00
categories:     [tronc commun S9, EPIQUANTI]
tags:           [tronc commun, EPIQUANTI, S9]
math: true
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/SkO0fpmtF)

# NISQ Computing

## Motivation

*Shor's algorithm - how many qubits does it take to factor an integer ?*

Textbook examples of quantum algorithm largely assume that qubits and gates are not *subject* to noise. In the absence of noise, to factor and integer ,ade of $1024$ bits takes about $2050$ qubits and over $10^9$ gates

In the presence of noise, quantum error correction has to be incorporated into the computation, adding a large overhead.

![](https://i.imgur.com/1ijEcy7.png)

Fault-tolerant quantum computations of arbitrary length are not within reach of today's technology (need qubits in the millions)

Algorithms for small number of qubits (in the $\sim100$) and limite coherence time will need to **offload** **pre and post-processing** to classical computers. Noisy Intermediate Scale quantum (**NISQ**) computed is thriving field of research:

- $50-100$ qubits
- Limited gate fidelity
- Limited qubit connectivity
- Limited correction capabilities $\to$ low depth circuit
- Killer apps: simulate correlated matter, machine learning, optimization

![](https://i.imgur.com/vz4YGLX.png)


## Variational Quantum Algorithms

Variational Quantum Algorithms are a **hybrird quantum-classical** approach.

<div class="alert alert-info" role="alert" markdown="1">
*Goal*: finding ground state of a Hamiltonian $H$, or alternatively, optimizing a **cost function**
</div>

1. Choose a good Ansatz $\vert\psi(\theta)\rangle$
2. Design a quantum circuit that implements $\vert\psi(\theta)\rangle$
3. Measure cost function $E_{\theta}=\langle\psi(\theta)\vert H\vert\psi(\theta)\rangle$
4. Use classical optimizer to find optimal $\theta^{\*}$

![](https://i.imgur.com/3KLHyOb.png)


VQA consist of a quantum processor that can prepare quantum states belonging to a parameterized class $\{\psi(\theta)\rangle\}$ efficiently and an external loop (running on classical hardware) that optimizes its parameters

<div class="alert alert-danger" role="alert" markdown="1">
The absence of error correcting means that the effective error rate will be non-vanishing, and as a consequence, the length of the possible circuit will be bounded
</div>

## VQA: Inner routine

<div class="alert alert-info" role="alert" markdown="1">
The inner routine prepares a state parameterized by $\theta$
</div>


# Quantum Approximate Optimization Algorithm

## Combinatorial optimization

<div class="alert alert-info" role="alert" markdown="1">
Combinatorial optimization is about finding an optimal configuration in a set of possible configurations. 
</div>

In general, combinatorial problems are very big so exhaustive search is not tractable.

There are many methods to tackle optimisation problems, such as Constraint Programming, Branch and Bound/Cut methods, and **local search** heuristics.

A specific NP-hard problem under consideration, known Quadratic Unconstrained Binary Optimization Problem (**QUBO**), can be expressed a a local energy problem and therefore phrased as an **Ising model**. Given a set of spins $s_i = \pm1$, the foal is to find the configuration which minimizes the energy function.

$$
H(s_1,\dots s_N) = -\sum_{i\lt j}J_{ij}s_is_j-\sum_{i=1}^Nh_is_i
$$

![](https://i.imgur.com/wvZQEk6.png)


## Simulated Annealing

Heuristic algorithms are used to find approximate solutions to combinatorial problems that, while being suboptimal, are "good enough". **Simulated Annealing** is a **local search heuristic** inspired by the physical process of thermal annealing.

![](https://i.imgur.com/AWOMZxv.png)


SA performs **local changes** in the current candidate solution and checks whether the new candidate has lower energy. If it does, it becomes the leading candidate, if it does not, *one may still accept the new candidate with probability*, in the hope that it will help explore the space of solutions. This **hill-climbing** events become less liekly as the algorithm progresses, and they are controller by an **effective temperature** parameter.

<div class="alert alert-danger" role="alert" markdown="1">
C'est du recuit simule !
</div>

## Tunneling effect

<div class="alert alert-info" role="alert" markdown="1">
Tunneling is the intuition behind QA.
</div>

Classicaly, particles with low energy will rebound upon collision with a high energy barrier.

![](https://i.imgur.com/imdMTlr.png)

In the quantum setting, it is possible for a low energy particle to pass through the energy wall. This is because quantum particles are not point-like, but rather like wave-packets.

## Quantum annealing recap

Recall that in QA, an easy Hamiltonian is gradually

![](https://i.imgur.com/yzesXCA.png)

## Ansatz

![](https://i.imgur.com/SmNClQZ.png)


![](https://i.imgur.com/uYPdW0a.png)

## QAOA For MaxCut

![](https://i.imgur.com/cJHtJo2.png)
