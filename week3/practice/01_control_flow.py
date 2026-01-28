# Week 3 Day 1: Control Flow
# Goal: Master if/else and loops

# Exercise 1: If/Else Logic Tree
# ------------------------------
# Context: You are validating an LLM response size.
# Create a variable 'response_length' = 150
# If length < 100, print "Too short"
# If length > 500, print "Too long"
# Else, print "Perfect"

response_length = 150
if response_length < 100:
    print("Too short")
elif response_length > 500:
    print("Too long")
else:
    print("Perfect")


# Exercise 2: For Loops
# ---------------------
# Context: Iterating through a list of model names to run a test.
models = ["gpt-4", "gpt-3.5", "claude-3", "llama-2"]

# Loop through the list
# Print "Testing model: [model_name]"
# If the model is "llama-2", print "Skipping local model" and use 'continue' to skip the rest of the loop block
# If the model is "claude-3", print "Found target model!" and use 'break' to stop the loop entirely

for model  in models:
    print(f"Testing model: {model}")
    if model == "llama-2":
        print("Skipping local model")
        continue
    elif model == "claude-3":
        print("Found target model!")
        break


# Exercise 3: While Loops
# -----------------------
# Context: Retrying an API call until it succeeds (simulation).
retries = 0
max_retries = 3

# Create a while loop that runs as long as 'retries' is less than 'max_retries'
# Inside the loop:
#   Print f"Attempt {retries + 1}..."
#   Increment 'retries' by 1
#   If retries equals 2, print "Success!" and break the loop

while retries < max_retries:
    print(f"Attempt {retries + 1}...")
    retries += 1
    if retries == 2:
        print("Success!")
        break