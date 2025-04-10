"""
In this task, you'll create a simple Zoo Management System where different types of animals
(e.g., **Lion**, **Tiger**, **Elephant**) are represented as classes.
Each type of animal should inherit from a general **Animal** class, 
and each animal should have its own specific behavior for feeding, making sounds, and moving. 
You will use **polymorphism** to make each animal's behavior unique.

### **Steps:**


1. **Create a Parent Class `Animal`:**
    - The `Animal` class will have common attributes like `name` and `species`.
    - It should have methods like `feed()`, `make_sound()`, and `move()` that will be **overridden** in the child classes.

2. **Create Child Classes for Different Animals:**
    - **Lion**: Inherits from `Animal`. It should have an additional method `hunt()`, which is specific to lions.
    - **Tiger**: Inherits from `Animal`. It should have a specific implementation of `make_sound()` (e.g., "Roar!").
    - **Elephant**: Inherits from `Animal`. It should have a specific implementation of `move()` (e.g., walking slowly).

3. **Polymorphism:**
    - All animal types should override the methods (`feed()`, `make_sound()`, `move()`) to provide animal-specific behavior.
    - You should be able to call the same methods on all animal objects and get different behaviors depending on the type of animal.

4. **Create Multiple Animal Objects:**
    - Instantiate at least one object of each animal type: **Lion**, **Tiger**, and **Elephant**. (Or what ever you choose).
    - Call `feed()`, `make_sound()`, and `move()` on each object to see polymorphism in action.

5. **Challenge:**
    - Create a method `show_animal_details()` in each animal class that displays detailed information about that animal (e.g., name, species, and specific attributes if you added some).
    - **Add `get_picture()` Method to Animal Classes**
        You will extend the zoo management system by adding a `get_picture()` method to each animal class.

"""

