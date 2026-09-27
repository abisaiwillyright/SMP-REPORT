# Project: Modular Calculator
# Project: Fitness and Discipline Calculator

import math
def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return bmi

def bmi_category(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif bmi < 25:
        return 'Normal weight'
    elif bmi < 30:
        return 'Overweight'
    else:
        return 'Obesity'


# Test
print("----BMI Calculator----")
weight = 84 #kg
height = 1.78 #m
bmi = calculate_bmi(weight, height)
print(f'Weight: {weight} kg')
print(f'Height: {height} m')
print(f'BMI: {bmi:.1f}')  # Rounded to 1 decimal place
print(f'Status: {bmi_category(bmi)}')
