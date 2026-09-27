# Complete Fitness and Discipline Report

import math
from datetime import date

# -------------- DATA COLLECTION --------------
client_name = 'James'
weight_kg = 84
height_m = 1.78
weekly_steps = [9200, 7500, 10500, 8800, 6900, 11000, 9600]
protocols = ['OMAD', '2MAD', 'OMAD', 'Autophagy Marathon', 'OMAD', '2MAD', 'OMAD', 'Autophagy Marathon']
step_goal = 8000

# -------------- FUNCTIONS --------------
def calculate_bmi(weight_kg, height_m):
    return round(weight_kg / (height_m ** 2), 1)

def bmi_category(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif bmi < 25:
        return 'Normal weight'
    elif bmi < 30:
        return 'Overweight'
    else:
        return 'Obesity'

def weekly_step_summary(steps_list, goal=8000):
    return {
        'days_hit': len([s for s in steps_list if s >= goal]),
        'average': sum(steps_list) // len(steps_list),
        'best': max(steps_list),
        'worst': min(steps_list),
        'total_days': len(steps_list)
    }

def estimated_calories(steps):
    return math.floor(steps * 0.04)

def protocol_summary(protocol_list):
    return {protocol: protocol_list.count(protocol) for protocol in set(protocol_list)}

# -------------- REPORT GENERATION --------------
today = date.today().strftime("%B %d, %Y")
bmi = calculate_bmi(weight_kg, height_m)
steps_report = weekly_step_summary(weekly_steps, step_goal)
protocol_report = protocol_summary(protocols)
total_calories = sum(estimated_calories(steps) for steps in weekly_steps)

print(' = ' * 35)
print(f' WEEKLY REPORT: {client_name.upper()}')
print(f' Date: {today}')
print(' = ' * 35)
print(f' \nBODY')
print(f' Weight: {weight_kg} kg')
print(f' BMI: {bmi} ({bmi_category(bmi)})')
print(f' \nSTEPS (Goal: {step_goal})')
print(f' Days on goal: {steps_report["days_hit"]} / {steps_report["total_days"]}')
print(f' Average steps: {steps_report["average"]}')
print(f' Best day: {steps_report["best"]} steps')
print(f' Worst day: {steps_report["worst"]} steps')
print(f' calories burned from walking: {total_calories} kcal')
print(f' \nPROTOCOLS')
for protocol, days in protocol_report.items():
    print(f' {protocol}: {days} day(s)')
print('' + ' = ' * 35)