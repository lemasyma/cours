# CAMA : Ecriture du produit scalaire
:::warning
Attention a l'écriture du produit scalaire !
$$
A \, {\bf d}^k \, . \, {\bf d}^k  \not= A  ({\bf d}^k \, . \, {\bf d}^k)
$$
:::
## Notation matricielle
Pour éviter toute confusion on peut utiliser **la notation matricielle**.
$$
A \, {\bf d}^k \, . \, {\bf d}^k = {\bf d}^k}^T A \, {\bf d}^k
$$
## Exemple : multiplier par $A^{-1}$
* Avec la notation du produit scalaire on risque d'écrire : $$ A^{-1} \, A \, {\bf d}^k \, . \, {\bf d}^k = {\bf d}^k \, . \, {\bf d}^k \quad \textrm{mais c'est faux} $$
* Avec la notation matricielle on écrit : $$ A^{-1} \, { {\bf d}^k }^T A \, {\bf d}^k $$
:::info
Cela nous permet de voir que les matrices ne se simplifient pas.
:::
## Autre notation
Il existe également comme notation **<a, b>** pour le produit scalaire entre a et b. Avec l'exemple precedent on obtient : 
$$
A^{-1} \, < A \, {\bf d}^k \,, \, {\bf d}^k> 
$$
