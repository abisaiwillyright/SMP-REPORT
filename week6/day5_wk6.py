# Project: Data Analysis Report

import micropip
#await micropip.install('pandas')
#await micropip.install('numpy')
import pandas as pd
import numpy as np

#Step 1: Load and Inspect the Data
# 28 days of SMP fitness log
data = {
    "day":      list(range(1, 29)),
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200,
                 8900, 10800, 9100, 11200, 7900, 10000, 9700,
                 9500, 10300, 8600, 11500, 8200, 9800, 10600,
                 9000, 10100, 8400, 10900, 7500, 9600, 10400],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0,
                 6.0, 8.5, 7.0, 7.5, 9.0, 7.0, 7.5,
                 7.0, 8.0, 6.5, 7.5, 8.0, 7.0, 8.5,
                 7.0, 7.5, 6.5, 8.0, 9.5, 7.0, 8.0],
    "water":    [7, 8, 6, 9, 8, 7, 8, 6, 9, 8, 8, 7, 9, 8,
                 7, 8, 6, 9, 8, 7, 9, 8, 8, 6, 9, 7, 8, 9],
    "protocol": (["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"] * 4),
    "cold_shower": ([True, True, False, True, True, True, True,
                     False, True, True, True, True, False, True] * 2),
    "bench_kg": [80, 82, 78, 85, 80, 83, 84,
                 81, 85, 80, 86, 79, 84, 83,
                 82, 86, 79, 88, 81, 85, 87,
                 82, 86, 80, 87, 79, 84, 86],
}

df = pd.DataFrame(data)

print(f'Shape: {df.shape}')
print(f'\nColumns: {list(df.columns)}')
print(f'\nData types:\n', df.dtypes)
print(f'\nMissing values: {df.isna().sum()}')
print(f'\nFirst 3 rows:\n', df.head(3).to_string())
print(f"{'='*50}\n")


# Step 2: Filter and Analyze
# High-performance days: 10k+ steps AND 7.5+ hours sleep
high_perfomance = df[(df['steps'] >= 10000) & (df['sleep_hr'] >= 7.5)]
print(f"High performance days: {len(high_perfomance)}/28")


# Protocol comparison
print('\nMetrics by fasting protocol:')
protocol_stats = df.groupby('protocol').agg(
    avg_steps=('steps', 'mean'),
    avg_sleep=('sleep_hr', 'mean'),
    avg_bench=('bench_kg', 'mean'),
    avg_water=('water', 'mean'),
    days=('day', 'count')
).round(1)

print(protocol_stats)
print(f"{'='*50}\n")



# Step 3: NumPy Analysis
print("****28-Day NumPy Analysis****")

steps1 = df['steps']
print(f'\nSteps:')
print(f' Mean:          {np.mean(steps1):,.0f}')
print(f' Std dev:       {np.std(steps1):,.0f}')
print(f' 25th pctile:   {np.percentile(steps1, 25):,.0f}')
print(f' 75th pctile:   {np.percentile(steps1, 72):,.0f}')
print(f' Day 10+:       {np.sum(steps1 >= 10000)}/28')

bench = df['bench_kg']
print(f'\nBench press:')
print(f' mean:    {np.mean(bench):.1f} kg')
print(f' Max:     {np.max(bench)} kg (Day {np.argmax(bench)+1})')
print(f' Trend:   {'inceasing' if bench[-7:].mean() else 'flat/decresing'}')


# Correlation: do more steps correlate with better bench?
corr = np.corrcoef(steps1, bench)[0,1]
print(f'\nCorrelation steps vs bench: {corr:.3f}')
print('Interpretation:', 'positive relationship' if corr > 0.3 else 'Weak/no relation')
print(f"{'='*50}")



# Step 4: Full Report
W = 54
print('='*W)
print(' SMP 28-DAY FITINESS ANALYSIS REPORT')
print('-'*W)


# Overall stats
print(f'OVERALL METRICS')
print(f" {'Days tracked:':<25} 28")
print(f" {'Total steps:':<25} {steps1.sum():,}")
print(f" {'Avg daily:':<25} {steps1.mean():,.0f}")
print(f" {'Days hitting 10k:':<25} {(steps1 >=10000).sum()}/28 ({(steps1 >= 10000).mean()*100:,.0f}%)")
sleep = df['sleep_hr']
print(f" {'Avg sleep:':<25} {np.mean(sleep):,.1f} hrs")
print(f" {'Bench press range:':<25} {bench.min()} to {bench.max()} kg")
print(f" {'Bench press trend:':<25} + {bench[-7:].mean() - bench[:7].mean():.1f} kg (wk1 to wk4)")
print('-'*W)


# Week-by-week
print(f"\n WEEKLY BREAKDOWN")
print(f" {'Week':<8} {'Avg Steps':>12} {'10k Days':>8} {'Avg Bench':>10}")
print(f" {'-'*44}")
for wk in range(4):
    s = steps1[wk*7:(wk+1)*7]
    b = bench[wk*7:(wk+1)*7]
    hits = (s >= 10000).sum()
    print(f" Week {wk+1:<3} {s.sum():>12,.0f} {hits:>8}/7 {b.mean():>9.1f} kg")
print(f"{'-' * W}")


# Protocol breakdown
print(f" PROTOCOL COMPARISON")
proto_stats = df.groupby("protocol")[["steps", "sleep_hr", "bench_kg"]].mean().round(1)
for proto, row in proto_stats.iterrows():
    print(f"  {proto}: avg steps={row['steps']:,.0f}, sleep={row['sleep_hr']}h, bench={row['bench_kg']}kg")
print(f"{'-' * W}")


# Top days
top3 = df.nlargest(3, "steps")
print(f" TOP 3 STEP DAYS")
for _, row in top3.iterrows():
    print(f"  Day {int(row['day']):2d}: {int(row['steps']):,} steps  ({row['protocol']})")

print(f"\n{'=' * W}")