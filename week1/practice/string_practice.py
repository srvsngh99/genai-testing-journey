# Week 1: String Manipulation Exercises
# Focus: Mastering string methods for AI/Prompt Engineering

print("--- Exercise 1: Clean LLM Response ---")
# Given this messy response, extract just the answer
response = "\n\n  The answer is: **42**  \n\n"
# TODO: Write code to extracting "42"
# Hint: Use strip(), replace() or more strip()

# Your code here:
cleaned_response = response.strip().replace("**", "").replace("The answer is: ", "")
print(f"Result: '{cleaned_response}'")


print("\n--- Exercise 2: Parse Structured Output ---")
# Extract each item from this response into a Python list
llm_output = "1. Apple\n2. Banana\n3. Cherry"
# Needed result: ['Apple', 'Banana', 'Cherry']
# Hint: split() is your friend

# Your code here:
items = [line.split(". ", 1)[1] for line in llm_output.split("\n")]
print(f"Result: {items}")


print("\n--- Exercise 3: Build a Prompt from Parts ---")
# Combine these into a single prompt with proper formatting
role = "helpful assistant"
task = "summarize the following text"
constraints = ["be concise", "use bullet points", "max 100 words"]
# Hint: Use f-strings and "\n".join() for the constraints

# Your code here:
constraints_text = "\n- ".join(constraints);
prompt = f"You are {role}.\nYour task is to {task}.\nConstraints: \n- {constraints_text}"
print(f"Result:\n{prompt}")

#alternate way with numbers
constraints = "\n".join(f"{i+1}. {c}" for i, c in enumerate(constraints))
prompt = f"You are {role}.\nYour task is to {task}.\nConstraints: \n{constraints}"
print(f"Result:\n{prompt}"  )


print("\n--- Exercise 4: Validate Response Format ---")
# Check if the response follows expected format
response = "ANSWER: Paris"
# Check if response starts with "ANSWER:"
# Hint: startswith()

# Your code here:
is_valid = False
if response.startswith("ANSWER:"):
    is_valid = True
print(f"Is Valid: {is_valid}")


print("\n--- Exercise 5: Template Substitution ---")
# Replace placeholders in this template
template = "Hello {name}, your order {order_id} is {status}."
# Values: name="John", order_id="12345", status="shipped"
# Hint: Use .format() or f-string logic (though f-string needs vars defined first)

# Your code here:
final_message = template.format(name="John", order_id="12345", status="shipped")
print(f"Result: {final_message}")
