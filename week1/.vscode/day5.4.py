daily_steps = [3200,7100, 9800, 4100, 10500, 6400]
minimum = 7000

total = 0
valid_days = 0

for steps in daily_steps:
    if steps < minimum:
        print(f"skipping {steps} (below minimum)")
        continue  #skip this day, go to next.
total += steps
valid_days +=1

print(f"\nValid days: {valid_days}")
print(f"Total steps (valid_days): {total}")
print(f"Avarage: {total // valid_days}")