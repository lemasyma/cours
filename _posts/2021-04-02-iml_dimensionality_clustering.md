---
title:          "IML: Unsupervised clustering"
date:           2021-04-02 13:00
categories:     [Image S8, IML]
tags:           [Image, SCIA, IML, S8, clustering]
description:    Unsupervised clustering
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/HJmN9d4Su)

# Why do we care 

<div class="alert alert-info" role="alert" markdown="1">
Group the input data into clusters that share some characteristics
</div>

- Find pattern in the data (data mining problem)
- Visualize the data in a simpler way
- Infer some properties of a given data point based on how it relates to other data point (satistical learning)

![](https://i.imgur.com/T01V0W4.png)

# Why is it tricky
Belongs to unsupervised learning
- No grounds truth available to learn/evaluate quality of the algorithm

![](https://i.imgur.com/1vBcxct.png)

How to assess how much data points are related to each other?
- Which criteria (features) are the most relevant
- Which metrics make the most sense

How to assess the soundness of the resulting cluster? Is it relevant ?
![](https://i.imgur.com/ojmJbwz.png)


# Families of clustering approaches

- **Distance-based clustering**
    - centroid-based approach (k-mean)
    - connectivity-based approaches (based on distance)
- **Density-based clustering**
    - set of dense points
- **Distribution-based clustering**
    - likelihood of point to belong to the same distribution
- **Fuzzy clustering**
    - Relaxed clustering paradigm where a data point can be assigned to multiple clusters with a quantified degree of belongingness metric (fuzzy $c$-means clustering,...).

# $k-$means clustering

Partition $n$ observations $x_1,...,x_n$ int $k$ clusters $C=\{C_1,...,C_k\}$ where each observations $x_i$ belongs to the cluster $C_{j*}$ whose mean $\mu_{j*}$ is the closest: $x_i\in S_{j*}$ with $j^*=argmin_j\Vert x_i-\mu_j \Vert_2$

![](https://i.imgur.com/JvfTtlf.png)

![](https://i.imgur.com/LVIwYHS.png)

La croix represente le centre, on veut la plus petite distance depuis un centre pour ajouter un point dans un cluster:
![](https://i.imgur.com/qrvcbBc.png)

- Minimize within-cluster sum of squares (variance)
- Overall optimization problem:


![](https://i.imgur.com/ZOvFM5r.png)
- NP-hard problem, no guarantee to find the optimal value
- Stochastic and very sensitive to initial conditions
- Sensitive to outliers (thank you $L_2$ norm)
- Probably the most used clustering algorithm

## $k-$means and Voronoi tesselation

<div class="alert alert-info" role="alert" markdown="1">
**Voronoi tesselation**
parition of the Euclidean space relatively to discrete points/seeds. Each region/Voronoi cell is composed of all the points in the space that are closer to the cell seed than any other seed

![](https://i.imgur.com/5xj4XVA.png)

</div>

- $k$-mean provides a way to obtain a Voronoi tesselation of the input space, where seeds are the final cluster means
- Alternatively, one case use some pre-computer Voronoi tesselation seeds as initial clusters for $k$-means

![](https://i.imgur.com/qtY0EkL.png)


## Determining the optimal number of cluster

Combien de clusters a vue de nez pour cette image ? ![](https://i.imgur.com/7c42CyF.png)

> 2, 3, 4, 14....

Compute explained variance for an increasing number of clusters $k$

![](https://i.imgur.com/THW7YRL.png)

<div class="alert alert-success" role="alert" markdown="1">
Plot and find the bend of the elbow

![](https://i.imgur.com/2GEZX4h.png)

</div>

<div class="alert alert-warning" role="alert" markdown="1">
Sometimes it does not work :( 

![](https://i.imgur.com/eelA1rX.png)

</div>

## Sometimes, $k$-means works...

But most of the time not as expected.

<div class="alert alert-warning" role="alert" markdown="1">
Probably because the $L_2$ norm that $k$-means tries to minimize
</div>

![](https://i.imgur.com/l8CifIm.png)

- Sensible of *curse of dimensionality*
- Form "normalized Gaussian" clusters
- Does not adapt to manifold geometry
- Sensible to class imbalance
- Sensible to outliers

## Simple Linear Iterative Clustering

> A kick-ass image segmentation algorithm using $k$-means

<div class="alert alert-info" role="alert" markdown="1">
SLIC superpixels uses a modified $k$-means clustering in the $Labxy$ space to produce $k$ clusters regurlaly sampled and perceptually coherent from a color point of view.
</div>

![](https://i.imgur.com/gpGsA50.png)

![](https://i.imgur.com/t4AZsqN.png)

![](https://i.imgur.com/TM6AfmQ.png)

## k-medoids clustering

> Possible extension to $k$-means

<div class="alert alert-warning" role="alert" markdown="1">
Cluster centroids are not initial data points $\Rightarrow$ can be problematic
</div>

$\Rightarrow$ Replace centroids by medoid (points with the smallest distance to all other points in the cluster)
![](https://i.imgur.com/JgMr7rx.png)

![](https://i.imgur.com/sgBbLcY.png)

$\Rightarrow$ $k$-medoid algorithm

Overall objective: find $k$ medoids $m_1, . . . , m_k$ that minimize the partitioning cost

![](https://i.imgur.com/9nQxiRq.png)
![](https://i.imgur.com/Zeasggl.png)


# Fuzzy $c$-means clustering

<div class="alert alert-warning" role="alert" markdown="1">
$k$-means is a **hard** clustering method: each data point 100% belongs to the cluster
</div>

<div class="alert alert-info" role="alert" markdown="1">
**Soft** clustering methods allow each data points to belong to several clusters with various degrees of membership
</div>

![](https://i.imgur.com/6LY1olR.png)

# Gaussian mixture models

> $k$-means on steroids

$k$-means works for spherical clusters, but fails in any other cases $\Rightarrow$ try harder Model probability density function $f$ of data as a mixture of multivariate Gaussian

![](https://i.imgur.com/L9AKAI7.png)

![](https://i.imgur.com/1wFKjes.png)
Cette courbe est une superposition de plusieurs Gaussiennes:
![](https://i.imgur.com/BQPOTaP.png)


![](https://i.imgur.com/agg6coo.png)

![](https://i.imgur.com/otkQSp3.png)

<div class="alert alert-danger" role="alert" markdown="1">
Il faut pouvoir estimer les facteurs de proportions de ces gaussiennes dans la somme
</div>

## The EM algorithm

### Initialization
- Select $k$ random points as initial means $\hat\mu_1,...,\hat\mu_k$
- Init all covariance matrices $\hat\sum_1,...,\hat\sum_k$ as whole data sample covariances matrix $\hat\sum$
- Set uniform mixture weight $\hat\phi_1,...,\hat\phi_k=\frac{1}{k}$

### Alternate until convergence

**Expectation step**
Compute membership weight $\hat\gamma_{ij}$ of $x_i$ with respect to $j^{th}$ component $\mathcal N(x\vert\mu_j,\sum_j)$

![](https://i.imgur.com/klkB7x8.png)

**Maximization step**
Update weights (in that ordre)

![](https://i.imgur.com/i59ad2z.png)

<div class="alert alert-success" role="alert" markdown="1">
Tadaaaa

![](https://i.imgur.com/fxyRwVS.png)

</div>

## $k$-means vs GMM

> Let the fight begin!

![](https://i.imgur.com/Z4GXU9M.png)

![](https://i.imgur.com/DypjLho.png)

# Kernel Density Estimation

> Nonparametric estimation

<div class="alert alert-info" role="alert" markdown="1">
**Goal**
Estimate probability density function $f$ based on observations $x_1,...,x_n$ only, assumed to derive from $f$ ~~otherwise wtf are we doing here~~

![](https://i.imgur.com/m6D3SSw.png)

</div>

The kernel density estimator with bandwith $h$ at given point $x$ is given by

![](https://i.imgur.com/fzYYYkY.png)

![](https://i.imgur.com/raArYI8.png)

## Exemples
![](https://i.imgur.com/YaZHrgS.png)


## Mean shift clustering

<div class="alert alert-info" role="alert" markdown="1">
shift each point to the the local density maximum of its KDE, and assign to the same cluster all points that lead to the same maximum

![](https://i.imgur.com/dfK2m9G.png)
![](https://i.imgur.com/I8GJKaQ.png)

</div>

### Exemples
![](https://i.imgur.com/kqlMnY4.png)

On peut faire la meme chose sur les images en couleurs:
![](https://i.imgur.com/k29t87Y.png)

# DBSCAN

> Density-base spatial clustering of applications with noise

- Divide points into 3 categories (core, boundary, outliers) whether there are at least $minPts$ in their $\epsilon$-neighborhood or not
- Find the connected component of core points (ignore all non-core points)
- Assign non-core points to nearby clusters if it is less than $\epsilon$ away, otherwise assign to noise

![](https://i.imgur.com/k5bta0x.png)

![](https://i.imgur.com/AbrcJDe.png)


# Spectral clustering

<div class="alert alert-info" role="alert" markdown="1">
View clustering task as a min-cut operation in a graph
</div>

![](https://i.imgur.com/Y4Kj0pb.png)

- Compute similarity graph (but which one?) of data $x_1,...,x_n$

![](https://i.imgur.com/S6F7mS5.png)

- Compute (weighted) adjacency matrix $W$, degree matrix $D$ and Laplacian matrix $L=D-W$
- Perform eigendecomposition of $L=(E,\triangle)$

<div class="alert alert-info" role="alert" markdown="1">
**Fact #1**
0 is and eigenvalue of $L$ with multiplicity $\sim\#$ connected components in graph, its eigenvectors are identity vectors of those connected components

![](https://i.imgur.com/VZycsNT.png)

</div>

<div class="alert alert-info" role="alert" markdown="1">
**Fact #2**
Eigenvector of smallest non-zero eigenvalue (Fiedler vector) gives the normalized min-cut of graph

![](https://i.imgur.com/TTP3aX6.png)

</div>

- Performs $k$-means clustering of the $k$ smallest eigenvectors $[e_1,...,e_k]_{n\times k}$

![](https://i.imgur.com/Cpn3550.png)


# Hierarchical clustering

> A very natural way of handling data

<div class="alert alert-info" role="alert" markdown="1">
**Goal**
Generate a sequence of nested clusters and ordre them in a hierarchy, represented by a dendogram
![](https://i.imgur.com/j8dnpgU.png)

</div>
- Leaves the dendogram = initial data
- Inner nodes of the dendogram = clusters

## Exemple
![](https://i.imgur.com/apVnKYK.png)

## Agglomerative vs Divise clustering

Agglomerative: merge clusters from fine to coarse (bottom-up approach)
![](https://i.imgur.com/VJunfOZ.png)

Divisive clustering: split clusters (top-down approach)
![](https://i.imgur.com/eypuhD0.png)

- Needs some heuristics to avoid the $O(2^n)$ ways of spitting each cluster...
- Not so used in practice

## Bestiarity
![](https://i.imgur.com/WKmG55N.png)



![](https://i.imgur.com/SnuNeX5.png)

# Overall comparison of all methods
![](https://i.imgur.com/C0N9moV.png)
