# List, Tuple, Set

Here’s a basic explanation of **List**, **Tuple**, and **Set** in Python, suitable for beginners.

---

### 1. **List**

- A **list** is an ordered, mutable (modifiable) collection of items.
- Lists are defined by square brackets `[]`.
- Lists allow duplicate items and can contain elements of different data types (e.g., integers, strings, other lists).

**Example:**

```python
# Creating a list
fruits = ["apple", "banana", "cherry", "apple"]
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'apple']

# Creating a list with elements of different data types
fruits = [1, "banana", 3.78]
print(fruits)

# Creating a list with duplicate
fruits = [1, "banana", 3.78, 1]
print(fruits)

# Accessing elements
print(fruits[0])  # Output: apple

# Negative elements
print(fruits[-1])

# Slicing a List
my_list = ['h','e','l','l','o','!','d','o','r']
print(my_list[2:5])
print(my_list[5:])
print(my_list[:])

# Adding elements
fruits.append("grape")
print(fruits)  # Output: ['apple', 'orange', 'cherry', 'apple', 'grape']

# Extend 
numbers = [1,3,5]
even_numbers = [4,6,8]
numbers.extend(even_numbers)
print("List after append:", numbers)

# Insert
numbers = [1,3,4,5,6]
numbers.insert(1,2)
print(numbers)

# Modifying elements
fruits = ["banana","melon","apple"]
fruits[1] = "orange"
print(fruits) 

# Remove Items from a list 
languages = ['Python','Java','C#','C','Javascript']
del languages[1]
print(languages)
del languages[-1]
print(languages)
del languages[0:2]
print(languages)

# Using Remove 
languages = ['Python','Java','C#','C','Javascript']
languages.remove('Python')

# Iterating through a list 
languages = ['Python','Java','C#','C','Javascript']
for language in languages 
  print(language)
  
# Check if element Exists in a List 
languages = ['Python','Java','C#','C','Javascript']
print('C' in languages)
print('Dor' in languages)

#List Length
languages = ['Python','Java','C#','C','Javascript']
print(len(languages))
```

**Characteristics of Lists:**

- **Ordered**: Elements have a specific order and can be accessed by index.
- **Mutable**: You can modify, add, or remove elements.
- **Allows duplicates**: Lists can contain repeated items.

---

### 2. **Tuple**

- A **tuple** is an ordered, immutable (cannot be modified) collection of items.
- Tuples are defined by parentheses `()`.
- Like lists, tuples can contain elements of different data types.

**Example:**

```python
# Different types of tuples

# Empty tuple
my_tuple = ()
print(my_tuple)  # Output: ()

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)  # Output: (1, 2, 3)

# Tuple with mixed data types
my_tuple = (1, "Hello", 3.4)
print(my_tuple)  # Output: (1, 'Hello', 3.4)

# Nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)  # Output: ('mouse', [8, 4, 6], (1, 2, 3))

###################################################################################

# Creating a variable with a single element
var1 = ("Hello")  # This is a string, not a tuple
print(type(var1))  # Output: <class 'str'>

# Creating a tuple with one element
var2 = ("Hello",)  # Adding a comma makes it a tuple
print(type(var2))  # Output: <class 'tuple'>

# Parentheses are optional for single-element tuples
var3 = "Hello",
print(type(var3))  # Output: <class 'tuple'>

###################################################################################

# Access Python Tuple Elements 
# Indexing 
letters = ("p", "r", "o", "g", "r", "a", "m", "i", "z")
print(letters[0]) # prints "p"
print(letters[5]) # prints "a"

# accessing tuple elements using negative indexing
letters = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(letters[-1]) # prints 'z'
print(letters[-3]) # prints 'm'

# accessing tuple elements using slicing
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
# elements 2nd to 4th index
print(my_tuple[1:4]) # prints ('r', 'o', 'g')
# elements beginning to 2nd
print(my_tuple[:-7]) # prints ('p', 'r')
# elements 8th to end
print(my_tuple[7:]) # prints ('i', 'z')
# elements beginning to end
print(my_tuple[:]) # Prints ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

###################################################################################

# Methods
my_tuple = ('a', 'p', 'p', 'l', 'e',)
print(my_tuple.count('p')) # prints 2
print(my_tuple.index('l')) # prints 3

# iterating through the tuple
languages = ('Python', 'Swift', 'C++')
for language in languages:
  print(language)
  
# Check if element exists
languages = ('Python', 'Swift', 'C++')
print('C' in languages) # False
print('Python' in languages) # True
```

**Characteristics of Tuples:**

- **Ordered**: Elements have a specific order and can be accessed by index.
- **Immutable**: You cannot modify, add, or remove elements after the tuple is created.
- **Allows duplicates**: Tuples can contain repeated items.

### Why use Tuple and Not a List ?

- Once you create a tuple, you cannot change it, Use a tuple when you have a collection of items that should not change, if you want to store the days of the week.
- Tuples are Faster - Because tuples are fixed and can’t be modified, Python can access them faster than lists. If you have a set of constant values and you care about speed, tuples are a better choice. They’re also useful for large datasets that are read-only.
- Data that doesn’t change

### Quick Summary:

- **Use tuples** for collections of items that won’t change and if you need to make your code faster.
- **Use lists** if you need flexibility to change, add, or remove items from your collection.

---

### 3. **Set**

- A **set** is an unordered, mutable collection of unique items.
- Sets are defined by curly braces `{}`.
- Sets automatically remove duplicate values and do not support indexing (since they are unordered).

**Example:**

```python
# create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)

# create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)

# create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)

# create an empty set
empty_set = set()
# create an empty dictionary
empty_dictionary = { }
# check data type of empty_set
print('Data type of empty_set:', type(empty_set))
# check data type of dictionary_set
print('Data type of empty_dictionary', type(empty_dictionary))

###################################################################################

# Duplicated Items in a set
numbers = {2, 4, 6, 6, 2, 8, 2, 2, 2, 2}
print(numbers) # {8, 2, 4, 6}

###################################################################################

# Adding elements
numbers = {21, 34, 54, 12}
print('Initial Set:',numbers)
# using add() method
numbers.add(32)
print('Updated Set:', numbers)

# Update
companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']
companies.update(tech_companies)
print(companies)
# Output: {'google', 'apple', 'Lacoste', 'Ralph Lauren'}

###################################################################################

# Removing elements
languages = {'Swift', 'Java', 'Python'}
print('Initial Set:',languages)
# remove 'Java' from a set
removedValue = languages.discard('Java')
print('Set after remove():', languages)

###################################################################################

# Iterate 
fruits = {"Apple", "Peach", "Mango"}
# for loop to access each fruits
for fruit in fruits:
  print(fruit)
  
###################################################################################

# Find Number of Set Elements
even_numbers = {2,4,6,8}
print('Set:',even_numbers)
# find number of elements
print('Total Elements:', len(even_numbers))

###################################################################################

## Union
# first set
A = {1, 3, 5}
# second set
B = {0, 2, 4}
# perform union operation using |
print('Union using |:', A | B)
# perform union operation using union()
print('Union using union():', A.union(B))

## Intersection
# first set
A = {1, 3, 5}
# second set
B = {1, 2, 3}
# perform intersection operation using &
print('Intersection using &:', A & B)
# perform intersection operation using intersection()
print('Intersection using intersection():', A.intersection(B))

## Diff
# first set
A = {2, 3, 5}
# second set
B = {1, 2, 6}
# perform difference operation using &
print('Difference using &:', A - B)
# perform difference operation using difference()
print('Difference using difference():', A.difference(B))

## Check if equal 
# first set
A = {1, 3, 5}
# second set
B = {3, 5, 1}
# perform difference operation using &
if A == B:
print('Set A and Set B are equal')
else:
print('Set A and Set B are not equal')
```

**Characteristics of Sets:**

- **Unordered**: Elements do not have a specific order and cannot be accessed by index.
- **Mutable**: You can add or remove elements.
- **No duplicates**: Sets only store unique items.

---

### Summary Table

| Data Structure | Ordered | Mutable | Allows Duplicates | Syntax |
| --- | --- | --- | --- | --- |
| **List** | Yes | Yes | Yes | `[]` |
| **Tuple** | Yes | No | Yes | `()` |
| **Set** | No | Yes | No | `{}` |

These three data structures are commonly used in Python, each suited for different types of tasks.