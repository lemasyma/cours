---
title:          "CAMA : ma42 - Gradient conjugué"
date:           2020-05-25 10:00
categories:     [S6, Shannon, CAMA]
tags:           [S6, CAMA, Shannon]
math: true
description: Programmer le gradient conjugué
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/HkKafe6Jv)
# Cours du 25/05

# Programmer le gradient conjugué

A partir de ce [cours sur le gradient conjugué](http://perso.unifr.ch/ales.janka/numeroptim/07_conjgrad.pdf) programmez en Python + Numpy le gradient conjugué en exploitant les astuces mathématiques indiquées pour optimiser
votre code.

* Effectuez des tests pour valider votre code. 
* Comparez la vitesse de convergence à celle du gradient avec μ optimal. Tracez des courbes de convergence (cf la feuille qui en parle)
* Comparez les temps de calcul.


Note : Veuillez écrire des fonctions les plus propres possibles, en particulier qui n'utilisent pas des variables globales comme c'est le cas dans ma correction du gradient (ma33).

<details markdown="1">
<summary>Solution</summary>

~~~ python
import numpy as np
import scipy.linalg as lin
import matplotlib.pylab as plt

%matplotlib inline
%config InlineBackend.figure_format = 'retina'
~~~
~~~ python
def make_system(N):
    A = 1.0 * np.random.randint(-10, 10, size=(N,N))
    A[np.diag_indices(N)] = 0.1 + np.abs(A).sum(axis=0)    # diag dominante
    A = A + A.T                                            # symétrique
    A = A / np.abs(A).sum(axis=0).mean()
    b = 1.0 * np.random.randint(-10,10,size=(N))
    return A, b

A, b = make_system(2)
print(A, "\n\n", b)
~~~
~~~
[[ 0.65174129 -0.32338308]
 [-0.32338308  0.70149254]] 

 [ 6. -1.]
~~~
~~~ python
def gradient_conjugué(A, x0, b, error=1E-9, convergence=False):
    x = x0.copy()  # je ne veux pas modifier les paramètres qu'on me donne
    e2 = error**2
    r = A @ x - b  # le gradient mais aussi le résidu
    r2 = r @ r
    p = -r
    if convergence:
        conv = [np.sqrt(r2)]
    while r2 > e2:
        alpha = (r @ r) / np.dot(A @ p, p)
        x += alpha * p
        r += alpha * (A @ p)
        beta = (r @ r) / r2
        p = -r + beta * p
        r2 = r @ r
        if convergence:
            conv.append(np.sqrt(r2))
    return np.array(conv) if convergence else x
~~~
~~~ python
gradient_conjugué(A, np.array([0.,0.]), b, convergence=True)
~~~
~~~
array([6.08276253e+00, 2.51964707e+00, 2.22044605e-16])
~~~
~~~ python
def compute_error(N, method=gradient_conjugué):
    A, b = make_system(N)
    x = method(A, np.zeros(N), b)
    err = A @ x - b
    return np.sqrt(err @ err)

compute_error(10)
~~~
~~~
4.165926057296536e-15
~~~

## Comparons avec le gradient simple
~~~ python
def gradient(A, x0, b, e = 1E-9, convergence=False, max_iterations=1000):
    x = x0.copy()
    e2 = e**2
    k = 0
    gradJ = A @ x - b
    g2 = gradJ @ gradJ
    divergence_limite = 1E6 * g2
    if convergence:
        conv = [np.sqrt(g2)]
    while g2 > e2:
        µ = np.dot(gradJ, gradJ) / np.dot(A @ gradJ, gradJ)
        x -= µ * gradJ
        gradJ = A @ x - b
        g2 = gradJ @ gradJ
        if convergence:
            conv.append(np.sqrt(g2))

        # la suite n'est que des tests pour se protéger
        if g2 > divergence_limite:  # au cas où on diverge
            print("DIVERGE")
            break
        k += 1
        if k > max_iterations:  # c'est trop long, je crains la boucle infinie
            print('Trop long, boucle infinie ?')
            break
    return np.array(conv) if convergence else x
~~~
~~~ python
# vérifions que ca marche

compute_error(10, method=gradient)
~~~
~~~
6.767792116739432e-10
~~~

## Perfs
~~~ python
# comparons les performances

seed = 123
np.random.seed(seed)

%timeit compute_error(1000, method=gradient)
~~~
~~~
34 ms ± 4.23 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
~~~
~~~ python
seed = 123
np.random.seed(seed)

%timeit compute_error(1000, method=gradient_conjugué)
~~~
~~~
32.1 ms ± 847 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
~~~
Le gain n'est pas clair...

## Nombre d'iteration dans les 2 cas
~~~ python
N = 1000
A,b = make_system(N)
x0 = np.zeros(N)
~~~

### Pour le gradient simple
~~~ python
err = gradient(A, x0, b, convergence=True)
~~~
~~~ python
plt.plot(np.arange(err.shape[0]), err)
plt.title('Convergence du gradient')
plt.semilogy();
~~~
![](https://i.imgur.com/slve81U.png)

### Pour le gradient conjuge
~~~ python
err = gradient_conjugué(A, x0, b, convergence=True)
~~~
~~~ python
plt.plot(np.arange(err.shape[0]), err)
plt.title('Convergence du gradient conjugué')
plt.semilogy();
~~~
![](https://i.imgur.com/lIn7THw.png)
Argh, le gradient conjugué n'est pas la révolution prédite !
</details>

# Un cas réel

Logiquement vous devriez être décu aussi on va tester avec un problème réel qui correspond à cet exemple de l'[équation de Poisson](https://doc.freefem.org/tutorials/poisson.html). Le système matriciel de ce problème est téléchargeable [ici](https://www.lrde.epita.fr/~ricou/cama/data/Ab.npz). Une fois le fichier sauvé, pour récupérer A et b faites :

``` python
npz = np.load('/tmp/Ab.npz')
A = npz['A']
b = npz['b']
```

* Faites une étude rapide de A, indiquez quel pourcentage des valeurs de A est différent de 0. Afficher l'image de la matrice avec `plt.imshow(A)` (faire une grande image pour voir quelque chose).
* Refaites la comparaison entre les deux méthodes avec ce système matriciel.
* Regardez la documentation de `lin.solve` (en particulier les options) et comparer `lin.solve` à vos deux algorithmes.

<details markdown="1">
<summary>Solution</summary>

~~~ python
print(A.min(), A.max())
~~~
~~~
-1.5693731138089555 4.357203686821435
~~~

~~~ python
diff0 = (A != 0).sum() / (A.shape[0] * A.shape[1])
print(f"Pourcentage de valeurs != 0 : {100 * diff0:.3} %")
~~~
~~~
Pourcentage de valeurs != 0 : 0.339 %
~~~
~~~ python
plt.figure(figsize=(15,15))
plt.imshow(A)
~~~
![](https://i.imgur.com/sZDkpZj.png)

## Comparaison gradient simple et conjugué
~~~ python
%time err = gradient_conjugué(A, np.zeros(len(A)), b, convergence=True)
~~~
~~~
CPU times: user 1.75 s, sys: 155 ms, total: 1.91 s
Wall time: 521 ms
~~~
~~~ python
plt.plot(np.arange(err.shape[0]), err)
plt.title('Convergence du gradient conjugué')
plt.semilogy();
~~~
![](https://i.imgur.com/cZ0HyLY.png)
~~~ python
# le gradient simple

%time err = gradient(A, np.zeros(len(A)), b, convergence=True, max_iterations=10000)
~~~
~~~
CPU times: user 1min 11s, sys: 4.3 s, total: 1min 15s
Wall time: 19.4 s
~~~
~~~ python
plt.plot(np.arange(err.shape[0]), err)
plt.title('Convergence du gradient')
plt.semilogy();
~~~
![](https://i.imgur.com/Qr2sVIE.png)
On voit la supériorité du gradient conjugué tant en nombre d'itérations (175 contre 7800) qu'en temps de calcul (0,5 s contre 20 s).

## Comparaison avec `lin.solve`
~~~ python
?lin.solve
~~~
~~~ python
%time x = lin.solve(A, b, assume_a='pos')
~~~
~~~
CPU times: user 170 ms, sys: 85.1 ms, total: 255 ms
Wall time: 94.4 ms
~~~
~~~ python
r = A @ x - b
r @ r
~~~
~~~
2.0359257929180678e-25
~~~
On note aussi lin.solve est plus rapide et sa solution est nettement meilleure... lin.solve utilise une méthode directe ici. Cela est dû au fait que Scipy utilise la bibliothèque Lapack (qui est imbatable).

## Le gradient conjugué de Scipy (avec Lapack)
Le gradient conjugué à tout son sens pour les matrices creuses aussi il est dans la partie "sparse" de Scipy. On a vu que notre matrice à plus de 99 % de valeur nulles ce qui en fait bien une matrice creuse. Aussi je la charge dans le format COO qui ne stocke que les valeurs non nulles et:

~~~ python
import scipy.sparse as sparse
from scipy.sparse.linalg import cg

Ac = sparse.load_npz('/tmp/Acoo.npz')
%time x = cg(Ac, b)
~~~
~~~
CPU times: user 24.8 ms, sys: 15.1 ms, total: 39.9 ms
Wall time: 10.8 ms
~~~
On gagne un facteur 10 !
</details>