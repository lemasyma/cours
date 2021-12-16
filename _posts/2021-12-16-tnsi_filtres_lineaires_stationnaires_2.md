---
title:          "TNSI: Filtres lineaires stationnaires - 2"
date:           2021-12-15 14:00
categories:     [Image S9, TNSI]
tags:           [Image, S9, TNSI]
math: true
---

Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/Sk3z8p4tF)

# Filtres lineaires

1. Linearite $$\begin{aligned}\mathcal H\{ax_1[n]+bx_2[n]\} &= a\mathcal H \{x_1[n]\}+b\mathcal H\{x_2[n]\} \\ &= ay_1[n] + by_2[n]\end{aligned}$$
2. Stationnarite $$y[n]=\mathcal \{x[n]\}\Leftrightarrow \mathcal H\{x[n-n_0]\}=y[n-n_0]$$

$$
x[n] = \sum_{p=-\infty}^{+\infty}x[p]\delta[n-p]\\
\mathcal H\{x[n]\} = \sum_{p=-\infty}^{+\infty}x[p]\mathcal \{\delta[n-p]\}\\
\mathcal H\{x[n]\} = \sum_{p=-\infty}^{+\infty}x[p]h[n-p]=x \ast h[n]
$$

<div class="alert alert-danger" role="alert" markdown="1">
$h[n]$ est la **reponse impulsionnelle discrete**
</div>

3.La causalite

$$
\mathcal H\{x[n]\} = \sum_{p=-\infty}^{+\infty}h[p]x[n-p]\to h[p]=0\text{ pour } p\lt0
$$

4.Stabilite

$$
\vert\mathcal H\{x[n]\}\vert\le \sum_{p=-\infty}^{+\infty}\vert h[p]\vert \vert x[n-p]\vert \le \sup_{n\in\mathbb Z}\vert x[n]\vert\sum_{p=-\infty}^{+\infty}\vert h[p]\vert
$$

<div class="alert alert-success" role="alert" markdown="1">
On parle de ***BIBO stability***: *Bounded Input Bounded output*
</div>

- Filtres a reponse impulsionnelle finie (RIF)
- Filtres a reponse impulsionnelle infinie (RII)
- Filtre causal
- Filtre non causal

La TF joue un role fondamental dans l'analyse des operateurs stationnaires

$$
\hat y (\omega)=\hat h(x)\hat x(\omega)\quad \omega=2i\pi f\quad \omega\in[-\pi, \pi]
$$

<div class="alert alert-danger" role="alert" markdown="1">
$\hat h(\omega)$ est la **fonction de transfert** ou **reponse frequentielle du filtre**
</div>

2 effets:
- *amplitude*: amplification $(\vert \hat h(\omega)\vert\lt 1)$
- *phase*: decalage et deformation de $x$

### Exemple

Soit $x[n]\to x_b[n]=x[n]+b[n]$

Filtre moyenneur $$h_{\Pi}[n]=\begin{cases}1 \\ 0\end{cases}$$ pour $\Pi$ echantillons.

$$
\hat h(\omega)=\frac{1}{\Pi}\frac{\sin(\frac{\omega}{2}\Pi)}{\sin(\frac{\omega}{2})}e^{-\frac{\omega}{2}(\Pi-1)}
$$

Un filtre causal va etre centre en $0$:

![](https://i.imgur.com/mEo3U9a.png)

Un filtre non causal ne l'est pas:

![](https://i.imgur.com/43CissZ.png)

On a une suite d'echantillons:

![](https://i.imgur.com/CwKwmae.png)

Si on applique un filtre causal, on va *forcement* avoir un decalage dans le temps

# Types de filtres

- Filtres a phase nulle
- Filtres a phase lineaire (implique un decalage en temps)
- Filtre a phase non lineaire

$$
\hat h(\omega) = e^{-i\omega a}\\
\hat y (\omega)=\hat h(\omega)\hat x(\omega) = e^{-i\omega a}\hat x(\omega)\\
y[n] = x[n-a]
$$

## Passe-bas ideal

![](https://i.imgur.com/8LsH4g0.png)

$$
\hat h(\omega) = \begin{aligned}
1 &\forall \vert\omega\vert \le w_c\\
0
\end{aligned}\\
\hat h (\omega)=\Pi(\frac{\omega}{2\omega_c})\quad\text{ou }\Pi(x)=\begin{cases}
1&\vert x\vert\le\frac{1}{2}\\
0
\end{cases}
$$

## Reponse impulsionnelle d'un filtre passe-bas ideal

<div class="alert alert-danger" role="alert" markdown="1">
TFTd inverse

$$
\begin{aligned}
h[n] &= \frac{1}{2\pi}\int_{-\pi}^{pi}\hat h(\omega)e^{i\omega n}d\omega\\
&= \frac{1}{2\pi}\int_{-\omega_c}^{\omega}e^{i\omega n}d\omega\\
&= \frac{1}{2\pi}\frac{1}{in}(e^{i\omega_cn}-e^{-i\omega_cn})=\frac{1}{\pi n}\sin(\omega_cn)\\
\end{aligned}
$$

</div>

Quand on applique une fonction porte en frequence, ca revient a faire une convolution en temps de:

![](https://i.imgur.com/DMKGV7Y.png)

![](https://i.imgur.com/mvJTBeB.png)

En augmentant le nombre d'echantillons:

![](https://i.imgur.com/L0eSHmm.png)

<div class="alert alert-warning" role="alert" markdown="1">
On introduit des artefacts numeriques dus aux approximations mathematiques
</div>

## Construire un filtre

<div class="alert alert-info" role="alert" markdown="1">
**Lobe principal**
Pente de coupure (transition abrupte de niveau) TODO
</div>

## Equations recurrentes a coefficients constants

On souhaite resoudre une equation de forme:

$$
\sum_{k=0}^{N-1}a_ky[n-k]=\sum_{k=0}^{\Pi-1}b_kx[n-k]
$$

- $a_k$ equivalent a construire un filtre en passant par l'espace de Fourier
- $b_k$ controle l'entree pour eviter les effets indesirables

*Comment calculer ces coefficients ?*

*Et la fonction de trasnfert de ce filtre ?*
> Fourier ?

$$
\frac{\hat y(\omega)}{\hat x(\omega)}=\frac{\sum_{k=0}^{M-1}b_ke^{-ik\omega}}{\sum_{k=0}^{N-1}a_ke^{-ik\omega}}=\hat h(\omega)
$$

## Transformee en Z

La TZ d'un signal discret $x[n]$:

$$
X(z) = \sum_{n=-\infty}^{+\infty}x[n]\underbrace{z^{-n}}_{\color{red}{\mathbb C}}\quad\text{avec } R_1\le \vert z\vert\le R_2
$$

La TFtd avec $z=e^{i\omega f}$

<div class="alert alert-success" role="alert" markdown="1">
La TFtd est egale a la TZ sur le cercle unite
</div>

> Pour nos filtres, il faut donc que le cercle unite appartienne au domaine de convergence

Si on reprend l'equation de depart, sa TZ:

$$
Y(z)\sum_{k=0}^{N-1}a_kz^{-k}=X(z)\sum_{k=0}^{M-1}b_kz^{-k}\\
Y(z)=H(z)X(z)\\
H(z)=\frac{\sum_{k=0}^{M-1}b_kz^{-k}}{\sum_{k=0}^{N-1}a_kz^{-k}}=\color{red}{c\frac{\prod_{k=0}^{M-1}(1-Z_kZ^{-1})}{\prod_{k=0}^{N-1}(1-Z_kZ^{-1})}}
$$

![](https://i.imgur.com/l4l261U.png)

roni

![](https://i.imgur.com/jibTDfT.png)

qp3ihpr

![](https://i.imgur.com/2cIrVRx.png)

elkwfnwlef

$$
h[n] = \frac{1}{N}(𝟙_{\{0,\dots,N-1\}})\\
\downarrow\\
H(z) = \frac{1}{N}(\sum_{n=0}^{N-1}z^{-n})\to\frac{1-z^{-N}}{1-z^{-1}}\\
H(\omega) = \frac{1-e^{-i\omega N}}{1-e^{-i\omega}}
$$

## Specification pour la synthese de filtre

1. Choix d'une bande passante et d'une bande stoppante
2. Forme de la phase
3. Limite de calcul $\to$ le degre de la fonction de tranfert (cad $M$ et $N$)

![](https://i.imgur.com/ziVM2gU.png)

- $\omega_p$: frequence de coupure de la bande passante
- $\omega_s$: frequence de coupure de la bande coupee
- $\delta_p$: ondulation en bande passante
- $\delta_c$: ondulation en bande coupee
- $(\omega_p + \omega_s) / 2$: frequence de coupure du filtre

## Filtres RII vs RIF

### Filtres RII

|               Avantages                |       Desavantage       |
|:--------------------------------------:|:-----------------------:|
|       Calcul efficace (recursif)       |  Probleme de stabilite  |
| Facile d'obtenir une attenuation forte | Difficulte a construire |
|            Adapte a l'audio            |   Phase non lineaire    |

$$
H(z) = \frac{\Sigma b_kz^{-k}}{\Sigma a_kz^{-k}}
$$

### Filtre RIF

|                         Avantages                         |          Desavantage           |
|:---------------------------------------------------------:|:------------------------------:|
|                      Toujours stable                      |     Probleme de stabilite      |
| Synthese optimale possible (algorithme de Parks McCellan) |    Difficulte a construire     |
|                  Phase lineaire possible                  | Cout computationnel plus eleve |

$$
H(z) = \Sigma b_kz^{-k}
$$

## Filtres RII

Filtres couramment utilises sont issus du monde analogique

### Exercice

1. Comparer les filtres de:
    - Butterworth, Chebyshev I, Chebyshev II et Elliptic
    - `scipy.signal.iirfilter`
    - `scipy.signal.freqs` $\to$ tracer entre $[-1, 1]$
    - Interpreter
2. Suppression composante directe $\to$ DC biais ($\to$ signal non centre)
    - *Quel filtre frequentiel ?*
        - Supprimer $\omega = 0$
    - $\color{red}{\text{A faire a l'aide de la TZ}}$

$$
\color{green}{H(z) = c\frac{\Pi(1-\overbrace{z_n}^{\color{red}{\text{zeros}}}z^{-1})}{\Pi(1-\underbrace{P_n}_{\color{red}{\text{pole}}}z^{-1})}}
$$

On veut supprimer la frequence a $0$

![](https://i.imgur.com/iqKk2L1.png)

$$
H(z)=c\frac{\Pi(1-z_nz^{-1})}{\Pi(1-P_nz^{-1})}\quad\text{on s'en fiche du denominateur}\\
\color{red}{\Pi(1-z_n\underbrace{z^{-1}}_{=1})=0\to (1-z_n\times 1) = 0 \\ z_n=1}\\
H(z) = \overbrace{1-z^{-1}}^{z^0}\\
H(\omega) = 1-e^{-i\omega n}\to y[n] = x[n - 0] - x[n-1]\\
H(z) = \frac{1-z^{-1}}{1-\alpha z^{-1}}\to y[n]-\alpha y[n-1]=x[n]-x[n-1] \quad \alpha\in[0;1]\\
h(\omega) = \frac{1-e^{-i\omega}}{1-\alpha e^{-i\omega}}\to y[n]=x[n]-x[n-1]+\alpha y[n-1]
$$

## Filtres RIF

Construction optimal par **minimax**
Algorithme de Parks % McClellan / algorithme de Remez
- Phase lineaire
- Oscillation en bande passante et stoppante

L'algorithme consiste a minimiser l'oscillation maximale

La phase lineaire est obtenue a partir d'une reponse impulsionnelle symetrique ou antisymetrique (longueur paire ou impaire)

<div class="alert alert-danger" role="alert" markdown="1">

$$
H(\omega) = A(\omega)e^{-i\omega\delta + \phi_0}
$$

</div>


|             | Symetrique                                                         |                             Asymetrique                             |
| ----------- | ------------------------------------------------------------------ |:-------------------------------------------------------------------:|
| **Impaire** | $\color{red}{\text{Type I}}$ ![](https://i.imgur.com/buyR5jZ.png) $$\text{Retard entier} \\ \phi_0 = 0 \\ \text{pas de zeros imposes}$$  | $\color{red}{\text{Type III}}$ ![](https://i.imgur.com/68yg9sy.png) $$\text{Retard entier} \\ \phi_0 = 0 \\ \text{zeros imposes en }\omega = 0 \text{ et } \pi$$ |
| **Paire**   | $\color{red}{\text{Type II}}$ ![](https://i.imgur.com/QOUI7P5.png) $$\text{Retard non entier} \\ \phi_0 = \pi/2 \\ \text{zeros imposes en }\omega = \pi/2$$ | $\color{red}{\text{Type IV}}$ ![](https://i.imgur.com/eWAtzLO.png) $$\text{Retard non entier} \\ \phi_0 = \pi/2 \\ \text{zeros imposes en }\omega = 0$$  |


### Exercice

1. Designer un filtre simple par troncature en choisissant judicieusement la fenetre
2. Creer un filtre avec scipy et l'algorithme de minimax (`signal.remez`)
3. Analyser l'impact des parametres

<details markdown="1"><summary>Solution</summary>

![](https://i.imgur.com/5xU1MBy.png)

On fait comme si Fourier se met des oeilleres 

On veut appliquer une fonction porte

![](https://i.imgur.com/sYSExhF.png)

![](https://i.imgur.com/HIhFXMt.png)

</details>

Soit $P$ impulsion d'une fonction $e$ emise a differents instant. On souhaite retrouver les instants des differentes impulsions

$$
\begin{matrix}
e[n] = \underbrace{\sum_{k=0}^{K-1}\alpha^k\delta[n-k]}\quad \alpha\in]0;1[&y[n] = (x\ast e)[n]\\
\sum_{n=0}^{K-1}\alpha^kz^{-n}=\frac{1-\alpha^Kz^{-K}}{1-\alpha z^{-1}}&Y(z)=X(z)\ast E(z)\begin{aligned}&\to \frac{Y(z)}{E(z)} \\ &\to \frac{1}{E(z)}\end{aligned}
\end{matrix}\\
H(z)\cdot Y(z)\\
H(z) = \frac{1-\alpha z^{-1}}{1-\alpha^Kz^{-K}}\to y[n]-\alpha y[n-1] = x[n] - \alpha^K x[n-K]
$$

1. Trouver un filtre a l'aide de la TZ qui permet de retrouver $x$ (en connaissant $e$)
2. Determiner le filtre en temps
