---
title:          "EPIQUANTI : Architecture d'un ordinateur quantique et technologies habilitantes"
date:           2021-10-12 14:00
categories:     [tronc commun S9, EPIQUANTI]
tags:           [tronc commun, EPIQUANTI, S9]
math: true
---

Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/ryztYlXBK)

Lien du [livre du prof](https://www.oezratty.net/wordpress/2021/understanding-quantum-technologies-2021/)

[Slide du cours](https://www.oezratty.net/Files/Work/Olivier%20Ezratty%20Quantique%20EPITA%205B%20Oct2021.pdf)

![](https://i.imgur.com/k5BEC4V.png)

<div class="alert alert-warning" role="alert" markdown="1">
La correction d'erreur "normale" est tres differente de celle de l'informatique quantique
</div>

# QEC Zoo

![](https://i.imgur.com/Lk6GIhP.png)

## Envoyer un Qubit

<div class="alert alert-info" role="alert" markdown="1">
Principe general

![](https://i.imgur.com/FoU49xy.png)

</div>

## Shor 9 error correction code

![](https://i.imgur.com/zNR7YEN.png)

## Surface code QEC

<div class="alert alert-info" role="alert" markdown="1">
QEC adapted to 2D bit architectures like with superconductors from Google

![](https://i.imgur.com/VVEs4Wq.png)

</div>

<div class="alert alert-warning" role="alert" markdown="1">
Au-dessus de 20 qubits, on a trop d'erreurs
</div>

AlissonBob, Amazon et UCI pretendent pouvoir reduire le nombre de qubits physiques necessaires pour faire des calculs.

## More on quantum computing speed

Quand on fait une operation de portes sur des qubits intriques, c'est comme si on faisait cette operation sur plusieurs etats.

On va prendre une porte de Hadamard: on a une vingtaine d'operations.

Or, d'apres IBM, comme le calcul quantique est probabiliste il faut l'executer plusieurs fois, cad $4000$ fois.

<div class="alert alert-success" role="alert" markdown="1">
$4000\times20=80 000$ portes executees pour juste une porte de Hadamard !

<div class="alert alert-warning" role="alert" markdown="1">
Et c'est un cas **simple**
</div>

</div>

De meme, pour les autres portes:

![](https://i.imgur.com/hzUADdg.png)

<div class="alert alert-danger" role="alert" markdown="1">
On veut corriger le taux d'erreur pour utiliser le moins de qubits physiques possible
</div>

## Qubits connectivity

### IBM

![](https://i.imgur.com/6uyOW99.png)

Rocheser 53 qubits, october 2019
65 qubits, october 2020

### Google

![](https://i.imgur.com/MCQDvgY.png)

Sycamore 53 qubits, october 2019

*Pourquoi un qubit blanc ?*
> Parce qu'il marche pas ptdr

### IonQ

<div class="alert alert-info" role="alert" markdown="1">
Cas particulier des **ions pieges**
</div>

Ils sont tous connectes les uns aux autres

![](https://i.imgur.com/TheHEeD.png)

- 11 qubits, 2018

![](https://i.imgur.com/mQ0VOg9.png)

# "Rackability" examples

## Pasqual

Double depth racks
- Model of cold atoms computer with $100-100$ qubits, planned for $2021-2023$

![](https://i.imgur.com/mnolCDF.png)

## Quandela

Single depth rack
- Prometheus

![](https://i.imgur.com/TgvYd8C.png)


## Data center constraints

![](https://i.imgur.com/o0u3pVS.png)

*Combien est-ce que ca consomme dans un data center ?*
> Je sais pas / ca depend
> [name=Olivier Ezratty] [time=Tue, Oct 12, 2021 4:50 PM] [color=#907bf7]
> Ca depend du nombre de rack

# Cooling

<div class="alert alert-info" role="alert" markdown="1">
**Goal**: reduce thermal noise affecting qubits
</div>

![](https://i.imgur.com/RmGUwi8.png)

## Micro-waves sources

![](https://i.imgur.com/nB4woVh.png)

<div class="alert alert-warning" role="alert" markdown="1">
Chaque fils supra-conducteur coute $3000$\$
</div>

## Details from a 15 mK cryostat

![](https://i.imgur.com/4hmy5BA.png)

![](https://i.imgur.com/oU4uTub.png)

## Some companies

Dilutions and systems
- Finland 
    - Bluefors
    - IBM
    - Rigetti 
    - CEA
- US: 
    - JanisULT
    - Google
- UK: 
    - Oxford instruments
    - Microsoft
    - DWave
- France: 
    - CryoConcept
    - Neel
    - LPENS
- Netherlands: 
    - Leiden Cryogenics
    - IBM

Cabling
- Japan
    - Coax Co. LTD
- Netherlands
    - Delft Circuits
- France
    - Radiall

Pulse tubes and compressors
- US
    - Cryomech
- Japan
    - Sumitomo

## Available cooling power

| Cryostat | pulse tubes                    | minimum temperature | 20mK stage               | 100 mK stage                            | MC cold plate                               |
| -------- | ------------------------------ | ------------------- | ------------------------ | --------------------------------------- |:------------------------------------------- |
| Bluefors | lD250 <br> XLF400 <br> XLD1000 | 1 <br> 2 <br> 2     | 10mk <br> 8 mK <br> 8 mK | $12\mu$ W <br> $12\mu$ W <br> $34\mu$ W | $250\mu$ W <br> $450\mu$ W <br> $1000\mu$ W |

## IBM

Goldeneye fridge designed for 1121 qubits Condor completion planned for 2023.

5 and 14 days to cool down.

*design shown is not fake*

![](https://i.imgur.com/golLfWa.png)

- Cabling paths shows they will use some sort of cryoCMOS
- using separate pulse tubes to and bottom

