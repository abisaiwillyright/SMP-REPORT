# Simulates what response.json() returns from a fitnes API

data = {
    'user_id': 1,
    'name': 'James Opondo',
    'date': '2024-11-18',
    'steps': 9200,
    'water_glasses': 8,
    'cold_shower': True,
    'fasting_protocol': 'OMAD',
    'sleeping_hours': 7.5,
    'workout_competed': True
}

print('Name:', data['name'])
print('Steps:', data['steps'])
print('Protocol:', data['fasting_protocol'])
print('Cold Shower:', data['cold_shower'])
print('Sleep:', data['sleeping_hours'], 'hours')