# Inheritance & Polymorphism

![image.png](/images/oop6.png)

### Inheritance in Python

**Inheritance** is a core concept of Object-Oriented Programming (OOP) that allows a class (child or derived class) to inherit attributes and methods from another class (parent or base class). This promotes code reuse and modularity.

### Key Points:

- The child class inherits all the attributes and methods of the parent class.
- The child class can also have its own additional attributes and methods.
- The child class can **override** the methods of the parent class.

### Example of Inheritance:

```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

# Another child class inheriting from Animal
class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."

# Using the classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Output: Buddy barks.
print(cat.speak())  # Output: Whiskers meows.
```

---

### Polymorphism in Python

**Polymorphism** allows objects of different classes to be treated as objects of a common superclass. This means a method with the same name can behave differently depending on the object that calls it. It emphasizes the concept of "one interface, multiple implementations."

### Key Points:

- Achieved using method overriding and dynamic method resolution.
- Promotes flexibility and makes code easier to extend.

### Example of Polymorphism:

```python
# Parent class
class Animal:
    def speak(self):
        return "This animal makes a sound."

# Child classes overriding the speak method
class Dog(Animal):
    def speak(self):
        return "Dog barks."

class Cat(Animal):
    def speak(self):
        return "Cat meows."

# Polymorphic behavior
def animal_sound(animal):
    print(animal.speak())

# Different objects passed to the same function
dog = Dog()
cat = Cat()

animal_sound(dog)  # Output: Dog barks.
animal_sound(cat)  # Output: Cat meows.

```

---

### Explaining the Difference

1. **Inheritance** is about creating a hierarchy of classes where a child class derives properties and behaviors from a parent class.
    - Example: Dog and Cat are specific types of Animal.
2. **Polymorphism** is about using a unified interface to interact with objects of different types.
    - Example: Both Dog and Cat can "speak," but their behavior differs based on their specific implementation.