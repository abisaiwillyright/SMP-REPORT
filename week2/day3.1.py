#Creating dictionary.

daily_log = {'steps': 9200, 'water_glasses':8, 'cold shower': True, 'fasting_protocal': 'OMD', 'sleep_hours': 7.5}
print(daily_log)


#Accessing values in the dictionary.
print('Steps today:', daily_log['steps'])
print('Protocal:', daily_log['fasting_protocal'])
print('Cold shower:', daily_log['cold shower'])
print('Sleep time:', daily_log['sleep_hours'])


#Add new key in the dictionary.
daily_log['pages_read'] = 30
print('After adding pages_read:', daily_log)


#Update an existing key in the dictionary.
daily_log['steps'] = 10400
print('After updating steps:', daily_log)


#Deleting a key from the dictionary.del daily_log['fasting_protocal'
del daily_log['fasting_protocal']
print('After deleting fasting_protocal:', daily_log)


#Checking if a key exists.
if 'steps' in daily_log:
    print('Steps recorded:', daily_log['steps'])

if 'sleep_hours' not in daily_log:
    print('Sleep hours not logged yet,')


#Looping through key and values together.
for key, value in daily_log.items():
    print(key, ':', value)