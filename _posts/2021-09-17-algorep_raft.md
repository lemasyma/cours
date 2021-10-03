---
title:          "ALGOREP: Raft"
date:           2021-09-17 16:00
categories:     [Image S9, ALGOREP]
tags:           [Image, SCIA, S9, AlGOREP]
math: true
description: Raft.
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/HkugKGz7t)

[Les slides du cours](https://www.lrde.epita.fr/~renault/teaching/algorep/)

# Overview
<div class="alert alert-info" role="alert" markdown="1">
**Goal**
Replicate logs (commands) in a set of servers
</div>
- On va avoir des indexs
- Des informations qu'on va mettre sur chaque index/ligne

<div class="alert alert-success" role="alert" markdown="1">
On veut que tout le monde ait le meme log
</div>

<div class="alert alert-info" role="alert" markdown="1">
**Overview**
Once all servers agree for a log entry, all server can run it $\Rightarrow$ All server will then compute the same value (replication)
</div>

<div class="alert alert-danger" role="alert" markdown="1">
C'est exactement le projet
</div>

## Limitations and restrictions

<div class="alert alert-danger" role="alert" markdown="1">
On veut elire un chef a la majorite
</div>

## Comparaison avec Paxos

- Paxos est de l'approche distribuee
- Raft non, il y a un leader et tout le monde communique avec le chef
    - Avantage: une machine est chef que pendant un laps de temps

## Summary

1. Election
2. Operation normal
3. Coherence de l'algo
4. Problemes qu'on peut avoir

# Server state

3 roles:
- Leader
- Follower
- Candidate

Chaque server commence follower:
![](https://i.imgur.com/5xrXUel.png)

![](https://i.imgur.com/BdDbjfG.png)

![](https://i.imgur.com/UNq0Img.png)

![](https://i.imgur.com/TPKx5fz.png)

![](https://i.imgur.com/efPuOpM.png)

## Time divided into Terms

- On va faire par epoch
- On veut un chef par epoch

<div class="alert alert-warning" role="alert" markdown="1">
En fonction des processus qui meurent et naissent, on peut avoir de l'info obsolete
</div>

Raft est un algo pessimiste qui va passer son temps a nettoyer.

## Heartbeats

<div class="alert alert-info" role="alert" markdown="1">
Leader can send heartbeat to keep authority
</div>

## Leader changes

![](https://i.imgur.com/VTCis8I.png)

- Chacune des cases est remplie avec des actions
- L'info stockee sur $S_1$ a la premiere ligne du log a ete calculee pendant la $1^{ere}$ epoch

<div class="alert alert-warning" role="alert" markdown="1">
Ensuite viennent les complications
</div>

Le log est stable sur les 2 premieres colonnes

*Mais apres ?*
> L'information de $S_4$ n'a pas ete propagee

<div class="alert alert-danger" role="alert" markdown="1">
Il faut faire attention a l'information locale et celle connue par tout le monde
</div>

<div class="alert alert-success" role="alert" markdown="1">
On ecrit l'information locale quand elle est acceptee par tout le monde
</div>

## Election basics

- Increment current term
- Change to Candidate state
- Vote for self
- Send RequestVote RPCs to all other servers, retry until either
    1. Receive votes from majority of servers
        - Become leader
        - Send AppendEntries heartbeats to all other servers
    3. Receive RPC from valid leader
        - Return to follower state
    5. No-one wins election (election timeout elapses)
        - Increment term, start new election

## Properties of the election

Safety: allow one winner per term
- Each server gives out only one vote per term
- 2 different candidates can't accumulate majorities in same term

Liveness: some candidate must eventually win

## How to replicate log entries ?

<div class="alert alert-info" role="alert" markdown="1">
On veut un log coherent par rapport aux differents serveurs
</div>

On a:
- Des entrees
    - Avec des commandes
    - Le terms
- Des indexs

# Normal operations

L'algorithme commence a tourner.

- Le client envoie une commande au leader
- Le leader prend la commande et le met dans son log
- Le leader envoie `AppendEntries` RPCs aux followers
- Une fois que l'entree est prise
    - Leader passes command to its state machine, returns result to client
    - I Leader notifies followers of committed entries in subsequent AppendEntries RPCs
    - Followers pass committed commands to their state machines
- Crashed/slow followers ? ⇒ Leader retries RPCs until they succeed

## Example 1

![](https://i.imgur.com/cwXb5HK.png)
- $S_4$ et $S_5$ sont en retard
- Vu qu'il sont en retard, si on declenche une nouvelle epoch ils ne peuvent pas etre chef

*Quel probleme peut-on avoir ?*
> Ca peut accentuer les gens en avance et en retard en fonction des epochs
> On va avoir des sous-systemes qui vont se creer avec des logs pas coherents

## Example 2

![](https://i.imgur.com/XiSkn7w.png)

On a un truc bizarre, $S_5$ n'a pas d'epoch 2. On a une divergence.

Pour l'epoch 5, $S_5$ peut etre elu car il a un log long, mais pas coherent avec celui des autres. Il va donc demander des rollabacks jusqu'au dernier point d'intersection.

# New commitment rules

For a leader to decide an entry is committed :
- Must be stored on a majority of servers
- At least one new entry from leader’s term must also be stored on majority of servers

![](https://i.imgur.comEFB4YT.png)

## Client protocol

![](https://i.imgur.com/bu62zdo.png)
