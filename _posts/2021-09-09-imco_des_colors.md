---
title:          "IMCO: Describing color"
date:           2021-09-09 14:00
categories:     [Image S9, IMCO]
tags:           [Image, S9, IMCO]
description: Describing color
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/ByH7S8wGt)

# Describing a relative color
- Need of a vocabulary to describe a color
- 2 (or more) objects may be all blue, but different
    - Need additional descriptions within colors
- How do we organize colors ?

## Blue jacket ?

![](https://i.imgur.com/PVcn60f.jpg)

All of this is blue

![](https://i.imgur.com/MVgzI3D.png)

This is navy blue

![](https://i.imgur.com/e6jzkAM.png)

This is dark navy blue

<div class="alert alert-warning" role="alert" markdown="1">
What about colors that are hard to describe ?
</div>

## How ? - Desert Island Experiment

A person with normal color vision is on an island and need to group pebbles

1. Think about colo in terms of common color names (red, blue, green, etc.)
2. How to arrange achromatic samples ?
    - Orders from darker to lighter
3. How to arrange chromatics smaples ?
    - By color (hue)
    - > Example: group all red pebbles together
4. How to arrange chromatic samples of the same hue ?
    - order by lightness
    - order by how much color they contain (chroma)

<div class="alert alert-success" role="alert" markdown="1">
We know how to arrange chromatic samples of the same **hue**
</div>

# Color attributes
We found color attributes

- Pyschological attributes that describe colors:
    - Hue
    - Lightness

<div class="alert alert-info" role="alert" markdown="1">
**Definition: Hue**
Attribute of a visual sensation according to which an area appears to be similar to one of the perceived colors: red, yellow, green, and blue, or to a combination of 2 of them
</div>

- achromatic color: perceived with lacking hue
- *chromatic* color: perceived color with hue

<div class="alert alert-danger" role="alert" markdown="1">
11 primitives colors
$\color{white}{\text{white}}, \color{gray}{\text{gray, }}\color{black}{\text{black, }} \color{red}{\text{red, }}\color{green}{\text{green, }} \color{yellow}{\text{yellow, }} \color{blue}{\text{blue, }} \color{orange}{\text{orange, }} \color{purple}{\text{purple, }} \color{pink}{\text{pink, }} \color{brown}{\text{brown}}$
</div>
Elementary colors: white, black, red, green, yellow, blue
- unique hues according to opponent color theory

<div class="alert alert-info" role="alert" markdown="1">
**Definition: Lightness**

- *Brightness*: attribute of a visual sensation according to which an area appears to emit, or reflect, more or less light $\to$ relative
- *Lightness*: the brightness of an area judged *relative to* the brightness of a similarity illuminated area that appears to be white or highly transmitting $\to$ absolute

$$
\text{Lightness}=\frac{\text{Brightness}}{\text{Brightness(white)}}
$$

</div>

<div class="alert alert-info" role="alert" markdown="1">
**Definition: Chroma**
- *Colorfulness*: Attribute of a visual sensation according to which the perceived color of an area appears to be more or less chromatic
- *Chroma*: Colorfulness of an area judged as a proportion of the brightness of a similarly illuminated area that appears white or highly transmitting

$$
\text{}Chroma = \frac{\text{Colorfulness}}{\text{Brightness(white)}}
$$

</div>

# Color Order Systems

## Munsell Color system

Composition:
- Hue
    - 10 hues (each divided into 10 subhues)
- Lightness (called Value)
    - 11 steps (0: ideal black, 10: ideal white)
- Chroma
    - Range depending on the hue

![](https://i.imgur.com/RwGGDUo.png)

<div class="alert alert-danger" role="alert" markdown="1">
<i class="bi bi-exclamation-circle-fill"></i> Eyes are all differently sensitive
</div>

Notation: H V/C
- H = Hue, V = Value, C = Chroma
- e.g. 5Y 7/12 or 5R 1/4

![](https://i.imgur.com/LslCfdb.jpg)
> Munsell Color Tree from Pantone

# How to communicate color ?

<div class="alert alert-success" role="alert" markdown="1">
Pantone and other organizarions
</div>

## Pantone Color-Naming System

- Used in the printing/manufactuing industry
- Swatches are used to specify colors
- Printed using 14 inks
- Useful for specifying communicating color
- Patented ! Need a license to use the list

# Describing Relative Color
## Color Mixing Systems

![](https://i.imgur.com/J1HHL46.png)

Amounts give a specification, not the resulting color
- RGB value $\text{{}100, 20,90\text{}}$ in your screen $\neq$ RGB $\text{{}100, 20,90\text{}}$ in my screen
- CMY value $\text{{}90, 10,50\text{}}$ in your printer $\neq$ CMY $\text{{}90, 10,50\text{}}$ on my printer
- RGB value $\text{{}100, 20,90\text{}}$ in my screen $\neq$ CMY $\text{{}90, 10,50\text{}}$ on my printer

## HSV/HSL Spaces

![](https://i.imgur.com/mao3nDP.png)

- Hue: color
- Saturation: measure of chroma
- Value or Lightness: measure of lightness

HSV/HSL difference:
- HSL: maximum lightness = white
- HSV: maximum Value = "intense" color

![](https://i.imgur.com/bpHpqkL.png)

## HSV $\leftrightarrow$ RGB

![](https://i.imgur.com/zi8IPi6.png)

## YCbCr Space

- Y is Luminance $\simeq$ Brightness
- Cb is related to blue Chrominance
- Cr is related to red Chrominance

![](https://i.imgur.com/FeBRkDH.png)

![](https://i.imgur.coms3Xqrn.png)

> Used a lot in color compression

## Decomposition

Divide image in RGB
![](https://i.imgur.com/TQVcfBp.png)

Divide Image in HSV
![](https://i.imgur.com/cxI95zr.png)

Divide image in YCbCr
![](https://i.imgur.com/cQhyYeT.png)

## Use Case - Color Segmentation

<div class="alert alert-success" role="alert" markdown="1">
HSV or YCbCr can be used in Image and Video Processing (e.g., skin segmentation)
</div>

However, as RGB and CMYK, resulting color is only relative to capture condition

# Describing Standard Color

- Use an universal way (i.e., numbers) to communicate color instead of using names
- Need to standardize the color forming conditions
    - Illuminant (viewing lighting)
    - Observer (the human visual response to a given stimulus)
    - Object reflectance ($\lambda$-dependent spectral measurement)
- Colorimetry

## CIE Standard Observers

- Light sources (primaries): $435.8nm$, $546.1nm$, $700nm$
- CIE 1931 Standard Colorimetric Observer
    - $2^o$ visual angle ($2^o$ Observer)
    - $17$ color normal observers
- CIE 1964 Standard Colorimetric Observer
    - $10^o$ visual angle ($10^o$ Observer)
    - 76 color normal observers

![](https://i.imgur.com/HDn9vh3.png)

## CIE Standard Iluminants

- D: Different types of daylight
    - D50 ($\color{cyan}{5003K}$) (warm daylight)
        - printing/graphic arts
    - D65 ($\color{blue}{6504K}$) (natural daylight)
        - art/film/photography
- A: incandescent lamp ($\color{orange}{2856K}$)
- F: Fluorescent light
    - F2 (4230K), F11 (4000K)

## Color Temperature

Temperature uses as a reference an ideal object called "Black Body"

<div class="alert alert-info" role="alert" markdown="1">
**Definition: Black Body**
An object that absorbs completely heat and light, and radiates the energy back.

It radiates light when heated.
</div>

![](https://i.imgur.com/zBD67xY.png)

![](https://i.imgur.com/SK5jofj.jpg)

## CIE Standard Iluminants

- Warm: $T \lt 3300K$
    - Dormitory, Restaurant, Hotel, Coffee Shop
- Intermediate: $3300K\lt T\lt 5300K$
    - Stores, Shcool, Libraries
- Cold: $T\gt 5300K$
    - Offices, Hospitals

## Computing XYZ Tristimulus Values

<div class="alert alert-info" role="alert" markdown="1">
*$XYZ$ Tistimulus Value* $\to$ amounts of 3 specified stimuli required to match a color
</div>

$$
\begin{aligned}
X &= k\int_{\lambda}I(\lambda)R(\lambda)\bar x_{\lambda}d\lambda\\
Y &= k\int_{\lambda}I(\lambda)R(\lambda)\bar y_{\lambda}d\lambda\\
Z &= k\int_{\lambda}I(\lambda)R(\lambda)\bar z_{\lambda}d\lambda\\
\end{aligned} \quad k =
$$

![](https://i.imgur.com/AImcGXK.png)

## Chromaticity Diagrams: CIE 1931

All Hues are perceivable by the standard observer

![](https://i.imgur.com/VzIKK4l.png)
> MacAdam Ellipses
> Where are the grey ? Brown ? No light info !

![](https://i.imgur.com/UPHmJlk.gif)

## Uniform color spaces

- CIE XYZ Space is not perceptually uniform
    - equal perceptual differences between colors $\neq$ equal distances in the XYZ space
- CIE recommenced uniform color spaces
    - CIE 1976 $L\times u\times v$
    - CIE 1976 $L\times a\times b$

### Example

In matplotlib:
![](https://i.imgur.com/G9EoNgx.png)

### CIE $L\times a \times b$ Space
$$
L^* = 116f(\frac{Y}{Y_n})-16
\begin{cases}
a^* = 500[f(\frac{X}{X_n})-f(\frac{Y}{Y_n})]\\
b^* = 200[f(\frac{X}{X_n})-f(\frac{Y}{Y_n})]
\end{cases}
$$

### $L\times C\times h$

![](https://i.imgur.com/i88JLUv.png)

# What's left ?

- Modeling cognitive effects or phenomena
- How to obtain absolute color attributes (brightness and colorfulness) ?
- Debate about accuracy of $\bar x, \bar y, \bar z$ Color Matching Functionc
    - Representativeness of the population used for the experiments
    - Limitaations of equipment used for the experiments
    - How to understand color perception of "color anomalous" observers ?