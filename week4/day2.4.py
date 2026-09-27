# Else and Funally

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print('Cannot divide by zero.')

    else:
        print(f'{a} / {b} = {result}')

    finally:
        print('(Calculation attempted)')
    print()

safe_divide(100, 4)
safe_divide(100, 0)
safe_divide(9200, 7)