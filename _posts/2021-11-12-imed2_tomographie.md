---
title:          "IMED2: De la radiographie a la tomographie"
date:           2021-11-12 09:00
categories:     [Image S9, IMED2]
tags:           [Image, S9, IMED2]
math: true
---

Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/Syw4WoiwK)

# La radiographie
## Controle automatique de l'exposition

> AEC: la technologie de tous les appareils modernes d'imagerie RX

<div class="alert alert-info" role="alert" markdown="1">
"*Automatic Exposure Control (AEC) is an X-ray exposure termination device*"
</div>

![](https://i.imgur.com/OYqmMZV.png)

![](https://i.imgur.com/HHlbjpl.png)

Le scanner a pour objectif d'imager toute une portion du patient de haut en bas

## Radiographie conventionelle

![](https://i.imgur.com/oRzoHvh.png)

![](https://i.imgur.com/DT6tZSs.png)

## Pathologie en orthopedie

![](https://i.imgur.com/3PCeiBJ.jpg)

# Tomographie

## Kezako ?

> Une technologie d'imagerie revolutionnaire!

![](https://i.imgur.com/8jKdmC9.png)

> La legende raconte que les royalties des Beatles ont ete utilisees pour financer le scanner

*Est-ce qu'il y a une anatomie ou la 3D n'est pas suffisante ?*
> Le coeur avec les phases cardiaques

<div class="alert alert-success" role="alert" markdown="1">
Il y a enormement de choses qui ont evolues d'un point de vue techno, ce qui a fait evoluer d'un point de vue clinique
</div>

## De tres nombreuses applications !

> Une meme theorie, des instrumentations specifiques

![](https://i.imgur.com/CAzxblk.jpg)

- Le truc mutlicouleur: institut Fraunhofer en Allemagne
    - Image d'un bloc de caillou pour savoir ce qu'il y a dedans
    - Et il y avait une tete de T-Rex !
- Color map pour la sismique
    - Eh oui, la sismique c'est de la tomographie
- Imagerie Synchrotron

## Limites de l'imagerie projective

> Cas pratique: neuro-imagerie interventionnelle

![](https://i.imgur.com/MR8e2Jh.png)

Les tranches ne sont pas suffisantes, il faut egalement tourner autour du patient

![](https://i.imgur.com/igfucP3.png)

- L'angiographie 3D est maintenant utilisee en routine clinique
    - Axinnat R., et al, "3D angiography" 
    - Orth, Robert C., et al "C-a, cone-beam CT: general principles and technical considerations for use in interventional radiology"
- Exemples
    - Quantification d'un anevrisme
    - Traitement de malformations arterio-veineuses
    - Pose de stents complexe
    - $\dots$

![](https://i.imgur.com/FodTWX7.png)

Pour un anevrisme: on fait du *coiling*; on injecte du file a memoire de forme

*Quelles dimensions utiliser ?*
> Il faut mesurer la taille de l'anevrisme

# Theorie de la reconstruction tomographique

## Decomposition du probleme

> 5 etapes

1. Comprendre la relation geometrique entre un point de l'image (de la scene) et de sa projection ![](https://i.imgur.com/b8dmu1A.png)
    - Tous les faisceaux incidents sont paralleles
2. En deduire l'ecriture de la ligne integrale se projetant en un point du detecteur
3. Demontrer un theoreme fondamental (*theoreme coupe-projection*) liant l'image a sa projection dans le domaine de Fourier
4. Exploiter ce theoreme pour exprimer l'image en fonction de ses projections
5. Comprendre comment passer d'une formulation mathematique continue a un algorithme de reconstruction (discretisation)

## Etape 1

> Comprendre la relation geometrique entre un point de l'image (de la scene) et sa projection

![](https://i.imgur.com/VQNHXDJ.png)

$$
\color{orange}{\boxed{\color{black}{x =} \underbrace{\color{black}{(x\cdot\theta)\theta}} \color{black}{+ (x\cdot\theta^{\bot})\theta^{\bot}\\
u_{\theta}(x) = x\cdot \theta}}}
$$

Evolution sinusoidale en fonction de $\theta\to$ **SINOGRAMME**

![](https://i.imgur.com/QayxdZd.png)

## ASTRA Toolbox

[Astra Toolbox](https://www.astra-toolbox.com/)

![](https://i.imgur.com/zdmOuId.png)

![](https://i.imgur.com/EdUO90z.png)

![](https://i.imgur.com/BU1bTnC.png)

```python=
vol_geom = astra.creat_vol_geom(N, N)
proj_geom = astra.create_proj_geom('parallel', 1.0, nbins, angles)
# For CPU-based algorithms, a "projectro" object specifies the projection
# model used. In this case, we use the "strip" model.
proj_id = astra.create_projector('strip', proj_geom, vol_geom)
```

```python=
sinogram_id, sinogram = astra.create_sino(img, proj_id)
plt.imshow(sinogram, extent = [detector.min(), detector.max(), angles.max() * 180 / np.pi])
```

## Etape 2

> En deduire l'ecriture de la ligne integrale se projetant en un point du detecteur

![](https://i.imgur.com/0if6uFS.png)

$$
\color{orange}{\boxed{\color{black}{p_{\theta}(u) = \int\int_{u_{\theta}(x) = u}f(x)dx}}}
$$

$$
z= u \theta + t \theta^{\bot}\\
p_{\theta}(u) = \int_{-\infty}^{+\infty}f(u\theta+t\theta^{\bot})dt
$$

On veut selectionner tous les points qui verifient $u_{\theta}(\underline{x}) = u$

$$
\begin{aligned}
p_{\theta}(u) &= \iint_{u_{\theta}(\underline{x}}f(\underline{x})d\underline{x} \\
&= \iint f(\underline{x})\delta(u_{\theta}(\underline{x} - u)d\underline{x}\\
&=\iint f(x)\delta(u-\theta \cdot x )dx
\end{aligned}
$$

## Etape 3

> Demontrer un theoreme fondamental (*theoreme coupe-projection*) liant l'image a sa projection dans le domaine de Fourier

<div class="alert alert-danger" role="alert" markdown="1">
**Theoreme de coupe-projection**

$$
F_1[p_{\theta}](\rho) = F_2[f](\rho_{theta})
$$

![](https://i.imgur.com/m5NuXS4.png)

</div>

![](https://i.imgur.com/C8DLNhF.gif)

<div class="alert alert-success" role="alert" markdown="1">
On est en train d'echantillonner le plan de Fourier
</div>

### Demonstration

$$
F_1[p_{\theta}](\rho) = F_2[f](\rho_{theta})
$$

<div class="alert alert-info" role="alert" markdown="1">
*Rappel*

$$
p_{\theta}(u) = \iint f(x)\delta(u-\theta \cdot x )dx
$$

</div>

Trasnformee de Fourier de $p_{\theta}$:

$$
\begin{aligned}
F_1[p_{\theta}](p) &= \int_{-\infty}^{+\infty}p_{\theta}(u)e^{-2i\pi\rho u}du\\
&=\color{orange}{\int_{-\infty}^{+\infty}}\iint f(x)\delta(u-\theta \cdot x )\color{orange}{e^{-2i\pi\rho u}du}dx
\end{aligned}
$$

On permute les integrales:

$$
\begin{aligned}
F_1[p_{\theta}](p) &=\color{orange}{\int_{-\infty}^{+\infty}}\iint f(x)\delta(u-\theta \cdot x )\color{orange}{e^{-2i\pi\rho u}du}dx\\
&= \iint f(x)\color{orange}{e^{-2i\pi\rho(x\cdot\theta)}}dx\\
&= \iint f(x)e^{-2-\pi x\cdot\rho\theta}dx\\
&= F_2[f](\rho\theta)
\end{aligned}
$$

## Etape 4

> Exploiter ce theoreme pour exprimer l'image en fonction de ses projections

$$
f(x)= \iint F_2[f](\nu)e^{2i\pi \nu\cdot x}d\nu
$$

Nous faisons un changement de coordonnees en coordonnees polaires:

$$
\nu = \rho\theta \to d\nu = \vert\rho\vert d\rho d\theta
$$

$$
\begin{aligned}
f(x)&=\int_0^{\pi}\color{orange}{\underbrace{\int_{-\infty}^{+\infty}F_2[f](\rho\theta)e^{2i\pi\rho\theta\cdot x}\vert\rho\vert d\rho}}d\theta\\
&\color{orange}{\int_{-\infty}^{+\infty}(\vert\rho\vert\times}\color{blue}{F_1[p_{\theta}](\rho)}\color{orange}{e^{2i\pi\rho\theta\cdot x}d\rho}\\
&= (h * p_{\theta})(u_{\theta}(x))\\
&= BP_{\theta}[h * p_{\theta}](x)
\end{aligned}
$$

<div class="alert alert-danger" role="alert" markdown="1">
C'est un filtre rampe

![](https://i.imgur.com/Fuw1kiz.png)

$$
\begin{aligned}
f(x) &= \int^{\pi}_0(h * p_{\theta})(u_{\theta}(x))d\theta\\
&= \int^{\pi}_0PB_{\theta}[h * p_{\theta}](x)d\theta\\
&= \int^{\pi}_0 FBP_{\theta}[p_{\theta}](x)d_{\theta}
\end{aligned}
$$

</div>

- Le theorime coupe-projection relie la projection et explique pourquoi la tomographie ca marche
- Back Projection $\theta$
- Changement de donnees de cartesien vers polaire

Rampe $p\to\vert p\vert$

$$
\begin{aligned}
\rho\to\vert \rho\vert &= \overbrace{(2i\pi\rho)}^{\color{red}{\text{derivee spartiale}}}times \frac{1}{2\pi}(\overbrace{-i\times\text{signe}(\rho)}^{\color{red}{\text{transformee de } \underline{\text{Hilbert}}}})\\
\phi(t) &= \int_{-\infty}^{+\infty} F_1[\phi](\rho)e^{2i\pi\rho t}d\rho\\
\phi'(t) &= \int_{-\infty}^{+\infty} F_1[\phi](\rho)(2i\pi\rho)e^{2i\pi\rho t}d\rho
\end{aligned}
$$

![](https://i.imgur.com/doA9W5x.png)


## Etape 5

<div class="alert alert-info" role="alert" markdown="1">
Formulation semi-discrete
</div>

- Seul l'echantillonnage angulaire est decrit: $N$ projections acquises aux angles $\{\theta_1,\dots,\theta_N\}$
- Le reste de la formule reste exprimee dans le domain continu

$$
f(x) = \int_{0}^{\pi}FBP_{\theta}[p_{\theta}]d\theta\\
\downarrow\\
f(x) = \frac{\pi}{N}\sum_{k=1}^NFBP_{\theta_k}[p_{\theta_k}](x)
$$

<div class="alert alert-info" role="alert" markdown="1">
Formulation discrete
</div>

- On inclut dans la discretisation, le caractere discret de dl'image et de sa projection
- TODO

# Unites des niveaux de gris

<div class="alert alert-danger" role="alert" markdown="1">
***Housnfield Units (HU)***

$$
HU = 1000\times \frac{\mu-\mu_{water}}{\mu_{water}-\mu_{air}}
$$

</div>

- Echelle normalisee et standard pour tous les appareils de tomodensitometrie (CT)
- Parfois utilsee avec un offset de  (sans offset : $Air = -1000$; avec offset : Air = 0 HU)
- Valeurs typiques (sans offset)
   - TODO