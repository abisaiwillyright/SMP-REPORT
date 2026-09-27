daily_steps = [8200, 5100, 11300, 6800, 4200, 10100]
minimum_steps = 8000

#a for a loop to iterate through the daily_steps list and check if each day's steps meet the minimum step goal
for steps in daily_steps:
    if steps >= minimum_steps:
        print(f"Excellent. You have hit your daily step goals of {steps} steps")
    else:
        print(f"Low. You have only walked {steps}, you need to walk more to hit your target")

#a continue statement to skip anyday below 5000 steps and calculate the weekly avarage steps.
total_steps = 0
for steps in daily_steps:
    if steps < 5000:
        print(f"Skipping day with {steps} steps, as is below the minimum steps.")
        continue
    total_steps += steps
avarage_steps = total_steps // len(daily_steps)
print(f"Your avarage steps for the week: {avarage_steps} steps")

#a while loop to coount how many consecutive days from the start hit the target before the first miss of the target.
consecutive_days = 0
i = 0
while i < len(daily_steps) and daily_steps[i] >= minimum_steps:
    consecutive_days +=1
    i = 1
    print(f"You had {consecutive_days} consecutive days, meeting the goal steps.")