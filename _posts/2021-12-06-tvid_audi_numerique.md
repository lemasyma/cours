---
title:          "TVID: L'audio numerique en pratique"
date:           2021-12-06 10:00
categories:     [Image S9, TVID]
tags:           [Image, S9, TVID]
math: true
---

Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/HJeFGIsKY)

# Onde sonore

Le briques de base de la compression du son sont un peu differentes de celle de la video.

## Perception du son

*Qu'est-ce que c'est le son ?*

<div class="alert alert-info" role="alert" markdown="1">
**Onde sonore**
Variations de pressions convoyees par un milieu gazeux

![](https://i.imgur.com/FecVgyR.gif)

</div>

Pour la perception:
- Oreille humaine
- Transducteur sonore $\Rightarrow$ signaux electriques
- Trois parties:
    - Oreille externe: captation
    - Oreille moyenne: amplification
    - Oreille interne: transducteur

### Oreille externe

- Collecte et amplifie les sons
- Localise les sons (pavillon, phase)
- L'envoie dans le conduit auditif
- Protege le tympa (cerumen)

![](https://i.imgur.com/ZMNW5wU.png)

### Oreille moyenne

- Vibration aerienne $\to$ solidienne (tympan)
    - Transformer les vibrations accoustiques en vibrations solides
- Amplification: marteau / enclume / etrier
- Protection niveaux forts (80dB): reflexe stapedien

![](https://i.imgur.com/kF6MRiR.png)

![](https://i.imgur.com/hmjtuEq.png)


### Oreille interne

- Transforme le signal en signal electrique
- Vestibule: centre de l'equilibre
- Cochlee: transforme les vibrations en signaux electriques
    - Recouverte de cellules cillees
    - Hautes Frequences en bas (debut)
    - Basses Frequences en haut (fin)
- Membrane basilaire: filtre special parole meme en environnement bruyant

![](https://i.imgur.com/j8ekJ9r.png)

> Accouphenes: cellules cillees petees qui envoient n'importe quoi
> Lie aux problemes de circulation du sang
> Aussi l'usure: on a ecoute des trucs trop forts

## Specifications

- Spectre: $20 HZ \to 20 KHz$
- Perception d'intensite **logarithmique**
    - $dB = 3\times\log_2(ratio)$
    - $3 dB: \times2, 20 dB:\times 100$
    - Jusqu'a $120dB$ pour l'oreille
- Seuils de perception minimale **variables**

![](https://i.imgur.com/sg0aZkk.png)

# Enregistrement du son

<div class="alert alert-info" role="alert" markdown="1">
**Objectif**
Capter les variations acoustique dans un materiau
</div>

Analogique:
- Transduction solide
- Transduction magnetique

Numeriques:
- Representations binaires
- Nombreuses
    - Fete du string pour les formats

## Transduction solide du son

<div class="alert alert-info" role="alert" markdown="1">
**Principe**
- Amplifier l'onde avec un pavillon
- Graver l'onde dnas un materiau par un mobile
</div>

Pionnier: **phonographe**, Thomas Edison, 1877

![](https://i.imgur.com/3UIZQGi.png)

![](https://i.imgur.com/kGsI0vK.gif)

<div class="alert alert-info" role="alert" markdown="1">
En verite, c'est un francais, Edouard-Leon Scott de Martinville, 1860 le pionner avec le **Phonautographe**

![](https://i.imgur.com/b87vhKC.png)

</div>

<div class="alert alert-danger" role="alert" markdown="1">
On ne pouvait que ecrire, relire detruisais le charbon qu'il utilisait pour graver
</div>

<div class="alert alert-success" role="alert" markdown="1">
On a reussi a reconstruire un de ses enregistrements ou il chante au clair de la lune

> a̷̙͔̳̹̱̭͔̲̺̳͉̪̰̼͂̀̈́͑̓̆͂͌̓̀̈́͐̒͐̂͛͑͒̑͑̕͝ų̸̨̼̼̫̙͔̳̺̖̯̳̼̳͓̪̪̫͔͖̘̤̜̒̅̉̾̈́͌̍́̚̕͜͜͝ ̴̹̥̝̺̫̘̬̩͓̣͈̔͑c̶̲̠̥̫͓̠̋͜͜͜ļ̶̡̧̨̛͔̟̥̜͚͚̗̪̱͍͈͎͖̪̣̣͕̩͕̩͔̭͖̟͚͗̉̇̆̃̇̊̀̓́̔̈͆̾̅̏̍̀̑́̔̍̐̿̆̕̕̚͜͠ͅͅą̸̡̢̧̟͇͚̣̲̜͉͓̺̫̭̟̖̘̝̞̼̙̞̭̭͎͚̤̙̺̠͒́͑͛̅̀̓͗̽̑̆͑̀͂͂͂î̴̢̨̨̡͉̞̘̘͕̖̤̮̱͚̝̘̺̅́̄̿͂͜͜ř̷̛̛͈͚̥̭̖̭͉̺͓̰͚͎̳̹̟̜͔̭̖̰̥̖̈́̈́̆̿̂̽̂̔̾̈́̃͂͛̓̑͋̒͋̎̆̈́́̓̓̀̆͋͜͜͠͝ ̴̢̧̡̡̛̪̯̞̞͈̖̜̻̺͓̥̭̝̥̘̝̖̰̠̩̱̬̼͙̗͈̳̳̝͉̗̩͒͆̿̇̓̌͌̅̈̒̑̽̈̎̈̅̾̓̒̀̄̓̊͗̂̈́͆͌̚̕͜͝͝͝͝ͅd̸̢̺̞̦͇̘̙̪͖̻͎͚̺͕̼͓̦̲͖̩̝̫̠͑̈̔́̀̒̂̀͋̐̈́̓̈́̔̽̓̏̅̐͊̑͜͝ͅe̶̳͉̼͎͉̯͍̿̍͛́͂̑̓̑͒̀̏̈́̚͝ ̶̢̪̻̘͓̹̰̬̥͚̟̻̝͚͍͎͍̗̲̩̦̪̣̦͉͈̩̯̤͕̟͙̝̙͒̈́̍̒̔̍̈́̄̌͋̑͋̄͗͐̽̅͑̋͗̏̈́͊̾̏̒̈́̈́̎̿̍̄̚̚̕͜͜͝͝͝͝ͅl̵̡̖̹̟͚̞͈̙̘̗͈̭͍̲͉̩̥̙͖̻͓̼͚̱͎͖̤̝̺̱̺͍̲̰̯̥̊̆̉́̔͐̒̋͒̂̌̈́̒̄̄̚̚̚ā̶̢̢̨̡̭̝̺̙͖͎͖̣̘̯̤͓̺̞̠͇͙͈̦̻̘͔̭̮̝͓̪̘́̃̀̀̊̓͂̓̐͐́̎̽ͅ ̴̨̧̢̭̳̗̮͔͈͎̘͙̣̠̝̙͋̔̑́́͒̓͂̑̈̈̌̆̏͒̑͋̔̂͑̈́͂̕̚͝͠͝l̵̛̛̬̥͓͇͇͖̈̾͗́̍̊̆̅̏̄̓̐̍̉̐͛͂͛͋̓͂̋͐͑̑́̅̍͒̆̕̚̕̚͠͠͝ū̸̡̡̨͙̱͙̩͖̠̼̳̮͎̞̪͉̮̩̮̭̝̝̦̬̹̳͍̰̙̟̪͕̥̰̬̠̙̰̉͊ͅͅn̶̨̡̢̛̬͓͕͙̳̘̣̗͍̲̣̮̬̞͔̞̬̣͙͕̘̦͐́̒̂̀̓͒̊̈́̿̑̈́̐̏͛͋̚͝͝ͅȩ̵̙̬̜͔̳͍̹̣̪̦̮̮̰̮̫̤̻̳̗̦͕̰̝̪̣͎̄̿̅̏̉͋̽́̐͝͝͝

</div>

> Thomas Edison avait compris que ca devait etre reproductible

**Gramophone**, Emile Berliner, 1886
- Meme principe qe le Phonographe
- Disque rotatif industrialisable
    - Carton (fragile)
    - Celluloid (inflammable)
    - Vinyle (compromis)
- Vitesse **angulaire** constante: $78$ a $100$ rpm
- Du bord vers le centre
- Perte de qualite au centre
    - Perte de bande passante

![](https://i.imgur.com/llQa6jL.png)

Les microsillons reconstruisant le son:

![](https://i.imgur.com/OCxs71K.png)

> En faisant les reflets qu'on voit sur un disque

![](https://i.imgur.com/ASTGoeQ.gif)

## Transduction magnetique du son

<div class="alert alert-info" role="alert" markdown="1">
**Principe**
- Onde accoustique $\to$ signal electrique
- Signal electrique $\to$ champ magnetique
- Polariser un substrat magnetisable
</div>
- Assez coercitif
    - Coercitivite magnetique: resistance d'un milieu magnetique a se faire remagnetiser
    - Plus un milieu est coercitif, plus il est resistant

*Comment ca se passe ?*

![](https://i.imgur.com/2431kKo.png)

- Tete en anneau, magentisation horizontale
- On a une bande magnetique qui defile
- On induit ce champ magnetique qui polarise les particules
- On a un signal accoustique qu'on a electrise et magnetise

Ecrite: Courant electrique $\to$ Champ magnetique
Lecture: Champ magnetique $\to$ Courant electrique

Pionnier: **Telegraphone a fil**, Valdemar Poulsen (neerlandais), 1898
- Magnetisation d'un fil de fer
- Bande quelques minutes
- **$1^{er}$ enregistrement: Empereur Franz Josef d'Autriche, 1900**
- Evolution immediate: fil de fer $\to$ lame d'acier
- Plus robuste, plus dangereux

**Magnetophone a bande**, BASF/AEG (allemands), 1930

![](https://i.imgur.com/7ruOiQb.png)

**Cassete 8 pistes**, Ampex/RCA/MOTOROLA (US), 1963

![](https://i.imgur.com/cMEFKwk.png)

> On dirait une bobine mais elle s'enroule sur elle-meme

![](https://i.imgur.com/y6CkVHW.png)

<div class="alert alert-success" role="alert" markdown="1">
Lecture sans fin !
</div>

> Quand on le mettais dans l'auto-radio (c'etait fait pour les voitures), ca rembobinait et ca jouait en boucle

*Pourquoi 8 pistes ?*
> C'est en stereo en 4 voie, des qu'on arrive a la fin d'une piste, on saute 2 voies
> Il y a ~1h30 de musique

**Compact Cassette**, Philips (Neerlandais), 1963

![](https://i.imgur.com/49RX9BN.png)

![](https://i.imgur.com/vQ8Ygxe.gif)

# Enregistrement numerique du son

## Onde sinusoidale

<div class="alert alert-info" role="alert" markdown="1">
Une onde sinusoidale est:
- **continue** dans le temps
- **continue** en intensite
</div>

![](https://i.imgur.com/Tq5B56w.png)

- Discretiser un signal continu **periodiquement**
- $\Rightarrow$ Choix d'une frequence $F_e$

## Theoreme de Shannon

Un signal est une somme de sinusoides:

![](https://i.imgur.com/NIYjaeW.png)

- La frequence la plus elevee est $f_{max}$
- Echantillonner a $F_e$ est valide si 

$$
F_e\gt 2\times f_{max}
$$

En dessous: **aliasing**
- $=$ repliement de spectre
- $=$ frequences parasites

![](https://i.imgur.com/n49p8YZ.png)

## Echantillonage

![](https://i.imgur.com/nGFK6kH.png)

<div class="alert alert-success" role="alert" markdown="1">
Signal echantillone en intervalles reguliers
</div>

*Quid de l'intensite ?*

- Sous-ensemble discret de valeur d'un espace contine $\{0\to V_{max}\}$
- Idealement les valeurs quantifiees appartiennent a la courbe

![](https://i.imgur.com/0uXYnzN.png)

<div class="alert alert-danger" role="alert" markdown="1">
Sauf que **non**
</div>

## Pas de quantification

Espace discret a $N$ valeurs $[0\dots V_{max}/N]$

![](https://i.imgur.com/AL0D0kW.png)

- En numerique: $N=2^M$ aec $M$: nombre de bits

<div class="alert alert-danger" role="alert" markdown="1">
Erreur de quantification $e$

$$
0\lt e\lt V_{max} / 2^M
$$
</div>

![](https://i.imgur.com/dEECk1c.png)

<div class="alert alert-warning" role="alert" markdown="1">
Erreur de quantification **inevitable**
</div>

- $N$ petit $\to$ $\color{red}{e}$ eleve
- $\color{orange}{Visible}$
- $\color{red}{Audible}$

### $\color{red}{e}$ d'un signal triangulaire

![](https://i.imgur.com/dkS4h4b.png)

### $\color{red}{e}$ d'un signal sinusoidal

![](https://i.imgur.com/uaiOoQk.png)

## Format PCM

<div class="alert alert-info" role="alert" markdown="1">
**Pulse Coded Modulation**
</div>

- Signal continu discretise en temps et en intensite
- Via circuits CNA/ADC
- **Echantillonnage** temporel a $F_e$ ![](https://i.imgur.com/65KcP7B.png)
    - $F_e\ge 2f_{max}$
    - Sinon *aliasing*
- **Quantification** d'intensite sur $N$ bits: $2^{N}$ valeurs
    - Erreur de quantification $e$
    - Dynamique $\simeq 6dB$ par bit ($16bits\simeq96 dB$)
- **Reconstruction** ![](https://i.imgur.com/gRzaUjk.png)
    - Via circuits CNA/DAC
    - Filtre passe-bas fort a $F_e/2$

# Audio numerique non compresse

## CD

![](https://i.imgur.com/HNkz53J.png)

![](https://i.imgur.com/xmPpHlX.gif)

- Sony + Philips, 1982
- Diametre: $12 cm$
- PCM: $44.1KHz$, $16$ bits, stereoo
- Debit: $2\times44100\times2=176.4Ko/s (1.411 Mb/s)$
- Lecture:
    - Du centre vers le bord
    - Laser infrarouge
    - Vitesse **lineaire** constante $500\to200 rpm$
- $74$ minutes de son $\Rightarrow 783Mo$
    - Peu de correction d'erreur
    - Pas grave...
- Avec correction d'erreur: $650Mo$
    - $\Rightarrow$ CD-ROM (Read Only Memory)

## DAT

![](https://i.imgur.com/zX5Z3Rl.png)

![](https://i.imgur.com/P1ibwuJ.jpg)

![](https://i.imgur.com/aTdAVX1.png)

- Sony, 1987
- 2 canaux PCM, $48KHz$, $16$ bites
- Debit: $2\times 48000\times 2 = 192Ko/s (1.536 Mb/s)$
- Lecture:
    - Bande magnetique
    - $\sim 50cm/min (8.15mm/s)$
    - $4mm$ d'epaisseur
- Jusqu'a **3h par bande**

*Comment ?*

![](https://i.imgur.com/Ev6CTi1.png)

- $\Rightarrow$ Lecture **hellicoidale**
    - Tete rotative $2000rpm$
    - *Inclinee*
    - $\Rightarrow 3.15m/s$
    - Comme VHS
    - Et streamers (DDS, AIT, LTO, ...)

![](https://i.imgur.com/SmPvlpD.gif)

## DVD-A

![](https://i.imgur.com/G7M5Cc1.png)

<div class="alert alert-success" role="alert" markdown="1">
Un DVD contient bien plus de donnees
</div>

> On etait dans l'infrarouge pour les CDs, on est dans les rouges pour les DVD-A
> D'ou le nom blu-ray

- DVD Forum, 2000
- 2 a 6 canaux
- $44.1 KHz$ a $192KHz$
- $16$, $20$, $24$ bits
- Majoritairement non compresse
- Cas extremes: Meridian Lossless Packing
    - $\color{green}{\text{Sans perte}}$
- Lecture:
    - Laser rouge
    - Simple couche/double couche ($8.5Go$)

<div class="alert alert-danger" role="alert" markdown="1">
Incompatible DVD-VIDEO, CD AUDIO, CD-ROM
</div>

![](https://i.imgur.com/2Kmz0hF.gif)

## Super Audio CD

![](https://i.imgur.com/zICzaNR.png)

- Sony + Philips, 1999
- "Successeur du CD"
- 2 a 6 canaux
- $\color{red}{2.8224MHZ !?}$
- $\color{orange}{1\text{ bit ??}}$

<div class="alert alert-danger" role="alert" markdown="1">
LISIBLE PAR LA PS3 ???
</div>

<div class="alert alert-success" role="alert" markdown="1">
Format DSD
</div>

## Format PWM

- Approximation d'un signal analogique par des pulses
- Bruit de quantification $=V_{max}/2^N$
- Rappel PCM:
    - **Densite constante $=$**
        - Largeur pulses **constante**
        - Amplitude **variable**
        - Bruit audible (8 bits, 16 bits...)
    - Reconstruction du signal
        - Filtrage BF a $F_e/2$

![](https://i.imgur.com/VCD89Ol.png)

- $\color{red}{\text{PMW: Pulse With Moderation}}$
    - **Densite variable $=$**
        - Largeur pulses **variable**
        - Amplitude **constante**
    - Reconstruction du signal:
        - Integration
        - +Filtrage BF

### Inconvenients

- Electronique rapide
- Bruit max de quantification fort $[0\dots V_{max} / 2]$ !

### Avantages

- Bruits de quantification tres haute frequence ($MHz$)
    - Personne n'est capable de l'entendre

<div class="alert alert-success" role="alert" markdown="1">
Inaudible !
- Qualite $++$

Filtrage BF simple
- Cout $--$
</div>

# Compression numerique du son

L'audio non compresse,

![](https://i.imgur.com/cllGKsr.png)

## Qualite CD

- 2 canaux, $44.1KHz$, $16$ bits
- Non compresse: $2\times 44.K \* 2$
- $\color{red}{176.4 Ko/s = 1.411 Mb/s}$
- CD: 650 Mo data, $\sim 780 Mo$ audio
    - $\Rightarrow 74$ min
- ADSL de 2000:
    - $64 Kb/s$ a $45$ euros par mois: non
    - $128 Kb/s$ a $90$ euros par mois: non
    - $2 Mbits$ a $200$ euros par mois:
        - $100\%$ du debit en audio
        - "et mon internet ?"
- Aujourd'hui (fibre, 4G, 5G)
    - Toujours pas mainstream
    - Reste un service Premium (Deezer HiFi, Spotify HD, ...)

## Qualite "Home Cinema"

![](https://i.imgur.com/lLga0Nk.png)

- $\ge 6$ canaux, $48KHz$, $16$ bits
- Non compresse: $6\times 48K\* 2$
- $\color{red}{576 Ko/s = 4Mbit/s = 2Go/h}$
- Dvd: $4.9 Go$
    - $\Rightarrow 2.5h$ de son
    - pas de video !
- ADSL, mauvaise 4G: 8 Mbits
    - 50\% du debit juste en audio
    - Et le debit video ?

<div class="alert alert-danger" role="alert" markdown="1">
Injouable sans compresseur
</div>

# Algorithmes temporels

## Differential PCM (DPCM)

<div class="alert alert-info" role="alert" markdown="1">
**Hypothese**: signal source stationnaire
</div>
- $=$ proprietes independantes dans le temps (esperance, variance)
- Ok avec des basses frequences
- (Pas sur en hautes frequences)

<div class="alert alert-info" role="alert" markdown="1">
**Principe**: pas le sample PCM courant depend du precedent
</div>

- Codage des differences $\Rightarrow$ **Differential PCM**

**Encodeur**
- Memoriser les 2 valeurs consecutives
- Calcule la difference $\Rightarrow$ dynamique reduite
- Encodage du residu avec moins de bits
- Compression de $25\%$

![](https://i.imgur.com/qKwWwNw.png)

**Decodeur**
- Accumule la valeur reconstruite courante
- Dequantifie le residu
- Signal reconstruit $=$ d'origine ?
- $\color{red}{NON!}$
- La quantification des differences induit de l'erreur $\color{red}{\text{qui s'accumule a la reconstruction}}$

![](https://i.imgur.com/0gznc1Z.png)


## DPCM in-loop

**Encodeur ameliore**
- Memorise deux valeurs consecutives
- Calcule la difference $\Rightarrow$ dynamique reduite
- Encodage sur moins de bits !
- Compression de $25\%$
- Calcule la valeur reconstruite **en prevision du decodeur**

![](https://i.imgur.com/LNI6HWc.png)

<div class="alert alert-success" role="alert" markdown="1">
Erreur de construction **contenue**
</div>

**Decodeur**
- Idem decodeur simple

![](https://i.imgur.com/InZfEyf.png)

## Adaptive DPCM

<div class="alert alert-info" role="alert" markdown="1">
Codage differentiel adaptatif
</div>

**Encodeur**
- Minimise l'erreur differentielle adaptativement:
    - **Prediction du signal** courant avec les valeurs passees
        - Polynome ordre $\sim 8$
    - **Quantification variable du residu**
        - 4 a 6 bits
    - Compression de 75\%

![](https://i.imgur.com/lNFvyij.png)


**Usages**
- Multimedia (MS/IMA ADPCM, 44.1KHz, 4 bits)
- Telephonie ($G.721$ $8KHz$, $5-6$ bits)

![](https://i.imgur.com/3ELAoUM.png)

> Dans les DS et GBA, le son est **exclusivement** en ADPCM
> On se mange l'erreur de la compression

**Raffinement: deux bandes de frequences**
- Deux residus, deux debits
- Bande passante plus grande ($7KHz\Leftrightarrow F_e = 14 KHz$)
- $\Rightarrow G.722$ (VolP HQ, DECT HQ)

## NICAM

<div class="alert alert-info" role="alert" markdown="1">
Nearly Instantaneous Companded Audio Multiplex
</div>

- BBC, $\sim1986 \to 2012$, France $1995\to 2011$
- $32kHz$, $14$ bits stereo, $728Kbits/s$
- Codec multiplexe avec signal video analogique (QPSK)

> Exemple: signal SECAM + NICAM @ 5.85 MHz

![](https://i.imgur.com/90Vu8zD.png)

Filtrage BF luma: image plus floue :(

> On ne peut pas faire rentrer plus que ce qui est possible dans un meme tuyau

### Parenthese perceptuelle

*Comment on percois le son ? Qu'entend l'oreille ?*
> Le son peut etre masque par d'autres sons

- Phenomene de masquage sonore temporel

<div class="alert alert-info" role="alert" markdown="1">
**Posterieur**

Si on son $\color{red}{faible}$ suit un son $\color{green}{fort}$, l'oreille n'entend $\color{red}{\text{pas}}$ le son $\color{red}{faible}$

</div>

*Est-ce qu'il y a un masquage anterieur ?*
> Oui !

<div class="alert alert-info" role="alert" markdown="1">
**Anterieur**

Si on son $\color{green}{fort}$ suit un son $\color{red}{faible}$, l'oreille n'entend $\color{red}{\text{pas}}$ le son $\color{red}{faible}$ (non causal !)

</div>

> Autant qu'on le deteste, notre cerveau un bien un temps de latence de traitement

![](https://i.imgur.com/T47sZJ1.png)

$\Rightarrow$ **Latence de perception** des transitoires de dynamique

### NICAM: Principe de fonctionnement

- **Echantillonnage** PCM 32 KHz 14 bits
- **Decoupage** en tranches de $1ms=32$ samples
- **Pour chaque tranche**:
    - Prendre le plus grand sample $\Rightarrow$ sert de **facteur d'echelle**
    - Quantifier a $10$ bits tous les samples
    - Selon le **facteur d'echelle** ("Compand")
    - $\color{red}{Faible}$: enlever les bits de poids $\color{green}{forts}$ vides (petits signaux, pas de perte)
    - $\color{green}{Fort}$: enlever les bits de poids $\color{red}{faibles}$ (signaux fortsm pertes "negligeable")

Au pire: quantification forte et breve de petits signaux $\to$ RSB eleve
- Variations dynamiques et masquage temporels cachent la misere

**Decodeur**
- Dequantifier selon le facteur d'echelle
- CNA avec $1ms$ de latence ("**Nearly instantaneous**")

### Schematisation

![](https://i.imgur.com/9hRX8rw.png)

### Quantification Compand

![](https://i.imgur.com/LiVyVxe.png)

# Quantification non-lineaire : A-LAW

## Contexte

- Proprietes temporelles de la voix:
    - Peu de niveaux $\color{green}{forts}$
    - **Beaucoup** de niveaux $\color{red}{faibles}$, silences
    - Voix numerique: typiquement $8KHz/8$ bits
- Rappel numerisation PCM:
    - Bruit de quantification uniforme
    - **Fort** dans les niveaux $\color{red}{faibles}$, **faible** dans les niveaux $\color{green}{forts}$
- Autrement dit:
    - PCM 8 bits degrade souvent la voix
    - Quelles alternatives ?

## Principe

**Modifier la dynamique**
- **Augmenter** les niveaux $\color{red}{faibles}$
- **Baisser** les niveaux $\color{green}{forts}$

<div class="alert alert-success" role="alert" markdown="1">
Bruit de quantification remodele
</div>

*Quelle fonction fait cela ?*
> Loi logarithmique

$$
F(x)=\text{sgn}(x)\begin{cases}
\frac{A\vert x\vert}{1+\ln(A)}, &\vert x\vert\lt \frac{1}{A}\\
\frac{1+\ln(A\vert x\vert)}{1+\ln(A)}, &\frac{1}{A}\lt \vert x\vert \lt1
\end{cases}
$$

![](https://i.imgur.com/J9L6GdM.png)

## En pratique

Analogiquement:
- *Avant* CAN + *apres* CNA
- Paquets numeriques: PCM 8 bits classiques

![](https://i.imgur.com/tCZHz8V.png)

Numeriquement:
- Apres CAN PCM $\color{green}{HQ}$ (12 bits) + *avant* CNA PCM HQ
- Paquets numeriques: traitement A-Law $12\leftrightarrow 8$ bits

![](https://i.imgur.com/FGQcLo1.png)

## Resultat

![](https://i.imgur.com/Fo5pb4w.png)

<div class="alert alert-success" role="alert" markdown="1">
On a inverse la tendance des erreurs
</div>

Erreur de quantification:
- **Forte** sur les signaux $\color{green}{forts}$
- **Faible** sur les signaux $\color{red}{faibles}$

Standard telephone $G.711$