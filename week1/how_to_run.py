"""
How to RUN Python Files - Complete Guide
========================================
"""

print("=" * 70)
print("METHOD 1: Run Python File from Terminal/Command Prompt")
print("=" * 70)

print("""
STEPS:
1. Open a terminal (Command Prompt, PowerShell, or Terminal)
2. Navigate to the folder where your Python file is
3. Type: python filename.py
4. Press Enter

EXAMPLE:
--------
$ python creating_variables_guide.py

This will run the file and show the output in the terminal.
""")

print("\n" + "=" * 70)
print("METHOD 2: Run Python File in VS Code")
print("=" * 70)

print("""
OPTION A - Using the Play Button:
----------------------------------
1. Open the Python file in VS Code
2. Look for the ▶ (play button) in the top-right corner
3. Click it
4. The output appears in the terminal at the bottom

OPTION B - Using the Terminal:
------------------------------
1. Open the Python file in VS Code
2. Press Ctrl + ` (backtick) to open the terminal
3. Type: python filename.py
4. Press Enter

OPTION C - Right-Click Menu:
----------------------------
1. Right-click on the Python file in the file explorer
2. Select "Run Python File in Terminal"
3. The output appears in the terminal
""")

print("\n" + "=" * 70)
print("METHOD 3: Run Python Directly by Double-Clicking (Windows)")
print("=" * 70)

print("""
On Windows, you can double-click a .py file to run it.
BUT: The terminal window will close immediately after running,
     so you won't see the output!

To keep it open, add this line at the end of your Python file:
    input("Press Enter to exit...")
""")

print("\n" + "=" * 70)
print("QUICK REFERENCE - Commands to Use")
print("=" * 70)

print("""
COMMAND                              WHAT IT DOES
─────────────────────────────────────────────────────────────────
python filename.py                   Run a Python file
python -c "print('Hello')"           Run Python code directly
python -i filename.py                Run file and stay in Python shell
python -m module_name                Run a Python module
python --version                     Check Python version

NAVIGATION COMMANDS:
─────────────────────────────────────────────────────────────────
cd folder_name                       Go into a folder
cd ..                                Go up one folder
cd c:\\Users\\User\\abisai-ai-demo\\files   Go to specific folder
dir                                  List files in current folder
pwd                                  Show current folder path
""")

print("\n" + "=" * 70)
print("EXAMPLE: Step-by-Step Instructions")
print("=" * 70)

print("""
You have these files in: c:\\Users\\User\\abisai-ai-demo\\files

FILE 1: creating_variables_guide.py
FILE 2: variables_tutorial.py

TO RUN THEM:
───────────

Step 1: Open Terminal (Windows)
   - Press: Windows Key + R
   - Type: cmd
   - Press Enter

Step 2: Navigate to the folder
   - Type: cd c:\\Users\\User\\abisai-ai-demo\\files
   - Press Enter

Step 3: List files to confirm
   - Type: dir
   - Press Enter
   - You should see creating_variables_guide.py and variables_tutorial.py

Step 4: Run a file
   - Type: python creating_variables_guide.py
   - Press Enter
   - Watch the output!

Step 5: Run another file
   - Type: python variables_tutorial.py
   - Press Enter
""")

print("\n" + "=" * 70)
print("TROUBLESHOOTING")
print("=" * 70)

print("""
PROBLEM: "python: command not found" or "'python' is not recognized"
SOLUTION: 
  - Python might not be installed
  - Or not in your PATH
  - Try: python3 filename.py (instead of python)
  - Or check if Python is installed: python --version

PROBLEM: "No such file or directory: filename.py"
SOLUTION:
  - You're not in the right folder
  - Check current folder: pwd (or cd without arguments)
  - List files: dir
  - Go to correct folder: cd path\\to\\folder

PROBLEM: File seems to run but I don't see output
SOLUTION:
  - Add this at the end of your Python file:
    input("Press Enter to exit...")
  - Or run from VS Code terminal (it stays open)

PROBLEM: Syntax Error when running
SOLUTION:
  - Check the error message
  - It will tell you the line number with the problem
  - Fix the typo or syntax issue
  - Save the file
  - Run again
""")

print("\n" + "=" * 70)
print("KEYBOARD SHORTCUTS IN TERMINAL")
print("=" * 70)

print("""
Arrow Up               See previous command
Arrow Down             See next command
Ctrl + C              Stop/Cancel current program
Ctrl + L              Clear terminal
Tab                   Auto-complete file/folder name
Ctrl + Home           Go to beginning of line
Ctrl + End            Go to end of line
""")

print("\n" + "=" * 70)
print("RECOMMENDED WAY TO RUN YOUR FILES")
print("=" * 70)

print("""
The EASIEST way for beginners:

1. Open VS Code
2. Click on your Python file
3. Look for the ▶ (play button) in top-right
4. Click it
5. Output appears in the terminal below

That's it! The terminal stays open so you can see everything.
""")
