import json

# JSON and Error handling

responses = ['{"steps": 9200, "protocol": "OMAD"}',
'{"steps": 10500, "protocol": "2MAD"}']

for r in responses:
    try:
        data = json.loads(r)
        print(f'Parsed OK: {data["steps"]} steps')
    except json.JSONDecodeError:
        print(f"Invalid JSON: {r[:30]}...")