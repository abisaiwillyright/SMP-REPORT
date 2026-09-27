# Simulating the API Response Structure

# Simulates the object that response.choise[0].message.content extracts from
# This morrors the actual PenoAI API response structure exactly, but is simplified for demonstration purposes.
class Message:
    def __init__(self, content):
        self.content = content
        self.role = "assistant"  # Assuming the role is always 'assistant' for this simulation

class Choice:
    def __init__(self, content):
        self.message = Message(content)

class SimulatedResponse:
    def __init__(self, content):
        self.choices = [Choice(content)]
        self.model = "gpt-4o-mini"  # Simulated model name
        self.usage = {"prompt_tokens": 45, "completion_tokens": 82, "total_tokens": 127}  # Simulated token usage

# Simulated response as if the API returned it
simulated_response = SimulatedResponse("Sleep was the limiting factor today. James hit 7,800 steps but 6 hours is below optimal. "
    "Tomorrow: prioritize 8+ hours tonight. Keep the step target at 9,000, not 10,000, "
    "since recovery is still incomplete. Add a 20-minute walk after lunch to hit it without needing a long session.\n")    
print(simulated_response.choices[0].message.content)  # This will print the content of the simulated response    
print(f"Token usage: {simulated_response.usage['total_tokens']}")  # This will print the token usage
print(f"Is the message role 'assistant'? {'Yes' if simulated_response.choices[0].message.role == 'assistant' else 'No'}")  # This will check if the role is 'assistant'
print(f"{'='*60}")




# Using a System Prompt
import json

# Different system prompts produce different outputs for the same user message
system_prompts = {
    "SMP Coach": (
        "You are a strict SMP fitness coach. Be direct, no fluff. "
        "Give one actionable recommendation per response. Max 3 sentences."
    ),
    "Data Analyst": (
        "You are a fitness data analyst. Focus on numbers and trends. "
        "Output structured observations, not advice."
    ),
    "Nutritionist": (
        "You are a nutritionist specializing in intermittent fasting protocols. "
        "Focus only on eating patterns and timing."
    )
}
user_message = "James: steps=7800, sleep=6hr, protocol=OMAD, water=5 glasses, day 3 of deficit."

# Simulated responses for each system prompt
simulated_responses = {
    "SMP Coach": (
        "Six hours of sleep on day 3 of a deficit is why the steps are low. "
        "Tonight, sleep must be 8+ hours. Tomorrow target 9,000 steps only."
    ),
    "Data Analyst": (
        "Observation: Steps 22% below 10k goal. Sleep deficit likely compounding protocol fatigue. "
        "Water intake at 5/8 target. Recommend tracking energy levels as a leading indicator."
    ),
    "Nutritionist": (
        "Day 3 of OMAD with sleep deficit suggests cortisol is elevated. "
        "Consider shifting to 2MAD tomorrow to reduce stress load and support recovery."
    )
}
# Print the simulated responses for each system prompt
for role, prompt in system_prompts.items():
    print(f"System Prompt: {role}")
    print(f"Prompt:        {prompt}")
    print(f"User Message:  {user_message}")
    print(f"Simulated Response: {simulated_responses[role]}")
print(f"{'='*60}")




# Multi-Turn Conversation
def simulate_ai_response(system_prompt, user_message):
    # This function simulates an AI response based on the system prompt and user message
    if system_prompt == "SMP Coach":
        return "Six hours of sleep on day 3 of a deficit is why the steps are low. Tonight, sleep must be 8+ hours. Tomorrow target 9,000 steps only."
    elif system_prompt == "Data Analyst":
        return "Observation: Steps 22% below 10k goal. Sleep deficit likely compounding protocol fatigue. Water intake at 5/8 target. Recommend tracking energy levels as a leading indicator."
    elif system_prompt == "Nutritionist":
        return "Day 3 of OMAD with sleep deficit suggests cortisol is elevated. Consider shifting to 2MAD tomorrow to reduce stress load and support recovery."
    else:
        return "Unknown system prompt."

# Build conversation manually (what your script would maintain)
conversation = [
    {"role": "system", "content": system_prompts["SMP Coach"]},
    {"role": "user", "content": user_message},
    {"role": "assistant", "content": simulate_ai_response("SMP Coach", user_message)}
]

user_inputs = [
    "James hit 7800 steps today and slept 6 hours. OMAD protocol, day 3.",
    "He also hit a bench press PR of 88kg despite the deficit.",
    "Should he switch from OMAD to 2MAD tomorrow?"
]
# print convaersation and responses
for user_input in user_inputs:
    conversation.append({"role": "user", "content": user_input})
    # Simulate AI response based on the last user input
    ai_response = simulate_ai_response("SMP Coach", user_input)
    conversation.append({"role": "assistant", "content": ai_response})
    print(f"User: {user_input}")
    print(f"AI: {ai_response}")
    print(f"user: {user_message}")

# Simulate AI response
rely = simulate_ai_response("SMP Coach", user_inputs[-1])

# Add assistant response
conversation.append({"role": "assistant", "content": rely})
print(f"Coach: {rely}")
print(f"{'='*60}")




# Extracting Structured Data.
import json

# System prompt requesting JSON output
system = """You are a fitness data analyst. Output your observations in JSON format with keys: 'steps', 'sleep', 'protocol', 'water', 'day'. Do not include any advice or recommendations."""

# What the AI would respond with based on the system prompt and user message
ai_response = {
    "steps": 7800,
    "sleep": 6,
    "protocol": "OMAD",
    "water": 5,
    "day": 3
}
# Parse the AI response as if it were returned from the API
parsed_response = json.dumps(ai_response, indent=4)
print("Parsed structured data from AI response:")
for key, value in ai_response.items():
    print(f"{key}: {value}")

# use it programatically
parsed_response = json.loads(parsed_response)
if parsed_response["steps"] >= 10000:
    print("\nGoal achieved!")
else:
    print("\nGoal not achieved. Steps below 10,000.")
    print(f"Sleep rating: {parsed_response['sleep']}hrs, Protocol: {parsed_response['protocol']}, Water intake: {parsed_response['water']} glasses, Day: {parsed_response['day']}")

print(f"{'='*60}")