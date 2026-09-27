# Project: Grade Tracker.

import csv
import io
import json

# Students data
csv_data = """name,score1,score2,score3
Jame Omondi,85,90,78
Sandra Waweru,72,,88
Patrick Njiru,91,87,94
Grace Achieng,60,bad data,70
Brian Kamau,55,48,62"""

f = io.StringIO(csv_data)
reader = csv.DictReader(f)

for row in reader:
    print(dict(row))
print("="*75)

# Convert scores to Integer (Parse Scores Safely)
def parse_score(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

# Test
print("Parse Score")
print(parse_score('85'))
print(parse_score(''))
print(parse_score('bad data'))
print(parse_score(None))
print("="*75)

# Calculate Avarage and Letter Grade
def calculate_avarage(scores):
    valid = [s for s in scores if s is not None]
    if not valid:
        return None
    return round(sum(valid) / len(valid), 1)
print('Avarage Scores')

def letter_grade(avg):
    if avg is None: return 'N/A'
    if avg   >= 90:   return 'A'
    elif avg >= 80: return 'B'
    elif avg >= 70: return 'C'
    elif avg >= 60: return 'D'
    else:           return 'F'

# Test
scores_a = [85,90,78]
scores_b = [72,None,88]
scores_c = [60,None,None]

for s in [scores_a,scores_b,scores_c]:
    avg = calculate_avarage(s)
    print(f'Scores: {s} | Avg: {avg} | Grade: {letter_grade(avg)}')
print("="*75)

# Full Grade Tracker
# Process CSV
f = io.StringIO(csv_data)
reader = csv.DictReader(f)
results = []

print(f"{'NAME': <20} {'AVG': <8} {'GRADE':<8} NOTES")
print("="*75)      

for row in reader:
    scores = [
        parse_score(row['score1']),
        parse_score(row['score2']),
        parse_score(row['score3'])
    ]
    invalid_count = scores.count(None)
    avg = calculate_avarage(scores)
    grade = letter_grade(avg)
    notes = f"{invalid_count} invalid score(s)" if invalid_count else "All scores valid"

    print(f"{row['name']:<20} {str(avg):<8} {grade:<8} {notes}")
    results.append({
        'name': row['name'],
        'scores': [row['score1'], row['score2'], row['score3']],
        'average': avg,
        'grade': grade
    })

print('=' *75)

# Class Summary
valid_avgs = [r['average'] for r in results if r['average'] is not None]
class_avg = round(sum(valid_avgs) / len(valid_avgs), 1)
print(f'\nClass Average: {class_avg}')
print(f'Stunds: {len(results)}')
print('=' *75)


# Export as JSON
print('\nJSON Export:')
print(json.dumps(results, indent=2))
