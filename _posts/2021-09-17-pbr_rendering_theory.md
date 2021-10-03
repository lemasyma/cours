---
title:          "PBR: Rendering Theory"
date:           2021-09-17 09:00
categories:     [Image S9, PBR]
tags:           [Image, S9, PBR]
math: true
description: Rendering Theory
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/S1r4A2ZXF)

[Slides du cours](https://davidpeicho.github.io/teaching/)

# Qui est-ce ?

- Epita 2018
- Chez Siemens

# TOC

1. Introduction
2. Light-Matter Interactions
3. Radiometry
4. Rendering Equation

# Light-Matter Interactions

## Disclaimer

<div class="alert alert-warning" role="alert" markdown="1">
I am not a physicist, and **Quantum Mechanics** is a really complex topix
</div>

## Rappel

![](https://i.imgur.com/EbYiQte.png)
- Champ magnetique et electrique transversal
- Equation de Maxwell
- Interactions avec la matiere

## Macroscopic Level: Interactions

- Emission
- In-scattering
- Out-scattering
- Absorption
    - onde electromagnetique absorbee

### Emission

![](https://i.imgur.com/DnsSQHi.png)
> Modele de Niels-Bohr

- Any vibrating charged particle converts energy into electromagnetic radiation

### Absorption

![](https://i.imgur.com/weQvo4a.png)

- L'electron va monter d'un niveau d'energie puis reemettre une emission

### Scattering

![](https://i.imgur.com/xGXBagp.png)

- On va pouvoir reflechir et transmettre
- La trajectoire de la lumiere va changer
    - Il va y avoir des interferences

Interferences constructives: quand la lumiere va changer de milieu, il y a le principe de Fermat "la lumiere suit toujours le chemin le plus court"

## Final notes

- Any charged particle can interact on electromagnetic radiation
- Quantum Theory and Quantum Electrodynamics can go really far
- I can only advise you to read more about this topic !

# Radiometry

## Energy

$$
Q=\frac{hc}{\lambda}
$$

- $h$: constant de Planck
- $c$: speed of light
- $\lambda$: wavelength

## Radiant Flux / Power

$$
\phi = \frac{dQ}{dt}
$$

## Irradiance

$$
E(p)=\frac{d\phi(p)}{dA}
$$

- $d\phi(p)$: power
- $dA$: finite surface area

![](https://i.imgur.com/FFCwFcc.png)

$$
E = \frac{\phi}{4\pi r^2}
$$

![](https://i.imgur.com/VngHBSf.png)

$$
E_1=\frac{\phi}{A}
E_2=\frac{\phi\cos(\theta)}{A}
$$

## Solid angle

<div class="alert alert-info" role="alert" markdown="1">
Area of a projected shape onto the Unit Sphere

![](https://i.imgur.com/oevDJCz.png)

</div>

## Radiant intensity

$$
I=\frac{d\phi}{d\omega}
$$

- $\phi$: power
- $\omega$: angle

![](https://i.imgur.com/kPVbPJ2.png)


## Radiance

<div class="alert alert-danger" role="alert" markdown="1">
On va l'utiliser pour faire tout le rendu
</div>

$$
L(p,w) = \frac{dE_{\omega}(p)}{d\omega}=\frac{d\phi(p)}{d_{\omega}dA^{\bot}}
$$

![](https://i.imgur.com/g6TJwZ0.png)

# Rendering equation

## Disclaimer

<div class="alert alert-warning" role="alert" markdown="1">
We assume that
- Light travels in vacuum
- We deal only with opaque surfaces
- Interactions at **object surface**
</div>

## Definition

$$
L_0(p,\omega_0)=\int_{\Omega}\underbrace{f_r(p, \omega_0,\omega_i)}_{\text{Réflectivité bidirectionnelle}}L_i(p,\omega_i)n\times \omega_i d\omega_i
$$

### BRDF

<div class="alert alert-info" role="alert" markdown="1">

On peut voir ca comme un ratio. C'est la quantite d'energie qui va etre emise en $\omega_0$ quand elle provient de $\omega_i$
</div>

![](https://i.imgur.com/rZ9xXbp.png)

<div class="alert alert-warning" role="alert" markdown="1">
C'est une grosse approximation de ce qu'il se passe
</div>
> Dans la vraie vie il y a de la transmission

Certaines boites utilisent de fonction plus avancees (BTDF, BSSRDF, etc.)

*Qui design ces BRDF ?*
> Lambert c'est une BRDF
> Phong utilise une BRDF

En general la BRDF c'est la propriete des materiaux pour savoir comment c'est reflete.

<div class="alert alert-danger" role="alert" markdown="1">
On ne veut pas que de l'energie soit **cree** lors de la reflection
</div>
> Il faut normaliser sinon on a des surprises

## Final notes

- Rendering equation uses all quantities we have seen
- The rendering equation is what we solve when generating 3D images
