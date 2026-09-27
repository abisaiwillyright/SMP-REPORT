# Write a program that saves your name and city to a text file
# Then reads it back and print it

import tempfile
import os

path = tempfile.mktemp(suffix='.txt')
with open(path, 'w') as f:
    f.write('Name: Abisai\nCity: Kisumu\n')
with open(path) as f:
    print(f.read())