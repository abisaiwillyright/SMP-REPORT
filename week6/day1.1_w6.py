# A Chicken Farm Weekly Log
import micropip
#await micropip.install('pandas')
import pandas as pd

data = {
    "day":        ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "eggs":       [312, 298, 320, 305, 290, 315, 308],
    "feed_kg":    [18.5, 18.0, 19.2, 18.8, 17.5, 18.6, 19.0],
    "deaths":     [0, 1, 0, 0, 2, 0, 0],
    "pen":        ["A", "A", "A", "B", "B", "B", "A"],
}

df = pd.DataFrame(data)

print('Weekly egg production log:\n', df.to_string())
print('-'*80)

print('Shape:', df.shape)
print('-'*80)
print('Summary statistics:\n', df[["eggs", "feed_kg", "deaths"]].describe().round(1).to_string())
print('-'*80)

print(f"Total eggs this week: {df['eggs'].sum()}")
print(f"Avarage daily eggs: {df['eggs'].mean():.1f}")
print(f"Worst day (eggs): {df.loc[df['eggs'].idxmax(), 'day']} ({df['eggs'].min()} eggs)")
print(f"Best day (eggs): {df.loc[df['eggs'].idxmax(), 'day']} ({df['eggs'].max()} eggs)")
print('-'*80)

print(f"Weekly total revenue (KES): {df['eggs'].sum()*18}  \n{df['eggs']*18}")
print('-'*80)