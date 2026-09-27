# A function that works with Dictionary.
print('---Client Report---')
def print_client(client):
    print(f'Name         : {client['name']}')
    print(f'Goal         : {client['goal']}')
    print(f'Bench        : {client['bench_press_kg']} kg')
    print(f'Sessions     : {client['weekly_sessions']} per week')
    print()

clients = [
        {'name': 'James', 'goal': 'fat loss', 'bench_press_kg': 80, 'weekly_sessions': 4},
        {'name': 'Mwange', 'goal': 'muscle gain', 'bench_press_kg': 100, 'weekly_sessions': 5},
        {'name': 'Maina', 'goal': 'endurence', 'bench_press_kg': 120, 'weekly_sessions': 6}]

for client in clients:
    print_client(client)

