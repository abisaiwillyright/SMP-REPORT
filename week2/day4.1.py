#Nested data

#A list of dictionary

week_log = [{'day': 'Monday', 'steps': 9200, 'protocal': 'OMD', 'cold_shower': True},
            {'day': 'Tuesday', 'steps': 10500, 'protocal': '2MAD', 'cold_shower': True},
            {'day': 'Wednesday', 'steps': 8800, 'protocal': 'OMAD', 'cold_shower': False},
            {'day': 'Thursady', 'steps': 11000, 'protoca': 'Autophagy', 'cold_shower': True},
            {'day': 'Friday', 'steps': 7600, 'protocal':'OMAD', 'cold_shower': True}]
print(week_log)


#Accessing values inside Nested data

week_log[0]['steps']  #Steps from the first day (Monday)
week_log[2]['day']   #Day name of the third record (Wednesday)


#First day's step count
print('Monday steps:', week_log[0]['steps'])


#Third day's protocal
print('Wednesday protocal:', week_log[2]['protocal'])

#Second day, all the details
print('Tuesday log:', week_log[1])


#Looping through a list of dictionaries
for log in week_log:
    status = 'Goal hit' if log['steps'] >= 8000 else 'Below goal'
    print(log['day'], '-', log['steps'], 'steps -', status)