---
title:          "SOCRA : Cours du 15 mai"
date:           2020-05-15 10:00
categories:     [S6, electif, SOCRA]
tags:           [S6, SOCRA, electif]
math: true
---

# Working with others
* Avoid : 
    * missing code files
    * ugly code naming
    * code deletion
* Anticipate problems
* Rules are required
    * Coding style
    * Code reviewal
    * Automated process

# Software Craftmanship Basics
* Quality : clean code, refactoring, tests, simple design
* Humility : question yourself, countinously improvement
* Sharing : pair programming, collective ownership of source code
* Pragmatism : understand constraint, adapt !
* Professionalism : treat your client as a partner

# Design patterns
## What is a design pattern ?
<div class="alert alert-info" role="alert" markdown="1">
A general, reusable solution to a commonly occurring problem within a given context in software design.
</div>

## GoF : 24 patterns
<div class="alert alert-info" role="alert" markdown="1">
* **Creational**
    * Builder, *Factory Method*, Abstract factory, Prototype, *Singleton*
* **Structural**
    * *Adapter*, Bridge, Composite, *Decorator*, Facade, Flyweight, Proxy, Delegation
* **Behavioral**
    * Chain of responsability, Command, Interpreter, Iterator, Mediator, Memento, *Observer*, State, *Strategy*, Template method, *Visitor* 
</div>

# Design patterns Creational
## The singleton
<div class="alert alert-info" role="alert" markdown="1">

**Restricts the instanciation** of a class to **one** object.
</div>

| Singleton                                      |
| ---------------------------------------------- |
| - Singleton : Singleton                        |
| - Singleton() <br> + getInstance() : Singleton |


```java=
public class Singleton {
    private static readonly Singleton instance = new Singleton();
    
    private Singleton() { }
    
    public static Singleton Instance() {
        return instance;
    }
}
```
<div class="alert alert-warning" role="alert" markdown="1">
This is a thread-safe implementation.
</div>

## Factory method
<div class="alert alert-info" role="alert" markdown="1">
**Creating objects without** having to **specify** the exact **class** of the object that will be created.
</div>
![](https://i.imgur.com/NKb1UH1.png)
```java=
interface IFruit {
    int Price { get; }
}

class Cherry : IFruit {
    public int Price { get; } = 75;
}

class Apple : IFruit {
    public int Price { get; } = 100;
}

class Banana : IFruit {
    public int Price { get; } = 150;
}

enum FruitType {
    Banana,
    Apple,
    Cherry
}
```
```java=
class FruitFactory {
    private Dictionary<FruitType, Func<IFruit>> mapper;
    
    public FruitFactory() {
        mapper = new Dictionary<FruitType, Func<IFruit>> {
            {FruitType.Apple, () => new Apple()},
            {FruitType.Banana, () => new Banana()},
            {FruitType.Cherry, () => new Cherry()}
        };
    }
    
    public IFruit Create(FruitType type) {
        if (!mapper.TryGetValue(type, out var result)) {
            throw new Exception("No fruit with type {type}");
        }
        return result();
    }
}
```

# Design Patterns Structural
## Adapter (aka Wrapper)
<div class="alert alert-info" role="alert" markdown="1">
**Allows** the **interface** of an existing class **to be used** as **another** interface.
</div>
![](https://i.imgur.com/1j4mxzy.png)
```java=
interface IOAdapter {
    String Read();
    void Write(String message);
}

class ConsoleAdapter : IOAdapter {
    public String Read() {
        return Console.Readline();
    }
    
    public void Write(String message) {
        Console.WriteLine(message);
    }
}
```

## Decorator
<div class="alert alert-info" role="alert" markdown="1">
Allows behavior to be added to an individual object, either statically or dynamically, without affecting the behavior of other objects from the same class.
</div>
![](https://i.imgur.com/UIEQvpi.png)

```java=
public interface IBananaDecorator : IFruit {
    Banana Banana { get; }
}

public class HandOfBanana : IBananaDecorator {
    const int factor = 4;
    
    public HandOfBanana(Banana banana)
    {
        Banana = banana;
    }
    
    public int Price => Banana.Price * factor;
    
    public Banana Banana { get; }
    
    public int Accept(IFruitVisitor fruitVisitor)
    {
        return Banana.Accept
        (fruitVisitor) * factor;
    }
}
```

# Design Patterns Behavioural
## Visitor
<div class="alert alert-info" role="alert" markdown="1">
A way of **separating an algorithm from an object** structure on which it operates.
</div>

![](https://i.imgur.com/nd0rkY2.png)

```java=
public interface IFruit {
    int Price { get; }
    int Accept(IFruitVisitor fruitVisitor);
}

public class Cherry : IFruit {
    public int Price { get; } = 75;
    
    public int Accept(IFruitVisitor fruitVisitor) {
        return fruitVisitor.Apply(this);
    }
}
```
```java=
public interface IFruitVisitor {
    int Apply(Cherry fruit);
    int Apply(Banana fruit);
    int Apply(Apple fruit);
}
```
```java=
internal class CherryPromotion : IFruitVisitor {
    private int count;
    
    public int Apply(Apple fruit) {
        return fruit.Price;
    }
    
    public int Apply(Banana fruit) {
        return fruit.Price;
    }
    
    public int Apply(Cherry fruit) {
        var reduction = 0;
        count++;
        if (count % 2 == 0) {
            reduction = -20;
        }
        return fruit.Price + reduction;
    }
}
```

## Observer
<div class="alert alert-info" role="alert" markdown="1">
An object, called the **subject**, maintains a **list of its dependents**, called **observers**, and **notifies them automatically** of any state **changes**, usually by calling one of their methods.
</div>
![](https://i.imgur.com/TvBWrfQ.png)
```java=
public interface IObservableBasket
{
    void Register(IBasketObserver observer);
    void Add(IFruit fruit);
}
```
```java=
public class ObservableBasket : IObservableBasket
{
    List<IFruit> list = new List<IFruit>();
    private readonly List<IBasketObserver> observers = ...
    
    public void Register(IBasketObserver observer) {
        observers.Add(observer);
    }
    
    public void Add(IFruit fruit) {
        list.Add(fruit);
        Notify(fruit);
    }
    
    private void Notify(IFruit fruit) {
        foreach (var observer in observers) {
            observer.Notify(fruit);
        }
    }
}
```
```java=
public interface IBasketObserver
{
    void Notify(IFruit fruit);
}

class BasketLogger : IBasketObserver
{
    public void Notify(IFruit fruit)
    {
        ConsoleAdapter.Instance.Write($"Item added : “
        + fruit.GetType().Name);
    }
}
```

## Strategy
<div class="alert alert-info" role="alert" markdown="1">
Enables selecting an algorithm at runtime.
</div>

![](https://i.imgur.com/aWNEFCm.png)

```java=
public class CherryForStrategy : Cherry
{
    public CherryForStrategy(IPriceStrategy strategy)
    {
        Strategy = strategy;
    }
    public IPriceStrategy Strategy { get; set; }
    public override int Price => Strategy.Apply(base.Price);
}
```
```java=
public interface IPriceStrategy
{
    int Apply(int defaultPrice);
}

public class SecondAtHalfPrice : IPriceStrategy
{
    private int count;
    
    public int Apply(int defaultPrice)
    {
        var reduction = 0;
        count++;
        if (count % 2 == 0)
        {
            reduction = -20;
        }
        return defaultPrice + reduction;
    }
}
```

# Organize your time
## Get Things Done
1. Capture / collect
2. Clarify / process
3. Organize
4. Reflect / plan
5. Engage / do

## Pomodoro
1. Focus on one task during 25 min
2. Take a break 5 min
3. Repeat 3 or 4 times
4. Take a break 20 min

## Eisenhower matrix
![](https://i.imgur.com/RA9PXe7.png)

# Organize your code
## Version control system
![](https://i.imgur.com/b3y4gOZ.png)

|VCS|Revision|Mode|
|---|--------|----|
|CVS|Per file|Client-server|
|SVN|Per commit|Client-server|
|GIT|Per commit|Distributed|

## Branching modes
* How many productions versions ?
* How many developers ?
* Which development process ?

### Feature
![](https://i.imgur.com/HKBZKIy.png)

### Release
![](https://i.imgur.com/J8SiYme.png)

# Organize your learning
## Train yourself
* Monitory technology
* Try them : POC
* Be careful of the silver bullet syndrome

## Train with others
* Coding dojo / Kata
* Pair programming
* Code reviews