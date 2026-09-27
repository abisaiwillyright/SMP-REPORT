# Reading and Writing Files


import io

# Simulating file write using in-memory buffer
file_content = io.StringIO()
file_content.write('Steps: 9200\n')
file_content.write('Water: 8 glasses\n')
file_content.write('Protocol: OMAD\n')
file_content.write('Cold shower: Yes')
file_content.write('Sleep hours: 7.5')

print('File written.contents:')
print(file_content.getvalue())


