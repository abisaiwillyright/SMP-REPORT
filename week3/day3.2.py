#  calculate how many full rest days fit into a training programme

import math

total_days = 50
training_days_per_week = 5
weeks = total_days // 7

print(f'Total days: {total_days}')
print(f'Full weeks: {math.floor(weeks)}')
print()

# Distance calculation using pythagoras
walk_east = 3.0
walk_north = 4.0
distance = math.sqrt(walk_east**2 + walk_north**2)
print(f'Direct distance: {distance} km')
