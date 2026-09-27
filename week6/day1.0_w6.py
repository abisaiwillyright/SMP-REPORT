# Creating a DataFrame

import micropip
#await micropip.install("pandas")
import pandas as pd

data = {
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"],
    "cold_shower": [True, True, False, True, True, True, True]
}

df = pd.DataFrame(data)
print(df.to_string())
print(f'\n{'*'*80}')



# Inspecting a DataFrame
print('Shape (rows, cols):', df.shape)
print('\nColumns:', list(df.columns))
print('\nData types:\n', df.dtypes)
print('\nFirst 3 rows:\n', df.head(3).to_string())
print(f'\n{'*'*80}')



# Selecting Columns
# Single column (returns a Series)
# Multiple columns (return a DataFrame).
print('Steps column:\n', df['steps'])
print(f'{'-'*80}')

print('Steps and protocol:\n', df[['steps', 'protocol']].to_string())
print(f'\n{'*'*80}')


# Selecting Rows
# iloc: by position
print('First row (iloc[0]):\n', df.iloc[0])
print(f'{'-'*80}')

print('Rows 0 to 2 (iloc[0:3]):\n', df.iloc[0])
print(f'{'-'*80}')

print('\nLast row (iloc[-1]):\n', df.iloc[-1])
print(f'\n{'*'*80}')



# Basic Statistics with describe()
print('Statistics for all numeric columns:\n', df.describe().to_string())
print(f'{'-'*80}')

print('Manual checks:')
print(f"Mean steps: {df['steps'].mean():.0f}")
print(f"Max steps: {df['steps'].max()}")
print(f"Min steps: {df['steps'].min()}")
print(f"Total steps: {df['steps'].sum()}")



