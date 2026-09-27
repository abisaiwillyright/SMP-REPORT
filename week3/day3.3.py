# The random module

import random

# Random integer between 1 to 10 (inclusive)
print('Random number:', random.randint(1,10))
print()

# Random float between 0 and 1
print('Random float:', random.random())
print()

# Random choice from the list
skills = ['welding', 'tilling', 'upholstery', 'phone repaire', 'copywriting']
print('Today skills focus:', random.choice(skills))
print()

# Shuffle a list
random.shuffle(skills)
print('Shuffled:', skills)