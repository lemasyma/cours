---
title:          "IML: Supervised learning"
date:           2021-04-14 14:00
categories:     [Image S8, IML]
tags:           [Image, SCIA, IML, S8]
description:    Supervised learning
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/HknU58EIO)

# Supervised learning

<div class="alert alert-info" role="alert" markdown="1">
**Supervised learning:** process of teaching a model by feeding it input data as well as correct output data. The model will (hopefully) deduce a correct relationship between the input and output
</div>
- An input/output pair is called *labeled data*
    - All pairs form the *training set*
- Once training is completed, the model can infer new outputs if fed with new inputs.

![](https://i.imgur.com/Qldp6N6.png)


Given some training data $\{x_i,y_i\}^n_{i=1}$, supervised learning aims at finding a model $f$ correctly mapping input data $x_i$ to their respective output
- The model can predict new outputs
- The learning mechanism is called *regression* or *classification*

![](https://i.imgur.com/Xfx2W4Y.png)

# Managing data for supervised learning
Hide some data out during training ($\simeq20\%$ data) to further evaluate model performances $\Rightarrow$ train/test split
Use validation set ($\simeq15\%$ data) if parameters are iteratively adjusted $\Rightarrow$ tain/validation split

![](https://i.imgur.com/dNjoxrs.png)

## Stratified sampling
> For classification purposes

CLasses might be imbalanaced $\Rightarrow$ use stratified sampling to guarantee a fair balance of train/est samples for each class

![](https://i.imgur.com/LEWGAc9.png)

# Regression
> The art of predicting values

<div class="alert alert-info" role="alert" markdown="1">
**Regression**: the output value to predict $y$ is quantitative (real number)
</div>

![](https://i.imgur.com/ASmFdgA.png)

$\Rightarrow$ How to mathematically model the relationship between predictor variables $x_i$ and their numerical output $y_i$ ?

## Linear regression
Sometimes, there's no need for a complicated model...

![](https://i.imgur.com/KnOVw16.png)

![](https://i.imgur.com/v2HuFrX.png)

## Ordinary Least Squares
![](https://i.imgur.com/o2HCOeb.png)

## Anscombes' quartet

For all 4 datasets $\{(x_1,y_1),(x_2,y_2),...,(x_{11},y_{11})\}$

![](https://i.imgur.com/5GCBu59.png)

Le 3e regression a une *donnee aberrante*, cad une donnee tres eloignee des autres qui risque de fausser la regression (probablement du au capteur qui s'est chie dessus)

$\Rightarrow$ Linear regression line $y=3+0.5x$ and $R^2=0.67$ are the **SAME** for all 4 datasets

## Least absolute deviation
Linear regression by OLS is sensitive to outliers (tj=hank you $L_2$ norm...)

![](https://i.imgur.com/GLH1gJh.png)
![](https://i.imgur.com/joBDMuK.png)

*Is it a good idea ?*
- $\beta_{LAD}$ is the MLE estimator of $\beta$ when noise follows a Laplace distribution
- No analyticial formula for LAD
    - Harder to find the solution
    - Must use gradient descent approach
- Solution of LAD **may not be unique**

![](https://i.imgur.com/OnwIuhP.png)
<div class="alert alert-warning" role="alert" markdown="1">
Toutes les droites dans le cone sont optimales
</div>

## Adding some regularization
Add apenalty term to OLS to eforce particular properties to $\hat\beta$

![](https://i.imgur.com/2Kcnvje.png)

## From regression to classification
### Logistic regression
Linear regression predicts a real value $\hat y$ based on predictor variables $x=(x^{(1)},...,x^(k))$
- Does not work is $y$ is boolean
- $P(y=1)=p$ and $P(y=0)=1-p$
- Use logistic regression instead

![](https://i.imgur.com/lLIaSGd.png)

Linear relationship between predictor variables and logit of event:

![](https://i.imgur.com/JA8tFGp.png)

![](https://i.imgur.com/bsuCgNc.png)

# k-nearest neighbors
k-NN classifier simply assigns test data points to the majority class in the neighborood of the test points
- no real training step

![](https://i.imgur.com/lv8noT8.png)

Result:
![](https://i.imgur.com/pBdj6Wt.png)

## Choosing k
- small k: simple but noisy decision boundary
- large k: smoothed boundaries but computationally intensive
- $k=\sqrt{n}$ can also serve as a starting heuristic, refined by cross-validation
- $k$ should be odd for binary classification

![](https://i.imgur.com/ydcwHXm.png)

## k-nearest neighbors for regression
Use the k nearest neighbors (in terms of features only) and average to get predicted value

![](https://i.imgur.com/XDcEhsh.png)

![](https://i.imgur.com/ETtZj4O.png)

# Support Vector Machine
## Linear SVM
Training set: $$\{x_i,y_i\}_{i=1}^n$$ with $x_i\in\mathbb R^p$ and $y_i\in\{-1,+1\}$

Goal: find hyperplane that best divide *positive* sample and *negative* samples

![](https://i.imgur.com/Lw1a9SK.png)
*Qu'est-ce qu'on a envie de faire ici ?*
Une moyenne

![](https://i.imgur.com/DxOBlOY.png)

<div class="alert alert-success" role="alert" markdown="1">
On cherche la droite qui *passe le plus au centre*

![](https://i.imgur.com/yLBeNxo.png)

</div>

Rappel: produit scalaire de 2 vecteurs colineaires:

$$
<\vec w, \vec{AB}> = \Vert \vec w\Vert.\Vert \vec{AB}\Vert
$$

![](https://i.imgur.com/Bg7DrvS.png)

## Soft margin SVM

Data may not be fully linearly separable

## Kernel SVM
> Remember the kernel trick ?

Kernel trick:
- map data points into high dimesional space where they would become linearly separable
- Effortlessly interfaced with the SVM by replacing dot product $<.,.>$ by kernelizes version $k(.,.)$

![](https://i.imgur.com/Eb8S2SB.png)


Widely used kernel functions:
- Polynomial kernel ![](https://i.imgur.com/jWSsnBZ.png)
- Gaussian RBF kernel ![](https://i.imgur.com/qFneRGj.png)
- Sigmoid kernel ![](https://i.imgur.com/0j7NqQr.png)

## Choosing the right kernel with the right hyperparameters

Kernel $\Rightarrow$ Try linear first. If does not work, RBF is probably the best kernel choice (unless you have some prior information on the geometry of your dataset)

Hyperparameters ($C$ + kernel parameter(s)) $\Rightarrow$ grid search and cross-validation

# Mutliclass SVM
## What if we have more than 2 classes ?
2 possible strategies

**one vs all:** One SVM model *per class* $\to$ separate the class from all other classes
- Assign new points with *winner takes all* rule
- if no outright winner, assign point to the class of closest hyperplane (Platt scaling)

**One versus one**: one SVM model *per pair of classes* $\to$ separate 2 classes at a time, ignoring the other data
- assign new points with *majority voting* rule

![](https://i.imgur.comRtugaz.png)

# Decision trees
<div class="alert alert-info" role="alert" markdown="1">
Decision trees use recusrive partitioning to create a sequence of decision rules on input features that nested split of data points
</div>

Input features can be numeric (decision $\le$) or categorical (decision $==$)

Decision node $=$ decision rule for one feature

Classification tree $\to$ predict class
Regression tree $\to$ predict real number

![](https://i.imgur.com/boFTfRm.png)

On the current node, try to apply all the possible decision rules for all features and select the decision that best split the data
Classification tree $\to$ impurity riterion
Regression tree $\to$ variance reduction

![](https://i.imgur.com/QV9u5WY.png)

Final decision boundaries $\equiv$ overlapping orthogonal half planes
Decision on new data $\to$ running it down through the branches and assign classes

## How to split a node

Which split should we choose between ![](https://i.imgur.com/upBo3VQ.png)

![](https://i.imgur.com/GBwhhZY.png)
> La reponse est goche

![](https://i.imgur.com/E0oAirn.png)

![](https://i.imgur.com/REyBYVW.png)

<div class="alert alert-success" role="alert" markdown="1">
Stop recursive partitionning if node is pure
</div>

## Pros and cons of decision trees
### Pros
- Simple decision rules
- Surprisingly computationally efficient
- Handle multiclass problems
- Handle numeric and categorical features at the same time

## Cons
- Strongly overfit data
    - Bad predictive accuracy

![](https://i.imgur.com/NWFghGJ.png)

<div class="alert alert-success" role="alert" markdown="1">
**Potential solution**
Restrain the growth of the tree by imposing a maximal tree depth
</div>

## Random forests
> Bagging several decision trees

Decision trees are *weak* classifiers when considered individually
- Average the decision of several of them
    - Compensate their respective errors (*wisdom of crowds*)
- Useless if all decision trees see the same data
    - introduce some variability with *bagging* (bootstrap aggregating)
- Introduce more variability by selecting only $p$ out of $m$ total features for each split in each decision tree (typically $p=\sqrt{m}$)

![](https://i.imgur.com/sypxX62.png)

Final decision is taken by majority voting on all decision tree outputs
![](https://i.imgur.com/ToaBCwg.png)


# Decision boundaries comparison
![](https://i.imgur.com/iizKHKj.png)

## Evaluating regression/classification performances
![](https://i.imgur.com/fvXdKV8.png)

# Cross-validation

$k$-fold cross validation
- Divide whole data into $k$ non-overlapping sample blocks
- Train $k$ models on $(k-1)$ training blocks and test on remaining block
- Compte perf metrics of each model + avergae & standard deviation of all $k$ models

![](https://i.imgur.comrYJlCm.png)

# Confusion matrix
![](https://i.imgur.com/KHqLVmX.png)
