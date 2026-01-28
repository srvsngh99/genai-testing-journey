# Week 3 Day 3: Functions Basics
# Goal: Define and call simple functions

# Exercise 1: Define a Validator Function
# ---------------------------------------
# Define a function named 'check_safety' that takes one argument: 'score'
# If score < 0.5, return "Unsafe"
# Else, return "Safe"

def check_safety(score: float):
    if score < 0.5:
        return "Unsafe"
    else:
        return "Safe"

print(check_safety(0.1))
print(check_safety(0.9))

# TEST YOUR FUNCTION:
# print(check_safety(0.1)) # Should be "Unsafe"
# print(check_safety(0.9)) # Should be "Safe"


# Exercise 2: Multiple Arguments
# ------------------------------
# Define a function 'format_prompt' that takes two arguments: 'system_msg' and 'user_msg'
# It should return a single string formatted like:
# "System: [system_msg] | User: [user_msg]"

def format_prompt(system_msg: str, user_msg: str):
    return f"System: {system_msg} | User: {user_msg}"

print(format_prompt("You are a bot", "Hi"))

# TEST YOUR FUNCTION:
# print(format_prompt("You are a bot", "Hi"))


# Exercise 3: Return vs Print
# ---------------------------
# Write a function 'calculate_tokens' that takes a string.
# It should split the string by spaces to count words (simulating tokens)
# It should RETURN the count (integer).
# Do not print inside the function.

def calculate_tokens(prompt: str):
    return len(prompt.split(" "))


# TEST YOUR FUNCTION:
count = calculate_tokens("This is a test prompt")
print(f"Token count is: {count}")
