# try and except

steps_data = ['two hundred', '92000', '7500', '8800', '6900']
for item in steps_data:
    try:
        steps = int(item)
        if steps >= 8000:
            print(steps, '- Gola hit')
        else:
            print(steps, '- Below goal')

    except ValueError:
        print(f" '{item}', is not a valid number, Skipping.")
