# Carpentry workshop daily log: day, chair made, timber used (metres)

import io

workshop_log = """monday,8,24
Tuesday,6,18
Wednesday,10,30
Thursady,7,21"""

total_chairs = 0
total_timber = 0
days = 0

f = io.StringIO(workshop_log)
print('===CARPENTY WORKSHOP LOG===')
for line in f:
    line = line.strip()
    if line:
        day, chairs, timber = line.split(',')
        chairs = int(chairs)
        timber = int(timber)
        print(f'{day}: {chairs} chairs | {timber}m timber')
        total_chairs += chairs
        total_chairs += timber
        days += 1

print('\n=======SUMMARY LOG======')
print(f'Total chairs made: {total_chairs}')
print(f'Total timber used: {total_timber}m')
print(f'Avarage chairs pre day: {total_chairs // days}')
