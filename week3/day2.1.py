# DEFAULT PARAMETERS AND SCOPE

def check_steps(steps, goal = 8000):
    if steps >= goal:
        print(f'{steps} steps - Goal of {goal} hit.')
    else:
        print(f'{steps} steps - Goal of {goal} missed.')

# Override the defauld goal
check_steps(9200, goal = 10000)
check_steps(11500, goal = 10000)
check_steps(8000, goal = 10000)