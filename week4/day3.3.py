# Working with JSON Files

import json
# Simulate writing
daily_log = {
    'steps': 9200,
    'water_glasses': 8,
    'cold_shower': True,
    'sleep_hours': 7.5
}

json_string = json.dumps(daily_log, indent=2)
print('Saved JSON:', json_string)


# Simulate reading it back
loaded_data = json.loads(json_string)
print('\nRead back as Python dictionary:')
for key, value in loaded_data.items():
    print(f' {key}: {value}')