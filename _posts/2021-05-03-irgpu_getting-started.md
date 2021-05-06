---
title:          "IRGPU:  Getting started with CUDA"
date:           2021-05-03 14:00
categories:     [Image S8, IRGPU]
tags:           [Image, S8, IRGPU]
description:  Getting started with CUDA
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/rkfdcPavd)

# CUDA overview
## What is CUDA ?
A product
- It enables to use NVidia GPUs for computation

A C/C++ variant
- Mostly C++ 15 compatible, with extensions
- and also some restrictions !

A SDK
- A set of compilers and toolchains for various architectures
- Performance analysis tools

A runtime
- An assembly specification
- Computation libraries (linear algebra, etc.)

A new industry standard
- Used by every major deep learning framework
- Replacing OpenCL as Vulka is replacing OpenGL

## The CUDA ecosystem (2021)
![](https://i.imgur.com/jyZ9il1.png)

## Libraries *or* Compiler Directives *or* Programming Language ?

CUDA is mostly based on a "new" **programming language**: CUDA C (or C++, or Fortran)
> This grants much flexibility and performance

But is also exposes much of GPU goodness through **libraries**

An it supports a few **compiler directives** to facilitate some constructs 

## The big idea: Kernels instead of loops

![](https://i.imgur.com/MomimT7.png)

![](https://i.imgur.com/RR1Uc8A.png)

![](https://i.imgur.com/2zpoK0Z.png)

<div class="alert alert-success" role="alert" markdown="1">
No more `for` loop !
</div>

## Arrays of parallel threads
A CUDA kernel is executed by a **grid** (array) of threads
- All threads in grid run the same kernel code (Single Program Mutliple Data)
- Each thread has indexes that is used to compute memory addresses and compute decisions

![](https://i.imgur.com/piRxw0Q.png)

## Threads blocks
Threads are grouped into thread blocks
- Threads witihin a bloc cooperate via
    - *shared memory*
    - *atomic operations*
    - *barrier synchronization*
- Threads in different blocks do not interact

![](https://i.imgur.com/tQmgcy8.png)

### A multidimensional grid of computation threads

Each thread uses indices to decide what data to work on:
![](https://i.imgur.com/IYWVCfx.png)

Each index has $x$, $y$ and $z$ attributes

Grid and blocks can have different dimensions, but they usually are 2 levels of the same work decomposition

![](https://i.imgur.com/UzThWvv.png)

### Examples

![](https://i.imgur.com/jI0Buab.png)

![](https://i.imgur.com/j5pp4Yl.png)

## Block decomposition enable automatic scalability

![](https://i.imgur.com/J2dsHmg.png)


# Architecture
## Programming modeling

**Block**
A set of *threads* that cooperate:
- Synchronisation
- Shared memory
- Block ID = ID in a **grid**

**Grid**
Array of blocks executing same *kernel*
- Access to global GPU memory
- Sync. by stop and start a new kernel

![](https://i.imgur.com/w77cxAe.png)

![](https://i.imgur.com/Ol0ccWU.png)

## Mapping Programming model to hardware

![](https://i.imgur.com/PpSdlGS.png)

### the SMs

![](https://i.imgur.com/ECGCbjm.png)

## Zoom on the SM

![](https://i.imgur.com/fIOI7dS.png)

<div class="alert alert-info" role="alert" markdown="1">
*warp*: 32 unites de calcul
</div>

- SM organize **blocks** into **warps**
- 1 warp = group of 32 threads

GTX 920:
- 128 cores = 4 x 32 cores
- Quad warp scheduler selects 4 warps (TLP)
- And 2 independant instructions per warp can be dispatched each cycle (ILP)

> Ex: 1 (logical) *block* of 96 threads maps to: 3 (physical) *warps* of 32 threads

## Zoom on the CUDA cores

![](https://i.imgur.com/aNJ0IX9.png)

- A *warp* executes 32 threads on the 32 CUDA cores
- The threads executes *the same* instructions (*DLP*)
- All instructions are SIMD (width = 32) instructions

Each core:
- FLoating point & integer unit
- Fused multiply-add (FMA) instruction
- Logic unit
- Move, compare unit
- Branch unit
- The first IF/ID of the pipeline is done by the SM

<div class="alert alert-warning" role="alert" markdown="1">
SIMT allows to specify the execution
</div>

## The SIMT Execution Model on CUDA cores
SIMT: on programme comme si on avait un thread qui execute une donnees mais ca se cache derriere des instructions SIMD (a + b devient la somme du vecteur a avec le vecteur b)

<div class="alert alert-danger" role="alert" markdown="1">
Chaque thread va executer le meme kernel et instructions
</div>

- Divergent code paths (branching) pile up!

![](https://i.imgur.com/HhwTHnQ.png)

![](https://i.imgur.com/V8hUjR1.png)


If/else: tous les threads vont effectuer en meme temps le if et else


### If/else
What is the latency of this code in the best and worst case ?

![](https://i.imgur.com/1P8XxsN.png)

- Best case: $a\gt0$ is false for every thread. For all threads: `inst-d`
- Worst case: $a\gt0$ and $b\gt0$ is true for some but not all threads. For all threads: `inst-a`, `inst-b`, `inst-c`, `inst-d`

### Loops

![](https://i.imgur.com/W47FpFq.png)

## Final note about terminology

![](https://i.imgur.com/HR8PZ9G.png)

# GPU memory model
## Computation cost vs. memory cost
Power measurements on NVIDIA GT200

![](https://i.imgur.com/8rcKY55.png)

With the same amount of energy:
- Load 1 word from external memory (DRAM)
- Compute 44 flops

<div class="alert alert-success" role="alert" markdown="1">
Must optimize memory first
</div>

## External memory: discrete GPU
Classical CPU-GPU model
- Split memory space
- Highest bandwith from GPU memory
- Transfers to main memory are slower

![](https://i.imgur.com/v7rzntd.png)
> Intel i7 4770 / GTX 780

## External memory: embedded GPU

Most GPUs today:
- Same memory
- May support memory coherence (GPU can read directly from CPU caches)
- More contention on external memory

![](https://i.imgur.com/fmaa5LI.png)

## GPU: on-chip memory

Cache area in CPU vs GPU:
![](https://i.imgur.com/WUxFyh8.png)

But if we include registers:
![](https://i.imgur.com/IKccvrI.png)

<div class="alert alert-success" role="alert" markdown="1">
GPU has many more registers but made of simpler memory
</div>

## Memory model hierarchy 
### Hardware

![](https://i.imgur.com/JdjOci5.png)

Cache hierarchy:
- Keep frequently-accessed data Core
- Reduce throughtput demand on main memoru L1
- Managed by hardware (L1, L2) or software (shared memory)

On CPU, caches are designed to avoid memory latency
On GPU, multi-threading deals with memory latency

### Software
![](https://i.imgur.com/K1c7Aqe.png)

![](https://i.imgur.com/LvmwjeC.png)

## Building and running a simple program

![](https://i.imgur.com/OU0vg4l.png)

## What you need to get started
- NVidia GPU hardware
- NVidia GPU drivers, properly loaded
- CUDA runtime libraries
- CUDA SDK (NVCC compiler in particular)

# Summary
- Host vs Device $\leftrightarrow$ Separate memory
    - GPU are computation units which require explicit usage, as opposed to a CPU
    - Need to load data and fetch result from device
- Replace loops with kernels
    - Kernel = Function computed in relative isolation on small chunks of data
- Divide the work
- Compile and run using CUDA SDK

# Host view of GPU computation
## Sequential and parallel sections
- We use the GPU(s) as co-processor(s)

![](https://i.imgur.com/kO7Anul.png)

## CUDA memory primitives

![](https://i.imgur.com/NE4pw2T.png)

**Why 2D and 3D variants ?**
- Strong alignment requirements in device memory
    - Enables correct loading of memory chunks to SM caches (correct bank alignment)
- Proper striding management in automated fashion

## Host $\leftrightarrow$ Device memory transfer

![](https://i.imgur.com/y922J5t.png)

## Almost complete code

![](https://i.imgur.com/wWOFzSV.png)

## Checking errors

In practice check for API errors

![](https://i.imgur.com/0i5xiHN.png)

# Intermission: *Can I use memory management functions inside kernels ?*
**No**: `cudaMalloc()`, `cudaMemcpy()` and `cudaFree()` shall be called from host only

However, kernels may allocate, use and reclaim memory dynamically using regular `malloc()`

# Fix the kernel invocation line

We want to fix this line:
![](https://i.imgur.com/6GMimst.png)


Kernel invocation syntax:
![](https://i.imgur.com/w89y6Lw.png)

## How to set `gridDim` and `blockDim` properly ?

Lvl 0: Naive trial with as many threads as possible
![](https://i.imgur.com/xtNi10X.png)

- Will fail with large vectors
    - Hardware limitation on the maximum number of thread per block (1024 for compute capability 3.0-7.5)
- Will fail with vectors of size which is not a multiple of warp size

Lvl 1: It works with just enough blocks
![](https://i.imgur.com/9dpZy3p.png)

Lvl 2: Tune block size given the kernel requirements and hardware constraints
![](https://i.imgur.com/VvcBIdo.png)

## But wait...
![](https://i.imgur.com/hGbEKSS.png)

<div class="alert alert-warning" role="alert" markdown="1">
This code prints nothing !
</div>

<div class="alert alert-danger" role="alert" markdown="1">
Kernel invocation is asynchronous
</div>

![](https://i.imgur.com/r2N2gWq.png)

<div class="alert alert-success" role="alert" markdown="1">
Host code synchronization requires `cudaDeviceSynchronize()` because **kernel invocation is asynchronous** from host perspective.
</div>

On the device, kernel invocations are striclty sequential (unless you schedule them on different *streams*)

# Intermission: *Can I make kernels inside kernels ?*
**Yes**. This is the basic of *dynamic parallelism*

Some restrictions over the stack size apply.
Remember that the device runtime is a functional subset of the host runtime, ie you can perform device management, kernel launching, device `memcpy`, etc. but with some restrictions 

The compiler may inline some of those calls.

# Conclusion about the host-only view
A host-only view of the computation is sufficient for most of the cases:
1. upload data to the device
2. fire a kernel
3. download output data from the device

Advanced CUDA requires to make sure we saturate the SMs, and may imply some kernel study to determine the best:
- amount of threads per blocks
- amount of blocks per grid
- work per thread (if applicable)
- ...

This depends on:
- hardware specifications: maximum `gridDim` and `blockDim`, etc.
- kernel code: amount of register and shared memory used by each thread

# Kernel programming
## Several API levels

We now want to program kernels
There are several APIs available:
- PTX assembly
- Driver API (C)
- Runtime C++ API $\leftarrow$ **let's use this one**

## Function Execution Space Specifiers

![](https://i.imgur.com/iGYXzbR.png)

- `__global__` defines a kernel function
    - Each `__` consists of 2 underscore characters
    - A kernel function must return void
    - It may be called from another kernel for devices of compute capability 3.2 or higher (Dynamic Parallelism support)
- `__device__` and `__host__` can be used together
- `__host__` is optional if used alone

## Built-in Vector Types
They make it easy to work with data like images
**Alignement mus be respected** in all operations

![](https://i.imgur.com/KoGHgLn.png)

![](https://i.imgur.com/Lvk3u6h.png)

![](https://i.imgur.com/BzDXwjl.png)

<div class="alert alert-info" role="alert" markdown="1">
They all are structures
</div>

They all come with a constructor function of the form `make_<type name>`

![](https://i.imgur.com/w2vZgUb.png)

The 1st, 2nd, 3rd and 4th components are accessible through the fields $x$, $y$, $z$ respectively

## Built-in variable

![](https://i.imgur.com/ZuyLHCx.png)

### Example
![](https://i.imgur.com/BKYIIF9.png)

## Memory hierarchy

![](https://i.imgur.com/5W9tTTJ.png)

![](https://i.imgur.com/pMWK6zQ.png)

## Types of Memory
- Registers
    - Used to store parameters, local variables, etc.
    - Very fast
    - Private to each thread
    - Lots of thread $\Rightarrow$ little memory per threads
- Shared
    - Used to store temp data
    - Very fast
    - *Shared* among all threads in a block
- Constant
    - A special cach for read-only values
- Global
    - Large and slow
- Caches
    - Transparent uses
- Local

## Salient features of Device Memory

![](https://i.imgur.com/GaNsqf7.png)

![](https://i.imgur.com/MgD8NoP.png)

## Cost to access memory

![](https://i.imgur.com/bjn3Pvg.png)

## Variable Memory Space Specifiers

**How to declaring CUDA variables**

![](https://i.imgur.com/KnC7phe.png)

*Remarks:*
- `__device__` is optional when used with `__shared__` or `__constant__`
- Automatic variables reside in a register

*Where to declare variables ?*
Can host access it ?

|Yes|No|
|-|-|
|**global** and **constant**, declare outside of any function|**register** and **shared**, use of declare in the kernel|

## Who can be shared by who ?

Possible memory access:
- Among threads in the same grid (a kernel invocation)
    - Global memory
- Among threads in the same block
    - Global memory
    - Shared memory

## Relaxed consistency memory model

The CUDA programming model assumes a device with a **weakly-ordered memory model**, that is the order in which a CUDA thread writes data to shared memory or global memory, is not necessarily the order in which the data is observed being written by another CUDA or host thread

### Example

![](https://i.imgur.com/cS4cxhv.png)

![](https://i.imgur.com/m5MoQtN.png)

*Possible outcomes for thread 2 ?*
![](https://i.imgur.com/G48Oday.png)

![](https://i.imgur.com/jInFIjp.png)

## Memory Fence Functions

Memory fence functions can be used to enforce some ordering on memory accesses

![](https://i.imgur.com/GoKrGxt.png)
Ensures that:
- All writes to all memory made by the calling thread before the call to `__threadfence_block()`
- All reads from all memory

## Synch functions

![](https://i.imgur.com/e5hbmpM.png)

<div class="alert alert-danger" role="alert" markdown="1">
Stronger than `__threadfence()` because it also synchronizes the execution
</div>

![](https://i.imgur.com/mVylLzi.png)

## Atomic functions

<div class="alert alert-info" role="alert" markdown="1">
Atomic functions perform a read-modify-write atomic operation on one 32-bit or 64-bit word residing in global or shared memory
</div>

Most of the atomic functions are available for all the numerical type

### Arithmetic functions

![](https://i.imgur.com/wmwCTvH.png)

# Debugging, performance analysis and profiling

## `printf`
Possible since Fermi devices (Compute Capability 2.x and higher)


Limited amount of lines:
- circular buffer flushed at particular times

## Global memory write
To dump then inspect a larger amount of intermediate data
Analysis code should be removed for production

### Example
![](https://i.imgur.com/tRumZ46.png)

## CUDA tools
![](https://i.imgur.com/dg1HAod.png)

## The complete compilation trajectory

![](https://i.imgur.com/bgsNioU.png)
