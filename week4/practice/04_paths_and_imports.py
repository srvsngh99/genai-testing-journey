"""
Practice 4: Paths and Imports

Goal: Advanced import techniques and troubleshooting.
"""

import sys
import os

# ---------------------------------------------------------
# Step 1: Adding to sys.path
# ---------------------------------------------------------
# Sometimes your code is not in a child folder, but a sibling one.
# Python can't see sibling folders by default.

# TODO: Create a folder called 'external_lib' OUTSIDE the 'practice' folder (i.e., in 'week4')
# TODO: Add a file 'utils.py' inside 'week4/external_lib/' with a function 'say_hello()'

# If we try to import it directly, it fails:
try:
    import external_lib.utils
except ImportError:
    print("Expected Error: Cannot find external_lib")

# TODO: Fix it by appending to sys.path
# Get the parent directory (week4)
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir) # Go up one level to 'week4'

print(f"Adding to path: {parent_dir}")
sys.path.append(parent_dir)

# TODO: Now uncomment this import
import external_lib.utils
external_lib.utils.say_hello()

# ---------------------------------------------------------
# Step 2: Relative Imports (The dot notation)
# ---------------------------------------------------------
# Relative imports (from . import x) ONLY work inside packages.
# They do NOT work in top-level scripts like this one.

# TODO: Try adding "from . import 01_modules_basics" here.
# It will fail with "ImportError: attempted relative import with no known parent package"

# ---------------------------------------------------------
# Step 3: Absolute Imports
# ---------------------------------------------------------
# Always prefer absolute imports (full path from project root) whenever possible.
# Example: from week4.practice import my_math
