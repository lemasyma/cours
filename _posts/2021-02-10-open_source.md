---
title:          "Open Source: Comprendre, Contribuer"
date:           2021-02-10 9:00
categories:     [tronc commun S8, Open Source]
tags:           [tronc commun, Open Source, S8]
math: true
description: Comprendre, Contribuer
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/HJxdQGZWO)

Par Lionel Laske
lionel@lespot-bouygues.com

# Introduction
Lionel LASKE
* Responsable Le Spot BOUYGUES
* Membre du board de l'organisation Open source sugarlabs
* Auteur et Lead developpeur sugarizer 
    * 10 000 utilisateurs
    * 80 contibuteurs
    * Plateforme educative pour enfant
* Mentor Google Summer of Code depuis 2013

# Pourquoi ce cours ?
* Parce que l'Open Source est un phenomene mondial !
    * devenu culturel
    * open data: open source lie a la data 
        * Wikipedia
        * Open Street Map
        * TousAntiCovid
* Parce que c'est un sujet complexe
    * part de technique (Github)
    * part de juridique
    * modele economique
        * Comment ca fonctionne ?
        * Comment on gagne de l'argent avec des outils ouverts ?
* Pour nous faire partager son experience

# Partie 1 - Comprendre
## Quizz Time
Quelle est la societe qui contribue le plus sur GitHub ?
- [ ] The Linux Foundation
- [ ] Google
- [x] Microsoft
- [ ] RedHat

* Microsoft
    * $1^{er}$ contributeur GitHub
    * TypeScript
    * Visual Studio Gode
    * GitHub
    * Npm
* Google
    * $2^{nd}$ contributeur GitHub
    * Android
    * Angular
    * TensorFlow
    * Kubernetes
* Facebook
    * React
    * React Native
    * GraphQL
* IBM
    * RedHat
    * Eclipse
    * Apache Spark

## Pourquoi on fait de l'open source ?
<div class="alert alert-warning" role="alert" markdown="1">
L'Open Source est omnipresent
</div>
![](https://i.imgur.com/8VmUZ7b.png)

## Avantages de l'Open Source
* Cout d'usage
* Cout de developpement
    * S'appuie sur d'autres developpeurs pour developper un outils
* Communaute
    * Mettre un projet en open source: permet de developper une communaute
    * Avancer plus vite sur l'outils
* Innovation
    * Plus facile d'innover
    * Beneficier des idees des autres
* Securite
    * Peut etre a double tranchant
    * Avoir le code ouvert: "Vous pouvez me faire confiance"
    * White hat trouvent des failles de securite
* Reversible
    * Voir comment sont traitees nos donnees

## Definition
<div class="alert alert-danger" role="alert" markdown="1">
Les 4 libertes fondamentales
* **Liberte 0**: Pouvoir executer le programme
* **Liberte 1**: Pouvoir etudier son fonctionnement
* **Liberte 2**: Pouvoir le redistribuer
* **Liberte 3**: Pouvoir le modifier et le redistribuer
</div>

*Comment s'assurer qu'un logiciel est Open Source ?*
Plusieurs licences possibles

|open source initative|Free Software Foundation|
|-|-|
|Approche pragmatique|Approche Ethique|
|Considerations techniques: logiciels de meilleurs qualites car plus de contributeurs et de reviewers|Considerations idealistes: l'utilisateur doit garder le controle du logiciel|
|Favoriser les modeles economiques|Liberer les utilisateurs|

### ... en opposition au logiciel proprietaire
* Seul l'auteur peut acceder au code source (ou des partenaires sous NDA)
* Pour utiliser le logiciel vous devez accepter une licence qui:
    * Interdit la redistribution/pret/revente

#### Exemple: Licence Windows
![](https://i.imgur.com/YNbBnnS.png)

## Historique
### Quizz Time
Qui a invente le concept d'Open Source ?
- [ ] Steve Job
- [ ] Linus Torvald
- [ ] Bill Gates
- [ ] Richard Stallman

<div class="alert alert-warning" role="alert" markdown="1">
Aucune des 4 reponses n'est fausse
</div>

### 1960: Prehistoire
* Le hardware est tres cher
* L'informatique est reservee aux chercheurs
* Le logiciel a une complexite limitee
* Le logiciel est disponible librement

### 1970: Proprietaire
* Baisse du cout des ordinateurs
* Augmentation de la complexite des logiciels
* Apparition des 1er micro-ordinateurs
* Premieres licences proprietaire
* Seules les universites continuent a partager le code

#### Anecdote : An Open Letter to Hobbyusts par Bill Gates
![](https://i.imgur.com/XVefRls.jpg)

### 1980: Naissance
* 1983: annonce du projet GNU par Richard Stallman
* 1985: Creation de la Free Software Fundation
* 1987: Lancement de GCC

#### Anecdote: l'imprimante de Stallman
* Richard Stallman est programmeur au AI Lab du MIT
* Il souhaite modifier le pilote d'une imprimante Xerox pour signaler automatiquement les bourrages papiers
* Il sollicite un collegue qui dispose du code source mais qui refuse *"Il m'a explique qu'il s'etait engage a ne pas en donner de copier"* car il avait une NDA avec Xerox
> *"Ce qui rendait l'enjeu important etait le caractere systematique et impersonnel de son refus, le fait qu'il s'etait engage d'avance a ne cooperer ni avec moi ni avec aucune autre personne"* - R. Stallman

### 1990: Fondation
* 1991: Creation de **L**inux
* 1993: Lancement des distributions Debian, NetBSD, FreeBSD, RedHat
* 1994: Creation de **M**ySQL
* 1995: Creation de **P**HP
* 1996: Creation d'**A**pache
* 1998: Lancement de Netscape
* 1999: Lancement de SourceForce

### 2000: Explosion
* 2002: Lancement Firefox
* 2004: Lancement de la distribution Ubuntu sur base Debian
* 2005: Lancement du projet Git
* 2007: Lancement de Android, sur une base Linux
* 2008: Lancement de GitHub
* 2008: Lancement de Chromium en meme temps que Chrome

### 2010: Evidence
* 2010: Lancement de nom
* 2013: Revelations de Edward Snowden
* 2014: Lancement de Signal
* 2018: Rachat de Github par Microsoft pour 7,5 milliards de \$
* 2019: Rachat de RedHat par IBM pour 34 milliards de \$

## Licences
### Quizz Time
Combien existe-t-il de licences Open Source "officiellement" reconnues ?
- [ ] 3
- [ ] 10
- [x] 100

### A qui appartient votre code ?
* A votre ecole si vous etes etudiants
* A votre employeur si vous etes salaries
* A vous si vous le faites chez vous
    * Sauf contrat employeur specifique

<div class="alert alert-danger" role="alert" markdown="1">
Pour permettre a d'autres d'y contribuer, il faut donc utiliser une licence **ouverte**.
</div>

|Permissive|Copyleft|
|-|-|
|Tout le monde peut modifier|Tout le monde peut modifier|
|Les versions peuvent ne pas etre modifiables|Tout le monde doit pouvoir modifier les versions modifiees|

### Ce que decrivent les licences
* Les regles de mention de paternite du programme
* Les regles pour modifier le programme
* Les regles pour redistribuer le programme
* Les regles pour associer d'autres licences dans le meme programme
* La protection contre les brevets

### Cartographie des licences Open Source
![](https://i.imgur.com/4TisdJa.png)

### Anecdote: la controverse React
* React est lance par Facebook en 2013 sous **Apache v2**
* En 2014 React passe sous licence **BSD** avec une note sur l'utilisation des brevets:
    * Permet d'utiliser les brevets possedes par Facebook
    * Facebook s'autorise a vous retirer les droits d'utilisation si vous menez une action en justice contre eux ou contre une autre entreprise utilisant React
* En 2015 Facebook ajoute une note supplementaire a la licence pour eviter les confusions
* En 2017 la fondation Apache prend position contre l'utilisation de React car il n'est pas sous une licence Open Source
* En novembre 2017, React passe sous licence MIT

### Anecdote: la licence SSPL MongoDB
* MongoDB est lance en 2009 sous licence **AGPL v3**
* Les clouds d'Amazon, d'IBM, ... louent des instances MongoDB sans que MongoDB en tire benefice
* En Octobre 2017, MongoDB devient une societe cotee
* En Octobre 2018 passe son code sous licence **SSPL** et soumet cette nouvelle licence a l'OSI
    * La licence impose qu'un fournisseur de cloud utilisant MongoDB ouvre *toute la stack technique* permettant son herbegement
* En Mars 2019 l'OSI refuse de consider la licence SSPL comme une licence Open Source
    * RedHat, Debian, Fedora et les autres distributions Linux excluent MongoDB de leurs distributions
* En Janvier 2019, Amazon lance DocumentDB, une base de donnees NoSQL compatible MongoDB

## Gouvernance
### Quizz Time
Qui décide des contributions acceptées dans le Kernel Linux ?
- [ ] Linus Torvald seul
- [x] Le board de la Linux Foundation
- [ ] Les entreprises qui contribuent au Kernel

### Le modeles de gouvernance Open Source
#### Dictateur bienveillant
* "BDLF": Benevolent Dictator For Life
* Le Dictateur est generalement l'auteur initial
* A le dernier mot sur toutes les grandes decisions
* Evite des discussions sans fin...
* La qualite et le succes du projet dependent beaucoup de la sagess du dictateur

##### Exemple: Gouvernance Linux
* Jeremy Malcolm - Internet Governance Forum
    * > "*Torvalds possesses ultimate authority* to decide which contributions to the Linux operating system kernel should be accepted and which should be refused"
    * > "The Linux kernel development process is neither anarchistic nor consensual: *if Torvalds does not like a patch, it does not go in to the kernel*"

![](https://i.imgur.com/YY6EF9e.png)

#### Gouvernance Communautaire
* Pilotage ouvert et public (mailing list, IRC, ...)
* Choix collegiaux:
    * Qui peut contribuer
    * Qui peut commiter
    * Qui peut resoudre les conflits
* Recherche de consensus dans la decisions
* Favorise la Meritocratie
* Release sont generalement mois frequentes car circuit de decision plus long

##### Exemple: Gouvernance FreeBSD
* Composition:
    * Contributeurs (plusieurs milliers)
    * Commiters (500)
    * Core team (9)
* Les Commiters approuvent les PR des Contributeurs
* Les Commiters elisent la Core Team
* La Core team choisi les Commiters parmi les Contributeurs
* La Core team decide des orientations du projet

#### Gouvernance Entreprise
* Une seule entite controle la Conception, le Developpement et les Release
* Contributions externes pas forcement bienvenue
* Roadmap pas necessairement publique
* Discussions internes et controverses pas forcement publiques

##### Exemple: Gouvernance AOSP
> "The Android Open Source Project (AOSP) includes individuals working a variety of roles. **Google is responsible** for Android product management and the engineering process for the core framework and platform; however, AOSP considers contributions from any source, not just Google."

> "Project leads are senior contributors who oversee the egineering for individual Android projects."

## Modeles Economiques
### Quizz Time
Quelle est la société qui tire le plus de revenu de l'Open Source ?
- [ ] Google
- [ ] Docker
- [x] RedHat

RedHat: 3,5 milliards de \$ de revenus par an
### Gagner de l'argent avec l'Open Source ?
* Vente de licences
    * Une version "Community" gratuite avec une licence copyleft
    * Une version "Entreprise" payante avec plus de features et une licence permissive
* Vente de services
    * Hosting ou mode SaaS
    * Formations/Certifications
    * Support
* Autres
    * Publicite
    * Dons/Mecenat
    * Droit d'usage de la marque

#### Exemple: 
##### Elastic Search
![](https://i.imgur.com/k51LHZ6.png)

##### IntelliJ IDEA
![](https://i.imgur.com/UnnLZOy.png)

##### VLC
* > "Le logiciel Francais le plus utilise au monde... et le moins rentable" J.B. Kempf
    * 1 million de telechargements/jour
    * 450 millions d'utilisateur
    * Plus de 3 milliards de telechargement
* Developpe en 1997 a l'Ecole Centrale Paris
* Sous GPL en 2001
* Gere par l'association VideoLan en 2008
* Creation en 2012 de la societe **VideoLabs**
    * 18 employes, 1m d'euros de CA
    * Monetise la terchnologie et les utilisateurs VLC pour delivrer des services

#### Anecdote: Heartbleed
* Vulnerabilite dans OpenSSL en 2011
* Decouverte en avril 2014
* OpenSSL etant utilise tres largement (Nginx, Apache, Android, ...) la faille touche 17% des serveurs wen et 800.000 objets connectes
* En 2012 la **Open SSL Foundation** touchait 2.000\$/an pour financer ses contributeurs
* Lancement en 2014 de la **Core Infrastructure Initiative**
    * Idee de la Linux Foundation
    * 3.000.000\$/an pour financer des projets Open Source "core"

# Partie 2 - Contribuer
## Pourquoi contribuer a l'Open Source ?
* Ameliorer ses competences
* Participer au bien commun
* Recontrer des gens du monde entier
* Apprendre ou apprendre aux autres
* Ameliorer les outils qu'on utilise
* Se faire connaitre

## Quel projet choisir ?
### Quizz Time
Quel est le pourcentage estimé de projets Open Source actifs ?
- [ ] 30%
- [x] 10%
- [ ] 5%

<div class="alert alert-danger" role="alert" markdown="1">
La plupart des projets Open Source sont des echecs...
![](https://i.imgur.com/GzpLcRn.png)
</div>

Les causes les plus courantes:
* Ne repond pas a un vrai besoin
* Plus assez de developpeuts interesses (ou le developpeur principal s'en desinteress)
* Le projet est depasse techniquement, un competiteur fait mieux
* Manque de documentation
* Manque de leadership, pb de gouvernance, conflits
* Manque de temps/d'argent

<div class="alert alert-success" role="alert" markdown="1">
Ce fort taux d'echec n'est pas necessairement une mauvaise chose, beaucoup d'idees peuvent en decouler
</div>

### Identifier les signes vitaux d'un projet
* Regarder les statistiques du projet
    * Watch / Star / Fork / Used by
* Verifier les commits
    * De quand date le dernier commit ?
    * Combien y a-t-il de contributeurs ?
* Verifier les issues
    * Combien y a-t-il d'issues ?
    * Sont-elles recentes ?
    * Sont-elles fermees regulierement ?
* Verifier les PR
    * Combien y a-t-il de PR ?
    * Sont-elles recentes ?

#### Exemple: 
##### React contributors vs Vue.js contributors
![](https://i.imgur.comS0jyyx.png)

##### Statistiques Angular sur Synopsis Open Hub
![](https://i.imgur.com/5JCgbVR.png)

### Verifier que le projet est accueillant
* Est-ce un projet Open Source ? Y a-t-il une licence ?
* Comment acceuille t-il les contributeurs ?
    * Y a-t-il un guide du contributeur ? un code de conduite ?
    * Y a-t-il de la documentation ?
    * Y a-t-il des issues tagguees "good first issue" ?
* Comment les mainteneurs repondent aux contributions ?
    * Repondent-ils rapidement aux questions/issues ?
    * Repondent-ils amicalement ?
    * Y a-t-il des dicussions sur les issues/PR ?
    * Remercient-ils les gens pour leur contribution ?

#### Exemple: code de conduite Kubernetes
![](https://i.imgur.com/CRJlWw9.png)

## Comment contribuer ?
### Checklist: demarrer une contribution
- [ ] Installer l'application/le projet
    * S'assurer que c'est la derniere version
- [ ] Jouer avec l'application/le projet
- [ ] Lire la doc
- [ ] S'abonner aux listes de diffusion, forum, IRC, slack, ...
- [ ] Commenter des posts/issues
    * C'est deja une contribution !
- [ ] Declarer une issue
    * Verifier qu'il n'y a pas deja une issue similaire
    * Indiquer les etapes pour la reproduire et l'env. de test
- [ ] Faire une Pull Request

### Creer une Pull Request
<div class="alert alert-info" role="alert" markdown="1">
Les Pull Request (PR) sont la base des contributions Open Source
![](https://i.imgur.com/BWm0e3H.png)
</div>

#### Exercie: First Contributions
* Un site pas a pas pour realiser votre $1^{ere}$ Pull Request
* Faites une PR pour ajouter votre nom a la liste des contributeurs
 
![](https://i.imgur.com/DZt8HUU.png)

#### Exemple: Hacktober Fest
* Evenement organise par Digital Ocean pour inciter a contribuer a des projets Open Source
* Chaque annee du 1$^{er}$ au 31 Octobre
* Les projets interesses inscrivent leur repo et tagguent des issues "hackotberfest"
* Les 70 000 premiers participants qui font 4 PR gagnent un t-shirt

## Le Google Summer Of Code
### Qu'est-ce que c'est ?
<div class="alert alert-info" role="alert" markdown="1">
Le Google Summer of Code (GSoC) est un programme "online" international destine a encourager les etudiants des ecoles et universites a participer au developpement de projets Open Source.
</div>

### Objectifs du programme
* Pour les organisations Open Source: **identifier** chaque annees de nouveaux dev
* Pour les etudiants: **participer** au dev de projets Open Source, se construire une experience et un reseau, etre **remunere** (~4,000 euros/2 mois)
* Pour Google: **soutenir** le monde de l'Open Source

### Comment ca marche ?
* Les organisations faisant de l'Open source font la demande a Google pour etre des organisations du GSoC
* Google choisit les organisations qui participent
* Les etudiants *soumettent leurs candidatures* pour realiser les projets proposes
* Les organisations choisissent les **meileurs** etudiants
* Les etudiants developpent, encadres par les mentors des organisations

### Quelques organisations participant au GSoC
![](https://i.imgur.com/zaMQLEY.png)

### Comment etre retenu au GSoC ?
- [ ] Commencer a contribuer avant Mars/Avril
- [ ] Se presenter a l'organisation
    * Mailing list, forum
- [ ] Multiplier les contributions (PR, issue)
- [ ] Bien comprendre le projet propose
    * Echanger avec les mentors
    * Suggerer des solutions
    * Realiser un prototype
- [ ] Passer du temps a rediger sa proposition
- [ ] Demander une relecture de sa proposition

# Conclusion

<div class="alert alert-danger" role="alert" markdown="1">
* L'Open Source est un phenomene culturel
* Comprendre son fonctionnement est indispensable
* Contribuer est une source de satisfaction et un vrai plus pour monter en competence
</div>

![](https://i.imgur.com/WVlpr9c.png)

# Questions/Reponses
Dans le cas où la licence est ajoutée après la création du repository, son effet est-il rétroactif ? La première version (les premiers commits avant la licence) du projet est-elle concernée par la nouvelle licence ?
> Non, la licence ne s'applique qu'aux versions actuelles

On a parlé de l'open source en terme de software. Qu'en est il du hardware ?
> Je ne peux pas vous en apprendre plus

Comment sera evalue le cours ?
> Aucune idee, a voir avec la pedago

# Ce n'est pas fini !
Pour en savoir plus: retrouver la version integrale sur YouTube

# Final Quizz
Avez-vous maintenant envie de devenir contributeur ?
- [ ] Oui
- [ ] Non
- [ ] Ne sais pas