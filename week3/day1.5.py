def day_report(steps, water, protocal):
    print('----- Daily Report-----')

    print(f'steps : {steps}')
    print(f'water : {water}, glasses')
    print(f'protocal : {protocal}')
    print()

def hit_goal(steps): return steps >= 8000
def water_target(water): return water >= 7

day_report(9200, 8, 'OMAD')
day_report(5700, 6, '2MAD')
day_report(11000,9,'Autophagy Marathon')

print('Gold hit (9200)?', hit_goal(9200))
print('Goal hit (7500)?', hit_goal(7500))
print('Goal hit (10000)?', hit_goal(11000))
print()

print('Water glasses taken(6)?', water_target(6))
print('Water glasses taken(8)?', water_target(8))
print('Water glasses taken(9)?', water_target(9))