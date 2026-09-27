import json

# Navigating Nested JSON
# Simulating API response with data

api_json = '''{"client": "James Omondi", "week": 1, "daily_logs":[
{"day": "Monday", "steps": 9200, "protocol": "OMAD"},
{"day": "Tuesday", "steps": 8800, "protocol": "2MAD"},
{"day": "Wednesdy", "steps": 7200, "protocol": "OMAD"},
{"day": "Thursday", "steps": 10500, "protocol": "Autophagy Marathon"},
{"day": "Friday", "steps": 11000, "protocol": "2MAD"}]}'''

data = json.loads(api_json)

print("Client:", data["client"])
print("Week:", data["week"])
print()

for log in data["daily_logs"]:
    status = "OK" if log["steps"] >= 8000 else "LOW"
    print(f" {log['day']}: {log['steps']} steps ({status})")