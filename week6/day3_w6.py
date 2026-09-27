# Grouping and Aggregation
# Basic Groupby
import micropip
#await micropip.install('pandas')
import pandas as pd

df = pd.DataFrame({
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200,],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"],
    "name":     ["James", "Sandra", "Patrick", "Grace", "Brian", "Kevin", "James"],
    "city":     ["Nairobi", "Mombasa", "Nairobi", "Kisumu", "Nairobi", "Mombasa", "Nairobi"]
})
# Average steps per fasting protocol
grouped = df.groupby('protocol')['steps'].mean().round()
print('Average steps by protocol:\n', grouped)

# Total steps per protocol
totals = df.groupby('protocol')['steps'].sum()
print('\nTotal steps by protocol:\n', totals)
print(f"{'-'*50}")



# Common Aggregation Functions
# Multiple aggregations on steps by city
city_stats = df.groupby('city')['steps'].agg(['mean', 'max', 'min', 'count']).round(0)
print("Steps statistics by city:\n", city_stats)
print(f"{'-'*50}")


# Grouping Multiple Columns at Once
# Average steps grouped by both city and protocol
beakdown = df.groupby(['city', 'protocol'])['steps'].mean().round(0)
print("average steps by city and protocol:\n", beakdown)
print(f"{'-'*50}")


# value_counts()
print("Protocol distribuiton:\n", df['protocol'].value_counts())
print("\nCity distribution:\n", df['city'].value_counts())
print(f"{'-'*50}")


# Handling Missing Data
import numpy as np

df = pd.DataFrame({
    "name":     ["James", "Sandra", "Patrick", "Grace", "Brian"],
    "steps":    [9200, None, 8100, 11000, None],
    "sleep_hr": [7.5, 8.0, None, 7.0, 9.0],
})

print("Original with NaN:\n", df.to_string())

# Fill missing steps with the column mean
df['steps'] = df['steps'].fillna(df["steps"].mean())
df['sleep_hr'] = df['sleep_hr'].fillna(df['sleep_hr'].median())

print('\nAfter filling NaN:\n', df.to_string())
print(f"{'-'*50}")

