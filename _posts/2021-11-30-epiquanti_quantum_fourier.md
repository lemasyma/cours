---
title:          "EPIQUANTI : Quantum Fourier Transform"
date:           2021-11-30 14:00
categories:     [tronc commun S9, EPIQUANTI]
tags:           [tronc commun, EPIQUANTI, S9]
math: true
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/HkaAtKQdY)

# Overview

## Three kind of quantum advantage

- Oracle-based
- Adiabatic optimisation
- Simulation of quantum systems

## Quer model and Oracles

<div class="alert alert-info" role="alert" markdown="1">
Oracle: boite noire qui repond oui ou non a une question
</div>

In the query model, you are given access to some function $f$, giving a Y/N answer to all inputs in polynomial time. This function is called the **blac-box**, or the **oracle**. An oracle with input $i$ and output $x_i$ can be described by the *unitary operation*

$$
O_x:\vert i,b\rangle\to\vert i, b\otimes x_i\rangle
$$

By linearity, this oracle gate can be applied to *quantum superpositions*. In order to measure the **time complexity** of an algorithm, one determines the **number of queries** it makes to the oracle.

$$
U_TO_xU_{T-1}O_x\dots O_xU_1O_xU_0\vert 0\dots0\rangle
$$

# Quantum Fourier Transform

## DFT Recap

Given a vector $x$ of dimension $2^N$ with components $x_j$, the **Discrete Fourier Transform** of a vect $x$ is avector $y$ of dimension $2^N$

$$
y_k=\sum_{j=0}^{2^N-1}x_je^{2ipi jk/2^N}
$$

![](https://i.imgur.com/vaFtTxI.png)

Matrix-vector multiplication takes $O(2^{2N})$ steps. The **Fast Fourier Transform** algorithm reduces this to $O(N2^N)$, which renders DFT computable in *linear time*

<div class="alert alert-success" role="alert" markdown="1">
This is done by exploiting symmetry of the DFT matrix representation
</div>

## Ket Notation

A state on $N$ qubits corresponds to a vector $x$ of dimension $2^N$ with components $x_j$. Take the computational basis:

![](https://i.imgur.com/c3Meczh.png)

The Fourier transform of state $\vert x\rangle$ is a state $\vert y\rangle$, i.e. vector of $2^N$ components $y_k$

$$
\vert y\rangle = \sum_{k=0}^{2^N-1}y_k\vert k\rangle = \sum_{\lambda=0}^{2^N-1}\sum_{j=0}^{2^N-1}e^{2i\pi j\frac{k}{2^N}}x_j\vert j\rangle
$$

## 1 qubit case

![](https://i.imgur.com/wnNUmVT.png)

## Exploiting the symmetry

Let us see how the QFT acts upon a computational basis vector. By **linearity of QM**, this will suffice for any quantum state

![](https://i.imgur.com/FmzSUvb.png)

![](https://i.imgur.com/f1yzUMw.png)

![](https://i.imgur.com/qMOa62b.png)

Notice that the $\omega_{N_j}$ in ($\vert 0\gt\omega_{N_j}1\gt$) depends on the integer value, i.e. on the value of all the qubits

This is implemented by performing controlled rotations on each qubit. The number of controlled rotations is the number of remaining qubits in the QFT.

This means that one needs around $N\times (N-1)/2$ gates to implement DFT

## Runtime analysis

![](https://i.imgur.com/GjyDP4M.png)

- Number of gates: $N(N+1)/2$
- Last reversed-ordering step: $sN/2$ swap gates, each needing 3 CNOTs
- Then the QFT on $N$ qubits has a runtime of $O(N^2)$ while the FFT takes about $O(N2^N)$ steps. So we have obtainend an exponential speed-up

# Quantum Phase Estimation

## Goal and assumptions

The most salient application of QFT is the Quantum Phase Estimation routine, which is the workhorse behind several quantum algorithms featuring exponential speed-up, such as **Shor's algorithm** and **Quantum Matrix Inversion**


<div class="alert alert-danger" role="alert" markdown="1">
**Goal**: Estimate the eigenvalue $\lambda=\exp(2\pi\phi)$ associated to a given eigenvector $\vert u\rangle$ of a unitary operator $U$
</div>

Two *assumptions* uynderly the QPE routine:
- Implement the gate $U^k$  in a controlled way with states from $t$ **qubit** register and non-negative $K$
- Prepare the state $\vert u\rangle$ as input. This can be relaxed at the expense of introducing randomness


## Circuit for QPE

The QPE algorithm ises 2 different qubit registers
- *Register 1*: necessary to implement the controlled $U$ gate. The length of this register determines the accuracy of the phase estimation
- *Register 2*: Used to prepare the state $\vert u\rangle$. The lenght will depend on the problem under consideration 

<div class="alert alert-danger" role="alert" markdown="1">
The number $\phi = 0.\phi_0\phi_1\phi_2\phi_3\dots$ can be expressed in binary form:

$$
\phi = \sum_{j=0}^{+\infty}\phi_j2^{-j-1}
$$

</div>

![](https://i.imgur.com/ulF6gOX.png)

![](https://i.imgur.com/aXbVEkS.png)


The QFT needs $O(t^2)$ gates. The number of needed gates is **polynomial in the number of bits** $\phi$. It can be shown that if the binary fraction expression of $\phi$ is truncated to some bit length the error can be controlled with logarithmic overhead

# Amplitude Amplification

## Classical motivation

Given the promise that ther is only one tagged marble in this jar containing $N$ crystal marbles, how many times, on average, do you need to randomly draw a marble before finding it ?

![](https://i.imgur.com/D97kyQU.png)


- Given a set of $N=2^n$ databases entries, with $n$ the number of bits used to denote the address of an entry, and no knowledge about the database searching for a particular entry takes **on average $N/2$ querie**, and $N$ queries in the worst case
- In the quantum case, this can be sped up to abour **$\sqrt{N}$ queries** thanks to Grover's algorithm

## Grover's algorithm

Les us assume that the database of size $N=2^n$ can be indexed by $n$ **qubits**. Starting with:

$$
\vert +++\dots+\rangle = H^{\otimes n}\vert 000\dots0\rangle=\frac{1}{\sqrt{2^n}}(\vert 000\dots0\rangle+\vert 000\dots1\rangle + \vert 111\dots0\rangle + \vert 111\dots1\rangle)
$$

The problem is to find indices of the states that correspon to a 'tagged' solution.

<div class="alert alert-success" role="alert" markdown="1">
GA finds thos indexes by **successive applications** of an **oracle gate (which can identify such a solution)** and a **diffusion gate**
</div>

![](https://i.imgur.com/T2MwJD4.png)

A signle Grover iteration consists of 4 steps:
1. Phase Oracle
2. H wall
3. Phase Gate
4. H wall

![](https://i.imgur.com/qUG22yx.png)

## The oracle gate

<div class="alert alert-info" role="alert" markdown="1">
A **phase oracle** checks, via the black-box function $f$, whether the entry is part of the solution space and, if it is, it flips te sign of the corresponding index. otherwise it does nothing.
</div>

![](https://i.imgur.com/AsrlPE3.png)

> Setps 2, 3,and 4 are collectively known as the **mean-reflection operation**

## Geometric interpretation

Given that $m\lt\lt N=2^n$ entries are solutions to the search problem, a Grover iteration can be seen as a small rotation in the $2$-dimensional subspace spanned by $\vert\phi_{YES}\rangle$ and $\vert\phi_{NO}\rangle$

![](https://i.imgur.com/5o0R3TY.png)
