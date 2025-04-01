# Lab:  Inheritance & Polymorphism

---

### Prerequisites:

- Understanding of classes and objects
- Basic Python syntax

---

## Objectives:

By the end of this lab, students will:

- Understand how inheritance works in Python
- Create subclasses from a parent class
- Override methods using polymorphism
- Practice real-world object design using class hierarchies

---

## Part 1: Inheritance

### Task 1: Create a Base Class `Instructor`

Create a class `Instructor` with the following:

- Attributes: `name`, `specialty`
- Method: `introduce()` that prints:
    
    `"Hi, I’m {name} and I specialize in {specialty}."`
    

---

### Task 2: Create a Subclass `DevOpsInstructor`

Create a subclass `DevOpsInstructor` that:

- Inherits from `Instructor`
- Adds a method `teach_tool(tool)` that prints:
    
    `"Today we'll learn how to use {tool}!"`
    

Create an object of `DevOpsInstructor`, introduce yourself, and call `teach_tool("Docker")`.

---

### Task 3: Create Another Subclass `DataInstructor`

- Inherits from `Instructor`
- Adds a method `teach_topic(topic)` that prints:
    
    `"Today's topic is {topic} in data science."`
    

---

## Part 2: Polymorphism

### Task 4: Create a `introduce_yourself()` Function

Write a function `introduce_yourself(instructor)` that:

- Accepts an object of type `Instructor` (or subclass)
- Calls the `.introduce()` method on it

Then:

- Create a `DevOpsInstructor` and a `DataInstructor`
- Call `introduce_yourself()` for both

> This demonstrates polymorphism — the same method name behaves differently depending on the object type.
> 

---

### Task 5: Override the `introduce()` Method

In both `DevOpsInstructor` and `DataInstructor`, override the `introduce()` method to include their teaching style.

Example output:

```
Hi, I’m Dor and I specialize in DevOps.
```

---

## Bonus Challenge: Use a List of Instructors

1. Create a list of mixed instructors (`DevOpsInstructor`, `DataInstructor`, `Instructor`)
2. Loop through the list and call `.introduce()` on each one
3. Call their respective teaching methods (if applicable)

This will demonstrate both **inheritance** and **polymorphism** in action.