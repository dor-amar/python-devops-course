"""Exercise 1: Basic Dictionary Operations.

In this exercise, you will work with basic dictionary operations by implementing
functions to manage student records. You will learn how to:
1. Create dictionaries
2. Update dictionary values
3. Access dictionary data
4. Merge dictionaries
"""

def create_student_record(name: str, age: int, grades: list) -> dict:
    """Create a student record dictionary.
    
    TODO: Implement this function to create a dictionary with the following structure:
    {
        "name": name,
        "age": age,
        "grades": grades
    }
    """
    # Your code here
    pass


def update_student_grade(record: dict, new_grade: float) -> dict:
    """Add a new grade to student's record.
    
    TODO: Implement this function to:
    1. Add the new grade to the grades list in the record
    2. Return the updated record
    """
    # Your code here
    pass


def calculate_average_grade(record: dict) -> float:
    """Calculate average grade from student record.
    
    TODO: Implement this function to:
    1. Get the grades list from the record
    2. Calculate and return the average grade
    """
    # Your code here
    pass


def merge_student_records(record1: dict, record2: dict) -> dict:
    """Merge two student records, combining their grades.
    
    TODO: Implement this function to:
    1. Create a copy of record1 to avoid modifying the original
    2. Add all grades from record2 to the grades list
    3. Return the merged record
    """
    # Your code here
    pass


def main():
    """Test your implementations here."""
    # Create a student record
    student = create_student_record("John", 20, [85.5, 90.0, 88.5])
    print(f"Created student record: {student}")
    
    # Update grade
    student = update_student_grade(student, 95.0)
    print(f"Updated grades: {student['grades']}")
    
    # Calculate average
    avg = calculate_average_grade(student)
    print(f"Average grade: {avg:.2f}")
    
    # Create another record and merge
    student2 = create_student_record("John", 20, [88.5, 95.0])
    merged = merge_student_records(student, student2)
    print(f"Merged grades: {merged['grades']}")


if __name__ == "__main__":
    main() 