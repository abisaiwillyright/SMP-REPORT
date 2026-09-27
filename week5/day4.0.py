# part1: Configuration

import os

BASE_URL = 'https://api.smptracker.com/v1'
API_KEY = os.environ.get('SMP_API_KEY', 'demo_key_123')
DEFAULT_CITY = 'Nairobi'
STEP_GOAL = 10000
MAX_RESULTS = 50

print('Configuration Loaded:')
print(f' Base URL: {BASE_URL}')
print(f' API Key:  {API_KEY[:8]}...')
print(f' City:     {DEFAULT_CITY}')
print(f' Seps Goal: {STEP_GOAL:,}')
print(f' Max Results:{MAX_RESULTS}')
print(f'{'='*50}\n')

# Part 2: Fetch Function
def fetch_members(city="Nairobi", limited=50):
    """
    Fetches member data from the SMP API.
    Returns a list of member dicts or raises RubtimeError.
    In production: Uses requests.get() with headers and params.
    """
    # Simulate the API response
    mock_response_status = 200
    mock_data = [
        {"id": 1, "name": "James Omondi", "city": "Nairobi", "steps": 9200, "protocol": "OMAD"},
        {"id": 2, "name": "John Waweru", "city": "Kisumu", "steps": 8800, "protocol": "OMAD"},
        {"id": 3, "name": "Monica John", "city": "Nairobi", "steps": 11000, "protocol": "2MAD"},
        {"id": 4, "name": "Willy Wisty", "city": "Mombasa", "steps": 10500, "protocal": "OMAD"},
        {"id": 5, "name": "Patrick Omondi", "city": "Nairobi", "steps": 9000, "protocol": "2MAD"},
        {"id": 6, "name": "Ruth Jumba", "city": "Mombasa", "steps": 7000, "protocol": "OMAD"}
    ]
    if mock_response_status !=200:
        raise RecursionError(f'API error: status {mock_response_status}')

    # Filter by city
    filtered = [m for m in mock_data if m['city'] == city]
    return filtered[:limited]

# call the function
members = fetch_members(city="Nairobi")
print(f'Fetched {len(members)} members from Nairobi')
for m in members:
    print(f' {m['name']}: {m['steps']} steps')
print()

members = fetch_members(city="Mombasa")
print(f'Fetched {len(members)} members from Mombasa')
for m in members:
    print(f' {m['name']}: {m["steps"]} steps')
print(f'{'='*50}\n')


# Part 3: Processing Function
def process_members(members, steps_goal=9000):
    if not members:
        return{'error': 'No members to process'}
    
    total = len(members)
    goal_met = [m for m in members if m['steps'] >= steps_goal]
    goal_missed = [m for m in members if m['steps'] < steps_goal]
    avg_goal = round(sum(m['steps'] for m in members) / total)
    top_performer = max(members, key=lambda m: m['steps'])

    return {
        'total_members': total,
        'goal_met_count': len(goal_met),
        'goal_missed_count': len(goal_missed),
        'avarage_steps': avg_goal,
        'top_perfomers': top_performer['name'],
        'top_steps': top_performer['steps'],
        'goal_met': [m['name'] for m in goal_met]
    }

summary = process_members(members, steps_goal=9000)
print('processed Summary:')
for key, value in summary.items():
    print(f' {key}: {value}')
print(f'{'='*50}\n')


# Partt4: Output
import json

def print_report(summary, city='Nairobi'):
    print('='*50)
    print(f' SMP MEMBER REPORT: {city.upper()}')
    print('='*50)
    print(f' Total members: {summary['total_members']}')
    print(f' Hit steps goal: {summary['goal_met_count']}')
    print(f' Missed goal: {summary['goal_missed_count']}')
    print(f' Avarage steps: {summary['avarage_steps']:,}')
    print(f' Top perfomers: {summary['top_perfomers']} ({summary['top_steps']:,} steps)')
    print('-'*50)
    print(' Members who hit goal:')
    for name in summary['goal_met']:
        print(f' {name}')
    print('='*50)




print_report(summary)

# Save to JSON
output = json.dumps(summary, indent=2)
print('\nJSON output saved:')
print(output)
print('='*50)