# Working with CSV Files

# Reading CSV with csv.reader - reads a CSV file and give you easch row as a list. The row (header) is just anothe line.

import csv
import io

# Simulate CSV content
csv_data = '''name, phone, skill, city
James Omondi,0700000001,welding,Nairobi
Sandra Waweru,0700000002,tilling,Mombasa
Patrick Njiru,0700000003,phone repair,nairobi
Grace Achieng,0700000004,copywriting,Kisumu
Brian Kamau,0700000005,upholstery,Nairobi'''

f = io.StringIO(csv_data)
reader = csv.reader(f) 

next(reader)   # Skip header row


for row in reader:
    print(row)

