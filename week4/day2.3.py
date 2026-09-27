# Catching Specific Error Types

def calculate_avarage(steps_list):
    try:
        total = sum(steps_list)
        avg = total / len(steps_list)
        return round(avg)
    except ZeroDivisionError:
        print('Error: List is empty. Cannot calculate avarage.')
        return 0
    except TypeError:
        print('Error: List contains no-numeric values.')
        return 0
print('Avarage:', calculate_avarage([9200, 10500, 8800, 11000]))
print('Avarage:', calculate_avarage([9200, 'eight thousand', 10500]))