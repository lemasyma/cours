---
title:          "AN3D: Bases du rendu graphique"
date:           2021-09-23 10:00
categories:     [Image S9, AN3D]
tags:           [Image, S9, AN3D]
math: true
description: Bases du rendu graphique
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/r1Tywht7t)

[Site du prof](https://imagecomputing.net/damien.rohmer/teaching/epita-ani3d/)
# Contexte

On a l'habitude de voir des models 3D virtuels

![](https://i.imgur.com/u01jKut.png)

**Conclusion: il est aise de concevoir et animer ses propres modeles 3D**

<div class="alert alert-danger" role="alert" markdown="1">
FAUX !

![](https://i.imgur.com/Eqc2ra1.gif)

</div>

![](https://i.imgur.com/i4IU5xU.png)

Outils:
- Blender
- Maya

Formation de 3 a 5 ans dans les ecoles d'infographie.

<div class="alert alert-warning" role="alert" markdown="1">
Le cout/temp passe sur la 3D n'a jamais ete aussi elevve
</div>

- Films animations/VFX
    - Cout moyen par sequence VFX ($\lt10s$): 50k\$
    - Cout animation 3D $\gt$ cout dessin manuel
- Jeu videos AAA
    - 100M\$
    - 2 a 4 annees de dev

<div class="alert alert-success" role="alert" markdown="1">
Les outils 3D se sont ameliores

<div class="alert alert-warning" role="alert" markdown="1">
Mais restent complexes et tres techniques (3 ans d'etude infographistes)
</div>

</div>

## Creation 3D

La quantite et la qualite demande a augmente plus rapidement que les outils

![](https://i.imgur.com/j1GhnJL.png)

Dessins/sculpture a la main restent plus efficace pour le prototypage/design

![](https://i.imgur.com/smLhQ8P.png)

# Equipe: Geometric & visual computing

- Equipe informatique graphique et vision

## Applications

Domaine d'applications typiques
- Loisirs & creations artistiques
- Modelisation & visualisation en Sciences Naturelles
- Prototypage et fabrication

![](https://i.imgur.com/SAMrb0U.png)

Notre "expertise"
- Methode interactive pour l'aide a la creativite
- Simulation visuelles
- Analyses de formes et algorithmique

## Aide: stages, emploi, poursuite en Informatique Graphique ?

Rem. IG: Domaine technique, R&D avancee
- Lien fort sujets recherche et entreprise
- Theses IG - sujets appliques qui interessent les industries

Si le domaine vous interesse:
- AFIG

# Plan du cours

1. Introduction et rappels d'Info Graphique
2. Warm-up systeme de particules
3. Animation descriptive
4. Animation physique
5. Animation de personnages

# Evaluation

- Un compte rendu de tp
    - Collision de spheres, tissus, ou personnage articule
    - $\simeq5$ pages
    - Notre demarche, resultats et analyses

# Computer graphics

## Main subfields

- Modeling
- Animation
- Rendering

## Representing 3D shapes for Graphics Application

![](https://i.imgur.com/FW5kb8J.png)

- Computer graphics: mostly focus on representing surfaces
- Scientific visualization: volume data

# Surfaces
## Two main rpz

![](https://i.imgur.com/EZzXLmd.png)

Representation d'une sphere:

![](https://i.imgur.com/jERIWvo.png)

## Difficulty of surface representation using function

![](https://i.imgur.com/QYfYPFE.png)

<div class="alert alert-success" role="alert" markdown="1">
C'est impossible, la forme est trop complexe
</div>

## Objective of surface representation

Main idea: use **piecewise approximation**

Ideal surface representation
- Approximate well any surface
- Require few samples
- Can be rendered efficiently (GPU)
- Can be manipulated for modeling

Example of models:
- Mesh-based
    - Triangular meshes, polygonal meshes, subdivision surfaces
- Polynomial
    - Polynomial: bezier, spline NURBS
- Implicit
    - grid, skeleton based, RBF, MLS
- Points sets

<div class="alert alert-warning" role="alert" markdown="1">
For projective/rasterization render pipeline: always render **triangular meshes** at the end
</div>

| Pros                                | Cons                                              |
| ----------------------------------- | ------------------------------------------------- |
| Simplest representation             | Requires large number of saples: complex modeling |
| Fit to GPU Graphics render pipeline | Tangential discontinuities at edges               |

## Mesh encoding

![](https://i.imgur.com/zlsTRbg.png)

## Example of 3D Mesh File

![](https://i.imgur.com/8IjQD62.png)

## Affine transforms and 4D vectors/matrices

![](https://i.imgur.comeSghLb.png)

## Perspective matrix

Perspective space: allows perspective projection expressed as a matrix.

Common constraints (in OpenGL):
- Wrap the viewing volume (truncated cone with rectangulare basis called `frutsum`) ($z_{near},z_{far},\theta$) to a cube
    - $\theta: view angle$
    - $p=(x,y,z,1)\in$ `frutsum` $\Rightarrow p'=(x',y',z',1)\in[-1,1]^30$

![](https://i.imgur.com/iBPiF7P.png)

$$
M=\begin{pmatrix}
f&0&0&0\\
0&f&0&0\\
0&0&C&D\\
0&0&-1&0
\end{pmatrix}\\
f=\frac{1}{\tan(\frac{\theta}{2})}\\
L = z_{near}-z_{far}\\
C= \frac{z_{far}+z_{near}}{L}\\
D= \frac{2z_{far}z_{near}}{L}
$$

In practice
- You must define $z_{near}, z_{far}$
- $z_{far}-z_{near}$ should be as small as possible for max depth precsion

*To which view space are mapped 3D world space points at $z_{near}, z_{far}$ ?*



## Fractals

<div class="alert alert-info" role="alert" markdown="1">
**Idea**
Recursively add self-similar details
</div>
- Simple rule $\to$ complex shape
- May look like complex natural details

![](https://i.imgur.com/q1RWgcj.png)

![](https://i.imgur.com/g1AbmLt.png)

# Perlin noise

> A widely used *noise* function

Creer une fonction pseudo-aleatoire continue 
- MAIS deterministe

![](https://i.imgur.com/qKVLfFF.png)

On prend des echantillons a des valeurs entiere
- Pour chaque on associe une tangente
- Utilise une fonction de hash
    - `float hash(float n) {return fract(sin(n)*1e4);}`

![](https://i.imgur.com/y3v43UI.png)

## Fractal Perlin Noise

On somme la fonction avec elle-meme en changeant ses parametres

![](https://i.imgur.com/OUfFnot.png)

$$
g(x)=\sum_{k=0}^N\alpha^kf(\omega^kx)
$$

- $f$: smooth Perlin noise function
- $N$: number of Octave
- $\alpha$: persistency
- $\omega$: frequency gain

![](https://i.imgur.com/U4EnyRs.png)

## Usage

- Material texture ![](https://i.imgur.com/66Xbwo9.png)
    - Ridge effect
    - Marble effect
- Animated textures ![](https://i.imgur.com/AcTPFBz.png)
    - Translation: $f(x,y+t)$
    - Smooth evolution: $f(x,y,t)$
- Moutain-looking terrain ![](https://i.imgur.com/RLfIpqt.png)
    - $z=f(x,y)$

## Applications

In almost any complex shape

![](https://i.imgur.com/MXqfa2K.png)

## Exercice
### Perlin Noise terrain

$$
S(u,v)=\begin{cases}
x(u,v)=u\\
x(u,v)=v\\
z(u,v)=hg(s(u+o), s(v+o))
\end{cases}
$$

The perlin noise

$$
g(u,v)=\sum_{k=0}^N\alpha^kf(2^ku,2^kv)
$$

$$
N=9\\
\alpha=0.4\\
h=0.3\\
s=1\\
o=0
$$

![](https://i.imgur.com/B583AGv.png)

- b: $N$ modifie
- a: $s$ modifie
    - Les montagnes du fond sont des "nouvelles" montagnes
    - on voit plus loin
- f: $o$ modifie
- e: $h$ modifie

### Animation

Reference surface function:

$$
(u,v)\in[0,1]^2, f(u,v)=(u,v,0)
$$

*How to generate the following animations ?*

> **Help**
> Dimension of the Perlin noise ?
> Which parameter $(u,v,t-\text{time})$ ?

![](https://i.imgur.com/0Ec7T1C.png)

- a: axe $z$ qui change
    - $f(u,v)=(u,v,p(u+t))$
    - Faux! $u+t$ nous fait deplacer dans les $t$ negatifs
    - $f(u,v)=(u,v,p(u-t))$
- b: $f(u,v)=(u,v,p(u+t, v))$
- c: piege !
    - On a le droit au bruit de Perlin 3D
    - $(u,v,p(u,v,t))$

<div class="alert alert-warning" role="alert" markdown="1">
Quand on a des textures animees a partir de bruit de Perlin, il y a une dimension supplementaire: le temps
</div>

- d: similaire a la c
- e: $f(u,v)=(u,v,p(u-t)+up(u,v,t))$
    - Multiplication par $u$ car le bruit est plus important a la fin
- v: on ne change pas que $z$ cette fois
    - $f(u,v)=(u+p(u,v,t),v+p(u,v,t), p(u,v,t))$

# Geometry processing libraries

Development libraries
- LibIGL
- CGAL
- GeoGram

Viewer (+lib)
- Graphite
- Meshlab

Software
- Blender

## Useful CG programming library

Useful libs
- Eigen
- GLM
- Assimpl
- DevIL

Minimalistic GUI
- ImGui
- NanoGui
- AnTweakBar

Full framework
- Qt

# Particle system

<div class="alert alert-info" role="alert" markdown="1">
**Definition**
Element at a given position + extra parameters (mass, life time, etc)
</div>

On appelle un systeme de particules en oppositionL
- Rigid bodies - Solid objects with static shape
- Deformable bodies - Continuum material that can deforms

| Pros                                                               | Cons                                    |
|:------------------------------------------------------------------ |:--------------------------------------- |
| Lightweight rpz                                                    | Simple model from physics point of view |
| Generic flexible model (spatial deformation, no connectivity, etc) |                                         |

## Particles systems in History

One of the first animated model in CG

![](https://i.imgur.com/XtdBToN.png)

## Example of particle system

Free fall of sphere under gravity
- Geometrical rpz of each particle: sphere
- Equation of motion $p(t)=\frac{1}{2}gt^2+v_0t+p_0$
- Initial position and speed may be placed at random position
- Each particle may have a different life time

![](https://i.imgur.com/7JnMcfO.png)

*What are the parameters used for $p_0$ and $v_0$ in this example ?*

$$
p_0=(0,0,0)\\
v_0=(\sin(), 1,\cos())
$$

Si on a un $\sin$ du temps, on aurait des particules emises suivant un cercle

![](https://i.imgur.com/TvNbpJi.png)

![](https://i.imgur.com/e4r2WS8.gif)
> Genre comme ca

Or, nos particules ne suivent pas ce cerlce, elles suivent un *nombre aleatoire* $\theta$:

$$
v_0=(\sin(\theta), 1,\cos(\theta))
$$
> Par exemple, $\theta\in[-\pi,\pi]$

## Bouncing spheres

![](https://i.imgur.com/jCfHKDs.png)

*What is the equation of motion (taking into account the bouncing) ?*
- Considere a particle emited at time $t=0$
- At what time $t_i$, the particle touch the floor ?
- What is the new speed after impact ?
- What is the complete equation of trajectory ?

$$
t_i=\\
p(t)=\frac{1}{2}gt^2+v_0t\\
p_g(t_i)=0\\
\begin{aligned}
\frac{1}{2}g_yt_i^2+v_{og}t_i=0&\Rightarrow\frac{1}{2}g_yt_i=-v_{oy}\\
&\Rightarrow=-2\frac{v_{oy}}{g_y}
\end{aligned}\\
p(t_i)\quad v(t_i)\to\begin{pmatrix}
V_x\\
-V_y\\
V_z
\end{pmatrix}\\
p_2(t)=\frac{1}{2}g(t-t_i)^2+v'(t_i)(t-t_i)+p(t_i)
$$

## General motions

<div class="alert alert-success" role="alert" markdown="1">
Motion equation is not restricted to physics-based equations
</div>

![](https://i.imgur.com/zl1IM7g.png)

- *What are the parameters associated to each particle ?*
- *What are the corresponding equations of motions ?*

> On dirait que les bulles sortantes bougent en forme de cercle
> ![](https://i.imgur.com/gwbhk9v.png)

$$
\text{rand}\to[0,1]\\
p_0=(?,0,?)
$$

*Comment faisons-nous pour recreer le cercle ?*
> On randomise $x$ et $y$ entre $-1$ et $1$
> Or ca nous fais un carre et on veut un cercle
> On tire au hasard 2 rayons $r_1$ et $r_2$

![](https://i.imgur.com/EEnH3BF.png)

$$
\sqrt{r_1^2+r_2^2}\gt R\\
\begin{cases}
R\cos(\theta)\\
R\sin(\theta)
\end{cases}
$$
Avec:
- $r_1, r_2\in[0,R]$

<div class="alert alert-success" role="alert" markdown="1">

On a donc $p_0,v_0,R,C$

$$
p(t) = p_0+v_0(t-t_0)+\begin{pmatrix}
r\cos(\theta t-t_0+\gamma)\\
r\sin(\theta t-t_0+\gamma)\\
0
\end{pmatrix}
$$
Avec:
- $\gamma$: un offset aleatoire

</div>

# Billboards, impostors, sprites

<div class="alert alert-info" role="alert" markdown="1">
Particle can be displayed as small images/thumbnails
</div>

In practice:
- Each particle is displayed as a quadrangle
- A texture is mappe on the quad

![](https://i.imgur.com/tLjh77C.png)

- The texture can contains transparency

## Usage

Large use of billboard for complex models
- vegetation, fire, etc.

![](https://i.imgur.com/T5p1APs.png)

## Example

![](https://i.imgur.com/jZdp7aA.png)

## Use case in production

![](https://i.imgur.com/Rjp8OXX.png)
> Le seigneur des anneaux

*Comment on ete fait ces chevaux liquides ? Comment a ete filme la scene ?*
> Il n'y a que des vrais chevaux sur la scene
> Pour l'eau, les chevaux ont ete fait a partir d'emission de particules

![](https://i.imgur.com/JlSPnl2.png)
> Zoom sur une chute d'eau

![](https://i.imgur.com/sxllziI.png)
> La base des tetes de chevaux

![](https://i.imgur.com/2QKHdYi.png)
> Couches de particules emisent a partir des tetes

![](https://i.imgur.com/Ipb8kV5.png)
> Ensemble final

![](https://i.imgur.com/pQwFcQw.png)
> La riviere

![](https://i.imgur.com/cpbIk38.png)
> Les vrais chevaux, qui ne meurent pas

![](https://i.imgur.com/McEjuu0.png)
> Faux chevaux et cavaliers modelises pour etre emporte par la riviere

