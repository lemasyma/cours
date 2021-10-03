---
title:          "ALGOREP: How to build a Failure Detectors"
date:           2021-09-13 14:00
categories:     [Image S9, ALGOREP]
tags:           [Image, SCIA, S9, AlGOREP]
math: true
description: How to build a Failure Detectorst.
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/Sy0dEWzmK)

[Les slides du cours](https://www.lrde.epita.fr/~renault/teaching/algorep/)

*On a un ensemble de machine. Comment monitorer pour savoir qu'une est morte ?*
> Si quelqu'un dans la salle a une machine qui meurt, on va le savoir
 
*Supposons qu'on a un admin 6, pourquoi c'est pas une bonne solution ?*
> Ca se scale pas bien
> On centralise dans un seul data center pour un systeme distribue

*Comment on pourrait faire pour detecter les machines qui meurent de maniere auto ?*
*Si on a une mamie agee, coment on sait ?*
> On la rappelle le matin, le midi, a 14h

*Et si la mamie est tres lente a repondre au telephone ?*
> On appelle une premiere fois, une seconde fois, etc.
> Au bout de certaines sonneries on la suppose morte

<div class="alert alert-success" role="alert" markdown="1">
On se forge une conviction de si la machine est vivante ou morte

<div class="alert alert-warning" role="alert" markdown="1">
On est pas sur a $100\%$
</div>

</div>

# Desirable properties

- Completness
- Accuracy
- Speed
- Scale
    - Equal load on each member
    - Network Message Load

## What real failure detectors prefer ?

- Success and accuracy
- Scale & Speed

# Strategies
## Centralized heartbeating

On a une machine centrale qui envoie des messages a tout le monde, sauf que la machine ne fait que ca et doit faire d'autre decisions
- On peut avoir une machine avec superposition de couches
    - Un chef pour les fautes, un chef pour les decisions, etc.

<div class="alert alert-success" role="alert" markdown="1">
On empile les couches jusqu'a contrer le theoreme d'impossibilite
</div>

## Ring Heartbeating

On va regarder nos voisins a gauche et a droite, pour propager le message qu'une machine est morte on doit faire le tour de l'anneau.

*Si notre voisin de droite est mort, comment on fait ?*
> On veut se connecter a son voisin de droite
> Et si son voisin de droite est mort aussi ?
> Soit on est coupe du reseau, soit systeme de cascade de mort de machines

## All-to-all heartbeating

- A processus heartbeats periodically all its neighbours
- If heartbeat not received from a process within timeout, mark this process as failed

## Gossiping heartbeating

On envoie un heartbeat a quelqu'un, cette personne dit telle ou telle personne est vivante
- On prend un pool de personnes random a qui envoyer notre heartbeat

## Conclusion

<div class="alert alert-danger" role="alert" markdown="1">
Heartbeat is a fundamental of Failure detection
</div>