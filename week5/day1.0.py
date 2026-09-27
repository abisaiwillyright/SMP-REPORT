# in VC Code (requires: pip install requests)

import requests

# Fetching user's profile from the API
url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url)
print(requests.status_codes)

users_data = response.json()
print(users_data)
print('='*140)


# Filtering API results
print('Total list - ', len(users_data))
print()

print(f"{'NAME':20} {'USERNAME':20} {'EMAIL ADDRESS':20} {'CITY':20} {'PHONE':25} {'COMPANY':20} {'WORK':20}")

for user in users_data:
    name = user['name']
    username = user['username']
    email = user['email']
    city = user['address']['city']
    phone = user['phone']
    company = user['company']['name']
    work = user['company']['catchPhrase']
    print('-'*149)

    print(f'{name:20} {username:20} {email:20} {city:20} {phone:25} {company:20} {work}')