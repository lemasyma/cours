---
title:          "IRGPU: Patterns for massively parallel programming"
date:           2021-05-05 14:00
categories:     [Image S8, IRGPU]
tags:           [Image, S8, IRGPU]
math: true
description: Patterns for massively parallel programming
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/rkmdFZed_)

# IRGPU: Patterns for massively parallel programming

# Programming patterns & memory optimizations

**The programming patterns**
- Map
- Map + Local reduction
- Reduction
- Scan

**The IP algorithms**
- LUT applications
- Local features extraction
- Histogram
- Integral images

# Map pattern

## Map pattern overview

- Un pixel en entree et sortie
- La dependance est nulle

<div class="alert alert-info" role="alert" markdown="1">
Map replicated a function over every element of an index set.
The computation of each pixel is independant wrt the others
</div>

`out(x,y) = f(in(x,y))`

![](https://i.imgur.com/fbjNWGZ.png)

![](https://i.imgur.com/Mk2oJIk.png)

*What do you think about `k`'s impact of the performance ?*
Le premier fait `threadIdx.x + k` et l'autre fait `threadIdx.x * k`

- A gauche, le thread numero i est le thread numero i+1: **c'est continue au niveau des addresses memoire** (lineaire)
- A droite: acces stride (palier)

![](https://i.imgur.com/AsmEcfK.png)

<div class="alert alert-success" role="alert" markdown="1">
- Linear sequential access with offset c'est bien
- Strided access c'est po bien
</div>

### Strided access pattern

![](https://i.imgur.com/UIPbkpm.png)

Sur le kernel numero 2, un grand temps du process est passe pour la gestion memoire (acces memoire mal fait)

# Memory performance
## Memory bandwith

What you think about memory

![](https://i.imgur.com/B9ci8TU.png)

Reality:

![](https://i.imgur.com/tv7pZTj.png)

## Memory access hierarchy

![](https://i.imgur.com/26hzlga.png)

- Memoire L2: cache intermediaire
- Memoire sur le chip low-latency
    - Registres
    - Shared memory
    - L1 (meme zone que shared memory)
        - Dire au processeur de gerer la memoire ou la gerer nous-meme
        - Dans ce cas on configure nous meme la shared memory
        - Sers de cache entre le L2 et la shared memory

## Cached Loads from L1 low-latency

2 choses a prendre en compte:
1. acces memoire alignes ou non
2. acces memoire coalesced (stride) ou non

2 types of global memory loads: **cached** or **uncached**

### Aligned vs Misaligned
A load is **aligned** if the first address of a memory access in 32 bytes
- Memory addresses must be type-aligned (`typeof(machin)`)
- Otherwise poor perf
- `cudaMalloc` = alignement on 256 bits at least

### Coalesced vs uncoalesced
A **load** is coalesced if a warp access is non-continuous


## Misaligned cached loads from L1

We need a load strategy:
- 32 threads of warp access a 32-bit word = 128 bytes
- 128 bytes = L1 bus (single load - bus utilization = 100%)
- Access permutation has no (or very low) overheard

![](https://i.imgur.com/iwWlZJZ.png)

- If data are not 128-bits aligned, 2 loads are required

Adresses 96-224 required.. but 0-256 loaded

![](https://i.imgur.com/Z4BOxMo.png)

- If data is accessed strided

![](https://i.imgur.com/sBfwvO6.png)

![](https://i.imgur.com/oeBdxY5.png)


*Pas possible d'augmenter la taille du bus ?*
Le bus est fixe (hardware)

## Loads from gloabl (uncached) memory

Same idea but memory is split in segments of 32 bytes

![](https://i.imgur.com/ri57qfT.png)

## Coalesced Memory Access (summary)

![](https://i.imgur.com/HzDzK61.png)

![](https://i.imgur.com/yofR2mV.png)

## How memory works for real

- DRAM is organised in 2D Core array
- Each DRAM core array has about 16M bits

![](https://i.imgur.com/fsGELN3.png)

### Example
- A 4x4 memory cell
- With 4 bits pin interface width

![](https://i.imgur.com/H9l2qyo.png)

### DRAM Burst

La memoire est lente
- DDR = 1/2 interface speed
- DDR2 = 1/4 interface speed
- DDR3 = 1/8 interface speed

<div class="alert alert-success" role="alert" markdown="1">
Solution: Bursting
</div>

Load N x interface width of **the same row**

![](https://i.imgur.com/keRA3iG.png)

Au lieu d'avoir 1/4, on renvoit 3 x 1/4

Better, but not enough to saturate the memory bus

## Summary
- Use **coalesced** (*contiguous* and *aligned*) accessed to memory

![](https://i.imgur.com/D5Nbfwi.png)

*How to make coalesced loads with 2D arrays ?*
![](https://i.imgur.com/zVRBvKI.png)

<div class="alert alert-danger" role="alert" markdown="1">
Ca correspond au **pitch**
</div>
Pitch: taille des lignes pour que le debut des lignes correspond a un multiple de 32

# Using shared memory

## Transposition
![](https://i.imgur.com/TEq18Ug.png)

![](https://i.imgur.com/1FkMRoY.png)

*Where are non-coalesced access ?*
Sur un warp, les `x` sont lineaire (0 - 31). Ici, ce qui est lineaire selon x c'est la lecture dans `in`.
32 threads vont ecrire 32 elements non-continus

<div class="alert alert-success" role="alert" markdown="1">
`a[x][y]`
</div>

## Tiling and memory privatization

<div class="alert alert-info" role="alert" markdown="1">
On decoupe le travaille en sous-block (tuile)

![](https://i.imgur.com/AaI69bz.png)

</div>
> Ca marche bien sur les images !

For each block:
- Read the tile from global to private block memory
- process the block (used shared memory)
- write the tile from the private (shared) block memory to global memory

![](https://i.imgur.com/MdMGfx4.png)

### Collaborative loading and writing then BLOCKDIM = TILEDIM
- All threads load one or more data
- Access must be **coalesced**
- Use barrier synch to make sure that all threads are ready to start the phase

![](https://i.imgur.com/CV8GUbH.png)

*Est-ce que ecrire dans la tile c'est lineaire ?*
Pour chaque ligne `y`, `x` va varier le plus rapidement possible: c'est lineaire

### Tiled transposition in shared memory

![](https://i.imgur.com/3kENRo7.png)

L'algorithme pour transposer en utilisant la shared memory commence par copier la taille en shared memory, transpose en shared memory et transpose les acces coalesced en memoire globale

![](https://i.imgur.com/KscPzBJ.png)

*A quel moment on fait des acces aligned dans la shared memory ?*
On lit de maniere alignee en global, on ecrit en aligne partout sauf la derniere ligne ou c'est un acces non-aligne

![](https://i.imgur.com/gqT5i0W.png)

Performance (GB/s on TESLA K40)

![](https://i.imgur.com/bcKFDsm.png)

Speed up de 2 entre la version qui utilise la shared memory et celle qui ne l'utilise pas

# About shared memory

*Comment on peut combler le gap (encore) entre les GB/s de la TESLA ?*

## DRAM banks

- Bursting: access multiple locations of a line in the DRAM core array (horizontal parallelism)

![](https://i.imgur.com/j7rOC0e.png)

<div class="alert alert-success" role="alert" markdown="1">
Permet d'utiliser d'avantage la memoire a sa capacite totale
</div>

## Bank conflits in shared memory

- If 2 threads try to perform 2 **different** loads in the same bank $\to$ **Bank conflict**
- Evert bank can provide 64 bits every cycle
- Only 2 modes:
    1. Change after 32 bits
    2. Change after 64 bits

![](https://i.imgur.com/3lRZhel.png)

<div class="alert alert-success" role="alert" markdown="1">
Demander la meme adresse par 2 threads differents ne pose pas de problemes
</div>

Les addresses consecutives ne sont pas dans les memes banques. 

### 2-way conflicts:

![](https://i.imgur.comXkxAjy.png)

On fait 2 loads en shared memory

<div class="alert alert-warning" role="alert" markdown="1">
Conflict = serialized access po bien
</div>

![](https://i.imgur.com/YmfxB50.png)

## Concrete example for shared memory

- Bank size: 4B = 4 uint8
- 32 Banks - Many channels
- Warp size = 32 threads

![](https://i.imgur.com/oQ66wiH.png)

![](https://i.imgur.com/O7xreLP.png)


**Pour le premier cas du tableau:**
*Est-ce qu'il a des threads qui demandent des addresses differentes dans une meme banque ?*
Non

*Quel est le nombre de loads (requetes memoire) qu'on va effectuer ?*
Une seule requete memoire

|op|Items|Bank used|Conflict Free|#Loads|
|--|-----|---------|-------------|------|
|`load M[tid.x]`|$[0,1,...,31]$|$[0,1,...,7]$|Oui|1|
|`load M[tid.x % 4]`|$[0,1,2,3,0,1,2,3...]$|$[0]$|Oui|1|
|`load M[tid.x + 1]`|$[1,2,3,...32]$|$[0,1,...,8]$|Oui|1|
|`load M[tid.x * 2]`|$[0,1,2,3,...62]$|$[0,1,...,15]$|Oui|1|
|`load M[tid.x * 8]`|$[0,8,...248]$|$[0,2,...,30]$|Non (conflits sur toutes les banques)|2|
|`load M[tid.x * 12]`|$[0,8,...248]$|$[0,1,...,31]$|Oui|1|

`load M[tid.x * 8]`:
![](https://i.imgur.com/jAku2dw.png)

`load M[tid.x * 12]`:
![](https://i.imgur.com/etNDHqA.png)

# Bank conflicts in Transpose

![](https://i.imgur.com/J0S9MsY.png)

![](https://i.imgur.com/dQwmZid.png)

Si on a 32 banques, on utilisent que 2 banques sur 32 et on a plein de conflits.

<div class="alert alert-warning" role="alert" markdown="1">
Reading a column may cause bank conflict
</div>

## Solution to bank conflicts

### With padding (to WRAP_SIZE + 1)

![](https://i.imgur.com/ERSDmSC.png)

*Comment se passe la lecture des columns ?*
Avec le padding, on decale la lecture de 1 (on se decale d'une banaque). En lisant la 1ere column, on tombe toujours dans une banque differente, evitant ainsi les conflits.

### Index mapping function

![](https://i.imgur.com/FajHwoH.png)

## Performances (GB/s on TESLA K40)

![](https://i.imgur.com/NlafuWa.png)

## Shared memory (summary)

- Super fast access (almost as fast as registers)
- But limited resources

### Occupancy

![](https://i.imgur.com/H0OfGMx.png)

# Stencil Pattern

Use case:
- Dilation/erosion
- Box (Mean) / Convolution Filters
- Bilateral Filter
- Gaussian Filter
- Sobel Filter

![](https://i.imgur.com/k1qCOk7.png)

<div class="alert alert-warning" role="alert" markdown="1">
Il y a une dependance entre les pixels
</div>

## Naive Stencil Implem

Local average with a rectangle of radius $r$ (Ignoring border problems for now)

![](https://i.imgur.com/CDF9LBE.png)

## Naive Stencil Performance

Say we have this GPU:
- Peak power: 1 500 GFlops and Memory Bandwith: 200 GB/s

All threads access global memory
- 1 memory access for 1 FP addition
- Requires 1500 x `sizeof(float)` = 6 TB/s of data
- But only 200 GB/x mem bandwith $\to$ 50 GLFOPS (3% the peak)

![](https://i.imgur.com/WaaSHtg.png)

<div class="alert alert-warning" role="alert" markdown="1">
Problem: too many access to global memory
</div>

<div class="alert alert-success" role="alert" markdown="1">
Solution: tiling, copy data in shared memory to global memory
</div>

## Handling Border

![](https://i.imgur.com/7Ke7pfY.png)

1. Add border to the image to have in-memory access
2. Copy tile + border to shared memory

### The bad way
Each thread copies one value and border threads are then idle

![](https://i.imgur.com/i8tbBEO.png)

### The good way

A thread may copy several pixels

![](https://i.imgur.com/pvXUUJC.png)

## Stencil pattern with tiling performance

![](https://i.imgur.com/wN0CVgX.png)

# Reduction Pattern

## Intuition for reduction pattern

> Reduction combines every elemet in a collection into one element using an associative operator

## Reduction pattern: solution 1

![](https://i.imgur.com/WeQUfQW.png)

*Est-ce que c'est correct ?*
Non, on va avoir des acces concurentiels (data race)

### Data race

<div class="alert alert-info" role="alert" markdown="1">
Plusieurs parties d'un programme qui essaie d'acceder sans ordre predefini a la meme donnee
</div>

![](https://i.imgur.com/R1q5wFy.png)

We need to ensure that each of those read-compute-write sequences are **atomic**.

## Atomics reminder

Atomics
- Read, modify, write in 1 operation
- Cannot be mixed with accesses from other threads
- On global memory and shared memory
- Atomic operations to the same address are serialized

Operations
![](https://i.imgur.com/J0MTpux.png)

## Reduction Pattern Corrected

**Accumulation in global memory**

![](https://i.imgur.com/8QdeZd4.png)

**Analysis**

![](https://i.imgur.com/EcRZIrW.png)


Time: 5.619 ms
Correct result but **high contention** on the global atomic variable

<div class="alert alert-success" role="alert" markdown="1">
The execution is actually **sequential** !
</div>

## Global atomics: is this really parallel ?
This version will produce the right result. However, **is it really parallel ?**

How our global atomic instruction is executed:
1. lock memory cell
2. read old value
3. compute new value
4. write new value
5. release the memory cell

Memory cell = cache line burst

Our kernel generates a lot of collisions on global memory

## Leverage Shared Memory

Atomic operations are **much**

## Motivation for output privatization

![](https://i.imgur.com/v8beAV1.png)

![](https://i.imgur.com/mCcY84B.png)

## Using shared memory

![](https://i.imgur.com/xGWVBNv.png)

## Reduction pattern V2: Output privatization

![](https://i.imgur.com/R98fyGN.png)

### With sync

![](https://i.imgur.com/hT3muek.png)

![](https://i.imgur.com/qHcQ2Xc.png)

## Reduction functions and trees

On peut reduire en parallele plusieurs fragments

![](https://i.imgur.com/Ps454nh.png)

## Complexity in steps and operations

![](https://i.imgur.com/SDnMiRA.png)


The tree parallel version is:
- work efficient
- not resource efficient
    - Average number of thread $((N-1/\log_2(N))$ << peak requirement ($N/2$)

### Proof of number of operations
 
![](https://i.imgur.com/dpfV5lj.png)

## Reduction pattern: tree reduction without atomics

![](https://i.imgur.com/jJNk6qz.png)

- Use a local sum without atomics
    - Map reduction tree to compute units (threads)
- Add to a global atomic once for each block

![](https://i.imgur.com/Dv7RNfJ.png)

![](https://i.imgur.com/WEGvBcP.png)

**What is happening ?**
The (naive) tree version is slower than the locally sequential version

## Sp starvation

In each iteration, 2 control flow paths will be sequentiall traversed for each warp
- Threads that perform addition and threads that do not
- Threads that do not perform addition **still consume execution resources**

## Resource efficient version

![](https://i.imgur.com/vA8Y2QC.png)

Tous les threads vont etre utilise sauf a la fin. On va avoir que des warps actifs, a chaque iterations on libere la moitie des warps.

![](https://i.imgur.com/hKwmj9M.png)

## A quick analysis

For a 1024 thread block
- No divergence on the first 5 steps
    - 1024, 512, 256, 128, 64, 32 consecutive threads are active in each step
    - All threads in each warp either all active or all inactive
- The final 5 steps will still have divergence
    - Can use warp-level optimization then (warp suffle)

## Limit global collision
*What happens with very large input arrays ?*
**Lot of global atomics**

*How to avoid this ?*
**Global array, one cell for each block**
- No more locks
- But requires a second level of reduction

**More work per thread**
- Just fire enough blocks to hide latency
- Sequential reduction, then tree reduction
- "algorithm cascading"

## Algorithm cascading
Perform first reduction during the collaborative loading

<div class="alert alert-warning" role="alert" markdown="1">
Warning: kernel launch parameters must be scaled accordingly !
</div>

![](https://i.imgur.com/LsGjS5w.png)

## Last optimizations
 
 Loop unrolling
 - Unroll tree reduction loop for the last warp (less sync needed)
 - Unroll all tree reduction loops (need to know block size)
 - Unroll the sequential reduction loop (knowing the work per thread)

# Histogram computation
## Mandelbrot practice session

 During the practice session, you will have to compute the **cumulated histogram** of the image.
 
 1. Compute the histogram $H$
     - Count the number of occurences of each value
 2. Computed the cumulated histogram $C$

![](https://i.imgur.com/cGXIbYP.png)

<div class="alert alert-warning" role="alert" markdown="1">
Inefficient, *non-coalesced* memory access
</div>

## First sample code

![](https://i.imgur.com/eMOR4VG.png)

*What is the issue ?*
Ajouter un data array

![](https://i.imgur.com/rnUgffz.png)

## Parallel algorithm using output privatization

### Local histogram
#### Initialization

Shared memory must be initialized
This can be done with the "comb-like" pattern

![](https://i.imgur.com/unIYdXO.png)

<div class="alert alert-warning" role="alert" markdown="1">
We need synchronization after this stage
</div>

#### Computation
Like previous code, but with local atomics 

![](https://i.imgur.com/ke6xZ3o.png)

<div class="alert alert-warning" role="alert" markdown="1">
We need synchronization after this stage
</div>

#### Commit to global memory

![](https://i.imgur.com/je24ZHQ.png)

`int n = blockDim.x * threadIdx.y + threadIdx.x`

## Summary
Performance boosters:
- Coalesced accesses
- Output privatization

Requirements:
- atomics
- synchronization

# Scan pattern
## What is a scan ?

<div class="alert alert-info" role="alert" markdown="1">
Scan computes all partial reductions of a collection
</div>

![](https://i.imgur.com/yvFGSq8.png)

Usage:
- Integration (cumulated histogram)
- Resource allocation (memory to parallel threads, camping spots...)
- Base building block for many algorithms (sorts, strings comparisons)

## Performance baselines

![](https://i.imgur.com/Cj1a8dh.png)

**Sequential version**

### Naive parallel version

Have every thread to add up all x elements needed for the y element

## Scan pattern at the warp or block level
### Kogge-Stone

![](https://i.imgur.com/zh1JFSK.png)

- Number of steps: $\log N$ (bien)
- Ressource efficiency (bien)
- Work efficiency $\sim N\log N$ (pas bien)

### Brent-Kung

![](https://i.imgur.com/0JJb8j7.png)

- Number of steps: $2\log N$
- Ressource efficiency: all warps remain active till the end (pas bien)
- Work efficiency: $2N$ (bien)

### Sklansky

![](https://i.imgur.com/Skxx9gb.png)

- Number of steps: $\log N$
- Ressource efficiency: bien
- Work efficiency: $\frac{N}{2}\log N$ (bien)

## Scan Pattern at the Block or Grid Level

The patterns before can be applied:
- At the warp level (no sync until Volta)
- At the block level (thread sync)

At the global level: multi-level kernel app in global memory
- Scan then propagate
- Reduce then scan

### Scan then propagate

![](https://i.imgur.com/tEcHvf6.png)

### Reduce then scan

![](https://i.imgur.com/qzKo8RB.png)

## Summary

![](https://i.imgur.com/sfbYbdL.png)
