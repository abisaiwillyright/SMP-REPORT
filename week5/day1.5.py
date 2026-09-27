# Filter API Result

logs = [
    {'name': 'James Jasiri', 'steps': 9300, 'protocol': 'OMAD'},
    {'name': 'Sandra Kasandi', 'steps': 10700, 'protocol': '2MAD'},
    {'name': 'Patrick Njoroge', 'steps': 8300, 'protocol': 'OMAD'},
    {'name': 'Grace Jumba', 'steps': 11000, 'protocol': 'OMAD'},
    {'name': 'Brian Sunguti', 'steps': 7700, 'protocol': '2MAD'},
    {'name': 'Kevin Ijami', 'steps': 10900, 'protocol': 'OMAD'}
]

# OMAD Users who hit 10,000 teps

goal_hitters = [
    r for r in logs
    if r['protocol'] == 'OMAD' and r['steps'] >= 10000
] 

goal_misser = [
    r for r in logs
    if r['protocol'] == 'OMAD' and r['steps'] < 10000
]

print('OMAD users who hit 10k steps:')
for r in goal_hitters:
    print(f' {r['name']}: {r['steps']} steps')

print('\nOMAD users below 10k steps:')
for r in goal_misser:
    print(f' {r['name']}: {r['steps']} steps')
