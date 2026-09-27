# Return - getting the value back.

def calculate_avarage_steps(steps_list):
    total = sum(steps_list)
    avarage = total // len(steps_list)
    return avarage

weekly_steps = [9200, 10500, 8800, 11000, 7600, 9400, 10200]
avg = calculate_avarage_steps(weekly_steps)
print('Avarage steps this week:', avg)