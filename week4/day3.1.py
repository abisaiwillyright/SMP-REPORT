# Working with JSON

# Python to JSON Text
import json

daily_log = {
    'steps': 9200,
    'water_glasses': 8,
    'cold_shower': True,
    'fasting_protocol': 'OMAD',
    'sleeping_hours': 7.5
    }
# Convert to JSON string
json_text = json.dumps(daily_log)
print('Type:', type(json_text))
print('JSON:', json_text)

# Pretty print with indentation
pretty = json.dumps(daily_log, indent=2)
print('\nPretty JSON:', pretty)
