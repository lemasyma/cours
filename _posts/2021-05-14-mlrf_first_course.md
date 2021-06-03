---
title:          "MLRF: Lecture 01"
date:           2021-05-14 10:00
categories:     [Image S8, MLRF]
tags:           [Image, SCIA, MLRF, S8]
description: Lecture 01
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/S1nCkhs_O)

# Scope of this course

> Apply Machine Learning (ML) techniques to solve some practical Computer Vision (CV) problems

- About **Computer Vision** (CV)
- It should be called CV-ML, ML4CV or so...

We need some definitions:
- What is *Computer Vision* ? What is *Pattern Recognition* ? *Shape Recognition* ?
- What is *Machine Learning* ?
- How do those concepts relate together ?

# Agenda for lecture 1
1. Some definitions and basic notions
2. Course outline
3. Introduction to *Twin it !*
4. Pattern Matching

# Some definitions
## Computer Vision

<div class="alert alert-info" role="alert" markdown="1">
**Definition**
The automation of visual tasks with the goal of producing results directly or indirectly usable by humans
</div>
- **Input**: image(s) in machine format (image acquisition of a subpart of CV)
- **Output**: some pieces

### Exemple

<div class="alert alert-warning" role="alert" markdown="1">
How would you process image pixels to get those results ?
</div>

![](https://i.imgur.com/2BF45t3.png)

> Les photos de chats sur Internet c'est important

![](https://i.imgur.com/ynVQQe7.png)

![](https://i.imgur.com/XsmFBiR.png)

- Some applications are direct (like the insect recognition app):
    - a human reads and uses the output
- Some applications are indirect (like bank checking reading)
    - The output is fed to a business system
- Some applications extend what humans can naturally do
    - Either by extending our range

## Pattern Recognition

<div class="alert alert-info" role="alert" markdown="1">
**Definition**
The field of a pattern recognition is concerned with the automatic discovery of regularities in data through the use of computer algorithms and with the use of these regularities to take action such as *classifying* the data into different categories
> Bishop, 2006
</div>

IAPR: **pattern recognition**, **computer vision** and **image processing** in a broad sense

### Examples
- OCR
    - Computer vision
- Pedestrian detection
    - Computer Vision
- Credit fraud detection
    - Not computer vision

$\Rightarrow$ CV$\cap$PR$\neq\emptyset$

### Pattern Recognition is an *inverse* problem

> OCR example - Why Pattern Recognition is hard

![](https://i.imgur.com/ETm4YMn.png)

## "Shapes"

<div class="alert alert-info" role="alert" markdown="1">
**Definition**
A way to designate meaningful visual patterns.
</div>

Sometimes used to describe "visual percepts"

*Let S and S' be 2 shapes observed in 2 different images which happen to be similar.*

![](https://i.imgur.com/mo3c7OJ.png)

![](https://i.imgur.comL14MCD.png)

<div class="alert alert-warning" role="alert" markdown="1">
Some **statistics** can help us making better decisions...

Idea: **learn** the distance threshold under which shapes can be deemed identical
</div>

## Machine Learning
### Many forms of Machine Learning

- Focus on **inductive learning** (generalize from examples)
- We will consider both **supervised** (a "teacher" provides labels for examples) and **unsupervised** (only samples)
- Focus on **optimization-based learning techniques** (examples are represented as numerical vectors)

## Examples of optimization-based learning techniques
- Linear classifiers, SVMs
- Neural networks

## ("Statistical") Machine Learning

> Learning means **changing** in order to be **better** (according to a given **criterion**) when a similar situation arrives
> Learning **IS NOT** learning by heart
> Any computer can learn by heart, the difficulty is to **generalize** a behavior to a novel situation
> *Quoting S. Bengio*

### From an engineer's POV

> Machin Learning is about building programs with **tunable parameters** (typicalyy an array of floating point values) that are **adjusted automatically** so as to improve their behavior by **adapting to previously seen data**.
> Machine Learning can be considered *a subfield of AI* since those algorithms can be seen as building blocks to make computer learn
> *Scikit Learn Documentation*

# Why is learning difficult ?

Given a **finite amount of training data**, you have to derive a **relation for an infinite domain**.
In fact, there is an **infinite** number of such relations

![](https://i.imgur.com/aS55m47.png)

*Which relation is the most appropriate ?*

![](https://i.imgur.com/CSf1D5v.png)

... **the hidden test points**...

## Learning bias
It is **always** possible to find a model **complex enough** to fit **all** the examples
But how would this help us with **new samples** ? It should not **generalize** well.
We need to define a **family of acceptable solutions to search from**. It forces to learn a "smoothed" representation

### So in practice we need
- Examples (data!)
- A tunable algorithm (model)
- A evalutation of the model fitness to examples (risk, loss)
- A definition of the model search space (not too big, not too small)
- An optimization strategy

<div class="alert alert-success" role="alert" markdown="1">
**The bias/variance compromise**
Small search space:
- Easier to find the best (available) solution
- But it may be far from the ideal one

Large search space:
- It is hard to find the best (available) solution
</div>

## 3 kinds of problems
### Regression

![](https://i.imgur.com/CGxxpbw.png)

$$
x=\underbrace{\begin{pmatrix} \vdots \end{pmatrix}}_{\in\mathbb R^T}\\
y=\underbrace{\begin{pmatrix} \vdots \end{pmatrix}}_{\in\mathbb R^5}
$$

### Classification
![](https://i.imgur.com/XF0PQrn.png)

$$
x=\mathbb R^5\\
y=\mathbb R^T
$$

### Density estimation

![](https://i.imgur.com/0hxsLDl.png)

$$
x\in\mathbb R^5\\
\mathbb P(x)\in[0,1]
$$

![](https://i.imgur.com/MXb6dFE.png)

## 3 types of learning
- **Supervised** learning $(x,y)$
    - The training contains the desired behavior (desired class, outcome, etc.)
- **Reinforcement** learning $(x,\tilde y)$
    - The training data contains partial targets (for instance, simply whether the machines did well or not)
- **Unsupervised** learning
    - The training data is raw, no class or target is given
    - There is often a hidden goal in that task (compression, maximum likelihood, etc.)

![](https://i.imgur.com/crL8H8G.png)

## Model validation
![](https://i.imgur.com/bu3yFhU.png)

More on that later

1. You need to **test the generalization** power of your approach
2. So you need data not seen during the training: **a test set**
3. For which you know the **expected output** ("ground-truth", "gold standard", "target",...)

# Benefits of ML
## A duck example

How to filter the grass to keep only the duckshape, using threshold domain ?

![](https://i.imgur.com/kXq8hDI.png)

## Why using Machine Learning in computer Vision ?

To avoid knob turning. It's complex. It's unsafe

## But beware of the Machine Learning Magic

![](https://i.imgur.com/45IlSIH.png)

# Actual goals of this course
- Teach you that you can (and should whenever possible) **optimize the parameters** of your CV/PR product
- Show some **simple tools** to try to do it
- Address practical problem
    - describe a pattern
    - look for a pattern
    - match a pattern
    - classify a pattern
    - describe a set of patterns (an object/an image)
    - retrieve an object given a query, segment objects...
    - and face the unavoidable work surrounding them

# Course agenda
6 "weeks" (Friday to Friday)
See the [web page](https://www.lrde.epita.fr/~jchazalo/teaching/MLRF/202105_IMAGE_SCIA_S8/) for complete agenda
Weekly tests + assignments (practice sessions). **No final exam**

Weekly wokflow should be:
- **Friday, 09:30-10:00**: answer the weekly quiz on Moodle (*starting next Friday*)
- **Friday, 10:00-12:00**: attend the lecture using Teams
- **Friday, 14:00-17:00**: Work on the practice session and join the discussion using Teams
- **Before next Friday**: Complete the assignement and submit your results using Moodle (*for sessions 4, 5 and 6 only*)

# No deep learning !
- We need a course about basic techniques
- There are cases where setting up

# Pratice sessions: setup your dev. env.

Basically: Python with:
- Jupyter
- Numpy
- Matplotlin
- Scikit-image: RGB
- Scikit-learn
- OpenCV: BGR

# Why I love Scikit-Learn
## Numpy-friendly

![](https://i.imgur.com/TjB9l0u.png)

## 3-way documentation: User guide, API ref, Examples

![](https://i.imgur.com/2y3Kv0w.png)

## Super smart API
> Decomposition, level of detail, default values, consistency, etc

![](https://i.imgur.com/4B3UHFG.png)

![](https://i.imgur.com/VrAfggf.png)

# Introduction to *Twin it!*
## Overview
A poster game
- $X$ bubbles, all different but
- $Y$ bubbles, which have 1 (and only 1) twin

![](https://i.imgur.com/C21NkuT.jpg)


Your goals:
- Find the pairs

<div class="alert alert-success" role="alert" markdown="1">
Discussion (3 minutes):
1. How can we *decompose* the problem ?
2. How can we make *sure* our solution works ?
3. What should we *focus* on ?
</div>

Already done:
- Scan the poster
- Stitch the tiles
- Normalize the contrast

## Undelying problems
1. Isolate each bubble $\Rightarrow$ **Segmentation** ![](https://i.imgur.com/0zamne3.png)
    - We provide pre-computed results for this step
3. Compare image pairs $\Rightarrow$ **Matching** ![](https://i.imgur.com/LsR95M7.png)
    - We will focus on this one
    - We will use **Template Matching**
5. Identify pairs $\Rightarrow$ **Calibration** ![](https://i.imgur.com/3OrDVtM.png)

# Template matching
## Why template matching ?
A simple method which will be useful to understand
- Evaluation challenges
- The ideas behind keypoint detection (next lecture)

It can work on the Twin it! case
- Twice the same texture
- Textures are the **same scale**, without **rotation** nor **intensity change**
- Only need to cope with **translation** (and some **small noise**)

## Step by step: Compare 2 images
- 2 arrays of intensities ![](https://i.imgur.com/lTZgevq.png)
- Take the **absolute** difference

![](https://i.imgur.com/htN1gEO.png)

$$
R(x,y) = \vert I_1(x,y) - I_2(x,y)\vert
$$

- Sum the differences

![](https://i.imgur.com/lKTscKz.png)


$$
S=\sum_{x,y}(I_1(x,y) - I_2(x,y))^2
$$

(Opt.) Normalize so the results belongs to $[0,1]$

![](https://i.imgur.com/grXMn0J.png)


## Template Matching: Sliding comparison

- $I_1$ is a small template $T$ to match against $I_2$ (just $I$ after)
- We rewrite the preceding formula to compute a map $R$ of the shape of $I$
- Each pixel of $R$ will have the value of the SSD when the top-left pixel of $T$ in on the pixel $(x,y)$ of $I$

![](https://i.imgur.com/gWIgF8y.png)

## Several approaches $\Leftrightarrow$ Practice session

![](https://i.imgur.com/j8ByvfZ.png)


## About the denominator

![](https://i.imgur.com/rP4p1E2.png)

## Cross correlation: 2 things to know

![](https://i.imgur.com/R84XmMS.png)

**More robust to intensity shift**

## Ideal goal

For each bubble, retunr only a mathcin pair, if it exists

![](https://i.imgur.com/c8Cbgao.png)
