---
title:          "GPRO - Refresh from ing1 classes"
date:           2021-02-08 14:00
categories:     [tronc commun S8, GPRO]
tags:           [tronc commun, GPRO, S8]
math: true
description: Refresh from ing1 classes
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/SkITr20ed)

Refresh du cours de GPRO de l'ing1
# What is a Project ?
<div class="alert alert-info" role="alert" markdown="1">
Un projet est une entreprise **temporaire** initiee dans le but de fournir un produit, un service ou un resultat unique.
</div>
Exemple:
* Bridge
* Railroad
* Apollo
* Vaccine
* Mobile Ap
* Web Site

<div class="alert alert-warning" role="alert" markdown="1">
NOT a project: Operations
</div>

# Project Management
A **pragmatic approach** vs "Just do it!"

A quoi ca nous sert le project management ?
> En entreprise, travail toujours sur un projet, on aborde le project management de facon generic

## Characteristics of a project
1. Scope
    * Qu'est-ce qu'on veut faire ?
    * Comment on doit le faire ?
2. Time
    * S'organiser pour livrer le projet a une deadline
3. Cost
    * Realiser le projet avec le budget

![](https://i.imgur.com/hDnNidS.png)

# Parties prenantes - Stakeholders
<div class="alert alert-info" role="alert" markdown="1">
Toute personne ayant une influence sur le projet
</div>
Dans les parties prenantes:
* Pour une application, les utilisateurs
* Dans un stage, le maitre de stage

# Project life cycle
![](https://i.imgur.com/cC8xEjA.png)

Scope:
* Cadre du projet
* Pour une app, si on veut qu'elle tourne sur IOS, Android, etc.

Plannification:
* Organiser le travail
* Gros du boulot du chef de projet

Execute/control:
* Commencer a developper
* Suivre le plan

# PM Classic or AGILE ?

**BOTH !**

## Classic predictive
* Liste de fonctionnalites precises
* Decoupe en lots de travaux
* Partage le travail

<div class="alert alert-info" role="alert" markdown="1">
Predictive car on prevoit tout des le depart.
</div>

![](https://i.imgur.com/J6S8xBR.png)

## Agile
* Methode cyclique
* Developpe par cycles

Methode quand on est pas certain du but final
![](https://i.imgur.com/sTvw295.png)

### Agile Scrum
![](https://i.imgur.com/TX8Addr.png)
Un sprint dure maximum un mois et a chaque sprint on livre un bout de logiciel qui fonctionne

# QUIZZ 1
Parmi toutes ces realisations quelle est celle qui N'EST PAS un projet ?
- [ ] Modifier une application existante pour introduire une toute nouvelle fonctionnalite
- [ ] Construire un nouveau DATACENTER
- [x] Asssurer recurreement la mise en production de toutes les nouvelles applications, ou de nouvelles versions pour la corporation qui vous emploie
- [ ] Implementer une nouvelle application
- [ ] Mettre en oeuvre une nouvelle comptabilite sur SAP

# Phase 1: Initiate
Understand the meaning of the project

## Project Charter
Fiche de route du projet
Contient des infos detaillees:
* Objectifs
* Dates cles
* Parties prenantes

*Une objectif flou et vous ne savez pas ce qu'on attend de vous*
*Le client vous pilote sans donner une vision claire du projet*
**Vous avez le Droit et le Devoir de collecter les informations de comprehension du PROJECT CHARTER**

### Project Charter contents
* Project purpose
* Measurable project objectives and related success criteria
* High0level requirements
    * Fonctionnalites definies de maniere large
* High-level project decription, boundaries, and key deliverables
* Summary milestone schedule
* Key stakehodler list
    * Clients
    * Manager
    * Les gens qui travaillent sur le projet
* Overall project risk
* Project approval requirements
    * Faire valider le projet une fois fini

## Examples
### Exemple 1 - PFEE MTI Bouyfues Telecom 2020
* Presente d'abord le contexte
* Problematiques
    * Baisses des ventes suite a des promotions agressives de la concurrence
    * Veille concurrentielle faite a la main
    * Detection tardive des actions des concurrentes
* Objectifs du projet
    * Ameliorer la capacite d'analyse des marketplaes
    * Reduire le temps de reaction face aux promotions agressive des concurrentes
* Grandes lignes du projet
    * Visualiser les evolutions de prix
    * Predire l'evolution des prix
    * Alerter l'utilisateur de changement de prix
    * Disposer d'un module d'opti des prix sous contraintes
* Planning des Jalons principaux
* Risques globaux
    * Risque de livraison d'un projet difficilement maintenable
    * Risque que le scraping soit peu durable
    * Risque que la realisation ne corresponde pas aux attentes a cause d'un besoin faiblement ecrit
* Critere de sortie du projet
    * Les differents livrables sont fonctionnels dans une version pilote de production disponible sur l'env AWS de l'entreprise

### Exemple 2
* Perimetre
* Timeline

![](https://i.imgur.com/RHiRboO.png)

# Phase 2: Scope
![](https://i.imgur.com/WWgyS2K.png)

Product Scope (Perimetre Produit) pour un logiciel applicatif:
* Exigences fonctionnelles
* Contraintes (techniques, de qualite, projet)

## Exigence fonctionnelle
<div class="alert alert-info" role="alert" markdown="1">
Ce que le client attend comme fonction de notre produit
</div>

Exemples pour une application:
* Permet de creer un compte
* Permet de rejoindre un groupe de discussiom
* Permet de prendre RDV

<div class="alert alert-danger" role="alert" markdown="1">
Exigence fonctionnelle **N'EST PAS** une specifite fonctionnelle.
</div>

## Get the product scope
Situation 1: Customer team provides fully Documented Product/Project Scope
<div class="alert alert-danger" role="alert" markdown="1">
Dev team reviews the Scope with appropriate Product Owner
</div>

* Collecting requirements - Recueillir les exigences
* Fromalizing the requirements - formaliser les exigences
    * Tableau des exigences 

## Exemple
![](https://i.imgur.com/eX807Yo.png)

# Agile Methodology: The product backlog
## User story
<div class="alert alert-danger" role="alert" markdown="1">
En tant que `<qui>`, je veux `<quoi>` afin de `<pourquoi>`.
</div>

Difference GILE: On peut affiner au fur et a mesure les exigences en avancant dans la release.

## Exemple
![](https://i.imgur.com/ZV7lyaN.png)

Completer les Product Backlog ou les tableaux d'exigence
4 types d'exigences (projet dev de logiciel)
* Exigences Fonctionnelles
* Contraintes techniques
* Exigences Qualite
* Exigence du Projet

## Quizz 3
Dans la methode Predictive, un cahier des charges ou un tableau des exigences, ou, dans la methode Agile, un Product Backlog est un document dont le contenu correspond a:
- [ ] Description des mecanismes techniques permettant le fonctionnement du produit
- [ ] Description des travaux a mettre en oeuvre pour realiser le produit
- [ ] Description des tests unitaires pour valider le produit
- [x] Description du planning produit
- [ ] Description des exigences, besoins et fonctionnalites auxquels le produit correspond

# From SCOPE to Project Schedule
![](https://i.imgur.com/fHS017j.png)

## Take scope definition result as INPUT
![](https://i.imgur.com/Qp8jK39.png)

<div class="alert alert-warning" role="alert" markdown="1">
Work Breakdown Structure: WBS
Work Package: WB
</div>
WB are usually attached to a Project Deliverable

One WBS for Presence:
![](https://i.imgur.com/gBRyilA.png)

![](https://i.imgur.com/x2dAXY1.png)

# Defining activities
Amount of work that can be estimated

<div class="alert alert-warning" role="alert" markdown="1">
Need for expert judgement
</div>

# Define Milestones - Bornes
## Decomposition en activites
Presence 1-POC
![](https://i.imgur.com/zWhLK2j.png)

![](https://i.imgur.com/9mRTA3m.png)

# Resources
<div class="alert alert-warning" role="alert" markdown="1">
Need for expert judgement
</div>

# Duration
<div class="alert alert-warning" role="alert" markdown="1">
Need for expert judgement
</div>
* Estimate
* TOP Down vs Bottom UP

## Ordonner et Estimer
![](https://i.imgur.com/Jf6mkFS.png)

## Exemples from MTI PFEE
Construite via Microsoft project
![](https://i.imgur.com/eMCUAI9.png)

<div class="alert alert-danger" role="alert" markdown="1">
En resume, en decoupant l'ensemble des productions a realiser et le travail qu'elles representent.

Puis apres estimation, en repartissant dans le temps ces activites.

Vous disposez d'un plan et d'un planning initial (BASELINE) de realisation de votre projet complet.
</div>

# Planning AGILE
## Set an order to User Stories - Organiser les Users Stories
![](https://i.imgur.com/s3TXfmH.png)

On peut definir un **flot de narration**. Par rapport a ce flot de narration, pour chaque etape des User Stories corresponsdent (se connecter, se deconnecter, modification de mot de passe, creation de mot de passe, etc.).

Sur l'axe des ordonnees: organise les users stories suivant le **flot de narration** (ex: Je me connecte/deconnecte) $\rightarrow$ ce qui parait le plus important.

## Release Carving - Decoupage en Releases
*Quelles sont les fonctionnalites essentielles que l'on doit mettre en Release 1 Par Exemple ?*

Une fois qu'on a regroupe depuis le product backlog un des user stories pour la release (**Decoupage en sprint (Sprint Carving)**) on **affecte des "Story Points" (assign "Story Points")** $\rightarrow$ assigner des **points**
L'affectation des points doit etre fait par l'equipe de developpement.

![](https://i.imgur.com/xmHA2i4.png)

<div class="alert alert-danger" role="alert" markdown="1">
En resume,
Vous avez convenu dans le Productbacklog le perimetre de la release a realiser.

Vous avez decompose cette release en N Sprints d'un poids equivalent pouvant etre realises successivement dans le temps que represente un Sprint.
![](https://i.imgur.com/wq6gUmX.png)
</div>

### Exemple MTI PFEE
#### Exemple 1
![](https://i.imgur.com/asyZAV0.png)

#### Exemple 2
![](https://i.imgur.com/j4dC59s.png)
![](https://i.imgur.com/DPx7uQW.png)

## Des prerequis avant de commencer le developpement Sprint 0 ?
<div class="alert alert-warning" role="alert" markdown="1">
Each Sprint Starts with: **SPRINT PLANNING**
</div>
![](https://i.imgur.com/oGmk6Y0.png)

### Exemple MTI PFEE
![](https://i.imgur.com/kmLYMUR.png)

## Quizz 5
Quelle est la SEULE affirmation vraie concernant un SPRINT dans la methode Agile ?
- [ ] La duree d'un sprint peut etre de 3 mois
- [ ] Lors de l'execution d'un sprint, le client peut proceder a des changements de perimetre qui sont geres dans la gestion de changement
- [ ] Un Sprint peut debuter meme si le president n'est pas termnie
- [x] Un Increment Produit "Fini fonctionnel" et potentiellement utilisable est produit lors d'un Sprint
- [ ] La duree du Sprint est variable et s'adapte aux taches a realiser pour chacun d'eux

## Monitoring Sprint Execution: Daily SCRUM
![](https://i.imgur.com/kjg6XS2.png)

Une fois le sprint fini: **sprint review**
* Client et dev
* Demo
* Doit etre valide par le client

**Sprint retrospective**:
* Reunion de devs
* Qu'est-ce qui a marche
* Qu'est-ce qui n'a pas marche

## Communication Client-Dev
Construite dans la methode SCRUM, si le client a opte pour AGILE, il doit **imperativement** se plier a minima aux evenements prevus dans la methode.

Bien s'accorder sur les moyens (canaux, convocation, calendrier) pour fluidifier le processus

![](https://i.imgur.com/lN8HL5e.png)

# Executing in Predictive/Classic Project Management
Baseline to control

<div class="alert alert-success" role="alert" markdown="1">
In predictive just follow the plan but lot of unexpected events
</div>
Mettre en place un cadre de communication pour controler le dev du projet

## Exemple de plan de communication
![](https://i.imgur.com/Y8lcHQg.png)

* Formalisez le plan de communication
* Faites approuver par le clien
* Planifier la logistique des evenements de com (placer les RDV, format, diffusion des comptes rendus...)

# Internal review meetings - Reunions de suivi internes
## Analysing delays in Gantt Chart
![](https://i.imgur.com/ZUGsxVV.png)

## Change Management
![](https://i.imgur.com/1DBZjBV.png)

# Plan & Execute/control
<div class="alert alert-info" role="alert" markdown="1">
Individual project risk an uncertain event or condition that, if it occurs, has a positive or negative effect on one or more project objectives
</div>

La methode pour les risques:
![](https://i.imgur.com/BGTEzC4.png)

Liste de risques possibles:
![](https://i.imgur.com/rXl6RpI.png)

## Analyse qualitative
![](https://i.imgur.com/xNF8osZ.png)

On manage en priorite les risques a plus haut impact
![](https://i.imgur.com/C0VMFNn.png)
Dans ce cas le rouge et noir, en bleu on ignore, en jaune on regarde un peu en details

## Risk Response Strategy
* Accept
    * Acknowledge the existence of a threat but no proactive action is taken
* Avoid
    * Risk response is to eliminate the threat by appropriate action
* Transfer
    * Risk is transfered to a third party that will accept the risk and the potential impact
* **Mitigate**
    * Action is taken to **reduce** the probability and/or impact of a threat

<div class="alert alert-danger" role="alert" markdown="1">
En resume,
* Identifiez les risques qui peuvent affecter le projet
* Filtrez pour ne conserver que les plus significatifs
* Definir des strategies et des plans d'action pour les risques retenus
</div>