# Exercise

def safe_log_entry(data):
    try:
        steps = int(data['steps'])
    except (ValueError, TypeError, KeyError):
        print('Invalid steps data. Skipping entry.')
        return None
    water = data.get('water', 0)
    protocol = data.get('protocol', 'Unknown')

    print(f'Steps: {steps} | Water: {water} glasses | Protocal: {protocol}')
    return steps

entries = [
    {'steps': '9200', 'water': 8, 'protocal': 'OMAD'},
    {'steps': 'bad', 'water': 7, 'protocol': '2MAD'},
    {'steps': '8000', 'protocol': 'OMAD'},
    {'steps': '11000', 'water': 9}]

results = [safe_log_entry(e) for e in entries]
valid = [r for r in results if r is not None]
print(f'\nValid entries: {len(valid)}')