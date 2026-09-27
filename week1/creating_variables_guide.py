"""
How to CREATE Variables in Python - Step by Step Guide
=====================================================
"""

print("=" * 60)
print("STEP 1: Create a variable by assigning a value")
print("=" * 60)
print("""
SYNTAX:  variable_name = value

To create a variable, you:
1. Give it a name
2. Use the = sign (equals sign)
3. Assign a value to it
""")

# EXAMPLE 1: Create a variable with a text value (string)
print("\n>>> Example 1: Creating a string variable")
name = "Alice"
print(f'name = "Alice"')
                        
EXAMPLE 2: Create a variable with a number (integer)
print("\n>>> Example 2: Creating an integer variable")
age = 25
print(f"age = 25")
print(f"Result: age is now {age}")

# EXAMPLE 3: Create a variable with a decimal number (float)
print("\n>>> Example 3: Creating a float variable")
height = 5.9
print(f"height = 5.9")
print(f"Result: height is now {height}")

# EXAMPLE 4: Create a variable with True/False (boolean)
print("\n>>> Example 4: Creating a boolean variable")
is_student = True
print(f"is_student = True")
print(f"Result: is_student is now {is_student}")

print("\n" + "=" * 60)
print("STEP 2: Use your variables")
print("=" * 60)

print(f"\nYou can now use these variables:")
print(f"  name = {name}")
print(f"  age = {age}")
print(f"  height = {height}")
print(f"  is_student = {is_student}")

# Use them in sentences
print(f"\nExample: My name is {name}, I'm {age} years old, {height} tall, and I'm a student: {is_student}")

print("\n" + "=" * 60)
print("STEP 3: Create multiple variables at once")
print("=" * 60)

print("""
You can create multiple variables in one line by separating them with commas.
""")

# Create multiple variables in one line
x, y, z = 10, 20, 30
print(f"x, y, z = 10, 20, 30")
print(f"Result: x={x}, y={y}, z={z}")

# Create variables from a list
print("\nYou can also assign from a list:")
colors = ["red", "green", "blue"]
color1, color2, color3 = colors
print(f"colors = ['red', 'green', 'blue']")
print(f"color1, color2, color3 = colors")
print(f"Result: color1={color1}, color2={color2}, color3={color3}")

print("\n" + "=" * 60)
print("STEP 4: Change a variable's value")
print("=" * 60)

print("\nYou can change a variable's value anytime:")
count = 5
print(f"count = 5")
print(f"count is now: {count}")

count = 10
print(f"\ncount = 10")
print(f"count is now: {count}")

count = count + 5
print(f"\ncount = count + 5")
print(f"count is now: {count}")

print("\n" + "=" * 60)
print("STEP 5: Variable naming rules")
print("=" * 60)

print("""
Valid variable names:
""")
# Valid names
student_name = "Bob"
firstName = "Charlie"
first_name_2 = "David"
_private = "secret"

print(f"✓ student_name = 'Bob'      (good - snake_case)")
print(f"✓ firstName = 'Charlie'     (okay - camelCase)")
print(f"✓ first_name_2 = 'David'    (can include numbers)")
print(f"✓ _private = 'secret'       (underscore prefix)")

print("""
Invalid variable names (❌ would cause errors):
  ✗ 2student = "Eve"         (can't start with number)
  ✗ student-name = "Frank"   (can't use hyphens)
  ✗ student name = "Grace"   (can't use spaces)
  ✗ class = "Math"           (can't use Python keywords)
""")

print("\n" + "=" * 60)
print("STEP 6: Check what type a variable is")
print("=" * 60)

var1 = 42
var2 = "hello"
var3 = True
var4 = 3.14

print(f"\nvar1 = 42")
print(f"type(var1) = {type(var1)}")

print(f"\nvar2 = 'hello'")
print(f"type(var2) = {type(var2)}")

print(f"\nvar3 = True")
print(f"type(var3) = {type(var3)}")

print(f"\nvar4 = 3.14")
print(f"type(var4) = {type(var4)}")

print("\n" + "=" * 60)
print("QUICK PRACTICE: Try it yourself!")
print("=" * 60)

print("""
Try creating these variables:

1. favorite_food = "pizza"
2. rating = 9
3. price = 15.50
4. is_available = True

Then print them:
print(f"My favorite food is {favorite_food}")
""")

# Solutions:
print("\n--- Here's what it looks like: ---\n")

favorite_food = "pizza"
rating = 9
price = 15.50
is_available = True

print(f"My favorite food is {favorite_food}")
print(f"I rate it {rating} out of 10")
print(f"It costs ${price}")
print(f"Is it available? {is_available}")

print("\n" + "=" * 60)
print("SUMMARY - How to Create Variables:")
print("=" * 60)

print("""
1. Write the variable name
2. Add the = sign
3. Write the value
4. Press Enter

Example:  student_name = "John"

That's it! You now have a variable called 'student_name'
that contains the text "John"
""")
