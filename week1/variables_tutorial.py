"""
Python Variables Tutorial
========================

A variable is a named container that stores a value in memory.
You can use variables to store data and reuse it throughout your program.
"""

# ============================================================================
# 1. CREATING VARIABLES - BASIC ASSIGNMENT
# ============================================================================

# Variables are created by assigning a value using the = operator
name = "Alice"
age = 25
height = 5.9
is_student = True

print("=== 1. Basic Variable Assignment ===")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Is Student: {is_student}")
print()

# ============================================================================
# 2. VARIABLE NAMING CONVENTIONS
# ============================================================================

# Valid variable names
first_name = "Bob"          # snake_case (recommended in Python)
firstName = "Charlie"        # camelCase (not recommended in Python)
FirstName = "David"          # PascalCase (use for class names)
first_name_2 = "Eve"         # can include numbers (but not at start)
_private_var = "secret"      # underscore prefix indicates private
__dunder_var__ = "special"   # double underscore for special variables

print("=== 2. Variable Naming Conventions ===")
print(f"snake_case: {first_name}")
print(f"camelCase: {firstName}")
print(f"PascalCase: {FirstName}")
print()

# Invalid names (uncomment to see errors):
# 2first_name = "Frank"      # ❌ Cannot start with a number
# first-name = "Grace"       # ❌ Cannot contain hyphens
# first name = "Henry"       # ❌ Cannot contain spaces
# class = "Advanced"         # ❌ Cannot use reserved keywords

# ============================================================================
# 3. DATA TYPES
# ============================================================================

# String - text data
greeting = "Hello, World!"
multiline_text = """This is a
multi-line string"""

# Integer - whole numbers
count = 42
negative = -10
zero = 0

# Float - decimal numbers
pi = 3.14159
temperature = -5.5

# Boolean - True or False
is_active = True
is_deleted = False

# None - represents absence of value
nothing = None

print("=== 3. Data Types ===")
print(f"String: {greeting} (type: {type(greeting).__name__})")
print(f"Integer: {count} (type: {type(count).__name__})")
print(f"Float: {pi} (type: {type(pi).__name__})")
print(f"Boolean: {is_active} (type: {type(is_active).__name__})")
print(f"None: {nothing} (type: {type(nothing).__name__})")
print()

# ============================================================================
# 4. VARIABLE REASSIGNMENT
# ============================================================================

# Variables can be reassigned to new values
value = 10
print("=== 4. Variable Reassignment ===")
print(f"Initial value: {value}")

value = 20
print(f"After reassignment: {value}")

value = "Now I'm a string!"
print(f"Can change type: {value}")
print()

# ============================================================================
# 5. MULTIPLE ASSIGNMENT
# ============================================================================

# Assign multiple variables in one line
x, y, z = 1, 2, 3
print("=== 5. Multiple Assignment ===")
print(f"x={x}, y={y}, z={z}")

# Unpacking values from a list or tuple
colors = ["red", "green", "blue"]
color1, color2, color3 = colors
print(f"Colors: {color1}, {color2}, {color3}")

# Swapping values
a, b = 5, 10
print(f"Before swap: a={a}, b={b}")
a, b = b, a  # No temporary variable needed!
print(f"After swap: a={a}, b={b}")
print()

# ============================================================================
# 6. CONSTANTS (by convention)
# ============================================================================

# In Python, constants are written in UPPERCASE
# Note: Python doesn't enforce true constants, it's just a convention
PI = 3.14159
MAX_USERS = 100
DEFAULT_TIMEOUT = 30

print("=== 6. Constants (by Convention) ===")
print(f"PI: {PI}")
print(f"MAX_USERS: {MAX_USERS}")
print(f"DEFAULT_TIMEOUT: {DEFAULT_TIMEOUT}")
print()

# ============================================================================
# 7. TYPE CHECKING
# ============================================================================

# Using type() function
var1 = 42
var2 = "hello"
var3 = [1, 2, 3]

print("=== 7. Type Checking ===")
print(f"type(42): {type(var1)}")
print(f"type('hello'): {type(var2)}")
print(f"type([1,2,3]): {type(var3)}")

# Using isinstance() function (preferred)
print(f"isinstance(42, int): {isinstance(var1, int)}")
print(f"isinstance('hello', str): {isinstance(var2, str)}")
print(f"isinstance([1,2,3], list): {isinstance(var3, list)}")
print()

# ============================================================================
# 8. COLLECTION VARIABLES
# ============================================================================

# List - ordered, mutable collection
fruits = ["apple", "banana", "orange"]

# Tuple - ordered, immutable collection
coordinates = (10, 20, 30)

# Dictionary - key-value pairs
person = {"name": "John", "age": 30, "city": "New York"}

# Set - unique values, unordered
unique_numbers = {1, 2, 3, 4, 5}

print("=== 8. Collection Variables ===")
print(f"List: {fruits}")
print(f"Tuple: {coordinates}")
print(f"Dictionary: {person}")
print(f"Set: {unique_numbers}")
print()

# ============================================================================
# 9. VARIABLE SCOPE
# ============================================================================

# Global variable (accessible everywhere)
global_var = "I'm global"

def example_function():
    # Local variable (only accessible inside this function)
    local_var = "I'm local"
    print(f"Inside function - global: {global_var}")
    print(f"Inside function - local: {local_var}")

print("=== 9. Variable Scope ===")
print(f"Outside function - global: {global_var}")
example_function()
# print(local_var)  # ❌ This would cause an error!
print()

# ============================================================================
# 10. BEST PRACTICES
# ============================================================================

print("=== 10. Best Practices ===")
print("""
✓ Use descriptive names: student_age instead of sa
✓ Use snake_case for variables and functions
✓ Use UPPERCASE for constants
✓ Initialize variables before using them
✓ Use meaningful names that explain the purpose
✓ Avoid single-letter names except in loops
✓ Group related variables together
✓ Use comments for complex variable usage
""")

# Good examples:
user_email = "user@example.com"
registration_date = "2024-01-15"
is_verified = True

# Bad examples (avoid):
# ue = "user@example.com"  # Too abbreviated
# x = "2024-01-15"         # Not descriptive
# flag = True              # Unclear purpose

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

print("=== Practice Exercises ===")
print("""
1. Create a variable called 'my_age' and assign your age to it.

2. Create variables for:
   - Your first and last name
   - Your favorite color
   - Whether you like Python (True/False)

3. Create a variable and reassign it 3 times with different types.

4. Create 5 variables using multiple assignment in one line.

5. Create a dictionary variable with your personal information.

6. Swap two variable values without using a temporary variable.
""")

# Solution examples:
print("\n--- Solution Examples ---")

# Exercise 1
my_age = 25
print(f"1. my_age = {my_age}")

# Exercise 2
first_name = "John"
last_name = "Doe"
favorite_color = "blue"
likes_python = True
print(f"2. {first_name} {last_name} likes {favorite_color} and Python: {likes_python}")

# Exercise 3
var = 10
print(f"3a. var = {var} (type: {type(var).__name__})")
var = "text"
print(f"3b. var = {var} (type: {type(var).__name__})")
var = [1, 2, 3]
print(f"3c. var = {var} (type: {type(var).__name__})")

# Exercise 4
a, b, c, d, e = 1, "two", 3.0, True, None
print(f"4. a={a}, b={b}, c={c}, d={d}, e={e}")

# Exercise 5
person_info = {
    "name": "Alice",
    "age": 28,
    "city": "Boston",
    "occupation": "Engineer"
}
print(f"5. {person_info}")

# Exercise 6
num1, num2 = 100, 200
print(f"6. Before: num1={num1}, num2={num2}")
num1, num2 = num2, num1
print(f"6. After: num1={num1}, num2={num2}")
