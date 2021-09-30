---
title:          "CMKV: Implementation d'algorithme"
date:           2021-09-30 09:00
categories:     [Image S9, CMKV]
tags:           [Image, SCIA, S9, CMKV, sudoku, pastis]
description: Implementation d'algorithme
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/rytKW1QEF)

$$
T_{t+1}\leftarrow T_{t+1}\times\alpha
$$

<div class="alert alert-info" role="alert" markdown="1">
Evaluation : projet
</div>


# L'algorithme 

On fait une marche aléatoire 
```
T_
∅ <- ?
loop i_cond <- ?
    tirage
```

On tire un $x_{candidat}$, on preserve tous les $x\neq x_{candidat}$

$$
x=(x_1^{(t)},\dots,\color{blue}{x_{candidat}}, x_{candidat+1}^{(t)}, x_{N}^{(t)})
$$
Au lieu de changer touT le vecteur, on ne change qu'une valeure (le $x_{candidat}$), l'algorithme convergera plus vite

$$
\begin{matrix}
&x_{candidat}=(&\text{idem},&\boxed{i_{random}},&\text{idem},&\boxed{i_{random}},&\text{idem})\\
&&\updownarrow &\searrow&\updownarrow&\swarrow&\updownarrow\\
&&&\nearrow&&\nwarrow&\\
&x^{(t)} = (& &\boxed{} & &\boxed{} &)
\end{matrix}
$$

Comment choisir alpha ? 
On le prend très proche de 1

Algorithme de descente - principe : 
- parcourir toutes les variables
- Et pour chacunes des variables on parcourt toutes les valeurs possibles et on minimise l'energie (U) : Ca converge forcement mais ca converge vers un minimum local (et c'est pas ce qu'on cherche)

$$
x^{(t+1)}=(\text{arg}\min_{\omega_1\in\Omega_1}U(\omega_1,x_2^{(t)}), x_2^{(t)})\quad\text{var #}1\\
x^{(t+2)}=(x_1^{(t+1)}, \text{arg}\min_{\omega_2\in\Omega_2}U(\omega_2,x_2^{(t+1)}))\quad\text{var #}2\\
$$

Ici, la solution (le x que l'on retient) est le x tel que $U_{courant} = min$

<div class="alert alert-info" role="alert" markdown="1">
Tour statistique : si j'itere 1million de fois,c'est sur que j'ai parcouru toutes mes variables
</div>

```
∞ loop
    Umin
    pour toutes les variables
        ... descente
    Ucourant
    si Ucourant = Umin
        conv. or
    sinon
        Umin = Ucourant
```

Notre algo n'est PAS une descente, c'est un optimiseur ! (On cherche minimum global, pas local)

$$
P_{T_{\varnothing}}=\lim_{T\to\infty}P_T\\
$$

Loi aléatoire avec une marche uniforme : c'est le CHAOS

![](https://i.imgur.com/pE38hIP.gif)

*Comment on choisi $T_0$ ?*
On prend une grande et une petite valeur de temperature et on fait une **dichotomie**. On mesure le nombre de fois ou on a monte et descendu en energie, ces mesure doivent etre equivalentes.

*Si on a une temperature trop faible ?*
Alors ce n'est pas une loi uniforme.

$----->T$ Plus T élevée (on va vers la droite) plus on se rapproche d'une loi uniforme

$$
\begin{matrix}
T_{min} &T_{cherche} &T_{max}\\
&\equiv&\\
&\text{uniforme}&
\end{matrix}
$$

Si $T_{min}$ et $T_{max}$ loi uniforme alors on est trop a droite. Inversement, on sera trop à gauche. On veut donc : $T_{max}$ grand et $T_{min}$ petit mais pas trop.


*Comment on fait la dichotomie ?*
Il ne faut pas *uniforme* ou *pas uniforme*, il faut du **suffisemment uniforme**.


**Recap**
On cherche $T_0$ tq $P(T_0)$ suit une loi suffisemment uniforme
Il faut donc prendre un $T_{min}$ et $T_{max}$ avec une loi pas uniforme pour le min et uniforme pour le max.
On fait donc une dichotomie qui nous ramenera a 2 lois suffisemment uniforme pour trouver le $T_0$


![](https://i.imgur.com/AMMFXPo.jpg)

![](https://i.imgur.com/ZhtNcLw.png)

Peu de montées par rapport aux descentes énergétiques $=$ on converge

Si je n'arrive pu à monter alors je suis proche de ma solution


*Comment on optimise des tirages aleatoires ?*
Ou 

$$
i_{\text{candidat swap }1}\quad i_{\text{candidat swap }2}
$$

<div class="alert alert-success" role="alert" markdown="1">
On les precalcule

<div class="alert alert-danger" role="alert" markdown="1">
Le precalcul a un **biais**
</div>

</div>

On va utiliser un tableau circulaire.

```
loop
    icandidat <- aleatoire
```

<div class="alert alert-warning" role="alert" markdown="1">
C'est pas possible, on aura des valeurs enormes
</div>

On a un tableau de valeurs $x_{candidat}$ de longueur $L$:

| $\dots$ | $a_i$ | $\dots$ |
| ------- | ----- |:-------:|

$L$ est tres grand et nombre premier

On va faire un damier, $x^{(t)}=$

| $1$  | $11$ | $2$  | $12$ | $3$  |
| ---- | ---- | ---- | ---- |:----:|
| $13$ | $4$  | $14$ | $5$  | $15$ |
| $6$  | $16$ | $7$  |      | $8$  |
|      | $9$  |      | $10$ |      |

Par exemple, $4$ depend des valeurs qui l'entoure:

|                     | $11\updownarrow$ |                     |
| ------------------- | ---------------- | ------------------- |
| $13\leftrightarrow$ | $4$              | $\leftrightarrow14$ |
|                     | $16\updownarrow$ |                     |

$$
P_T(X=x)=\frac{1}{Z_T}e^{-\frac{U(x)}{\color{blue}{T}}}
$$

<div class="alert alert-info" role="alert" markdown="1">
**Propriete Markovienne**
La probabilite d'avoir $X^i=(x_1,\dots,x_{i-1},x_{i+1},\dots,x_n) = X\setminus X_i$

$$
P(X_i=x_i\vert X^i=x^i) = P(X_i=x_i\vert X_{\nu_i}=x_{\nu_i})
$$

</div>

$$
X_{\nu_i}=(X_{\nu_1^i},\dots,X_{\nu_w^i})
$$

<div class="alert alert-danger" role="alert" markdown="1">
$\nu_i$: voisinnage de $i$
</div>

<div class="alert alert-success" role="alert" markdown="1">
Le voisinnage d'un graphe complet d'un noeud c'est tous les noeuds sauf lui-meme
</div>

$$
\to \overbrace{X_{t-2}\to \underbrace{X_{t-1}\to X_t}_{P(X_t=x_t\vert X_{t-1}=x_{t-1})}}^{\color{blue}{P(X_t\vert X_{t-2})}}
$$

La propriété Markovienne est équivalente à celle des chaines de Markov

$$
\mathcal N(e)\text{ verifie}\begin{cases}
e\not\in \mathcal N(e)\\
e\in\mathcal N(e')\Rightarrow e'\in\mathcal N(e)
\end{cases}
$$

<div class="alert alert-info" role="alert" markdown="1">
**Clique**
C'est un ensemble de sommets qui sont voisins soit:

$$
E=\{\dots e_i\dots\}
\begin{cases}
E\neq\emptyset\\
\text{et}\\
\forall e,e'\in E,e\mathcal N e'\\
\text{ou}\\
\bar E=1
\end{cases}
$$

$e\mathcal N e'$: $e$ et $e'$ sont voisins

</div>

E est un ensemble de sommet 2 à 2 voisins

un singleton est une clique, on dit que c'est une clique d'ordre 1 

Une clique d'ordre n c'est un ensemble de n sommet 2 a 2 voisins


```
4 ord 1
4 ord 2
1 ord 3
----
9
```


Un graphe complet que l'on reduit aux voisins permet de reduire la dependance des variables.

$$
P(X=x)=\Pi_{\text{c clique}}\phi(x_c)
$$
- $\phi(x_c)$: fonction potentiel pour la clique $c$

![](https://i.imgur.com/D1HeI0H.png)

Toujours vrai si $\not\exists x, P(X=x)=\varnothing$

$$
\begin{aligned}
P(X=x)&=\frac{1}{Z}e^{-U(x)}\\
&= \frac{1}{Z}e^{-\sum_{c}E_c(x_c)}
\end{aligned}
$$
- Avec $U_c=\phi_c$ fonction potentielle pour la clique $c$
 
Modele graphique qui est un champs de Gibbs ?


<div class="alert alert-danger" role="alert" markdown="1">
On doit definir les fonctions $U_c$ et $\phi_c$, avec:

$$
U(x)=\sum_{c}U_c(x_c)
$$

</div>

$\bar c$: ordre de la clique

# Exemple

Sur une image en niveau de gris


$$
P(X=x\vert Y=y)=e^{-\sum_cU_c(x_c,y)}
$$

$X_i$ depend de $X_{i+1}$, $X_{i-1}$, $X_{i+nc}$, $X_{i-nc}$

![](https://i.imgur.com/fm0a9YI.png)


Probabilité équiprobable -> U vaut 0


on a une vraissemblance quand on melange X et Y
$$L(X=x_i|Y=y_i) \text{ proportionnelle à } e^{-U_{L}(x_i,y_i)}$$
Avec $U_L(...)$ une clique d'ordre 2

$$
U(X_i=\underbrace{x_i}_{\text{ordre }1})=\frac{1}{2}\\
U_1(\underbrace{\text{noir}}_{\text{dans }x})=\frac{1}{2}\\
U_1(\text{blanc})=\frac{1}{2}\quad\forall\text{ probabilite}
$$


$$
U_2(\underbrace{x_i,x_j}_{\text{ordre }2} = 1_{x_i\neq x_j})
$$
Avec $i$ et $j$:
- voisins
- independants

Definissons $U_L$
$$
U_L(x_i,y_i) = \begin{cases}
255-y_i&\text{si } x_i=\text{blanc et } j\text{ voisins et inde}\\
y_i&\text{sinon}
\end{cases}
$$

Tadaaa commande magique :clap: :clap: :cake: :cactus: :call_me_hand: :jack_o_lantern: :cat: 
:heart: 


$$
\begin{aligned}
U(x,y)&=\sum_cU_c(x_c,y)\\
&=\sum_iU_1(x_i)+\overbrace{\sum_{i,j_{voisins}}U_2(x_i,x_j)}^{\sum_i\sum_{j\in\mathcal N(i)}U_2(x_i,x_j)}+\sum_iU_2(x_i,y_i)\\
&= \sum_i\biggr(\overbrace{
U_2(x_i,y_i)
}^{\color{blue}{L(X\vert Y)
}}
+\overbrace{
\underbrace{
U_1(x_i)
}_{\text{ordre } 1}+
\underbrace{
\sum_{j\in\mathbb N(i)}U_2(x_i,x_i)
}_{\text{ordre } 2}
}^{P_{(\text{a priori})}}\biggr)\\
\Rightarrow U(x,y)&=\sum_iU_i(x_i,x_{\nu_i},y_i)
\end{aligned}
$$

Les énergies sont liées au proba 
P appriori = P sachant ...
Produit de P = Somme U (Car exp)



