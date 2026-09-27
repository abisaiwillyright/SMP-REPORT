# Exercise

import csv
import io

csv_data = """day,steps,protocol
Monday,9200,OMAD
Tuesday,7500,2MAD
Wednesday,10500,OMAD
Thursday,11000,OMAD
Friday,8000,Autophagy Marathom
Saturday,9600,OMAD"""

f = io.StringIO(csv_data)
reader = csv.DictReader(f)

valid_steps = []
for row in reader:
    steps = int(row['steps'])
    if steps >= 7000:
        valid_steps.append(steps)
        print(f"{row['day']}: {steps} steps ({row['protocol']})")
    else:
        print(f"{row['day']}: {steps} steps - flagged as invalid")

avg = sum(valid_steps) / len(valid_steps)
print(f'\nAvarage (valid days): {round(avg)} steps')  