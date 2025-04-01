# Lab: DevOps Instructor & Students

### Prerequisites:

- Comfortable with basic OOP (classes, methods, attributes)
- Understanding of `@property`, `@classmethod`, and `inheritance`
- Experience working with lists and dictionaries

---

## Objectives:

By the end of this lab, students will:

- Use inheritance to model roles in a bootcamp
- Implement private attributes and accessors
- Use class variables to track shared state
- Model relationships between objects (e.g., Instructor teaches Students)
- Work with decorators like `@classmethod`, `@property`

---

## Task 1: Create a `Student` Class

### ✅ Goal:

1. Define a `Student` class with:
    - `name` (public)
    - `_progress` (private, 0-100 scale)
    - `topics_learned` (list of strings)
2. Add methods:
    - `learn(topic)` → adds a topic to the list
    - `increase_progress(amount)` → increases progress (max 100)
    - `show_progress()` → prints a bar of progress (like "▇▇▇ 30%")

---

## Task 2: Create a `DevOpsInstructor` Class

### Goal:

1. Create a class `DevOpsInstructor` with:
    - `name` (public)
    - `students` (a list of `Student` objects)
2. Add methods:
    - `add_student(student)` → adds a student to the list
    - `teach(topic)` → goes through each student and:
        - adds topic to student’s topics
        - increases progress by 10
        - prints a message like `"Taught Git to Jessica"`

---

## Task 3: Track Total Students Across All Instructors

### ✅ Goal:

1. Use a class variable to track the total number of students across all instructors.
2. Use a `@classmethod` called `total_students()` to return that number.

---

## Task 4: Use Everything Together

### Goal:

1. Create 3 students: Alice, Bob, and Charlie
2. Create 2 instructors: Noa and Dor
3. Assign Eilon and Jessica to Noa, Yonatan to Dor
4. Noa teaches "Git", then "CI/CD"
5. Dor teaches "Kubernetes"
6. Print each student’s name, topics learned, and progress
7. Print total number of students across instructors

---

## 🧠 Bonus Task: Promote a Student

### ✅ Goal:

1. Add a method `check_graduation()` in `Student`
2. If progress >= 80%, print `"🎓 {name} has graduated!"`