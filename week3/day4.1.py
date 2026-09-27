# List Comprehensions

# Building Lists with Loops
weekly_steps = [7500, 92000, 10500, 9600, 11000, 6900]
goal_days = []
for steps in weekly_steps:
    if steps >= 8000:
        goal_days.append(steps)
print('Day targets:', goal_days)
print('--------------------')

# Another alternative to the above code using list comprehension
goal_days = [steps for steps in weekly_steps if steps >= 8000]
print('Day targets:', goal_days)

print('=======================')

# Transforming Items
# Convert each step count to km assuming 1.3km per 1000 steps
km_walked = [round(s * 1.3 / 1000, 2) for s in weekly_steps]
print('Distance walked in km:', km_walked)
print('steps:', weekly_steps)
print('--------------------')


# Convert each step count to calories burned assuming 0.04 calories per step
calories_burned = [round(s * 0.04, 2) for s in weekly_steps]
print('Calories burned:', calories_burned)
print('steps:', weekly_steps)
print()


# Comprehension vs Loop: When to Use Which
# Build a list of status strings for each day
print('========= STATUS LIST ========')
status = ['Goal hit' if steps >= 8000 else 'Below goal' for steps in weekly_steps]
for i, s in enumerate(status):
    print(f'Day {i + 1}: {weekly_steps[i]} steps - {s}')