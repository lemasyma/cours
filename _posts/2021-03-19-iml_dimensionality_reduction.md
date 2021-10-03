---
title:          "IML: Dimensionality reduction"
date:           2021-03-19 13:00
categories:     [Image S8, IML]
tags:           [Image, SCIA, IML, S8, principal component analysis]
math: true
description:    Dimensionality reduction
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/H1ZhGffNO)

# Why do we care ?
We have at hand $n$ points $x1,..., xn$ lying in some N-dimensional space, $x_i \in\mathbb R^n , \forall i = 1, . . . , n,$ compactly written as a $n × N$ matrix $X$
- One row of $X$ = one sample
- One column of $X$ = a given feature value for all samples

![](https://i.imgur.com/CmbXcfy.png)

## Example of real high-dimensional data
<div class="alert alert-warning" role="alert" markdown="1">
Real world data is very often high-dimensional
</div>

### MNIST image classification:

![](https://i.imgur.com/psXUjPa.png)

- Sample $x$:image with 28x28 pixels
- Data set: 60000 samples
- Dimensionality: $x \in\mathbb R^{28×28=784}$

### MUSE hyperspectral image analysis:

![](https://i.imgur.com/afKNwIT.png)

- Sample $x$: pixel with 3600 spectral bands
- Data set: image with 300x300 pixels
- Dimensionality: $x \in \mathbb R^{3600}$

> Pour discriminer les galaxies ~~c'est raciste ca monsieur~~

## The curse of dimensionality
<div class="alert alert-danger" role="alert" markdown="1">
High-dimensional spaces ~~suck donkey ballz~~ suffer from the *curse of dimensionality* (also called Hughes’ phenomenon)
</div>

### Sur $\mathbb R$
![](https://i.imgur.com/vesSPAR.png)

![](https://i.imgur.com/D1xI2ST.png)

### Sur $\mathbb R^2$
Revenir a la meme densite d'echantillonage:
![](https://i.imgur.com/jRNkOX5.png)

### Sur $\mathbb R^3$
![](https://i.imgur.com/7rK9gAn.png)

Revenir a la meme densite d'echantillonage:
![](https://i.imgur.com/PUKy7sm.png)

$$
\frac{\nu(\mathbb S^n)}{\nu([-1;1]^n)}=\frac{\pi^{\frac{n}{2}}}{2\Gamma(\frac{n}{2}+1)}\to_{n\to+\infty}0
$$

<div class="alert alert-warning" role="alert" markdown="1">
Points uniformly distributed in a $n$−cube of side 2 mostly fall outside of the unit sphere!

![](https://i.imgur.com/rh4aYb4.png)
</div>

# Why is it tricky?
- We naturally cannot picture anything that is more than 3D in our mind

![](https://i.imgur.com/JLWfSrR.png)
- Picturing something 3D in a 2D flat screen can already be misleading
- Real data naturally lives in (complex) high-dimensional space
- Real data is often strongly correlated

<div class="alert alert-warning" role="alert" markdown="1">
And somehow, we want to have a good look to our data before feeding it to some machine learning algorithm *(can I use the inherent structure of my data to pimp my machine learning performances?)*
</div>

# How ?
<div class="alert alert-info" role="alert" markdown="1">
Dimensionality reduction: transform data set $X$ with dimensionality $N$ into a new data set $Y$ ($n \times M$ matrix) with dimensionality $M \lt N$ (hopefully $M \lt\le N$) such that as **few information as possible is lost** in the process. 
$y_i$ ($i$th row of $Y$) is the low-dimensional counterpart *(the projection)* of $x_i$.
</div>

**INFORMATION ???**

![](https://i.imgur.com/OYfsA0d.png)

# Linear approaches
Somehow trying to find a low-dimensional subspace in which the projected data would not be too much distorted after projection.
- Johnson-Lindenstrauss lemma
- Classical scaling
- *(The one and only)* Principal Component Analysis
- And much more...

![](https://i.imgur.com/dugYCAS.png)

## Johnson-Lindenstrauss lemma
It’s not because you *can* that you *will*

<div class="alert alert-danger" role="alert" markdown="1">
Let $0\lt\varepsilon\lt1$ and let $x_1,...,x_n$ be $n$ points in $\mathbb R^N$. Then there exists a linear map $f:\mathbb R^N\to\mathbb R^M$ such that for every points $x_i$ and $x_j$

$$
(1-\varepsilon)\Vert x_i-x_j \Vert^2\le \Vert f(x_i)-f(x_j) \Vert^2\le(1+\varepsilon)\Vert x_i-x_j \Vert^2
$$

With $M=\frac{4\log(n)}{(\frac{\varepsilon^2}{2} − \frac{\varepsilon^3}{3}).}$

> Johnson, W. B., & Lindenstrauss, J. (1984). Extensions of Lipschitz mappings into a Hilbert space. Contemporary mathematics.
</div>

![](https://i.imgur.com/w1g2pBu.png)


<div class="alert alert-warning" role="alert" markdown="1">
La douille: il faut trouver la matrice $M$.
</div>

## Classical scaling
Also called Principal Coordinates Analysis (PCoA)

> Lots of formula here, but you just need to retain the overall idea

<div class="alert alert-danger" role="alert" markdown="1">
PCoA: project data points $X$ onto $Y$ with a linear mapping $M$ such that $Y = XM$ such that all pairwise distances between points do not change too much before/after projection
</div>

If $D$ is the $n \times n$ Euclidean distance matrix with entries $d_{ij} = \Vert x_i − xj\Vert_2$ and $D^{(2)} = [d_{ij}^2]$, PCoA seeks the linear mapping $M$ that minimizes

$$
\phi(Y)=\sum_{i,j}(d_{ij}^2-\Vert y_i-y_j\Vert^2)
$$

with $y_i = x_iM$ and $\Vert m_i\Vert^2=1\forall i$

<div class="alert alert-success" role="alert" markdown="1">
Solution: eigendecomposition (=diagonalisation) of the Gram matrix $K = XX^T = E\Delta E$
</div>

$K$ can be obtained by double centering $D^{(2)}:K=-\frac{1}{2}C_nD^{(2)}C_n$  with centering matrix $C_n=I_n-\frac{1}{n}ones(n,n)$

Optimal projection onto the first $M$ dimensions $Y=\Delta_M^{\frac{1}{2}}E_M^T$ with $E_M$  matrix of the $M$ largest eigenvectors of $E$.

## Principal component analysis
> Also known as the Karhunen-Loeve transform

Closely related to PCoA, but operates on the covariance matrix $X_c^T X_c$ PCA seeks the linear mapping $M$ that maximizes the projection variance $tr(M^T cov(X)M)$ with $\Vert mi\Vert^2 = 1 \forall i$.

$$
X=\begin{bmatrix}
\overbrace{x_{11}}^{u_1=\text{moyenne}} & \overbrace{x_{12}}^{u_2}\\
\vdots & \vdots\\
x_{n1}&x_{n2}
\end{bmatrix} \Rightarrow \text{centrage des donnees}
$$

$$
X_c=\begin{bmatrix}
x_{11}-u_1 & x_{12}-u_2\\
\vdots & \vdots\\
x_{n1}1-u_1&x_{n2}-u_2
\end{bmatrix}
$$

1. Center the data $X_c = C_nX$
    1.b (opt) Reduce the data
2. Compute covariance matrix $\sum=\frac{1}{n-1}X_c^TX_c$
3. Perform eigendecomposition $(E,\Delta)$ of $\sum$
4. Project on the first $M$ principal axes $Y=XE_M$

![](https://i.imgur.com/WJcHD4e.png)

![](https://i.imgur.com/Kw4ZzPC.png)


Data after projection is uncorrelated, but has
lost some interpretability

![](https://i.imgur.com/93SANtL.png)

## Major challenges related to PCA
PCA is probably the most popular and used unsupervised linear dimensionality reduction technique, but it comes with a bunch of operability questions, the 2 principles being:
1. How to automatically select the right number of dimensions to project?
    - ![](https://i.imgur.com/EmehUrr.png) ![](https://i.imgur.com/2Kgc8Gj.png)
2. How to project a new data point on a learned projection subspace?
    - See you in lab session for the answer

# Non-linear approaches
When it is assumed that the data does not live
in an Euclidean subspace (why would it anyway?),
some more advanced techniques must be relied
on.
- Isomap
- Locally linear embedding
- Kernel Principal Component Analysis (aka PCA on steroids)
- Multilayer autoencoders
- And much more... 

![](https://i.imgur.com/EEegGRS.png)

![](https://i.imgur.com/r8hJK6Z.png)

## Isomap
> Geodesic distance rocks

Isometric feature mapping: same idea as classical scaling, but using geodesic distance instead of Euclidean distance.

![](https://i.imgur.com/OlSpeIx.png)
![](https://i.imgur.com/fBSAufM.png)


1. Compute k-nearest neighbor graph of data $x_1,...,x_n$
2. Compute all pairwise geodesic distances
3. Apply classical scaling

![](https://i.imgur.com/qc77r5y.png)

### Exemple 
Isomap applied to some images of the digit 2 in MNIST data

![](https://i.imgur.com/4wnzodY.png)

## Locally linear embedding

Locally linear embedding: the manifold can be locally considered Euclidean

![](https://i.imgur.com/cz5QFIk.png)

For each point $x_i$:
1. get its k-nearest neighbors $x_j$, $j=1,...,k$
2. Get weights $w_{ij}$ that best linearly reconstruct $x_i$ with $x_j$: minimize $\sum_{i=1}^n\Vert x_i-\sum w_{ij}x_j\Vert$ ![](https://i.imgur.com/9r9RLAB.png)
    - with constraints $\sum w_{ij}=1$ (closed-form solution)
4.  Low-dimensional embedding $\to$ reconstruct $y_i$ with $y_j$ and same weights $w_{ij}$:

minimize 
$$
\sum_{i=1}^n\Vert y_i-\sum w_{ij}y_j\Vert
$$

with constraints $\frac{1}{n}\sum_iy_iy_i^T$ and $\sum_iy_i=0$ (eigendecomposition of a Gram matrix)

## The kernel trick

> When one actually wants to increase the dimension

Base idea: map $n$ non linearly separable points to a (possibly infinite) space where they would be with a function $\phi$

- How should we define $\phi$ ?
- Do we really want to compute stuff in a (possibly infinite) feature space?

<div class="alert alert-info" role="alert" markdown="1">
Mercer theorem: we do not need to know the mapping $\phi$ explicitly as long as we have a positive semi-definite kernel/Gram matrix $K=[\mathcal k(x_i,x_j)]=[<\phi(x_i),\phi(x_j)>]$
</div>

Widely used kernel functions:
- Polynomial kernel: $\mathcal k(x_i,x_j)=(x_i^Tx_j+1)^d$
- Gaussian RBF kernel: $\mathcal k(x_i,x_j)=e^{-\gamma\Vert x_i-x_j\Vert^2}$
- Sigmoid kernel: $\mathcal k(x_i,x_j)=\tanh(bx_i^Tx_j+c)$

## Kernel PCA

> PCA on steroids

The maths behind are quite hard, but the following scikit-learn recipe works fine:
1. Compute kernel matrix $k=[\mathcal k(x_i,x_j)]=[<\phi(x_i),\phi(x_j)>]$ and double-center it $K_c=C_nKC_n$
2. Eigendecomposition of $K_c$ is strongly related to this of the (intractable) covariance matrix in the feature space $\to$ get eigenvectors $V$ and corresponding eigenvalues $\Delta$ of $K_c$. ![](https://i.imgur.com/Mcio2jt.png)
3. Keep the first $M$ columns of $\sqrt{\Delta V}$ to get the coordinates of projected data points in the low $M$-dimensional space. ![](https://i.imgur.com/OkbLVXa.png)

But things get nasty when one wants to project a new data point $x$ that was not known when constructing the kernel...

## Non-linear PCA
> Also known as autoencoder

Overall idea:
1. train an autoencoder (neural network with an autoassociative architecture) to perform an identity mapping.
2. use the output of the bottleneck layer as low-dimensional code.

![](https://i.imgur.com/s1fuRi5.png)

Bottleneck code is a non-linear combination of entries (thanks to activation functions on the encoder layers) $\to$ learned mapping is a non-linear PCA.
![](https://i.imgur.com/rlaEDkG.png)

Principal components are generalized from straight lines to curves: the projection subspace which is described by all nonlinear components is also curved.

![](https://i.imgur.com/CtdC82G.png)

# Let’s recap
High-dimensional data set $X$ is a $n \times N$ matrix, with $n =$ number of samples and $N =$ dimensionality of underlying space.

![](https://i.imgur.com/tSi5kMZ.png)

- Parametric $\equiv$ explicit embedding from high-dimensional space to low-dimensional one
- For LLE: $p$ is the ratio of non-zero elements in a sparse matrix to the total number of elements
- For NL-PCA: $i$ is the number of iterations and w is the number of weights in the neural network

## t-Distributed Stochastic Neighbor Embedding
t-SNE is a popular method to see in 2D or 3D wtf is going on in a high-dimensional spaces.
1. Construct a probability distribution $p$ over pairs of points in the high-dim space: the more similar (the closer) the two points, the higher the probability
2. Define a second probability distribution $q$ over the points in the low-dim space, and dispatch the points such that the distance between p and q in minimized (for the KullbackLeibler divergence)

![](https://i.imgur.com/4645qRQ.png)

![](https://i.imgur.com/b4E3cZB.png)

![](https://i.imgur.com/PYnRtgM.png)

- t-SNE is excellent in visualizing the well-separated clusters, but fails to preserve the global geometry of the data.
- t-SNE depends on a perplexity parameter, which reflects the scale of search for close points.

## Independant component analysis
ICA aims to provide a solution to the so-called *cocktail party*: retrieving independent sources that got mixed-up together with unknown scaling coefficients.

![](https://i.imgur.com/2QEhLKX.png)

Goal: estimate source $s$ **and** mixing matrix $A$ from observation $x = As$.
- Ill-posed $\Rightarrow$ enforce independence on source components
- Work on higher order statistics (PCA limits to order-2 statistics)
- Unkown source must **not** be Gaussian-distributed

![](https://i.imgur.com/KyAc8m2.png)

Contrarily to PCA vectors, ICA vectors are not orthogonal and not ranked by importance,
but they are mutually independents.