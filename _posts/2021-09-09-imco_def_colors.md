---
title:          "IMCO: Defining colors"
date:           2021-09-09 10:00
categories:     [Image S9, IMCO]
tags:           [Image, S9, IMCO]
description: Defining colors
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/BysKxrvGY)

# Who Am I ?

Ricardo SAPAICO
- PhD in Computer Science, Tokyo Institute of Technology
- 10+ years of expereicne

## About DXO Labs

- ~18 years
- 50 people working in France

### Products

- DxO PhotoLab
    - LightRoom like
- DxO PureRaw
    - Smaller version of PhotoLab
    - Editing images quickly
    - EISA award
- Nik Collection by DxO
    - Plugin for Adobe
- DxO FilmPack

# Back to the course
## Why color matters ?

- Useful for quality inspection
    - Rely on color for a small object
    - Gives shape (shine color light on objects and create shadows)
- Cultural heritage
    - Paintings
    - If you take a picture of a painting, you want the photo to represents the painting well
    - Same for printing a copy of the painting
- Printing
- Computer graphics
    - Even tho not physical, you have to make sure you have the good colrs
- Photography
    - Sometimes, it's just a matter of doing the right thing to have a good picture
    - From color to B&W is not easy
    - Style Transfer IA on photography
    - Hyperspectral images

## Evaluation
- Attendance
    - Each class attended, you get $+0.5$
- Writtent report
    - Exercises using the data we will obtain during the TPs
    - A litlle bit of investigation for solving a typical color-related probleme in cameras
    - Group of 2 people
- Participation bonus: You can get up to $+2.0$ in your grade if:
    - You ask me technical question by mail
    - You ask technical questions in the IMCO group (Teams)
    - You reply a technical question in the IMCO group (Teams)

# Defining colors

![](https://i.imgur.com/1VAdDDP.png)
> White becomes pink with reflection

## What is (not) color

<div class="alert alert-info" role="alert" markdown="1">

- Color is NOT a property of an object
    - Once in the dark, no more color
    - Someone colorblind will see the color differently
- Color is NOT a particle
- Color is a sensation like touch
- Color is a sensation produced by a physical reality

</div>

> Grass is NOT green and sky is NOT blue,
> They are perceived as green and blue
> They have physical properties that makes them look that way

<div class="alert alert-danger" role="alert" markdown="1">
Color is in your HEAD
</div>

## How is color produced ?

![](https://i.imgur.com/vc3g59p.png)

- Sun: light
- Apple: object
- Human: sensor

## Electromagnetic spectrum

![](https://i.imgur.com/QRIMlej.png)

![](https://i.imgur.com/UYXKY9b.png)

*How can you see the black if it doesn't reflect any light ?*
> Because there is a shape (ex: a TV)
> Black isn't a color but we can perceive it

If we have a white surface and a red beam of light coming in, it would reflect the red.

# Object
## Surface and subsurface interaction with light

- specular 
- absorption 
- diffuse 
- transmittance 
- refraction 
- scattering

![](https://i.imgur.com/So1fhPa.png)
> To know of colors will work on this textile, you can only know it by printing hundreds of colors and extrapolate for the other ones

## Color is no 'part' of an object

- Dimension, shape, material (what it's made of), volume, density, porosity

# Sensor
## Human vision system

<div class="alert alert-info" role="alert" markdown="1">
**Reminder**
Refractive index:

$$
n=\frac{c}{\nu}
$$

</div>

![](https://i.imgur.com/FJLnR8v.png)

![](https://i.imgur.com/UgHS4ts.png)

- Cornea
    - The most significant image-forming element of the eye
    - Eye problemes, such as nearsightedness, farsightedness, astigmastism, can be attributed to it
- Lens
    - Serves the function of accomodation
    - It is layered, flexible structure that varies in index of refraction. This feature serves to reduce some of the aberrations
    - Distant object: it becomes "flatter" resulting in the decreased optical power
    - Nearby object: it becomes "fatter" thus has increased power
    - As we age, we lose flexibility. When we are about 50 years, the lens has completely lost its flexibility
- Iris + pupil
    - controls the pupil size
    - Pupil is the hole in the middle of the iris through which light passes. The pupil size is largely determined by the overall level of illumination
    - Pigmentation in the iris is what gives us *color*
- Retina
    - A thin layer of cells, approximately the thickness of tissue paper
    - Contains the visual system's photosensitive cells + initial signal processing and transmission "circuitry"
    - Photoreceptios: Rods and Cones
- Fovea
    - Area on the retina where we have the best spatial and color vision
- Optical nerve
    - Transfer info from the retina to the brain
    - 1 million fibers vs 130 million photoreceptors
        - There is a compression of the visual system
    - There are no photoreceptors where the nerve is
        - blind spot

### Rods and cones

Cones: useful to perceive color
Rods: useful in low-light

![](https://i.imgur.com/LU4ZjR2.png)

3 types of cones:
- Long
- Medium
- Short

<div class="alert alert-info" role="alert" markdown="1">
**Fun fact**
Most mammals have only blue and green cones, only primates have red
</div>

![](https://i.imgur.com/Zlgp18Y.png)

## Color matching experiment

![](https://i.imgur.com78WD7c.png)

> The observer adjusts the intensity of the primary colors until the results matches the test
> This test was like 100 years ago

![](https://i.imgur.com/uffOJSV.jpg)
> Chromaticity diagram

<div class="alert alert-info" role="alert" markdown="1">
**Spectrum Locus**
Chromaticity of monochromatic light at specified wavelength
</div>

## Spatial properties of Color Vision

In JPEG we have an image divided in luminance and chromatic information. Our eyes are less sensitive to chromatic infos, so JPEG subsamples then reconstructs the image

![](https://i.imgur.com/BcFFcjk.jpg)

# How to (re)produce color ?

- Additive process (RGB)
    - Light mixing
- Substractive process (CMY)
    - Used in printing
    - Paint mixing

## Color framework

![](https://i.imgur.com/Ta5TMvk.png)

![](https://i.imgur.com/LjECToz.png)

# Bonus
## Facts about animals

- Most fish, frogs and turtle and 3 to 5 cones
- Most mammals have retinas where rods predominate
    - *Is it because the Earth was dark when first mammals appeared ?*
- Nocturnal mammals like rats and mice have retinas dominated by rods (only 3 to 5% of cones)
- Snakes can see ultraviolet light

![](https://i.imgur.com/BqT2BZu.png)
*Why the eyes reflect the light ?*
> In the eyes, there are epithelial cells

<div class="alert alert-info" role="alert" markdown="1">
**Epithelial cells**
Prevents light from going back to the retina $\to$ keeps the sharpness and contrast
</div>

Nocturnal animals exchange image quality for image power. Their cells reflects the light back $\to$ the photoreceptors have a second chance to absorb energy

<div class="alert alert-warning" role="alert" markdown="1">
:warning: Different than having red eyes !
</div>

### Structural color: Iridiscence

![](https://i.imgur.com/0vbQ0mN.jpg)

Used for camouflage

## Facts about humans

- Red-green color blindness
    - $8\%$ males (XY chromosome)
    - $0.5\%$ females (XX chromosome)

of northern European descent

Around $12\%$ of the female population could be tetrachromatic

## To think over

- What is fluorescence ?
- Why a banana stays yellow under 2 different light sources ?