# Introduction to NumPy
import micropip
#await micropip.install("numpy")
import numpy as np

# From a python list
steps = np.array([9200, 10500, 8800, 11000, 7600, 9400, 10200])
print('steps array:', steps)
print('type:', type(steps))
print('dtype:', steps.dtype)
print('shape:', steps.shape)

# Zeros and ones
print('\nnp.zeros(5):', np.zeros(5))
print('np.ones(5):', np.ones(5))

# Range of numbers
print('\nnp.arange(1,8):\n', np.arange(1, 8))

# Evenly spaced
print('\nnp.linspace(0,1,5):\n', np.linspace(0,1,5))



# Vectorized Operations
# All at once, no loop needed
goal = 10000
deficit = steps - goal
print("\nSteps vs 10k goal:\n", deficit)

# Percentage of goal achieved
pct = (steps / goal * 100).round(1)
print("\nPercent of goal:\n", pct)

# Boolean mask: which days hit the goal?
hit = steps[steps >= goal]
print('\nHit goal:\n', hit)
print(f"{'='*50}\n")


# Statistical Analysis
# 4 weeks of daily steps (28 days)
steps_28 = np.array([
    9200, 10500, 8800, 11000, 7600, 9400, 10200,
    8900, 10800, 9100, 11200, 7900, 10000, 9700,
    9500, 10300, 8600, 11500, 8200, 9800, 10600,
    9000, 10100, 8400, 10900, 7500, 9600, 10400
])

print(f'28-day steps analysis')
print(f' Mean: {np.std(steps_28):,.0f}')
print(f' Median: {np.median(steps_28):,.0f}')
print(f' Std dev: {np.std(steps_28):,.0f}')
print(f' Min: {np.min(steps_28):,}')
print(f' Max: {np.max(steps_28):,}')
print(f' Total: {np.sum(steps_28):,}')
print(f' 75th percentile: {np.percentile(steps_28,75):,.0f}')
print(f' Days 10k+: {np.sum(steps_28 >= 10000)}/28')
print(f"{'-'*50}")

# Slice and Index Arrays
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print('First 3 days:', steps[:3])
print('Last 2 days:', steps[-2:])
print('Weekdays (Mon-Fri):', steps[:5])
print('Weekend:', steps[5:])
print(f"{'-'*50}")

# Best week start: first day above 10k
first_10k = np.argmax(steps >= 10000)  # index of the first True
print(f' First 10k+ day: {days[first_10k]} with {steps[first_10k]:,} steps')
print(f"{'-'*50}")

# Sort and show progression
sorted_steps = np.sort(steps)
print("Steps sorred low to high:", sorted_steps)
print(f"{'='*50}\n")


# NumPy and pandas Together
import micropip
#await micropip.install('pandas')
#await micropip.install('numpy')
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
})

# Pull a column as a NumPy array
steps_arr = df['steps'].to_numpy()
print('NumPy and pandas Together')
print('NumPay array from pandas column:\n', steps_arr)
print('Type:', type(steps_arr))
print(f"{'-'*50}")

# Use NumPy on it.
print(f'Meaan {np.mean(steps_arr):,.0f}')
print(f'Std dev: {np.std(steps_arr):,.0f}')
print(f"{'-'*50}")


# Add a normalized column back to the DataFrame
# Normalize to 0-1 range (min-max scaling)
df['steps_norm'] = (df['steps'] - df['steps'].min()) / (df['steps'].max() - df['steps'].min())
df['steps'] = df['steps_norm'].round(3)
print('With normolized steps:\n', df[['day', 'steps', 'steps_norm']].to_string())




