---
title:          "ALGOREP: Concensus for Asynchronous Systems"
date:           2021-09-13 16:00
categories:     [Image S9, ALGOREP]
tags:           [Image, SCIA, S9, AlGOREP]
math: true
description: Concensus for Asynchronous Systems.
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/BJtNyyTMt)

[Les slides du cours](https://www.lrde.epita.fr/~renault/teaching/algorep/)

*Est-ce qu'on est capable de creer un consensus asynchrone ?*
> Oui on l'utilise tous les jours
> Un papier theorique dit non mais si c'etait le cas Facebook et machin ne fonctionneraient pas
> En tout cas c'est impossible dans un mode completement asynchrone

# FLP
<div class="alert alert-info" role="alert" markdown="1">
**Abstract of the paper**
The consensus problem involves an asynchronous system of
processes,some of which may be unreliable. The problem is for the reliable processes to agree on a binary value. In this paper, it is shown that every protocol for this problem has the possibility of nontermination, even with only one faulty process.
</div>

<div class="alert alert-danger" role="alert" markdown="1">
**Impossibility result**
No completely asynchronous consensus protocol can tolerate even a single unannounced process death.

</div>

## Problem description

![](https://i.imgur.com/ZbPm6kW.png)

## Configurations

![](https://i.imgur.com/vWfR8Xx.png)

