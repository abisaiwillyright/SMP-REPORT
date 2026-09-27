# Using .get() for Missing Keys

records = [
    {'name': 'Patrick Achenya', 'steps': 9100, 'water_glasses': 7},
    {'name': 'Grace Jumba', 'steps': 8400},
    {'name': 'Brian Sunguti', 'steps': 10200, 'water_glasses': 9}
]

for r in records:
    water = r.get('water_glasses', 'not logged')
    print(f'{r['name']}: steps = {r['steps']}, water = {water}')
    