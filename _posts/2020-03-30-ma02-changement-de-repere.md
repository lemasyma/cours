---
layout: post
title:  CAMA : ma02
date:   2020-03-30 10:00
tags:   CAMA Shannon
description: Changement de repere
---

# CAMA : ma02 Changement de repere
# Cours du 30 / 03

## Matrice de passage
Une matrice peut representer un changement de repere : 
```python=
O = np.array((0,0))
I = np.array((1,0))
J = np.array((0,1))

A = np.array((3,3))
B = np.array((5,4))
C = np.array((1.5,4))
```
![](https://i.imgur.com/23vasZo.png)
:::danger
La matrice de passage sans la translation est l'ensemble des vecteurs de la seconde base exprimes dans la premiere.
```python=
D = np.array([(B-A), (C-A)]).T  # déformation sans la translation
```
```
array([[ 2. , -1.5],
       [ 1. ,  1. ]])
```
:::

### Vecteurs dans le nouveau repère
On exprime le vecteur $OJ$ dans la base rouge en utilisant la matrice de passage (l'origine d'un repere n'est pas utile pour un vecteur) :
```python=
D @ (J-O) # donne AC
```
```
array([-1.5,  1. ])
```
### Points dans le nouveau repère
Il faut prendre en compte la translation d'un repere d'un repere vers l'autre en separant la deformation de la translation pour rester en 2D : 
```python=
A + D @ I  #  passage de I en B
```
```
array([5., 4.])
```
On peut integrer la translation dans une matrice d'une dimension superieure (cf ma01).
```python=
P = np.identity(3) # definie la taille et initialise la derniere ligne (les autres seront remplacees)
P[:2, :2] = D      # deformation
P[:2, 2] = A       # translation
```
```
array([[ 2. , -1.5,  3. ],
       [ 1. ,  1. ,  3. ],
       [ 0. ,  0. ,  1. ]])
```
```python=
def to3D(x):
    if len(x.shape) == 1:
        return np.array([*x,1])
    elif len(x.shape) == 2:
        return np.array([*x,np.ones(len(x[0]))])
```
```python=
P @ to3D(J)  # is C
```
```
array([1.5, 4. , 1. ])
```
## Une application linéaire transposée dans le nouveau repère
Appliquons une rotation qui prend un point et le fais tourner dans le sens trigonométrique de θ autour de (0,0).
*Que fait cette rotation dans notre nouveau repere?*
* on applique plusieurs fois une rotation au point (1,0) autour de O (le cercle bleu)
* on déforme le cercle bleu avec la matrice de passage P  (la forme noire)
* on applique plusieurs fois la rotation déformée par P du point B autour de A (la forme orange pointillé)

:::danger
Pour calculer la rotation R dans le nouveau repere : 
$$Q = P \, R \, P^{-1}$$
avec  $P^{-1}$ permettant de revenir au repere d'origine pour effectuer la rotation
:::
```python=
def Rot(θ):
    return np.array([[np.cos(θ), -np.sin(θ)], [np.sin(θ), np.cos(θ)]])

def Rot3D(θ):
    return np.array([[np.cos(θ), -np.sin(θ), 0], [np.sin(θ), np.cos(θ), 0], [0, 0, 1]])
```
```python= 
# plusieurs rotation qui donnent le cercle bleu :
cercle = np.array([Rot(α) @ I for α in np.linspace(0, 2*np.pi, 10)]).T

# le cercle exprimé dans le nouveau repère (noir)
p_cercle = P @ to3D(cercle)

# construction de Q
Q = lambda θ: P @ Rot3D(θ) @ lin.inv(P)  # définition de Q en fonction de θ

# on applique Q pour faire tourner B autour de A (orange)
p_rot_A = np.array([Q(α) @ to3D(B) for α in np.linspace(0, 2*np.pi, 10)]).T 
```
![](https://i.imgur.com/5y3SBqb.png)
