"""Task: Student Finder.

Implement a function to find a student in a list by ID or name.
"""

def find_student(students: list, search_term: str, search_by: str = 'id') -> dict:
    """Find a student in the list by ID or name.
    
    Args:
        students (list): List of student dictionaries with 'id' and 'name' keys
        search_term (str): ID or name to search for
        search_by (str): Field to search by ('id' or 'name')
        
    Returns:
        dict: Student dictionary if found, None if not found
        
    Raises:
        ValueError: If search_by is not 'id' or 'name'
        
    Example:
        >>> find_student([{'id': '001', 'name': 'John'}], '001')
        {'id': '001', 'name': 'John'}
    """
    # Your code here
    pass


def main():
    """Test your implementation."""
    # Test cases
    students = [
        {'id': '001', 'name': 'John Doe'},
        {'id': '002', 'name': 'Jane Smith'},
        {'id': '003', 'name': 'Bob Johnson'}
    ]
    
    test_cases = [
        ('001', 'id'),           # Should find by ID
        ('Jane Smith', 'name'),  # Should find by name
        ('004', 'id'),          # Should return None
        ('Alice', 'name'),      # Should return None
        ('001', 'invalid'),     # Should raise ValueError
    ]
    
    for search_term, search_by in test_cases:
        try:
            result = find_student(students, search_term, search_by)
            if result:
                print(f"Found student: {result}")
            else:
                print(f"No student found with {search_by} '{search_term}'")
        except Exception as e:
            print(f"Error searching for {search_term} by {search_by}: {str(e)}")


if __name__ == "__main__":
    main() 