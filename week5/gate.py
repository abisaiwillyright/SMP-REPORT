# week5 gate pass code challange.

# Bolt Driver Earnings
data = {
    "driver": "Kamau Njoroge",
    "date": "2026-08-13",
    "trips": [
        {"route": "Westlands to CBD",     "fare_kes": 560},
        {"route": "CBD to South B",       "fare_kes": 420},
        {"route": "South B to Karen",     "fare_kes": 980},
        {"route": "Karen to Westlands",   "fare_kes": 720},
        {"route": "Westlands to Airport", "fare_kes": 740},
    ]
}

# Count the number of trips
total_trips = len(data["trips"])

# Calculate the total earnings
total_earnings = sum(trips["fare_kes"] for trips in data["trips"])

# Find the highest earning trip
highest_trip = max(data["trips"], key=lambda trip: trip["fare_kes"])

# results
print(f"Total trips:", total_trips)
print(f"Total earned: KES", total_earnings)
print(f"Highest trip: {highest_trip['route']} | KES {highest_trip['fare_kes']}")

print(f'\n{'='*80}')




# Supplier Pricing API
data = {
    "supplier": "Nairobi Steel Ltd",
    "prices": {
        "mild_steel_sheet": 4500,
        "angle_iron": 2800
    }
}


print(f'Mild steel sheets (3): KES', data["prices"]['mild_steel_sheet']*3)
print(f'Angle iron (6m): KES', data["prices"]["angle_iron"]*6)
print(f'Total: KES', data["prices"]['mild_steel_sheet']*3 + data["prices"]["angle_iron"]*6)
print(f'\n{'='*80}')



#Social Media API
data = {
    "user": "Amerix",
    "followers": 1200000,
    "last_post": {
        "title": "Cold shower protocol",
        "likes": 4800
    }
}

print(f'Followers:', data['followers'])
print(f'Last post likes:', data['last_post']['likes'])