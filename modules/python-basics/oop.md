# OOP - Classes & Objects

![image.png](/images/oop1.png)

### **Introduction to Object-Oriented Programming (OOP)**

- **Explanation**:
    - Introduce the concept of OOP and explain that it's a programming paradigm based on the concept of "objects" which can contain data (attributes) and code (methods).
    - Mention the four main principles of OOP: Encapsulation, Abstraction, Inheritance, and Polymorphism.

**Object-Oriented Programming (OOP)** is like organizing things in a way that makes them easy to understand and work with. Imagine you have a collection of things like toys. Each toy has a name, a color, and things it can do, like make a sound or move. In OOP, we group these details and actions together into something we call an "object."

### **Key Ideas of OOP**

1. **Encapsulation**:
    - **What It Is**: Think of encapsulation as putting all the important parts of a toy (like its color, size, and how it works) inside a box. The box keeps everything together and safe, so you can play with the toy without worrying about how it works inside.
    - **Example**: Imagine a `Dog` object. It has details like the dog's name and breed, and actions it can do, like `bark` or `sit`. All of this is wrapped up in one neat package—the `Dog` object.

![image.png](/images/oop2.png)

1. **Abstraction**:
    - **What It Is**: Abstraction is like a remote control for a toy car. You don’t need to know how the car's engine works; you just press the button, and it moves. Abstraction hides the complicated parts and only shows you what you need to use.
    - **Example**: When you use a `Dog` object and call the `bark()` action, you don’t need to know how the dog makes the barking sound—you just know it will bark when you ask it to.

![image.png](/images/oop3.png)

1. **Inheritance**:
    - **What It Is**: Inheritance is like having a family. Just like you might get your hair color from your parents, in programming, one object can inherit characteristics and behaviors from another.
    - **Example**: If we have a `Dog` object, we can create a `Puppy` object that automatically has everything a `Dog` has (like name and breed), but we can also add new things specific to puppies, like a `play()` action.

![image.png](/images/oop4.png)

1. **Polymorphism**:
    - **What It Is**: Polymorphism is a fancy way of saying that different toys can share the same name for an action, but the action might be a bit different for each toy.
    - **Example**: Both the `Dog` and `Puppy` objects can have a `bark()` action, but maybe the `Dog` barks loudly and the `Puppy` barks softly. Even though they both "bark," they do it in their own way.

![image.png](/images/oop5.png)

### **When Will We Use OOP?**

OOP is particularly useful in scenarios where:

1. **Complex Systems:**
    - When building large, complex systems like web applications, games, or simulations, OOP makes it easier to manage the codebase.
    - Example: A video game might have classes for `Player`, `Enemy`, and `Weapon`.
2. **Reusability Across Projects:**
    - If the functionality can be reused across multiple projects.
    - Example: A "Logger" class that records application logs can be reused in different projects.
3. **Extensibility:**
    - When your system is expected to grow or require frequent updates.
    - Example: An e-commerce system that may need to support new types of products or payment methods.
4. **Data-Driven Applications:**
    - When there are multiple related entities, and you want to group their properties and behaviors.
    - Example: A library system with classes like `Book`, `Member`, and `Librarian`.
5. **Long-Term Maintenance:**
    - For applications that need to be actively maintained or updated over time.
    - Example: A banking system where security updates and new features are regularly required.

### **What is The `__init__` method?**

- The `__init__` method in Python is a **special method** that is used to initialize an object when it is created. It is part of a class and is automatically called when an object (instance of the class) is instantiated. This method allows you to set up the initial state of an object by initializing its attributes with specific values.

### **What is `self`?**

- **Think of `self` as "this object"**: When you create an object from a class, `self` allows that object to refer to itself. It’s like saying, “this particular object I’m working with.”
- **Why do we need `self`?**: When you define methods in a class, you want those methods to work with the data (attributes) specific to the object that calls them. `self` lets you do that by linking the method to the object’s data.

### **2. Defining a Class**

- **Explanation**:
    - Explain what a class is: a blueprint for creating objects.
    - Introduce the `class` keyword.
- **Example 1: Basic Class Definition**
    
    ```python
    class Dog:
        def __init__(self, name, breed):
            self.name = name  # Attribute
            self.breed = breed  # Attribute
    
        def bark(self):  # Method
            print(f"{self.name} says Woof!")
    
    # Creating an object (instance) of the class
    my_dog = Dog("Buddy", "Golden Retriever")
    print(my_dog.name)  # Output: Buddy
    my_dog.bark()       # Output: Buddy says Woof!
    
    ```
    
- **Example 2: More Complex `__init__()`**
    
    ```python
    class Car:
        def __init__(self, make, model, year):
            self.make = make
            self.model = model
            self.year = year
    
        def start_engine(self):
            print(f"The {self.year} {self.make} {self.model}'s engine is now running!")
    
    my_car = Car("Tesla", "Model S", 2022)
    print(my_car.make)  # Output: Tesla
    my_car.start_engine()  # Output: The 2022 Tesla Model S's engine is now running!
    
    ```
    

### **4. Class Attributes vs. Instance Attributes**

### **Class Attributes**

- **Shared by all instances**: Defined at the class level, outside any method.
- **Same value for all objects**: Changing it affects all instances.

### **Instance Attributes**

- **Unique to each instance**: Defined using `self` inside methods like `__init__`.
- **Independent value per object**: Changing one doesn’t affect others.

### Examples

- **Example : Class Attribute**
    
    ```python
    class Circle:
        pi = 3.14159  # Class attribute
    
        def __init__(self, radius):
            self.radius = radius  # Instance attribute
    
        def area(self):
            return Circle.pi * (self.radius ** 2)
    
    circle1 = Circle(5)
    print(circle1.area())  # Output: 78.53975
    ```
    
- **Example**: **Instance Attributes**
    
    ```python
    class Car:
        def __init__(self, color):
            self.color = color  # Instance attribute
    
    car1 = Car("Red")
    car2 = Car("Blue")
    
    print(car1.color)  # Red
    car1.color = "Green"
    print(car2.color)  # Blue (unchanged)
    ```
    

### **5. Methods in Classes**

- **Explanation**:
    - Describe methods as functions that are defined inside a class and can operate on the object’s attributes.
- **Example 4: Defining Methods**
    
    ```python
    class Book:
        def __init__(self, title, author, pages):
            self.title = title
            self.author = author
            self.pages = pages
    
        def description(self):
            return f"{self.title} by {self.author} is {self.pages} pages long."
    
    my_book = Book("1984", "George Orwell", 328)
    print(my_book.description())  # Output: 1984 by George Orwell is 328 pages long.
    ```
    

### **6. Inheritance**

- **Explanation**:
    - Inheritance allows one class (child) to reuse the properties and methods of another class (parent), enabling code reuse and hierarchy creation. The child class can also extend or override the parent’s functionality to provide specialized behavior.
- **Example 5: Basic Inheritance**
    
    ```python
    class Animal:
        def __init__(self, name):
            self.name = name
    
        def speak(self):
            pass  # To be defined in child classes
    
    class Dog(Animal):
        def speak(self):
            return f"{self.name} says Woof!"
    
    class Cat(Animal):
        def speak(self):
            return f"{self.name} says Meow!"
    
    my_dog = Dog("Buddy")
    my_cat = Cat("Whiskers")
    print(my_dog.speak())  # Output: Buddy says Woof!
    print(my_cat.speak())  # Output: Whiskers says Meow!
    ```
    

- The `super()` method in Python is used to call a method from the parent (or superclass) in a child (or subclass). It is often used to extend or override parent class methods while still accessing the original functionality of the parent.

### **Key Points About `super()`**

1. **Access Parent Methods:**
    - `super()` allows you to call methods from the parent class directly, even if they are overridden in the child class.
2. **Used in Inheritance:**
    - It’s commonly used to initialize the parent class in the child class’s `__init__` method.

### **Exercise: Vehicles and Inheritance**

### **Objective:**

Students will create a base class called `Vehicle` and then create subclasses for specific types of vehicles, like `Car` and `Bicycle`, to understand how inheritance works.

### **Steps:**

1. **Create the `Vehicle` Base Class:**
    - This class will have attributes that are common to all vehicles, like `make`, `model`, and `year`.
    - It will also have a method `start()` that prints a message indicating the vehicle is starting.
    
    ```python
    class Vehicle:
        def __init__(self, make, model, year):
            self.make = make
            self.model = model
            self.year = year
    
        def start(self):
            print(f"The {self.make} {self.model} is starting.")
    ```
    
2. **Create the `Car` Subclass:**
    - The `Car` class will inherit from `Vehicle`.
    - Add an additional attribute for `number_of_doors`.
    - Override the `start()` method to include a specific message for cars.
    
    ```python
    class Car(Vehicle):
        def __init__(self, make, model, year, number_of_doors):
            super().__init__(make, model, year)
            self.number_of_doors = number_of_doors
    
        def start(self):
            print(f"The {self.make} {self.model} car with {self.number_of_doors} doors is starting.")
    ```
    
3. **Create the `Bicycle` Subclass:**
    - The `Bicycle` class will also inherit from `Vehicle`.
    - Add an additional attribute for `type_of_bike` (e.g., "mountain bike," "road bike").
    - Override the `start()` method to include a specific message for bicycles.
    
    ```python
    class Bicycle(Vehicle):
        def __init__(self, make, model, year, type_of_bike):
            super().__init__(make, model, year)
            self.type_of_bike = type_of_bike
    
        def start(self):
            print(f"The {self.make} {self.model} bicycle (a {self.type_of_bike}) is ready to ride.")
    
    ```
    
4. **Test the Inheritance:**
    - Create instances of `Car` and `Bicycle` and call their `start()` methods.
    
    ```python
    pythonCopy code
    my_car = Car("Toyota", "Corolla", 2022, 4)
    my_bike = Bicycle("Giant", "Escape 3", 2021, "road bike")
    
    my_car.start()  # Output: The Toyota Corolla car with 4 doors is starting.
    my_bike.start()  # Output: The Giant Escape 3 bicycle (a road bike) is ready to ride.
    ```
    

### **Example: BankAccount Class Demonstrating Encapsulation**

Let’s break down the provided example to illustrate how encapsulation works:

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.__balance}")
        else:
            print("Insufficient funds.")
```

### **Explanation of the Code:**

1. **Private Attribute (`__balance`):**
    - In this `BankAccount` class, the `balance` attribute is prefixed with double underscores (`__balance`). This is Python’s way of indicating that `balance` is meant to be private, meaning it cannot be accessed directly from outside the class.
    - This encapsulation of the `balance` attribute ensures that the balance can only be modified through the methods provided (`deposit` and `withdraw`), which control how the balance is updated.
2. **Public Methods (`deposit` and `withdraw`):**
    - The `deposit` and `withdraw` methods are public methods that allow interaction with the `__balance` attribute in a controlled manner. These methods ensure that only valid operations are performed (e.g., you can’t deposit a negative amount or withdraw more than the available balance).
    - These methods also provide feedback to the user about the current state of the balance after each operation, but they do so without exposing the balance directly.
3. **Usage Example:**
    - When `account.deposit(1000)` is called, the method checks that the amount is positive, adds it to the `__balance`, and prints the new balance.
    - When `account.withdraw(500)` is called, the method checks that there are sufficient funds before subtracting the amount and printing the new balance.
    
    ```python
    my_bank_account = BankAccount("Dor")
    print(my_bank_account.__balance)
    my_bank_account.deposit(700)
    my_bank_account.withdraw(700)
    
    ```
    

### **How This Demonstrates Encapsulation:**

- **Encapsulation** is shown here by the way `__balance` is hidden from direct access, ensuring that all interactions with the balance are done through the `deposit` and `withdraw` methods. This protects the balance from being accidentally or maliciously modified.
- **Abstraction** is also at play because users of the `BankAccount` class don’t need to know how the balance is managed internally; they just need to know how to deposit and withdraw money.

### **Key Takeaways:**

- **Encapsulation** keeps the internal state of an object safe by hiding its attributes and only allowing controlled access through methods.
- **Abstraction** simplifies the use of objects by hiding complex details and exposing only what’s necessary for interaction.

## **Polymorphism**

**Polymorphism** is a key concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. It enables a single interface (like a method) to work with different types of data or objects. This means you can call the same method on different objects, and each object will respond in its own way, even though the method name is the same.

### **Simple Explanation:**

- **Polymorphism** allows you to define a method in a parent class and then override it in child classes. Despite having the same method name, each child class can implement it differently.
- It’s like having a universal command that can be understood and executed differently by different types of objects.

### **Example: Polymorphism in Action with the `speak` Method**

Here’s how the provided example demonstrates polymorphism:

```python
class Bird:
    def speak(self):
        return "Tweet!"

class Dog:
    def speak(self):
        return "Woof!"

def animal_speak(animal):
    print(animal.speak())

bird = Bird()
dog = Dog()

animal_speak(bird)  # Output: Tweet!
animal_speak(dog)   # Output: Woof!

```

### **Explanation of the Code:**

1. **Classes with a Common Interface:**
    - **`Bird` Class:** This class has a method `speak()` that returns the sound a bird makes, which is `"Tweet!"`.
    - **`Dog` Class:** Similarly, this class also has a `speak()` method, but it returns `"Woof!"`, the sound a dog makes.
    
    Even though both classes have a `speak()` method, each one provides a different implementation. This is a key aspect of polymorphism—different objects can have methods with the same name but behave differently.
    
2. **The `animal_speak` Function:**
    - This function takes an `animal` as a parameter and calls its `speak()` method.
    - Because of polymorphism, you can pass either a `Bird` object or a `Dog` object to this function, and it will correctly call the `speak()` method of the appropriate class.
3. **Using Polymorphism:**
    - When `animal_speak(bird)` is called, it prints `"Tweet!"` because the `bird` object is an instance of the `Bird` class, so the `Bird` class’s `speak()` method is used.
    - When `animal_speak(dog)` is called, it prints `"Woof!"` because the `dog` object is an instance of the `Dog` class, so the `Dog` class’s `speak()` method is used.
    
    ```python
    bird = Bird()
    dog = Dog()
    
    animal_speak(bird)  # Output: Tweet!
    animal_speak(dog)   # Output: Woof!
    ```
    

### **How This Demonstrates Polymorphism:**

- **Polymorphism** is shown by the `animal_speak` function's ability to handle different types of animals (like a `Bird` or a `Dog`) without knowing their specific class. The function can call the `speak()` method on any object that has it, and the correct method for that specific object is executed.
- This makes the code more flexible and easier to extend. You could add more classes with their own `speak()` method (like `Cat`, `Cow`, etc.), and `animal_speak` would still work with them without any changes.

### **9. Practical Exercises**

- **Exercise 1**: Create a class `Student` with attributes for name and grades. Add a method to calculate the average grade.
    
    ```python
    class Student:
        def __init__(self, name, grades):
            self.name = name
            self.grades = grades
    
        def average_grade(self):
            return sum(self.grades) / len(self.grades)
    
    student1 = Student("John", [90, 85, 92])
    print(f"{student1.name}'s average grade: {student1.average_grade()}")  # Output: John's average grade: 89.0
    
    ```
    
- **Exercise 2**: Create a class `Rectangle` with attributes for width and height, and methods to calculate the area and perimeter.
    
    ```python
    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
    
        def area(self):
            return self.width * self.height
    
        def perimeter(self):
            return 2 * (self.width + self.height)
    
    rect = Rectangle(4, 5)
    print(f"Area: {rect.area()}")         # Output: Area: 20
    print(f"Perimeter: {rect.perimeter()}")  # Output: Perimeter: 18
    
    ```
    
- **Exercise 3**: Create a base class `Shape` and two derived classes `Circle` and `Rectangle`. Implement methods to calculate the area for each shape.
    
    ```python
    class Shape:
        def area(self):
            pass
    
    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius
    
        def area(self):
            return 3.14159 * self.radius ** 2
    
    class Rectangle(Shape):
        def __init__(self, width, height):
            self.width = width
            self.height = height
    
        def area(self):
            return self.width * self.height
    
    shapes = [Circle(5), Rectangle(4, 6)]
    for shape in shapes:
        print(f"Area: {shape.area()}")
    # Output:
    # Area: 78.53975
    # Area: 24
    ```
    

### 

### Disclaimer !

As a **DevOps Engineer**, you may not use **Object-Oriented Programming (OOP)** as extensively as software developers, but there are specific situations where OOP principles can be very beneficial. Here are scenarios where OOP is commonly used in DevOps: