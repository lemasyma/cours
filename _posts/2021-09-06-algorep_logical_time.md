---
title:          "ALGOREP: Logical Time"
date:           2021-09-06 10:30
categories:     [Image S9, ALGOREP]
tags:           [Image, SCIA, S9, AlGOREP]
math: true
description: Logical Time.
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/B19VSrQzK)

[Les slides du cours](https://www.lrde.epita.fr/~renault/teaching/algorep/)

# Problem statement
*Dans la classe, qui s'est reveille avant qui ?*
> $1^{ere}$ proposition: on demande l'heure du reveil de tout le monde
> Probleme: il faut que tout le monde ait un horloge

<div class="alert alert-warning" role="alert" markdown="1">
On ne peut pas faire l'hypothese qu'on a une horloge pour tout le monde, sinon on est synchrone
**Les horloges peuvent avoir des divergences**
</div>

> Quelqu'un peut dire qu'il est debout depuis 5h alors qu'en fait il etait 8h

> $2^{eme}$ proposition: On envoie un message des qu'on se leve (ne le fait pas, c'est pas bon pour la sante)
> On ne doit pas avoir de delais de transmission du message

<div class="alert alert-danger" role="alert" markdown="1">
***Quel evenement a eu lieu avant quel evenement ?***
</div>

*Est-ce qu'on a vraiment besoin de cette info ?*
> $1^{ere}$ proposition: pour savoir quand est-ce qu'une faute est arrivee et on relance le systeme dans un etat precedent $\Rightarrow$ c'est une **snapshot**

<div class="alert alert-warning" role="alert" markdown="1">
On n'a pas de garanti sur le delais des messages
</div>
Il faudrait prendre en compte la latence des messages et c'est trop complique

<div class="alert alert-success" role="alert" markdown="1">
On va utiliser des **horloges logiques**
</div>
On va essayer de construire un systeme ou on date les evenements par rapports a des evenements logique $\Rightarrow$ _**les envois de messages**_

> "J'ai vu le message d'Etienne avant de manger ma tartine"

Consider 3 processes $E$, $F$ et $G$
- With some local events: $e_1$, $f_1$, $f_3$, $g_2$, $g_3$
- With some *send* events: $g_1$, $f_2$, $e_2$
- With some *receive* events: $e_3$, $f_4$, $g_4$

![](https://i.imgur.com/rZQNUyp.png)

Ces 2 executions sont **impossibles a distinguer**

![](https://i.imgur.com/tF5SNlq.png)

<div class="alert alert-success" role="alert" markdown="1">
On va donner une notion de progres
</div>

# Scalar Time: Lamport Clocks

## Definitions

<div class="alert alert-info" role="alert" markdown="1">
![](https://i.imgur.com/53LQmNY.png)
</div>

<div class="alert alert-info" role="alert" markdown="1">
**Rule R1**
Before executing an event (send, receive, or internal), process pi executes the following

$$
C_i:=C_i+d\quad\text{with } d\gt0\text{, typically 1}
$$

</div>

<div class="alert alert-info" role="alert" markdown="1">
**Rule R2**
Each message piggybacks the clock value of its sender at sending time.

When a process $p_i$ receives a message with timestamp $C_{msg}$ , it executes the following actions :
- $C_i := max(C_i, C_{msg} )$
- Execute R1 and deliver message

</div>

## Example

1.
![](https://i.imgur.com/NRtJyFW.png)

2.
![](https://i.imgur.com/DZ0i5VA.png)

3.
![](https://i.imgur.com/wG1m8cY.png)

4.
![](https://i.imgur.com/JAapPIg.png)

5.
![](https://i.imgur.com/0eAzDhH.png)

6.
![](https://i.imgur.com/r9P4F0D.png)

7.
![](https://i.imgur.com/3snkcnA.png)

## Remarques

- On peut utiliser l'horloge de Lamport pour l'ordre
    - Il suffit de dire $e_1 \lt g_1$
- Si on incremente toujours de $1$, $h-1$ sera toujours le temps requis pour atteindre le process $e_h$
- No Strong Consistency

## Problem

<div class="alert alert-danger" role="alert" markdown="1">
The main problem in totally ordering events is that two or more events at different processes may have identical timestamp !
</div>

# Vector Time: Mattern Clocks

- On va toujours maintenir un compteur
- On va avoir une horloge local par processus
    - On gere comme une horloge de Lamport
- On maintient son horloge et celle de tout le monde

*Comment est-ce qu'on peut connaitre l'etat d'un processus ?*
> En envoyant un message

> On echange avec une $3^e$ personne qui n'a jamais echange avec Etienne
> On lui transmet l'avancement d'Etienne
> Si cette 3e personne envoie un message a Etienne, elle connaitra son avancee

*Pourquoi une personne tierce ?*
> Si on est que 2, on echange des messages qu'a 2 et on ne peut pas mettre en avant des horloges complexes

*En pratique, comment est-ce qu'on fait passer notre compteur local ?*
> Quand on structure un programme distribue, on incremente l'horloge local a des points stables (barre de progression de chargement, etc.)

## Example

![](https://i.imgur.com/jqziiZe.png)

> On envoie un message a $G$, on veut savoir s'il l'a recu mais il ghost
> Indirectement, on apprend que $G$ a avance de $5$ elements donc il est vivant, *mais est-ce qu'il a recu le message ?*
> On sait que $F$ n'avait pas d'information de notre part au depart
> Le $2$ envoye par $E$ a $G$ a ete renvoyee par $F$, sachant que $E$ n'a pas envoye de message a $F$ auparavant
> **On sait donc que $F$ a recu le message de $E$**

## Remarques

![](https://i.imgur.com/cz6tRvK.png)

## Efficient Implementation of Vector Clocks

*Comment on implemente ca de maniere efficace ?*

<div class="alert alert-info" role="alert" markdown="1">
**Implementation**
On peut garder les $n$ derniers messages avec nos voisins, on peut juste envoyer le differentiel de la derniere heure envoyer par quelqu'un et l'horloge courante
</div>

## Problem

<div class="alert alert-danger" role="alert" markdown="1">
Qu'est-ce qu'il se passe si j'ai une inversion de messages ?
</div>

*Est-ce qu'on est capable de gerer ce cas avec les horloges precedentes ?*
> Non.

![](https://i.imgur.com/5O2V6hu.gif)

<div class="alert alert-success" role="alert" markdown="1">
On va utiliser les **ragots** $\Rightarrow$ des **matrices d'informations**
</div>
> On m'a dit que tu m'as dit que...

$$
\begin{vmatrix}
E&F_E&G_E\\
E_F&F&G_F\\
E_G&F_G&G
\end{vmatrix}
$$

![](https://i.imgur.com/I5bka2J.png)

*La machine qui a le plus de communication serait-elle celle qui a le plus de chance d'etre a jour sur la timeline des processus sur chaque machine ?*
> Oui.

# Virtual Time System

<div class="alert alert-info" role="alert" markdown="1">
**Definition**
Virtual time system is an (**optimistic**) paradigm for organizing and synchronizing distributed systems
</div>

- Relies on Time Warp mechanism, i.e. lookahead-rollback mechanism
- When a conflict is discovered, the offending processes are rolled back to the time just before the conflict
- Processes are then executed forward along the **revised path**

# Conclusion

- Different kind of logical time
- Virtual time system (Jefferson) is a paradigm for organizing and synchronizing distributed systems

