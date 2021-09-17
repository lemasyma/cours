---
title:          "ALGOREP: Consensus is possible ! Paxos"
date:           2021-09-17 15:00
categories:     [Image S9, ALGOREP]
tags:           [Image, SCIA, S9, AlGOREP]
description: Consensus is possible ! Paxos.
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/SkMEqZM7Y)

[Les slides du cours](https://www.lrde.epita.fr/~renault/teaching/algorep/)

# A Word on Paxos

> "On va abandonner les systemes distribues c'est trop chiant"
> Lamport: a prouve accidentellement que ca marche

*Est-ce que Paxos c'est dur ?*
> Ca depend des gens

<div class="alert alert-info" role="alert" markdown="1">
On veut arriver au consensus mais pas gagner
</div>
> Comme si tous les candidats a la presidentielle veulent que quelqu'un soit elu

# Intuition

*On veut aller manger, tout le monde a faim et on a pas de chef. On peut discuter que un a un.*
> Des gens ont une idee initiale et des gens vont suivre

*Qu'est-ce qu'il peut arriver ?*
> Soit aucune idee n'est acceptee
> Soit on arrive pas a avoir une majorite ("Tu veux manger quoi ?" "M'en fou")

## Problem: Split votes

Consider 5 processes:
- P1, P2 accepts $\color{red}{red}$
- P3, P4 accepts $\color{blue}{blue}$
- P5 accepts $\color{green}{green}$

*Comment on fait ?*
> P5 rejoint un des groupes et tout le monde rejoint la majorite ?
> Comment P5 connait l'etat des autres ?

<div class="alert alert-success" role="alert" markdown="1">
On va les faire fight en 1v1 gare du nord
</div>
> On a rouge et noir
> On va envoyer un message a tous
> Avec le delai de propagation des messages, on va dire oui a noir ou oui a rouge
> Si noir arrive en premier, noir sera choisi, sinon rouge le sera
> Si on a propose noir et qu'on dit oui a rouge, alors on transmet le message comme quoi on propose rouge maintenant

## Example

![](https://i.imgur.com/9PSVmby.png)

# Paxos
## Basic Paxos

2 phases
1. On va envoyer des messages `Prepare`
    - "Je vais bloquer toutes les anciennes propositions"
2. `Broadcast accept`
    - "J'accepte ta valeur"

## Conceptual Roles in Paxos

- Proposer
- Acceptors
- Learners: learn the outcome

## Overview

### Phase 1

1. $[Proposer]$ Choose a proposal number $n$
2. $[Proposer]$ Broadcast `prepare(n)` to all servers
3. $[Acceptor]$ Response to `prepare(n)`
    - if $n\gt minProposal$ then $minProposal=n$
    - Return (accepted_proposal, accepted_value)
4. $[Proposer]$ When responses received from majority
    - if any accepted_value returned, replace value by accepted value for highest accepted_proposal

### Phase 2

1. $[Proposer]$ Broadcast `accept(n, value)` to all servers
2. $[Acceptor]$ Response to accept(n, value)
    - if $n \ge minProposal$ then accepted proposal = min proposal = n, accepted value = value
    - Return (min proposal)
4. $[Proposer]$ When responses received from majority
    - Any objection $(result \gt n)$ ? restart
    - Otherwise, value is chosen

## Example 2

![](https://i.imgur.com/SXVd9js.png)

## Example 3

![](https://i.imgur.com/Jp77Dyc.png)

## Liveness

<div class="alert alert-danger" role="alert" markdown="1">
Competing processes can livelock !
</div>

![](https://i.imgur.com/h2c628e.png)
> Les processus se battent pour avoir le dernier de la majorite

## Solutions

<div class="alert alert-success" role="alert" markdown="1">
Randomized delays before restarting
</div>

# Multi-Paxos

<div class="alert alert-info" role="alert" markdown="1">
Create a replicated log
</div>

