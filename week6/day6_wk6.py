# Assignments
# Exercise 1: DataFrames
# Create a DataFrame from a dictionary and inspect it

import pandas as pd
data = {
    "name": ["Eric", "James", "Amina", "Sara", "Abisai"],
    "score": [85, 72, 91, 68, 96],
    "city": ["Nairobi", "Mombasa", "Nairobi", "Kisumu", "Nairobi"]
}
df = pd.DataFrame(data)
print(f"\n       STUDENTS SCORES")
print(f"{'-'*50}")
print(df)
print("\nShape:", df.shape)
print(f"{'='*50}\n")



# Exercise 2: Filtering
# Filter to show only students from Nairobi with score above 80
result = df[(df['city'] == 'Nairobi') & (df['score'] > 80)]
print("Nairobi students above 80:\n", result)
print(f"{'='*50}\n")



# Exercise 3: Grouping
# Group by city and get the average score per city
print("Average city scores:\n", df.groupby('city')['score'].mean())
print(f"{'='*50}\n")



# Exercise 4: NumPy Challenge
# Create an array of 10 random integers between 1 and 100
# Print the mean, max, min, and standard deviation

import numpy as np
arr = np.array([23, 67, 45, 89, 12, 56, 78, 34, 90, 41])
print(f"Mean:    {arr.mean():.2f}")
print(f"Max:     {arr.max()}")
print(f"Min:     {arr.min()}")
print(f"STD:     {arr.std():.2f}")


# Total scores
print(f"\nTotal score:", df["score"].sum())
print(f"Mean score:", df["score"].mean())

