---
title:          "ALGOREP: Global Snapshot"
date:           2021-09-13 14:00
categories:     [Image S9, ALGOREP]
tags:           [Image, SCIA, S9, AlGOREP]
description: Global Snapshot.
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/rJ5JePQMY)

[Les slides du cours](https://www.lrde.epita.fr/~renault/teaching/algorep/)

# Problem statement

<div class="alert alert-danger" role="alert" markdown="1">
- No global clock
- No shared memory
- Unpredictable message delay
</div>

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
> Elle est mauvaise parce que la coupe se fait avant l'envoie $e_2$ mais aussi après la réception de $g_4$

## Consistent Global state

On a des regles:
1. Tout envoi a une reception
2. Une reception implique que l'envoi est dans l'etat global

Voila une coupure coherente:
![](https://i.imgur.com/KNE7Mzk.png)

# Snapshot for FIFO channels

*On veut envoyer un message puis un deuxieme, comment on fait pour que le premier message arrive avant le premier ?*
> Envoyer un message a tout le monde $\to$ **broadcast**
> Arreter ce que font les machines n'est pas une bonne idee
> On flush les canaux grace a la propriete FIFO avec le broadcast $\to$ plus aucun message en transit

*Probleme: le leader envoie un message a tout le monde "fait la snapshot". Une machine rapide relaie le message a une machine lente qui n'a pas recu le message original, elle va recevoir 2 fois le meme message. Comment on fait ?*
> On essaie de numeroter de maniere unique les snapshots

Dans un snapshot, on s'en fiche des messages applicatifs.

![](https://i.imgur.com7qmhrN.png)

![](https://i.imgur.com/kOjJyhC.png)


![](https://i.imgur.com/lP5Vkyu.png)

![](https://i.imgur.com/xBlYBe3.png)

![](https://i.imgur.com/gj3hc9I.png)

![](https://i.imgur.com/IY3I2R6.png)

![](https://i.imgur.com/ccPyCVn.png)

![](https://i.imgur.com/mMgsRhw.png)

![](https://i.imgur.com/1zqoE8M.png)

![](https://i.imgur.com/1eGz0iO.png)

![](https://i.imgur.com/RtQblV6.png)

*Prenons l'exemple de $f_3$-$e_4$, a ce moment un message est en transit. Comment on enregistre le message ?*
> Dans ce cas, seul $F$ peut enregistrer
> On va stocker dans les messages envoyes depuis notre derniere snapshot

## Chandy-Lamport Algorithm : Informal

![](https://i.imgur.com/szSTo7P.png)

## Correctness

- When a process $j$ receives a message $m_{i,j}$ 

## Complexity

<div class="alert alert-info" role="alert" markdown="1">
**Message complexity**
$O(e)$ for the record of a single instance of the algorithm, with $e$ the number of edges in the graph
</div>

<div class="alert alert-info" role="alert" markdown="1">
**Time Complexity**
$O(d)$ time with $d$ the diameter of the graph
</div>

## Remarks

- The recorded global state may not correspond to any of the gloal states that occured during the computation

$$
\color{red}{\text{BUT...}}
$$

- The recorded global state may not corresponds to any of the global states that occurred during the computation
- The recorded global state is a valid state in a equivalent execution

# Snapshot for non-FIFO channels

On envoie $A$ puis $B$, on suppose qu'on peut recevoir $B$ avant $A$

## Lai Yang Algorithm

On est tous initialement d'une couleur (ex: blanc). On se met en rouge si on fait une snapshot et on envoie des messages.

*Qu'est-ce qui se passe si on recoit un message rouge ?*
> Quelqu'un a fait un snapshot et c'est en cours
> A partir de maintenant j'envoie que des messages rouges

*Comment on sait quels etaient les messages en transit ?*
> Tous les messages blancs
> Le recepteur va sauvegarder les messages comme etant en transit

On n'est pas capable de:
- Borner les delais d'un message
- Avoir une file de message

Au moment de redemarrer le systeme, on ne renvoit pas de message blanc et on peut les integrer au snapshot directement au lieu de simuler leur reception.

Pour ne pas faire $\color{white}{\text{blanc}}$ $\color{red}{\text{rouge}}$ $\color{white}{\text{blanc}}$, on fait plutot $\color{white}{\text{blanc}}$ $\color{red}{\text{rouge}}$ $\color{purple}{\text{violet}}$ $\color{green}{\text{vert}}$ etc.

Si on recoit des messages blanch en snapshot violet, il y a un probleme dans le systeme. Ce n'est pas grave du moment que la couleur de la derniere snapshot est de la meme couleur pour toutes les machines.

## Mattern's Algorithm

<div class="alert alert-success" role="alert" markdown="1">
**Horloge de Mattern**
</div>

*Comment on fait si on veut manger chez Glados jeudi soir ?*
![](https://i.imgur.com/ihR2Gik.png)

> On envoit un message "A 19h je mange chez Glados"
> On va faire pareil pour cete algo

On se dit "RDV a un million" pour un snapshot (au plus tard). Avant la reception du message a 1 million, les machines doivent faire leurs snapshots