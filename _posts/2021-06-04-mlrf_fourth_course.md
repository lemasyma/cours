---
title:          "MLRF: Lecture 04"
date:           2021-06-04 10:00
categories:     [Image S8, MLRF]
tags:           [Image, SCIA, MLRF, S8]
description: Lecture 04
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/BJj638vqd)

# Agenda for lecture 4

1. Introduction
2. Content-based image retrievalasl (CBIR) using bags of features
3. Evaluating CBIR / Ranked Retrieval (RR) systems
4. Texture descriptors
5. Character descriptors

# Summary of last lecture

- Descriptor matching
    - 1-way
    - Cross check
    - Ratio test
    - Radius threshold
- Descriptor indexing
    - Indexing pipeline: train/query
    - Linear matching
    - kD-Trees
    - FLANN/hierarchical k-Means
    - LSH
    - Aproximate NN problem
- Projective transformations
    - Translation
    - Rotation
    - Scaling
    - ...
    - Projective
- Homography estimation
    - Least square
    - RANSAC
- Geometric validation

# Practice session 3: Take home messages
*Twin it!*: Extracting descriptors, matching them **by hand**
- Detect keypoints and extract surrounding pixels to flat vector
- Normalize them and compare them using cross correlation ($\sum_if_i\bullet g_i$)

Augmented Documents: Use an off-the-shelf detector/descriptor: ORB

Augmented Documents: Projective transforms and Homography estimation
- OpenCV provides the solver for machinery: list of matches $to$ $3\times 3$ matrix
- Just som coordinate transform (2D $\to$ 2D transform)
- Remember the classical matrix forms: **translation, rotation, ...**

# Next practice session

<div class="alert alert-success" role="alert" markdown="1">
Implement a simple **image search engine**
</div>

![](https://i.imgur.com/uwclkII.png)

<div class="alert alert-danger" role="alert" markdown="1">
Will be graded
</div>

# Local feature descriptors

## Introduction
*Given some keypoints in image 1, what are the more similar ones in image 2 ?*

![](https://i.imgur.com/vDMNGYF.png)

<div class="alert alert-info" role="alert" markdown="1">
This is a **nearest neighbor problem** in **descriptor space**
This is also a **geometrical problem** in **coordinate space**
</div>

<div class="alert alert-success" role="alert" markdown="1">
Local feature **detectors** give use the same feature under several perturbations: perspective, illumination, blur...
</div>

Local feature descriptors will associate a **vector to each local feature**.

Such description vector should be:
- **Compact** - to enable fast indexing and matching
- **Discriminative** - to enable object recognition
- **Robust to perturbations** - to tolerate real conditions

We will focus on 2 widely used descriptors for their pedagogical interest
- **HOG** (Histogram of gradients), used im SIFT
- **BRIEF** (Binary Robust Independent Elementary Features), used in ORB

# Histogram of Gradient
## Algorithm overview

1. (optional) global image normalization
2. Compute the gradient image in $x$ and $y$
3. Compute gradient hisograms
4. Normalise across blocks
5. Flatten into a feature vector
6. (quantify to integers)

![](https://i.imgur.com/zACmsUy.png)

![](https://i.imgur.com/xSKmwma.png)

## Exemple

![](https://i.imgur.com/vQ4mY5v.png)
> Cette sensation quand tu cogne ton coude au niveau du nerf

## Summary
### Pros
- Very stable over illuminations changes perpectives changes, blur

### Cons
- Slow to compute
- Quite large (128 bytes for original SIFT)

# BRIEF

General idea:
1. Sample pairs of points $$\{p(x), p(y)\}$$ in the **smoothed** (very spiky otherwise, like derivatives) keypoints neighborhood
2. Compute a simple **binary test**: $p(x)\lt p(y)$
3. Accumulate the results of $n_d$ tests to form a **binary vector of $n_d$ bits** (256 in ref.)

![](https://i.imgur.com/1SDVx4U.png)

## Sampling strategies

- GI: $(x_i, y_i)\sim$ i.i.d. Uniform($-\frac{S}{2}$, $+\frac{S}{2}$)
- GII: $(x_i, y_i)\sim$ i.i.d. Gaussian($0$, $\frac{1}{25}S^2$)
- GII:
    - $x_i\sim$ i.i.d. Gaussian($0$, $\frac{1}{25}S^2$)
    - $y_i\sim$ i.i.d. Gaussian($x_i$, $\frac{1}{100}S^2$)
- GIV: $(x_i, y_i)$ randomly sampled from discrete locations of a coarse polar grid introducing a spatial quantization
- GV: 
    - $x_i=(0,0)$
    - $y_i$ takes all possible values on a coarse polar grid containing $n_d$ points

![](https://i.imgur.com/AXKYqZM.png)
TODO

**What is the best approach ?**

<div class="alert alert-success" role="alert" markdown="1">
C'est la strategie 2
</div>

![](https://i.imgur.com/llHURZA.png)


![](https://i.imgur.com/MBS2vD7.png)

## Summary
### Pros
- Very fast to compute
- Very fast to match
- Very compact to store
### Cons
- Less robust than HoG(SIFT), DoH(SURF) on several real cases

# Invariance check
## Rotation invariance
- Add an angle measure
- Take the main gradient orientation 
    - (Take the averga around the keypoints)

We now have for each keypoint:
- Coordinates
- **Orientation**

Descriptor: computed over **normalized patch**

![](https://i.imgur.com/zBuVgaq.png)

## Scale invariance
Multi scale feature detection and computation:
- Add a keypoint for each relevant scale
- Possibly several keypoints at the same position

We now have for each keypoint:
- Coordinates
- Orientation
- **Scale**

Descriptor: computed on a **scaled patch**

![](https://i.imgur.com/yMyMl4u.png)


### Reminder: Gaussian sigma vs window size

![](https://i.imgur.com/tXEAYNh.png)

## Illumation invariance
SIFT approach:
1. Normalize the vector
    - Solves Affine but what non-linear sources like camera saturation?
    - ![](https://i.imgur.com/SIti7h8.png)
2. Cap the vector elements to $20\%$ (!) and renormalize
    - Now we have some illumination invariance
    - ![](https://i.imgur.com/NJb8ayu.png)

## Viewpoint invariance

Better, but more complex approaches can tolerate extreme viewpoint change

![](https://i.imgur.com/AM7wRyG.png)

# Complete pipelines
## SIFT (Scale invariant feature tr.)
1. Construct scale space
2. Take difference of Gaussians
3. Locate DoG Extrema
4. Sub pixel locate potential feature points
5. Filter edge and low contrast responses
6. Assigne keypoints orientations
7. Build keypoint descriptors
8. Matching, etc.

![](https://i.imgur.com/ULWDf5s.png)

## ORB (oriented FAST and rotated BRIEF)
1. Use FAST in pyramids to detect stable keypoints
2. Select the strongest features using FAST or Harris response
3. Finds their orientation using first-order moments
4. Computes the descriptors using BRIEF
    - Where the coordinates of random point pairs are rotated according to the measured orientation

# Conclusion about feature extraction
Selection of appropriate features:
- It is a **critical** decision
- Depends on the **specific application**

Features must:
- Be **invariant** to data variations (depending on the application)
    - rotation
    - perpective
    - noise
    - etc.
- Have **low dimensionality** for fast training, matching, reasonable storage

Features determine the **type of info** to work with:
- gray-level, binary, color image
- contours, vectorization, skeleton

Features also determine the **type of classifier / indexer**

# Content based image retrieval
## Two strategies using local descriptors
### Keep all local descriptors
Pros:
- Enables geometric validation
- better part detection in theory

Cons:
- Huge memory requirements

<div class="alert alert-success" role="alert" markdown="1">
Like what we did in practice session 3 to match parts of an image (useful to validate geometric constraints and classify an image at the same time)
</div>

### Build a global descriptor using local ones
- Inspired by text retrieval
- Compact representation
- Tricks to embed spatial information
- Limited memory requirements

<div class="alert alert-success" role="alert" markdown="1">
Like what we did in practice session 2 with the color histogram, at the bubble level
</div>

<div class="alert alert-info" role="alert" markdown="1">
**Bag of Feature** approach
</div>

## Pipeline with local descriptors (prev. lecture)

![](https://i.imgur.com/kCXVXCa.png)

## Pipeline with bag of features (current lecture)

![](https://i.imgur.comJqjwCc.png)

# Features extraction
## Sparse vs Dense detection

![](https://i.imgur.com/vvZpbRA.png)

![](https://i.imgur.com/9ksurAN.png)

<div class="alert alert-info" role="alert" markdown="1">
For dense detection, we usually filter regions with low variance
</div>

![](https://i.imgur.com/ww37BoR.jpg)

## Dimensionality reduction
Often used before encoding to:
- limit dictionary sizes
- facilitate quantization

Several techniques:
- Principal Component Analysis
- Signualr-Value Decomposition

![](https://i.imgur.com/hk6hNrO.png)

# Encoding
## Bag of Visual Words

- Modern approaches are derived from this one
- Reuses ideas of text/we search to images
- **From a set of descriptor, build a histogram of quantized descriptors** much alike a color histogram

## Quantization
- Discretization of some signal - **Lossy process!**
- Vectorial formulation: $f:R^d\to F$, with $F=\{1,2,...,k\}$
- Defines a **Voronoi diagram**, ie a decomposition of a metric space determined by the distances to a discrete set of points

![](https://i.imgur.com/MwrAUQh.png)

## Bag of Visual Words (continued)
- Cluster centers are determined using k-Means (once for all on a training set)
- Each descriptor is quantized: store the code of the closest centroid
- Build a histogram of descriptor count for each cluster

<div class="alert alert-info" role="alert" markdown="1">
The set of cluster centers is called the dictionary, the codebook or also the visual vocabulary
</div>

<div class="alert alert-warning" role="alert" markdown="1">
We can choose the number of words !
</div>

![](https://i.imgur.com/RGjy5BK.png)

![](https://i.imgur.com/RJUhOE7.png)

![](https://i.imgur.com/f1QlwOv.png)

### Vector size
The resulting vector size for a given image is given by:

$$
D=\text{vocabulary size}
$$

Usually, the bigger the vocabulary the better the results.
Several thousands of words are common.

### Normalization

#### Premiere methode
Problem:
- The values in the histogram are **absolute**: each bin count the number of occurence of each *visual word*
- This make the descriptor **sensitive to the variation of number of descriptors**

Solution:
- Normalize the histogram

#### Seconde technique
- Like for text retrieval, it is common to **reweight the BOVW vectors** using the **TFDIF** technique
- Goal: give more importance to rare words than to frequent ones
- For each dimension of the histogram, compute a new value $t_i$

![](https://i.imgur.com/URzKx5n.png)

## Variant: Soft BoVW

Use soft assignment to clusters, add counts to neighbor bins
 
![](https://i.imgur.com/a4WbGkI.png)

## Other variants
BoVW is only about counting the number of local descriptors

## VLAD: vector of locally aggregated descriptors

![](https://i.imgur.com/fClfKFr.png)

![](https://i.imgur.com/Sr75DHs.jpg)

## Fisher vector

![](https://i.imgur.com/cMgDD7Y.png)

# IR evalutation
## How to evaluate a retrieval system ?
We need a set of queries for which we know the expected results "Ground truth", aka "targets", "gold standard"

## Precision and recall
Used to measure the balance between
- Returning many results, hence a lot of the relevant results present in the database, but also a lot of noise
- Returning very few results, leading to less noise, but also less relevant results

<div class="alert alert-info" role="alert" markdown="1">
Precision ( P ) is the fraction of retrieved documents that are relevant:

![](https://i.imgur.com/IhJjsv6.png)
</div>


<div class="alert alert-info" role="alert" markdown="1">
Recall ( R ) is the fraction of relevant documents that are retrieved

![](https://i.imgur.com/r1Czp0V.png)
</div>

![](https://i.imgur.com/8isRfsq.png)

## F-measure

<div class="alert alert-info" role="alert" markdown="1">
F-measure is the wighted harmonic mean of precision and recall
![](https://i.imgur.com/haBncXm.png)
</div>


## How to evaluate a **ranked** retrieval system ?
When results are ordered, more measures are availables.

Common useful measure are:
- Precision-recall
- ROC graph nd the area under it (AUC)

### Precision-recall graph

![](https://i.imgur.com/kHO9icg.png)

#### Mean-average precision 

![](https://i.imgur.com/v9hTxL6.png)

#### Example: Compute the AP for a given query

For this query and the followinf results, plot the precision/recall graph

![](https://i.imgur.com/XHvHYC9.png)

<div class="alert alert-success" role="alert" markdown="1">
1, 3 et 9 sont pertinents ici
</div>

![](https://i.imgur.com/rpHF2Lx.png)

![](https://i.imgur.com/I13Ey9Q.png)

*Is the first result relevant ?*
Oui
- compute current precision: 1 relevant / 1 retrieved = 1
- Recall: 1 relevant

Repeter pour chaque resultat

![](https://i.imgur.com/cSj8Sl2.png)

<div class="alert alert-danger" role="alert" markdown="1">
Construction du graphe en dent de scie
</div>

![](https://i.imgur.com/Qy0tjaT.png)

<div class="alert alert-warning" role="alert" markdown="1">
Certaines librairies garde les valeurs superieures, **c'est pas bien**
</div>

Case 2: what if $\vert e_i\vert=4$ ?

![](https://i.imgur.com/aRmeh6t.png)

<div class="alert alert-danger" role="alert" markdown="1">
Ce qu'on veut c'est l'aire sous la courbe
</div>