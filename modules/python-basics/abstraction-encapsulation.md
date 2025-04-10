# Abstraction & Encapsulation

![image.png](/images/oop7.png){width=600px}

### Abstraction in Python

**Abstraction** is the concept of hiding the internal details of an object and exposing only the essential features. It allows you to focus on **what** an object does rather than **how** it does it. In Python, abstraction is typically achieved using **abstract classes** and **interfaces**.

### Key Points:

- Abstract classes cannot be instantiated directly.
- They define methods that must be implemented in derived classes.
- Use the `abc` (Abstract Base Class) module in Python to create abstract classes.

### **What is an Abstraction Class?**

In programming, an **abstraction class** is like a blueprint for other classes. It's a way of saying, "Here are some things that need to be done, but I'm not going to explain how to do them right now. You (the other classes) figure out the details."

An **abstraction class** usually has some **abstract methods**. These methods are like instructions without any specific details. Other classes that use this blueprint (called subclasses) must give the details of how these instructions should work.

### **Example:**

Imagine we have an abstract class called **Animal**. This class says that all animals must be able to make a sound and move, but it doesn't say how. It's up to each specific animal (like a dog or bird) to decide how to make a sound and how to move.

### Example of Abstraction:

```python
from abc import ABC, abstractmethod

# Abstract Class
class Animal(ABC):
    
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

# Subclass that inherits from Animal
class Dog(Animal):
    
    def sound(self):
        return "Bark"
    
    def move(self):
        return "Run"

# Subclass that inherits from Animal
class Lion(Animal):
    
    def sound(self):
        return "Roar"
    
    def move(self):
        return "Run"

# Creating objects of subclasses
dog = Dog()
print(dog.sound())  # Output: Bark
print(dog.move())   # Output: Run

lion = Lion()
print(lion.sound())  # Output: Chirp
print(lion.move())   # Output: Fly
```

### Explanation:

1. **Animal Class**: This is an abstract class. It has two abstract methods: `sound()` and `move()`. These methods don't have a body in the `Animal` class, so any subclass must provide its own implementation of these methods.
2. **Dog and Bird Classes**: These are subclasses of `Animal`. They inherit from `Animal` and implement the abstract methods `sound()` and `move()`.
3. **Instantiation**: You can't create an instance of the `Animal` class directly. However, you can instantiate `Dog` or `Bird`, as they provide implementations for all abstract methods.

### Benefits of Abstraction:

- **Simplifies the Interface**: By hiding the complex details, abstraction allows the user to interact with a simplified interface.
- **Enforces Structure**: Abstract classes enforce a structure for subclasses, ensuring that all subclasses implement necessary methods.
- **Flexibility and Extensibility**: You can add new subclasses that implement abstract methods without changing the code that uses the abstract class.

### In short:

- **Abstraction Class** = A blueprint with some instructions that others must follow.
- **Abstract Methods** = Instructions without details.
- **Subclasses** = They provide the details for those instructions.

### Example: **Vehicles**

Imagine we have an abstraction for **Vehicles**. All vehicles have the ability to **start** and **stop**, but how they start and stop may be different for each vehicle.

We’ll create an abstract class called **Vehicle** with two abstract methods: `start()` and `stop()`. Then, we’ll have different vehicles like **Car** and **Bike**, which will provide their own details of how they start and stop.

### Code Example:

```python
from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass  # No details, just an instruction

    @abstractmethod
    def stop(self):
        pass  # No details, just an instruction

# Subclass 1: Car
class Car(Vehicle):

    def start(self):
        return "Car is starting with a key turn!"

    def stop(self):
        return "Car is stopping with brake pedal!"

# Subclass 2: Bike
class Bike(Vehicle):

    def start(self):
        return "Bike is starting with a kickstart!"

    def stop(self):
        return "Bike is stopping by applying hand brake!"

# Create instances of the subclasses
car = Car()
print(car.start())  # Output: Car is starting with a key turn!
print(car.stop())   # Output: Car is stopping with brake pedal!

bike = Bike()
print(bike.start())  # Output: Bike is starting with a kickstart!
print(bike.stop())   # Output: Bike is stopping by applying hand brake!
```

### Breakdown:

1. **Vehicle (abstract class)**: This class says, "All vehicles must have a `start()` and `stop()` method," but it doesn’t give details about how to start or stop a vehicle.
2. **Car (subclass)**: The **Car** class provides the details for how it starts and stops (e.g., turning the key and using the brake pedal).
3. **Bike (subclass)**: The **Bike** class provides its own details for how it starts and stops (e.g., kickstarting and applying a hand brake).

### What Happens When We Run This Code:

- The abstract class **Vehicle** provides the structure (the methods `start()` and `stop()`), but it’s the **Car** and **Bike** classes that implement the actual behavior.
- You **cannot** create an instance of **Vehicle** directly because it doesn't have the full implementation of the methods (`start()` and `stop()`).
- The **Car** and **Bike** classes provide the specific implementations, so you can create objects of those classes and use their methods.

### In Short:

- **Abstraction** lets you define **what** should happen (like starting or stopping), but leaves the **how** up to the subclasses (like how a car or a bike actually starts or stops).
- It keeps your code **clean** and **organized**, while ensuring that each specific class handles its own behavior.

---

### Encapsulation in Python

**Encapsulation** is the concept of bundling the data (attributes) and methods (functions) that operate on the data into a single unit (class). It also restricts direct access to some of the object's components to enforce better control and security.

### Key Points:

- Encapsulation is implemented using **access modifiers**:
    - **Public** attributes/methods: Can be accessed from anywhere (default in Python).
    - **Protected** attributes/methods (`_attribute`): Indicate that an attribute is intended for internal use (convention only).
    - **Private** attributes/methods (`__attribute`): Cannot be accessed directly from outside the class.
- Use getter and setter methods to access and modify private attributes.

**Encapsulation** is one of the fundamental principles of Object-Oriented Programming (OOP). It refers to the concept of **bundling** the data (attributes) and methods (functions) that operate on that data into a single unit or class. It also involves restricting access to certain details of an object to protect its internal state from unintended modification. This is achieved using **access modifiers** (public, private, and protected) to control access to the attributes and methods of a class.

### Key Concepts of Encapsulation:

1. **Attributes (Data)**: Variables that store the state of an object.
2. **Methods (Functions)**: Functions that define the behavior of the object, i.e., how the data can be accessed or modified.
3. **Access Modifiers**: These are used to define the visibility of the attributes and methods:
    - **Public**: Can be accessed from anywhere.
    - **Private**: Cannot be accessed from outside the class. In Python, we make an attribute or method private by prefixing it with `__`.
    - **Protected**: Meant to be accessed only by the class and its subclasses. In Python, we use a single underscore (`_`) to denote protected members.

### Why Use Encapsulation?

- **Data Hiding**: Encapsulation helps in hiding the internal details of an object and only exposing what is necessary. This ensures the internal state of an object is protected from unintended interference.
- **Modularity**: Encapsulation promotes modularity by allowing objects to be treated as black boxes, where their internal workings don't affect other parts of the program.
- **Code Maintenance**: With encapsulation, you can change the internal implementation of a class without affecting other code that relies on it, as long as the public interface remains the same.

### Example of Encapsulation:

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner  # Public attribute
        self._balance = balance  # Protected attribute

    # Getter for the balance (read-only access)
    def get_balance(self):
        return self._balance

    # Setter for the balance (controlled modification)
    def set_balance(self, amount):
        if amount < 0:
            print("Balance cannot be negative!")
        else:
            self._balance = amount

    # Private method
    def __display_owner(self):
        return f"Account owned by {self.owner}"

# Using the class
account = BankAccount("Alice", 1000)

print(account.get_balance())  # Output: 1000
account.set_balance(500)      # Modifies the balance
print(account.get_balance())  # Output: 500

# Accessing protected attribute (allowed but discouraged)
print(account._balance)       # Output: 500

# Trying to access private method directly
# print(account.__display_owner())  # AttributeError
```

### **Explanation:**

1. **Private Attribute (`__balance`)**:
    - We used `__balance` to make the balance private. This means you can't directly access `__balance` from outside the class, so you cannot modify the balance directly.
2. **Public Methods (`deposit()`, `withdraw()`, `get_balance()`)**:
    - These methods allow controlled access to the balance. They provide functionality to deposit and withdraw money while ensuring that the balance remains valid.
    - **Deposit Method**: Adds money to the balance.
    - **Withdraw Method**: Deducts money from the balance, but checks if the balance is sufficient.
    - **Get Balance**: Returns the balance but doesn’t allow modification from outside.
3. **Encapsulation in Action**:
    - The **balance** is hidden inside the class (encapsulated) and can only be modified or accessed using the public methods.
    - You can’t directly change `account.__balance` from outside the class, which protects the internal state from unintended or invalid changes.

### Example: **Library System**

In this example, we will have a `Library` class with a private attribute `__book_count`. This count cannot be directly accessed or modified from outside the class. We’ll provide methods for adding and removing books in the library, ensuring that the book count can never go below zero.

### Code Example:

```python
class Library:
    def __init__(self, name, book_count=0):
        self.name = name               # Public attribute
        self.__book_count = book_count  # Private attribute (book count is encapsulated)

    # Public method to add books to the library
    def add_books(self, count):
        if count > 0:
            self.__book_count += count
            print(f"Added {count} books. Total books: {self.__book_count}")
        else:
            print("You must add a positive number of books.")

    # Public method to remove books from the library
    def remove_books(self, count):
        if 0 < count <= self.__book_count:
            self.__book_count -= count
            print(f"Removed {count} books. Total books: {self.__book_count}")
        else:
            print("Cannot remove more books than available or negative values.")

    # Public method to get the current book count (getter)
    def get_book_count(self):
        return self.__book_count

    # Public method to set a specific number of books (setter)
    def set_book_count(self, count):
        if count >= 0:
            self.__book_count = count
            print(f"Library book count set to: {self.__book_count}")
        else:
            print("Book count cannot be negative.")

# Create a Library instance
library = Library("City Library", 50)

# Add books to the library
library.add_books(20)

# Remove books from the library
library.remove_books(10)

# Try to set a valid book count
library.set_book_count(100)

# Try to access the private book count directly (This will give an error)
# print(library.__book_count)  # This will raise an AttributeError

# Access current book count using the getter
print(f"Current book count is: {library.get_book_count()}")
```

### Breakdown of the Code:

1. **Private Attribute (`__book_count`)**:
    - We use `__book_count` to make the number of books in the library private. This means it cannot be directly accessed or modified from outside the class, providing control over how the book count is updated.
2. **Public Methods (`add_books()`, `remove_books()`, `set_book_count()`, `get_book_count()`)**:
    - These methods allow controlled interaction with the private `__book_count` attribute.
        - `add_books(count)`: Adds a positive number of books.
        - `remove_books(count)`: Removes a positive number of books, ensuring it doesn’t go below zero.
        - `set_book_count(count)`: Allows setting a specific number of books, but it must be a non-negative value.
        - `get_book_count()`: Returns the current number of books.
3. **Encapsulation in Action**:
    - The **book count** is encapsulated inside the class. We use public methods to interact with it, which helps avoid invalid or unsafe changes (like removing more books than available).
    - You cannot directly access the `__book_count` from outside the class, ensuring that only valid actions are performed on the count.

### **Why Encapsulation Is Useful Here:**

- It **protects the data**: No one can accidentally change the number of books directly; they must go through the public methods.
- It **ensures data validity**: Only valid operations are allowed. For example, the system won’t let you remove more books than are available.
- It **promotes better maintenance**: If you need to change how the book count is managed in the future, you only need to change it inside the class, and everything else using the class remains unaffected.

---

### Explaining the Difference

1. **Abstraction** is about hiding the implementation details and focusing on the functionality.
    - Example: You know a `Rectangle` has an `area`, but you don’t worry about how it's calculated.
2. **Encapsulation** is about hiding the data and controlling access to it through methods.
    - Example: A bank account restricts direct access to the balance, ensuring it's only modified through defined methods.