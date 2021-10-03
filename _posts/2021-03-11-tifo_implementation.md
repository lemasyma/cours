---
title:          "TIFO: Implementation"
date:           2021-03-11 17:00
categories:     [Image S8, TIFO]
tags:           [Image, TIFO, S8, max tree, FFT]
math: true
description: Implementation
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/S1lhhfqXO)

[**FASTER-FASTER-FASTER!!!**](https://youtu.be/Z9G1Mf6TZRs)

# Introduction
- Efficacite
    - Taille des images
    - Contrainte sur le temps de reponse
    - Contrainte sur le materiel (telephone...)
- Solution
    1. Bien penser ses algorithmes (et ss structures de donnes)
    2. Revoir son implementation sur CPU
    3. Eventuellemnt envisager une implementation sur GPU

# Bien penser ses algorithmes
- Representation des images
- ...

Repenser les algorithmes
- FFT (Fast Fourier Transform)
- ...

## Representation des images
Comment representer une image
- Matrice
- Vecteur
- Arbre/grpah
    - Max Tree, Min Tree
    - Tree of Shapes...
- ...

Matrice, vecteur: bien respecter le cache de la amchine !

Max Tree:
Image:
![](https://i.imgur.com/fKt3Vb5.png)

Max-Tree Correspondant
![](https://i.imgur.com/2LelRdi.png)

Racine de l'arbre: image entiere
- On part du $\min$ de l'image
- Des que le $\min$ separe 2 regions, on a 2 branches dans notre arbre

<div class="alert alert-warning" role="alert" markdown="1">
Une branche de l'arbre, c'est une region de l'image.
</div>

- Un noeud correspond a *tous* les pixels
- Les feuilles, si elles sont petites et nombreuses elles sont peut-etre que du bruit

## Exemple
Calcul de l'ouverture ultime
- Long dans le cas general
- Solution: utilisation du max-tree

<div class="alert alert-info" role="alert" markdown="1">
On enleve les petites regions et on fait la difference entre l'image d'origine et l'image obtenue. On continue sur les zones plus grosses et on regarde chaque fois le contraste obtenu.
</div>

On peut estimer quel est le motif le plus contraste et le garder.

![](https://i.imgur.com/yLL4YmD.png)
On a des residus en coupant les branches.

On parcours l'image en profondeur avec le niveau de contraste:
![](https://i.imgur.com/zyT13HQ.png)

``` cpp
UO(noe, parent_leve, max_contrast) {
    node.r=max(parent_level-node.level, max_contrasy)
    for all child c
        UO(c, node_level.r)
}
```

Resultats:

|Format|Nb of pixels|Time (ms)|
|-|-|-|
|128x128|16384|0,18|
|256x256|65536|2,39|
|512x512|262144|12,01|
|1024x1024|1048576|52,04|
|2048x2048|4194304|235,53|

<div class="alert alert-warning" role="alert" markdown="1">
Un probleme difficile a la base est rendu plus simple et plus rapide en changeant le codage de l'image
</div>

![](https://i.imgur.com/WB1LLKr.jpg)

On calcule l'ouverture ultime et on recupere tous les objets saillants
![](https://i.imgur.com/UWimqy3.png)

Pour recuperer le texte, on relance l'ouverture ultime sur une partie de l'image

![](https://i.imgur.com/68iPxzc.png)

- Repenser les algorithmes
    - Exemple FFT
    - Implementation des filtres
    - L'image integrable

## Calcul rapide
- FFT (1965 - Cooley et Tukey) (Gauss 1805??)
- The DFT:

$$
x(l)=\sum_{k=0}^{N-1}x(k)e^{-\frac{2j\pi kl}{N}}, l=0,...,N-1
$$

avec $N$ complexe mults, $N-a$ complexe add **pour chaque $I$**
- $O(N^2)$

Exploiter la symetrie:

$$
\begin{aligned}
W_N&=e^{-\frac{2j\pi}{N}}\\
W_N^{k(N-n)}&=W_n^{-kn}=(W_N^{kn})^* &(W_N^{kN}=1)\\
W_N^{k(n)}&=W_N^{k(N+n)}=W_N^{(k+N)n}
\end{aligned}
$$

On suppose que $N=2^m$

$$
\begin{aligned}
X(l)&=\sum_{k\text{ pair}}x(k)W_N^{lk}+\sum_{k\text{ impair}}x(k)W_N^{lk}\\
&=\sum_{k=0}^{\frac{N}{2}-1}x(2k)e^{-\frac{2j\pi2kl}{N}} + \sum_{k=0}^{\frac{N}{2}-1}x(2k+1)e^{-\frac{2j\pi2(k+1)l}{N}}\\
&= \sum_{k=0}^{\frac{N}{2}-1}x(2k)W_n^{2kl} + \sum_{k=0}^{\frac{N}{2}-1}x(2k+1)W_N^{(2k+1)l}\\
&= \sum_{k=0}^{\frac{N}{2}-1}x(2k)(W_n^2)^{kl}+W_n^l\sum_{k=0}^{\frac{N}{2}-1}x(2k+1)(W_N^2)^{kl} &W_n^2=W_{\frac{N}{2}}
\end{aligned}
$$

- $\frac{N}{2}$ DFT des echantillons pairs, $\frac{N}{2}$ DFT des echantilons imapairs

$$
X(l)=X_p(l)+W_N^lX_i(l)
$$

- Somme de 2 DFTs de $\frac{N}{2}$ echantillons

![](https://i.imgur.com/Heijq5y.png)

- $2\frac{N}{2}^2+N$ mutliplications
- Passe de $O(N^2)$ a $O(N\log N)$

## L'image integrale
Souvent besoin de calculer des moyennes/ecart-types dans une image

On passe un masque sur une image
![](https://i.imgur.com/RwwU2L4.png)
La valeur obtenue est la sommes des pixels

Si on veut calculer l'aire d'un rectangle aligne sur les axes:

$$
Aire(ABCD)=C-B-D+A
$$

![](https://i.imgur.com/aHz2zEL.png)

## Implementation des filtres
- Decomposition des convolutions (filtres separables)
    - $N\times N\to N+N$
    - La taille du filtre a un impact sur la vitesse d'execution
- Prise en compte des bordures?

![](https://i.imgur.com/H9XSuyA.png)

# Implementation sur CPU
- Utilisation du parallelisme
- Utilisation des instruction SIMD
    - Auto-vectorisation
    - Intrinsics SIMD
    - Boost::simd
- ...

# CPU
## SIMD
<div class="alert alert-info" role="alert" markdown="1">
Single instruction multiple data
- MMX, SSE, AVX, NEON...
- Registres sous formes de vecteurs


![](https://i.imgur.com/NYvmDll.png)

</div>
- Bien adapte a l'image

SIMD: un peu d'histoire
- 1997 jeu d'instruction MMX sur P166 (intel) *L'ordinateur multimedia* - Regsitre 64bits paratages avec le FPU
- 1997 jeu d'instrucutin - 3DNow ! (AMD)
- 1999 jeu d'instruction SSE - Registres 128bits
- SSE2, SSE3, SSE4 - Registres 128bits
- AVX - Registres 512 256bits
- AVX512 - Registres 512bits
- Neon sur ARM

SIMD Usage
![](https://i.imgur.com/jnjnG6e.png)
- Par le compilateur:
    - Active sur GGC avec l'option `-ftree-vectorize` (par defaut active avec `-O3`)
    - Renseigner l'option `-march=(corei7,native...)`
    - On peut avoir plus d'info avec les options `-fopt-info-vec-*` (`-fopt-info-vec-optimized` `-fopt-info-vec-missed`)
- Sorties:
    - `knn.cpp.229: note: LOOP VECTORIZED` (attention: plusieurs passes)

Auto-vectorisation

``` cpp
for (std::size_t x = 0; x < l; ++x) {
    output_image[x] = input_image1[x] + input_image2[x];
} // en complet desaccord avec notre coding style
```

Entrees:
- `-Wall -O3 -g -Wextra -Werror -m64 -march=native -ftree-vectorize -std=c++11 -fopt-info-vec-optimized #-fopt-info-vec-missed`

Sorties:
![](https://i.imgur.com/Y8ipzRz.png)

- Par le compilateur (auto-vectorisation)
    - Pas toujours facile
    - s'assure que les donnees soient alignees (quasi impossible en cpp :-( )
        - `__attribute__((aligned(TL_IMAGE_ALIGNEMENT)))`
        - `std::align`
        - `Alignas(.)`
        - `aligned_alloc`
    - `__restrict__`
    - `assume` dans ICC
- Bonnes pratiques:
    - Utiliser des indices plutot que des pointeurs
    - Array of Structures vs Structure of Arrays
    - Ne pas interrompre une boucle

``` cpp
for (k = 0 ; k < size_vect; k++) {
    double t = v_example[k] - data[k_data++];
    res += t * t;
    // if (res > tresh) {
    //     breaks;
    // }
}
res *= -g;
return exp(res)
```

- SIMD - intrinsics
    - Possible de les utiliser en c/c++
- Exemple:

``` cpp
for (std::size_t x = 0; x < l; x+=16) {
    __m128i v_input_image1 = _mm_loadu_si128((const __m128i*)(input_image1 + x));
    __m128i v_input_image2 = _mm_loadu_si128((const __m128i*)(input_image2 + x));
     __m128i v_output1 = _mm_add_epi8(v_input_image1, v_input_image2);
     _mm_store_si128((__m128i*)(output_image+x), v_output1);
}
```
- Probleme d'alignement des donnees `aligned_alloc`
- Difficilement portable

![](https://i.imgur.com/8LFiO56.png)

- Function Multiversioning (GCC 4.8)
    - Utile pour la portabilite du programme

``` cpp
__attribute((target("default")))
int foo() {
    // The default version of foo
}
__attribute((target("sse4.2")))
int foo() {
    // foo version for SSE4.2
}
__attribute((target("arch=atom")))
int foo() {
    // foo version for the Intel ATOM processor
}
```

## Boost::simd
- Permet d'ecrire de maniere agnostique vis-a-vis de la vectorisation
- Le code devient portable
- Vectorisation vers certains processeurs gratuite et pour d'autres non

# Implementation sur GPU
Une fois qu'on a pousse nos algos a fond sur CPU...

- Implementation sur GPU
    - Cuda
    - OpenCL
    - Compute Shaders
    - ...

## Compute Shaders
- Glsl "portable" ou autre

![](https://i.imgur.com/m87IVeT.png)
On a plein de threads dans chaque work group

# Conclusion
- Pas de points "incontournables"
- Reflechir a notre implem pour qu'elle soit la plus efficace possible