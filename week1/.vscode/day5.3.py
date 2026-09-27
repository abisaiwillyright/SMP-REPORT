daily_steps = [3200, 7100, 9800, 10500, 6400, 11200]
target = 10000

for steps in daily_steps:
    print(f"checking: {steps} steps")
    if steps >= target:
        print(f"Target hit on this day: {steps} steps. stopping search.")
        break