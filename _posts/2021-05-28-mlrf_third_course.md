---
title:          "MLRF: Lecture 03"
date:           2021-05-28 10:00
categories:     [Image S8, MLRF]
tags:           [Image, SCIA, MLRF, S8]
description: Lecture 03
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/H1imEm0Fd)

# Agenda for lecture 3
1. Introduction
2. Finish lecture about local feature **detectors**
3. Local feature descriptors
4. Descriptor matching and indexing
5. Projective transformations
6. Homography estimation

# A word about Divise clustering
HAC is *bottom-up*, divisive clustering is performed *top-down*

Classical approach:
1. Start with all data
2. Apply flat clustering
3. Recursively apply the approach on each cluster until some termination

Pros: can have more than 2 sub-trees

# Summary of last lecture

Global image descriptors
- Color histogram
- Limited descriptive power
- Which distance function ?

Clustering
- K-means
- Hierarchical Agglomerative Clustering

Local feature detectors
- Image gradients
- Edge detector: Sobel, Canny
- Corner detector: Harris
    - Large image gradient in 2 directions
- Corner detector: FAST
- Corner detectors: LoG, DoG, DoH
- Blob detector: MSER

# Nest practice sessions

**Compute and match descriptors** for max. 1 hour (from practice session 2)

![](https://i.imgur.com/ME4rRyL.png)

Play with **ORB keypoint mathcing** to implement a simple AR technique (practice session 3) 

![](https://i.imgur.com/tOqFPM7.png)

# Introduction

*How are panorama pcitures created from multiple pictures?*

![](https://i.imgur.com/VC2FHNU.png)

1. Detect small parts invariant under viewpoint change: **keypoints**
2. Find pairs of mathcing keypoints using a **description** of their neighborhood
3. Compute the **most likely transformation** to blend images together

![](https://i.imgur.com/M7npHSo.png)

# Local feature descriptors

## Harris & Stephen conclusion

Harris-Stephens trick to avoid computing eigenvalues:
![](https://i.imgur.com/FLWPRWd.png)

<div class="alert alert-danger" role="alert" markdown="1">
Nowadays linear algebra is cheap, so **compute the real eigenvalues**.
</div>

Thein filter using $\min(\lambda_1, \lambda_2)\gt\lambda$, $\lambda$ being a threshold

<div class="alert alert-success" role="alert" markdown="1">
This is the Shi-Tomasi variant
</div>

## Build your own edge/corner detector

We need the eigenvalues $\lambda_1$ and $\lambda_2$ of the structure tensor (hessian matrix with block-wise summing)

![](https://i.imgur.com/7GstOaW.png)


```python
dst = cv2.cornerEigenValsAndVecs(src, neighborhood_size, sobel_aperture)
dst = cv2.cornerMinEigenVal(src, neighborhood_size, sobel_aperture)
```

## Harris summary
### Pros
Translation invariant
- Large gradients in both directions = stable points

### Cons
Not so fast
- Avoid to compute all those derivatives
Not scale invariant
- Detect corners at different *scales*

# Corner detectors, binary tests FAST
## Features from accelerated segment test (FAST)
*Keypoint detector used by ORB*

<div class="alert alert-info" role="alert" markdown="1">
**Segment test**
Compare pixel $P$ intensity $I_p$ with surrounding pixels (circle of 16 pixels)
</div>

<div class="alert alert-success" role="alert" markdown="1">
If $n$ contiguous pixels are either:
- all darker than $I_p-t$
- all brighter than $I_p+t$

then $P$ is detected as a corner
</div>

![](https://i.imgur.com/Eu4B86L.png)


## Tricks
1. Cascading
    - If $n=12$ ($\frac{3}{4}$ of the circle) 
3. Machine learning
4. How to perform **non-maximal suppression**

## FAST summary
### Pros
Very fast
- 20 times faster than Harris
- 40 times faster than DoG

Very robust to transformations (perspective in particular)

### Cons
Very sensitive to blur

# Corner detectors at different scales LoG, DoG, DoH
## Laplacian of Gaussian (LoG)

> The theoretical, slow way

<div class="alert alert-info" role="alert" markdown="1">
**Band-pass filter**
It detects objects of a certain size
</div>

![](https://i.imgur.com/7GcefOa.png)

### Laplacian = second derivative

Like sobel with 1 more derivation

Taylor, again:

![](https://i.imgur.com/vy1GaMl.png)

New filter $I_{xx} = \begin{bmatrix}&1 &-2 &1\end{bmatrix} \times I$

![](https://i.imgur.com/BAlsMNI.png)

### Laplacian filter $\nabla^2I(x,y)$

Edge detector, like Sobel but with second derivatives

![](https://i.imgur.com/6Yho5sq.png)

### Laplacian **of Gaussian**

> mexican hat

![](https://i.imgur.com/yZ1Bi2w.png)

### LoG = detector of circular shapes
<div class="alert alert-success" role="alert" markdown="1">
Detector of circular shapes:
</div>

![](https://i.imgur.com/UXh0ZNU.png)

LoG filter extrema locates "blobs"
- maxima = dark blobs on light background
- minima = light blobs on dark background

### Detecting corners/blobs

Build a scale space representation: *stack of images (3D) with increasing $\sigma$*

![](https://i.imgur.com/ZgwHcUl.png)

## Difference of Gaussian (DoG)

Fast approximation of LoG (Used by SIFT)

<div class="alert alert-info" role="alert" markdown="1">
LoG can be approximate by a Difference of 2 Gaussians (DoG) at different scales

![](https://i.imgur.com/WTrNA1i.png)

</div>

### DoG filter

It is a band-pass filter

![](https://i.imgur.com/xiqeck7.png)

![](https://i.imgur.com/gxogNF1.png)

> L'idee est : "est-ce que mes bosses sont comprises entre telles ou telles longueurs d'onde"

### DoG filter

Intuition
- Gaussian (g) is a low pass filter

![](https://i.imgur.com/oOaZRnt.png)

### DoG computation in practice

Take an image

![](https://i.imgur.com/zU0jFr7.png)

Blur it

![](https://i.imgur.com/PNSUndv.png)

Take the difference

![](https://i.imgur.com/sm39Q0d.png)


### DoG scale generation trick

<div class="alert alert-info" role="alert" markdown="1">
DoG computation use "octaves"
</div>
- "Octave" because frequency doubles/halves between octaves
- If $\sigma=\sqrt{2}$, then $3$ levels per octave
- Downsample images for next octave (like double sized kernel)
- Compute the DoG between images

![](https://i.imgur.com/Lx4twSa.png)

### DoG: Corner selection

<div class="alert alert-info" role="alert" markdown="1">
Throw out weak responses and edges
</div>

Estimate gradients
- Similar to harris, look at nearby responses
- Not whole image, only a few points! faster
- Throw out weak responses

Find cornery things
- Same deal, structure matrix, use dete and trace info (SIFT variant)

![](https://i.imgur.com/qUZfnNO.png)

## Determination of Hessian (DoH)

<div class="alert alert-info" role="alert" markdown="1">
Faster approximation
</div>

![](https://i.imgur.com/lNt6Chu.png)

![](https://i.imgur.comtMSuUG.png)

## LoG vs DoG vs DoH

![](https://i.imgur.com/sxQR6D6.jpg)

<div class="alert alert-success" role="alert" markdown="1">
On prefere un "Laplacian of Gaussian" pour detecter les petites etoiles
</div>

## LoG, DoG DoH summary
### Pros
Very robust to transformations
- Perspective
- Blur

Adjustable size detector

### Cons
Slow

# Blob detectors MSER
## Maximally Stable Extremal Regions (MSER)

> Detects regions which are stable over thresholds 

1. Create min & max-tree of the image
    - Tree of included components when thresholdinf the image ar each possible level 
    - ![](https://i.imgur.com/Nbj8pYi.png) 
    - ![](https://i.imgur.com/7kQ4564.png)
        - Le cerveau a une tumeur
2. Select most stable regions
    - between $t-\triangle$ and $t+\triangle$ 
    - $R_{t\*}$ is maximally stable iif $q(t)=\vert R_{t-\triangle}\text{\ } R_{t+\triangle}\vert/\vert R_t\vert$ as local minimum at $t^{\*}$
    - ![](https://i.imgur.com/EhzBlrT.png)


### Summary
#### Pros
Very robust to transformations
- Affine transformations
- Intensity changes

Quite fast

#### Cons
Does not support blur

# Local fetaure detectors: Conclusion
- Harris Stephens: can be very stable when combined with DoG
- Shi-Tomasi: Assumes affine transformation (avoid it with perspective)
- DoG: slow but very robust (perspective, blur, illumination)
- DoH: faster than DoG, misses small elements, better with perspective
- FAST: very fast, robust to perspective change (like DoG), but blur quickly kills it
- MSER: fast, very stable, good choice when no blur

![](https://i.imgur.com/AYG4TCS.png)

# Introduction
> Given som keypoints in image 1, what are the more similar ones in image 2 ?


![](https://i.imgur.com/9FCjhYP.png)

<div class="alert alert-info" role="alert" markdown="1">
This is a **nearest neighbor problem** in **descriptor space**
</div>
<div class="alert alert-warning" role="alert" markdown="1">
This is also a **geometrical problem** in **coordinate space**
</div>

# Matching
## Matching problem

<div class="alert alert-danger" role="alert" markdown="1">
Goal: given 2 sets of descriptors, find the best matching pairs
</div>

Need a **distanceorm**: depends on the descriptor
- Distribution (histogram)? Stats?
- Data type ?
    - Float, integers: Euclidean, cosine
    - Binary: Hamming

## 1-way matching

<div class="alert alert-info" role="alert" markdown="1">
For each $x_i$ in the set of descriptors $D_1$, find the closest element $y_i$ in $D_2$
</div>

![](https://i.imgur.com/JIOYVVN.png)

![](https://i.imgur.com/cX90LS3.png)

<div class="alert alert-success" role="alert" markdown="1">
We have a match $m(x_i, y_i)$ for each $x_i$
</div>

![](https://i.imgur.com/Lb6FbId.png)

## Symmetry test aka cross check aka 2-way matching

<div class="alert alert-info" role="alert" markdown="1">
For each $x_i$ in the set of descriptor $D_1$, find the closest element $y_i$ in $D_2$ such as $x_i$ is **also the closest** element to $y_i$
</div>

![](https://i.imgur.com/oSkRfIu.png)


![](https://i.imgur.com/mXPJRmi.png)

## Ratio test
<div class="alert alert-info" role="alert" markdown="1">
For each $x_i$ in $D_1$, find the 2 closest elements $y_i$ and $y_j$ in $D_2$ 
</div>

![](https://i.imgur.com/sSGDA3q.png)

### Calibrate the ratio

<div class="alert alert-warning" role="alert" markdown="1">
Adjust it on a training set !
</div>

For each correct/incorrect match in your annotated database, plot the *next to next closest distance* PDF.

**What is a good ratio in D. Lowe's experiment ?**
![](https://i.imgur.com/heyBGn6.png)

## Geometric validation

![](https://i.imgur.com/HWSJlMr.png)

## Summary

![](https://i.imgur.com/emb2LW0.jpg)


# Indexing
## Indexing pipeline

Use case: We have a database of images and we want to find an object from it

![](https://i.imgur.com/IT7nvU1.png)

## Bruteforce matching aka linear matching

<div class="alert alert-info" role="alert" markdown="1">
Simply scan all data and keep the closest elements
</div>

Does not scale to large databases, but can be faster on small ones

## kD-Trees

> binary tree in which every leaf node is a k-dimensional point

## FLANN - Efficient indexing

- Original version: hierarchical k-means
- Construction: repetitive k-means on data (then inside clusters) until minimum cluster size is reached
- Lookup: traverse the tree in a best-bin-first manner with backtrack queue, backtrack until enough point are returned

## Locally Sensitive Hasing (LSH)

<div class="alert alert-info" role="alert" markdown="1">
Hash items using family of hash function which project similar items in the same bucket with high probability
</div>

<div class="alert alert-danger" role="alert" markdown="1">
Not cryptographic hashing !
</div>

![](https://i.imgur.com/8pNSTNa.png)

![](https://i.imgur.com/34UbaCg.png)

En fonction de quel cote notre separatrice se trouve par rapport au point, on met notre bit a 1 ou 0

![](https://i.imgur.com/y91ZzFV.png)

![](https://i.imgur.com/olHjq6h.png)

<div class="alert alert-success" role="alert" markdown="1">
Approximation de la distance $\cos$ en binaire
</div>

![](https://i.imgur.com/KBfg4xN.png)

## Locality Sensitive Hashing (LSH)
- Fast and efficient with large spaces and lot of data
- Return a "good match", maybe not the best one
- kNN can be costly

## Which indexing ?

<div class="alert alert-success" role="alert" markdown="1">
Experiment
</div>

Advices for practice session:
![](https://i.imgur.com/6RI3g9V.png)


![](https://i.imgur.com/pWfbArP.png)

# Projective transformations
## A linear transformation of pixel coordinates

![](https://i.imgur.com/MuVLu6J.png)

## Image Mappings Overview

![](https://i.imgur.com/l0bhIFj.png)

## Math. foundations & assumptions

![](https://i.imgur.com/pRtFCWX.png)

- For planar surfaces, 3D to 2D perspectives projection reduces to a 2D to a 2D transformation
- This is just a change of coordinate system
- This transformation is **invertible**

## Translation

![](https://i.imgur.com/hsauJ6A.png)

## Scale

![](https://i.imgur.com/FdafdCS.png)


## Rotation

![](https://i.imgur.com/2gPwaoN.png)

### Notation: Partitioned matrices

![](https://i.imgur.com/CvxLHJd.png)

## Affine

![](https://i.imgur.com/JDWlKoO.png)

## Projective

![](https://i.imgur.com/JQVbpnZ.png)


## More on projective transform
- Each point in 2D is actually a vector in 3D
- Equivalent up to scaling factor
- Have to normalize to get back to 2D
- Using homogrpahy to project point
- Multiply $\tilde x$ by $\tilde H$

## Summary

![](https://i.imgur.com/HXJQHTn.png)

# Homography estimation, Geometric validation

## We want to recover H from keypoint matches

![](https://i.imgur.com/L1sAs1F.png)

## Recover the parameters of a perspective transform

![](https://i.imgur.com/QOPhp1a.png)

## How many correspondences are needed ?

Depends on the type of transform:
- How many for translation ?
- For rotation ?
- ...
- For general projective transform ?

<div class="alert alert-danger" role="alert" markdown="1">
Reminded: we have 2 knowns for each match
</div>

![](https://i.imgur.com/qrJNg89.png)

### Linear system

![](https://i.imgur.com/AdWjP58.png)

### Use Linear Least Square to solve $Ma=b$

![](https://i.imgur.com/7ZwlwZW.png)

### Solve the system
![](https://i.imgur.com/GFEOQIZ.png)

## How reliable is the estimate ?

![](https://i.imgur.com/NJJYp3J.png)

### Even worse

![](https://i.imgur.com/Lkqj3Hh.png)


## Is our data perfect ?

![](https://i.imgur.com/BSPY6Jy.jpg)

On a pas mal de bruit

## Overcoming Least Square Limitations
- We need a **robust estimation**

### RANSAC: RANdom SAmple Consensus

![](https://i.imgur.com/DG1ja8H.png)

![](https://i.imgur.com/UvDoR08.png)

#### Algorithm

![](https://i.imgur.com/TDS9vMN.png)

![](https://i.imgur.com/cfc8vdt.png)

## RANSAC works well with extreme noises

![](https://i.imgur.com/LWMNKmj.jpg)
