---
title:          "IMCO: Processing Color"
date:           2021-09-16 14:00
categories:     [Image S9, IMCO]
tags:           [Image, S9, IMCO]
math: true
description: Processing Color
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/rkBS7nl7F)

# How a camera works
## Human Eye vs a Camera

![](https://i.imgur.com/ZcLJrBY.png)

![](https://i.imgur.com/80uyhIo.jpg)

- Shutter: how long the camera is opened to let in light

## The imaging flow

![](https://i.imgur.com/IXzuXmc.png)

<div class="alert alert-warning" role="alert" markdown="1">
The camera pipeline for creating nice photos is a **secret recipe**
</div>

![](https://i.imgur.com/h1ZXocb.jpg)

## The color Imaging Flow

![](https://i.imgur.com/CoQ1rAh.png)
> [Source](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.11.77&rep=rep1&type=pdf)

Other possible steps:
- ISO Gain
- Noise Reduction
- Etc.

## Sensor

- Temporal Mutliplexing
    - Scan 3 times + use 1 sensor
    - 3 real values per pixel
    - Only for static scenes
    - Slow
- Scan 1 time + Use 3 sensors
    - 3 real values per pixel
    - Costly
    - Space
- Spatial Multiplexing
    - Scan 1 times + Use 1 sensor
    - Well-mastered technology
    - 1 real value per pixel (interpolation)
    - Loss of light

## Camera spectral sensitivity

![](https://i.imgur.com/YmBzcCr.png)
> [Source](http://www.gujinwei.org/research/camspec/)

## Sensor (from 110 years ago!)

Using temporal multiplexing

# Preprocessing

![](https://i.imgur.com/J5n438J.png)

- Dark Current Compensation
    - Signal present even when the length is close, which adds noise

*How to compensate ?*
> Capture a dark image for the given exposure time

$$
C_i(x,y)=R_i(x,y) - D_i(x,y)
$$

- Vignetting/Lens Shading/Flat Field correction
    - Image tends to darken on the corners/Non-uniform Illumination

*How to compensate ?*
> You tell me !

![](https://i.imgur.com/r3r3fdQ.png)

> Compute average RGB value of 15 White Patches

||Statistic|Red|Green|Blue|
|-|-|-|-|-|
| Before correction| Mean| 157.3|159.1|157.5|
|After correction|Mean|249.5|\ | \ |

<div class="alert alert-success" role="alert" markdown="1">
If you are taking RAW images there is a chance your image software already does it
</div>

# Color Constancy

<div class="alert alert-info" role="alert" markdown="1">
Property of the Human Visual Sytem that allows adapting to different scene illuminations
</div>

![](https://i.imgur.com/k9BTUxE.png)

## White Balance to the rescue

<div class="alert alert-info" role="alert" markdown="1">
The eye cares more about the intrinsic color of the object, not the color of the light leaving the object
</div>

- Easy for our eyes to judge what is white under different illuminants, but not so straightforward to camera

# White Balance

<div class="alert alert-info" role="alert" markdown="1">
The idea is to make white points the same between scenes
</div>

![](https://i.imgur.com/GXmaCh7.png)

White point is the $xyY$ (or $XYZ$) value of an ideal "white reference"

![](https://i.imgur.com/VpVbm9v.png)

<div class="alert alert-success" role="alert" markdown="1">
Hence, the camera is able to do the *Chromatic Adaptation*
</div>

## Chromatic Adaptation: How ?

- $\color{yellow}{\text{Source}}$ color
    - $(X_s, Y_s, Z_s)$ with white reference $(X_{WS}, Y_{WS}, Z_{WS})$
- $\color{blue}{Target}$ color
    - $(X_T,Y_T,Z_T)$ with white reference $(X_{WT}, Y_{WT}, Z_{WT})$

Computing $[M]$
1. Transform $XYZ$ to cone response domain
2. Scale using source/target white references
3. Transform back form cone domain $XYZ$

$$
[M] = [MA]^{-1}\begin{bmatrix}
\frac{\rho_T}{\rho_S}&0&0\\
0&\frac{\gamma_T}{\gamma_S}&0\\
0&0&\frac{\beta_t}{\beta_s}
\end{bmatrix} [MA]
$$

Where $\rho, \gamma,\beta$ are the cone responses for the given source and target colors

### Example

![](https://i.imgur.com/puiMaEP.png)

## White balance: automatic

*What if we don't help the camera ?*
> The camera doesn't know the illuminant

The camera will try to "guess" the white point in the image, and then balance the color automatically.

<div class="alert alert-warning" role="alert" markdown="1">
Unlike White Balance, the illuminant is very hard to estimate
</div>

### How ?

- Gray world assumption
    - The average of all colors in the image is gray
    - Green channel is taken as "gray" reference
    - White-balanced image is: $k_{r}R,G,k_bB$
        - $k_r=\frac{G_{mean}}{R_{mean}}$
        - $k_b = \frac{G_{mean}}{B_{mean}}$
-  White patch algorithm
    -  Assumes that highlights = specular reflections of illuminant
    -  Maximum $R,G,B$ values are good estimation of white point
    - White balanced image is: $k_{r}R,G,k_bB$
        - $k_r=\frac{G_{max}}{R_{max}}$
        - $k_b = \frac{G_{max}}{B_{max}}$
- *How does GIMP does it ?*
    1. Discards pixels colors at the extremes of $R,G,B$ histograms
        - Thresholds of $0.05\%$ of total pixel count
    2. Do Histogram Stretching of remaining pixel colors, for each channel
    3. Plus some smart post-processing
- Smart Color Balance method
    1. Discards "black" and "white" pixels
    2. Stretch the histogram of the remaining pixels
    3. Plus some smart post-processing

<div class="alert alert-warning" role="alert" markdown="1">
Those are very basic algorithms.
</div>

Modern cameras use sophisticated white-balance, based on data-driven solutions
- One Way
    - Compute features from image
    - Find similar images in databases of images with good white balance
    - Use white balance from image

# Demosaic

- Each pixel has a different color filter
- Bayer Pattern is the most used Color Filter Array (CFA)
- Why More Green ?
    - Frequency of the G color band is close to the peak of the human luminance frequency response $\to$ better sharpness

## Linear interpolation

![](https://i.imgur.com/kTz8wFd.png)
- Average of neighors
- Smoother kernels (bicubic) can also be used

## Typical error

Taking a picture of striped pattern $\to$ color artifact

<div class="alert alert-success" role="alert" markdown="1">
To overcome these problems, most demosaicing methods convert the image to the YCbCr
</div>

## Solution

- Each pixel has a different color filter
- Bayer Pattern is the moste used Color Filter Array (CFA)
- Interpolation methods are patented or proprietary
- And of course deep learning to the rescue

![](https://i.imgur.com/loSktkw.png)

# Color Transform $RGB_c\to RGB_u$

## Color Correction

- Cameras are meant to produce pleasing scenes rather than colorimetrically accurate scenes
    - Spectral Sensitivities of the camera are not identical to human color matching functions
- To obtain colorimetric accuracy, we need to transform the image from the sensor's color space to the colorimetrics $(XYZ)$ space
- By default Factory-computed Color Space Transforms (CST) are used
- When precision is needed, Color Charts are used to obtain a specific transform for the camera and scene

<div class="alert alert-success" role="alert" markdown="1">
We can use ICC color profile
</div>

## Color Correction Charts

*ColorChecker Digital SG* (SG=Semi-gloss)
![](https://i.imgur.com/PkFsrVV.png)
- 140 patches (96 uniques colors)

*Artist Paint Target*
![](https://i.imgur.com/GqZACDz.png)

*ColorBuild 300 Patch Target*
![](https://i.imgur.com/TPCJYyg.png)

## Color Correction Methods

- $30+$ years of continous research on how to transform form RGB to XYZ spaces
    - A lot of ways to do it !
- Most of them solve the following equation:

$$
X=MP
$$
- $X$: Reference $XYZ$ values $[3\times m]$
- $P$: Camera $RGB$ values $[N\times m]$
- $M$: Correction matrix $[3\times N]$
- $m$: nb of data points
- $N$: nb of dimensions

||ColorChecker Classic|ColorChecker Digital SG|
|-|-|-|
|m|24|140|

### Linear

Linear Mapping from $RGB$ to $XYZ$
- $N=3$
- Not affected by exposure change

### Polynomial Color Correction

Linear Mapping From $RGB$ to $XYZ$ + add polynomial components to reduce errors
- $N=9$, if $2^{nd}$ order polynomial
- Affected by exposure changes
- High polynomial degree tends to do overfitting

### Root Polynomial Color Correction

Linear Mapping from $RGB$ to $XYZ$ + add root polynomial components
- $N=6$, if $2^{nd}$ Order Polynomial
- Not affected by exposure change

# Measuring with RGB Cameras: Recap

- Cameras ar *not* light measurement devices
- From the moment an image is captured by the sensor, there are a lot of steps which could impact the final color rendition. This processing is proprietary

# Future trends ?

## White balance: Mixed illumination

<div class="alert alert-warning" role="alert" markdown="1">
The white balance fails if 2 illuminants are in the same image
</div>

## Denoising

Best current solutions use Deep Learning
- Predict the noise instead of denoising the image

## HDR Imaging

- HDR Imaging is quite mature
- Some challenges when acquiring moving scenes or shooting a video
- HDR from a single image using Deep Learning ?

## Multispectral Imaging

- Used mostly for quality inspection and classification of materials
- In principle, it could be used for measuring Reflectance

## Spectra from RGB

- When measuring color with an RGB camera, we measure the ligth response in 3 wavelengths
