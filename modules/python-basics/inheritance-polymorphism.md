# Inheritance & Polymorphism

![image.png](/images/oop6.png){width=600px}

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

### **Example with Multiple Inheritance:**

Python also supports **multiple inheritance**, where a child class can inherit from more than one parent class. Here’s an example:

```python
# Parent class 1
class Engine:
    def start_engine(self):
        print("Engine started.")

# Parent class 2
class Radio:
    def play_radio(self):
        print("Radio is playing.")

# Child class inheriting from both Engine and Radio
class CarWithRadio(Engine, Radio):
    def __init__(self, make, model):
        self.make = make
        self.model = model

# Creating an object of CarWithRadio
car = CarWithRadio("Honda", "Civic")
car.start_engine()  # Inherited from Engine
car.play_radio()    # Inherited from Radio
```

### **Explanation of Multiple Inheritance:**

- The `CarWithRadio` class inherits from both `Engine` and `Radio` classes.
- It can access methods from both parent classes, such as `start_engine()` from `Engine` and `play_radio()` from `Radio`.

### **Advantages of Inheritance:**

1. **Code Reusability**: You can reuse the methods and attributes from the parent class in the child class.
2. **Organization**: Inheritance helps organize your code better by allowing you to group related functionality together.
3. **Extensibility**: You can extend the functionality of a parent class in the child class, providing specific details or overriding methods.

---

## Super

The `super()` method in Python is a built-in function that allows you to call methods and constructors from a parent (or superclass) in a child (or subclass). It is primarily used in the context of **inheritance** to enable **method overriding** and **constructor inheritance**.

### **Why Use `super()`?**

- **Access Parent Class Methods**: It helps call methods from the **parent class** (superclass) without explicitly referring to the parent class by name.
- **Constructor Inheritance**: It allows a child class to **call the constructor** of its parent class and initialize the inherited attributes.
- **Avoid Code Duplication**: It promotes **code reuse** by allowing the child class to invoke functionality from the parent class and then add its own behavior on top.

### **Basic Syntax of `super()`**

```python
super().method_name()  # Calls a method from the parent class
```

### **How `super()` Works:**

- In Python, **`super()`** refers to the **next class** in the method resolution order (MRO). It’s particularly useful when you have **multiple inheritance**.
- **`super()`** allows you to access methods from the **parent class** (or classes in the case of multiple inheritance) without explicitly naming them.

---

### **Example of `super()` in Action**

Let’s revisit the **Employee example** with a `Company` class, and demonstrate how `super()` is used to call the parent class constructor.

### **Code Example:**

```python
# Parent class (Superclass)
class Product:
    def __init__(self, name, price):
        self.name = name      # Product name
        self.price = price    # Product price

    def display_info(self):
        print(f"Product: {self.name}, Price: ${self.price}")

# Child class (Subclass) for Electronics
class Electronics(Product):
    def __init__(self, name, price, warranty):
        # Calling the parent class's __init__ method using super()
        super().__init__(name, price)
        self.warranty = warranty  # Warranty period for electronics

    def display_info(self):
        # Overriding the display_info method to include warranty information
        print(f"Product: {self.name}, Price: ${self.price}, Warranty: {self.warranty} years")

# Child class (Subclass) for Clothing
class Clothing(Product):
    def __init__(self, name, price, size):
        # Calling the parent class's __init__ method using super()
        super().__init__(name, price)
        self.size = size  # Clothing size

    def display_info(self):
        # Overriding the display_info method to include size information
        print(f"Product: {self.name}, Price: ${self.price}, Size: {self.size}")

# Create instances of Electronics and Clothing
laptop = Electronics("Laptop", 1000, 2)  # Name, Price, Warranty period
tshirt = Clothing("T-shirt", 20, "M")    # Name, Price, Size

# Displaying info using inherited and overridden methods
laptop.display_info()  # Display info for electronics
tshirt.display_info()  # Display info for clothing
```

### **Understanding `super()` in the Store Example**

In the previous example, the `super()` method is used in the child classes (`Electronics` and `Clothing`) to call the **constructor** (`__init__()`) of the **parent class** (`Product`). Let’s go through the example and explain how `super()` works in this context.

### **What is `super()`?**

The `super()` function in Python is used to:

1. **Call methods from the parent class** (superclass) from within a child class.
2. **Ensure that the parent class's method is executed** before executing any code in the child class.

### **How `super()` Works Internally:**

The `super()` function returns a **proxy object** that allows access to methods and attributes in the parent class. When we call `super().__init__(name, price)`, we are telling Python:

- "Go up to the **parent class** (`Product`) and call its `__init__` method, passing the `name` and `price` arguments."
- This ensures that the child class doesn't have to explicitly reference the parent class by name.

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

### **Example of Polymorphism:**

Imagine a scenario where we have a `Shape` class, and different types of shapes (like `Circle` and `Rectangle`) inherit from it. Each shape can have a method `area()`, but the implementation of `area()` will be different for each shape.

### **Code Example:**

```python
# Parent class (Superclass)
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Child class (Subclass) for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)  # Area of circle: πr^2

# Child class (Subclass) for Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width  # Area of rectangle: length * width

# Create instances of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Polymorphism in action: calling area() on different objects
print(f"Circle area: {circle.area()}")        # Calls Circle's area method
print(f"Rectangle area: {rectangle.area()}")  # Calls Rectangle's area method
```

### **Explanation:**

1. **Shape (Parent Class)**:
    - The `Shape` class defines an abstract method `area()`. We use `raise NotImplementedError` to ensure that this method is overridden by any subclass. This makes `Shape` an abstract class that serves as a blueprint for the subclasses.
2. **Circle and Rectangle (Child Classes)**:
    - The `Circle` and `Rectangle` classes inherit from `Shape` and override the `area()` method to provide their own specific implementations.
    - The `Circle` class calculates the area using the formula πr2\pi r^2πr2, and the `Rectangle` class calculates the area using the formula length×width\text{length} \times \text{width}length×width.
3. **Polymorphism in Action**:
    - Even though we are calling the `area()` method on different objects (`circle` and `rectangle`), the method behaves differently based on the type of object.
    - This is **polymorphism**: the same method name (`area()`) has different behaviors depending on the object it’s called on.

### **Why is this Polymorphism?**

- The `area()` method in both the `Circle` and `Rectangle` classes has the same name, but they provide different implementations.
- Polymorphism allows us to call the same method (`area()`) on different objects (`circle` and `rectangle`), and the correct version of the method is executed based on the object type.
- This makes the code more flexible and reusable, as we don’t need to know the specific type of shape when calculating the area. We can just call `area()` on any `Shape` object, and it will behave correctly based on the object type.

- **Polymorphism** allows the same method to behave differently based on the object it is acting upon.
- In Python, polymorphism is often implemented via **method overriding**, where a child class provides a specific implementation of a method already defined in the parent class.

---

### Explaining the Difference

1. **Inheritance** is about creating a hierarchy of classes where a child class derives properties and behaviors from a parent class.
    - Example: Dog and Cat are specific types of Animal.
2. **Polymorphism** is about using a unified interface to interact with objects of different types.
    - Example: Both Dog and Cat can "speak," but their behavior differs based on their specific implementation.