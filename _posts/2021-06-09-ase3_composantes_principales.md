---
title:          "ASE3: Analyse en composantes principales"
date:           2021-06-09 09:00
categories:     [tronc commun S8, ASE3]
tags:           [tronc commun, ASE3, S8, ACP]
description:    Analyse en composantes principales
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/rJwkEJC9u)

# Donnees et leurs caracteristiques

## Tableau des donnees

Les observations de $p$ variables sur $n$ individus sont regroupes en une matrice $X$ a $n$ lignes et $p$ colonnes

$$
X=\begin{matrix}te_1 \\ \vdots \\ te_i \\ \vdots \\te_n\end{matrix}\begin{pmatrix}
X^{(1)} &\dots &X^{(j)} &\dots &X^{(p)}\\
\vdots&\vdots&\vdots&\vdots&\vdots\\
\dots&\dots &\color{red}{X_i^{(j)}} &\dots &\dots\\
\vdots&\vdots&\vdots&\vdots&\vdots\\
\dots&\dots&\dots&\dots&\dots
\end{pmatrix}\\
te_i=(X_i^{(1)},X_i^{(2)},\dots,X_i^{(j)},\dots,X_i^{(p)})\\
e_i=\begin{pmatrix}X_i^{(1)} \\ \vdots \\ X_i^{(j)} \\ \vdots \\ X_i^{(p)}\end{pmatrix}
$$

$$X_i^{(j)}$$ est la valeur prise par la variable $X$ sur le ieme individu.

## Matrice des poids

On associe a chaque individu un poids $p_i\ge0$ (probabilite de choisir l'individu)

$$
\sum_{i=1}^np_i=1, D=
\begin{pmatrix}
    p_1 &0&\dots&0 \\ 
    0 &p_2&\dots&0 \\ 
    \vdots &\vdots &\ddots&\vdots\\
    0 &0 &\dots &p_n
    \end{pmatrix}
$$

Si $p_i=\frac{1}{n}\Rightarrow D=\frac{1}{n}I_n$ ou $I_n$ matrice identite $$\begin{pmatrix} 1&0&\dots &0 \\ 0&1&\dots&0 \\ \vdots&\vdots&\ddots &\vdots \\ 0 & 0&\dots&1 \end{pmatrix}$$ $\forall i=1,\dots,n$

## Centre de gravite
La vecteur $g$ des moyennes arithmetiques de chaque variable $X^{(j)}$ est definie par $g=(\bar X^{(1)},\bar X^{(2)},\dots,\bar X^{(p)})$

$$
\bar X^{(j)}=\sum_{i=1}^np_iX_i^{(j)}\quad\text{moyenne de } X^{(j)}\quad\forall j\in [1,p]
$$

<div class="alert alert-danger" role="alert" markdown="1">
Le tableau des donnees centrees est la matrice Y telle que 

$$
y_i^{(j)}=X_i^{(j)}-\bar X^{(j)}\quad\forall j\in[1,p], \forall i\in[1, n]
$$

</div>

## Matrice de variance-covariance et matrice de correlation

<div class="alert alert-info" role="alert" markdown="1">
**Definition**:
On appelle matrice de variance-covariance:

<div class="alert alert-danger" role="alert" markdown="1">

$$
V=Y^TDY
$$

</div>
</div>

Si on note $D_{\frac{1}{S}}$ la *matrice diagonale des inverses des ecarts-types*:

$$
D_{\frac{1}{S}} = \begin{pmatrix}
\frac{1}{S_1} &\dots &0\\
\vdots &\ddots &\vdots \\
0&\dots&\frac{1}{S_p} 
\end{pmatrix}
$$

ou:
- $S_j=\sqrt{V(X^{(j)})}=\sqrt{\sum_{i=1}^np_i(X_i^{(j)}-\bar X^{(j)})^2}$
- $V(X^{(j)})$: variance de $X^{(j)}$
- $S_j$: ecart-type de $X^{(j)}$

On appelle la matrice des donnees centrees et reduite: $Z$ telle que:

$$
Z_i^{(j)}=\frac{y_i^{(j)}}{S_j}
$$

<div class="alert alert-danger" role="alert" markdown="1">
Matriciellement:

$$
Z=Y\bullet D_{\frac{1}{S}}
$$

</div>

La matrice regroupant les coefficients de correlation lineaire entre les $p$ variables est $R$:

$$
R=\begin{pmatrix}
1&\dots&p_{ij}\\
\vdots&\ddots&\vdots\\
p_{ij}&\dots&1
\end{pmatrix}\quad\text{symetrique}\\
r_{ij}=\underbrace{p_{ij}}_{\text{coefficient de correlation}}=\frac{Cov(X^{(i)}, X^{(j)})}{S_iS_j}
$$

Ou: $Cov(X^{(i)}, X^{(j)})$: covariance

$$
Cov(X^{(i)}, X^{(j)})=\sum_{k=1}^np_k\underbrace{y_k^{(i)}y_k^{(j)}}_{\text{produit scalaire des variables centrees}}
$$

**Remarque:**

$$
\begin{aligned}
R&=D_{\frac{1}{S}}VD_{\frac{1}{S}}\\
&=D_{\frac{1}{S}}Y^TDYD_{\frac{1}{S}}\\
&\Leftrightarrow\color{red}{\boxed{R=Z^TDZ}}
\end{aligned}
$$

# Espaces des individus
Chaque individu etant un vecteur defini par $p$ coordonnees est considere comme un element d'un espace vectoriel $F$ appele *l'espace des individus*.
Les $n$ individus forment alors un nuage de points dans $F$ et $g$ en est le barycentre (ou centre de gravite).

On munit l'espace $F$ d'une metrique (distance):

$$
\underbrace{<e_i, e_j>}_{\text{produit scalaire}}=e_i^TMe_j
$$

ou: $M$ est une matrice symetrique et definie positive (S.D.P)

**Remarque:** si $M=I$ (matrice identite), on se retrouve avec le produit scalaire usuel.

Si $$M=D_{\frac{1}{S^2}}=\begin{pmatrix}\frac{1}{S_1^2}&\dots&0 \\ \vdots &\ddots &\vdots \\ 0 &\dots &\frac{1}{S_p^2}  \end{pmatrix}$$ cela revient a diviser chaque caractere par son ecart-type.

## Inertie

<div class="alert alert-info" role="alert" markdown="1">
**Definition:**
On appelle inertie totale du nuage de points la moyenne ponderee des carres des distances des points au centre de gravite:

$$
\begin{aligned}
I_g&=\sum_{i=1}^np_i(e_i-g)^TM(e_i-g)\\
&=\sum_{i=1}^np_i\Vert e_i-g\Vert^3
\end{aligned}
$$


</div>

### Proprietes de l'inertie

On peut montrer que l'inertie du nuage est egale a la trace de la matrice $MV$:

<div class="alert alert-danger" role="alert" markdown="1">

$$
I_g=Trace(MV)=Trace(VM)
$$

</div>

# Espace des variables

On note $E$: l'espace des variables 

$$
X^{(j)}=\begin{pmatrix}X_i^{(j)} \\ \vdots \\ X_n^{(j)} \end{pmatrix}
$$

On munit $E$ de la metrique $M=D$ avec D la matrice des poids 

$$
\underbrace{<X^{(j)}, X^{(k)}>}_{\text{produit scalaire}}=(X^{(j)})^TDX^{(k)}
$$

Si les variables sont centrees:

$$
\begin{aligned}
(X^{(j)})^TDX^{(k)}&=\sum_{i=1}^np_iX^{(j)}_iX^{(k)}_i\\
&=Cov(X^{(j)}, X^{(k)})
\end{aligned}
$$

La norme de $X^{(j)}$ (variable centree)

$$
\begin{aligned}
\Vert X^{(j)}\Vert^2&=<X^{(j)}, X^{(j)}>\\
&=\sum_{i=1}^np_i(X_i^{(j)})^2=S_j^2\\
\Rightarrow\Vert X^{(j)}\Vert&=S_j\quad\text{ecart-type}
\end{aligned}
$$

On mesure l'angle entre 2 variables $X^{(j)}$ et $X^{(k)}$ (centrees):

$$
\cos(\theta_{jk})=\frac{<X^{(j)}, X^{(k)}>}{\Vert X^{(j)}\Vert\Vert X^{(k)}\Vert}\quad\text{similarite cosinus}\\
\color{red}{\boxed{\cos(O_{jk}) = \frac{Cov(X^{(j)}, X^{(k)})}{S_jS_k} = p_{jk}}}
$$

<div class="alert alert-success" role="alert" markdown="1">
On retrouve le coefficient de correlation lineaire.
</div>

# Variables engendree par un tableau des donnees

A une variable $X^{(j)}$, on peut associer un axe de l'espace des individus $F$ et un vecteur de l'espace des variable et on peut egalement deduire $X^{(1)}, X^{(2)},\dots,X^{(j)}, \dots, X^{(p)}$ de nouvelles variables par combinaison lineaire.

Soit $\triangle$ un axe de $F$. $\triangle$ est engendre par un vecteur unitaire $a$ $$(a^T\underbrace{M}_{\text{metriques}}a=1)$$ et projetons les individus sur $\triangle$ (projection $M$-orthogonale)

![](https://i.imgur.com/ECi7TRA.png)

$$
\begin{aligned}
c_i=a^TMe_i&=e_i^TMa\\
&=<e_i,a>\quad\text{produit scalaire}
\end{aligned}
$$

La liste des coordonnees $c_i$ des individus sur $\triangle$ forme une nouvelle variable artificielle $C$

$$
C=\begin{pmatrix}C_1 \\ C_2 \\ \vdots \\ C_n\end{pmatrix}=X\underbrace{Ma}_{=u}=Xu
$$

On pose $u=Ma$: facteur

$$
\Rightarrow C=Xu=\sum_{j=1}^pu_jX^{(j)}
$$

<div class="alert alert-success" role="alert" markdown="1">
Donc la nouvelle variable $C$ est une combinaison lineaire des variables initiales.
</div>

L'ensemble des variables $C$ que l'on peut engendrer par combinaison lineaire des vecteurs colonnes de $X$ forme un sous-espace vectoriel (s.e.v.) de $E$ de dimension $\le p$

**Remarque**: Si $M=I\Rightarrow u=a$

On suppose que les variables sont centrees ($X=Y$) pour simplifier

<div class="alert alert-info" role="alert" markdown="1">
**Proposition**:

<div class="alert alert-danger" role="alert" markdown="1">

$$
V(C) = u^TVu\quad\text{variance de }C
$$

</div>
</div>

> **Demonstration:**
> $$
> \begin{aligned}
> V(C) &=c^TDc\\
> &= (Xu)^TDXu=u^T\underbrace{X^TDX}_{V}u\\
> &\Rightarrow V(C)u^TVu
> \end{aligned}
> $$

Le but de la methode est d'obtenir une representation approchee du nuage des $n$ individus dans un s.e.v de dimension faible.

<div class="alert alert-warning" role="alert" markdown="1">
Ceci s'effectue par projection
</div>

Il faut deformer le moins possible les distances en projection, ce qui signifie que l'inertie du nuage projete sur le s.e.v. $F_k$ soit maximale.

Soit $P$: la projetction $M$-orthogonale sur le s.e.v. $F_k$

$$
Pe_i=f_i\\
P^2=P\quad\text{et}\quad P^TM=MP
$$

![](https://i.imgur.com/cdisQKu.png)

Le nuage projete est associe au tableau: $XP^T$ car:

$$
\underbrace{f_i=Pe_i}_{\text{vecteur colonne}}\Rightarrow \underbrace{f_i^T=e_i^TP^T}_{\text{vecteur ligne}}
$$

On determine la matrice de var-covariance du tableau $XP^T$:

$$
(XP^T)^TD(XP^T)\quad\text{(les var sont centrees)}\\
=PX^TDXP^T\\
=\color{red}{\boxed{PVP^T}}
$$

On determine l'inertie du nuage projete: $Trace(PVP^TM)$

$$
\begin{aligned}
Tr(PVP^TM)&=Tr(PVMP)\\
&=Tr(VMP^2)\quad\text{car }Tr(AB)=Tr(BA)\\
&=Tr(VMP)
\end{aligned}
$$

<div class="alert alert-success" role="alert" markdown="1">
Donc l'inertie du nuage projete est $Trace(VMP)$
</div>

Le probleme est donc de trouver $P$: projection $M-$orthogonale de rang $k$ maximisant la trace de $VMP$, ce qui determinera $F_k$ ($\text{dim } F_k=k$)

## Theoreme

<div class="alert alert-info" role="alert" markdown="1">
**Theoreme**:
Soit $F_k$ un s.e.v. portant l'inertie maximale, alors le s.e.v. de dimension $k+1$ portant l'inertie maximale est la somme directe de $F_k$ et du s.e.v. de dimension $1$ $M$-orthognal a $F_k$ portant l'inertie maximale.

<div class="alert alert-danger" role="alert" markdown="1">

$$
F_{k+1}=F_k+\underbrace{b\mathbb R}_{\text{dimension }1}
$$

</div>

</div>

Pour obtenir $F_k$ on pourra proceder de proche en proche en cherchant d'abord le s.e.v. de dimension $1$ d'inertie maximale puis le s.e.v. de dimension $1$ $M-$orthogonal au premier d'inertie maximale.

On chercher la droite de $\mathbb R^2$ passant par $g$, maximisant l'inertie du nuage projete sur cette droite, On rappelle la projection $M$-orthogonale sur la droite dirigee par $a$:

$$
P=a(a^TMa)^{-1}a^TM
$$

Inertie du nuage projete sur cette droite:

$$
\begin{aligned}
Tr(VMP)&=Tr(VMa(a^TMa)^{-1}a^TM)\\
&= \frac{1}{a^TMa}Tr(VMaa^TM)\\
&= \frac{1}{a^TMa}Tr(a^TMVMa)\\
&=\frac{a^TMVMa}{a^TMa}
\end{aligned}\\
\frac{d}{da}(\frac{a^TMVMa}{a^TMa})=0\quad\text{(*)}
$$

## Rappel

<div class="alert alert-info" role="alert" markdown="1">

$$
\frac{d}{da}(\underbrace{a^TAa}_{\text{forme quadratique}})=Aa+A^Ta
$$

</div>

<div class="alert alert-danger" role="alert" markdown="1">
Si $A$ est symetrique:

$$
\frac{d}{da}(a^TAa)=2Aa
$$

</div>

$$
\begin{aligned}
\text{(*)} &\Rightarrow \frac{(a^Tma)2MVMa-(a^TMVMa)2MA}{(a^TMa)^2}=0\\
&\Rightarrow MVMa=\biggr(\frac{a^TMVMa}{a^TMa}\biggr)Ma\\
&\Rightarrow VMa=\biggr(\frac{a^TMVMa}{a^TMa}\biggr)a\\
&\Rightarrow \color{red}{\boxed{VMa=\lambda a}}\quad\text{avec }\lambda=\frac{a^TMVMa}{a^TMa}
\end{aligned}
$$

<div class="alert alert-success" role="alert" markdown="1">
Donc $a$ est un vecteur propre de $VM$ associe a $\lambda$ (valeur propre).
</div>

<div class="alert alert-warning" role="alert" markdown="1">
Il faut que $\lambda$ soit maximale.
</div>

Donc le s.e.v. $F_k$ de dimension $k$ est engendre par les $k$ vecteurs propres de $VM$ associes aux $k$ plus grandes valeurs propres.

<div class="alert alert-info" role="alert" markdown="1">
On appelle composantes principales:

<div class="alert alert-danger" role="alert" markdown="1">

$$
C^{(i)}=Yu^{(i)}\quad u^{(i)}\text{: facteur}
$$

</div>

</div>

Si les variables initiales sont centrees alors $C^{(i)}=Xu^{(i)}$

<div class="alert alert-danger" role="alert" markdown="1">

$$
V(C^{(i)}) = \lambda i\quad\forall i
$$

</div>

# Qualites des representations sur les plans principaux

Le but de l'A.C.P. etant d'obtenir une representation des individus dans un espace de dimension plus faible que $p$.

<div class="alert alert-info" role="alert" markdown="1">

Le critere le plus utilise est celui du pourcentage d'inertie totale expliquee on mesure la qualite de $F_k$ par:

$$
\frac{\lambda_1+\lambda_2+\dots+\lambda_k}{\lambda_1+\lambda_2+\dots+\lambda_p}
$$

</div>

<div class="alert alert-warning" role="alert" markdown="1">
Inertie totale:

$$
\lambda_1+\lambda_2+\dots+\lambda_p=I_{tot}
$$

</div>

Si par exemple $\frac{\lambda_1+\lambda_2}{I_{tot}}=90\%$, on concoit qu'une representation du nuage dans le plan des 2 premiers axes principaux sera tres satisfaisante.

# Correlations entre composantes principales et variables initiales

La methode la plus naturelle pour donner une signification a une composante principale $C^{(i)}$ est de la relier aux variables $X^{(j)}$ (variables intiales) en calculant les coefficients de correlation lineaire

$$
\rho(X^{(j)}, C^{(i)})
$$

et en s'interessant aux plus forts coefficients en valeur absolue

<div class="alert alert-danger" role="alert" markdown="1">

$$
\rho(X^{(j)}, C^{(i)})=\frac{Cov(X^{(j)}, C^{(i)})}{\sigma_{X^{(j)}}\sigma_{C^{(i)}}}
$$

</div>

$$
Cov(X^{(j)}, C^{(i)}) = <y^{(j)}, C^{(i)}>\quad\text{ou }y^{(j)}\text{ : var centree}
$$