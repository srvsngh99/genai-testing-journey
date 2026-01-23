# Week 3 Day 3: Functions Basics
# Goal: Define and call simple functions

# Exercise 1: Define a Validator Function
# ---------------------------------------
# Define a function named 'check_safety' that takes one argument: 'score'
# If score < 0.5, return "Unsafe"
# Else, return "Safe"

# TODO: Define the function here


# TEST YOUR FUNCTION:
# print(check_safety(0.1)) # Should be "Unsafe"
# print(check_safety(0.9)) # Should be "Safe"


# Exercise 2: Multiple Arguments
# ------------------------------
# Define a function 'format_prompt' that takes two arguments: 'system_msg' and 'user_msg'
# It should return a single string formatted like:
# "System: [system_msg] | User: [user_msg]"

# TODO: Define the function here


# TEST YOUR FUNCTION:
# print(format_prompt("You are a bot", "Hi"))


# Exercise 3: Return vs Print
# ---------------------------
# Write a function 'calculate_tokens' that takes a string.
# It should split the string by spaces to count words (simulating tokens)
# It should RETURN the count (integer).
# Do not print inside the function.

# TODO: Define the function here


# TEST YOUR FUNCTION:
# count = calculate_tokens("This is a test prompt")
# print(f"Token count is: {count}")
