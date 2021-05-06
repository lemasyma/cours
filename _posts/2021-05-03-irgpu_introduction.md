---
title:          "IRGPU: Introduction"
date:           2021-05-03 10:00
categories:     [Image S8, IRGPU]
tags:           [Image, S8, IRGPU]
description: Introduction
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/ryMz0maDu)

# Agenda
1. GPU and architectures (2h)
2. Programming GPUs with CUDA (2h)
3. TP 00 CUDA (3h)
4. Efficient programming with GPU (2h)
5. TP 01 CUDA

# GPU and architectures
## Why using GPU ?

<div class="alert alert-info" role="alert" markdown="1">
On veut faire de la programmation **rapide**.
</div>
Un programme rapide est un programme qui *consomme moins*.

<div class="alert alert-warning" role="alert" markdown="1">
C'est important de consommer moins
</div>
> Ex: nos smartphones consomment enormement d'energie, avoir des programmes qui consomment le moins possible permet d'economiser la batterie

On est aujourd'hui dans l'ere du big data, on veut traiter rapidement un tres gros volume de donnees. Sinon on aurait jamais ete capable d'avoir des techs comme les reseaux de neurones.

On veut que les programmes s'executent dans un temps borne.
> On est pas des gistres... Mais quand meme

On veut pas une reponse d'1h avec des systemes critiques embarques (voitures, fusees, etc.)

![](https://i.imgur.com/5jy52aK.png)

## Power Consumption on Smartphones
CPU is a major source of power in smartphones (even with graphical-oriented app)

![](https://i.imgur.com/yjVzRpI.png)

> Une bonne partie de la batterie est consommee par le CPU et GPU

Aujourd'hui, on essaie de tout transferer sur le GPU car ca consomme moins que le CPU

## Power Consumption of Some Processors
![](https://i.imgur.com/RzDoEgV.png)

*Qu'est-ce qu'on remarque du prix par Gigaflops ?*
<div class="alert alert-success" role="alert" markdown="1">
Le GPU est **beaucoup plus rentable** que le CPU.
</div>

<div class="alert alert-danger" role="alert" markdown="1">
Tous les calculs ne sont pas basculables du CPU au GPU.
</div>

# Scientific Computing
## A bit of history - The first GPU
Ce qui a motive la creation des GPU c'etait la medecine, etc. (meme si le gaming en a prit l'avantage).

- Back in 70's GPU were for Image Synthesis
- First GPU: Ikonas RDS-3000
    - A l'epoque: tres difficile de programmer en GPU
- N. England & M. Witton founded Ikonas Graphics Systems

![](https://i.imgur.com/mQviBRh.png)


## The first GPGPU

![](https://i.imgur.com/YjRHZzv.png)


<div class="alert alert-info" role="alert" markdown="1">
**General Purpose GPU**
</div>

First programmable GPU:
- Vertex Shaders: programmable vertex transforms, 32-bits float
    - Pipeline graphics
    - Shaders: etapes de la pipeline qu'on pouvait remplacer
    - A ouvert la voie vers le scientific computic
- Data-dependent, configurable texturing + register combiners

Enabled early GPGPU results:
- Hoff (1999): Voronoi diagrams on NVIDIA TNT2
- Larsen & MacAllister (2001): first GPU matrix multiplication (8-bit)
- Rumpf & Strzodka (2001): first GPU PDEs

## GPGPU for physics simulation on Geforce 3

Approximate simulation of natural phenomenon

![](https://i.imgur.com/OfG7Gl3.png)


## GEFORCE FX (2003): floating point
True programmability enabled broader simulation research
- Ray Tracing
- Radiosity
- PDE solvers
- Physically-base simulation
- FFT (2003)
- High-level language: Brook for GPU (2004)

![](https://i.imgur.com/vT03I3c.png)

## GPGPU becomes a trend (2006)
2 factors for the massive surge in GPGPU dev:
- **Architecture Nvidia G80**
    - Dedicated computing mode - threads rather than pixels/vertices
    - General, byte-addressable memory architecture
- **Software support**
    - C and C++ languages and compilers for GPUs (spoiler.. it's **CUDA**)

![](https://i.imgur.com/kjsUg1A.png)

![](https://i.imgur.com/3kRFHS6.png)
> Le graphique a droite veut rien dire (c'est du marketing)

## 2010's
### Accelerating discoveries

![](https://i.imgur.com/GuYxUDd.png)

<div class="alert alert-danger" role="alert" markdown="1">
Without GPUs, supercomputer would like 5x more times
</div>

![](https://i.imgur.com/EJioPKf.png)

And data center gave birth to **Deep-Learning**

![](https://i.imgur.com/ANumAzh.png)
> Les reseaux de neurones existaient deja dans les annees 80 mais on n'avait pas la puissance de calcul avant 2010's

## Embedded systems - The *real*-time constraints

![](https://i.imgur.com/82MVjXL.png)

Need both of the 2 worlds:
- Need ultra-performance computing
- With limited resources

# GPU vs CPU for parallelism
## How to get things *done* quicker
1. Do less work
2. Do *some* work better (i.e. the one being he more time-consuming)
3. Do *some* work at the sane time
4. Distribute work between different workers
    1. Choose the most adapted *algorithms*, and avoid re-computing thing
    2. Choose the most adapted *data structures*
5. Parallelism

## Why parallelism ?
<div class="alert alert-info" role="alert" markdown="1">
**Moore's law**: processors are *not* getting twice as powerful every 2 years anymore
</div>

![](https://i.imgur.com/V2HJYR3.png)

- So the processor is getting smarter
    - Out-of-order execution / dynamic register renaming
    - Speculative execution with branch prediction
- And the processor is getting super-scalar
    - Executer des choses en meme temps
    - Nos CPUs sont des processeurs super-scalaires

## Toward data-oritented programming

![](https://i.imgur.com/hkNh64r.png)

## The burger factory assembly line

![](https://i.imgur.com/9CaFieq.png)

*How to make several sandwiches as fast as possible ?*
- Avoir plusieurs personnes qui travaillent en meme temps sur le meme sandwich et vont executer les taches independantes en meme temps, avoir un worker maitre qui s'occupe d'assembler tout
- Avoir plusieurs workers qui travaillent en meme temps sur des sandwichs differents
- Mix entre les 2 strategies precedente: un worker qui peut bosser sur un sandwich ou plusieurs en meme temps
- Pipeline: un worker fait une etape et passe le sandwich a un autre worker
- Un worker a plusieurs bras


A prendre en compte:
- La latence
- Le debit

Avec la 1ere strategie:
2 cycles
- optimisation en latence et debit
- Pas la plus efficace car etape de synchronisation

Avec la 2e strategie
- Optimisation en debit mais pas en latence

Avec la 3e strategie:
- Tres lourd niveau synchronisation

## Data-oriented programming parallelism

Flynn's Taxonomy

![](https://i.imgur.com/rl9WOdu.png)

- SISD: no parallelism
- SIMD: same instruction on data group (vector)
- MISD: rare, mostly used for fault tolerant code
- MIMD: usual parallel mode (multithreading)
- SPMT: Single Programm Multiple Thread
    - Execute le meme programme

### Optimize for latency (MIMD with collaborative workers)

4 **super-workers** (4 CPU cores) collaborate to make 1 sandwich
- Manu gets the bread and wait for the others

![](https://i.imgur.com/1iAvEme.png)


Time to make 4 sandwicches: $s$ (400% speed-up)

### Optimize for throughtput (MIMD Horizontal with multiple jobs)

![](https://i.imgur.com/piN1o3u.png)

Time to make 4 sandwiches: *s* (400% speed-up)

### Optimize for throughput (MIMD Vertical Pipelining)

![](https://i.imgur.com/aY23s66.png)

### Optimize for throughput (SIMD DLP)

![](https://i.imgur.coml4iW3P.png)

<div class="alert alert-success" role="alert" markdown="1">
Un seul optimise en latence
</div>

## More cores is trendy

Data-oriented design have changed the way we make processors (even CPUs)
- Lower clock rate
- Large vector-size, more vector-oriented ISA
- More cores (processing units)

![](https://i.imgur.com/PKtI2Cc.png)

<div class="alert alert-info" role="alert" markdown="1">
Parallelisme: SIMD
</div>

Depuis 2005/2006, on a des "faux" coeurs pour faire du multi-threading

![](https://i.imgur.com/MdzsNoT.png)

![](https://i.imgur.com/fB4ikRi.png)

## CPU vs GPU performance

And you see it with HPC apps:
![](https://i.imgur.com/9aLv19X.png)

## Towards Heterogeneous Architectures

But don't forget, you may need to optimize both **latency** and **throughput**

What is the bounds speedup attainable on a parallel machine with a program which is parallelizable at $P\%$ (i.e. must run sequentially for $(1-P)$)

![](https://i.imgur.com/IcHh1Nf.png)

![](https://i.imgur.com/jjnaj9M.png)

![](https://i.imgur.com/5CoCqIB.png)

<div class="alert alert-success" role="alert" markdown="1">
Utiliser la bonne architecture pour le bon travail
</div>

![](https://i.imgur.com/Qun7G6L.png)

# GPU vs CPU architectures
## It's all about the data... The CPU:

![](https://i.imgur.com/bF0AHjZ.png)

- optimized for low-latency **access** (many memory caches)
- Control logic for out-of-order and speculative execution

![](https://i.imgur.com/WzKN3uI.png)

![](https://i.imgur.com/ZHQfywy.png)


## It's all about data.. the GPU:

![](https://i.imgur.com/jIoDCAp.png)

## Hiding latency with thread parallelism & pipelining

So... you want to hide the latency of getting data from from global memory... how ?

1 CPU Core:
![](https://i.imgur.com/38NUipK.png)

1 GPU SMP (Streaming Multiprocessor)
![](https://i.imgur.com/DCwroWs.png)

CPU:
- low-latency memory to get data ready
- each thread context switch has a cost

GPU:
- memory latency hidden by **pipelining**
- context switch is free

Latency hiding:
- = do other operations when waiting for data
- = having a lot of parallelism
- = having a lot of data
- will run faster
- but not faster than the peak
- what is the peak btw ?

<div class="alert alert-info" role="alert" markdown="1">
**Peak**:
1. Peak de la memoire
    - Donnee par un nombre 
2. Peak du compute
    - Nombre d'instructions qu'on peut executer par secondes
</div>

## It's all about data... Little's law"

![](https://i.imgur.com/U5Bcw6d.png)

La latence est typiquement la longueur de la pipeline

## Hiding latency

With thread parallelism & pipelining

*Note that pipeline exists on CPUs (cycle de Von Neumann)*

![](https://i.imgur.com/Z838j2O.png)

## More about forms of parallelism (the why!)

![](https://i.imgur.com/Ok9TNLF.png)

## More about forms of parallelism (the how!)

![](https://i.imgur.com/XAU5irO.png)
![](https://i.imgur.com/ohaIgXG.png)
![](https://i.imgur.com/z18k7lR.png)

*Pourquoi on a un TLP horizontal sur les CPUs ?*
Multicoeurs
*Pourquoi on a un TLP vertical sur les CPUs ?*
Les hypercoeurs (coeurs logiques). Ce ne sont pas des vrais coeurs mais des threads capables de switch sur les coeurs.

## Extracting parallelism

![](https://i.imgur.com/dgwbeju.png)

## Parallel architectures and parallelism

![](https://i.imgur.com/fEMA6gi.png)

![](https://i.imgur.com/A2TGqEe.png)

- All processors use hardware to turn parallelsim into performance
