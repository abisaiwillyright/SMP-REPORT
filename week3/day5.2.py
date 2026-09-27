# Step Goal Checker

import math


def weekly_step_summary(steps_list, goal=8000):
    days_hit = len([s for s in steps_list if s >= goal])
    avarage = sum(steps_list) // len(steps_list)
    best = max(steps_list)
    worst = min(steps_list)
    total_days = len(steps_list)
    return days_hit, avarage, best, worst, total_days

weekly = [9200, 7500, 10500, 8800, 6900, 11000, 9600]
result = weekly_step_summary(weekly)

print('----Step Summary----')
print(f' Days on goal: {result[0]} / {result[4]}')
print(f' Avarage  : {result[1]} steps')
print(f' best day : {result[2]} steps')
print(f' worst day: {result[3]} steps')


import math
# Estimated calories burned from walking (0.04 calories per step)
print('\n--------------------------------------')
def estimated_calories(steps):
    calories = steps * 0.04
    return math.floor(calories)

daily_cals = [estimated_calories(steps) for steps in weekly]
print('Estimated daily calories burned from walking:')
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
for day, cals in zip(days, daily_cals):
    print(f'{day}: {cals} kcal')

print('\nTotal :', sum(daily_cals), 'kcal')