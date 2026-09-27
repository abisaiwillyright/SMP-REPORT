import urllib.request, json

# Fetch a public API and print the response

url =  "https://httpbin.org/json"
with urllib.request.urlopen(url) as response:
    data = json.loads(response.read())
print(data)
print(f'\n{'*'*100}')

print(json.dumps(data, indent=2))
print(f'\n{'*'*100}')


import json
# Parse this nested JSON and print the author and title
response = '{"book": {"title": "Clean Code", "author": "Robert Martin", "year": 2008}}'
data = json.loads(response)
book = data["book"]
print(f"Title: {book['title']}")
print(f"Author: {book['author']}")
print(f'\n{'*'*100}')



import urllib.request, json
# Make a request with a custom header
req = urllib.request.Request(
    "https://httpbin.org/headers",
    headers={"X-Custom-Header": "AmerixMasterclass"}
)
with urllib.request.urlopen(req) as r:
    data = json.loads(r.read())
print(data["headers"])
print(f'\n{'*'*100}')



import urllib.request, json, requests
# Fetch a joke from a public API and print it
url = "https://official-joke-api.appspot.com/random_joke"
try:
    with urllib.request.urlopen(url, timeout=10) as r:
        joke = json.loads(r.read())
    print(joke['setup'])
    print(joke['punchline'])
except Exception as e:
    print(f"Could not fetch joke: {e}")
print(f'\n{'*'*100}')




import json

# Simulated API response from a steel supplier
response_text = '''
{
    "supplier": "Nairobi Steel Ltd",
    "date": "2026-07-27",
    "prices": {
        "mild_steel_sheet": 4500,
        "angle_iron": 2800,
        "square_tube": 3200
    },
    "currency": "KES",
    "unit": "per metre"
}
'''

data = json.loads(response_text)

print(f"Supplier: {data['supplier']}")
print(f"Date: {data['date']}")
print(f"\nSteel prices ({data['currency']} {data['unit']}):")
for item, price in data["prices"].items():
    print(f"  {item.replace('_', ' ').title()}: KES {price:,}")

# One steel door frame: 3 pieces of angle iron (2m each) + 1 mild steel sheet
angle_cost = data["prices"]["angle_iron"] * 2 * 3
sheet_cost = data["prices"]["mild_steel_sheet"]
frame_cost = angle_cost + sheet_cost

print(f"\nDoor frame quote:")
print(f"  Angle iron (3 x 2m): KES {angle_cost:,}")
print(f"  Mild steel sheet: KES {sheet_cost:,}")
print(f"  Total: KES {frame_cost:,}")
print(f'\n{'*'*100}')




import json

# Simulated crop market API response
response_text = '''
{
    "market": "Wakulima Market, Nairobi",
    "date": "2026-07-27",
    "prices_per_bag_kes": {
        "maize": 3800,
        "beans": 9200,
        "wheat": 5500,
        "sorghum": 3200
    },
    "bag_weight_kg": 90
}
'''

data = json.loads(response_text)

# Farmer's current stock in bags
stock = {"maize": 12, "beans": 5, "wheat": 8, "sorghum": 20}

print(f"Market: {data['market']}")
print(f"Date: {data['date']}\n")
print("Crop Valuation:")
print("-" * 40)

total_value = 0
for crop, bags in stock.items():
    price = data["prices_per_bag_kes"][crop]
    value = bags * price
    print(f"{crop.title()}: {bags} bags x KES {price:,} = KES {value:,}")
    total_value += value

print(f"\nTotal stock value: KES {total_value:,}")
print(f'\n{'*'*100}')