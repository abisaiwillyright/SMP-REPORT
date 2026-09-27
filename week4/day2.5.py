# Raising your own Error

def long_steps(steps):
    if not isinstance(steps, int):
        raise TypeError('Steps must be integer.')
    if steps < 0:
        raise ValueError('Steps cannot be negative.')
    print(f'Steps logged: {steps}')

try:
    long_steps(9200)
    long_steps('five')
except ValueError as e:
    print('ValueError:', e)
except TypeError as e:
    print('TypeError:', e)