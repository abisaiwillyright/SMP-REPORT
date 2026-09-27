# Chicken farm Egg collection Log

import io

# Daily egg collection log: pen, eggs_collected, feed_kg

farm_log = '''pen A,240,12
pen B,185,10
pen C, 310,15
pen D,92,8
pen E,275,13
pen F,318,17'''

total_eggs = 0
total_feed = 0
low_pens = []

print('====DAILY CHICKEN FARM EGGS COLLECTION LOG====')
f = io.StringIO(farm_log)
for line in f:
    line = line.strip()
    if line:
        pen, eggs, feed = line.split(',')
        eggs = int(eggs)
        feed = int(feed)
        efficiency = eggs / feed
        status = 'Good' if eggs >= 200 else "Low yield"

        print(f'{pen}: {eggs} eggs | {feed}kg feed | {efficiency:.1f} eggs/kg [{status}]')

        total_eggs += eggs
        total_feed += feed
        if eggs < 200:
            low_pens.append(pen)

print('\n==== DATA SUMMARY ====')
print(f'Total eggs: {total_eggs}')
print(f'Total feed used: {total_feed}kg')
print(f'pens needing attention: {', '.join(low_pens)}')
