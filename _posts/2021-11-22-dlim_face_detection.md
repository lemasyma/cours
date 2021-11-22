---
title:          "DLIM: Face detection"
date:           2021-11-22 14:00
categories:     [Image S9, DLIM]
tags:           [Image, S9, DLIM]
math: true
---

Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/rksnLMt_F)

# Face detection in general

*Why is facre detection so difficult ?*
> Pose (*Out-of-Plane Rotation*) and orientation (*In-Plane Rotation*)
> Presence or absence of structural components
> Occlusions
> Imaging conditions
> Faces are highly non-rigid object (*deformations*)

## Related problems

- Face localization
- Facial feature extraction (landmarks such as eyes, mouth, ...)
- Face recognition
- Verification
- Facial expression

# Overview of different approaches:

1. Knowledge top-down *base method*
2. Feature invariant methods (localization)
3. Template-matching methods (localization)
4. Appearance-based methods (detection)

## Apparence-based methods **in details**

- Eigenfaces
- Distribution-based methods
- Support Vector Machines (SVM)
- Sparse Network of Winnows
- Naive Bayes Classifier
- Hidden Markov models

![](https://i.imgur.com/vy81DNW.png)

- Information Theoretic Approaches (ITA)
- Inductive Learning (C4.5 and Find-S algorithms)
- Artficial Neural Networks (ANN) techniques
    - Shallow networks (inverse de Deep)
    - Deep learning

![](https://i.imgur.com/Kzwwlwo.png)

Les connections residuelles permettent de faire une retropropagation beaucoup plus loin que le reste du reseau.

<div class="alert alert-warning" role="alert" markdown="1">
Le gros defaut des VGG: ils ont **enormement** de poids
</div>

> poids $=$ parametres $\neq$ hyperparametres

![](https://i.imgur.com/0AF2tEV.png)

Il y a de moins en moins de neurones en \%.

<div class="alert alert-danger" role="alert" markdown="1">
Plus on a de poids, plus on a de chance que notre reseau soit puissant mais plus on a de chance qu'une partie serve a rien.
</div>

# The beginning in 1994

<div class="alert alert-info" role="alert" markdown="1">
Burel et Carel proposent une methodologie pour les ANN's:

1. La phase d'entrainement ou un systeme *tunes* les parametres internes
2. La phase d'entrainement local ou le systeme adapte les poids specifiques a l'environnement d'un site local
3. La phase de detection durant laquelle **les poids ne bougent pas**

</div>

Vaillant, Montcoq et Le Cun: first translation invariant ANN, decides if each pixel belong or not to a given object

Yang et Huang: first fully automatic human face recoginition system

## 1997

<div class="alert alert-info" role="alert" markdown="1">
Rowleu, Baluja, Kanade propose the first rotation-invariant method:
- Uses template-based approach
- Methodology:
    - Regions are proposed
    - A router network estimates the orientation of this region
    - This network prepares the windows using this angle
    - A detector network decides if the window contains a face

![](https://i.imgur.com/rWhIs2L.png)

</div>

## 2004

<div class="alert alert-info" role="alert" markdown="1">
First real-time face detection algo by Viola & Jones
</div>

- Tells if a given image of arbitrary size contains a human face, and if so, where it is
- Minimizes false positive and false negative rates
- Usually 5 types of Haar-like features

![](https://i.imgur.com/DuYfZWB.png)


- $24\times 24$ image contains **a huge number of features** ($162886$)
- Integral image for feature computation

![](https://i.imgur.com/vRsIdvf.png)

- $A=1$, $B=2$, $C=3$, etc.

<div class="alert alert-success" role="alert" markdown="1">
Allows a low computational cost of features
</div>

<div class="alert alert-info" role="alert" markdown="1">
**Principle**

> The algorithm should deploy more resources to work on those windows more likely to contain
a face while spending as little effort as possible on the rest

</div>

- We can use *weak classifiers*
- Then we can mae a strong one with a sequence of weak ones
- Viola & Jones: use AdaBoost

![](https://i.imgur.com/g4sPVPF.png)

The more layers, the less false positive:

![](https://i.imgur.com/kqlK5x2.png)

![](https://i.imgur.com/OPqvcQy.png)

# Overfeat (2014)

<div class="alert alert-info" role="alert" markdown="1">

- Winner of the ImageNet Large Scale Visual Recognition Challenger of 2013
- Makes at the sae time classification (blocks), localization (grouping blocks) and detection (merge windows)
- This multitask approach boosts the performance of the network
- Trained on ImageNEt 2012

</div>

- Inspired for multi-viewing voting
- Uses multiscale factor of 1.4
- Using a dense sliding windows thanks to convolution

> The better aligned the network window and the object, the strongest the confidence of the
network response.

- Efficiency: convolution computations in overlapping regions are *shared*
- Bounding boxes are accumulated instead of suppressed
- Only *one shared network for 3 functionalities*
- Uses a *feature extractor* for classification purpose
- Use *offset to refine the resolution of the proposed windows*
- Detection fine-tuning: negative training on the fly

## Methodology

- decomposition into blocks with 3 offsets
- for each block, estimation of the most probable corresponding class
- (overlapping) region proposals for each class (see below)
- bounding box deduction for each class (see below)

![](https://i.imgur.com/g6BS6RD.png)

![](https://i.imgur.com/q9SZ6Rv.png)

![](https://i.imgur.com/2Bdxt6e.png)

![](https://i.imgur.com/LbgeFtC.png)

![](https://i.imgur.com/3qVcyge.png)

# The MTCNN face detection algorithm (2016)

## Zhang, Zhang & Li

- Real-time deep-learning-based face detection algorithm
- The MTCNN is a cascade of 3 similar networks (P/R/O-nets)
- The four steps:
    1. Computation of the (multiscale) image pyramid
    2. P-nEt: propositional network
    3. R-net: refinement net (filters and refines the results of the P-Net)
    4. O-net: output network (still refines, and propose landmarks)

![](https://i.imgur.com/gbmBdst.png)

- Use **hard sample mining** (the $30\%$ easier cases fo not intervene in the retropropagation) to improve the detection results
- Originality: uses *multi-task* learning, that is, every network
    - predict bounding boxes
    - use regression to refine/calibrate the position of the edges of the bounding box
    - applies Non-Maxmal Suppression (NMS) to keep only relevant candidate windows (merge of highly overlapped candidates)
    - (can) propose 5 facial landmarks
- This multi-task seems to improve face detection compared to usual mono-task learning
- How does it work in pratice? It minimizes:

$$
Loss=$\alpha_1\times L_{detection} + \alpha_2\times L_{regression} + \alpha_3\times L_{landmarks}$
$$

where the first is based on cross-entropy, and the others are based on Euclidian loss

![](https://i.imgur.com/ntCzVfd.png)

# Fast R-CNN and its predecessors (2014-2015)

## Spatial-Pyramid Pool network (2014)

- Have been proposed to speed up R-CNN by sharing computation,
- The SPPnet computes a shared feature map using convolutions over the entire image, and only then extract features corresponding to each proposal to make the prediction,
- Then it concatenates the features of the proposal coming from each scale thanks to MaxPooling to a $6 \times 6 \times$ scales map (spatial pyramid).
- SPP-nets accelerates R-CNN by 10 to 100 times at test times and by 3 at training time.
- Drawback 1: Like the R-CNN, it is a multi-stage approach:
    - First, feature extraction using convolution,
    - Second, fine-tuning of a network using log loss,
    - Third, SVM training,
    - Fourth, fitting bounding-box regressors.
- Drawback 2: Features are written to disk,
- The fine-tuning cannot update the convolutional layers that precede the spatial pyramid pooling (limited accuracy).

## Fast R-CNN0 (2015)

<div class="alert alert-info" role="alert" markdown="1">
a Fast Region-based Convolutional Network method,
</div>

- Mainly made of several innovation to make is faster
- Uses Singular Value Decomposition (SVD) truncation to fasten the computations,
- Uses a multi-task loss to train all the network in one single stage (it jointly learns to classify objects proposals (windows) and refine their spatial locations),
- Trains the VGG16 9 times faster than the RCNN and 3 times faster than the SPP-nets,
- Is able to retropropagate the error in the convolutional layers (contrary to SPPnets and RCNN) and then increases the accuracy,
- No disk storage is required for feature caching.

![](https://i.imgur.com/GSOTYDB.png)

![](https://i.imgur.com/d7Vkumr.png)

# Faster R-CNN (2016)

<div class="alert alert-info" role="alert" markdown="1">
- Usual object detection methods depended on (slow) region proposal algorithms,
- They got the original idea to use ANN’s to do these predictions on GPU (much faster),
- They called this technology Region Proposal Networks (RPNs).
</div>

## Properties

- is just made of several convolutional layers applied on the feature maps,
- It is then a fully convolutional layer (weights are shared in space),
- It is then translation-invariant in space (contrary to MultiBox method),
- it can be seen as a mini-network with a sliding-window applied on the feature map to predict proposals,
- predicts at the same time proposals using regression and objectness scores,
- is able to predict proposals with a wide range of scales and aspect ratios (bye default, 3 and 3 respectively).

<div class="alert alert-success" role="alert" markdown="1">
Since the Fast R-CNN does not have region proposal, they added their RPN before the Fast-RCNN to obtain the Faster R-CNN,
</div>

- The RPN is then an **attention network** since it tells to the Fast R-CNN where to look
- Since the efficiency of the Fast R-CNN depends on the region proposals, better proposal thanks to the RPN implies a better accuracy of the Faster R-CNN,
- To ensure that features used between the RPN and the Fast R-CNN are the same, they shared the weights of the Feature Extractor between them (faster, more accurate).
- It took then 10 milliseconds to compute the predictions of the RPN.

![](https://i.imgur.com/zoZ9vtf.png)

# Mask R-CNN (2018)

<div class="alert alert-info" role="alert" markdown="1">
Extension of Faster R-CNN
</div>


<div class="alert alert-danger" role="alert" markdown="1">
aim is **instance segmentation**
</div>

Has 3 outputs/prediction
1. the usual bounding box predictions (from Faster R-CNN),
2. the usual classification predictions (still from Faster R-CNN),
3. the mask predictions (A small FCN applied to each RoI – NEW !!),

*No competition* is done among classes prediction
- Mask prediction is done *in parallel*
- The training is done with a multi-task loss:

$$
Loss = \alpha_1L_{class} + \alpha_2L_{reg}+\alpha_3L_{mask}
$$

- We can easily change the backbone (feature extractor)
- It runs a 5 fps

![](https://i.imgur.com/BRmLTQK.png)

![](https://i.imgur.com/1xomgWc.png)

![](https://i.imgur.com/VXdyxTt.png)

# R-FCN Architectures (2016)

<div class="alert alert-info" role="alert" markdown="1">
Region-based Fully Convolutional Networks
</div>

- 2-stage object detection strategy
- Every layer is convolutional, whatever its role
- Almost all the computations are shared on the entire image
- Rols (candidate regions) are extracted to a Region Proposal Network (RPN)
- Uses position-sensitive score maps

![](https://i.imgur.com/MkSJ4sw.png)

![](https://i.imgur.com/EoDV021.png)

![](https://i.imgur.com/GwQyIok.png)

On decale la fenetre sur la droite:

![](https://i.imgur.com/zfNAKy8.png)

> At top-middle probability map, the white pixels correspond to the probability that a head 

# RetinaNet (2018)

- One-stage detector
- Uses an *innovative focal loss*
- Naturally handles *class imbalance*
- Uses a **Feature Pyramid Network** (FPN) backbone of ResNet architecture
- Then it provides a *rich* multi-scale feature pyramid (efficiency)
- At each scale, they attach *subnetworks* to classify and make regressions

![](https://i.imgur.com/Urr3Vbx.png)

# Detectrons (2018-2019)

## Detectron V1 2018 (Facebook)

![](https://i.imgur.com/Hwu5RhV.png)

## Detectron  V2 (Facebook)

![](https://i.imgur.com/GqBOC9W.png)

![](https://i.imgur.com/EEB6f2K.png)

![](https://i.imgur.com/cblq1WV.png)

# Real-time detection algorithms

## YOLO (You Only Look Once) (2016)

- single-shot detection architecture
    - Designed for real-time applications
    - It does NOT predict regions of interests
    - It predicts a fixed amount of detections on the image directly,
    - They are then filtered to contain only the actual detections.
- faster than region-based architectures
- lower detection accuracy
- performs a multi-box bounding box regression on the input image directly
- Method: the image is overlayed by a grid, and for each grid cell, a fixed amount of detections are predicted.
    
![](https://i.imgur.com/Np8qiEY.png)

## SSD (Single Shot Multibox Detector) (2016)

- Is a single-shot detection architecture
- Instead of performing bounding box regression on the final layer like YOLO, SSDs append additional convolutional layers that gradually decrease in size.
- For each additional layer, a fixed amount of predictions with diverse aspect ratios are computed,
- It results in a large number of predictions that differ heavily across size and aspect ratio.

![](https://i.imgur.com/ZQIztkw.png)

## YOLOv2 (YOLO 9000) (2016)

- Extension of YOLOv1
- Ability to predict objects at different resolutions,
- Computes the first bounding box predictions using clustering,
- Better performance than SSD.