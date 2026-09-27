# Filtering a List of Dictionaries
Clients = [{'name': 'James', 'goal': 'fat loss', 'sessions': 4},
           {'name': 'Maria', 'goal': 'muscle gain', 'sessions': 3},
           {'name': 'John', 'goal': 'fat loss', 'sessions': 5},
           {'name': 'Maria', 'goal': 'muscle gain', 'sessions': 2},
           {'name': 'David', 'goal': 'fat loss', 'sessions': 6}]
# Get names of all fat loss clients
fat_loss_clients = [client['name'] for client in Clients if client['goal'] == 'fat loss']
print('Fat loss clients:', fat_loss_clients)
print()

# Get names of all clients with 4 or more than 4 sessions
high_frequency_clients = [client['name'] for client in Clients if client['sessions'] >= 4]
print('Active clients:', high_frequency_clients)
