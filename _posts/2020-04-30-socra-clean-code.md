---
title:          "SOCRA : Cours du 30 avril"
date:           2020-04-30 10:00
categories:     [S6, electif, SOCRA]
tags:           [S6, SOCRA, electif]
math: true
---
# Clean code, what is it ?
## What is your pain ?
* Bugs ?
    * Not cool when a client find a bug
* Coding style ?
    * Having a bad coding style
* Working with others ?
    * Coordinating actions

## Developer life...
<div class="alert alert-danger" role="alert" markdown="1">
Never thanked, only complaints !
</div>

By code : 
* Compilation failed
* Seg fault
* Stack overflow

By client : 
* ASAP
* Bad UX
* Not working

## ...is awesome !
* We create products
* We discover new trades
* We learn !

# Software craftmanship manifesto
<div class="alert alert-info" role="alert" markdown="1">
Not only working software, but also **well-crafted software**.
Not only responding to change, but also **steadily adding value**.
Not only individuals and interactions, but also **a community of professionals**.
Not only customer collaboration, but also **productive partnership**.
</div>

## Technical debt impact
* Code readbility
* New features development
* Bug fixing

## Be...
<div class="alert alert-info" role="alert" markdown="1">
* KISS : Keep It Simple Stupid
* DRY : Don't Repeat Yourself
* Focused 
    * YAGNI : You Ain't Gonna Need It
* DIE : Duplication Is Evil ~~plz don't actually die~~
    * Copy/paste is easy but hard to bug fix
</div>

## Simple rules
Bugs are everywhere : one operation per line helps you identify the location

<div class="alert alert-warning" role="alert" markdown="1">
```java=
list.Add(line.WordToString());
```
</div>

become : 
<div class="alert alert-success" role="alert" markdown="1">
```java=
var words = line.WordToString();
list.Add(words);
```
</div>


Do not ask twice for the same thing, it improves your system perfs
<div class="alert alert-warning" role="alert" markdown="1">
```java=
Foo(lines.Where(l => l.section == null).ToArray());
Bar(lines.Where(l => l.section == null).ToArray(), lines);
```
</div>

become : 
<div class="alert alert-success" role="alert" markdown="1">
```java=
var linesWithSection = lines.Where(l => l.section == null).ToArray();
Foo(linesWithSection);
Bar(linesWithSection, lines);
```
</div>


<div class="alert alert-danger" role="alert" markdown="1">
Everytime ask yourself : *Sould I be able to understand my code in 6 months ? One year ?*
</div>
* Use explicit names
* Read your code
* Code phrases

# How ?
## OO Principles
* Encapsulation
* Inheritance
* Polymorphism
    * Overloading
    * Templates / Generics
    * Subtypings

## S.O.L.I.D. ~~Snake~~
* SRP : Single Responsibility Principle
* OCP : Open/closed principle
* LSP : Liskov Substitution Principle
* ISP : Interface Segregation Principle
* DIP : Dependency Inversion Principle

## Single Responsibility Principle
*A class should have only one reason to change.*
<div class="alert alert-warning" role="alert" markdown="1">
```javascript=
public class Person {
    public String Name { get; set; }
    public String Email { get; set; }
    
    public Person(String Name, String email)
    {
        Name = name;
        Email = email;
        ValidateEmail();
    }
    
    private void ValidateEmail()
    {
        // throw if not an email
    }
}
```
</div>
<div class="alert alert-success" role="alert" markdown="1">
```java=
public class Person
{
    public String name { get; set; } 
    public Email Email { get; set; }
}

public class Email
{
    public String Adress { get; private set; }
    
    public Email(String address)
    {
        Address = address;
        ValidateEmail();
    }
    
    private void ValidateEmail()
    {
        // throw if not an email
    }
}
```
</div>

## Open/Close Principle
*Software entities should be open for extension, but closed for modification.*
<div class="alert alert-warning" role="alert" markdown="1">
```javascript=
public class Greeter {
    String formality;
    
    public String Greet() {
        if (this.formality == "formal") {
            return "Good evening, sir.";
        } else if (this.formality == "casual") {
            return "Sup bro?";
        } else if (this.formality == "intimate") {
            return "Hello Darling!";
        } else {
            return "Hello.";
        }
    }
    
    public void SetFormality(String formality) {
        this.formality = formality;
    }
}
```
</div>
<div class="alert alert-success" role="alert" markdown="1">
```java=
public class Greeter {
    private Personality personality;
    
    public Greeter(Personality personality) {
        this.personality = personality;
    }
    
    public String greet() {
        return this.personality.greet();
    }
}
```
</div>

## Liskov Substitution Principle
<div class="alert alert-danger" role="alert" markdown="1">
If $S$ is a subtype of $T$, then objects of type $T$ in a program may be replaced with objects of type $S$ without altering any of the desirable properties of that program.
</div>
## Interface segregation principle
*Many client-specific interfaces are better than one general-purpose interface.*

## Dependency Injection Principle
*One should "depend upon abstractions, not concretions".*
<div class="alert alert-warning" role="alert" markdown="1">
```java=
public class FileLogger {
    public void Info(String message) {
        // Write message into a file
    }
}

public class Application {
    private FileLogger logger;
    
    public Application() {
        this.logger = new FileLogger();
    }
    
    public void Run() {
        logger.Info("Running");
    }
}
```
</div>
<div class="alert alert-success" role="alert" markdown="1">
```java=
public class FileLogger : ILogger {
    public void Info(String message) {
        // Write message onto a file
    }
}

public class Application {
    private ILogger logger;
    
    public Application(ILogger logger) {
        this.logger = logger();
    }
    
    public void Run() {
        logger.Info("Running");
    }
}
```
</div>

# Be Agile
## V Cycle
![](https://i.imgur.com/eOKmk7c.png)

## Agile
![](https://i.imgur.com/3F4JzhU.png)

![](https://i.imgur.com/a0MWMoL.png)

## SCRUM 
### Methodology
* Product owner
* Scrum master
* Developer team
* Backlog

### Workflow
* Sprint Meeting Planning
    * Plan what needs to be done for the next version
* Daily Scrum Meeting
    * where are we at
* Sprint Retrospective
    * what is well done, what is not, etc.

![](https://i.imgur.com/NdyXimB.png)

## KANBAN
Tickets per action
![](https://i.imgur.com/KFEKdWu.png)

# Think tests
## Why do we test ?
* Tests to help understand requirements
* Tests protects future developments
* Tests are a fall protection
* We are human after all

## How do we test ?
<div class="alert alert-danger" role="alert" markdown="1">
We create code to test our code.
</div>
* **Unit Test :** Focus on ONE function usage, mock dependencies
* **Integration Test :** Crosses the boundary between components
* **Behaviour Test :** An example of the user using the system

## The test pyramid
![](https://i.imgur.com/cuCjAtC.png)

## TDD : Test Driven Development
No code without a test
1. Write a test which fails
2. Write the code which fulfil the test
3. Refactor source code (feature and test !)

## What is a good unit test ?
* Easy to understanf, clear when it fails
* Determinist
* Focused
* AAA : Arrange / Act / Assert

## BDD : Behaviour Driven Development
<div class="alert alert-info" role="alert" markdown="1">
A simple test :  **Given......When.......Then.......**
* **Given** a user with an account
* **When** he tries to create a new account with existing account credentials
* **Then** it must be logged in with the existing account
</div>

## The double loop
![](https://i.imgur.com/Tqx0OPp.png)

## Test coverage
<div class="alert alert-danger" role="alert" markdown="1">
A 100% covergae is not a bug-free code.
</div>
