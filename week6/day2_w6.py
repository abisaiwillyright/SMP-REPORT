# Filtering and Transforming Data
# Filter Rows

import micropip
import pandas as pd

df = pd.DataFrame({
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"],
})

# Days where step goal was hit
goal_days = df[df['steps'] >= 10000]
print('Days with 10k+ steps:\n', goal_days[["day", "steps", "protocol"]].to_string())
print(f"{'-'*50}")

# Days with less than 7.5 hours sleep
low_sleep = df[df['sleep_hr'] < 7.5]
print("Days with less than 7.5 hrs sleep: \n", low_sleep[['sleep_hr']].to_string())
print(f"{'*'*50}")


# Multiple Conditions
# OMAD days with 10k+ steps
omad_goal = df[(df['protocol'] == 'OMAD') & (df['steps'] >= 10000)]
print("OMAD days with 10+ steps:\n", omad_goal[['day', 'steps', 'protocol']].to_string())
print(f"{'-'*50}")

# Days with either goal steps OR 8+ hours sleep
either = df[(df["steps"] >= 10000) | (df["sleep_hr"] >= 8.0)]
print("Days with 10k steps OR 8+ hrs sleep:\n", either[['day', 'steps', 'sleep_hr']].to_string())
print(f"{'*'*50}")



# Filtering with "&" (AND)
# Days with either 10k+ steps OR 8+ hours sleep
step_sleep = df[(df['steps'] >= 10000) & (df['sleep_hr'] >= 8.0)]
print("Days with 10+ steps and 8+ sleep hrs:\n", step_sleep[['day', 'steps', 'sleep_hr']].to_string())
print(f"{'-'*50}")



# Filtering with .isin()
# Days with OMAD and 2MAD
omad_2mad = df[df['protocol'].isin(['OMAD', '2MAD'])]
print("Days with OMAD and 2MAD:\n", omad_2mad[['day', 'protocol', 'steps', 'sleep_hr']].to_string())
print(f"{'*'*50}")




# Adding New Columns
# Boolean column: did we hit the step goal?
df["hit_goal"] = df["steps"] >= 10000

# Numeric column: steps deficit or surplus vs 10k goal
df["steps_vs_goal"] = df["steps"] - 10000

# Category column: sleep rating
df["sleeping"] = df["sleep_hr"].apply(lambda x: "Good" if x >= 8 else "Low")

print(df[["day", "steps", "hit_goal", "steps_vs_goal", "sleeping"]].to_string())
print(f"{'*'*50}")


# Renaming and Dropping Columns
# Rename a column
df = df.rename(columns={'sleep_hr': 'sleep_hours'})
print("After rename:\n", list(df.columns))
print(f"{'-'*50}")

# Drop a column
df = df.drop(columns=['protocol'])
print("After drop:\n", df.to_string())
print(f"{'*'*50}")


# Sorting
# Sort by steps, highest first
ranked = df.sort_values('steps', ascending=False).reset_index(drop=True)
ranked.index = ranked.index + 1  # 1-based ranking

print("step leaderboard:")
for i, row in ranked.iterrows():
    print(f" #{i} {row['day']:10} {row['steps']:,} steps")