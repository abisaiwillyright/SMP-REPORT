my_log = {'steps': 10500, 'water_glasses': 8, 'fasting_protocal': '2MAD', 'cold_shower': True, 'sleep_hours': 7.0}
print('My profile')
for key, value in my_log.items():
    print(key, ':', value)

print()
if my_log['steps'] >= 8000:
    print('Step target achieved, you are doing better.')

else:
    print('Step target missed, you need to walk more.' )