---
title:          "CCMP2 : Seance de revisions"
date:           2020-07-02 11:00
categories:     [S6, tronc commun, CCMP2]
tags:           [S6, CCMP2, tronc commun]
math: true
---

Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/SJfulmi0L)

# Revisions CCMP2
## Middle End
1. Traduction vers le langage Tree
2. Lineariser le code
    * *etape de linearisation*: casser l'arborescence
    * faire remonter les expressions et instructions qui sont imbriquees jusqu'a la racine
    * on doit conserver la semantique de notre programme
    * si on remonte quelque chose trop haut il peut ecraser d'autres instructions
3. Traduction vers des **Block de Bases**
    * commence par un label, fini par un JUMP ou CJUMP
    * necessaire car: les microprocesseurs actuels n'ont pas des if then else, ils connaissent les CJUMP, condition, label
    * on tronconne le code
    * si on a un block qui commence sans labe => on rajoute un label
    * si on a un block qui fini sans jump => on rajoute un jump
    * permet d'avoir des BB qui peuvent etre "bouges" a volonte
## Back End
1. Finir la linearisation
    * Choisir un microprocesseur et regarder son jeu d'instruction
    * Instruction Selection pour trouver la meilleure instruction en supposant qu'on a un nombre de registres illimite
    * Couvrir l'AST par le jeu d'instructions
    * code non generique => diverge en fonction des microprocesseurs
2.  Analyse de vivacite 
    * construire un controle flow graph
    * calculer live in et live out (duree de vie de nos variables)
    * deduit le graphe d'interference => variable a et b vivent simultanement (peuvent pas etre dans le meme registre)
3. Allocation des registres
    * input : AST linearise + graphe d'interference
    * on va travailler sur le graphe d'interference
    * une fois le registre pour une variable trouve on va propager les modification dans l'AST (a = registre 1, b = registre 2, etc.)
    * probleme quand on decremente le nombre de registres
        * mettre des variables dans le meme registre
        * si pas assez de registres: faire un spill, mettre des variables sur la pile
    1. Faire une coloration
    2. Si on n'y arrive pas: faire un spill
    3. Recacul graphe de flow control
    4. Reproduire du in et out
    5. Reproduire un graphe d'interference
![](https://i.imgur.com/UgePR1e.png)

# Partiel
![](https://i.imgur.com/NWFPaM2.png)
![](https://i.imgur.com/5FkEs8j.png)
![](https://i.imgur.com/yQnsAsm.png)
![](https://i.imgur.com/VHxmnUE.png)
![](https://i.imgur.com/FRXGAsX.png)
![](https://i.imgur.com/argKhDy.png)
![](https://i.imgur.com/Nw8VhrO.png)
![](https://i.imgur.com/LleEPsH.png)
On reprend le code et on regarde toutes les utilisations de a.
Une premiere idee serait de faire des utilisations directement avec le stack pointer. Le probleme c'est que les architectures actuelles n'ont pas un double acces de memoire
![](https://i.imgur.com/odD4mue.png)
![](https://i.imgur.com/gOEej1C.png)
