# Exercise

import io

# Simulated file: one line per day with step count

weekly_data = '''Monday: 9100
Tuesday: 7600
Wednesday: 10700
Thursday: 8900
Friday: 6900
Saturday: 11100
Sunday: 9700'''

goal = 8100
days_on_goal = 0

f = io.StringIO(weekly_data)
for line in f:
    line = line.strip()
    if ':' in line:
        day, steps_str = line.split(':', 1)
        steps = int(steps_str.strip())
        status = 'Goal hit' if steps >= goal else 'Below goal'
        print(f' {day}: {steps} steps - {status}')
        if steps >= goal:
            days_on_goal += 1

print(f'\nDays on goal: {days_on_goal}/7')