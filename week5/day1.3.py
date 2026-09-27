# Looping Through a List Response
# Simulates: response.json() from /api/weekly-logs

weekly_logs = [
    {'day': 'Monaday', 'steps': 9200, 'protocol': 'OMAD'},
    {'day': 'Tuesday', 'steps': 10500, 'protocol': '2MAD'},
    {'day': 'Wednesday', 'steps': 8800, 'protocol': 'OMAD'},
    {'day': 'Thursday', 'steps': 11000, 'protocol': 'OMAD'},
    {'day': 'Friday', 'steps': 7600, 'protocol': '2MAD'}
]

for log in weekly_logs:
    status = 'Goal met' if log['steps'] >= 10000 else 'Short'
    print(f'{log['day']:10} {log['steps']:6} steps {status}')