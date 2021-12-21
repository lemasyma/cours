---
title:          "ASE1 : Typical exam"
date:           2020-06-02 15:00
categories:     [S6, tronc commun, ASE1]
tags:           [S6, ASE1, tronc commun]
math: true
---

Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/Sks-MFbeP)

# Format

Fichier excel deja pret ou on devra mettre nom + prenom + uid. Format CSV fr, separation des champs avec ,

# Jouons avec R

```R
UID<-20254 #UID de l'etudiant
X<-runif(1000) #Loi uniforme pour une variable X et on en prend mille
plot(X) #Affiche X
Z<-1:1000 #Vecteur Z
plot(Z)
alpha<-UID/23000
K<-UID/7500
```

```R
alpha
```
```
0.8806087
```
```R
K
```
```
2.700533
```
Ces nombres sont differents pour tout le monde
```R
V<-K*X^alpha
W<-K*Z^alpha

sort(V) #Loi uniforme de V
sort(W) #Loi uniforme de W
```
Le vecteur W a ete construit par vous, il depend de votre numero. Vous devez etre capable de decrire W.

```R
boxplot(W) #Ne sera pa demande au partiel
```
![](https://i.imgur.com/VqyYL8S.png)
```R
summary(W) #Decrit des valeurs utiles
```
```
Min    1st Qu.    Median    Mean    3rd Qu.    Max
2.7    350.1      643.5    630.1    919.1      1193.8 
```
```R
sd(W) #Ecart type
var(W) #Variance
```
On aura la commande dans l'enonce. 
```R
cor(V, W) #Correlation entre V et W
```

```R
K<-2.5
alpha<-2.1
W<-K*Y^alpha
summary(W)
```
Jouez avec `mean`, `sd`, `boxplot`, `summary`, `var`, `cov`, `cor`.

```R
X<-1:100
Y<-X^2
plot(X, Y)
```
![](https://i.imgur.com/Y9AUK1r.png)
Le coefficient de correlation de X et Y au pif ?
Plutot proche de 1 car la courbe ressemble a une droite. :snail: 

```R
cor(X, Y)
```
```
0.96
```

# Intervalle de confiance
On va s'interesser au poids d'un nouveau-ne. :snail: 
* On en a pese 49
* On a trouve une moyenne de 3.6 Kgs

Je sais que l'ecart-type est de 0.5 Kg. Je souhaite avoir un intervalle de confiance a $95\%$ du poids moyen.

Derniere hypothese: le poids suit une loi normale.

Il y a 2 facons de faire:
* Rappeler le raisonnement
* Apprendre la formule du cours

## Rappelons le raisonnement
En general "Observation = moyen + ecart = moyenne + k * ecart type" sauf qu'on doit faire une deduction sur la moyenne.

Estimation de moyenne de type moyenne observee +- k * ecart type. Quand on connait l'ecart type K depend de la distribution de la loi normale.

```R
x.barre<-3.6
sigma<-0.5

n<-49
```

## Formule du cours
Un intervalle de confiance a $95\%$, $\alpha = 5\%$, $\frac{\alpha}{2} = 2.5\%$ et $1-\frac{\alpha}{2} = 0.975$

On utilise `qnorm`
```R
u<-qnorm(0.975)
u
```
```
1.959964
```
```R
mu.inferieur<-x.barre-u*sigma0/sqrt(n) #Formule du cours
mu.superieur<-x.barre+u*sigma0/sqrt(n)
```
<div class="alert alert-success" role="alert" markdown="1">
L'intervalle de confiance a $95\%$ est $[3.46, 3.74]$.
</div>

On a mesure un ecart type de 0.53 Kgs. Quel est l'intervalle de confiance?
On a mesure une moyenne de 3.6 Kgs et un ecart type de 0,53 Kgs sur 49 bebes.

```R
v<-qt(0.975, 49-1)
v
```
```
2.010635
```
```
ecart<-v*0.53/sqrt(n-1)
```
```R
mu.inferieur<-x.barre-ecart
mu.superieur<-x.barre+ecart
```
```
3.44
3.75
```

# Patients malades
Pour une maladie donnee, un traitement gueri $90\%$ des patients.
J'ai fait un test avec 1000 patients et 850 sont gueris au bout de 2 semaines. :snail: 

J'accepte le 90% sur cette base?
Un test de chi2, dans le cours.
![](https://i.imgur.com/lECLYxw.png)

Ici : k=2 classes
1. patients gueris, p1 = 0.9
2. patients non gueris, p2 = 0.1

![](https://i.imgur.com/WqHFb5t.png)
![](https://i.imgur.com/mhZGk33.png)

```R
n<-1000
N1<-850
N2<-150
p1<-0.9
p2<-0.1
```
```R
Z<-(N1-n*p1)^2/(n*p1) + (N2-n*p2)/(n*p2)
Z
```
```
27.77778
```
![](https://i.imgur.com/c8NKL3F.png)
```R
qchisq(0.95, 1)
```
```
3.84
```
```R
qchisq(0.99, 1)
```
```
6.63
```
La valeur de Z est trop grande, les ecarts de Z sont trop grands. En principe Z doit rester petit, on va refuser l'hypothese de guerison a $90\%$. :snail: 

H0: la proba de guerison est de $90\%$, la proba de non guerison est $10\%$.

# Regression lineaire
```R
plot(X, Y, col="blue")
```
![](https://i.imgur.com/bbcPJuc.png)

<div class="alert alert-danger" role="alert" markdown="1">
On veut appliquer ces formules
![](https://i.imgur.com/6rSnFG6.png)
</div>

```R
mX<-mean(X)
mY<-mean(Y)

sX<-sd(X)
sY<-sd(Y)

rho<-cor(X, Y)
```
```R
beta<-rho*sY/sX
alpha<-mY-beta*mX
```
```R
PREV<-beta*X+alpha
```
```R
points(X,PREV,col="red",pch=19,cex=0.8)
```
![](https://i.imgur.com/EG0pguK.png)
```R
ECARTS<-Y-PREV
```
```R
var(PREV)
var(ECARTS)
```
```R
var(PREV) + var(ECARTS)
```
```
2174766
```
:snail: 