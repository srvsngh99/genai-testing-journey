from prompt_formatter import (
    PromptTemplate, 
    validate_contains_keywords, 
    clean_response,
    count_tokens_estimate,
    format_list_as_text
)

# 1. Create a prompt template
template = PromptTemplate("You are a {role}. Task: {task}. Constraints: {constraints}")

# 2. Prepare dynamic data
role = "Python Expert"
task = "Explain string slicing"
constraints_list = ["use simple terms", "provide 2 examples", "maximum 100 tokens"]

# 3. Use utils to format the list
formatted_constraints = format_list_as_text(constraints_list, style="bullet")

# 4. Fill the template
prompt = template.fill(
    role=role, 
    task=task, 
    constraints=formatted_constraints
)

print("--- Generated Prompt ---")
print(prompt)
print(f"\nEstimated tokens: {count_tokens_estimate(prompt)}")

# 5. Simulate cleaning a messy response
messy_response = """
    
    Here is the explanation:
    String slicing is like cutting a cake...
    
    ```
    text = "Hello"
    print(text[0:2]) # He
    ```
    
"""
cleaned = clean_response(messy_response)

print("\n--- Cleaned Response ---")
print(cleaned)

# 6. Validate the response
keywords = ["slicing", "text"]
is_valid = validate_contains_keywords(cleaned, keywords)
print(f"\nResponse contains required keywords: {is_valid}")
