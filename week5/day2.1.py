# Extracting Fields from a List of Records
# Raw API response: list of full user records

import requests

raw = [
    {'id': 1, 'name': 'James Omondi', 'email': 'james@smp.ke', 'steps': 9200, 'protocol': 'OMAD', 'sleep': 7.5, 'active': True},
    {'id': 2, 'name': 'Sandra Weru', 'email': 'sandra@smp.ke', 'steps': 10500, 'protocol': '2MAD', 'sleep': 8.0, 'active': True},
    {'id': 3, 'name': 'Patrick Njiru', 'email': 'Njiru@smp.ke', 'steps': 8100, 'protocol': 'OMAD', 'sleep': 6.5, 'active': False},
    {'id': 4, 'name': 'Grace Achieng', 'email': 'ga@smp,ke', 'steps': 11000, 'protocol': 'OMAD', 'sleep': 7.0, 'active': True},
    {'id': 5, 'name': 'Brian Kamau', 'email': 'bk@smp.ke', 'steps': 7400, 'protocol': '2MAD', 'sleep': 9.0, 'active': True}
]

# Extract only active users with name, steps, protocol
clean = [
    {
        'name': r['name'],
        'steps': r['steps'],
        'protocol': r['protocol']
    }
    for r in raw if r['active']
]
for record in clean:
    print(f"{record['name']:20} {record['steps']:6}' steps {record['protocol']}")