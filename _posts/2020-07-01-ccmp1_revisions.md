---
title:          "CCMP1 : Seance de revisions"
date:           2020-07-01 11:00
categories:     [S6, tronc commun, CCMP1]
tags:           [S6, CCMP1, tronc commun]
math: true
---

Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/ByqNwptAI)

# Rappels

Compilateur a 3 etapes
* front-end
* middle-end
* back-end

On utilise des outils:
1. Le scanner
    * prend en entree un fichier (Java, ...)
    * but : reconnaitre des mots (j'ai reconnu un entier, variable ...)
        * renvoie un token quand reconnais quelque chose
        * token $sujet$, token $verbe$, token complement
2. Le parser
    * marche main dans la main avec le scanner
        * tokens doivent etre connus par le scanner + parser
    * check si le flux de tokens est valide par rapport a une grammaire
        * il faut definir la grammaire: peut etre ambigue ~~TC flashbacks~~
        * ex : Sujet Verbe Complement Point
    * utilise un **arbre de derivation**: $\text{sujet}\to\text{verbe}\to\text{complement}$
        * probleme: embarque tout un tas de choses inutiles
        * ex : $Point$
    * retourne un **AST** (Abstract Syntax Tree)
        * rpz les differents elements du langage source
    * etre capable de gerer les cas d'ambiguite (conflits shift/reduce)
    * verifier que l'AST soit valide
        * utiliser un **visiteur**
    * trouver un mecanisme pour automatiser l'AST: **visiteur**
3. Le binder
    * lier les utilisations aux declarations des variables
    * faire une premiere phase de nettoyage pour etre sur que notre AST est correct
    * si ce n'est pas bon : **erreur de typage**
        * utiliser des regles d'inferences
    * liage declaration-appel 
4. Type-checker
    * verifie si le programme est semantiquement correct
    * parcours l'AST
    * check la coherence des types de variable
    * deduction des types

![](https://i.imgur.com/86onRvQ.png)

# Annale Mars 2018
## Visiteur
Permettent de prendre une hierarchie de classe et d'etre capable de la visiter, cad explorer chacun des elements les un a la suite des autres.
Il a egalement un traitement exclusif d'une classe: un visiteur peut visiter les enfants d'un noeud. Il a un traitement exclusif d'une classe.
Resoudre le probleme du dispatch statique/dynamique.
## Appliquer les regles d'inference
![](https://i.imgur.com/AK4c6Bs.png)


Si je suis capable de montrer que 1 est de type entier je ne fais rien. Si je suis capable de montrer que 4 est de type entier et que je suis capable de montrer que 1 est de type entier alors $4 + 2$ est de type **entier**
Je suis capable de montrer que 3 est de type floatant alors $4 + 2 * 3.0$ est de type floatant.
8.0 est de type flottant alors l'expression est de type floatant
## Difference coerxicion ouvrante/retrecissante
![](https://i.imgur.com/7gCDNFT.png)

* coerxicion ouvrante : prendre un type *petit* et le mettre dans un type plus *gros*
```cpp
int i = ....
float j = i
```
* coexircion fermante : sens inverse mais on perd de l'info
## Reprise sur erreur
![](https://i.imgur.com/P22CYm2.png)
```
if (toto;
blablabla)
```
L'utilisateur peut ecrire quelque chose de invalide mais le programme est capable de nous redonner des informations sur la suite du programme. L'erreur est sur le ';', on se met en mode erreur et on continue a "manger" des tokens jusqu'a retrouver un etat stable pour afficher plusieurs erreurs (ex: retrouver la parenthese fermante).
Lire et discard les tokens jusqu'a retrouver un token valide
## Construction dans un langage existant
### AST
Java, C, C++ (plus de Tiger)
![](https://i.imgur.com/fRrtgGQ.png)

### Liaison des noms
![](https://i.imgur.com/mZ6TEcv.png)

### Que modifie le ebreak
![](https://i.imgur.com/HVU8OOQ.png)
Le ebreak va nous permettre de breaker sur plusieurs niveaux de boucle
1. Le scanner ?
    * oui
2. Le parser?
    * oui
    * ebreak est-il une instruction ou une expression ?
        * **instruction** car ne retourne pas de valeur
3. L'AST?
    * ne seras pas demander car toute la promotion ne fait pas Tiger

### Problemes de typage
![](https://i.imgur.com/zcpT4gi.png)

Verifie qu'on ait un entier et non autre chose. Vu que le ebreak prend un argument c'est forcement une expression, hors un string est une expression. Il va falloir s'assurer dans le type checker que la valeur prise par le ebreak est un nombre.

### Lier le ebreak avec un while
![](https://i.imgur.com/SeKkiEX.png)
On pourrait lier le ebreak avec le while mais on ne sait pas ce qu'il y a la suite car on peut avoir des valeurs que au runtime.

## Desucrage
Prendre une construction et la transformer en une autre construction
![](https://i.imgur.com/9dHNYwn.png)
![](https://i.imgur.com/9sJOJ0q.png)


Evaluation : QCM points negatifs