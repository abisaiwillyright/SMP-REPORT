week_log = [{'day': 'Monday', 'steps': 9200, 'protocal': 'OMAD'},
            {'day': 'Tuesday', 'steps': 10500, 'protocal': '2MAD'},
            {'day': 'Wednesday', 'steps': 8800, 'protocal': 'OMAD'},
            {'day': 'Thursday', 'steps': 11000, 'protocal': 'Autophagy marathon'},
            {'day': 'Friday', 'steps': 7600, 'protocal': 'OMAD'}]
total = 0
for log in week_log:
    print(log['day'], '|', log['steps'], '|', log['protocal'])
    total += log['steps']

avarage = total / len(week_log)
print()
print('Avarage steps:', avarage)
