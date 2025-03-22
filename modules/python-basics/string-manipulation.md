### **1. Introduction**

- Brief review of what strings are and how they're used in Python.
- Overview of what will be covered in the session.

### **2. String Indexing and Slicing**

- **Example 1: Basic Indexing**
    
    ```python
    text = "Hello, World!"
    print(text[0])   # Output: H
    print(text[-1])  # Output: !
    
    ```
    
- **Example 2: Slicing**
    
    ```python
    text = "Hello, World!"
    print(text[0:5])   # Output: Hello
    print(text[7:])    # Output: World!
    print(text[:5])    # Output: Hello
    print(text[-6:])   # Output: World!
    
    ```
    

### **3. String Methods**

- **Example 3: Using String Methods**
    
    ```python
    text = "   Python Programming   "
    print(text.strip())       # Output: "Python Programming"
    print(text.replace("Python", "Java"))  # Output: "   Java Programming   "
    print(text.lower())       # Output: "   python programming   "
    print(text.upper())       # Output: "   PYTHON PROGRAMMING   "
    print(text.startswith("P"))  # Output: False (because of leading spaces)
    
    ```
    
- **Example 4: Splitting and Joining Strings**
    
    ```python
    text = "apple,banana,cherry"
    fruits = text.split(",")
    print(fruits)  # Output: ['apple', 'banana', 'cherry']
    
    joined_text = " ".join(fruits)
    print(joined_text)  # Output: "apple banana cherry"
    
    ```
    

### **4. String Formatting**

- **Example 5: Using f-strings**
    
    ```python
    name = "Alice"
    age = 30
    print(f"Hello, {name}! You are {age} years old.")  # Output: "Hello, Alice! You are 30 years old."
    
    ```
    
- **Example 6: Formatting Numbers**
    
    ```python
    pi = 3.14159
    print(f"Pi rounded to 2 decimal places: {pi:.2f}")  # Output: "Pi rounded to 2 decimal places: 3.14"
    
    ```
    

### **5. Escape Characters**

- **Example 7: Using Escape Characters**
    
    ```python
    text = "She said, \"Hello!\""
    print(text)  # Output: She said, "Hello!"
    
    multiline_text = "First line\nSecond line\nThird line"
    print(multiline_text)
    # Output:
    # First line
    # Second line
    # Third line
    
    ```
    

### **6. Concatenation and Repetition**

- **Example 8: Concatenating Strings**
    
    ```python
    greeting = "Hello"
    name = "Bob"
    full_greeting = greeting + ", " + name + "!"
    print(full_greeting)  # Output: "Hello, Bob!"
    
    ```
    
- **Example 9: Repeating Strings**
    
    ```python
    word = "Hi! "
    repeated_word = word * 3
    print(repeated_word)  # Output: "Hi! Hi! Hi! "
    
    ```
    

### **7. Practical Exercises**

- **Exercise 1**: Given a string containing a full name (e.g., "John Doe"), write a program to swap the first and last names.
    
    ```python
    name = "John Doe"
    first_name, last_name = name.split()
    swapped_name = f"{last_name}, {first_name}"
    print(swapped_name)  # Output: "Doe, John"
    
    ```
    
- **Exercise 2**: Write a program that takes a sentence and counts the number of vowels in it.
    
    ```python
    sentence = "This is a simple sentence."
    vowels = "aeiouAEIOU"
    count = sum(1 for letter in sentence if letter in vowels)
    print(f"Number of vowels: {count}")  # Output: "Number of vowels: 7"
    
    ```
    
- **Exercise 3**: Write a program to check if a given string is a palindrome.
    
    ```python
    word = "radar"
    is_palindrome = word == word[::-1]
    print(f"Is '{word}' a palindrome? {is_palindrome}")  # Output: "Is 'radar' a palindrome? True"
    
    ```
    

### **8. Q&A and Recap**

- Open the floor for any questions.
- Summarize key takeaways from the class.