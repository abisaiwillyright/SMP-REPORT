# Variable Scope

step_goal = 8000  # Global variable

def check_today(steps): 
    result = 'hit' if steps >= step_goal else 'missed'  # result is local
    print(f'Goal {result}: {steps} steps')

check_today(9200)
check_today(7000)

# This would cause an error - result not exist here:
# print(result)