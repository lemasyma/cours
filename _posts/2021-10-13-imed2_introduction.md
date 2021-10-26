---

title:          "TVID: 2D Motion Estimation"

date:           2021-10-25 10:00

categories:     [Image S9, TVID]

tags:           [Image, S9, TVID]

math: true

---

Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/H1FoSk4UK)



# Scalable video recording



<div class="alert alert-info" role="alert" markdown="1">
**Scalability** referes to the capacity of recovering physically meaningful image or video information from deconding only partial compressed bitstreams

</div>
- Quality scalability: 

    - finer to finer quantizations

- Spatial scalability: 

    - different spatial resolutions (Laplacian, Pyramid, ...)

- Temporal scalability: 

    - we can jump frames and add the missing ones progressively

- Frequency scalability: 

    - lower frequencies to higher frequencies

- Combination of basic schemes

- Granularity: coarse vs fine ones



<div class="alert alert-info" role="alert" markdown="1">
**Object-based scalability**: different resolutions for different objects

</div>


# 2D motion vs optical flow



![](https://i.imgur.com/DY7iRNh.png)



On a une sphere en train de tourner sans illumination: dans le flux video, il n'y a pas de difference.



Prenons ensuite une sphere dont la source lumineuse bouge: l'information visuelle changera.



<div class="alert alert-danger" role="alert" markdown="1">
The observed of apparent 2D motion is called **optical flow**

</div>


## Optical flow equation and ambiguity in motion estimation



- Imaginons une sequence video $\psi(x,y,t)$

- On image un point $(x,y)$ deplace en $(x+d_x,y+d_y)$ au temps $t+d_t$



<div class="alert alert-info" role="alert" markdown="1">
Under the *constant intensity assumption*, the images of the same object point at different times have the same luminance value



$$

\psi(x+d_x,y+d_y,t+d_t)=\psi(x,y,t)

$$

</div>


On fait un developpement de Taylor:



$$

\psi(x+d_x,y+d_y,t+d_t)=\psi(x,y,t)+\frac{\partial\psi}{\partial x}d_x+\frac{\partial\psi}{\partial y}d_y+\frac{\partial\psi}{\partial t}d_t

$$



On obtient:



$$

\frac{\partial\psi}{\partial x}d_x+\frac{\partial\psi}{\partial y}d_y+\frac{\partial\psi}{\partial t}d_t = 0

$$



Definisson $v_x=\frac{d_x}{d_t}$, $v_y=\frac{d_y}{d_t}$, $v_t=\frac{d_xt}{d_t}=1$



$$

\frac{\partial\psi}{\partial x}v_x+\frac{\partial\psi}{\partial y}v_y+\frac{\partial\psi}{\partial t} = 0

$$



Qui peut etre ecrit:



$$

\nabla\psi^Tv+\frac{\partial\psi}{\partial t}=0

$$



Avec $\psi^T$ le gradient spatial



![](https://i.imgur.com/Kg83lmC.png)



The flow vector $v$ at any point $x$ can be decomposed into 2 orthogonal components:



$$

v=v_ne_n+v_te_t

$$



<div class="alert alert-success" role="alert" markdown="1">
As we can observe, when a straight edge moves in the plane, we can only detect the normal $v_n$ of its motion vector !

</div>


Because $\nabla\psi=\Vert\nabla\psi\Vert e_n$ the optical flow equation can be rewritten as:



$$

v_n\Vert\nabla\psi\Vert+\frac{\partial\psi}{\partial t}=0

$$



Avec $\Vert\nabla\psi\Vert$ la *magnitude* du vecteur gradient.



Les consequences de ces equations sont:

1. A chaque pixel $x$

2. We can compute



$$

v_n=-\frac{\frac{\partial\psi}{\partial t}}{\Vert\nabla\psi\Vert}

$$



![](https://i.imgur.com/Cu0jdXe.png)



- This ambuigity in estimationg the motion vector is known as the *aperture problem*

- The motion can be estimated uniquely only if the aperture contains at least 2 different gradient directions



# General methodologies



- We consider the ME between 2 given frames, $\psi(x,y,t_1)$ and $\psi(x,y,t_2)$



![](https://i.imgur.com/nnTbnRE.png)



<div class="alert alert-warning" role="alert" markdown="1">
The problem is referred as to as **forward motion estimation**

</div>


## Notation



*Comment encoder les vecteurs de mouvements ?*

Ils ne sont pas les memes en fonction de l'espace, il faut les encoder de facon parametrique.



<div class="alert alert-info" role="alert" markdown="1">
*Fonction mapping*: nouvelle position



$$

w(x,a)=x+d(x,a)

$$



</div>


Avec le parametre $a$ qui encode le mouvement, ca nous donne la nouvelle position.



$$

a=[a_1,a_2,\dots,a_n]^T

$$



# Motion representation



![](https://i.imgur.com/fD9E0VK.png)



Different representations de mouvement.



Image b: pixel-based

- On a un vecteur pour chaque pixel de l'image



Image c: on va la faire en TP

- On suppose qu'on fait un decoupage par bloc

- On fait un vecteur de mouvement par bloc



*Pour le champ de vecteur, comment est-ce qu'on parametrise ?*

> Translations

> Polynomial motions

> Rotations

> ...



<div class="alert alert-success" role="alert" markdown="1">
On estime que l'image est faite de pixel et on fait de la pixel-wise

</div>


<div class="alert alert-warning" role="alert" markdown="1">
Ca fait 2 millions d'inconnues a trouver

</div>


On rajoute de la **regularite**.



<div class="alert alert-info" role="alert" markdown="1">
En general, on decoupe en **regions**.

</div>


*On estime d'abord le mouvement ou une region ?*



## Approche par blocs



![](https://i.imgur.com/7MJrtko.png)



On decompose l'image en blocs (ex: pour une image $100\times100$, en $33\times 33$)



<div class="alert alert-warning" role="alert" markdown="1">
On a des blocs qui vont se superposer car le mouvement n'est pas uniforme

</div>
> Et on s'en fout !



On a egalement des coins qui ont bouges.



<div class="alert alert-success" role="alert" markdown="1">
Il faut faire de la descente de gradient

</div>


- Les version les plus simples qu'on peut imaginer c'est en terme de translation

- Les blocs sont un bon compromis entre la precision et la complexite



![](https://i.imgur.com/BBNALxg.png)



<div class="alert alert-danger" role="alert" markdown="1">
It can induce **warping effects**

</div>


# Motion esimation criteria



<div class="alert alert-info" role="alert" markdown="1">


Displaced Frame Difference (DFD):



$$

E_{DFD}(a)=\sum_{x\in\Lambda}\vert\psi_2(w(x,a))-\psi_1(x)\vert^p

$$



where $\Lambda$ is the domain of all pixels in $\psi_1$ and $p$ a positive number



</div>


- When $p=1$, the above error is called *mean absolute difference (MAD)* and when $p=2$ *Mean Squared Error (MSE)*

- The *error image* $e(x,a)=\psi_2(w(x,a))-\psi_1(x)$ is usually called displaced frame difference (DFD) image

- When $a$ is optimal ($p=2$)



$$

\frac{\partial E_{DFD}}{\partial a}=2\sum_{x\in\Lambda}(\psi_2(w(x,a))-\psi_1(x))\frac{d(w(x,a))}{da}\nabla\psi_2(w(x,a))=0

$$



## Prenons un cas plus simple



$$

\frac{\partial\psi}{\partial t}d_t=\psi_2(x)-\psi_1(x)

$$



It is equivalent to minimize:



$$

E_{flow}=\sum_{x\in\Lambda}\vert\nabla\psi_1(x)^Td(x,a)+\psi_2(x)-\psi_1(x)\vert^p

$$



This solution verifies when $p=2$



$$

\frac{\partial E_{flow}}{\partial a}=2\sum_{x\in\Lambda}(\nabla\psi_1(x)^Td(x,a)+\psi_2(x)-\psi_1(x))\frac{\partial d(x,a)}{da}\nabla\psi_i(x)

$$



We can add a **penalty term** in our equation to enforce the smoothness of our vector field (i.e. must vary smoothly)



$$

E_s=\sum_{x\in\Lambda}\sum_{y\in N_x}\Vert d(x,a)-d(y,a)\Vert^2

$$



We want to minimize:



$$

E_{total}=E_{DFD}+w_sE_s

$$



with $w$ the *weighting coefficient*.



- We have to regularize but not too much (to avoid *over-blurring*)



# Minimzation methods



On va surtout regarder la methode exhaustive

- La methode de gradient

- La methode de Newton-Raphson



<div class="alert alert-warning" role="alert" markdown="1">
Avec la descente de gradient et le probleme de dimensionnalite, on tombe souvent sur des minimums locaux et non globaux

</div>


![](https://i.imgur.com/HtkyTw7.png)



- One important search strategy is to use a *multi-resolution* representation of the motion field and conduct the search in a *hierarchical manner*

- The basic idea is to first search the motion parameters in a coarse resolution, propagate this solution into a finer resolution, and then refine the solution in the finer resolution

- It can combat the slowness of exhaustive search methods



# Regularization



$$

E=\sum_{x\in\Lambda}(\frac{\partial\psi}{\partial x}v_x+\frac{\partial\psi}{\partial y}+\frac{\partial\psi}{\partial t})^2 + w_s(\Vert\nabla v_x\Vert^2+ \Vert\nabla v_y\Vert^2)

$$



# Block matching algorithm (BMA)



- Les blocs peuvent etre de forme polygonale

    - On prend en pratique des carres

- On suppose qu'on fait de la translation



## The Exhaustive Search Block Matching Algorithm (EBMA)



Under the block-wise translation model



$$

w(x;a) = x+d_{m}\quad x\in B_m

$$



Then the error can be written:



$$

E(d_m,\forall m\in\mathcal M)=\sum_{m\in\mathcal M}\sum_{x\in B_m}\vert\psi_2 (x+d_m)-\psi_1(x)\vert^p

$$



We can estimate the MV for each block individually



$$

E_m(d_m)=\sum_{x\in B_m}\vert\psi_2 (x+d_m)-\psi_1(x)\vert^p

$$



# Deformable block matching algorithm



![](https://i.imgur.com/YNVO2t9.png)



$$

d_m(x)=\sum_{k=1}^K\Phi_{m,k}(x)d_{m,k}\quad x\in B_m

$$



Le deplacement au bloc $m$ de $x$ est une somme ponderee des deplacements en 4 coins



# Node-based motion representation



- Nodal MVs vs Polynomial coefficients

    - Nodal

        - Stabilite



## Motion estimation using node-based model



$$

a=[d_k;k\in\mathcal K]

$$



$$

E(a)=\sum_{x\in B}(\psi_2(w(x,a))-\psi_1(x))^2

$$



where:



$$

w(x,a)=x+\sum_{k\in\mathcal K}\phi_k(x)d_k

$$



# Mesh-based motion estimation



- Dans le cas des blocs: estime independants et deformes

- Mesh: maillage sur l'image et on se permet de les deplacer en meme temps

    - Tout est corrole



![](https://i.imgur.com/Fp8ODR8.png)





<div class="alert alert-warning" role="alert" markdown="1">
**Contrainte a connaitre**: on ne veut pas que nos 2 carres s'inversent

</div>


- On a souvent des discontinuetes au niveau des edges

- Plus on augmente le nombre de noeuds, plus on a une estimation precise

    - Mais la puissance de calcul explose



# Global motion estimation



Plusieurs methodes existent



*Est-ce qu'on est dans le cadre ou pas d'avoir uniquement la camera qui bouge ?*

> Au foot et tennis, une grande partie du decor est stable



# Region-based motion estimation



*Est-ce qu'on separe en region ou on estime le mouvement ?*



3 approches possibles



# Multi-resolution motion estimation



- Various ME approaches can be reduced to solving an error minimization problem

- Major difficulties

    - Many local minima in the gradient-descent case

    - Not easy to reach the global minimum

    - Computation high



![](https://i.imgur.com/HCogSzT.png)



Pyramide laplacienne: on decompose l'image en bandes de frequence


