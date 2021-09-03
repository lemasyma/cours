---
title:          "ALGOREP: Introduction"
date:           2021-09-03 14:00
categories:     [Image S9, ALGOREP]
tags:           [Image, S9, AlGOREP]
description: Introduction.
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/B1F8g5JfF)

# Introduction to Distributed Algorithms

Supposons qu'on soit tous des machines, avec CPU, GPU, etc.

![](https://i.imgur.com/1w7bLpa.jpg)

On interroge quelqu'un qui repond vite, et un autre qui repond lentement. Si on a pas de reponse, on envoie une 2e message.

*Comment tu determines la difference entre un etudiant mort et un etudiant lent ?*
En tant que machine on ne sait pas.

## Forewords

> A distributed system is a collection of independant computers that appears to its users as a single coherent system
> **Andrew S. Tanenbaum**

> A distributed system is one in which the failure of a computer you didn't even know can rend you computer unusable
> **Leslie Lamport**

## Mais pourquoi ?

L'utilite:
- La securite
- La stabilite
    - Un ordi qui crash $\neq$ tout qui casse
- Probleme de matos
    - Google ne peut pas tout stoquer sur un ordi

:::success
- **Si une machine apprend quelque chose, on peut la transmettre**
    - Si le prof meurt mais nous a transmis ses infos, on peut continuer son cours
:::

:::danger
C'est la **replication**
:::

# What is a distributed system ?

:::info
**Definition**
A distributed system is:
- A collection of autonomous computer
- connected through a network
- which enables computers to coordinate their activities
- so that users perceive the system as a single one
:::

## Exemple

- Grid/Cluster computing
- World Wide Web
- Network File Server
- Banking Network
    - Bosser la-dedans pour se faire de la moula
- Peer-to-peer Network
- Process Control System
- Sensors Network

## Parallel versus Distributed ?

Parallel
![](https://i.imgur.com/cXziFbC.png)

Distributed
![](https://i.imgur.com/6DNhE2O.png)

## Pitfalls in Distributed Systems !

1. The network is reliable
2. The network is secure
3. The network is homogeneous
4. The topology does not change
5. Latency is zero
6. Bandwith is infinite
7. Transport cost is zero
8. There is one administrator
    - pas d'administrateur tout-puissant

## Challenges distributed systems ?

- Scalability
    - Avoid Bottlenecks, Good Performances, Physical Ressources
- Heterogeneity
    - Network, hardware, OS, programming language, implem
- Concurrency
    - Managing shared ressources
- Failures
    - Detect, masking, tolerating, recovery, redundancy
- Communications
    - Synchronous, asynchronous

# In this class

1. Systeme distrib point de vue theorique et pratique
2. Concepts generaux
    - Passer de programmes complexes a une abstraction
    - algorithmes
    - analyse de complexite
    - presenter les resultats d'impossibilite
3. Practical through a **project**
    - Un bon gros projet sa mere
    - Groupe de 4
    - Specs faibles pour appliquer le cours

# Model Assumptions

- Modeles IPCs
- Notion de temps
    - On a pas tous la meme frequence/horloge

1. Modele synchrone
2. Modele asychrone
    - c dur
    - resume a un modele partiellement synchrone
3. Model partiellement synchrone

# Abstractions

*Comment avoir une vue d'ensemble ?*
> Il faut monter en abstraction

## Forewords

> Success really depends on the conception of problems, the design of the system, not on the details of how it's coated
> **Leslie Lamport**

## Maximal Abstraction

On va se donner un graphe
- noeud: unite de calcul
- lien: topologie

### Processes (informally)

1. Local event: je calcule fibonnacci
2. Send message: j'ai fini de calculer fibonnacci
3. Receive message: mon voisin a fini de calculer fibo

## Various Timing models

:::danger
Synchronising processes is one of the most difficult part of distributed system
:::

### Asynchronous model

![](https://i.imgur.com/o37gaJr.png)

:::info
No timing assumption about processes and channels, i.e. no physical assumptions about delays.
:::

- Each process have local view of time called logical time
- Any time an event occurs (local or global) at process p, its logical clock is updated:
    - local event increase logical time by one unit
    - global event requires more complex strategies (details in a later lecture).

### Synchronous model

![](https://i.imgur.com/qZU2iil.png)

Il y a un tick
- La tout le monde est vivant
- La tout le monde est mort

Au moment du tick:
- evenements locaux
- envois de messages
- recevoir des messages

*Est-ce que c'est realiste ?*
> D'apres la majorite de la classe, non

:::success
On est capable de simuler ce tick
:::

#### Complexity in Synchronous Model

*Qu'est-ce qui nous ralentit ?*
> On peut avoir un algo en tete qui marche hyper bien mais une fois implemente pas du tout, juste a cause de l'envoie de messages

:::info
**Definition**
Un tick s'appelle un round (espace entre 2 pointilles rouges)

![](https://i.imgur.com/qZU2iil.png)
:::
Pour determiner le tick:
- Utiliser l'horloge interne
- Avoir le meme temps envoye aux machines

2 measures of complexity are considered for synchronous distributed algorithms
- *Time Complexity*: measured in term of number of rounds until all the required outputs are produced.
- *Communicatin Complexity*: measured in term of non-null messages that are sent. (We may also sometime consider the number of bits in these messages).

### Partially Synchronous model

![](https://i.imgur.com/yWCC8qL.png)

Quand on effectue une tache, on sait par avance le temps qu'elle prend.

:::success
Ca nous permet de faire de la detection de fautes (programme qui a crash, etc.)
:::

# Process Failures Model

:::danger
**Process Failures**: Until it fails, a process is supposed to execute the algorithm assigned to it

![](https://i.imgur.com/CnWtJGu.png)

:::

On a une hierarchie de problemes.

:::info
Quand on parle de tolerance aux fautes, on dit qu'on est tolerable jusqu'a $n$ fautes.
:::

- **Arbitrary fault (Byzantines)**
    - Je peux supporter n'importe quel type de faute, meme les actes de malveillance
- **Omissions**
    - On ne va pas recevoir un message
    - C'est un black-out
    - Revenir peut etre dur
- **Lies**
    - A process that does not send expected responses
    - Often due to malicious behavior
- **Crashes**
- **Recovery**

## Link failure

:::info
Crash, Loss, Duplicate can be addressed by some lower level protocol, for instance TCP
:::

:::info
As long as the network remains connected, link crashes may be masked by routing
:::

:::info
Link Crashes reveal a lot of impossibility results (see later lectures)
:::

## Link Abstraction

- **Fair-loss Links**
- **Stubborn links**
- **Perfect links**
    - Le monde ideal

# Combining Abstractions
## Classical combinations

- Fail Stop
- Fail Noisy
- Fail Recovery

# Abstracting Properties
## Basic properties of Distributed Systems

:::info

- Safety
    - states that the algorithm should not do anything wrong
- Liveness
    - On sait qu'on va finir par obtenir une certaine ressource
    - states that eventually something good happens

:::

# Conclusion

:::danger
L'unique facon de faire des systemes distribues est d'utiliser des **abstractions**
:::

