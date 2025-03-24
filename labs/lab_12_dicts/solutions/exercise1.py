"""Solution for Exercise 1: Basic Dictionary Operations."""

from typing import Any, Dict, List


def create_student_record(name: str, age: int, grades: List[float]) -> Dict[str, Any]:
    """Create a student record dictionary.
    
    Args:
        name: Student's name
        age: Student's age
        grades: List of student's grades
        
    Returns:
        Dictionary containing student information
    """
    return {
        "name": name,
        "age": age,
        "grades": grades
    }


def update_student_grade(record: Dict[str, Any], new_grade: float) -> Dict[str, Any]:
    """Add a new grade to student's record.
    
    Args:
        record: Student record dictionary
        new_grade: New grade to add
        
    Returns:
        Updated student record
    """
    record["grades"].append(new_grade)
    return record


def calculate_average_grade(record: Dict[str, Any]) -> float:
    """Calculate average grade from student record.
    
    Args:
        record: Student record dictionary
        
    Returns:
        Average grade
    """
    grades = record["grades"]
    return sum(grades) / len(grades)


def merge_student_records(record1: Dict[str, Any], record2: Dict[str, Any]) -> Dict[str, Any]:
    """Merge two student records, combining their grades.
    
    Args:
        record1: First student record
        record2: Second student record
        
    Returns:
        Merged student record
    """
    merged = record1.copy()
    merged["grades"].extend(record2["grades"])
    return merged 