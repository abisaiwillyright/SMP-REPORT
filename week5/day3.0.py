# Method 1: Environment Variables

import os, requests, export

# In Terminal (Mac/Linux) - temporary, lasts the session
#export OPENAI_API_KEY="sk-abc123yourrealkeyhere"

# In Command Prompt (Windows) - temporary
#set OPENAI_API_KEY=sk-abc123yourrealkeyhere

api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not set in environment")

headers = {"Authorization": f"Bearer {api_key}"}
response = requests.get("https://api.openai.com/v1/models", headers=headers)

