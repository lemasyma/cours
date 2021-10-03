---
title:          "ALGOREP: Leader Election"
date:           2021-09-06 9:00
categories:     [Image S9, ALGOREP]
tags:           [Image, SCIA, S9, AlGOREP]
math: true
description: Leader Election.
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/ByqOGjJfY)

[Les slides du cours](https://www.lrde.epita.fr/~renault/teaching/algorep/)

# Leader Election in a Synchronous Ring

## Problem statement

- The netwok digraph is a ring with $n$ nodes
- All processes are identical
- Each process can only communicate with clockwise neighbors and counterclockwise neighbors

<div class="alert alert-info" role="alert" markdown="1">
One process outputs *"I'm the leader"* while the other process output *"I'm note the leader"*
</div>

![](https://i.imgur.com/q9FpDjt.png)

Si tu prend 2 robots identiques, ils divergent lors de la connexion au reseau

## Impossibility Result for Identical Processes

<div class="alert alert-info" role="alert" markdown="1">
**Theorem**
Let $S$ be a system of $n$ processes, $n \gt 1$, arranged in a bidirectionnal ring. If all the processes are identical then $S$ does not solve the leader-election problem.
</div>

## Sketch of proof

1. Suppose there is a system $S$ that solves this problem
2. Without loss of generality, we can assume that each process of $S$ have a unique initial state.
3. By induction on the number $r$ of rounds, all the processes are in identical states immediately after $r$ rounds.
4. Then if a process reaches a state where it considers to be the leader, all the other processes do so.
5. But this violates the uniqueness requirement

## Problem Statement $\color{red}{Revisited}$

- The network digraph is a ring with $n$ nodes
- All processes are identical $\color{red}{\text{except for a UID}}$
- Each process can only communicate with clockwise neighbour and counterclockwise neighbour

*Propositions:*
- Envoyer un message disant "Je suis peut-etre leader"
    - Mais beaucoup de messages
- Anneau unidirectionnel

# LCR Algorithm

1. Chaque processus envoie son UID
2. Quand il recoit un UID, il le compare avec le sien
    - Si l'UID est plus grand, il l'envoie a son voisin
    - Sinon discard

![](https://i.imgur.com/Bn5Q87g.png)

![](https://i.imgur.com/ybOTA02.png)

![](https://i.imgur.com/jp66WDV.png)

<div class="alert alert-info" role="alert" markdown="1">
$n$ machines = $n$ rounds
</div>

## Complexity

- Meilleur cas: $O(n)$ messages
- Pire cas: $O(n^2)$ messages

<div class="alert alert-info" role="alert" markdown="1">
Quand un noeud est elu, $n$ rounds et $n$ messages sont necessaires
</div>

# HS Algorithm (comparison-based)

- Bidirectionnal Ring
- The size of the ring is unknown
- Comparison-based algo
- $\color{red}{\text{It elects the process with the maximum UID}}$

![](https://i.imgur.com/aeXwRbZ.png)

![](https://i.imgur.com/AqgvCho.png)

## Algorithm

1. On a des phases de process $i$
2. Dans chaque phase $l$
    - Process $i$ send out tokens containings its $UID_i$ in both directions
    - Tokens travel distance $2^l$ and return to their origin $i$
    - When a process $i$ receive a token $t$ containing $UID$ $t_{uid}$
        - if $t_{uid}$ $\lt$ $UID_i$ then the token is discarded
        - if $t_{uid}$ $\gt$ $UID_i$ then the process $i$ relays the token
        - if $t_{uid}$ $=$ $UID_i$ then the process is the leader
    - If both tokens come back safely, process $i$ starts a new phase
    - Otherwise the process considers itself as a non-leader

## Communication Complexity

1. **Phase 0**: tout le monde envoie un message a gauche et a droite et recoit un message des 2 cotes
    - On envoit 4 messages par noeud: $4\times n$ messages
3. **Phase $l$**: On a survecu a la phase $l-1$, il y a $2^{l-1}+1$ qui sont morts autour de moi, il y a $\lfloor\frac{n}{2^{l-1}+1}\rfloor$ process qui envoient un messgae a cette phase. Le nombre de message est $4\times 2^l \lfloor\frac{n}{2^{n-1}+1}\rfloor\le8n$

<div class="alert alert-success" role="alert" markdown="1">
How many phases are executed before a leader is elected ?

$$
1+\lceil\log n\rceil
$$

</div>

<div class="alert alert-danger" role="alert" markdown="1">

The number of messages is at most $8n(1 + \lceil\log n\rceil)$

</div>

## Time Complexity

- The time complexity for phase $l$ is $2^{l+1}$
    - $\color{red}{\text{The complexity of all but the final phase is }2\times2^{\log n}}$
- In the final phase takes $n$ since tokens only travels outbound
- The final complexity is at most $3n$ (if $n$ is power of $2$) $5n$ otherwise.

## Summary

<div class="alert alert-danger" role="alert" markdown="1">
$O(n)$
</div>

<div class="alert alert-danger" role="alert" markdown="1">
$O(n\log n)$
</div>

# TimeSlice Algorithm

![](https://i.imgur.com/YO3sOQl.png)


# Lower Bounds

<div class="alert alert-success" role="alert" markdown="1">
**Comparison-based**
The best case is $\Omega(n \log n)$ messages.
</div>

<div class="alert alert-success" role="alert" markdown="1">
**Non-Comparison-based**
$O(n)$ messages can be reached but only at the cost of large time complexity (Ramsey Theorem).
</div>

# Leader Election in other

## Flooding Algorithm

![](https://i.imgur.com/y3ZvKqF.png)

![](https://i.imgur.com/r4Jxo6K.png)

# Breadth-First Search

<div class="alert alert-info" role="alert" markdown="1">
We want to build the directed spanning tree for the network
</div>

## Example

1. ![](https://i.imgur.com/0cXITeO.png)
2. ![](https://i.imgur.com/tN4LoZW.png)
3. ![](https://i.imgur.com/ere2Uvv.png)
4. ![](https://i.imgur.com/0ygen12.png)
5. ![](https://i.imgur.com/hunuFto.png)

## Children pointers

![](https://i.imgur.com/i8CgDzE.png)

## Leader Election

![](https://i.imgur.com/6j0I6sk.png)

# Minimum Spanning Trees

*Comment est-ce qu'on construit un arbre courant en sequentiel ?*
> "On enfile des noeuds" (mais c'est un BFS ca)

## Problem Statement

*How to find the minimum/maximum spanning tree ?*

<div class="alert alert-danger" role="alert" markdown="1">
A minimum-weight spanning tree minimizes the total cost for any source process to communicate with all the other process in the network
</div>

$\color{red}{\text{Let us assume that } n \text{ is known}}$

*Est-ce qu'on a besoin d'un leader ?*
> Minorite de oui: on aurait besoin de quelqu'un qui synchro tou, mais c'est trop sequentiel
> Majorite de non

<div class="alert alert-success" role="alert" markdown="1">
On peut **synchroniser avec les process avec les rounds**
</div>

> Imaginons que Mael est un process, qu'il a un lien avec Etienne et tout le monde
> Imaginons qu'on peut ponderer les liens (Etienne$\leftrightarrow$Mael $=$ fibre, les autres wifi)
> Imaginons que quelqu'un a une connexion encore plus rapide avec Mael
> *Comment est-ce qu'on se met d'accord ?*
> $1^{ere}$ suggestion: tableau de booleens pour savoir qui se co a qui $\Rightarrow$ **Mais qui stock le tableau ?**
> $2^{eme}$ suggestion: tout le monde a le tableau de boolens $\Rightarrow$ **infernal de synchro tout le monde**

> Reprenons naivement:
> 2 process s'envoient des messages mutuellement, **le composant est cree**
> Maintenant il faut elire un chef
> Si tous les process sont synchro par 2, maintenant on peut synchroniser 2 paires
> On continue jusqu'a synchro tous les composants

<div class="alert alert-warning" role="alert" markdown="1">
Avec cette strategie, on aura un temps de propagation plus long pour un message (2 messages au lieu de 1)
</div>

2 interets:
1. Le BFS est complique a faire, on lancais $n$ BFS
    - Beaucoup de messages sequentiels en parallele
2. Maximiser le fait qu'on soit en distribue

*Qu'est-ce qu'on va faire apparaitre avec cette methode ?*
> Du $\log$ car on divise par 2 a chaque fois

*Comment faire pour savoir les liens d'un composant avec le reste du monde ?*
> Quand on creer une paire, les process peuvent echanger leurs listes de voisins
> On peut faire une phase de flooding dans le composant

*Comment ca genere un arbre courant ?*
> 2 process creent un arbre courant entre eux
> On rajoute une paire, on a un arbre courant a 4
> etc.

*Ou est-ce que l'arbre courant va etre stocke ?*
> Chacun va avoir une *vision locale*

*Si jamais un composant a 2 voisins avec le meme degre minimal, comment faire ?*
> Si ce composant ne repond pas a un des 2 voisins dans le temps imparti, c'est qu'il s'est mis avec l'autre

<div class="alert alert-warning" role="alert" markdown="1">
Avec cette methode, on perd les performance de notre systeme
</div>

> On a un composant qui peut faire des aggregations simultanees pour avoir des performances resonnables

## Complexity

- Time: $O(n\log n)$
- Communication: $O((n+\vert E\vert)\times\log(n))$
    - $O(n)$ messages sent per level

## Remarks

<div class="alert alert-info" role="alert" markdown="1">
**Non-unique edge weight**
We can define a lexicographic order using UID of processes
</div>

<div class="alert alert-info" role="alert" markdown="1">
**Leader election**
When building the MST a leader is elected naturally !
</div>