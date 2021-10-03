---
title:          "AN3D: Interpolate position"
date:           2021-09-24 10:00
categories:     [Image S9, AN3D]
tags:           [Image, S9, AN3D]
math: true
description: Interpolate position
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/rkfLOWsmF)

# Animation in Computer Graphics

2 main ways to describe animation

1. Kinematics
2. Dynamics

Ways to genre animation

1. Descriptive animation
2. Motion tracking
3. Procedural generation
4. Physically based simulation
5. Leaning-based synthesis

![](https://i.imgur.com/GNzkbnR.png)

## Descriptive Animation

<div class="alert alert-info" role="alert" markdown="1">
The artist/an algorithm fully describes the motion and deformation
</div>

| Pros                       | Cons                              |
| -------------------------- |:--------------------------------- |
| Full control on the result | May introduce un-physical effects |

## History of CG Animation

First production of animated films (Disney)

<div class="alert alert-info" role="alert" markdown="1">
**Principle**
- Animator in chief: create *key frames*
- Assistants: fill the *in between* (secondary drawings)
</div>

Principle of Key Framing:
![](https://i.imgur.com/Px3ykmn.png)

## Key framing in CG

- Create *manually* a set of key frames
- Interpolate positions

# Production pipeline: Interpolate position

- Given a set of key positions (pos + time), we want to find an interpolating space-time curve

![](https://i.imgur.com/xJzguUM.png)

- Input: $(p_i, t_i)$

## Linear Interpolation

![](https://i.imgur.com/NWL7kme.png)

![](https://i.imgur.com/cbva620.png)

| Pros                             | Cons                        |
| -------------------------------- |:--------------------------- |
| Simple                           | Non smooth trajectory       |
| Constant speed between keyframes | Generates straight segments |

## Smooth curve

![](https://i.imgur.com/MFclrg4.png)
- $\alpha_i$ polynomial basis function of degree $d$

*Which polynomial/degree choose ?*

## Lagrange polynomial interpolation

<div class="alert alert-info" role="alert" markdown="1">
Interpolate all points at once
</div>

![](https://i.imgur.com/7pL9OQV.png)

Degree of polynomial: $N-1$

<div class="alert alert-success" role="alert" markdown="1">
**Known solution: Lagrange polynomial**

![](https://i.imgur.com/ePjYO45.png)

</div>

### Comparison

![](https://i.imgur.com/owXSuhn.png)

<div class="alert alert-warning" role="alert" markdown="1">
En pratique, on n'utilise jamais cette interpolation
</div>

## Spline

<div class="alert alert-info" role="alert" markdown="1">
**Idea**
- Define each part a polynomial
- Smooth junctions between them
</div>

![](https://i.imgur.com/xDZVgdQ.png)

How to choose the polynomial
- Sufficiently high degree to be smooth
- Sufficiently low degree to avoid oscillations

<div class="alert alert-success" role="alert" markdown="1">
In Graphics, cubic polynomials are often used
> Allow up to $\mathcal C^2$ junctions
</div>

## Hermite interpolation

<div class="alert alert-info" role="alert" markdown="1">
Cubic curve interpolationg points and derivatives at extermities
</div>

![](https://i.imgur.com/uQ9G7N8.png)

## Interpolating curve

Initial problem: set of multiple keyframes position+time

2 solutions:
- Set explicitely derivatives for each keyframe - *teadious*
- Compute automatically plausible derivatives from surrounding samples - *often used*

### Cardinal spline:

Set:

$$
d_i=\mu\frac{p_{i+1}-p_{i-1}}{t_{i+1}-t_{i-1}}
$$

- $\mu$ curve tension $\in[0,2]$
- $\mu = 1$ is commonly used 
    - *Catmull Rom Spline*

![](https://i.imgur.com/EYz4uwc.png)

## Wrap-up algorithm

Compute $p(t)$ as a cubic spline interpolation
- Given keyframes $(p_i, t_i)_{i\in[0,N-1]}$
- Given time $t\in[t_1,t_{N-2}]$

![](https://i.imgur.com/6zQAcFe.png)

1. find $i$ such that $t\in[t_i,t_{i+1}]$
2. Compute $$d_i=\mu\frac{p_{i+1}-p_{i-1}}{t_{i+1}-t_{i-1}}$$ and $$d_{i+1}=\mu\frac{p_{i+2}-p_{i}}{t_{i+2}-t_{i}}$$
3. Compute $$p(t) = (2s^3-3s^2+1)p_i + (s^3-2s^2+s)d_i + (-2s^3+3s^3)p_{i+1} + (s^3-s^2)d_{i+1}$$
    - with $s=\frac{t-t_i}{t_{i+1}-t_i}$

## Limitation of cubic curve interpolation

- Only $\mathcal C^1$, but not $\mathcal C^2$ at junctions: curvature/acceleration discontinuity
- Non-constant peed along each polynomial

## Curve editing

- Animation software (Maya, 3DSMax, Blender, etc) always come with a *curve editor*
- Artists can manually ajust their position, time, and **derivatives** on curve editor
    - One curve for each scalar parameter
        - position $(x,t,z)$
        - scaling $(s_x,s_y,s_z)$
        - rotation/quaternion
- Can also use a wrapper function $w$ to change time $p(t) = f(w(t))$

![](https://i.imgur.com/YkPhgqi.png)

## Usage of keyframes interpolation

<div class="alert alert-info" role="alert" markdown="1">
Interpolate every vertex of multiple meshes
</div>

![](https://i.imgur.com/pkuTH3W.png)

## Multi-target blending

Interpolate between multiple key poses
- Interesting for facial animation

- Per-vertez formulation $p_i(t)=\sum_{k}^{N_{poses}}$

## Blend shapes

$$
p_i(t) = b_i^0 + \sum_k^{N_{poses}}\omega_k(t)(\underbrace{b_{ki}-b_i^0})
$$

# Physically-based simulation
## When physically based simulation is needed

- Accurate dynamics
- Teadious to model by hand or procedurally
    - Multiple interacting elements
    - Complex animated geometry

## Material model

- Elasticity
    - Purely elastic models don't loose energy when deformed
- Plasiticity
    - Ductile material: can allow large amout of plastic deformation without breaking (plastic)
    - Brittle - Opposite (glass)
- Viscosity
    - Resistance to flow (usually for fluid, *ex:honey*)

In reality
- Elasto-plastic materials
    - Allow elastic behavior for small deformation, and plastic at larger one
- Visco-elastic materials
    - Elastic properties with delay

# Rigid spheres

![](https://i.imgur.com/zGLqPpa.png)

## System modeling

Particles modeling the center of hard spheres
- Spheres can collide with surrounding obstacles
- Spheres can collide with each others

System: $N$ particles with position $p_i$, speed $v_i$, mass $m_i$, modeling a sphere of radius $r_i$
- initial conditions: $p_i(0)=p_i^0,v_i(0)=v_i^0$

Forces: $F_i=$

![](https://i.imgur.com/NoMSt6P.png)

$$
v^{k+1} = v^k+hg\\
p^{k+1}=p^j+hv^{k+1}
$$

# Collision with a plane

Plane $\mathcal P$: parameterized using a point $a$ and its normal $n$

$$
\{p\in\mathbb R^3\in\mathcal P\Rightarrow (p-1)\cdot n =0\}
$$
- Sphere above plane: $(p_i-1)\cdot n\gt r_i$
- Sphere in collision: $(p_i-a)\cdot n\le r_i$

![](https://i.imgur.com/Bc3pALN.png)


```cpp
for (int i = 0; i < N; ++i) {
    float detection = dot(p[i]-a, n);
    if (detection <= r[i]) {
        // ... collision response
    }
}
```

## Collision response with plane

*What should we do when a collision is detected ?*
> On peut changer la vitesse
> ![](https://i.imgur.com/qhXT43l.png)

<div class="alert alert-success" role="alert" markdown="1">
On decompose la vitesse selon 2 composantes: la tangente et la normale
</div>

$$
\vec v\begin{cases}
v_n\to &-v_n\\
&+\\
v_r\to &v_t
\end{cases}\\
\text{composante normale: } (\vec v\cdot\vec n)=v_n\\
\text{composante tangente: }\vec v-v_n\vec n
$$

<div class="alert alert-danger" role="alert" markdown="1">
Collision response = **Update speed**
</div>

### Result

<div class="alert alert-info" role="alert" markdown="1">
Applying collision response on speed only
</div>

![](https://i.imgur.com/s8WRrZK.png)
> Les boules tombent en-dessous du plan

<div class="alert alert-warning" role="alert" markdown="1">
Quand notre sphere rebondit, il est possible qu'une partie passe au travers du plan, donc on considere en collision, donc on inverse sa vitesse, donc en collision, etc
</div>

*Comment on contre ca ?*
> Si ma sphere est dans le sol, on s'arrange pour qu'elle ne soit pas dans le sol
> On la "repousse" pour qu'elle soit en contact avec la surface

## Collision response with a plane: position

Three possibilities:
1. Correct position in projecting on the constraint
    - Pros: simple to implement
    - Cons: Physically incorrect position
3. Approximate the correct position
4. Go backward in time to find exact instant of collision
    - Continuouse collision detectino
    - Pros: physically correct
    - Cons: Computationally heavy

![](https://i.imgur.com/cIjW5w8.png)

### Result

![](https://i.imgur.com/7MXFMCj.png)
> Ca marche !

$$
p_i^{new} = p_i+d_n
$$

# Collision between speheres

Given 1 spheres $(p_1, v_1, r_2, m_2), (p_2, v_2, r_2, m_2)$

Collision when

$$
\Vert p_1-p_2\Vert\le r_1+r_2
$$

![](https://i.imgur.com/Gk7x6DO.png)

*What will happen with speeds ?*
> $v_1\to v_1^{new}, v_2\to v_2^{new}$

## Notion of impulse

An impulse $J$ is the integrted force over time

$$
J=\int_{t_1}^{t_2}F(t)dt
$$

<div class="alert alert-warning" role="alert" markdown="1">
Result in a sudden change of speed (momentum) in a discrete case
</div>

For a particle with a constant mass

$$
\int_{t_1}^{t_2} F(t)dt=\int_{t_1}^{t_2} ma(t)dt
$$

## 2 spheres in collision

![](https://i.imgur.com/Pao0ouU.png)
> J'ecris pas ca vous etes fous

![](https://i.imgur.com/ofvC6R7.png)

![](https://i.imgur.com/ikzMec2.png)

## Summary
1. Detect collision $\Vert p_1-p_2\Vert\le r_1+r_2$
2. if collision (relative speed$\gt\epsilon$)
    - Elastic collision (bouncing) $v_{1/2}=\alpha v_{1/2}\pm\beta \frac{J}{m_{1/2}}$
    - If *static* contact (relative speed $\le\epsilon$)
        - Friction $v_{1/2}=\mu v_{1/2},\mu\in[0,1]$
        - Avoids *jittering*
3. Correct position (project on contact surface)
    - $p=p+\frac{d}{2u}$
    - $d=r_1+r_2-\Vert p_1-p_2\Vert$: collision depth
    - For small impacts, can use *position based dynamics*
        - $v^{new} = \frac{(p^{new}-p^{prev})}{\delta t}$

## Note on collision stack

Optimiser ne pas avoir a simuler les spheres sur le sol et immobiles
- Faire des graphes des solides et les traiter comme des solides rigides

# Modeling elastic shapes with particles

<div class="alert alert-info" role="alert" markdown="1">
**Spring mass systems**
- Particles: samples on shape
- Springs: link closed-by particles in the reference shape
</div>

## Spring structure

How to model spring connectivity ?
- Structutal springs
    - 1-ring neighbors springs ($\simeq$ mesh edges)
    - Pros: limit elongation/contraction
    - Cons: Allows shearing, and bending
    - ![](https://i.imgur.com/GLtjfce.png)
    - **Add extra springs connectivity**
- Shearing springs
    - Diagonal links
- Bending springs
    - 2-ring neighborhood
    - ![](https://i.imgur.com/ajKTQz8.png)

# Cloth simulation
## Mass-spring cloth simulation

- Particles are sampled on a $N\times N$ grid
    - Each particle has a mass $m$
- Set structural, shearing and bending springs

![](https://i.imgur.com/XEQcEBu.png)

## Forces

- On each particle: gravity + drag + spring forces

$$
F_i(p,v,t)=m_ig-\underbrace{\mu v_i(t)}_{\text{facteur d'attenuation}}+\sum_{j\in\nu_i}K_{ij}(\Vert p_j(t)-p_i(t)\Vert-L_{ij}^0)\frac{p_i(t)-p_i(t)}{\Vert p_j(t) -p_i(t)\Vert}
$$
- $\nu_i$: neighborhood of particle $i$
- $L_{ij}^0$: rest length of spring $ij$

Associated ODE

$$
\forall i
\begin{cases}
p_i'(t) = v_i(t)\\
v_i'(t)=F_i(p,v,t)
\end{cases}
$$