---
title:          "RVAU: Moteur 3D"
date:           2021-09-29 11:15
categories:     [Image S9, RVAU]
tags:           [Image, S9, RVAU]
math: true
description: Moteur 3D
---

Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/rysnpo-VK)

*Qu'est-ce qu'un moteur 3D ?*
> Un logiciel qui permet de modeler un environnement 3D
> Permet de representer un environnement avec les interactions physique

# Moteur 3D

- Scene
    - Objets
    - Cameras
    - Lumieres
    - etc

Graphe de scene:
- Pour manipuler les objets 3D de la scene
![](https://i.imgur.com/JDQ2m8T.png)

- Utilise une API 3D bas niveau

![](https://i.imgur.com/8BmhvTf.png)

## Composants

![](https://i.imgur.com/3ZCyBcS.png)

## Editeur

<div class="alert alert-info" role="alert" markdown="1">
Editeur/environnement de developpement
</div>

![](https://i.imgur.com/FWBqFjh.png)

## Import de modeles 3D

![](https://i.imgur.com/tgqHFN9.png)
- C'est la jungle pour les extensions de format 3D

<div class="alert alert-danger" role="alert" markdown="1">
Differentiation entre les formats 3D
</div>
- Infographie 3D
- CAO

![](https://i.imgur.com/mBVc2hy.png)

# Modelisation CAO

- Operations parametriques
    - Extrusion ![](https://i.imgur.com/CFQTvsk.png)
    - Revolution ![](https://i.imgur.com/m0q6BPF.png)
    - Conge ![](https://i.imgur.com/YXJyPT6.png)
    - Chanfrein ![](https://i.imgur.com/IosVIkM.png)
- Operations booleennes
    - Geometrie de constructions de solides (CSG)

![](https://i.imgur.com/OC9ONNk.png)

## Tesselation

<div class="alert alert-info" role="alert" markdown="1">
Creation d'un maillage: passage d'un modele CAO a un modele triangule
</div>

![](https://i.imgur.com/Msqn8Pd.png)

![](https://i.imgur.com/Ol13z5C.png)

## Imports de modeles 3D

- Import de modeles tesselles

Pour unity:
- **Autodesk FBX `.fbx`**
- Collada `.dae`
- Wavefront `.obj`
- Autodesk 3DS `.3ds`
- AutoCAD Drawig eXchange Format `.dxf`

# Exemples de moteurs 3D

![](https://i.imgur.com/3bXbAeH.png)

# Unity

![Uploading file..._2z0gxblts]()

## Projet

- Assets
- ProjectSettings

![](https://i.imgur.com/ENqul6O.png)

![](https://i.imgur.com/czjwRau.png)

## Hierarchy

- Gestion du graphe de scene

## GameObject

- Transform
- Ensemble de composants

![](https://i.imgur.com/Yn1bVIU.png)

## Composant

- Derive de la classe MonoBehaviour

![](https://i.imgur.com/raUei5t.png)

## Monobehavior

- Functions callback
    - `Start()`
    - `Update()`
    - `FixedUpdate()`
    - `LateUpdate()`
    - `OnGUI()`
        - Tous les appels dedies a l'interface graphique/affichage

![](https://i.imgur.com/8g24eCG.png)

<div class="alert alert-warning" role="alert" markdown="1">
C'est du **mono-thread**
</div>

# Documentation Unity

![](https://i.imgur.com/tkRfX5y.png)

# Assets Store

![](https://i.imgur.com/LvM6M1Z.jpg)
