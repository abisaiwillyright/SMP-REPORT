# API KEY AUTHENTICATION

# Method 1: Environment Variables
# Simulate Reading an Env Variable

import os

print('Method 1: Environment Variables')
# Simulate: key loaded from environment (not hardcoded)
os.environ['SMP_API_KEY'] = "smp_test_key_abc123"   # set for demo only

api_key = os.environ.get("SMP_API_KEY")

if not api_key:
    print("ERROR: API key not found. Set the SMP_API_KEY environment variable.")
else:
    # # Show only first 8 chars for safety
    masked = api_key[:8] + "..." + api_key[-4:]
    print(f'Key loaded  {masked}')
    print("Ready to make authenticated requests.\n")


   #  Method 2: The .env File (Recommended)
from dotenv import load_dotenv
import os
print('Method 2: The .env File (Recommended)')
load_dotenv()    # reads .env and sets environment variables

api_key = os.getenv("SMP_API_KEY")
print(api_key)




# Passing Keys in Requests
# Method A: Query Parameter in the URL
import requests
try:
    url = f"https://api.weatherprovider.com/current?city=Nairobi&apikey={api_key}"
    response = requests.get(url)
except:
    print(f'\nError, API key not found\n')

# Or using the params dict (cleaner)
params = {
    'city': 'Nairobi',
    'Apikey': api_key
}
try:
    response = requests.get("https://api.weatherprovider.com/current", params=params)
except:
    print(f'Error, API Key not found\n')

# Method B: Authorization Header
# Bearer token (used by OpenAI, many modern APIs)
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
try:
    response = requests.get(url, headers=headers)
except:
    print(f'Error, API Key not found\n')
    
# Or as a custom header (varies by API)
headers = {"X-API-Key": api_key}
try:
    response = requests.get(url, headers=headers)
except:
    print(f'Error, API Key not found\n')

# Simulate: load key from environment
os.environ["SMP_API_KEY"] = "smp_live_abc123xyz"
api_key = os.getenv("SMP_API_KEY")

# Build request components (what you would pass to requests.get)
url = "https://api.amptracker.com/v1/members"
params = {"city": "Nairobi", "limit": 10}
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
print('Simulate Authenticated Request Structure')
print('URL:', url)
print('Params"', params)
print('Auth header:', 'Bearer' + api_key[:8] + '...\n')

# Simulate a 200 response
print('Response status: 200')
print("response body: {'members': [....], 'total': 42}")


# Handling Authentication Errors
print('\n\n----Handling Auth Errors----')
def handle_api_response(status_code, body):
    if status_code == 200:
        return body
    elif status_code == 401:
        raise PermissionError('Authentication failed. Check your API key.')
    elif status_code == 403:
        raise PermissionError("Access denied. Your key does not have permission for this endpoint.")
    elif status_code == 429:
        raise RuntimeError('Rate line exceeded. wait before retrying.')
    elif status_code >= 500:
        raise RuntimeError(f"Server error ({status_code}). Try again later.")
    else:
        raise RuntimeError(f'Unexpected status: {status_code}')

# Test with different status codes
test_cases = [
    (200, {"members": [{"name": "James Omondi"}]}),
    (401, {"error": "invalid_key"}),
    (429, {"error": "rate_limit_exceeded"}),
    (500, {"error": "internal_server_error"}),
]  
for status, body in test_cases:
    try:
        result = handle_api_response(status, body)
        print(f'Status { status}: OK, got {result}')
    except Exception as e:
        print(f'Status {status}: {e}')
