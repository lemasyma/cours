---
title:          "CCMP2 : Intermediate Representation"
date:           2020-04-27 11:00
categories:     [S6, tronc commun, CCMP2]
tags:           [S6, CCMP2, tronc commun]
math: true
---

Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/HJ06Js4yD)
# Cours du 27/04
Boulot qui reste a faire:
* Lineariser le programme
* Allocation des registres
* Gerer la pile

## Compilers structure
Ends:
* *front end*: analysis
    * lexical analysis (scanning)
    * synctactic analysis (parsing)
    * ast generation
    * static semantice analysis (type checking)
    * source language specific optimizations
    * hir generation
* *middle end*: generic synthesis
    * optimisations generiques
* *back end*: specific synthesis
    * register allocation

The gcc team suggests:
* *front-end* name ("a front end")
* *front-end* adjective ("the front-end interface")

## Retargetable Compilers
![](https://i.imgur.com/8V0vB0i.png)
Si on veut generer du ARM a partir du JAVA, le trait rpz un compilateur complet. On rajoute un compilateur de JAVA a MIPS, de JAVA a IA-32, etc. et ce pour tous les compilateurs en entree.
Cette strategie n'est pas bonne car il y a beaucoup de compilateurs et de la duplication de code.

Supposons qu'on aie une representation intermediaire:
![](https://i.imgur.com/Jca3vYB.png)
Il suffit plus d'un traducteur de la representation intermediaire vers ARM, MIPS, etc. On a plus que 4 traducteurs, on a transforme une multiplication en addition.

<div class="alert alert-danger" role="alert" markdown="1">
Comment definir cette representation intermediaire?
</div>
On a besoin d'une representation flexible pour pouvoir etre la cible des langages de hauts niveaux mais assez assembleur pour etre traduit en assembleur.
1. Le front-end "tire" le langage intermediaire vers lui
2. Le back-end "tire" la representation intermediaire pour etre le plus proche possible du langage assembleur
### Premiere idee: baricentre
<div class="alert alert-info" role="alert" markdown="1">
Affecter un poids aux langages en entree et ceux en sortie: avoir un **baricentre**
</div>
Si tout le mone a un poids de 1, le langage intermediaire sera plutot front-end, sinon plutot backend.

<div class="alert alert-warning" role="alert" markdown="1">
Comment calculer le baricentre de tous mes langages ?
</div>
On fait l'instersection de toutes les fonctionnalites des langages.
<div class="alert alert-danger" role="alert" markdown="1">
Qu'est-ce qui se passe le jour ou on rajoute un nouveau langage? **Le baricentre va bouger**.
</div>
### Seconde idee
Deux langages intermediaires: un pour le front-end, un pour le back-end
![](https://i.imgur.com/OAxScQO.png)
Traduction de Java a 1 c'est facile, de 1 a 2 difficile.
On aura plein de petits traducteurs simples et un gros traducteur complique, on a seulement 10 traducteurs.

On rajoute deux nouveaux langages intermediaires:
![](https://i.imgur.com/aYOptRX.png)
La traduction de 1 vers 3 et de 4 vers 2 est moins dure que de 1 vers 2.
<div class="alert alert-danger" role="alert" markdown="1">
On est en train de **reconstruire** une multiplicite de traducteurs.
</div>
### Idee finale
1. couche: *j'enleve la partie objet*
2. couche: enlever le support des fonctions variadique
3. couche: transformer les for en while
4. couche: enlever une autre fonctionnalite
5. etc.

![](https://i.imgur.com/zyZF2FX.png)


C'est le **desucrage**. Dans notre langage intermediaire on veut desucrer notre langage en entier.
<div class="alert alert-danger" role="alert" markdown="1">
Comment definir tous ces langages intermediaires?
</div>
Syntax, grammaire, type-checker, etc.
Deux solutions:
1. Nouveau parser/lexer mais pas coherent
2. On va definir des langages intermediaires mais on va jamais ecrire de parser
    * on va definir une grammaire
    * on va traduire l'AST de notre langage original en AST du langage choisir

### Other Compiling Strategies
* Intermediate language-based strategies: SmartEiffel, GHC
* Bytecode strategy: Java bytecode (JVM), CIL (.NET)
* Hybrid approaches: GCJ (Java bytecode or native code)
* Retargetable optimizing back ends: MLRISC, VPO (Very Portbale Optimizer), and *somehow* C-- (Quick C--)
* Modular systems: LLVM (compiler as a library, centered on a typed IR). Contains the LLVM core libraries, Clang, LLDB, etc. Also:
    * VMKit: a substrate for virtual machines (JVM, etc.)
    * Emscripten: an LLVM-to-JavaScript compiler. Enables C/C++ to JS compilation

<div class="alert alert-danger" role="alert" markdown="1">
Intermediate Representations (IR) are fundamental.
</div>

## Intermediate representations
### Format? Representation? Language?
*Intermediate representation:*
* a faithful model of the source program
* "written" in an abstract language, the **intermediate language**
* may have an external syntax
* may be interpreted/compiled (havm, byte code)
* may have different levels (gcc's Tree is very much like C)

### What language flavor ?
* imperative?
    * Stack based?
    * Register based?
* Functional?
    * Most function languages are compiled into a lower lever language, eventually a simple $\lambda$-calculus.
* Other?

### What level?
A whole range of expressivities, typically aiming at making some optimizations easier:
* Keep array expressions?
    * **Yes**: adequate for dependency analysis and related optimizations
    * **No**: Good for constant folding, strength reduction, loop invariant, code motion, etc.
* Keep loop construcs?

<div class="alert alert-danger" role="alert" markdown="1">
What level of machine independence?
* Explicit register names?
</div>
On doit construire notre langage en essayant d'etre le plus proche possible du code assembleur tout en etant suffisemment abstrait pour pas faire rentrer le nom des registres

### Designing an Intermediate Representation
> Intermediate-language design is largely an art, not a science.
> Muchnink, 1997

```cpp=
float a[20][10]
...
a[i][j+2]
```

Traduction dans les langages intermediaires:
```go=
t1 <- a[i, j+2]
```
<div class="alert alert-info" role="alert" markdown="1">
On va avoir besoin de **temporaires** pour noter les resultats intermediaires.
</div>
```go=
t1 <- j + 2
t2 <- i * 20
t3 <- t1 + t2
t4 <- 4 * t3
t5 <- addr a
t6 <- t5 + t4
t7 <- *t6
```
On a une approche progressive plus agreable qu'une approche directe.
```go=
r1 <- [fp - 4]
r2 <- r1 + 2
r3 <- [fp - 8]
r4 <- r3 * 20
r5 <- r4 + r2
r6 <- 4 * r5
r7 <- fp - 216
f1 <- [r7 + r6]
```
Sans la traduction precedente, il est impossible de comprendre comment cette traduction fonctionne.

### GCC
![](https://i.imgur.com/fjm3kTD.png)

### Stack Based: Java Byte-Code
```java=
class Gcd {
    static public int gcd(int a, int b) {
        while (a != b) {
            if ( a > b)
                a -= b;
            else
                b -= a;
        }
        return a;
    }
    
    static public int main(String[] arg) {
        return gcd(12, 34)
    }
}

```
![](https://i.imgur.com/G8trZai.png)

### Stack Based (Edwards, 2003)
Advantages
* Trivial translation of expressions
* Trivial interpreters
* No pressure on registers
* Often compact

Disadvantages
* Does not fit with today's architecture
* Hard to analyze
* Hard to optimize

### Register Based *tc*'s Tree
<div class="alert alert-info" role="alert" markdown="1">
Une representation sous forme de registre est fatalement **plus verbeux**.
</div>
Du a: 
* La pile
* L'epilogue
* Le prologue

Chaque fonction utilise un certain nombre de registres, il y a beaucoup de travails supplementaires pour maintenir la coherence des registres.

### Register Based: What structure ?
How is the structure coded ?
* **Addresses**
    * Expressions and instructions have names or (absolute) addresses. (Stack based is a bit like relative address)
        * 2 address instructions ? (*triples*)
        * 3 addresses instructions ? (*quadruples*)

Quadruples vs Triples:
```go=
i <- i + 1

t1 <- i + 1
t2 <-  p + 4
t3 <- *t2
p <- t2
t4 <- t1 < 10
*r <- t3
if t4 goto L1
```
```go=
(1) i + 1
(2) i sto (1)
(3) i + 1
(4) p + 4
(5) *(4)
(6) p sto (4)
(7) (3) < 10
(8) *r sto (5) 
(9) if (7), (1)
```
On note le resultat de chaque ligne dans (nb). Autant ne pas prendre cette strategie et prendre une proche des microprocesserus actuels.

### Register Based (Edwards, 2003)
Advantages:
* Suit today's architecture
* Clearer data flow

Disadvantages
* Harder to synthesize
* Less compact
* Harder to interpret

## Tree
On a besoin d'un langage intermediaire qui nous sert de support pour le reste du cours
### Grammar
![](https://i.imgur.com/jBq9xdN.png)
### Tree sample
![](https://i.imgur.com/d4zSAYb.png)

# Memory management
On en train de faire remonter les infos du microprocesseur au langage intermediaire, on doit gerer le minimum possible de la memoire pour rester abstrait
## Memory Hierarchy
Different kinds of memory in a computer, with different performances:
* **Registers** Small memory units built on the CPU
* **L1 Cache** Last main memory acces results
* **L2 Cache** (MB, 10 cycles)
* **Memory** The usual ram (GB, 100 cycles)
* **Storage** Disks (100GB)

Use the registers as much as possible

### Register Overflow
<div class="alert alert-info" role="alert" markdown="1">
Si notre langage a pas la recursion, on n'a pas de pile a gerer.
</div>
What if there are not enough registers ? Use the main memory, but how?
Recursion:
* **Without:** Each name is bound once. It can be statically allocated a single unit of main memory (Cobol, Concurrent Pascal, Frotran)\
* **With:** a single name can be part of several concurrent bindings. Memory allocation must be dynamic

### Dynamic Memory Allocation
Depending on the persistence, several models:
* Global: global object whose liveness is equal to that of the program, are statically allocated
* Automatic: liveness is bound to that of the host function
* Heap: Liveness is indenpendant of function liveness
    * User controlled: malloc/free
    * Garbage collected
* Stack
![](https://i.imgur.com/fdJuAyu.png)

## Activation Blocks
* In recursive languages, a single routine can be "opened" several times concurrently
* An *activation* designates one single instance of execution
* Automatic variables are bound to the liveness of the activation
* Their location is naturally called *activation block* or *stack frame*

### Activation Blocks Contents
Data to store on the stack:
* arguments: incoming
* local varibales: user automatic variables
* return address: where to return
* saved registers: the caller's environment to restore
* temp: compiler automatic variables, spills
* static link: when needed

### Activation Blocks Layout
Est-ce qu'on peut mettre le content dans l'ordre que je veux ?
<div class="alert alert-info" role="alert" markdown="1">
On doit decider d'un layout respecte par tous les compilateurs.
</div>
The layout is suggested by the constructor.
![](https://i.imgur.com/Z3s32f7.png)
<div class="alert alert-danger" role="alert" markdown="1">
* **fp**: frame pointer
* **sp**: stack pointer
</div>
Au milieu de ces 2 pointers on a notre block d'activation. Lors d'un appel de fonction, on descend **fp** sur **sp** puis on descend **sp**. On doit etre capable de stocker l'ancienne valeur de **fp**.

### Flexible Automatic Memory
*auto*: Static size, automatic memory
*malloc*: Dynamic size, persistent memory
Automatic memeory is extremely convenient
```c=
int
open2(char* str1, char* str2, int flags, int mode){
    char name[strlen(str1) + strlen(str2) + 1];
    strcpy(strcpy(name, str1), str2);
    return open(name, flags, mode)
}
```
On est en train de faire un **tableau dynamique**.

On est sur une variable locale stockee sur la pile, cad stockee sur le bloc d'activation. On doit etre capable de preallouer la zone necessaire. Hors ici on dit que la taille de la zone depend des parametres au runtime et ne sera pas connu lors de la compilation.

Pour une meme fonction f, on peut avoir des blocs d'activation de taille variable. Au moment ou on rentre dans la fonction on doit pousser le stack pointer vers le bas avec **alloca**:
```c=
int
open2(char* str1, char* str2, int flags, int mode){
    char *name = (char *) alloca(strlen(str1) + strlen(str2) + 1);
    strcpy(strcpy(name, str1), str2);
    return open(name, flags, mode)
```

### Advantages of alloca
* Using alloca wastes very little space and is very fast
* On peut simuler alloca

## Nonlocal variables
<div class="alert alert-info" role="alert" markdown="1">
Une variable est consideree comme une variable non locale si elle est declaree dans une fonction englobante et utilisee dans une autre fonction imbriquee.
</div>
### escapes-n-recursion
```ocaml=
let function trace(fn: string, val: int) =
    (print(fn); print("("); print_int(val); print(")"))
    
    function one(input : int) =
    let function two() =
        (trace("two", input); one(input - 1))
    in
        if input > 0 then
            (two(); trace("one", input))
    end
in
    one(3); print("\n")
end
```
Resultat de l'execution:
![](https://i.imgur.com/xBIh9yO.png)
![](https://i.imgur.com/tAO1Kxr.png)
