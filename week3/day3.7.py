# Exersise

import math
import random

def generate_week():
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Wed', 'Thu', 'Fri', 'Sat', 'Sum']
    total = 0
    goal_days = 0

    for day in days:
        steps = random.randint(6000, 12000)
        total += steps
        if steps >= 8000:
            goal_days += 1
        print(f' {day}: {steps} steps')

    avg = math.floor(total / 7)
    print(f'\nAvarage steps : {avg}')
    print(f'\nDay on goal : {goal_days} / 7')

generate_week()