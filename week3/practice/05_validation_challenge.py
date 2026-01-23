# Week 3 Day 5: Validation Challenge
# Goal: Build a mini validation library

"""
Scenario:
You are building the core logic for the Week 3 Mini-Project.
You need small, reusable functions to check if an LLM response is valid.
"""

# 1. JSON Validator
# -----------------
# Write a function 'is_valid_json_start(text)'
# It should return True if the stripped text starts with '{'
# Otherwise False

# TODO: Code here


# 2. Length Validator
# -------------------
# Write a function 'check_length(text, min_len, max_len)'
# Returns True if text length is within bounds, else False

# TODO: Code here


# 3. Keyword Check
# ----------------
# Write a function 'contains_word(text, word)'
# Returns True if 'word' is inside 'text' (case insensitive), else False

# TODO: Code here


# 4. Master Validator
# -------------------
# Write a function 'validate_response(response)'
# It should use the functions above to check:
# - It starts with '{'
# - It is between 10 and 200 characters long
# - It contains the word "success"

# If ALL pass, return True. If ANY fail, return False (and maybe print which one failed)

# TODO: Code here
