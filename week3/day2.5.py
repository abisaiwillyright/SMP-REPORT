def calculate_bmi(weight_kg, height_m):
    bmi=weight_kg / (height_m **2)
    return round(bmi, 1)

def bmi_category(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif bmi < 25:
        return 'Normal'
    elif bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'

weight = 84
height = 1.78
bmi = calculate_bmi(weight,height)
category = bmi_category(bmi)

print(f'Weight: {weight}kg | Height: {height}m')
print(f'BMI: {bmi} | Category: | {category}')