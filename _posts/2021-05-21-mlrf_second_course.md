---
title:          "MLRF: Lecture 02"
date:           2021-05-21 10:00
categories:     [Image S8, MLRF]
tags:           [Image, SCIA, MLRF, S8]
math: true
description: Lecture 02
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/SyZvLkrYO)

# Agenda for lecture 2
1. Introduction
2. Global image descriptors
3. Clustering
4. Local feature detectors

# Introduction
## Summary of last lecture
Machine learning
- Machine learning = searching for the best model in a hypothesis space
- Inductive machine learning, optimization-based
- Inductive bias, bias/vairance compromise
- Supervised, reinforcement, unsupervised learning
- Regression, classification, density estimation
- Model validation: test generalisation, separate/decorrelate test & training sets

Template matching
- Sum of squared differences $(T-I)^2$, or correlation-based methodes ($T\times I$)
- Normalization needed for correlation-based methods
- Tolerates translation and small noise, but not rotation, intensity shift, ...

## Debrief of practice session 1

**PS1 content**
1. Jupyter tricks
2. NumPy reminders 
3. Intro to image manipulations
4. Twin it! part 1: template matching
5. (Bonus level: segmentation)

### Take home messages

![](https://i.imgur.com/igVepmo.png)

> How annoying was it to *manually adjust color thresholds* to select the duck ?
> How could have we *automated* it ?

Results with method `SQDIFF_NORMED` (lower is better)

![](https://i.imgur.com/dS4iuLi.png)

> Strengths and weaknesses of *template matching* for the *Twin It!* case ?
> Effects of *normalization* ?

## Next practice session

*Twin it!* again, with a slightly more elaborated approach
1. Pre-selected bubbles based on their colors $\Rightarrow$ color histograms

![](https://i.imgur.com/dIXqJBc.png)

### Color histogram: in details

1.1 Color quantization: reduce the colors of the bubbles

![](https://i.imgur.com/PU2Lk3G.png)

1.2. Compute the color histogram of each bubble

![](https://i.imgur.com/rG7g1OL.png)

1.3. Compute the distance matrix between each bubble, using its color histogram

![](https://i.imgur.com/AqJonwW.png)


1.4 Visualize the bubbles in an interesting way using hierarchical clustering

2.For the pre-selected bubbles, check their content is similar 
- $\Rightarrow$ Detect stable points and extract the patches around them ![](https://i.imgur.com/YmgFLav.png) ![](https://i.imgur.com/zmSqLzZ.png)
- Compare (match) those patches ![](https://i.imgur.com/Uzm6ihK.png) ![](https://i.imgur.com/UQWmc6N.png)

# Image descriptors
## Issues with method based on pixel comparison

What is important ? What do they consider? **Raw pixels!**
- We want to be able to make use of **domain knowledge**
- > Like sensitivity to shape, or dominant color information

## Overview
Different sizes and contents
- Different kinds of descriptors

![](https://i.imgur.com/pLlx1Rd.png)

Different problems $\Rightarrow$ Different choices
- Computation/memory constraints
- Which perturbations do we have to tolerate ?

# Global image descriptors
## Two approaches
**Global image descriptors**
- Compute **statistics about the content** of the image
- Produce a **single global vector**

<div class="alert alert-info" role="alert" markdown="1">
Very attractive because they are very fast to compute and match, but...
</div>

**Bag of Features techniques** (lecture 4)
- **Select regions** of interest in the image (may be a variable quantity)
- Compute descriptors for each region
- Index each part separately (like a text seach engine which indexes words)

> It is always possible to build a sing descriptors from multiple ones

## Color histograms
High invariance to many transformation
> rotation, scaling thanks to normalization, perspective
But limited discriminative power

**Easy to implement**
1. Reduce the colors (opt. when performing backprojection)
2. Compute a reduced color histogram on each image
3. Use a distribution distance to compare the descriptors

### Some results on *Twin It!*

![](https://i.imgur.com/1c2fPAo.jpg)

### Steps by step
#### 1: Color reduction
1. use K-Means or any other clustering technique to find *N* useful colors
2. Project each pixels


![](https://i.imgur.com/ohG04XD.jpg)

<div class="alert alert-warning" role="alert" markdown="1">
**One possible result** on the *Twin It!* poster
</div>

#### 2: Histogram computation

You already know it (*Normalize it*)

![](https://i.imgur.com/SPYYQlQ.png)

#### 3: Descriptor comparison

![](https://i.imgur.com/ZP3GDlZ.png)

# Other global image descriptor
## More global descriptors
GIST of a scene:
- Oliva, Torralba, "Modeling the shape of the scene"

![](https://i.imgur.com/GGvNF8M.png)

# Global descriptors
## Drawback
*Accordin to F. Perronnin:*
Highly efficient to compute and to match $\Rightarrow$ **perfect in theory**

<div class="alert alert-warning" role="alert" markdown="1">
But robusteness vs informativeness tradeoff is hard to set
</div>

(personal conclusion)
- Approache based on **global image descriptors** are confined to **near-duplicate detection** applications until now
- Modern search engine uses local representations and leverage them

# Clustering
## Finding groups in data
Many techniques:
- Connectivity models
    - hierarchical clustering,...
    - clustering = set of neighbors
- Centroid models: k-means
    - cluster = centroid point
- Distribution model
    - Gaussian mixtures models est. w. Expection maxim
    - cluster = statistical distribution
- Density models
- Graph-based models

Always the same goal:
- Minimise the differences between elements within the same cluster
- Maximise the differences between elements within different cluster

Number of clusters:
- Many methods require to choose it beforehand
- Several techniques to adjust the number of clusters automatically

Outliers rejection:
- Some techniques do not assign lonely points to any cluster

<div class="alert alert-success" role="alert" markdown="1">
Focus on HAC and K-Means today
</div>

# Hierarchical Agglomerative Clustering

![](https://i.imgur.com/wOxBd2O.png)

## Some linkage types
- Single linkage
    - minimizes the distance between the closest observations
- Maximum or complete linkage
- Average linkage
- Centroid linkage
- Waard criterion

## Divisive clustering
HAC is *bottom-up*, divisive clustering is *top-down*
Classical approach:
1. Start with all data
2. Apply flat clustering
3. Recursively apply the approach on each cluster until some termination

Pros: can have more than 2 sub-trees, must faster than HAC
Cons: same issues as flat clustering, non-determinism

# K-means
## K-Mean clustering (again)
<div class="alert alert-info" role="alert" markdown="1">
The K-means algorithm aims to choose centroids that minimise the inertia, or within-cluster sum-of-squares criterion

![](https://i.imgur.com/uWZCcSl.png)

</div>
- it does not maximizes inter-cluster disantce
- it puts centers so as to get the best coverage (may not be on a density peak !)

### Algorithm
Initialization:
- Randomly selected cluster centers
- Calculate distance oiunts $\Leftrightarrow$ centers
- Assign each point to closest center
- Update cluster centers: avg of points

Result: centroid centers
- local maximax
- tessellation / Voronoi set over the dataset

![](https://i.imgur.com/MsQrOMB.png)

The previous algorithm is called "**Batch K-Means**" or simply "**K-Means**" because it considers the **whole dataset at each iteration**.

Batcj K-Means is not only **sensible to outliers** and **initialization**, it is also **very slow** to compute on large datasets..

It is possible to avoid this speed/memory issue by **randomly smapling the dataset at each step**.
- Results are only slightly worse
- Speed and memory requirements make it usable on bigger datasets
- This approach is call "**Online K-Means**" or "**MiniBatch K-Means**"

## Application: Color quantization

![](https://i.imgur.com/acFEo2s.png)

## Many clustering techniques to play with !

![](https://i.imgur.com/GEU50Xd.png)

# Evaluation of clustering
## Need some supervision ?
By construction, clustering algorithms are optimal as they are expect to find some optimal balance between high intra-cluster similarity and low inter-cluster similarity, on their training set.

How do these internal criteria translate into good effectiveness for applications ?

A common approach is to rely on labeled data to compute new indicators:
- Purity: sort of "agreement" inside each cluster
- Normalized Mutual Information (NMI) and Entropu: information measures
- Rand Index (RI) and F measure: error counts

## Modern density estimation point of view
But what about if we leave some samples out for testing the generalization ?

HAC or K-Means "overfit" the underlying data distribution.

It does not alway make sense, but if we are interested in density estimation, then we can assess how well our model estimates the probability $P(x)$ of unseen data. The "E" step of the EM algo is based on this idea.

# Local feature detectors
## Introduction

> How are panorama pictures created from multiple pictures ?

![](https://i.imgur.com/gGQi6VP.png)

1. Detect small parts invariant under viewpoint change: "Keypoints" ![](https://i.imgur.com/pQK2QNY.png)
2. Find pairs of amthcing keypoints using a description of their neighborhood
3. Compute the most likely transformation to blend images together

## Some classical detectors
Edge (gradient detectors)
- Soble
- Canny

# Edge detectors
## What's an edge ?
- Image is a function
- Edges are rapid changes in thi function
- The derivative of a function exhibits the edges

![](https://i.imgur.com/zEYXFac.png)

![](https://i.imgur.com/bk8ZLcB.png)

<div class="alert alert-info" role="alert" markdown="1">
Gris = elevation comme dans le watershed
</div>

## Image derivatives

Recall:

![](https://i.imgur.com/GOiWeYU.png)

- We don't have an "actual" function, must estimate
- Possibility: set $h=1$
- Apply filter |-1|0|+1| to the image ($x$ gradient)

![](https://i.imgur.com/k3b1Jkz.png)

<div class="alert alert-success" role="alert" markdown="1">
We get terribly spiky results
</div>
We need to interpolate/smooth
- Gaussian filter

We get a sobel filter

![](https://i.imgur.com/rIHqWke.png)

![](https://i.imgur.com/VXGlNR0.png)

## Sobel filter

![](https://i.imgur.com/QYCNAO3.png)


## Gradient magnitude with Sobel

![](https://i.imgur.com/z3SOgYg.png)

## Canny edge detection
<div class="alert alert-info" role="alert" markdown="1">
Extract real lines !
</div>

### Non-maximum suppression

![](https://i.imgur.com/jA3uwmy.png)

![](https://i.imgur.com/B79XXLk.png)

![](https://i.imgur.com/B2BL2eX.png)

### Finalization

![](https://i.imgur.com/bGO4YCe.png)

# Corner detectors
## Good features

Good features are unique!
- Can find the "same" feature easily
- Not mistaken for "different" features

Good features are robust under perturbation
- Can detect them under translation, rotation
- Intensity shift
- Noise

## How can we find unique patches ?
Sky? Bad!
- Very little variation
Edge? OK
Corners? Good!

![](https://i.imgur.com/d2wxBTr.png)

## Self-difference

![](https://i.imgur.com/UFz6Eey.png)

![](https://i.imgur.com/7TeRwBZ.jpg)

![](https://i.imgur.comq2u4Sc.png)


## Harris corner detector
<div class="alert alert-info" role="alert" markdown="1">
Naive computation:

![](https://i.imgur.com/GuM7zyB.png)

![](https://i.imgur.com/ROWWgQv.png)

</div>

> Bon a partir de maintenant c'est que des screens parce que le prof trace

![](https://i.imgur.com/uPIIC8u.png)

![](https://i.imgur.com/Gs4gDUJ.png)

![](https://i.imgur.com/3sEA6um.png)

This allows us to "simplify" the original equation

![](https://i.imgur.com/HM1yPdt.png)

and more important making it **faster to compute**, thanks to simpler derivatives which can be **computed for the whole image**.

If we developp the equation and write it as usual matrix form, we get:
![](https://i.imgur.com/HfuTWn3.png)

where $A(x,y)$ is the structure tensor:

![](https://i.imgur.com/MPPJwRD.png)

This trick is useful because $I_x$ and $I_y$ can be computed very simply.

![](https://i.imgur.com/1mI6CEC.jpg)

![](https://i.imgur.com/23vb2Xg.png)

<div class="alert alert-danger" role="alert" markdown="1">
The need for **eigenvalues**
If the edge is rotated, so are the values of $I_x$ and $I_y$.
Eigenvalues give us the ellipsis axis lens.
</div>

![](https://i.imgur.com/K0lYoMy.png)

![](https://i.imgur.com/ZRsWaTA.png)

![](https://i.imgur.com/3tNu1L9.png)

### Summary

![](https://i.imgur.com/SSCDJz6.png)

![](https://i.imgur.com/Y6jAik7.png)
