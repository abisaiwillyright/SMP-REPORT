import io

# Simulate file content

file_data = '''Steps: 9200
Water: 8 glasses
Protocol: OMAD
Cold shower: Yes
Sleep hours: 7.5'''

# Simulate reading the whole file
f = io.StringIO(file_data)
content = f.read()
print('Full file content:')
print(content)
print('='*30)

# Reading Line by Line
f = io.StringIO(file_data)
lines = f.readlines()

print(f'\nNumber of lines: {len(lines)}')
print()

for line in lines:
    line = line.strip()  # Remove new line character at the end.
    print('Line:', line)
print('='*30)


# Simulate append
file_data += '\nPages read: 30\n'
file_data += 'Workout: bench press 5*5 at 80kg'

print('\nFile after appending:')
print(file_data)
print('='*30)

# Processing file data
log = {}
f =io.StringIO(file_data)
for line in f:
    line = line.strip()
    if ':' in line:
         key, value =line.split(':', 1)
         log[key.strip()] = value.strip()

print('\nParsed log:')
for key, value in log.items():
    print(f' {key}: {value}')