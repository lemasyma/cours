---
title:          "PBR: Real-time Implementation"
date:           2021-09-17 10:00
categories:     [Image S9, PBR]
tags:           [Image, S9, PBR]
description: Real-time Implementation
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/BykhvaZXK)

[Site du cours](https://davidpeicho.github.io/teaching/)

# Before we start

*Comment on genere une image ?*
- On a vu le raytracing
- On a vu la rasterization

<div class="alert alert-success" role="alert" markdown="1">
On va se focus sur le temps reel avec de la rasterization
</div>

# Old Times

## Lambert

![](https://i.imgur.com/oleyxt6.png)

On a tous fait un Lambert model
- Plus l'angle est eleve entre la normal et la lumiere, moins il n'y a d'energie

<div class="alert alert-warning" role="alert" markdown="1">
Il n'y a pas de modele $100\%$ diffus
</div>

<div class="alert alert-success" role="alert" markdown="1">
En une seule operation on a notre BRDF
</div>
> Il existe d'autres modeles mais la difference visuelle n'est pas assez bonne pour etre utilises

## Phong

![](https://i.imgur.com/eFnmhj1.png)

- Approximation pas tres bonne
- MAIS precurseur a son epoque ($'70s$)

Pas de conservation d'energie:
![](https://i.imgur.com/yKPb7ft.png)

## Pseudocode

### Lambert

```glsl
void main()
{
 vec3 diffuse = kD * dot(normal, lightDirection) * color;
 gl_FragColor.rgba = vec4(diffuse, 1.0);
}
```

### Phong

```glsl
void main()
{
 vec3 r = reflect(- viewDirection, normal);
 vec3 diffuse = kD * dot(normal, lightDirection) * color;
 vec3 specular = kS * pow(max(dot(lightDirection, r)), exponent);
 gl_FragColor.rgba = vec4(diffuse + specular, 1.0);
}
```

# What and why

## Introduction

<div class="alert alert-warning" role="alert" markdown="1">
Non-physical model requires a lot of tweaking
</div>

> Si on a un artiste qui fait une scene en exterieur puis on lui dit qu'on doit aller dans un tunnel en voiture, l'artiste pleure
> Il doit *tweaker* les materiaux pour que ca ait l'air joli en fonction de la lumiere

<div class="alert alert-success" role="alert" markdown="1">
C'est pour ca qu'il y a eu l'avenement du **Real Time Rendering** vers 2013
</div>

<div class="alert alert-warning" role="alert" markdown="1">
C'est dur de definir le PBR
</div>

<div class="alert alert-info" role="alert" markdown="1">
**Definition: PBR**
Modele mathematiques et approximations que nous allons tous suivre pour decrire les interactions entre la lumiere et la matiere
</div>

## What is PBR ?

![](https://i.imgur.com/opZAa4s.png)

*Pourquoi c'est populaire ?*
> Decrit le monde plus precisement, donne des rendus realistes
> Tout le monde utilise plus ou moins les memes inputs
> Moins de tweaking

<div class="alert alert-success" role="alert" markdown="1">
Win-win pour les ingenieurs et artistes
</div>

# Microfacets Theory

![](https://i.imgur.com/Kgyv2AT.png)
> Ce modele approxime ce qu'il se passe dans la vraie vie

<div class="alert alert-info" role="alert" markdown="1">
On dit que tous les materiaux sont composes de miroirs plus ou moins alignes
</div>

![](https://i.imgur.com/3xOhCri.png)

![](https://i.imgur.com/DCGx8E9.png)

*C'est quoi la difference entre un miroir et un plastique ?*
> Notre premier cas sera un miroir
> Le second est un materiaux super diffus

# Dielectrics vs Conductors

![](https://i.imgur.com/BehJABt.png)

## Conductors

![](https://i.imgur.com/FLY4bUa.png)

La couleur diffuse serait une approximation du sub-surface scattering

![](https://i.imgur.com/2nt0t5nAd.png)
- Les conducteurs reflete $0-20\%$ de la lumiere

<div class="alert alert-warning" role="alert" markdown="1">
Les metaux n'ont pas de sub-surface scattering
</div>

![](https://i.imgur.com/LiDb9rJ.png)
- Les conducteurs refletent $60-90\%$ de la lumiere
- Certains conducteurs ont leur couleur propre due aux longueurs d'ondes absorbees

# BRDF

## BRDF Simplification

$$
f_r(p,\omega_0,\omega_i)=f_d(p,\omega_0,\omega_i) + f_s(p,\omega_0, \omega_i)
$$

![](https://i.imgur.com/teFQIK6.png)

<div class="alert alert-success" role="alert" markdown="1">
Notre BRDF devient pulg & play
</div>
> On peut remplacer par ce qu'on veut du moment que $\int\le1$

## Implementation notes

$$
f_r(p,\omega_0,\omega_i)=k_df_d(p,\omega_0,\omega_i) + k_sf_s(p,\omega_0, \omega_i)\\
k_d+k_d\le1
$$

## Diffuse Lobe

$$
f_d(p,\omega_0,\omega_i) = \frac{\rho}{\pi}
$$
- $\rho$: reflectance spectrum

![](https://i.imgur.com/D4TjB54.png)

## Specular Lobe

$$
f_s(p,\omega_0,\omega_i)=\frac{D(\omega_0,\omega_i)F(\omega_0,\omega_i)G(\omega_0,\omega_i)}{4(\omega_0,\omega_i)(\omega_i\times n)}
$$

![](https://i.imgur.com/AQemlwI.png)


### Specular BRDF

$$
D_{GGX}(n,h,a)=\frac{\alpha^2}{\pi((n\times h)^2(\alpha^2-1)+1)^2}\\
\vec h=\frac{\vec v+\vec L}{\Vert\vec v+\vec L\Vert}
$$
- Normal distribution function $D(\omega_0, \omega_i)$
- Estimates the area of microfacets aligned to give perfect specular
- As usual, lots of different NDF equations...
- To be consistent, let's implement the Trowbridge-Reitz equation
- Low roughness means few samples contributing a lot to specular

![](https://i.imgur.com/FGdwVds.png)

### Shadowing term $G(\omega_0,\omega_i)$

![](https://i.imgur.com/zblR4rX.png)

$$
G(n,v,l,k)=\underbrace{G_{SchlickGGX}(n,v,k)}_{Obstruction}\underbrace{G_{Schlik}(n,l,k)}_{Shadowing}\\
G_{SchlickGGX}(n,v,k)=\frac{n\times v}{(n\times v)(1-k)+k}
$$
- On va approximer $k=\alpha$
- Approximation de l'occlusion

<div class="alert alert-warning" role="alert" markdown="1">
L'orientation des facettes peut *pieger* la lumiere
</div>

![](https://i.imgur.com/jBMa2j0.png)

### Effet Fresnel

![](https://i.imgur.com/acaVBPu.png)
> On a un joli coucher de soleil sur la mer (ou ocean)
> L'eau est un miroir modulo les vagues

<div class="alert alert-info" role="alert" markdown="1">
Pour tout materiaux, la reflectance va etre maximale aux **angles rasants**
</div>

<div class="alert alert-danger" role="alert" markdown="1">
L'effet Fresnel c'est le poids du *specular lobe* $k_s$
</div>

$$
F_{Schlik}(v,h,f_0,f_{90}) = f_0+(f_{90}-f_0)(1-v\times h)^5\\
F_{Schlik}(v,h,f_0) = f_0+(1-f_0)(1-v\times h)^5\\
F_0(ior)=\frac{(1-ior)^2}{(ior+1)^2}
$$
- $f_0$: base reflectivity at normal incidence
- $f_{90}$: base reflectivity at grazing angle
    - Almost always 1 for conductors

![](https://i.imgur.com/yqpy1aK.png)

![](https://i.imgur.com/3Sz2oqI.png)
> Fresnel reflectance for common materials

- For dialectics, $f_0$ is often approximated with $0.04$
- Some materials $f_0$ are tainted (gold, copper)
- Implementation note:
    - For dielectics, pick $0.04$ $f_0$
    - For conductors, store $f_0$ in albedo texture
    - Use *metallic* input to lerp between the 2

## Demo !

![](https://i.imgur.com/1MkiBjt.png)

### Direct-Lightning pseudocode

```glsl
vec3 radiance = vec3(0.0);
for(int i = 0; i < NB_LIGHTS; ++i)
{
 vec3 w_i = lights[i].direction;
 vec3 kS = FresnelShlick(f0, wi, w_o);
 vec3 specularBRDFEval = kS * f_s(p, w_i, w_o);
 vec3 diffuseBRDFEval = (1.0 - kS) * f_d(p, w_i, w_o);

 radiance += (diffuseBRDFEval + specularBRDFEval) * sampleLight(lights[i], p, w_i) * dot(normal, w_i);
}

```

## Textures

![](https://i.imgur.com/YnKZiob.png)
> Les artistes font plusieurs textures

## To remember !

- Diffuse is an approximation of sub-surface scattering
- La plupart des moteurs connus vont avoir des *metallics workflow*
- Ca simplifie beaucoup la vie

# Ponctual light

# Point light

- Infinitely small
- Isotropic
- Describe only by a position
- Simple to code and fast to sample
- Power unit should be set using **Lumens**
- How to select a proper value ?
- Not as accurate as **Area Light**

$$
L_i(p,\omega_i)=\frac{\phi}{4\pi r^2}n\times\omega_i
$$

![](https://i.imgur.comvZM6gv.png)

<div class="alert alert-warning" role="alert" markdown="1">
Cette lumiere n'existe pas dans la vraie vie
</div>

### Note

- On ne va pas parler de directionnal light (deja fait)
- Si on utilise une directionnal light, il faudra tweaker les parametres
- Ce n'est pas aussi fidele que les **Area lights**

# Image Based Lightning

![](https://i.imgur.com/F1YWzrP.png)
- 4 points lights

![](https://i.imgur.com/dbOlXwe.png)
- Avec environnement

$$
L_0(p,\omega_0)=\int_{\Omega}(f_d(p,\omega_0,\omega_i) + f_s(p,\omega_0,\omega_i))L_i(p,\omega_i)n\times w_i\\
L_0(p,\omega_0)=\int_{\Omega}f_d(p,\omega_0,\omega_i)L_i(p,\omega_i)m\times\omega_i+\int_{\Omega}f_s(p,\omega_0,\omega_i)L_i(p,\omega_i)m\times\omega_i
$$

## IBL Diffuse

$$
\int_{\Omega}f_d(p,\omega_0,\omega_i)L_i(p,\omega_i)m\times\omega_i
$$

![](https://i.imgur.com/QnEpTEC.png)

*Mais c'est juste un flou gaussien ?*
> C'est pas si faux que ca, c'est assez proche

$$
L_0(p,n)=\int_{\Omega}\frac{\rho}{\pi}L_i(p,\omega_i)n\times\omega_id\omega_i\\
L_0(p,n)=\frac{\rho}{\pi}\int_{\Omega}L_i(p,\omega_i)n\times\omega_id\omega_i\\
$$

Il faut faire une integration par angle solide, et c'est complique.

![](https://i.imgur.com/TTsOV4U.png)

- Utilisation des coordonnees spheriques pour l'integration
- Discretiser l'integrale avec la somme de Riemann 
- Calculer pour chaque texel, avec la direction $N$ du centre

## IBL Specular

$$
\int_{\Omega}f_s(p,\omega_0,\omega_i)L_i(p,\omega_i)m\times\omega_i
$$

![](https://i.imgur.com/8rspkCX.png)

$$
L_0(p,\omega_0)=\int_{\Omega}L_i(p,\omega_i)d\omega_i\times\int_{\Omega}f_r(p,\omega_0,\omega_i)n\times\omega_i d\omega_i
$$

![](https://i.imgur.com/9dMsNTc.png)
> Ca a ete teste et ca marche: c'est ca la 3D

Changer le niveau de roughness c'est faire du downsampling, pourquoi par appliquer la roughness en faisant des images de plus en plus petites

![](https://i.imgur.com/Z9XpfPY.png)

### Pre-computed BRDF

$$
\begin{aligned}
\int_{\Omega}f_r(p,\omega_0,\omega_i)n\times\omega_id\omega_i &= F_0\int_{\Omega}f_r(p,\omega_0,\omega_i)(1-(1-\omega_0\times h)^5)n\times\omega_id\omega_i\\
&+\int_{\Omega}f_r(p,\omega_0,\omega_i)(1-\omega_0\times h)^5n\times\omega_id\omega_i
\end{aligned}
$$
> Obtained bu substituting Fresnel Shlick
> Only 2 inputs left: roughness, viewing angle

![](https://i.imgur.com/pAtF0cE.png)

At runtime:
1. Fetch pre-integrated BRDF texture
2. Fetch convoluted environment
3. Apply the above equation to get the full specular component

### Specular: compisistion

```glsl
c2 brdf = GetIntegratedBRDF(NdotV, roughness);
vec3 prefilteredSpecular = GetPrefilteredSpecular((NdotV, roughness);
vec3 specular = prefilteredSpecular * (F * brdf.x + brdf.y);
```
- `F`: Fresnel term

## To remember

- C'est juste du pre-filtering

# Colorspace and color precision

![](https://i.imgur.com/uCfnJup.png)

- sRGB vs Linear
- Monitors apply pow function to luminance
- Toute l'industrie a du se base sur les ecran qui font ca donc ils ont cree le $sRGB$
- Sur photoshop, une image sera encodee en sRGB pour retrouver les couleurs imaginees

<div class="alert alert-warning" role="alert" markdown="1">
On va eviter de faire nos calculs en sRGB
</div>
- Soit on fait tout en sRGB
- Soit on fait tout en lineaire $\Rightarrow$ **OUI**
    - On applique a la fin la fonction sRGB pour convertir en lineaire

## HDR vs LDR

![](https://i.imgur.com/Azsqnoz.png)

<div class="alert alert-info" role="alert" markdown="1">
HDR: High Dynamic Range
</div>

Reinhard Tonemapping:
$$
color_{final}=\frac{c}{c+1}
$$
- HDR has larger range of values
- Units will create radiance color outside the $0\dots1$ range
- Perform computation in HDR, tonemap to LDR is required
- HDR is required to get correct PBR result
- Especially important for IBL

# Going further

## Advanced materials

![](https://i.imgur.com/SmKlFAT.png)
> Examples: hair, skin, cloud, etc.

