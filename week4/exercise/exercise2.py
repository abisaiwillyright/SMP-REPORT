# Wrap a division operation in try/except
# Handle ZeroDivisionError and ValueError separately

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Cannot divide by zero'
    except ValueError as e:
        return f'Invalid input: {e}'

print(safe_divide(10, 2))
print(safe_divide(10, 0))