# Functions and Modules
# Assignments
# Write a function called greet that takes aname and retuns greetings string.

def greet(name):
    return f"\nHello, {name}. Welcome to the program."

print(greet("Alice"))
print(greet("Bob"))
print(greet("Abisai"))
print()

# Write a function caled power(base, exponent=2) that turns base raised to exponent.
def power(base, exponent=2):
    return base ** exponent
print(''+'=' * 85)
print('POWER FUNCTION')
print(power(3))
print(power(2, 10))

# Use alist comprehension to get all even numbers from 1 to 30
even_numbers = [num for num in range(1, 31) if num % 2 == 0]
print(''+'=' * 85)
print('EVEN NUMBERS:', even_numbers)

# Squuares of even numbers
squares_of_even_numbers = [num ** 2 for num in even_numbers]
print('SQUARES OF EVEN NUMBERS:', squares_of_even_numbers)
print(''+'=' * 85)

# Write a function that takes a list of scores and returns the avarage, hights, and lowest.
def score_summary(scores):
    return {
        'average': sum(scores) / len(scores),
        'highest': max(scores),
        'lowest': min(scores)
    }
result = score_summary([78, 91, 63, 85, 72])
for key, value in result.items():
    print(f'{key}: {value}')
print(''+'=' * 85)


