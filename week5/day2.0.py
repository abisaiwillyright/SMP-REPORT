# Navigate Nested Structure

response = {
    'status': 'success',
    'user': {
        'id': 42,
        'name': 'Kevin Minodi',
        'location': {
            'city': 'Kisumu',
            'country': 'Kenya'
        }
    },
    'today': {
        'steps': 10800,
        'cold_shower': True,
        'fasting': {
            'protocol': 'OMAS',
            'window_hours': 23
        },
        'workout': {
            'complated': True,
            'bench_press_kg': 90,
            'duration_minutes': 55
        }
    }
}

# Navigate layer by layer
name = response['user']['name']
city = response['user']['location']['city']
steps = response['today']['steps']
protocol = response['today']['fasting']['protocol']
bench = response['today']['workout']['bench_press_kg']

print(f'Name: {name}')
print(f'City: {city}')
print(f'steps: {steps}')
print(f'protocol: {protocol}')
print(f'Bench: {bench} kg')