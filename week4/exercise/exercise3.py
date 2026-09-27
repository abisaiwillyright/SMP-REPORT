# Create a python dictionary and convert it to JSON
# Then parse it back and access a value

import json
data = {'name': 'Abisai', 'age': 30, 'city': 'Kisumu'}
json_str = json.dumps(data, indent=2)
print(json_str)
parsed = json.loads(json_str)
print(f'Name: {parsed['name']}')
