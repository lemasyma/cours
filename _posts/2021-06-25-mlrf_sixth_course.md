---
title:          "MLRF: Lecture 06"
date:           2021-06-25 10:00
categories:     [Image S8, MLRF]
tags:           [Image, SCIA, MLRF, S8]
description: Lecture 06
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/Hy2LfRFju)

# Practice 5: Take home messages

<div class="alert alert-danger" role="alert" markdown="1">
BoVW is linear classification friendly
</div>
- And linear classifier are to be prefered whenever possible

Data preparation is tedious
- An important part of the time is dedicated to data analysis
- Plus we prepared a lot of things for you in the previsous sesssions

Scikit-learn is easy and super powerful
- Calssifier evaluation in 1 line
- But there is more: parameter tuning, cross-validation, etc. in 1 or 2 lines
- Data preprocessing + classification (pipelines) in 1-3 lines

# Some classifiers – part 2
## How to build non-linear classifiers ?
2 solutions:
1. **Preprocess** the data - *seen last time*
    - *Ex: explicit embedding, kernel trick...*
    - Change the input to make it linearly separable
2. **Combine** multiple **linear classifiers** into nonlinear classifier - *current topic*
    - *Ex: boosting, neural networks...*
    - Split the input space into linear subspaces

# Non-linear classification using combinations of linear classifiers
## Multi-layer Perceptron

<div class="alert alert-info" role="alert" markdown="1">
Combine features linearly, apply a linear activation function $\phi$, repeat
</div>

![](https://i.imgur.com/Da6rwGt.png)

## Universal approximation theorem

What if $\phi$ not linear ?

<div class="alert alert-success" role="alert" markdown="1">
Universal approximation theorem (Cybenko 89, Hornik 91)
![](https://i.imgur.com/JYVtKXM.png)

</div>

## Decision tree

Works on categorical (like, "red", "black") and numerical (both discrete and continuous) random variables

![](https://i.imgur.com/s1NXMQV.png)

![](https://i.imgur.com/xzuMcj6.png)


Train by optimizing classification "purity" at each decision (threshold on a particular dimension in numerical case)

Very fast training and testing. Non parametric.

No need to preprocess the features

BUT: very prone to **overfitting** without strong limits on depth

![](https://i.imgur.com/PHHgLkO.png)

## Random Forests

<div class="alert alert-info" role="alert" markdown="1">
**Average** the decision of multiple decision trees
</div>

![](https://i.imgur.com/oe9tXJS.png)

Randomize in 2 ways:
1. For each tree, pick a **bootstrap** sample of data ![](https://i.imgur.com/pu6Gxp8.png)
2. For each split, pick random sample of features ![](https://i.imgur.com/2vQd5KX.png)

More trees are always better

# Ensemble methods
## "Bagging" or "bootstrap aggregating"

<div class="alert alert-info" role="alert" markdown="1">
Underlying idea: part of the variance is due to the specific choice of the training data set
</div>

1. Let use create many similar training data sets using **bootstrap**
2. For each of them, train a new classifier
3. The final function will tbe the **average** of each function ouptuts

<div class="alert alert-danger" role="alert" markdown="1">
If generalization error is decomposed into bias and variance terms then bagging reduces variance (averag of large number of random error $\simeq 0$)
</div>

*Random forest = a way of bagging trees*

## "Boosting", AdaBoost variant

Combinaison of weak classifiers $\sum_m\alpha_mG_m(x)$

$\alpha_m$ increases with precision (less errors, bigger $\alpha_m$)

The classifier $G_m$ is trained with **increased error cost** for the observatins which were misclassified by $G_{m-1}$

![](https://i.imgur.com/3iISNzY.png)

# A quick comparison

![](https://i.imgur.com/mofCSdU.jpg)

# More tricks
## Data augmentation

*Add realistic deformations to your input in order to improve domain coverage.*

For **image data**, depending on what is possible in productin: rotations, horizontal & vertical dlips, scaling, translation, illumination change, warping, noise, etc.

![](https://i.imgur.com/ulNegtw.png)

For **vector data**: intersting problem. Possible approach: train/fit PCA then add random noise in low-energy features

## Reject

Several options:
1. *Improve the model of class boundary*
    - In 1-vs-all training, add noise to the "others" samples
2. *Adjust the decision function dependinf on your application*
    - Look at the prediction probabiblity of your classifier, and threshold it as per your need using a ROC curve
3. *Model the noise*
    - Add a "none" class to your classifier, with samples for real life cases of negatives samples

# More theory on ML
## What is our goal ?

> Given **samples** (described by features) and **true labels**,
> find a **good** function
> which wil correctly **predict labels**
> given new **data samples**

Problems:
- Which family for our function?
- What is “good”?
- How to train / find such function?

## What are the sources of error ?
- Noise
    - Your data is not perfect. (or “*Every model is wrong.*”)
    - Even if there exist an optimal underlying model, the observations are corrupted by noise (e.g. multiple y for a given x).
    - **- Even the optimal solution could be wrong.**
    - ![](https://i.imgur.com/Jukh31q.png)
- Bias
    - You need to simplify to generalize.
    - You classifier needs to drop some information about the training set to have generalization power.
    - **The set of solutions explored does not contain the optimal solution.**
    - ![](https://i.imgur.com/MlmJgiw.png)
- Variance
    - You have many ways to explain your training dataset
    - It is hard to find an optimal solution among those many possibilities.
    - **If we draw another training set from the same distribution, we would obtain another solution.**
    - ![](https://i.imgur.com/504PfiR.png)

## 2 big issues
Under-fitting
- Caused by **bias**
- Your model assumptions are too strong for the data, so the model won't fill well
- ![](https://i.imgur.com/Ivvw6xL.png)

Over-fitting
- Caused by **variance**
- Your algorithm has memorized the data including the noise, so it can’t generalize.
- ![](https://i.imgur.com/rB8koEQ.png)

# The theory
## Bias (statistical definition)

Let $T$ be a statistic used to estimate a parameter $\theta$. 

If $E[T] = \theta + bias(\theta)$ then $bias(\theta)$ is called the bias of the statistic $T$, where $E[T]$ represents the expected value of the statistics $T$.

If $bias(\theta) = 0$, then $E[T] = \theta$. So, $T$ is an unbiased estimator of the true parameter, say $\theta$. 

## Expected Risk

Let $D_n$ be a training set of examples $z_i$ drawn independently from an unknown distribution $p(z)$

We need a set of functions F. Example: linear functions $f(x) = a \times x + b$

We need a loss function $L(z, f)$. Example: $L((x, y), f ) = (f (x) − y)^2$

<div class="alert alert-info" role="alert" markdown="1">
The **Expected Risk**, i.e. the expected generalization error, is:

![](https://i.imgur.com/hU9xLCN.png)

</div>

But we do not know $p(z)$, and we cannot test all $z$!

## Empirical Risk

<div class="alert alert-info" role="alert" markdown="1">
Because we cannot measure the real **Expected Risk**, we have to estimate it using the **Empirical Risk**:
![](https://i.imgur.com/buQaJeQ.png)

$D_n$ is our dataset
</div>

And our training procedure then relies on **Empirical Risk Minimization (ERM)**:
![](https://i.imgur.com/t8tiBBp.png)

And the training error is given by:
![](https://i.imgur.com/9revSrN.png)

### Does this make sense?

<div class="alert alert-success" role="alert" markdown="1">
**The empirical risk is an unbiased estimate of the risk**, i.e. the more test samples we have, the more accurate our estimate is, **under iid assumption**.
</div>

![](https://i.imgur.com/Mo0ZQBM.png)

## But the training risk is biased

The training error is a biased estimate of the risk, i.e. the solution $f^★ (D_n)$ found by minimizing the training error is better on $D_n$ than on any other set $D'_n$ drawn from $p(z)$.

![](https://i.imgur.com/brPepp2.png)

However, under certain assumptions, the difference between the expected and the empirical risks can be bounded. This is an important result from the work of Vapnik

Note that the empirical risk on the test set is an unbiased estimate of the risk.
![](https://i.imgur.com/dLakZp5.png)

## Estimate the Expected Risk with the Empirical Risk
*For a given capacity*, using more samples to train and evaluate your predictor **should** make your Empirical Risk converge toward the best possible Expected Risk, if the ERM is consistent for $F$, given your training set $D_n$.

![](https://i.imgur.com/aUHJXBD.png)

The difference between Expected Risk and Empirical Risk is **bounded** but depends on the *capacity* of $F$ (set of possible functions).

There is an **optimal** capacity for a given number of training samples $n$.

![](https://i.imgur.com/8cPTpvd.png)

## Capacity
The capacity $h(F)$ is a measure of its size, or complexity (or VC dimension)

For classification, the capacity of $F$ is defined by Vapnik & Chervonenkis as:
- the largest $n$
- such that there exist a set of examples $D_n$
- such that one can always find an $f \in F$
- which gives the correct answer for all examples in $D_{n'}$
- for any possible labeling.

## The Bias-Variance Dilemma
Intrinsic dilemma: when the capacity $h(F)$ grows, the bias goes down, but the variance goes up!

![](https://i.imgur.com/mgX4zCj.png)

![](https://i.imgur.com/rxjY8kI.png)

## Decomposing the bias-variance-error for MSE
For a regression problem with a mean square loss, we have the following decomposition. Let $Y = f(X) + \varepsilon$, with $\varepsilon \sim N(0, \sigma_{\varepsilon}^2)$ and $f_D(X)$ an estimator of $f(X)$, learned over the training set $D$. The error at a particular point $X = x_0$ is:

![](https://i.imgur.com/LRsxpLB.png)

![](https://i.imgur.com/7S5ueXj.png)

# In practice
## Empirical Risk and Expected Risk

<div class="alert alert-danger" role="alert" markdown="1">
Measure train and test error
</div>

Use hold-out sets, cross-validations, etc. to get a test error.

**Train** error: **Empirical** Risk.
*Can my model learn something (by heart)?*

**Test** error: Coarse estimate of the **Expected** Risk.
*Can my model generalize to unseen data?*

## Detect under-fitting and over-fitting

![](https://i.imgur.com/tA9gs0r.png)

![](https://i.imgur.com/iFls3iy.png)

## Some solutions / hints

![](https://i.imgur.com/fwFAoQX.png)

![](https://i.imgur.com/0fD8QHJ.png)

# How to get started?
1. Get enough data in the right format from your customer *(hard)*
2. Check and split data *(boring but mandatory)*
3. Agree on a loss function and minimum performance goal *(moderate)*
4. Try to overfit a predictor on some samples (train set loss), increase complexity only if needed (capacity check)
5. Fit on more data *(more = better)*
6. Check for overfitting (val set loss) and add regularization if needed
7. Evaluate performance thoroughly (test set loss) *(reports, identify failure cases, etc.)*
8. Do some hyper-parameter optimization, try other models…
9. ...

# Introduction to practice session 6
## Using classification to segment images

Until now
- 1 image $\to$ many vectors (instance recognition)
- 1 image $\to$ 1 vector (image retrieval, image classification)

Today / next practice session : 
- 1 pixel →1 vector (pixel classification, image semantic segmentation)

# Brain Anatomy and Imaging
## Human brain = Where human OS is stored and run

![](https://i.imgur.com/ysWPXnI.png)

![](https://i.imgur.com/zOtjdsr.png)

## To investigate brain malfunction, two options:

![](https://i.imgur.com/BfAL7lO.png)

![](https://i.imgur.com/acPZDvM.png)

## Magnetic Resonance Imaging (MRI)

![](https://i.imgur.com/ttg3xJf.png)

![](https://i.imgur.com/S8aRYVR.png)

## Everything you always wanted to know about MRI

![](https://i.imgur.com/geUyEAg.png)

Hydrogen atoms are naturally abundant in humans, particularly in water and fat.

Pulses of radio waves excite the nuclear spin energy transition, and macroscopic polarization that is detected by antennas. 

Magnetic field gradients localize the polarization in space. By varying the parameters of the pulse sequence, different contrasts may be generated between tissues based on the relaxation properties of the hydrogen atoms therein.

## What you actually need to know

MRI is a large family of imaging techniques

They can produce 3D scans of various appearances in order to emphasize some human tissues versus others.

![](https://i.imgur.com/fuh9DXP.png)

# BraTS: Brain Tumor Segmentation Competition
## Original segmentation task
Given a 3D scan (skull-stripped, registered) of a patient with T1, T2, T1C and FLAIR modalities, predict a tumor class for each voxel (the patient suffers from a glioma):

![](https://i.imgur.com/fJN1dK4.png)

Avec:
- edema (yellow), 
- non-enhancing solid core (red), 
- necrotic/cystic core (green), 
- enhancing core (blue).

## Original dataset
The 2018 competition we use the data from originally contains 285 brain scans.

# Your Mission
## A simplified competition
Because dealing with 3D and data normalization would take you much time and pain, we:
1. already performed **data normalization**
2. extracted **2D (axial) slices** that you have to process

## Actual task
Given a $240\times240$ image with $4$ modalities (already normalized), predict for each pixel whether it belongs to a tumor or nor.

![](https://i.imgur.com/TTDbvMR.png)

## Actual dataset
Train set
- $256$ normalized slices, one per patient, containing $240\times240$ images with $4$ channels ($1$ for each modality), `float32`
- $256$ target segmentations, one per patient, containing $240\times240$ images with $1$ channel (indicating tumor or clean region), `uint8`

Test set
- $29$ normalized slices, one per patient (not in the training set), containing $240\times240$ images with $4$ channels ($1$ for each modality), `float32`
- *Ground truth kept secret for grading*

# Suggested Pipeline
## Data preprocessing
<div class="alert alert-warning" role="alert" markdown="1">
We already did this step.
</div>

## Choose and train a classifier
There are several suggestions in the reference notebook: SVM, neural network, etc.

- Input = 1 vector of 4 components for each pixels
- Output = 1 for tumor, 0 for “not tumor”

<div class="alert alert-warning" role="alert" markdown="1">
Do not use background (“black”) pixels for training, they would ruin your classification
</div>

<div class="alert alert-warning" role="alert" markdown="1">
Deep nets can work but they are harder to train well.
</div>

<div class="alert alert-warning" role="alert" markdown="1">
And don’t use deep nets, we’ll play with them next semester
</div>

## Validate your training

Create and use a validation set extracted from the full training set.

To not train on the samples it contains.

`sklearn.model_selection.train_test_split` may be your friend.

<div class="alert alert-danger" role="alert" markdown="1">
Check visually results from both train and val sets!
</div>

## Interpret your results

![](https://i.imgur.com/6euveJc.png)

## Add some context to each pixel
You can get better results by looking at the neighborhood of a pixel to classify it better: train with vectors of size $N\times M$ instead of $1\times M$.

## Fighting underfitting and overfitting

<div class="alert alert-danger" role="alert" markdown="1">
You do not have much data to train on
</div>

If you pick a classifier which is too simple, you may underfit: you will get low and similar scores both on the train and test sets

Choosing another classifier may be a good idea here.

You may also easily overfit your classifier, especially if you use one with a large capacity: you will get excellent scores on the train set, and bad ones on the test set.

Regularization may be necessary.

## Post processing
We suggest in the notebook to “clean up” the results by removing very small isolated pixels marked as tumor.

You may have many other ideas here

# Going Further
## Many options
- Data augmentation to increase train set
- Larger / better neighborhood for each pixel
- Better ANN structure than the one suggested in the notebook
- Change the representation space? (Fourier, wavelets…)
- As the tumors under consideration may not have “holes”, improve the post-processing
- ~~Super heavy classifiers (UNet, Gradient Boosted Trees…)~~
- ...

# Conclusion
## Course overview: a very small glimpse of CV/PR/ML

![](https://i.imgur.com/D2H4xvT.png)

## Welcome to 2012
AlexNet by A. Krizhevsky, I. Sutskever, G. E. Hinton halved error rate on ImageNet competition

![](https://i.imgur.com/WtFw5va.png)

![](https://i.imgur.com/0vA9SRl.png)

## Deep learning

Will be there for a few years!

Is a natural extension of what we saw: feature extraction, encoding, pooling, classification in a **single, integrated, globally optimized pipeline.**

Requires skills you learned: **dev, math, data preparation, evaluation.**
*Input data still need to be properly normalized, for instance.*

Requires **a lot of practice**: read papers, don’t be impressed by the math, implement them.

If not applicable, then pick one of the good old technique we talked about.
