---
title:          "ISAT: Remote sensing"
date:           2021-12-09 09:00
categories:     [Image S9, ISAT]
tags:           [Image, S9, ISAT]
math: true
---

Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/rkBvAV1cF)

# Introduction

## Remote sensing

![](https://i.imgur.com/l6qGllr.png)

*What is remote sensing ?*

- **Remote**: operating without a direct contact
- **Sensing**: perform a measure
- Measure something at a distance, rather than in situ. It relies on propagated signal of some sort, for example optical, acoustical, or microwave

# Remote sensing image

## Panchromatic image

La particularite de ces systemes est qu'ils ont leur propre source d'illumination, en envoyant des signaux qui interagissent avec des objets d'interete.

> Exemple: on prend une photo avec de la lumiere, c'est un *systeme actif*

Ici on s'interesse a la teledetection ou on utilise des sources d'illumination externe (le soleil)

On s'interesse principalement au regime optique de la lumiere, avec de l'optique geometrique. On est dans les plages du visible a l'infrarouge.

On va regarder l'heterogeneite des donnees qu'on peut avoir en teledetection:

![](https://i.imgur.com/RHiGIbG.png)

## Multispectral

On a aussi des images multispectral:

![](https://i.imgur.com/mqu6Dzv.jpg)

## Hyperspectral

![](https://i.imgur.com/qmpdBjI.png)

## From low spatial resolution...

![](https://i.imgur.com/EHBiDCM.png)

## To high spatial resolution

![](https://i.imgur.com/eUAZEmV.png)

## Spatial details in satellite images

![](https://i.imgur.com/pGEnH4e.png)

## Spatial details in aerial images

![](https://i.imgur.com/MKQMJEj.png)

![](https://i.imgur.com/u9KjtH7.png)

![](https://i.imgur.com/M60x59o.gif)

## Spatial details in drone images

![](https://i.imgur.com/rNzUv9r.png)

![](https://i.imgur.com/OoPGx3m.png)

![](https://i.imgur.com/9T87xgJ.png)
> Bonne precision pour identifier des feuilles de plante, utile pour verifier leur etat de sante

![](https://i.imgur.com/yUpX8Nh.gif)

![](https://i.imgur.com/pUnxFWw.png)
> J'espere que vous vous en rappelez

## Multitemporal images

![](https://i.imgur.com/CCZUZmt.png)

> Ce sont les Alpes, par-dessus Grenoble
> Ce sont des recombinaisons fausses couleurs
> Il y a des parties manquantes sur l'image a cause des nuages

On a une acquisition par jour par satellite, et on a 2 satellites.

<div class="alert alert-success" role="alert" markdown="1">
On arrive a faire un suivi de certains phenomenes
</div>

![](https://i.imgur.com/8p8LcNt.png)

On a certaines satellites "*Agile*" capablent d'orienter leurs cameras

Voici d'autres acquisitions:

![](https://i.imgur.com/j6Jpc0e.png)

![](https://i.imgur.com/AwfHSri.png)

![](https://i.imgur.com/Xd6xY0U.png)

En comparant les images, on voit clairement le deplacement de la camera

## Multiangular drone images

![](https://i.imgur.com/UXbpTpD.jpg)

![](https://i.imgur.com/PTlD9E4.jpg)

On entre en convergence en *computer vision*, on retrouve les memes problematiques.

# Applications

## Thematic classification

On veut tirer des informations de ces images, par exemple: *semantic segmentation*

![](https://i.imgur.com/Z5dAwlZ.jpg)

## Anomaly detection

Detecter des evenements rares comme des phenomenes naturels.

![](https://i.imgur.com/K06PDXH.jpg)

![](https://i.imgur.com/jFfAHHV.png)

![](https://i.imgur.com/OEjRmYM.png)

[(Video) Nearly 20 Years of Change at Your Fingertips](https://youtu.be/X16cfGPL2wA)

# Optical radiation model

## Optical Remote sensing principle

![](https://i.imgur.com/EePMBTR.png)

Quant a la source d'illumination:

![](https://i.imgur.com/K0XEVCn.png)

On a des longueurs d'ondes beaucoup plus elevees par rapport a ce qu'on utilise dans les capteurs optiques, on peut aller jusqu'aux ondes radios

## Solar radiation


<div class="alert alert-info" role="alert" markdown="1">
The **spectral radiant exitance** ($M_{\lambda}[Wm^{-2}\mu m^{-1}]$) of a black body is modeled by **Planc's blackbody equation**

$$
M_{\lambda} = \frac{C_1}{\lambda^5(e^{\frac{C_2}{\lambda T}}-1)}
$$

- $C_1, C_2$ constant
- $\lambda$ wavelength $[\mu m]$
- $T$ black body temperature $[K]$

The blackbody function peaks at a wavelength given by **Wien's law**

$$
\lambda_{max} = \frac{2989}{T}
$$

</div>

![](https://i.imgur.com/I2YE3va.png)

Pour le soleil, le pic d'emission par rapport a sa temperature se trouve dans le visible


## Solar spectral irradiance


<div class="alert alert-info" role="alert" markdown="1">
- $E_{\lambda}^0$ **spectral irradiance** $[Wm^{-2}\mu m^{-1}]$ power density that reaches the earth
    - Quantite d'energie
- Spectral irradiance at the top of atmosphere

$$
E_{\lambda}^0 = \frac{M_{\lambda}}{\pi}\times\frac{\text{area solar disk}}{(\text{distance to earth})^2}
$$

</div>

![](https://i.imgur.com/O0ZqMUw.png)


*Et le Red-Shift ?*
> On a un soleil dans une autre galaxie, si l'emission de cette etoile etait dans le jaune mais que la galaxie se deplace, on a une *reduction en frequence* qu'on voit comme un shift dans le spectre d'emission
> **C'est l'effet Doppler qui fait ca**, caracterise par la nature ondulatoire de la lumiere
> C'est comme ca qu'on arrive a estimer les velocite de galaxies
> On relie ca aux gazs presents dans les etoiles, ces derniers ont des spectres d'emissions particulier donc avec le *red-shift* on peut estimer le decalage

## Solar/Earth radiation

![](https://i.imgur.com/iWwohQa.png)

Tout corps avec une temperature $\le 0K$ aura un spectre d'emission hors du visible

# Radiation Components

On est a l'exterieur de l'atmosphere:

![](https://i.imgur.com/R2vTFS5.png)

## Optical remote sensing component

![](https://i.imgur.com/J01Ea8Y.png)

## Radiation mechanism

![Uploading file..._xmizolcjh]()

## Radiation component

<div class="alert alert-info" role="alert" markdown="1">
**Radiance** reaching the satellite sensor

$$
L_{\lambda}^s = L_{\lambda}^{su} + L_{\lambda}^{sd} +  L_{\lambda}^{sp}
$$

- $L_{\lambda}^{su}$ the unscattered, surface-reflected radiation
- $L_{\lambda}^{sd}$ the down-scattered, surface-reflected skylight
- $L_{\lambda}^{sp}$ the up-scattered path radiance
</div>

## Surface-reflected, unscattered component $L_{\lambda}^{su}$

- The atmosphere interacts with radiation both on the solar and view path
- The fraction or radiation that arrives at the earth's surface is the **solar path transmittance**, $\tau_s(\lambda)$
- The molecular absorption bands of water and carbon dioxide cause deep absorphtion features that, in 2 bandas near $1.4\mu m$ and $1.9\mu m$, completely block transmission of radiation

## Solar path

![](https://i.imgur.com/jXisSV9.png)

- $0$: Rien qui est transmis
- $1$: La couche est totalement transparente

### Exemple: Sentinel-2 spectral responses

![](https://i.imgur.com/7pInZW4.png)

## Atmospheric scattering mechanisms

L'aerosol est la composante principale qui va determiner l'absorption. Ces bandes ne sont pas forcement utiles pour le monitorage de la surface terrester mais sont des indicateurs lors du moment de l'acquisition.

Si on considere l'interaction de la couche atmospherique avec la source d'illumination, on a la transmission qui va determiner une modulation de l'energie.

<div class="alert alert-info" role="alert" markdown="1">
**Atmospheric scattering**
- *Absorption* mainly due to molecules of oxygen, carbon dioxide, ozone and water which attenuates the radiation very strongly in certain wavelengths
- *Scattering* by atmospheric particles is the dominant mechanism that leads to radiometric distortion in image data
</div>

<div class="alert alert-info" role="alert" markdown="1">
**Rayleigh scattering**
- scattering due to air molecules
- effect proportional to $\lambda^{-4}$
- scattering mechanism in a clear sky
</div>

<div class="alert alert-info" role="alert" markdown="1">
**Mie scattering**
- scattering by aerosol (e.g. smoke, clouds, haze) with molecules larger than those of the air ($1-10$ times $\lambda$)
- not much dependent on the wavelength
</div>

![](https://i.imgur.com/NPpGnSy.png)

![](https://i.imgur.com/D2euiQZ.png)

> On a du *scattering* avec des nuages ou du brouillard

<div class="alert alert-warning" role="alert" markdown="1">
Ce type de *scattering* n'est pas forcement selectif en fonction de la longueur d'onde
</div>

![](https://i.imgur.com/KXfbQkK.png)

# Interaction with the surface

## Solar path

<div class="alert alert-info" role="alert" markdown="1">
Spectral irradiance at the earth’s surface

$$
E_{\lambda} = \tau_s(\lambda)E_{\lambda}^0
$$
</div>

![](https://i.imgur.com/rv5Jp9c.png)

## Irradiance at the surface

<div class="alert alert-info" role="alert" markdown="1">
- The irradiance at the surface depends on the incident angle
- The **incident irradiance**

$$
E_{\lambda}(x,y) = \langle\tau_s(\lambda)E_{\lambda}^0n(x,y), s\rangle = \tau_s(\lambda)E_{\lambda}^0\cos[\theta(x,y)]
$$
</div>

![](https://i.imgur.com/LxtDGTI.png)

## Surface radiance

<div class="alert alert-info" role="alert" markdown="1">
- The incidence radiation interacts with the materials on the surface
- Assumption of a Lambertian surface $\to$ equal radiance in all directions
- **surface radiance** $L_{\lambda}(x,y)$

$$
\begin{aligned}
L_{\lambda}(x,y) &= \rho(x,y,\lambda)\frac{E_{\lambda}(x,y)}{\pi}\\
&=\rho(x,y,\lambda)\frac{\tau_s(\lambda)E_{\lambda}^0\cos[\theta(x,y)]}{\pi}
\end{aligned}
$$

with $\rho$ the **diffuse spectral reflectance**, $\pi$ geometric factor

- **Bi-directional Reflectance Distribution Function** (BRDF)

$$
BRDF(x,y,\phi,\theta)\simeq \frac{L_{\lambda}(\phi)}{E_{\lambda}(x,y)}
$$
</div>

### Measuring the BRDF

![](https://i.imgur.com/NUwztcw.png)

# At the sensor

## Radiation mechanism

![](https://i.imgur.com/4aXwNLv.png)

On mesure la combinaison de ces 3 composantes au niveau du capteur

## Radiance at the sensor

<div class="alert alert-info" role="alert" markdown="1">
- Radiance reaching the sensor passes through the atmosphere
- Depends on the view angle
- **at-sensor radiance**

$$
\begin{aligned}
L_{\lambda}^{su}&= \tau_{v}(\lambda)L_{\lambda}\\
&= \rho(x,y,\lambda)\frac{\tau_{v}(\lambda)\tau_s(\lambda)E_{\lambda}^0\cos[\theta(x,y)]}{\pi}
\end{aligned}
$$

with $\tau_v(\lambda)$ the view path transmittance.
</div>

![](https://i.imgur.com/AbmI271.png)

## Surface reflected, atmosphere-scattered component $L_{\lambda}^{sd}$

<div class="alert alert-info" role="alert" markdown="1">
- The sensor also sees radiance arising from radiation that is scattered downward by the atmosphere ("skylight") and then reflected at the earth upward
- **Radiance due to skylight**

$$
L_{\lambda}^{sd} = F(x,y)\rho(x,y,\lambda)\frac{\tau_v(\lambda)E_{\lambda}^d}{\pi}
$$

with $E^{d}_{\lambda}$ the irradiance at the surface due to skylight and $F(x,y)$ the fraction of the sky hemisphere that is visible from the pixel of interest.
</div>

On peut comparer ces 2 images:

![](https://i.imgur.com/6tZEo8h.png)

Les zones d'ombre n'ont pas de composante direct d'illumination. On recoit l'information d'une composante qui est reflechi sur cette zone qui est reflechi par l'atmosphere.

Sans atmosphere, on n'a pas d'information car pas d'eclairage (photo 2).

<div class="alert alert-danger" role="alert" markdown="1">
L'interet est d'essayer de voir, si on traite une image donnee, quelles sont les variables physiques d'interet.
</div>

# Image formation in optical sensors

## Acquisition geometry

- Directions
    - Cross-track
    - Along-track
- Scanners
    - Line scanner
    - Whiskbroom scanner
    - Pushbroom scanner
- Geometry of acquisition different from pinhole
- **Field of view** (FOV) full cross-track angular coverage
- **Ground-projected Field Of View** (GFOV) ground coverage of the FOV

![](https://i.imgur.com/V4FAMJe.png)

<div class="alert alert-info" role="alert" markdown="1">
**Instaneous Field of View** (IFOV)

$$
IFOV = 2\arctan \biggr (\frac{w}{2f}\biggr)\simeq \frac{w}{f}
$$

- $f$: focal length
- $w$: size of a detector element
</div>

<div class="alert alert-info" role="alert" markdown="1">
**Instantaneous Ground-projected Field Of View** (GIFOV)

$$
GIFOV = 2H\tan\biggr(\frac{\text{IFOV}}{2}\biggr)\simeq \frac{w}{m}
$$
</div>

![](https://i.imgur.com/TKQTFJD.png)

<div class="alert alert-info" role="alert" markdown="1">
**Ground-projected Sample Interval** (GSI)

$$
\text{GSI} = w_d\cdot\frac{H}{f}=\frac{w_d}{m}
$$

with $w_d$ the inter-detector spacing

- GSI determined by cross-track and in-track sampling rates
- Cross-track GSI usually matches the GIFOV
- In-track GSI depends on the sampling rate and the platform velocity (and scanning velocity)

</div>

![](https://i.imgur.com/JSxrfE3.png)


## Overall sensor model

![](https://i.imgur.com/hSj7qKE.png)

## Sensor characterization

The sensor will sense the physical signal with a non-zero
- Integration time
- Spectral bandwith
- Spatial distance

<div class="alert alert-info" role="alert" markdown="1">
Generic sensor model

$$
o(z_0)=\int_w i(\alpha)r(z_0-\alpha)d\alpha\\
o(z) = i(z) * r(z)
$$

- $z$ physical quantity to measure
- $o(z)$ sensor output
- $i(z)$ input signal
- $r(z)$ sensor response

</div>

## Spatial resolution

![](https://i.imgur.com/gRG3bY7.png)

*Pourquoi on descend a des resolutions tres poussees ?*
> Car d'un point de vue technologique, on arrive a produire des capteurs avec des grande precisions
> On est limites a un facteur qui est le rapport signal/bruit

## Point spread function

D'un point de vue de caracterisation des instruments:

![](https://i.imgur.com/EByMjs9.png)

Cette transformation est donnee par la *point spread function*. C'est la reponse a une impulsion sur un Dirac (ici un point tres brillant qui va etre "etale" par un point optique)

The sensor modifies the spatial properties of the signal
- blurring
- distortion of geometry

<div class="alert alert-success" role="alert" markdown="1">
The blur is characterized by **Point Spread Function** (PSF)
</div>

<div class="alert alert-info" role="alert" markdown="1">
The acquired electronix signal $e_b$ representing the signal $s_b$ given by:

$$
e_b(x,y)=\int_{\alpha_{min}}^{\alpha_{max}}\int_{\beta_{min}}^{\beta_{max}}s_b(\alpha,\beta)\text{PSF}(x-\alpha, y-\beta)d\alpha d\beta\\
e_n = \text{PSF}*s_b
$$
</div>

The PSF is composed of different components:
- optical PSF $\text{PSF}_{opt}$
- image motion $\text{PSF}_{im}$
- detector PSF $\text{PSF}_{det}$
- electronix PSF $\text{PSF}_{el}$

$$
\text{PSF} = \text{PSF}_{opt} * \text{PSF}_{im} * \text{PSF}_{det} * \text{PSF}_{el}
$$

<div class="alert alert-warning" role="alert" markdown="1">

The 2D PSF is assumed to be separable:

$$
\text{PSF}(x,y) = \text{PSF}_c(x)\text{PSF}_i(y)
$$

</div>

![](https://i.imgur.com/qhFXpXL.png)

<div class="alert alert-info" role="alert" markdown="1">
**Optical PSF**
- The optics spread a punctual light source on the focal plane
- Effect due to
    - Optical diffraction
    - Lens aberrations
    - Misalignments of the optics
- Typically the $\text{PSF}_{opt}$ is modeled as a 2D Gaussian function

$$
\text{PSF}_{opt}(x,y) = \frac{1}{2\pi ab}e^{-\frac{x^2}{a^2}}e^{-\frac{y^2}{b^2}}
$$

with $a$ and $b$ the width of the PSF in the cross- and in-track direction
</div>

<div class="alert alert-info" role="alert" markdown="1">
**Detector PSF**
- Blurring due to the non-zero spatial extent of each cell in the detector
- The blur is uniform over the spatial area of the detector
- Typically the $\text{PSF}_{det}$ is modeled as a 2D rectangular pulse function

$$
\text{PSF}_{det}(x,y) = \text{rect}\frac{x}{w}\text{rect}\frac{y}{w}
$$

with $w$ the width of the PSF
</div>

![](https://i.imgur.com/cIEZ2h5.png)

## Modulation Transfer Function

![](https://i.imgur.com/WvM7ASr.png)

> C'est les modules de la reponse sous filtre
> On retrouve ces profils dans les directions de deplacement de la plateforme

<div class="alert alert-warning" role="alert" markdown="1">
D'un point de vue configuration, on ne veut pas avoir de superposition
</div>

## Point Spread Function and sampling

![](https://i.imgur.com/dzpw72Y.png)

On fait une sorte de filtre anti aliasing

## Spectral resolution

![](https://i.imgur.com/t6MwXoI.png)

> Si on prend un capteur qu'avec 4 bandes, on aura 4 valeurs par acquisition
> La resolution sera differentes qu'avec plus de capteurs

## Spectral response

<div class="alert alert-info" role="alert" markdown="1">
The digital number (DN) stored in a pixel $p$ is (approximately) given by

$$
\text{DN}_{pb} = K_bL_{pb} + offset_b
$$

with $K_b$ and $offset_b$ the gain and offset in the A/D conversion
</div>

## Bayer pattern

![](https://i.imgur.com/8mN7KkS.png)

## Multispectral sensors

![](https://i.imgur.com/6lCW0RD.png)

### Example: WorldView2 sensor

![](https://i.imgur.com/cAtjqek.png)

#### Spectral responses

![](https://i.imgur.com/ATmcMEy.png)

> Ca permet de garantir d'avoir des niveaux d'energie suffisant

### Example: Sentinel-2 spectral response

![](https://i.imgur.com/aSfWxYM.png)

### Example: VEN$\mu$S

VEN$\mu$S (Vegetation and Environment monitoring on a New MicroSatellite)

![](https://i.imgur.com/vlR8RjO.png)

Illustration of a three-array TDI detector unit (image credit: EIOp Ltd.)

![](https://i.imgur.com/ZEEMjVU.png)


## Question - The rainbow plane

![](https://i.imgur.com/6LXcylC.png)

> Trouvee sur Google Earth

On a des repliques colorisees differement de cet avion

*Pourquoi ?*
> On a fait les acquisitions de differents spectres a differents moments

*Pourquoi on a les "contours" de l'avion ?*
> On dirait le domaine frequentiel

<div class="alert alert-success" role="alert" markdown="1">
On dirait un gradient de l'avion
</div>

Ce sera donc une derivee premiere ou seconde calculee sur l'image de l'avion.

*Pourquoi faire ca ?*
> Car c'est la fusion d'une image panchromatique avec une image multispectrale

<div class="alert alert-danger" role="alert" markdown="1">
**RECAP**: surligner les effets lies a la physique et la nature, et aborder les concepts lies a la formation de l'image d'un point de vue de l'acquisition
</div>
