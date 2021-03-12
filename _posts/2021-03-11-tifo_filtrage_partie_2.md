---
title:          "TIFO: Filtrage, partie 2"
date:           2021-03-11 15:00
categories:     [Image S8, TIFO]
tags:           [Image, TIFO, S8]
description: Filtrage, partie 2
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/rJHpPmYm_)

# Signal
<div class="alert alert-info" role="alert" markdown="1">
Representation Mathematiques d'un phenomene physique
</div>

Traitement du signal
- Elaboration, detection et interpretation des signaux

Classification des signaux
- Morphologique: continu/discret
- Spectrale: Bande de frequence BF/HF
- Energie: Energie finie/Puissance moyenne finie
- Typologie: deterministe/aleatoire
- Periodicite: non peridique/$x(t)=x(t+T)$

## Energie
- Energie $w_x$ d'un signal $x$

$$
W_x=\int_{-\infty}^{+\infty}\vert x(t)\vert^2dt
$$

- Les signaux a energie finie verifient la condition:

$$
W_x=\int_{-\infty}^{+\infty}\vert x(t)\vert^2\lt+\infty
$$

- Les signaux a support borne (cad duree limitee) sont a ernegie finie

## Puissance
- Puissance moyenne $P$ du signal $x$

$$
P_x=\lim_{T\to+\infty}\frac{1}{T}\int_{-\frac{T}{2}}^{\frac{T}{2}} \vert x(t\vert^2dt)
$$

- Energie finie $\Rightarrow$ puissance moyenne nulle

$$
W_x\lt+\infty\Rightarrow P_x=0
$$

- Puissance moyenne finie $\Rightarrow$ energie infinie

$$
0\lt P_x\lt+\infty\Rightarrow W_x\to+\infty
$$

> Ex: les signaux periodiques

## Signaux classiques
### Porte

$$
\Pi_{\frac{T}{2}}=
\begin{cases}
    1 &\text{si } t\in[-\frac{T}{2};\frac{T}{2}]\\
    0 &\text{ailleurs}
\end{cases}
$$

![](https://i.imgur.com/4DeYK0u.png)


### Echelon d'Heavyside

$$
u(t)=
\begin{cases}
    0 &\text{si } t\lt0\\
    1 &\text{si } t\ge0
\end{cases}
$$

![](https://i.imgur.com/dbT1FaV.png)


### Signe

$$
sgn(t) =
\begin{cases}
    -1 &\text{si } t\lt0\\
    0 &\text{si } t=0\\
    1 &\text{si } t\gt0
\end{cases}
$$

![](https://i.imgur.com/DlsoWDy.png)


### Triangulaire

$$
\triangle_T(t)=
\begin{cases}
    \frac{1-\vert T\vert}{T} &\text{si } \vert t\vert T\\
    0 &\text{ailleurs}
\end{cases}
$$

![](https://i.imgur.com/XjAwXKo.png)


### Gaussienne

$$
g(t) = \frac{1}{\delta\sqrt{2\pi}}e^{-\frac{t^2}{2\delta^2}}
$$

![](https://i.imgur.com/W2jobhi.png)

### Sinus cardinal

$$
sinc(t) = \frac{sin(t)}{t}
$$

![](https://i.imgur.com/r7iemnU.png)

# Series de Fourier
- On consider les fonctions $g_n(t)$

$$
g_n(t) = e^{2j\pi\frac{nt}{T}}
$$

- Que vaut

$$
<g_n(t),g_m(t)> = \frac{1}{T}\int_Tg_n(t)g_m^*(t)dt=
\begin{cases}
    0 &\text{si } n\neq m\\
    1 &\text{si } n= m
\end{cases}
$$

avec $g_m^*$ le conjugue dans les complexe

- Soit $f(t)$ periodique de periode $T(T\gt 0)$. Un signal 1D periodique peut etre vu comme une somme de sinusoides

$$
f(t) = \sum_{n=-\infty}^{+\infty}C_ng_n(t)
$$

*Comment trouver $C_i$ ?*

$$
\begin{aligned}
\frac{1}{T}\int f(t)g_i^*(t)dt &= \frac{1}{T}\int(\sum C_ng_n(t))\int g_i^*(t)dt\\
&= \frac{1}{T}\int(...+C_{i-1}g_{i-1}(t)+C_{i}g_{i}(t)+C_{i+1}g_{i+1}(t)+...)g_i^*(t)dt\\
&= \frac{1}{T}\int(...+C_{i-1}g_{i-1}(t)g_i^*(t)+C_{i}g_{i}(t)g_i^*(t)+C_{i+1}g_{i+1}(t)g_i^*(t)+...)dt\\
&=...+\frac{1}{T}\int C_{i-1}g_{i-1}(t)g_i^*(t)dt + \frac{1}{T}\int C_{i}g_{i}(t)g_i^*(t) + \\ &\frac{1}{T}\int C_{i-1}g_{i-1}(t)g_i^*(t)dt+...\\
&=...+C_{i-1}\underbrace{\frac{1}{T}\int g_{i-1}(t)g_i^*(t)}_{=0 \text{ car } i-1\neq i}+ C_i\underbrace{\frac{1}{T}\int g_{i}(t)g_i^*(t)}_{=1} + C_{i+1}\underbrace{\frac{1}{T}\int g_{i+1}(t)g_i^*(t)}_{=0 \text{ car } i+1\neq i}\\
&= C_i
\end{aligned}
$$

## Harmoniques
$C_n$: harmoniques

![](https://i.imgur.com/jMA4bzu.png)
> On les sommes pour obtenir la sinusoides resultat

- $C_0$: frequence continue
- $C_1$: frequence fondamentale
- ...
- $C_n$: $n^{ieme}$ harmonique
- f reel $\Rightarrow$ $C_n=C_{-n}^*(f(t)=f^*(t))$

## Frequences
- Basses frequences
    - Lentes variations
    - Zones presque uniformes
- Hautes frequences
    - Variations rapides
    - Contours/coins

Se retrouve dans les images
![](https://i.imgur.com/lyMAUYT.png)
> Quand des details apparaissent, on monte dans les frequences

# Series et transformees de Fourier
## Spectre
- D'amplitude: $\vert C_n\vert$
- De phase $Arg(C_n)=arctg(-\frac{b_n}{a_n})$
- De puissance $\vert C_n\vert^2$
- $f(t)$ reel $\Rightarrow$ spectre d'amplitude symetrique

<div class="alert alert-danger" role="alert" markdown="1">
**Relation de PARSEVAL**: Il y a conservation de la puissance de la representation temporelle a la representation frequentielle.
</div>
On ne perde pas d'information lorsqu'on passe de l'un a l'autre.

## Signaux
On considere jusqu'a present des signaux periodiques
- On peut generaliser en prenant $T\to+\infty$

On defini $TF\{x(t)\}$

$$
X(f) = \int_{-\infty}^{+\infty}x(t)e^{-2j\pi ft}dt
$$

On defini $TF^{-1}\{x(t)\}$

$$
x(t)=\int_{-\infty}^{+\infty}X(f)e^{+2j\pi ft}df
$$

<div class="alert alert-warning" role="alert" markdown="1">
Toutes les infos contenues dans le signal sont contenues dans le spectre
</div>

## Transformee usuelles

### Porte
Transformee de Fourier: Sinus cardinal
![](https://i.imgur.com/KBqeeMQ.png)


### Constante
Transformee de Fourier: Fondamentale
![](https://i.imgur.com/t8zxwfc.png)


### Peigne de Dirac
Transformee de Fourier: un autre Peigne de Dirac
![](https://i.imgur.com/V2ihqFY.png)

## Existence de la transformee de $f(t)$
- $f(t)$ bornee
- Integrale de $f(t)dt$ existe
- Les discontinuires de $f(t)$ sont en nombre limite

<div class="alert alert-warning" role="alert" markdown="1">
On s'autorisera systematiquement a faire la transformee de Fourier de l'image
</div>

## Proprietes
- Linearite

$$
Kf(t)+g(t) \Leftrightarrow KF(t)+G(t) \text{ } K\text{ complexe}
$$

- Similitude: Une dilatation dans le domaine temporel correspond a une contraction dans le domaine frequentiel
    - $f(at)\Leftrightarrow\frac{1}{\vert a\vert}F(\frac{f}{a})$ (a reel)
- Derivee:
    - $\frac{dx(t)}{dt}\Leftrightarrow 2i\Pi fX(f)$
    - $\frac{dx(f)}{df}\Leftrightarrow -2i\Pi fX(t)$

Dans notre cas:
- Signal borne et echantillone

Soit le pic de Dirac $\delta(t)$:
![](https://i.imgur.com/GiSFjFy.png)

Soit le pic de Dirac $\delta(t_0)$:
![](https://i.imgur.com/J8yMJHR.png)

$$
\delta(t_0)=\delta(t-t_0)\\
f(t)\delta(t_0)=f(t_0)
$$

![](https://i.imgur.com/4UbgUri.png)![](https://i.imgur.com/P8TBvFd.png)

Soit le peigne de Dirac $Ш(t)$:

$$
\sum_{n=-\infty}^{+\infty}\delta(t-nT)
$$

![](https://i.imgur.com/HmM6mE8.png)

$f(t).Ш(t_0)=$
![](https://i.imgur.com/jLuGj0X.png)

![](https://i.imgur.com/9F7Lk0H.png)

<div class="alert alert-danger" role="alert" markdown="1">
Une fonction echantillonee, c'est une fonction multipliee par un peigne de Dirac.
</div>

# Transformee de Fourier
Dans notre cas:
- Signal discret (echnatillonne) + support borne
    - Transformee de Fourier Discrete

$$
\begin{aligned}
&X(f)=\int_{-\infty}^{+\infty}x(t)e^{-2j\pi ft}dt &X(f)=\sum_{t=-\infty}^{+\infty}x(t)e^{-2j\pi ft}
\end{aligned}
$$
$$
X(l)=\sum_{k=0}^{N-1}x(kT_e)e^{-2j\pi lf_ekT_e}
$$

<div class="alert alert-success" role="alert" markdown="1">
\begin{aligned}
&X(l)=\sum_{k=0}^{N-1}x(t)e^{\frac{-2j\pi}{N} kl} &X(k)=\sum_{k=0}^{N-1}x(t)e^{\frac{2j\pi}{N} lk} 
\end{aligned}
</div>

## Notes
$F_e$ frequence d'echantillonnage
- $X(0)\to-2F_e(/0)$
- $X(N-1)\to +2F_e(/+4F_e)$
- Pas en frequence: $F_e/N$

## Calcul rapide de la TFD
Fast Fourier Transform (1965 - Cooley et Tukey

$$
\begin{aligned}
X(l)&=\sum_{k=0}^{N-1}x(k)e^{-\frac{2j\pi kl}{N}}\\
&= \sum_{k=0}^{\frac{N}{2}-1}x(2k)e^{-\frac{2j\pi 2kl}{N}} + \sum_{k=0}^{\frac{N}{2}-1}x(2k+1)e^{-\frac{2j\pi 2(k+1)l}{N}}\\
&= \sum_{k=0}^{\frac{N}{2}-1}x(2k)e^{-\frac{2j\pi 2kl}{N}} + e^{-\frac{2j\pi l}{N}}\sum_{k=0}^{\frac{N}{2}-1}x(2k+1)e^{-\frac{2j\pi2kl}{N}}
\end{aligned}
$$

<div class="alert alert-info" role="alert" markdown="1">
Pour calculer la TFD sur un signal de taille $N$, on calcul la transformee de Fourier sur les coeeficients pairs $(\frac{N}{2})$ et la transformee de Fourier sur les coefficients impairs $(\frac{N}{2})$... et recursivement
</div>

## Dans notre cas (Image)
- Signal 2D: TF2D (Transformee de Fourier a 2 dimensions)

## Visualisation du spectre:
On peut aller de $-2F_e$ a $2F_e$ 
![](https://i.imgur.com/63xdsEb.png)
Representation pas pratique car le max d'information se retrouve dispatche aux differents angles.


On interverti les cadrants. Les basses frequences se retrouvent au centre
![](https://i.imgur.com/0qcdsyb.png)

![](https://i.imgur.com/79Z4ndK.png)

Resultat:
![](https://i.imgur.com/23BGjDV.png)

# La convolution
![](https://i.imgur.com/R6uOQZj.png)

*Reponse impulsionnelle ?*
Reponse a une impulsion $\delta(t)$, cad envoyer un pic de Dirac unitqire et recupere la reponse impulsionnelle du filtre h(t).

<div class="alert alert-danger" role="alert" markdown="1">
Cela caracterise le filtre.
</div>
On peut en deduire pour n'importe quel signal la sortie du filtre.

La reponse du filtre est donnee par un produit de convolution

$$
y(t)=x(t)\times h(t)=\int_{-\infty}^{+\infty}x(u)h(t-u)du
$$

## Reponse impulsionnelle
![](https://i.imgur.com/xgPkFWO.png)

*Si le signal est une serie d'impulsions ?*
1. On calcule la reponse du filtre a la 1$^{ere}$ impulsion
2. On calcule la reponse de la seconde impulsion
3. De meme pour la 3$^{eme}$

![](https://i.imgur.com/Dwo12RK.png)

![](https://i.imgur.com/vlHrm10.png)

![](https://i.imgur.com/1MdYSYj.png)

<div class="alert alert-success" role="alert" markdown="1">
Par le principe de supperposition, les reponses s'additionnent
![](https://i.imgur.com/e0tNhBA.png)

![](https://i.imgur.com/gwFtNAg.png)

</div>
C'est ce qu'on fait lors du produit de convolution.

## Proprietes
- Commutative: $f(t)* g(t)=g(t)* f(t)$
- Distributive: $(x(t)+y(t))*g(t) = x(t)* g(t)+y(t)* g(t)$
- Associative: $(x(t)* y(t))* z(t)=x(t)* (y(t)* z(t))$

## Theoreme de Plancherel
<div class="alert alert-danger" role="alert" markdown="1">

|Temps|Frequences|
|-|-|
|Convolution $*$|Multiplication $.$|
|Multiplication $.$|Convolution $*$|

</div>

## Autre propriete
$$
f'*g=f*g'=(f*g)'
$$

# Consequences du lien convolution $\leftrightarrow$ multiplication
- Spectre d'un signal echantillonee
- Revisite du filtrage
    - Passe haut
    - Passe bas
    - Passe Bande
    - Rejecteur
- Deconvolution

Autres consequences:
- DoG - Difference de gaussiennes
- LoG - Laplacien d'une gaussienne

Spectre d'un signal echantillonne:
$f(t)Ш(t_0)=$

![](https://i.imgur.com/J86iwi8.png)

Dans le domaine frequentiel:
![](https://i.imgur.com/PfB1Cba.png)
> La TF du peigne de Dirac est un autre peigne de Dirac plus espace

<div class="alert alert-warning" role="alert" markdown="1">
Le signal se repete a l'infini, on n'a besoin de connaitre qu'un espace
</div>

## Revisite du filtrage
Passe haut / Passe Bas/ Passe Bande / Rejecteur

![](https://i.imgur.com/cR8Un02.png)
1. On a un signal qu'on veut filtrer pour enlever le bruit
2. On passe en frequenciel et on a le spectre du signal
    - Les hautes frequences sont du bruit
3. On defini un signal pour les enlever
    - 1 sur toutes les basses frequences
    - 0 partout ailleurs
    - On multiplie les 2
4. On obtient le spectre supprime de toutes les bases frequences
5. On fait l'inverse de la TF et on obtient le signal sans les hautes frequences

*En pratique, est-ce qu'on fait tout ca ?*
Non.

![](https://i.imgur.com/0QGvViy.png)
On peut faire l'inverse
1. Prendre le filtre defini
2. Faire l'inverse et de le passer en temporel
    - en temporel, la porte devient un sinus cardinal
3. Convoluer le filtre avec le signal
4. On obtient notre signal filtre

## Autre consequence
Convolution
- $f'=f*h\Rightarrow F\times H = F'$

Deconvolution
- $\frac{F'}{H} = F\to$ domaine temporel
    - Tres difficile si on ne connait pas le filtre initial
    - Probleme des 0 (ou des valeurs tres petites dans $H$)

> Si on floute le visage de quelqu'un pour anonymat avec un filtre gaussien, on peut arriver a deconvoluer et retrouver le visage d'origine (tres difficile en pratique)
> 
> Il faudrait mettre un gros carre noir et non flouter le visage

Detection de bord
- ($f*$ gauss)'$\to f*$guass' (la derivee de la gaussien est connue formellement)
    - Realise a la fois le lissage et la derivee

LoG
- Laplacient d'une gaussienne

Dog
- Difference de gaussienne

# Filtrage
- Passe Bas
    - Description
        - Coef central superieur ou egal aux autres
        - Autres coefs positifs
    - Effet
        - Pixel central devient une moyenne ponderee des voisins
        - Les regions homogenes sont peut changees
        - Les frontieres sont etalees
        - Reduit le bruit
- Passe Haut
    - Description
        - Coef central positif et eleve
        - Autres coefs petits, negatifs ou nuls
        - La somme des coefficients est nulle
    - Effet
        - Zones homogenes: perte de la notion d'intensite
        - Frontieres sont renforcees

# Proprietes de la TF2D
![](https://i.imgur.com/WT0mY6z.png)

![](https://i.imgur.com/h2i8RNf.png)
Le module de l'image ne change pas

![](https://i.imgur.com/6XHKZct.png)
Le module change mais la phase est invariante a la rotation

![](https://i.imgur.com/RwbJISb.png)

![](https://i.imgur.com/fVTnmCj.png)

## Impact du flou
<div class="alert alert-info" role="alert" markdown="1">
Cela veut dire que les hautes frequences sont reduites/degradees.
</div>

![](https://i.imgur.com/JHF9Bhd.png)
![](https://i.imgur.com/78ud8tB.png)

![](https://i.imgur.com/P4hSQdw.png)
![](https://i.imgur.com/xplxG7F.png)

Si on bouge, on a un flou directionnel, cad on a preserve l'information dans un sens et perdu dans l'autre.

![](https://i.imgur.com/MgRSpEb.png)

![](https://i.imgur.com/NoeeQ5k.png)

## Skew estimation
*Application:*
On a un document qui passe dans un scanner, il n'est pas forcement droit et on veut corriger l'orientation.

On voit la rotation dans le spectre et on refait une transformee de Fourier.

![](https://i.imgur.com/Q5bn6sZ.png)

On peut estimer l'orientation du fichier d'origine.

# Autres transformations
- Short Term Fourier Transform
- Discret Cosinus Transform
- Ondelettes
- Radon
- Wigner
- Hilbert
- ...

## Transformee en cosinus discrete
On fait la transformee de Fourier sur une base de sinusoide reel (utilise en JPEG)

Probleme
- definiton varie d'un ouvrage a un autre
- Pour le JPEG, l'encodeur et le decodeur peuvent utiliser une transformee differente

## Short Term Fourier Transform
- probleme:
    - FT: soit le temps, soit la frequence
- Solution: ne considerer que des petits intervalles

$$
X(f,t')=\int_{-\infty}^{+\infty}x(t)w^c(t-t')e^{-2j\pi t}dt
$$

- Impact de la taille de w
    - W etroit $\Rightarrow$ localisation temporelle correcte mais mauvaise resolution frequentielle
    - W large $\Rightarrow$ localisation temporelle imprecise mais bonne resolution frequentielle

## Transformee en ondelettes
- Avantages:
    - FT: soit le temps, soit la frequence
    - STFT: diffculte de regler la taille de w et taille fixee une fois pour toutes
    - Transformee en ondelette:
        - Representation temps-frequence
            - la frequence avec sa position spatiale
        - Adaptation de la resolution en fonction de la frequence
            - Basses frequence $\to$ Privilegie la resolution frequentielle
            - Hautes frequence $\to$ Privilegie la resolution temporelle
        - analyse des signaux non stationnaires 

Definition:

$$
\Psi_x^\psi(\tau,s)=\frac{1}{\sqrt{\vert s\vert}}\int x(t)\psi^c\biggr(\frac{t-\tau}{s}\biggr)dt\\
\Psi_x^\psi(\tau,s)=\int x(t\psi_{\tau, s}^c)(t)dt\\
\psi_{(\tau,s)}=\frac{1}{\sqrt{\vert s\vert}}\psi\biggr(\frac{t-\tau}{s}\biggr)
$$

### Exemples
- Haar
- Mexican Hat
- Morlet

![](https://i.imgur.com/ca1R9HU.png)

## Usage
- Compression
- Filtrage
- Approximation
- ...