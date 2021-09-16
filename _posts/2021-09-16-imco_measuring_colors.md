---
title:          "IMCO: Measuring Color"
date:           2021-09-16 10:00
categories:     [Image S9, IMCO]
tags:           [Image, S9, IMCO]
description: Measuring Color
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/r1Bb5OxXt)

# Video time

[Konica Minolta Sensing](https://youtu.be/C7etwDKApm8)

# How can we measure colors ?

- Spectrophotometer
    - Response through the entire visible spectrum
    - Relatively small areas (few $cm^2$) - Resolution is 1 point
    - "Falt surfaces"
- RGB Camera
    - Response in 3 wavelengths (Red, Green Blue)
    - Large areas - High Spatial Resolution ($\lt50$MPixels)
    - Any kind of surfaces
- Hyperspectral camera
    - Response throughout the entier visible spectrum (and more)
    - Large areas - Low Spatial Resolution ($\le2$MPixels)
    - Any kind of surfaces

# When NOT to Measure color

- Using instrument to measure color and compute differences objectively is not always needed
- For example: A company has a corporate color (possible $^{TM}$)
    - Tour de France: Pantone 123C
    - Veuve Cliequot: Pantone 137C
    - Louboutin: Pantone 18.1663TP
- Products carrying the color are sold; however they are manufactured by different providers

## Judging by visual assessment

- Need consistent lightning
- Need consistent viewing
- Need to Check for Metamers

<div class="alert alert-success" role="alert" markdown="1">
Use a light booth !
</div>

- Sufficient when there are few standard samples to be matched
- Sufficient when tolerance is judged visually by color experts
- Requires all manufacturers to have a physical copy of the standard, and to have the same hardware
- Because there are no measurements, we don't know to adjust color workflow in case we need to match a color

# Measuring with Spectrophotometers

## Remember Light interaction

<div class="alert alert-info" role="alert" markdown="1">
Spectrometer can measure reflectance and transmittance (specular and/or diffuse)

![](https://i.imgur.com/zBrLx4W.png)

</div>

## Time for another video

[What is a Spectrophotometer? ](https://youtu.be/kXsCJwBIX14)

## Light Reflection vs Material

- Matte
    - Light is reflected in all directions equally
- Semiglossy
    - Light is reflected in all direction but a small part is reflected orthogonal to the incident angle
- Glossy
    - Light is reflected in all directions but a big part is reflected orthogonal to the incident angle

## Spectrophotometers: In a Nutshell

- Spectral reflectance
    - The ratio of reflected light ($r$) to the incident light ($i$) under specific geometric conditions

$$
R_{\lambda}=\frac{\phi_{\lambda}^r}{\phi_{\lambda}^i}
$$

- Spectral transmittance
- - The ratio of transmitted light ($t$) to the incident light ($i$) under specific geometric conditions

$$
T_{\lambda} = \frac{\phi_{\lambda}^t}{\phi_{\lambda}^i}
$$

- All measuring instrument need to be calibrated
    - using White Tile made from *Spectralon*

## Spectrophotometers: reflectances ?

![](https://i.imgur.com/NfAwvsX.png)

## Interlude: fluoresence

<div class="alert alert-warning" role="alert" markdown="1">
Fluroescence can create colors we don't see
</div>

- Use an instrument called a Bispectrometer to measure it

![](https://i.imgur.com/05oZqBT.png)


![](https://i.imgur.com/qoGVgLN.png)
> Donaldson matrix obtained from a green sample emitting a more satured green light

![](https://i.imgur.com/iFaryug.png)

## Colorimeter vs Spectrophotometers

- Colorimeters are used generally to calibrate screens
- They mimic the way our eyes perceive color

They measure reflectance in 3 wavelengths (R, G, B)
They do not provide a spectral response


# Spectrophotometers
## Types

![](https://i.imgur.com/H11vJu9.png)

- Bidirectionnal
    - Non-structured and flat surfaces (paper, plastics)
- Sphere ![](https://i.imgur.com/m4vKZ8B.png)
    - Structured and glossy surfaces (textiles, metallic)

## SPIN vs SPEX

- SPIN Specular Included (gloss is accounted for)
    - Color is measured independent of the sample's gloss or surface texture
- SPEX Specular Excluded

![](https://i.imgur.com/2VmtYrC.png)

![](https://i.imgur.com/OpOF587.png)

### Specifications

> Example: Automotive interior plaque (items produced using different materials)
> - SPIN: looks at the material independant of surface texture
> - SPEX: values which depend on gloss and surface conditions


# Different spectro models
## Specifications

<div class="alert alert-warning" role="alert" markdown="1">
Choose depending on what you need
</div>

||X-RIte i1Pro 2|X-RITE Ci62|Barbieri LFP qb
|-|-|-|-|
|Measurment geometry|$45^o$ a:$0$ (ring illumination)|$di:8^o$|$45^o$c:$0$ (circumferential)|
|Light source|Gas filled tungsten lamp and UV LED|Gas-filled tungsten lamp|3 point circle, 7-LED chip|

## Geometry

Reflectance of a semi-glossy object
- $di:8^o$

<div class="alert alert-info" role="alert" markdown="1">
A high gloss sample with the same pigmentation is visually judged darker by the eye when compared to a matte sample
</div>
- $\color{orange}{45^o:0}$: measure that color difference
- $\color{green}{di:8^o}$ measure the same color in both cases
- $\color{orange}{45^o:0^o}$ simulates normal behavior
    - e.g. when we read a magazine

![](https://i.imgur.com/6bvG3Cj.png)

### Aperture


||X-RIte i1Pro 2|X-RITE Ci62|Barbieri LFP qb
|-|-|-|-|
|Measurment aperture|$4.5mm$|$4$ or $8mm$|$2$,$6$ and $8mm$|

![](https://i.imgur.com/CHWwPDt.png)

Small aperture
- Measures quickly
- may miss relevant info

Large aperture
- more accurate
- measurement takes longer
- needs larger sample

## Conditions

||X-RIte i1Pro 2|X-RITE Ci62|Barbieri LFP qb
|-|-|-|-|
|Measurment conditions|M0, M1, M2|N/A|M0, M1, M2, M3|

- M0
    - legacy measurement (tungsten lamp, no standardization of UV content in illuminat, UV strength changes through time)
- M1
    - Spectral distribution of illuminant
- M2
    - UV is excluded
- M3
    - Polarized light

<div class="alert alert-warning" role="alert" markdown="1">
Measurement conditions impact the color
</div>

## Spectral range

||X-RIte i1Pro 2|X-RITE Ci62|Barbieri LFP qb
|-|-|-|-|
|Spectral range|$380-730nm$|$700-400nm$|$380-750nm$|

## Repeatability


||X-RIte i1Pro 2|X-RITE Ci62|Barbieri LFP qb
|-|-|-|-|
|Short term repeatability|$0.1$ $\Delta E_{94}$|$0.05$ $\Delta E_{ab}$|$0.05$ $\Delta E_{00}$|

2 different *i1Pro 2* spectro
- 10 measurements of the same object were taken for each instrument
- $\Delta E$ between first and other 9 measurements were computed for each instrument

||X-RIte i1Pro 2|X-RITE Ci62|Barbieri LFP qb
|-|-|-|-|
|Inter-instrument agreement|Average $0.4$ $\Delta E_{94}$ Max $1.0$ $\Delta E_{94}$|Average $0.4$ $\Delta E_{ab}$ Max $1.0$ $\Delta E_{ab}$|Average $0.4$ $\Delta E_{00}$ Max $1.0$ $\Delta E_{00}$|

# Transmittance Measurement
- When we need transmittance ?
    - Light Filters
    - Printed Ads
    - Food Inspection

![](https://i.imgur.com/dimTGld.png)

## Inter-instrument agreement

- Compared measurements of 16 samples used for printing

![](https://i.imgur.com/uNniTKT.png)

# Recap

- Many different (standardized) methods to measure Reflectance (and Transmittance)
- Unfortunately, measured Reflectance/Transmittance is not unique as it depends on the instrument you sued to measure it
- Type of instrument to used depends on what you want to measure, and how frequent you want to measure
- Only measurements tales under the same conditions can be truly compared. Therefore, **it is necessary to note the following information in a color measurement report**:
    - Color instrument (geometry, aperture, measurement condition)
    - Illuminant/observer standards, if you give $L\times a\times b$ values

# Future trends: beyond color

## Visual appearance of materials

- Reflection
- Transmission
- Absorbance

![](https://i.imgur.com/aa9jyC1.jpg)

![](https://i.imgur.com/auHszs1.jpg)

![](https://i.imgur.com/JEE12Bp.jpg)

## BRDF Measurement

<div class="alert alert-info" role="alert" markdown="1">
Bi-directional Reflectance Distribution Function (BRDF) gives a more complete characterization of light interaction with the surface

![](https://i.imgur.com/MDjrtDW.png)

</div>

<div class="alert alert-danger" role="alert" markdown="1">
We measure how light reflects in all directions

![](https://i.imgur.com/Kvkc9tO.png)

</div>

- BRDF allows characterizing the surface appearance at a microscopic level (used in Computer Graphics to render objects)
- Measurable with Goniophotometers

![](https://i.imgur.com/M2n3Cb2.png)

<div class="alert alert-warning" role="alert" markdown="1">
How to measure BRDF faster and cheaper ?
</div>

# Sources

- [Les boules](http://rgl.epfl.ch/materials)
- [Litteralement tout le cours](https://www.xrite.com/-/media/xrite/files/whitepaper_pdfs/l10-001_a_guide_to_understanding_color_communication/l10-001_understand_color_en.pdf)
- [Spectrophotometer](https://www.barbierielectronic.com/wp-content/uploads/2021/02/WP07_Why-larger-measuring-aperture-counts_e_v1-1.pdf)
- [Spectral measurment X-RITE](https://www.xrite.com/blog/effective-ways-measure-reflective-surfaces)


# Metamerism

## What's that ?

<div class="alert alert-info" role="alert" markdown="1">
metamerism is a perceived matching of colors with different (nonmatching) spectral power distributions.
</div>

## Most important types

- *Illuminant Metamerism*
    - Different spectral characteristic and
        - same color when viewed under one light
        - different color when view under another light
- *Observer Metamersim*
    - Different spectral characterisic and
        - same color when viewed by one observer
        - different color when view by another observer

## Examples: 
### Car industry

![](https://i.imgur.com/gLszXkp.png)

[Source](https://coats.com/en/information-hub/Differentiating-Metamerism-and-Illuminants)

### Other

![](https://i.imgur.com/a7gmKDW.png)

[Source](https://www.verivide.com/it-looked-nothing-like-that-in-the-shop-metamerism-an-explanation/)

## Metamerism vs Color Inconstancy

- Color inconstancy: A single object changing color with changes in the color of the illumination
- Metameric pair: Two objects having color inconstancy

## Recap

- Metamerism is an effect we need to consider if a pair of objects will be viewed under more than one type of illuminant
- In the printing industry, neutral (grayscale) colors are more susceptible to illuminant metamerism as a mix of inks is used
- In the case of displays, illuminant metamerism is not a problem as they create their own light
