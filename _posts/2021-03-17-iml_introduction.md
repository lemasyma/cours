---
title:          "IML:Introduction"
date:           2021-03-17 11:00
categories:     [Image S8, IML]
tags:           [Image, SCIA, IML, S8]
description:    Introduction
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/SkZk7Iy4O)

# Motivation
## What is learning ?
It's all about evolving

<div class="alert alert-info" role="alert" markdown="1">
**Definition**
*Learning*: Improver over experience to perform better in new situations.
</div>

<div class="alert alert-danger" role="alert" markdown="1">
**Quoting S. Bengio**
Learning is **not** learning by heart.
Any computer can learn by heart.
The difficulty is to **generalize** a behavior to a novel situation.
</div>

## Can machines learn ?
A new **science** with a goal and an object.

<div class="alert alert-info" role="alert" markdown="1">
How can we **build** computer systems that automatically improve with experience, and what are the **fundamental laws** that govern all learning processes ?
> Tom Mitchel, 2006
</div>

## What is it good for ?
According to Peter Norvig

The **3 main reasons** why you may want to use Machine Learning:
- Avoid coding **numerous complex rules** by hand
    - lower cost, more effective, faster reaction to changing problem
- **Optimize the parameteres** of your system given a dataset of yours
    - Better accuracy
- Create systems for which you **do not know the rules conscioulsy** (e.g. recognize a face)
    - Greater potential

## AI vs Machine Learning
- AI is a very fuzzy concept, much like "any computer program doing something useful"
    - Think "if-then" rules
- ML can be considered a **subfield of AI** since those algorithms can be seen as building blocks to make computers learn to behave more intelligently by somehow *generalizing* rather that just storing and retrieving data items like a database system would do
- *Engineering point of view*: ML is about builiding programs with *turnable parameters* (typically an array of floating point values) that are **adjusted automatically** so as to improve their behavior by **adapting to previously seen data**

![](https://i.imgur.com/uFNlTYR.png)

## Machine Learning vs Deep Learning
Traditional Machine Learning
![](https://i.imgur.com/ARU88yJ.png)

Deep Learning
![](https://i.imgur.com/23lFNOm.png)

## AI vs ML vs DL
DL $\subset$ ML $\subset$ AI
![](https://i.imgur.com/G5m0ihN.png)

## Exercise
Machine Learning Examples

Can you list examples of projects or products involving Machine Learning ?
- Google Lens

# Machine Learning Problem
## Why is learning difficult ?
Generalization is an ambiguous process.

Given a **finite** amount of **training data**, you have to derive a **relation** for an **infinite** domain.
In fact, there is an infinite number of such relations.

![](https://i.imgur.com/E2H7Vqq.png)

How should we draw the relation?
![](https://i.imgur.com/6i7kE3w.png)

Which relation is the most appropriate?
![](https://i.imgur.com/yoef59O.png)
...the hidden test points (seen after the training)...

## Learning bias
How to guide generalization

- It is always possible to find a model complex enough to fit all the examples
    - Example: polynomial with very high degree
- But how would this help us with new samples?
    - It should not generalize well.
- We need to define a family of acceptable solutions to search from
    - It forces to learn a “smoothed” representation.
    - ... but it should not smooth the representation too much!

<div class="alert alert-info" role="alert" markdown="1">
**Occam’s Principle of Parsimony** *(14th century)*
One should not increase, beyond what is necessary, the number of entities required to explain anything.
</div>

When many solutions are available for a given problem, we should select the simplest one.
But what do we mean by simple?
We will use prior knowledge of the problem to solve to define what is a simple solution.
> Example of a prior: smoothness

## Learning as a search problem
Hypothesis space / initial, compatible (with train set), optimal, and ideal solutions

What are the sources of error ?

### Noise, intrinsic error
Your data is not perfect (can have noisy or erroneous labels). (or “Every model is wrong.”) Even if there exist an optimal underlying model, the observations are corrupted by noise.

![](https://i.imgur.com/0znzEP8.png)

### (Inductive) bias, approximation error
We are exploring a restricted subset of all possible solutions. Your classifier needs to drop some information about the training set to have generalization power (simplify to generalize).
![](https://i.imgur.com/T0k5vWm.png)

### Variance, estimation error
You have many ways to explain your training dataset. It is hard to find an optimal solution among those many possibilities. Our exploration is not very accurate, we are limited by data we see during training.
![](https://i.imgur.com/294MgwX.png)


Bias / variance compromise
- Low bias $\Leftrightarrow$ high variance: large search set, can capture many useless details
    - overfitting
- High bias $\Leftrightarrow$ low variance: small search set, limited exploration, solution too simple
    - underfitting.
- Solutions: regularization (penalize solutions which are too complex), early stopping (stop when no more progress)...

![](https://i.imgur.com/5t9RqN0.png)

![](https://i.imgur.com/xgrMNWy.png)

## Parameters of a ML problem
Many variations for each element

- **Protocol**: supervision? feedback? how many samples for each “experience”?
- **Measure of success**: error cost? convergence? ...
- **Inputs** (representation space): quality (noise, distribution) and nature (numerical, symbolical, mixed)
- **Solutions** (space hypothesis/functions to explore): many approaches

## Three kinds of ML problems
According to Samy Bengio

### Regression
![](https://i.imgur.com/9gTFbLi.png)

Regression input: samples described by several input variables (correlated)
Regression output: a quantitative variable (scalar)
![](https://i.imgur.com/HlQKxro.png)


### Regression, classification
![](https://i.imgur.com/BdmXbiT.png)

Classification input: samples described by several input variables (correlated)
Classification output: a qualitative variable (class, category)

![](https://i.imgur.com/qfN99qz.png)

![](https://i.imgur.com/hrOyg36.png)


### Regression, classification, density estimation
![](https://i.imgur.com/EyhXQ4w.png)

Density estimation input: samples described by several input variables (correlated)
Density estimation output: estimate of the probability distribution function over
the feature space

![](https://i.imgur.com/zdy2E5T.png)


## Three kinds of supervision/trainings
According to Lecun, S. Bengio

- Supervised learning: Training data contains the desired behavior — desired class, outcome, etc
    - Medium feedback
- Reinforcement learning: Training data contains partial targets — Did the system do well or not? Is some object present in the image (without knowing is position)?
    - Weak feedback
- Unsupervised/Self-supervised learning: Training data is raw, no class or target is given.
    - There is often a hidden goal in the task: compression, maximum likelihood, predict parts from other parts (BERT-like)...
    - Lot of feedback

## Forms of Machine Learning
According to Cornuejols and Miclet

- Exploration-based: Generalization or specialization of rules
    - Examples: Grammatical inference, heuristic discovery for SAT solvers...
- Optimization-based: Topic of this course.
    - Examples: linear separators and SVMs, neural networks, decision trees, Bayesian networks, HMMs...
- Approximation-based: Data compression, analogy.
    - Examples: KNN, embedding spaces

# Machine Learning Engineering
## ML from an engineer point of view
Solve problems using the right tool

![](https://i.imgur.com/2vByGal.png)

## Some taxonomy
Simplified view of pre-2010 Machine Learning

![](https://i.imgur.com/aD8ibpM.png)


## Choosing the right tool
Why we love scikit-learn

![](https://i.imgur.com/D2SlFXo.png)


## Representing data
Why we love scikit-learn

![](https://i.imgur.com/QEnVIpe.png)



## Related domain
At the cross-roads of numerous fields

- Signal processing
- Databses, information retrieval
- Statistics
- Pattern Recognition
- Optimization
- Data science, data mining