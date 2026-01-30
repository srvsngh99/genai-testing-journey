"""
Practice 3: Virtual Environments and Sys Path

Goal: Understand where Python looks for code and what environment you are in.

NOTE: This script is for INSPECTION and LEARNING.
"""

import sys
import os

# ---------------------------------------------------------
# Step 1: Where am I?
# ---------------------------------------------------------
print("--- Python Executable Location ---")
print(sys.executable)
print("----------------------------------\n")

# TODO: Run this script.
# IF it prints something like ".../venv/bin/python", you are in a virtual env.
# IF it prints "/usr/bin/python" or "/usr/local/bin/python", you are likely global.

# ---------------------------------------------------------
# Step 2: System Path
# ---------------------------------------------------------
print("--- sys.path (Where Python looks for imports) ---")
for path in sys.path:
    print(path)
print("-------------------------------------------------\n")

# OBSERVATION:
# Notice that the FIRST entry is usually the directory containing this script.
# This is why you can import files in the same folder.

# ---------------------------------------------------------
# Step 3: Check for Packages
# ---------------------------------------------------------
# TODO: Try to import a common package like 'requests'.
# If it fails, we need to install it.

try:
    import requests
    print("SUCCESS: 'requests' library found!")
    print(f"Version: {requests.__version__}")
except ImportError:
    print("FAILURE: 'requests' library NOT found.")
    print("TODO: Run 'pip install requests' in your terminal.")

# ---------------------------------------------------------
# CHALLENGE:
# ---------------------------------------------------------
# 1. Open your terminal.
# 2. Create a virtual environment: python3 -m venv venv
# 3. Activate it: source venv/bin/activate (Mac/Linux) or venv\Scripts\activate (Win)
# 4. Run THIS script again. Notice 'sys.executable' has changed!
# 5. It will likely say 'requests' not found.
# 6. Run 'pip install requests'.
# 7. Run THIS script a 3rd time. Success!
