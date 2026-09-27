# Simulating step counts

import random

print('Simulatedstep count for this week:')
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
for day in days:
    steps = random.randint(5000, 13000)
    status = 'Ok' if steps >= 8000 else 'low'
    print(f' {day}: {steps} steps - {status}')