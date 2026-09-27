# Exercise
people = [{'name': 'Joseph', 'steps': [9200, 10500, 8800, 11000, 76000, 9400, 10200]},
          {'name': 'Maria', 'steps': [7500, 9200, 10500, 9600, 11000, 6900, 8000]},
            {'name': 'John', 'steps': [5000, 6000, 7000, 8000, 9000, 10000, 11000]},
            {'name': 'David', 'steps': [10000, 11000, 12000, 13000, 14000, 15000, 16000]},
            {'name': 'Sarah', 'steps': [8000, 8500, 9000, 9500, 10000, 10500, 11000]}]

# All step counts above 10000 across all people
above_10000 = [step for person in people for step in person['steps'] if step > 10000]
print('Step counts above 10000:', above_10000)

# Names with avarage steps above 9000
average_steps_above_9000 = [person['name'] for person in people if sum(person['steps']) / len(person['steps']) > 9000]
print()
print('Best performers above 9000 steps:', average_steps_above_9000)
