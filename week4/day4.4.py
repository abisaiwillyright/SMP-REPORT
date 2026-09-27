# Writing with Dictionary Writer (csv.DictWriter)

import csv
import io

clients = [
    {'name': 'James', 'skill': 'welding', 'city': 'Nairobi', 'session': 4},
    {'name': 'Timothy', 'skill': 'tilling', 'city': 'Nairobi', 'session': 4},
    {'name': 'Caroline', 'skill': 'copywriting', 'city': 'Kisumu', 'session': 3},
    {'name': 'cynthia', 'skill': 'writting', 'city': 'Mombasa', 'session': 2}
]

output = io.StringIO()
fieldnames = ['name', 'skill', 'city', 'session']
writer = csv.DictWriter(output, fieldnames=fieldnames)

writer.writeheader()
writer.writerows(clients)

print(output.getvalue())