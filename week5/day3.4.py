import dotenv



import os
from dotenv import load_dotenv

load_dotenv() # reads .env and loads variables

openai_api_key = os.getenv("OPENAI_API_KEY")
weather_api_key = os.getenv("WEATHER_API_KEY")
stripe_secrit_key = os.getenv("STRIPE_SECRIT_KEY")

# Print the keys
print(f'OpenAI API Key:', openai_api_key)
print(f'Weather API Key:', weather_api_key)
print(f'Stripe Secrit Key:', stripe_secrit_key)

