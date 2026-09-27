# Code Challenge 1 — Tiling Contractor Jobs


#import pyodide_js
#await pyodide_js.loadPackage("micropip")
import micropip 
#await micropip.install("pandas")
import pandas as pd

jobs = [
    {"client": "Kamau", "boxes_used": 30, "price_per_box": 1800},
    {"client": "Mutua", "boxes_used": 48, "price_per_box": 2100},
    {"client": "Odhiambo", "boxes_used": 20, "price_per_box": 1600},
    {"client": "Wanjiru", "boxes_used": 60, "price_per_box": 2200},
]

# calculate and print total boxes laid and total revenue.
df = pd.DataFrame(jobs)

# Total boxes used
print("Total:", df['boxes_used'].sum())

# Clients revenues
result = df["boxes_used"] * df['price_per_box']

print("Revenue: KES", result.sum())
print('\n')

# Code Challenge 2 — Patient Risk Screening
import micropip
#await micropip.install("pandas")
import pandas as pd

patients = [
    {"name": "Alice",  "bp": 155, "glucose": 130, "creatinine": 0.9},
    {"name": "Brian",  "bp": 120, "glucose": 118, "creatinine": 1.5},
    {"name": "Carol",  "bp": 148, "glucose": 142, "creatinine": 1.0},
    {"name": "David",  "bp": 130, "glucose": 110, "creatinine": 0.8},
    {"name": "Eve",    "bp": 160, "glucose": 98,  "creatinine": 1.1},
    {"name": "Frank",  "bp": 125, "glucose": 115, "creatinine": 0.7},
]
df = pd.DataFrame(patients)

# Filter to count how many patients are at risk for each condition.

# Blood pressure above 140 mmHg = hypertension risk.
bp_risk = df[(df["bp"] > 140)]
print("Hypertension risk:", len(bp_risk))

# Blood glucose above 126 mg/dL = diabetes risk.
suger_risk = df[(df['glucose'] > 126)]
print("Diabetes risk:", len(suger_risk))

# Creatinine above 1.2 mg/dL = kidney risk.
k_rsk = df[(df['creatinine'] > 1.2)]
print("Kidney risk:", len(k_rsk))



