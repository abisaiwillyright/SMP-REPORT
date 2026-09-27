# Importing Specific Functions

from math import sqrt, floor, ceil
from random import randint, choice

# No need to write math.sqrt() or random.randint()

print('Square root of 225 :', sqrt(225))
print('Floor of 9.7 :', floor(9.7))
print()

protocols = ['OMAD', '2MAD', 'Autophagy Marathon']
print('Today protocal:', choice(protocols))
print('Random step bonus:', randint(100, 500), 'steps')