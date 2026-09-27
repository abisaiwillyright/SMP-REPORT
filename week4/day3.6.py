import json

# EXERCISE

week_report = {'name': 'Jame', 
               'steps': [9200, 10500, 8800, 7600, 11000],
               'protocol': ['OMAD', '2MAD', 'Autophagy Marathon', 'OMAD']}

# Convert to JSON
json_str = json.dumps(week_report, indent=2)
print('\nJSON output:')
print(json_str)

# load back and calculate avarage
loaded = json.loads(json_str)
avg = sum(loaded['steps']) / len(loaded['steps'])
print(f'\nAvarage steps for {loaded['name']}: {round(avg)}\n')