# SOCRA : cours du 04 / 06

## GoF : 24 patterns
:::info
* **Creational**
    * Builder, *Factory Method*, Abstract factory, Prototype, *Singleton*
* **Structural**
    * *Adapter*, Bridge, Composite, *Decorator*, Facade, Flyweight, Proxy, Delegation
* **Behavioral**
    * Chain of responsability, Command, Interpreter, Iterator, Mediator, Memento, *Observer*, State, *Strategy*, Template method, *Visitor* 
:::

## Organize your time
* Get Things Done
* Pomodoro

## Organize your code
* Version Control System (VCS)
* Branching : feature / release

## Organize your learning
* Monitor technology
* POC
* Coding dojo / Kata
* Pair programming

# IT in company
## Software needs
* Software
* Apache
* Monitoring
* Linux
* Network

## Classic segregation ~~*it's not what you think*~~
| IT-Development | IT-Production | IT-System |
|----- | ------- | --------- |
| Develop software | Manage software in production | Manage hardware and OS+ |
|  | Assist users | Handles DPR |
| Paid for new features | Paid for uptime | Paid for stability, security |
![](https://i.imgur.com/NOM3TL2.png)

# Assume failures
:::danger
No software is guaranteed without bugs.
:::

## User error investigation
* Call support (Niveau 1)
* Use standard procedures (N1)
* Check logs (N2)
* Check configuration (N2)
* Call development : error in software (N3)

## Help them using
* Error messages
* Cristal clear logs

### Examples : Logs
```
Create new wish
Error returned
```
:::warning

With that kind of log, impossible to know what happened.
:::
```
2020-03-31 09:48:26.1539|INFO|0HLULB1T307F0|WishController|Create : New wish for #433 by #ce4ed122-3cfd-47cd-a8ea-9d0b9d4c55f4 : My Mobility
2020-03-31 09:48:26.1575|WARN|0HLULB1T307F0|WishController|HasOneNotNull - Property not found : LinkedID
2020-03-31 09:48:26.1577|WARN|0HLULB1T307F0|WishController|Error returned form HasOneNotNull : Property not found : LinkedId
```
:::success

With this kind of log, we see the error right away.
:::

## Logs
* Use different levels : Trace, Debug, Info, Warning, Error, Fatal
* Use and existing framework
* There is never too much logs

# From dev to PROD
![](https://i.imgur.com/MkzAWp5.png)

## CI/CD Quesaco
:::info
* Continous : forming an unbroken whole; without interruption
    * integration : the coodination of processes
    * delivery : delivering letters, packages.... babies...
    * deployement : bringing resources into effective action
:::

### CI process goal
Validate code at each steps, for each developers
Confirm software stability (a minimum)
Create a delivery workflow
Avoid human interaction

### How to go live
:::info
1. Take a (development) ticket
2. Develop using BDD, TDD (and pair programming)
3. Push on VCS
4. Deploy on a test environment
5. Test your software
6. Everything is OK, then deploy on production

Eventually calculate metrics like coverage, technical debt...
:::

### A software
![](https://i.imgur.com/cauOa40.png)


### Delivery process
1. Get sources
2. Add version
3. Build
4. Run tests
5. Publish components

### Environments
DEV, PROD, PRE-PROD, UAT

#### Create packages
1. Get sources
2. Add version
3. Build
4. Run tests
5. **Create one package for each components**

![](https://i.imgur.com/EwVdkaH.png)


### CI/DC Tools
:::info
* **Shell script!**
* Jenkins
* Travis CI
* Bamboo
* Teamcity
:::

## Monolyth
* AKA Single-tiered
* Self-contained
* Independant

## Multi-tier
* Layer separation
* Flexible

### 3-tier
| Presentation |
|--|
| Logic |
| Data |

#### Example
| *Console* : Get report|
|--|
| *Business Logic* : list of all sales and aggregate them |
| *Data : MySQL* : access sales' store |

## SOA : Service Oriented Architecture
:::info
A service : 
* represents a business activity
* is self contained
* is a black box for its consumers
* may consist of other underlying services
:::
![](https://i.imgur.com/FbbSbO5.png)

# Communication
## Local : IPC
|File|Shared Memory|
|----|----|
|Local - Bidirectional, one process at time for writing|Local - Bidirectional, one process at time for writing|

|Signal|Socket|
|----|---|
|Local - Unidirectional, not used for data|Local or netowrk - bidirectional, synchrone|

|Pipe|Message queue|
|----------|----------|
|Local - Unidirectional|Local or network - bidirectional, asynchrone|

## Problem..
:::warning
*What if a I send a message and the service is down ?*
*How to send a message which can be handled by multiples service, but only processed by one ?*
*How to handle a client deconnection ? A master ?*
:::

### Message queueing (aka MQ)
:::success
* Like a mailbox
* Increase TCP/IP features:
    * Durability - purging : is the message saved ? What is TTL ?
    * Delivery policy : should the message be delivered once more ?
    * Security : which applications should have the message ?
    * Notifications : the publisher can be notified when message is received
:::
Implementations : Apache ActiveMQ, OMQ, RabbitMQ, JMS, ...

# API
## CRUD
![](https://i.imgur.com/UBlEchs.png)
## REST
* CRUD operations
* Stateless
* On HTTP/S

VERB | Request has body| Response has body | Safe | Indempotent | Cacheable|
|----|-----------------|-------------------|------|-------------|----------|
|GET|Optional|YES|YES|YES|YES|
|POST|YES|YES|NO|NO|YES|
|PUT|YES|YES|NO|YES|NO|
|DELETE|NO|NO|NO|YES|NO|

```
/api/users
```
|GET|POST|PUT|DELETE|
|---|----|---|------|
|Retrieve all users|Create a new user|N/A|Delete all users|
```
/api/users/{id}
```
|GET|POST|PUT|DELETE|
|---|----|---|------|
|Retrieve one user|Create a new user|N/A|Delete one user|

## OpenData - OpenAPI
* Free to use, reuse and redistribute
* Lots of companies : GAFAM, RATP, gouvernements...
* Lots of domains : genetic, chemical, geographic, justice...
* Swagger ~~oh no it's 2010 again~~

## An SOA Software
![](https://i.imgur.com/wyJlGY2.png)

To manage more users : 
![](https://i.imgur.com/YvAlHfv.png)

# But there is still a problem..
## The current state problem
:::warning
*What did my user?*
*How can I guaranty it?*
*Can I prove it?*
:::
:::success
So let's think events!
:::
## Events afterall
|Item added|
|------|
|Item removed|
|Payment received|
|Order shipped|

1. Item added : book
2. Item added : DVD
3. Item removed : DVD
4. Payment received
5. Order shipped

## Events sourcing
* Command : user intention => AddItemToCart
* Event : happened in the past => ItemAddedToCart
    * Immutable
* Event store

## CQRS
Command and Query Responsibility Segregation
![](https://i.imgur.com/wE59hu0.png)

# Cloud
## How to run ?
* Software
* Libraries - dependencies
* Operating system
* **Hardware**

## I am a user
**I USE SERVICES!!!!**

## I'm a developer
* *Why should I care about hardware failure ?*
    * Infrastructure as a Service
* *Why must I update the operating system ?*
    * Platform as a service
* *Is the (right) JVM installed ?*
    * Platform as a service
* *I know nothing about SQL Server, I just want a database !*
    * Platform as a service / Software as a Service
* *ITO are against me !*

## IaaS to SaaS
![](https://i.imgur.com/Bnhwajw.png)

## Me or nothing
|Entreprise|Cloud provider|
|----------|--------------|
|On premise|Cloud|

Entreprise & cloud provider : **hybrid**


## Lambda functions
* One endpoint, one function
* Focus on objective
* Access defined resources
* Call other functions if 

# To conclude
## Software craftmanship
* Clean code, SOLID, Design pattern
* Methodologies
    * Technical : TDD, DDD
    * Organizational : agility, SCRUM, Kanban
* Mindset : (learn, fail, repeat,)$^n$ then succeed