---
title:          "ALGOREP: Global Snapshot"
date:           2021-09-06 11:30
categories:     [Image S9, ALGOREP]
tags:           [Image, SCIA, S9, AlGOREP]
description: Global Snapshot.
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/rJ5JePQMY)

[Les slides du cours](https://www.lrde.epita.fr/~renault/teaching/algorep/)

# Problem statement

On est dans un data center, EDF coupe l'electricite $\Rightarrow$ **on est mort**.

*Comment est-ce qu'on backup ?*
> Etienne nous dit de backup, il y en a un qui est un peu lent. Il y a un crash et on a loupe le backup

<div class="alert alert-success" role="alert" markdown="1">
On definit un etat stable
</div>

*Qu'est-ce qu'on fait de l'info entre nous (les messages) ?*
> Si on definit un etat stable ou rien ne transite, sinon c'est pas un systeme distrib

<div class="alert alert-warning" role="alert" markdown="1">
On doit definir un backup pendant que des messages passent, des apps tournent, etc.
</div>

# Global state and cuts
## Cuts

<div class="alert alert-info" role="alert" markdown="1">
**Definition**
A **cut** in a time diagram is a line joining an arbitrary point on each process line that slices the space-time diagram into a PAST and a FUTURE.
</div>

![](https://i.imgur.com/Fkgr5p6.png)

## Global state

<div class="alert alert-info" role="alert" markdown="1">
**Definition**
The global state of a distributed system is a collection of the local states of the processes and the channels.
</div>

![](https://i.imgur.com/pQIAruj.png)

## Consistent cut

![](https://i.imgur.com/1wSGiwQ.png)

*Qu'est-ce qu'on pense de cette cut ?*
> Le probleme est qu'il ne faut pas qu'on soit dans des moment ou il y a un envoie et un evenement qui risque de ne pas etre retrouve

## Consistent Global state

On a des regles:
1. Tout envoi a une reception
2. Une reception implique que l'envoi est dans l'etat global

Voila une coupure coherente:
![](https://i.imgur.com/KNE7Mzk.png)
