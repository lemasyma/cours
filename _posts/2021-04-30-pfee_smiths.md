---
title:          "PFEE - Sujet 6.1 et 6.2: Smiths group"
date:           2021-04-30 15:00
categories:     [Image S8, PFEE]
tags:           [Image, S8, PFEE]
math: true
description: Smiths group
---
Lien de la [1ere note Hackmd](https://hackmd.io/@lemasymasa/BkKNDSEw_)
Lien de la [2nd note Hackmd](https://hackmd.io/@lemasymasa/r1uyVBtD_)


# Sujets 6.1

## Introduction

Presentation psr Clement Fang
- Ancien Image 2020

Serge Maitrejean
- Responsable de l'innovation
- Doctorat en physique

Eric Garrido
- Doctorat en physique nucleaire

Groupe Smiths
- Cote en bourse a Londres
- 4 divisions
- Smith detection: scanner et detection
    - Detection de choses illicites ou non-declarees

![](https://i.imgur.com/slPVgpB.png)

En france:
- Base a Vitry-sur-Seine
- A peu pres 200 personnes
- IA / traitement d'image...

![](https://i.imgur.com/bbd3Ugq.png)

## Les techs au sein de Smith
![](https://i.imgur.com/EtGhHb9.png)

## Global presence
![](https://i.imgur.com/k36uuzX.png)

## Vehicle, cargo & mobile screening
![](https://i.imgur.com/tp46Aw7.png)

## High energy X-ray imaging
![](https://i.imgur.com/28UHq2J.png)

### Which target / threat we are looking for ?
![](https://i.imgur.com/fyedcWY.png)

### SD Paris Partnerships
![](https://i.imgur.com/OtSFwq7.png)
> Epita est cense etre la

## Cigarettes detection
![](https://i.imgur.com/DUjLNGD.png)

### Some big seizures made thanks to our iCmore in the news
![](https://i.imgur.com/T0DgE8z.png)

### iCmore Weapons detection
![](https://i.imgur.com/4t4eIAw.jpg)

## More in-depth
### Truck Radioscopy
- Imaging with X-Rays but with a scanning principle

![](https://i.imgur.com/gmvNTi8.png)

- Pulsed X-ray source: X-Ray pulses (flash) oh three $\mus$ every 2 or 3 milliseconds
- One vertical line of detectors/pixels (5 or 20 mm width, 5 mm height): one column of image is recorded for each X-ray pulses
- Truck speed is limited: < displacement of detector width between 2 pulses (typically 5-7 km/h)
- Or resolution is bad (large detectors)


### A new tech: Matrix detector
- Multicolumn detector (column)

![](https://i.imgur.com/hzgY8W1.png)

- Large resolution improvement (Left one line, Right Matrix detector)

### But noting or nobody is perfect
- First problem: missing part ![](https://i.imgur.com/POzBDQK.png)
- Easy to solve by slowing down the speed but... ![](https://i.imgur.com/xyvOhW7.png)
    - Superposition: le meme point se voit 2 fois

### The problem of depth at low speed: rearranging data ?
- The way of ordering data is depending on the depth where objects are located.. But we don't know the depth ! It's a stereo effect

![](https://i.imgur.com/ANiwbzh.png)

### Ordering data is depending on the depth
- We have to assume where in depth the object are located, if we are wrong strong artifacts appears

![](https://i.imgur.com/zf7bU3A.png)

### Turning a drawback onto an advantage
- Minimizing the artifacts $\Leftrightarrow$ Finding the depth of the objects and providing a optimum high resolution image

### Curent status
- Proof of concept has been done using energy minimization technics
- Work on this approach is pursuing
- A comprehensive set of data has been acquired from which the "exact images" can be extracted
- We want to test another approach, neural networks and deep learning are good candidates

### The work
- Getting familiarized with the problem (not so easy)
- Getting familiarized with the current method
- Initating Matrix Detector Deep Learning process for:
    - Building the best radioscopic planar images
    - Finding the depth where objects are located


# Sujets 6.2

## Introduction

Presentation psr Clement Fang
- Ancien Image 2020

Serge Maitrejean
- Responsable de l'innovation
- Doctorat en physique

Eric Garrido
- Doctorat en physique nucleaire

Groupe Smiths
- Cote en bourse a Londres
- 4 divisions
- Smith detection: scanner et detection
    - Detection de choses illicites ou non-declarees

![](https://i.imgur.com/slPVgpB.png)

En france:
- Base a Vitry-sur-Seine
- A peu pres 200 personnes
- IA / traitement d'image...

## High energy discrimination
- Same principle as an X-ray
- It looks like and X-ray
- but with an X-ray we only have grayscale information

![](https://i.imgur.com/7S9ouXj.png)

Plus un objet et dense et epais, plus il sera noir

![](https://i.imgur.com/spwENVI.png)

![](https://i.imgur.com/Zu9TwHr.png)

![](https://i.imgur.com/yrVneRA.png)

## Work to do
Improving the performance of the material discrimination project by:
- Better management of the overlay problem
- Creatin better quality of scans

### Overlay
- 2 ojects that overlay make the material detection wrong
- Find a method to segment the objects, then assign their atomic number

### Improve scan quality
Create a neural network to convert acquisition from low device to high

![](https://i.imgur.com/zmJkaoq.png)

### An AI that assigns the atomic number of objects
Create a color scale image with only the grayscale image

![](https://i.imgur.com/5DL4PU5.png)

### Provided 
- Reference method
- Database
- Script to help for you for your tasks
