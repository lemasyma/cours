---
title:          "IMED2: Introduction"
date:           2021-10-13 16:00
categories:     [Image S9, IMED2]
tags:           [Image, S9, IMED2]
math: true
---

# Agenda

1. Introduction to Medical Imaging
    - What is medical imaging ?
    - Roles, Players, Modalities
    - Anatomical vs Functional Imaging
    - Ionizing vs Non-ionizing Radiation
3. Nuclear medicine
    - Basic concepts

# Tomorrow
1. X-ray Physics
    - Basic concepts
    - X-ray production
    - X-ray interaction with matter
    - X-ray detectors
3. Diagnostic Radiology

# GE Healthcare

+1800 employees
- R&D ($35\%$)
- Production ($22\%$)
- European Center for Maintenance ($16\%$)
- Support Functions & Other ($27\%$)

![](https://i.imgur.com/pGHOGOh.png)

# Introduction
## A recent history

- 1895: discory of X-rays, first applications
- 1958: First gamma camera, Nuclear Medicine
- 1962: First UV of fetus
- 1967: First CET head scanner
- 1972: First head MR scanner
- 1990: first PET scanner

![](https://i.imgur.com/waIYHCb.png)

- 2000's-2010's: Digital Age
    - IA

# What is medical imaging ?

## Process
![](https://i.imgur.com/UCgOLoA.png)

## Roles
![](https://i.imgur.com/kq2vis2.png)

## Players

*Who are diagnostic imaging customers ?*
- Healthcar systemes, hospitals, and clinics
- Governmnent officials
- Pharmaceutical firms
- Genetics & Bio-science researchers

## Modalities overview

![](https://i.imgur.com/193JGg9.png)

## Ionizing vs non-ionizing radiation

![](https://i.imgur.com/Rmk0X7P.png)

# Anatomix vs Functional Imaging ?

## Contrast Agents

<div class="alert alert-info" role="alert" markdown="1">
Contrast agents are substances used  to enhance visibility of internal structures in X-ray or MR-based imaging techniques
</div>

- Iodine-based
    - Injected in the bloodstream to highlight blode vessels
- Gaolinium-based
    - Vascular ferromagnetic contrast agent visible in MRI
- Baarium-based
    - orally to help imaging digestive system, including esophagus, stomach and GI tracks

## Radioisotope Contrast Agents

<div class="alert alert-info" role="alert" markdown="1">
Radioisotope contrast agents are based on atmos with excess nuclear energy, making it unstable. They emit the excess energy to highlight body functions
</div>

- Tc-99m
    - Injected in the bloodstream to study brain, myocardium, thyroid, lungs, liver, gallblader
- $^{18}$F-FDg
    - Mark the glucose metabolism

![](https://i.imgur.com/d1AqGJC.png)

# Nulcear imaging

# Key components

![](https://i.imgur.com/xcqhsCE.png)

# Nuclear Medicine

## Anatomical vs Functional Imaging

![](https://i.imgur.com/2KRe4Lw.png)

![](https://i.imgur.com/hLsHvQW.png)

# Gamma-rays Physics

## Basics Concepts 

### Quanta

![](https://i.imgur.com/4VJtf3T.png)

### Atomic Model

![](https://i.imgur.com/HXOc2d5.png)

![](https://i.imgur.com/kzCXZBQ.png)

### Characteristic Radiation

![](https://i.imgur.com/x219yk9.png)


Product of electron transistions between 2 electric shells:

Two steps:
1. Electrons (or photons) collid with a shell electron, which is removed from orbit
2. Electrons from higher energy shell fills the vacancy and an X-ray photon is emitted

### Exponential Behavior

![](https://i.imgur.com/w0UYTx7.png)

Exponential decay/growth:

$$
\frac{\Delta N}{\Delta t}=\pm\lambda N\\
\text{provided: }\lambda\Delta t\lt\lt1\\
\text{then: } N=N_0e^{\pm\lambda\Delta t}
$$

![](https://i.imgur.com/JyJEFDz.png)


### Attenuation

![](https://i.imgur.com/1f5FRK1.png)

Z-ray photon life span:
1. Photon is transmitted through the matter
2. Photon is absorbed (end of life)
3. Photon is scattered ($E_{new}\le E$)

If $E_{new}\gt0$, then more A, B or C

Transmitted photons:

$$
I(E)=I_0(E)\cdot e^{-\mu(E)\cdot t}\quad\text{Berr-Lambert lawa}
$$

### Isotopes Decay

Glossary:
- IsotoPes = atoms with the same number of protons (Z)
- IsotoNes = atoms with the same number of neutrons
- Nuclides = nuclei with differing numbers of protons and neutrons are called nuclei
- Radioisotopes = atoms with unstable nuclei

<div class="alert alert-info" role="alert" markdown="1">
**Isomeric Transition**

Nucleus in an excited state returns to the more stable state release of a photon (gamma, $\sim88\%$)

</div>

- Sometimes the nucleus energy may eject an electron (ionized radiation $\sim12\%$) which deposes radiation dose to the patient

Example: $^{99m}_{43}Tc\to^{99}_{43}Tc+\gamma$

![](https://i.imgur.com/ix5jw14.png)

<div class="alert alert-info" role="alert" markdown="1">
**Beta-plus decay**
Proton converted to a neutron by releasing positron $(\beta)+$ and a neutrino
</div>
- Since positron is an antimatter analog


<div class="alert alert-info" role="alert" markdown="1">
**Electron capture**
Proton converted to a neutron by capturing an electron and releases a neutrino. It happens in nuclei with too few neutrons
</div>

Since the electron is removed from the shell, it releases **characteristic X-rays**

### Summary

![](https://i.imgur.com/5EuIoox.png)


![](https://i.imgur.com/Y6AanJm.png)

## Radiopharmaceuticals
### Production

![](https://i.imgur.com/bYeiVCP.png)


### Ideal characteristics

Ideal Characteristics
- Short-half life (but not too short)
- Monochromatic Gamma-ray production
- Gamma-ray energy high enough to easily cross patient body (deposing minimal dose)
- Gamma-ray energy low enough to be stopped by the detector
- Have minimal production of other particles (add noise to our measurements)
- Localize to the organ of interest, non toxic, ...
- Inexpensive and readily available

Technetium-99m
- Close to ideal characteristics
- Decays with $88\%$ in emission of 140.5 keV photon
- $12\%$ internal conversions (electrons, characteristic x-rays, ...)

### Transport Issues

![](https://i.imgur.com/ddhiFh7.png)

### Common Isotopes

![](https://i.imgur.com/qAuz6WJ.png)

# Diagnostic Radiology

## Instrumentation

### Gamma Camera

| Nuclear Imaging $\Leftrightarrow$ | X-ray Imaging     |
|:--------------------------------- | ----------------- |
| Radioctive isotope                | X-ray tube        |
| Collimator                        | Anti-scatter grid |
| Gamma camera                      | X-ray detector    |

- Nuclear Medicine detector also measures not only the number of events, but the time and energy of each detected event
- Ideally imaging is performed from unscattered photons that undergo photoelectric absorption in the detector
- Scintillator + Electronics must be very fast to detect individual events

![](https://i.imgur.com/TANN5yx.png)

### Pulse Height Analyzer with Nal Crystal

![](https://i.imgur.com/YvZ7Yh1.png)

### Collimators

![](https://i.imgur.com/3mGWeLX.png)

Efficiency
- Resolution = bar patterns, MTF, FWHM of point source, ...
- Sensitivity = fraction of gamma rays the pass through the holes (typically $0.01\%$)
- Increasing blades/holes length: Res $\uparrow$, Sen $\downarrow$
- Type (parallel, convergence, ...) modulates Res & Sen
- Increasing blades/holes

![](https://i.imgur.com/0Oil8u8.png)

# Clinical application

## Single Photon Emission CT

![](https://i.imgur.com/4gbaOCb.png)

Characteristics
- Long decay isotope
- Single photon emitted and captured by camera
- Tomography technique generates 3D volume of radioactivity density
- Multi-head cameras allows for faster acquisitions
- Poor spatial resolution VS excellent contrast resolution
- Noise is a major factor

Reconstruction (same as CT)
- Filtered Back-Projection
- Iterative techniques

### Applications

![](https://i.imgur.com/OkNiGZl.png)

## Positron Emission Tomography

![](https://i.imgur.com/fWFjvuP.png)

Characteristics
- Positron emitter (F-18)
- Two 511 kEV annihilation photons $180^o$ apart
- No collimator needed

![](https://i.imgur.com/ymsxxff.png)

### Application

![](https://i.imgur.com/85UcYKX.png)

# Wrap-up

Isotopes
- Exponential Decay, half-life
- Isomeric Transition (Tc-99m), Electronic $\to$ gamma rays, SPECT
- Beta-plus (F-18) $\to$ PET
- Beta-minus $\to$ Therapy

Applications in medicine
- Radiopharmaceuticals $\to$ fission, cyclotron, accelerators, generators
- Gamma cameras, collimators
- SPECT, single photon emission (gamma-rays: 70-400 keV) $\to$ orthopedics
- PET, positron emission (511 keV) $\to$ oncology