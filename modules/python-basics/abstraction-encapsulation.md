# Abstraction & Encapsulation

![image.png](/images/oop7.png){width=600px}

### Abstraction in Python

**Abstraction** is the concept of hiding the internal details of an object and exposing only the essential features. It allows you to focus on **what** an object does rather than **how** it does it. In Python, abstraction is typically achieved using **abstract classes** and **interfaces**.

### Key Points:

- Abstract classes cannot be instantiated directly.
- They define methods that must be implemented in derived classes.
- Use the `abc` (Abstract Base Class) module in Python to create abstract classes.

### Example of Abstraction:

```python
python
Copy code
from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Concrete class implementing abstract methods
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Another concrete class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Using the classes
rect = Rectangle(4, 5)
circle = Circle(3)

print("Rectangle area:", rect.area())  # Output: Rectangle area: 20
print("Circle perimeter:", circle.perimeter())  # Output: Circle perimeter: 18.84

```

---

### Encapsulation in Python

**Encapsulation** is the concept of bundling the data (attributes) and methods (functions) that operate on the data into a single unit (class). It also restricts direct access to some of the object's components to enforce better control and security.

### Key Points:

- Encapsulation is implemented using **access modifiers**:
    - **Public** attributes/methods: Can be accessed from anywhere (default in Python).
    - **Protected** attributes/methods (`_attribute`): Indicate that an attribute is intended for internal use (convention only).
    - **Private** attributes/methods (`__attribute`): Cannot be accessed directly from outside the class.
- Use getter and setter methods to access and modify private attributes.

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

---

### Explaining the Difference

1. **Abstraction** is about hiding the implementation details and focusing on the functionality.
    - Example: You know a `Rectangle` has an `area`, but you don't worry about how it's calculated.
2. **Encapsulation** is about hiding the data and controlling access to it through methods.
    - Example: A bank account restricts direct access to the balance, ensuring it's only modified through defined methods.