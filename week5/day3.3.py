import os, base64, requests

# Step 1: Load credentials from environment (never hardcode)
os.environ['MPESA_CONSUMER_KEY'] = 'demo_consumer_key_abc123'
os.environ['MPESA_CONSUMER_SECRET'] = 'demo_secrit_xyz789'

consumer_key = os.getenv('MPESA_CONSUMER_KEY')
consumer_secrit = os.getenv('MPESA_CONSUMER_SECRET')

# Step 2: Encode credentials (Daraja requires Base64)
credentials = f'{consumer_key}:{consumer_secrit}'
encoded = base64.b64encode(credentials.encode()).decode()

# Step 3: In production you POST this to Daraja to get a token:
url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
headers = {"Authorization": f"Basic {encoded}"}
response = requests.get(url, headers=headers)
token = response.json()["access_token"]

# Simulate the token response
simulated_token = 'Q2xpZW50X0lENmJlYjA2NWEtMjA4Ny00OTU2'

print('Credentials encoded (Base64):', encoded[:20] + '...')
print()
print('Simulated token received:', simulated_token[:20] + '...')
print()
print('In production, pass this token to every M-Pesa API call:')
print(f' headers = {{"Autherization": "Bearer {simulated_token[:12]}..."}}')
print()
print('Example endpoint: STK Push (prompt customer to pay)')
print('POST https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest')