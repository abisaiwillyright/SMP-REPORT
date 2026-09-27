# Dairy log: cow_name, morning_litres, evening_litres

import io

milk_log = """Maridadi,6.5,7.2
Mrembo,4.2,4.8
Bella,4.11,4.8
Rosa,3.2,3.5
Lola,7.8,8.4"""

total_herd = 0
low_producers = []
print('========== DAIRY LOG ==========')

f = io.StringIO(milk_log)
for line in f:
    line = line.strip()
    if line:
        name, morning, evening = line.split(',')
        daily = float(morning) + float(evening)
        status = 'OK' if daily >= 10 else 'LOW'
        print(f'{name}: {daily} litres [{status}]') 
        total_herd += daily
        if daily < 10:
            low_producers.append(name)
print('\n======= SUMMARY PRODUCE =======')
print(f'Herd total: {total_herd:.1f} litres')
print(f'Low producers: {', '.join(low_producers) if low_producers else 'None'}')