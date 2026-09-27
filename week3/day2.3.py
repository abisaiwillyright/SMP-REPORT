# Keyword Arguments.

def client_report(name, goal, sessions=4, bench_kg=60):
    print(f'{name} | Goal: {goal} | Session/week: {sessions} | Bench: {bench_kg}Kgs')

# Position arguments
client_report('James', 'fat loss')

# Key arguments: order does not matter
client_report(goal='musle gain', name='Mwangi', bench_kg=100)

# Mix of positional and keyword
client_report('Sandra', 'endurance', bench_kg=50)