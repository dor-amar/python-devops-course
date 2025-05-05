# Regular Expressions Lab

## Introduction
This lab will help you practice using regular expressions in Python. You'll work through 5 exercises that cover different aspects of regex usage, from basic pattern matching to more complex text processing tasks.

## Learning Objectives
- Practice using common regex patterns and functions
- Apply regex to real-world scenarios
- Develop pattern matching skills
- Learn to validate and extract data using regex

## Exercise 1: Email Validator
Create a function that validates email addresses. The function should:
- Accept an email string as input
- Return True if the email is valid, False otherwise
- Consider the following rules:
  - Must contain @ symbol
  - Username can contain letters, numbers, dots.
  - Domain must contain letters, numbers, dots.
  - Must end with a valid domain extension (2-4 characters)

```python
def validate_email(email):
    # Your code here
    pass
```

## Exercise 2: Log Parser
Create a function that parses a log file and extracts error messages. The function should:
- Accept a file path as input
- Return a list of tuples containing (timestamp, error_message)
- Consider the following log format:
  ```
  2023-01-01 10:00:00 ERROR: Database connection failed
  2023-01-01 10:01:00 INFO: System started
  2023-01-01 10:02:00 ERROR: Invalid user input
  ```

```python
def parse_error_logs(file_path):
    # Your code here
    pass
```

## Exercise 3: URL Extractor
Create a function that extracts all URLs from a text. The function should:
- Accept a text string as input
- Return a list of all valid URLs found
- Support both http and https protocols
- Handle URLs with and without www
- Extract the full URL including query parameters

```python
def extract_urls(text):
    # Your code here
    pass
```

## Exercise 4: Password Validator
Create a function that validates password strength. The function should:
- Accept a password string as input
- Return True if the password meets all requirements, False otherwise
- Password requirements:
  - At least 8 characters long
  - Contains at least one uppercase letter
  - Contains at least one lowercase letter
  - Contains at least one number
  - Contains at least one special character (!@#$%^&*)

```python
def validate_password(password):
    # Your code here
    pass
```

## Exercise 5: Text Cleaner
Create a function that cleans text by:
- Removing HTML tags
- Converting multiple spaces to single spaces
- Removing special characters except basic punctuation
- Converting text to lowercase
- Removing extra newlines

```python
def clean_text(text):
    # Your code here
    pass
```

## Testing Your Solutions
For each exercise, test your function with various inputs. Here are some test cases to consider:

### Exercise 1 Test Cases:
```python
emails = [
    "user@domain.com",
    "user.name@domain.com",
    "user@sub.domain.com",
    "invalid@domain",
    "user@domain.c",
    "user@domain.com1"
]
```

### Exercise 2 Test Cases:
```python
log_content = """
2023-01-01 10:00:00 ERROR: Database connection failed
2023-01-01 10:01:00 INFO: System started
2023-01-01 10:02:00 ERROR: Invalid user input
2023-01-01 10:03:00 WARNING: High memory usage
"""
```

### Exercise 3 Test Cases:
```python
text = """
Visit https://www.example.com or http://test.com
Check out https://sub.domain.com/path?query=value
Invalid: www.example.com (no protocol)
"""
```

### Exercise 4 Test Cases:
```python
passwords = [
    "Password123!",
    "weak",
    "NoSpecialChar123",
    "nouppercase123!",
    "NOLOWERCASE123!"
]
```

### Exercise 5 Test Cases:
```python
text = """
<h1>Hello World</h1>
<p>This is a test.   Multiple spaces here.</p>
Special characters: @#$%^&*
Multiple
newlines
"""
```


## Tips
- Use `re.compile()` for patterns you use multiple times
- Test your patterns with various edge cases
- Break down complex patterns into smaller parts
- Use online regex testers to verify your patterns
- Document your regex patterns with comments

## Resources
- [Python re module documentation](https://docs.python.org/3/library/re.html)
- [Regex101 - Online regex tester](https://regex101.com/)
