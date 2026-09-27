# PROJECT - FULL DARSHBOARD
import json
import importlib.util

file_path = r"C:\Users\User\abisai-ai-demo\week5\day1.3.py"
spec = importlib.util.spec_from_file_location("data", file_path)
data_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(data_module)

print(data_module.weekly_logs)
print(f'\n{'='*140}')

file_path = r"C:\Users\User\abisai-ai-demo\week4\day4.4.py"
spec = importlib.util.spec_from_file_location("data", file_path)
data_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(data_module)

print(data_module.clients)
print(f'\n{'='*140}')

# preview

