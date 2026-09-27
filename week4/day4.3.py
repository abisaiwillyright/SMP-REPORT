# Writing CSV with csv.writer

import csv
import io

output = io.StringIO()
writer = csv.writer(output)

# Write header
writer.writerow(['name', 'steps', 'protocol', 'goal_hit'])

# Wrute data rows
data = [
    ['Jame', 9200, 'OMAD', True],
    ['Sandra', 10000, '2MAD', True],
    ['Patricia', 7600, 'OMAD', False],
    ['Jumba', 11000, 'Autophagy Marathon', True]]

for row in data:
    writer.writerow(row)

print('General CSV:')
print(output.getvalue())