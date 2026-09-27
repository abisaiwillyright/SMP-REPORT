# Save a list of 3 students (name, score) to JSON
# Read it back and print only students who scored above 70

import json, tempfile

students = [
    {'name': 'Abisai', 'score': 85},
    {'name': 'Omondi', 'score': 62},
    {'name': 'Fred', 'score': 93}
]
path = tempfile.mktemp(suffix='.json')
with open(path, 'w') as f:
    json.dump(students, f)
with open(path) as f:
    loaded = json.load(f)
for s in loaded:
    if s['score'] > 70:
        print(f'{s['name']}: {s['score']}')