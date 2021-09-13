---
title:          "ALGOREP: Consensus (with failures) in synchronous systems"
date:           2021-09-13 14:00
categories:     [Image S9, ALGOREP]
tags:           [Image, SCIA, S9, AlGOREP]
description: Consensus (with failures) in synchronous systems.
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/HyWKjT2fY)

[Les slides du cours](https://www.lrde.epita.fr/~renault/teaching/algorep/)

On vote a la majorite pour pizza vs kebab. Ca suppose:
- Qu'on est impair
- Chaque voix a le meme poids
- Que la majorite est d'accord

Supposons qu'on soit $11$, on ne peut pas arriver a un consensus si quelqu'un ne repond pas. Ca suppose:
- La machine est morte
- Le lien avec la machine est mort

# What is a consensus ?

<div class="alert alert-info" role="alert" markdown="1">
**Defintion: consensus**
All process must agree on a value even if inputs can be arbitrary.

There is generally a *validity condition* describing the outputs values that are permitted for each patterns' input
</div>

- Agreement on wether to commit or abort transaction in a database
- Agreement on a specific value reading multiple captors (altitude for instance)
- Classification of a component as faulty

<div class="alert alert-success" role="alert" markdown="1">
On va construire des algos **tolerants aux fautes**.
</div>

# Link Failures

## The coordinated attack problem

On a un ensemble de generaux qui attaquent une ville. La seule facon qu'ils aient de prendre la ville seraient de se coordonner.
- Ils peuvent communiquer avec des messagers
    - Les messagers peuvent se faire tuer

*Est-ce que j'attaque ou pas ?*

<div class="alert alert-danger" role="alert" markdown="1">
**Comment faire quand les communications ne sont pas fiables ?**
</div>

> On sait qu'il faut 10 min pour faire le trajet entre 2 generaux
> On demande aux messagers de revenir

*Mais si le messaer a transmis le message mais ne revient pas ?*
> On en renvoit un autre

*Mais s'il se fait tuer aussi ?*
> L'assassin a un tas de cadavre

On peut decouper les interactions de nos generaux en rounds.

![](https://i.imgur.com/wxpsTte.png)
Fleche verte: message envoye

![](https://i.imgur.com/WdBoRcB.png)
0/1: ne pas attaquer/attaquer

Il y a un moment ou on peut perdre un message ($\color{green}{\to}$)

*Comment faire ?*
> 1. On prend une valeur par defaut si on n'attend pas de consensus (spoiler: non)

Supposons qu'on supprime un message.

![](https://i.imgur.com/XFRxJ2G.png)

*Est-ce qu'on a un changement pour le processus $P_2$ ?*
> Non, pour lui ca ne change rien

![](https://i.imgur.com/PpAXGA1.png)

<div class="alert alert-warning" role="alert" markdown="1">
Or, pour un algorithme qui marche avec consensus, il faut que tous les processus soient en accord en meme temps.
</div>

On peut toutefois tres bien dire qu'on s'arrete en $D-1$ round et que l'autre message peut etre perdu.

![](https://i.imgur.compTVWaj.png)

<div class="alert alert-success" role="alert" markdown="1">
On peut se limiter au round precedent, on baisse la complexite de l'algo.
</div>

On peut donc supprimer le message $P_2\color{green}{\to} P_1$ precedent, et de la meme maniere surprimer le message $P_1\color{green}{\to} P_2$

![](https://i.imgur.com/iQ4FwQh.png)

*Comment $P_1$ prend la meme decision que $P_2$ ?*
> On sait qu'on a toujours une decision qui doit etre prise au plus tard qu round $D$
> Or, si on n'a pas envoye de message, la decision etait connue de tout le monde au round $D-1$
> On repete l'etape pour le round $D-1$ jusqu'a arriver aux premiers message

<div class="alert alert-success" role="alert" markdown="1">
On construit un algo sans envoi de messages
</div>
> Un algo commence avec $0$, $0$ est decide
> Un algo commence avec $1$, $1$ est decide

*Quelle est l'unique facon de changer de configuration ?*
> De recevoir un message

<div class="alert alert-danger" role="alert" markdown="1">
C'est une **execution bivalente**
</div>

## Recap

On veut faire un consensus dans tous les systemes distribues. Dans un systeme synchrone, on suppose qu'on a des problemes avec des liens, on montre le **theoreme de l'impossibilite** et qu'un message peut etre perdu indefiniment.

On se base donc sur un etat pour tout le monde et le seul moyen de changer de configuration est de recevoir un message.

## Impossibility Result

<div class="alert alert-info" role="alert" markdown="1">
Let $G$ be a graph with 2 nodes connected by a single edge.

<div class="alert alert-danger" role="alert" markdown="1">
Then, no algorithm solves the coordinated attack problem on $G$
</div>
</div>

### Proof (by contraction)
- Suppose a solution exists, given by an algorithm $A$
- Let $\alpha$ be the execution when both processes starts with $1$ and eventually outputs $1$ with all messages delivered.
- Let $\alpha_1$ be the same than $\alpha$ except that all messages are lost after $r$ rounds. In $\alpha_1$ both processes output $1$.
- Let $\alpha_2$ be the same than $\alpha_1$ except that the last (round $r$) message from process $1$ to process $2$ is not delivered.
- $\alpha_1\sim^1 \alpha_2$ : $\alpha_1$ is indistinguishable from α2 from process $1$ point of view
- Since process $1$ outputs $1$ in $\alpha_1$, then it outputs $1$ in $\alpha_2$.
- By termination and agreement, process $2$ outputs $1$
- Let $\alpha_3$ be the same than $\alpha_2$ except that the last message from process $2$ to process $1$ is not delivered.
- $\alpha_2\sim^1 \alpha_3$ : $\alpha_2$ is indistinguishable from $\alpha_3$ from process $2$ point of view.
- Since process $2$ outputs $1$ in $\alpha_2$, then it outputs $1$ in $\alpha_3$. The same for process $1$ by termination and agreement.

<div class="alert alert-danger" role="alert" markdown="1">
**IMPOSSIBLE!**
</div>

# Process failures
## Problem Statement

<div class="alert alert-info" role="alert" markdown="1">
What if communications are reliable, but processes may fail ?
</div>

2 kinds of failure models:
- Stopping failures: Processes may stop without warning
- Byzantine failures $1$ : fautly processes may exhibit completely unconstrained behaviors.


![](https://i.imgur.com/F6Fg0kh.png)

## Floodset
*Comment regler ca ?*
> FloodSet: Flooding

On calcule le diametre de notre systeme

![](https://i.imgur.com/qWVcIjp.png)


### Example

![](https://i.imgur.com/SCtlEX4.png)

![](https://i.imgur.com/y3k1j3O.png)

![](https://i.imgur.com/FW7JjwD.png)

![](https://i.imgur.com/8WfbarK.png)

![](https://i.imgur.com/1PA97X3.png)

## Stopping Algorithm: EIG

> Etienne : "J'explique mal et vous comprenenez mal"

On va se baser sur un EIG tree

![](https://i.imgur.com/qh9Th6s.png)

Cet algo va marcher direct pour les fautes byzantines

> Etienne est vivant, envoie un message et creve.
> Comme ca on peut deduire a quel round Etienne est mort

### Example

![](https://i.imgur.com/mSgM1fJ.png)

Le processus $3$ echoue au round $1$ mais a envoye un message au processus $1$ mais pas au processus $2$.

*Comment $2$ peut etre au courant que $3$ a envoye un message a $1$* ?
> $1$ doit lui relayer le message

A la dernier ligne, on doit savoir quelle info a ete propagee par le processus $3$, le dernier etage de l'arbre doit etre le meme pour tous les processus corrects.

<div class="alert alert-warning" role="alert" markdown="1">
Si on veut supporte $20$ fautes, il faut avoir $20$ lignes
</div>

<div class="alert alert-info" role="alert" markdown="1">
**Construction**
1. On initie le $1^{er}$ etage de l'arbre avec sa propre valeur et on la propage aux autres
2. Au $2^e$ etage on recoit la valeur initiale des autres processus
3. Pour tous les autres rounds, le process $i$ diffuse une pair $(x,v)$ qui va etre un des labels de l'etage precedent
    - Il se construit en se basant sur l'etage precedent et en recevant la valeur des autres elements
</div>

## Why byzantine is more complicated than stopping ?

<div class="alert alert-info" role="alert" markdown="1">
Three processes cannot solve the agreement problem if one of them is faulty !
</div>