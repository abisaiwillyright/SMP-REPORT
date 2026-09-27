# Reading with Dctionary Reader

import csv
import io

csv_data = """name,steps,water,protocol,cold_shower
Jame Omondi,9200,8,OMAD,True
Sandra Weru,10500,9,2MAD,True
Patrick Njiru,7600,6,OMAD,False
Grace Jumba,1100,8,Autophagy Marathon,True"""

f =io.StringIO(csv_data)
reader = csv.DictReader(f)

for row in reader:
    steps = int(row['steps'])
    status = 'Goal hit' if steps >= 8100 else 'Below goal'
    print(f'{row['name']}: {steps} steps | {row['protocol']} | {status}')
    