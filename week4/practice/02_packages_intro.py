"""
Practice 2: Packages Intro

Goal: Understand how to organize code into folders (packages).

Structure to create:
week4/
└── practice/
    ├── 02_packages_intro.py (This file)
    └── text_tools/          (New Folder)
        ├── __init__.py      (New File)
        └── converters.py    (New File)
"""

# ---------------------------------------------------------
# Step 1: Create the Package Structure
# ---------------------------------------------------------
# TODO: Create a folder named 'text_tools' in the same directory as this file.
# TODO: Create an empty file named '__init__.py' inside 'text_tools'.
# TODO: Create a file named 'converters.py' inside 'text_tools'.

# ---------------------------------------------------------
# Step 2: Add Code to Module
# ---------------------------------------------------------
# TODO: Inside 'converters.py', add:
# def to_uppercase(text):
#     return text.upper()

# ---------------------------------------------------------
# Step 3: Import from Package
# ---------------------------------------------------------
# TODO: Uncomment below to test module import

from text_tools import converters
print(converters.to_uppercase("hello world"))

# HINT: If you get ModuleNotFoundError, ensure 'text_tools' is a folder next to this script
# and it has an __init__.py file (though in Python 3.3+ it's not strictly required, it's good practice).

# ---------------------------------------------------------
# Step 4: The Power of __init__.py
# ---------------------------------------------------------
# TODO: Inside 'text_tools/__init__.py', add:
# from .converters import to_uppercase
# (This exposes the function at the package level)

# TODO: Now you can import directly from the package! Uncomment below:

import text_tools
print(text_tools.to_uppercase("this is cool"))

# QUESTIONS TO PONDER:
# 1. Why do we need __init__.py? (It marks a directory as a package)
# 2. What happens if you remove __init__.py? (Try it!)
