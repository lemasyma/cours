---
title:          "ALGOREP: What is Model-Checking ? How to build a Model Checker ?"
date:           2021-09-20 14:00
categories:     [Image S9, ALGOREP]
tags:           [Image, SCIA, S9, AlGOREP]
math: true
description: What is Model-Checking ? How to build a Model Checker ?
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/ryqrFeUXF)

[Les slides du cours](https://www.lrde.epita.fr/~renault/teaching/algorep/)

*Si on a un ping pong, comment on verifie que l'algo marche ?*
> On lance et un espere que ca marche?
> Non ca c'est etre religieux

<div class="alert alert-danger" role="alert" markdown="1">
Il faut check toutes les relations et entralecements possibles (effets de bord, etc).
</div>

<div class="alert alert-success" role="alert" markdown="1">
Il faut faire des preuves automatiques
</div>

On va prendre des outils capables d'en faire, en utilisant
- La **description** $\neq$ *implementation* du systeme distribue
    - S'abstraire des pbs de langage

# Qu'est-ce qu'un systeme ?

On veut qu'une fusee n'explose pas en vol

# Why is a model required ?

On va considerer que TOUS les systemes qu'on etudie soit un systeme infini.

Le code suivant serveur peut etre considere un systeme:

```cpp=
unsigned received_= 0;
while (1)
{
    accept_request();
    received_ = received_ + 1 ;
    reply_request();
}
```

<div class="alert alert-success" role="alert" markdown="1">
Avec un modele, on enleve le probleme de `received_`
</div>

![](https://i.imgur.com/1Y6k9jq.png)

## A more realistic example

On a une abstraction des differents comportements de notre systeme

![](https://i.imgur.com/pAtexf4.png)

On est capable de construire l'integralite du systeme. On veut faire le produit cartesien de tout le monde.

![](https://i.imgur.com/WS3YtPO.png)

A l'etat initial du systeme, tout le monde est dans l'etat $1$.

Pour passer de l'etat $111$ a l'etat $211$, on doit avoir en meme temps un message recu et en transit.

*Est-ce qu'on peut avoir 2 envois simultanement ?*

# Kripke structure

![](https://i.imgur.com/rqDYHuQ.png)

On definit un alphabet, un etat, une transition.

![](https://i.imgur.com/4hzeDyn.png)


![](https://i.imgur.com/Ufq8OxJ.png)

## Example

![](https://i.imgur.com/png8488.png)

<div class="alert alert-info" role="alert" markdown="1">
On utilise des booleens qu'on appelle des **propositions atomiques**
</div>
- On etiquete notre modele pour savoir si on peut atteindre un chemin

# How to express finite behavior ?

*Combien de propositions atomiques ?*
> 3 (rouge, orange, vert)

![](https://i.imgur.com/yU43i0J.png)

*Comment on exprime les comportements a l'infini ?*
> On utilise une logique

## Linear Temporal Logic

![](https://i.imgur.com/PULGKlU.png)

On s'interesse aux operateurs:
- $U$: "vrai jusqu'a qu'autre chose soit vrai"
- $X$: "a la prochaine etape c'est vrai"

## Globally

![](https://i.imgur.com/YE8Qz2F.png)

## Finally

![](https://i.imgur.com/3A8v1UD.png)

## Next

![](https://i.imgur.com/RbB1UJS.png)

## Until

![](https://i.imgur.com/BTqPeRe.png)

## Retour au feu rouge

![](https://i.imgur.com/eAFHerm.png)

![](https://i.imgur.com/GfvJgRZ.png)

# Automata for model checking

![](https://i.imgur.com/8S8W9ih.png)

<div class="alert alert-info" role="alert" markdown="1">
**Buchi**: Transformer une logique d'evenement en automate

![](https://i.imgur.com/8mRO1xQ.png)

</div>

## Express property automaton

![](https://i.imgur.com/9IApuvL.png)

## Automata approach for model checking

![](https://i.imgur.com/fiSh4ce.png)

On a reussi a creer un modele pour Aut. A et Kripke. On fait un produit synchronise

<div class="alert alert-info" role="alert" markdown="1">
**Produit synchronise**
On a l'automate de la propriete

![](https://i.imgur.com/6P1LFsd.png)

On a l'automate du systeme. Quand on lit $d_1$ et $r_1$, on doit s'assurer de lire la meme chose dans notre systeme, on supprime les chemins qui font diverger ces valeurs, par le produit cartesien.
</div>

![](https://i.imgur.com/JgsjEd4.png)

On regarde cette automate, si on trouve une pastille noir qui s'appelle en boucle, on a un contre-exemple a notre propriete.

![](https://i.imgur.com/BH8OjA1.png)
> La reponse est oui

![](https://i.imgur.com/m6Y3jyu.png)
