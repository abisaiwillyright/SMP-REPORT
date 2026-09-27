# Defining and calling a funtion

# Define the function
def show_daily_goal():
    print('Step goal:, 8000 steps')
    print('Water goal: 8 glasses')
    print('Cold shower: yes')


# call the function
show_daily_goal()
print('---')
show_daily_goal()  # Call it again
print()

# Parameters - Passing information in
def  check_steps(steps):
    if steps >= 10000:
        print(steps, 'steps - Goal exceeded')
    elif steps >= 8000:
        print(steps, 'steps - Goal hit')
    else:
        print(print, 'steps - Below goal')


# Call with diffarent values
print()
check_steps(9200)
check_steps(7500)
check_steps(11000)