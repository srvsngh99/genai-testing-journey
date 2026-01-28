# Week 3 Day 4: Advanced Functions
# Goal: Master *args, **kwargs, and default values

# Exercise 1: Default Arguments
# -----------------------------
# Define a function 'call_llm' with two parameters:
# - 'input_text' (required)
# - 'model' (optional, default to "gpt-3.5")
# Inside logic: print f"Calling {model} with input: {input_text}"

def call_llm(input_text: str, model: str = "gpt-3.5"):
    print (f"Calling {model} with input: {input_text}")


# TEST:
call_llm("Hello") # Should use gpt-3.5
call_llm("Hello", "claude-3") # Should use claude-3


# Exercise 2: *args (Variable Positional Args)
# --------------------------------------------
# Context: Validating multiple prompts at once.
# Define 'validate_prompts' that takes any number of string arguments (*args).
# Loop through the args.
# If a prompt is empty string "", print "Found empty prompt!"
# Else print "Prompt valid."

def validate_prompts(*args):
    for prompt in args:
        if prompt == "":
            print("Found empty prompt!")
        else:
            print("Prompt valid.")

# TEST:
validate_prompts("Hi", "", "Test")


# Exercise 3: **kwargs (Variable Keyword Args)
# --------------------------------------------
# Context: Configuring a test run with flexible settings.
# Define 'configure_test' that takes **kwargs.
# Print "Configuring test..."
# Check if key 'temperature' is in kwargs. If yes, print f"Temperature set to {kwargs['temperature']}"
# Check if key 'debug' is True. If yes, print "Debug mode ON"

def configure_test(**kwargs):
    print("Configuring test...")

    # Check for 'temperature' key
    if 'temperature' in kwargs:
        print(f"Temperature set to {kwargs['temperature']}")

    # Check if 'debug' key exists and is True
    if kwargs.get('debug'):
        print("Debug mode ON")


# TEST:
configure_test(temperature=0.7, debug=True, owner="Sourav")

