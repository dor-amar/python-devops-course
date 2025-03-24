### **Project Title**: **Student Management System**

---

### **Description**:

The Student Management System is a simple console-based application where users can perform the following actions:

1. Add a student.
2. View all students.
3. Calculate the average score of students.
4. Find the highest scorer.
5. Exit the program.

---

### **Phases of the Project**

---

### **Phase 1: Basic Setup and Menu System**

1. Create a file named `student_management.py`.
2. Write a function named `show_menu()` to display the following options to the user:
    - 
        1. Add a Student
    - 
        1. View All Students
    - 
        1. Calculate Average Score
    - 
        1. Find the Highest Scorer
    - 
        1. Exit
3. Create a `main()` function that repeatedly calls `show_menu()` and asks the user to choose an option.
4. Use a `while` loop to allow the program to run until the user selects **Exit**.

---

### **Phase 2: Adding Students**

1. Write a function named `add_student()` to:
    - Take the student's name and score as inputs from the user.
    - Store them in a global list of dictionaries (e.g., `students = []`).
    - Example structure of `students`:
        
        ```python
        students = [
            {"name": "Dor", "score": 85},
            {"name": "Jessica", "score": 90},
        ]
        
        ```
        
2. Add validation to ensure the score is a number between 0 and 100.

---

### **Phase 3: Viewing All Students**

1. Write a function named `view_students()` to:
    - Print all students in a formatted table.
    - If the list is empty, print a message saying "No students available."
- **Example Output**:
    
    ```
    Name    | Score
    ----------------
    Dor         | 85
    Jessica     | 90
    
    ```
    

---

### **Phase 4: Calculate Average Score**

1. Write a function named `calculate_average()` to:
    - Calculate and return the average score of all students.
2. Call this function when the user selects the **Calculate Average Score** option and display the result.
3. If no students exist, print an appropriate message.

---

### **Phase 5: Find the Highest Scorer**

1. Write a function named `find_highest_scorer()` to:
    - Find the student with the highest score.
    - Return their name and score.
2. Display the result when the user selects this option.

---

### **Phase 6: Optimize with Lambda Functions**

1. Use a **lambda function** to sort the `students` list by score in descending order when finding the highest scorer.
2. Example:
    
    ```python
    highest = max(students, key=lambda x: x["score"])
    
    ```
    

---

### **Phase 7: Add Error Handling**

1. Ensure the program doesn't crash due to invalid input by:
    - Using `try-except` blocks for input conversion.
    - Handling edge cases (e.g., empty student list when calculating averages).

---

### **Phase 8: Final Polishing**

1. Add comments and docstrings for all functions.
2. Use default arguments for optional features (e.g., default score for a student if not provided).
3. Add an option to clear all students for testing purposes.

---

### **Bonus Tasks**

1. Allow the user to search for a student by name and display their details.
2. Add functionality to update or delete a student's record.
3. Export the student list to a CSV file.

---

### **Deliverables**

1. Submit the Python script `student_management.py`.
2. Include test cases in the form of sample inputs and outputs.

---

### **Evaluation Criteria**

1. **Correctness**: All functionalities work as intended.
2. **Code Quality**: The code is clean, modular, and follows best practices.
3. **Error Handling**: The program gracefully handles invalid inputs and edge cases.
4. **Bonus Features**: Extra points for implementing bonus tasks.

---

### **Example Run**

```
Welcome to the Student Management System!
1. Add a Student
2. View All Students
3. Calculate Average Score
4. Find the Highest Scorer
5. Exit
Enter your choice: 1

Enter student name: Dor
Enter student score: 85
Student added successfully!

1. Add a Student
2. View All Students
3. Calculate Average Score
4. Find the Highest Scorer
5. Exit
Enter your choice: 2

Name    | Score
----------------
Dor   | 85

```