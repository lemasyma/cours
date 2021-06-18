---
title:          "MLRF: Lecture 05"
date:           2021-06-018 10:00
categories:     [Image S8, MLRF]
tags:           [Image, SCIA, MLRF, S8]
description: Lecture 05
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/Hy2LfRFju)

# Agenda
1. Introduction
2. Image classification overview
3. Some classifiers - part 1
4. Classifier evaluation

# Summary of last lecture
Content-based image retrieval
- 2 strategies: keep all local descriptors for all images vs **1 descriptor per image**
- Bag of Visual Words pipeline
    - Focus on encoding

Evaluation of image retrieval systems
- Precision
- Recall
- F-Measure
- mAP

Texture descriptors (on les a pas du tout vu)
- What is a texture ?
- Fast and classic approaches
- Descripteurs a l'ancienne

# Practice session 4: Take home messages
BoVW
- Usually requires some **preprocessing** of the descriptors: centering, rotation/axes permutation, dimensionality reduction...
- Is based on a **quantization step** (assign descriptors to clusters)
- Is **just a histogram**, like the color histogram of sessino 2
- We can compute **more advanced statistics** to get better results (VLAD, FVs)

<div class="alert alert-warning" role="alert" markdown="1">
**Best practices:**
- Test arrays shapes and types as soon as possible
- Make a small change, test, fix, tes, validate, repeat
- Get a complete, basic pipeline ASAP and improve it until time is over
</div>

# Next practice session

Implement a simple **image classifier**:

![](https://i.imgur.com/JRTgDIl.png)

<div class="alert alert-danger" role="alert" markdown="1">
**Will be graded**
</div>

## Steps

1. Load resources
2. Train a BoVW model
3. Split the dataset into training and validation sets
4. Compute the BoVW descriptor for each image
    - We will make a small change here (sqrt + L2-norm)
6. Prepare training structures
7. Train a classifier and evaluate its performance
    - Training and evaluating is easy with scikit learn
9. Display some results
10. Test on meme image
11. Compute the results on the test set and export them

# Image classification overview

## Instance recognition vs Class recognition
### Instance recognition
Re-recognize a known 2D or 3D rigid object, potentially being viewed from a novel viewpoint, against a cluttered background, and with partial occlusions

*Ex: practice session 3*

![](https://i.imgur.com/zjxx8F3.png)

### Class recognition
Recognize any instance of a particular general class such as "cat", "car" or "bicycle"

Aka *category-level* or *generic* object recognition

<div class="alert alert-warning" role="alert" markdown="1">
More challenging
</div>

*This lecture and next practice session*

![](https://i.imgur.com/fvvBXlU.png)

## Pipeline overview

![](https://i.imgur.com/ufF8vdn.png)

## Our image classification pipeline
This is a **supervised** machine learning task
- We need a dataset with samples
- Images will be represented as BoVW vectors of fixed size ![](https://i.imgur.com/iGnNMb9.png)
- Targets will be encoded as integers ![](https://i.imgur.com/OV5hiUn.png)
    - 0: Muffin
    - 1: Chihuahua

This is a very usual data representation for a classification problem

<div class="alert alert-info" role="alert" markdown="1">
Classifier inputs = "samples" with "features"
Classifier outputs = "labels"
![](https://i.imgur.com/RUZZam9.png)

</div>

Now we just need to select an appropriate method, prepare our data, run some training, test the results, adjust some parameters, compare approaches, display results, ... 

# Data preparation
## NumPy formatting

![](https://i.imgur.com/WnT18Ch.png)

## Training/validation/test separation
- **You cannot estimate the generalization performance of your predictor/estimator/classifier on its training set**
- You need to keep some samples aside for later evaluation

## Other "funny" things to do IRL
- Collect data
- Clean data
- Check data
- Clean again
- Annotate
- Check
- Compute/convert/scale features

## Feature selection

<div class="alert alert-info" role="alert" markdown="1">
Consists in dropping some data columns
</div>

Can help later stages:
- Less data to process
- Better properties (like decorrelated features, etc.)

Which columns ?
- Hard problem in general
    - Because features may be informative **as a group**
- Some simpler and helpful techniques:
    - Remove features with low variances
    - Dimensionality reduction techniques are not exactly feature selection, but can still have a similar effect

# Some classifiers - part 1
## Disclaimer

<div class="alert alert-warning" role="alert" markdown="1">
What follows is a very limited selection
</div>

Only classifiers suitable for image classification as we present it today

<div class="alert alert-info" role="alert" markdown="1">
**input = feature vector**
**output = label**
</div>

Many other approaches

## What is our goal ?

<div class="alert alert-danger" role="alert" markdown="1">
Given samples (described by features) and true lables, find a good function which will correctly predict labels given new data samples
</div>

## Parametric vs Non Parametric Classifiers
### Parametric examples
Logisitic regression, Linear Discriminant Analysis, naive Bayes, Perceptrion, Simple Neural Networks..

> A learning model that summarizes data with a set of parameters of fixed size (independant of the number of training examples) is called a parametric model. No matter how much data you throw in nature

### Non-parametric examples
k-Neares Neighbors, Decision Trees, SVMs

> *"Non-parametric models differ from parametric models int that hte model structure is not specified a priori but is instead determined from data. The term non-parametric is not meant to imply that such models completely lack parameters but that the number and nature of the parameters are flexible and not fixed in advance"*
> Wikipedia

> *"Nonparametric methods are good when you have a lot of data and no prior knowledge"*

## Dummy classifiers

Say you have a dataset with 9 muffins and 1 chihuahua.

You have a new sample to classify.

**Which class should you bet on ?**

![](https://i.imgur.com/Sy1wvkC.png)

If your class prior probabilities $P(C_1), P(C_2),\dots$ are not equal, then you should bet on the **most frequent class!** ($g(x)=argmax_yp(y)$)

Without such information, you can just pick at random

*Waht is the expected accuracy (true predictions / total predictions) if you have N classes an pick one at random ?*

<div class="alert alert-info" role="alert" markdown="1">
Scikit-learn offers a DummyClassifier class which helps testing such a strategy
</div>

### What's the point ?

1. Quickly build and test your complete pipeline with a mockup classifier
2. Quickly get a baseline for the performance
3. (look for obvious bias in the dataset, but you should have cleaned it before !)

## K Nearest Neighbor (kNN)

Keep all training samples

View new samples as quieries over the previously learned / indexed samples

![](https://i.imgur.com/vGq3eFP.png)

Assign the class of the closest(s) samples

$$
f(x) = y_i, i = argmin_j\Vert x_j-x\Vert
$$

![](https://i.imgur.com/13qgkgU.png)


We can check more than one sample

![](https://i.imgur.com/yQB482y.png)


![](https://i.imgur.com/NYzoX1K.png)

### Remember thi bias/variance compromise ?

![](https://i.imgur.com/LxXw7gB.png)

### Pros
- very simple to implement
- Capacity easily controlled with k
- Can be tuned to work on large datasets: indexing, data cleaning, etc.
- Good baseline
- Non parametric
- Lazy learner

### Cons
- In high dimension, all samples tend to be very close (for Euclidean dimension)
- Large memory consumption on large datasets
- Requires a large amount of samples and large k to get best performance

<div class="alert alert-danger" role="alert" markdown="1">
**Setting K:**

$$
K\simeq\sqrt{\frac{m}{C}}
$$

$\frac{m}{C}$: average number of training sample/class
</div>

## Other distance-based classifier
### Minimal euclidean distance

**Very basic classifier**

Distance to the mean $m_i$ of the class

It does not take into account differences
in variance for each class

Predicted class for x:

$$
g(x) = argmin_iD_i(x)
$$

![](https://i.imgur.com/zTOkAeB.png)


### Minimal quadratic distance (Mahalanobis)
For each class $i$, the mean $m_i$ and covariance matrix $S_i$ are computed from the set of examples

The covariance matrix is taken into account when computing the distance from an image to the class $i$

The feature vector of the image $x$ is projected over the eigenvectors of the class

$$
g(x) = argmin_iD_i(x)
$$

![](https://i.imgur.com/iBAfkDT.png)


# A quick introduction to Bayesian Decision Theory
## Example - RoboCup

![](https://i.imgur.com/6znaC7D.png)

![](https://i.imgur.com/gS6isnG.png)

![](https://i.imgur.comkITm9Y.png)

## General case: maximum a posteriori (MAP)

<div class="alert alert-info" role="alert" markdown="1">
General case: need to tale into consideration $p(y)$ and $p(x)$
</div>

- $p(x\vert y)$: class conditional density (here: histograms)
- $p(y)$: class priors, e.g. for indoor RoboCup
- $p(floor) = 0.6$, $p(goal) = 0.3$, $p(ball) = 0.1$
- $p(x)$: probability of seeing data $x$

Optimal decision rule (Bayes classifier): maximum a posteriori (MAP):

$$
g(x) = argmax_{y\in Y}p(y\vert x)
$$

### How to compute $p(y\vert x)$ ?

$$
p(y\vert x) = \frac{p(x\vert y)p(y)}{p(x)}\quad\text{Bayes' rule}
$$

If classes are equiprobables and error cost is the same, then, because $p(x)$ is constant, we get the maximum likelihood estimation:

$$
g(x) = \underbrace{argmax_{y\in Y}p(y\vert x)}_{\text{MAP}}\simeq\underbrace{argmax_{y\in Y}p(x\vert y)}_{\text{ML}}
$$

## Generative, discriminant and "direct" classifiers

![](https://i.imgur.com/UlPjAcK.png)

# Generative Probabilistic Models
## Some classical Generative Probabilistic Models

Training data $X=\{x-1,\dots,x_n\}$, $Y=\{y_1,\dots,x_n\}$. $X\times Y\in\mathcal X\times\mathcal Y$

For each $y\in\mathcal Y$, build model for $p(x\vert y)$ of $X_y:=\{x_i\in X:y_i=y\}$

- Histogram: if $x$ can have only a few discrete values
- Kernel Density Estimator ![](https://i.imgur.com/ZIJ8gxo.png)
- Gaussian ![](https://i.imgur.com/KFvVTpi.png) 
- Mixture of Gaussians ![](https://i.imgur.com/KDKezfM.png)

Typically, $\mathcal Y$ small (few possibles lables), $\mathcal X$ low dimensional

## Class conditional densities and posteriors

![](https://i.imgur.com/DUCdiKg.png)

## Naive Bayes Classifiers

![](https://i.imgur.com/E5Pz6Qx.png)

![](https://i.imgur.com/VxjSGbd.png)


# Linear discriminant classifiers
## General idea for binary classification

![](https://i.imgur.com/l6uLtyC.png)

![](https://i.imgur.com/H4NM4Za.png)

Learn w and b
- you can compute $p(y\vert x)\simeq\hat y$

<div class="alert alert-warning" role="alert" markdown="1">
Problem: how to learn w and b ?
</div>

## Logistic Regression

Linear classifier, $f$ is logistic function

$$
\sigma(x) = \frac{1}{(1+e^{-x})} = \frac{e^x}{(1+e^x)}
$$
- Maps all real $\to[0,1]$

Optimize $\sigma(w^Tx+b)$ to find best $w$

Trained using gradient descent (no closed form solution)

![](https://i.imgur.com/RZoBc0Y.png)

## Gradient descent

Formally:

$$
w_{t+1}=w_t-\eta\nabla L(w)
$$

Where $\eta$ is *step size*, how far to step relative to the gradient

![](https://i.imgur.com/eXfRl8J.png)

## From 2 classes to C classes: 2 strategies

![](https://i.imgur.com/hB0yq8C.png)

![](https://i.imgur.com/E8QRm0Z.png)

$$
\hat y = argmax_{i\in Y}w_ix
$$

## Maximum Margin classification

![](https://i.imgur.com/8zbmVyB.png)

What is the best $w$ for this dataset ?

Trade-off:
large margin vs few mistakes on training set

![](https://i.imgur.com/3tH5H3Z.png)

## Support Vector Machin (SVM)

![](https://i.imgur.com/AMNYWuJ.png)

## Logistic Regression vs SVM

Optimization problems:

![](https://i.imgur.com/NGEFBBe.png)

## About the regularizer

![](https://i.imgur.com/zY3MiZQ.png)

## Effect of cost parameter C (regularization, again)

![](https://i.imgur.com/QEjgzaK.png)

# Non-linear discriminant classifiers
## Non-linear classification

What is the best linear classifier for this dataset?

![](https://i.imgur.com/4IRGUzO.png)

<div class="alert alert-success" role="alert" markdown="1">
None. We need something nonlinear!
</div>

2 solutions:
1. Preprocess the data (explicit embedding, kernel trick…)
2. Combine multiple linear classifiers into nonlinear classifier (boosting, neural networks…)

# Non-linear classification using linear classifiers with data preprocessing
## Data preprocessing idea

Transform the dataset to enable linear separability

![](https://i.imgur.com/iJr7bVs.png)

## Linear separation is always possible
The original input space can always be mapped to some higher-dimensional feature space where the training set is separable.

![](https://i.imgur.com/21JoSx4.png)

## Explicit embedding

Compute $\phi(x)$ for all $x$ in the dataset.

Then train a linear classifier just like before

<div class="alert alert-warning" role="alert" markdown="1">
Used to be avoided because of computation issues, but it is a hot topic again.
</div>

## Kernel trick
Linear classification requires to compute only dot products $\phi(x_i),\phi(x_j)$

**The function $\phi(x)$ does not need to be explicit,** we can use a kernel function

$$
k(x,z)=\phi(x)\phi(z)
$$

which represents a dot product in a “hidden” feature space.

<div class="alert alert-success" role="alert" markdown="1">
This gives a non-linear boundary in the original feature space.
</div>

## Popular kernel functions in Computer Vision

Linear kernel”: identical solution as linear SVM

![](https://i.imgur.com/dtD4CbJ.png)

“Hellinger kernel”: less sensitive to extreme value in feature vector

![](https://i.imgur.com/Cz0oSkY.png)

“Histogram intersection kernel”: very robust
![](https://i.imgur.com/CDbNlrq.png)

“$X^2$-distance kernel”: good empirical results
![](https://i.imgur.com/dG3QTIm.png)

“Gaussian kernel”: overall most popular kernel in Machine Learning
![](https://i.imgur.com/f0yjvx6.png)

## Explicit embedding for the Hellinger kernel

![](https://i.imgur.com/bakMDIs.png)

Using simple square root properties, we have:

$$
k(x,x’) = \phi(x)\phi(x’) = \sqrt{x} \sqrt{x'}
$$

Tricks for next practice session: given a BoVW vector,
1. L1 normalize it (neutralizes effect of number of descriptors)
2. Take its square root (explicit Hellinger embedding)
3. L2 normalize it (more linear-classifier friendly)

# Metrics
## Confusion matrix and Accuracy

![](https://i.imgur.com/OZXWA8Q.png)

## Problems with Accuracy
All the following classifiers have a 90% accuracy

![](https://i.imgur.com/2ciC5Uz.png)

*Do all errors have the same cost?*

## Precision, recall, F-score

![](https://i.imgur.com/VMpNMQH.png)

## Plotting a Precision/Recall for classification data

For binary classification

Instead of $\hat y = argmax_yp(y\vert x)$, take **all possible thresholds** for $p(y\vert x)$

![](https://i.imgur.com/VtynSfU.png)

## TPR, FPR, ROC

ROC: “Receiver Operating Characteristic”
Kind of signaloise measure under various tunings

![](https://i.imgur.com/k3BeCv0.png)

Ligne rose: random results

## More about ROC curves: 
### Adjusting the threshold

[http://www.navan.name/roc/](http://www.navan.name/roc/)

![](https://i.imgur.com/2CQamZr.png)

### Class overlap

![](https://i.imgur.com/BWAThY5.png)

# Split the dataset to assess generalization performance
## Bootstrap

Draw randomly, with replacement samples from the training set.

Enables us to estimate the variance of estimators we use in the classification rule.

![](https://i.imgur.com/ZuxQOyR.png)


## Holdout

Just keep a part of the dataset for later validation/testing

![](https://i.imgur.com/513iOG6.png)

## Cross validation

![](https://i.imgur.com/4KkbALB.png)

### with meta parameter tuning

![](https://i.imgur.com/vf2xEDm.png)

## StratifiedKFold (best)

![](https://i.imgur.com/IELUcaX.png)

## Missing things
- Cost of misclassification
- Multiclass classification evaluation
- ...