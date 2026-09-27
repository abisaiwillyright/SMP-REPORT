# JSON Text to Python

import json

# This is what an API response might look like
api_response = '{"steps": 9200, "water_glasses": 8, "cold_shower": true, "protocol": "OMAD"}'

# Convert JSON string to Python dictionary
data = json.loads(api_response)

print('Type:', type(data))
print('Steps:', data['steps'])
print('Cold shower:', data['cold_shower'])
print('Protocol:', data['protocol'])