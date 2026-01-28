# 📘 Week 3: Control Flow & Functions

## 🎯 Week 3 Goal
By end of this week, you will:
- Master `if/else` logic and Loops (`for`, `while`)
- Learn **List Comprehensions** (Pythonic way to loop)
- Deep Dive into **Functions** (*args, **kwargs, return values)
- Build a **Validation Library** (Mini-Project)

---

## 📅 Daily Breakdown

| Day | Focus | Practice File | Status |
|-----|-------|---------------|--------|
| **Monday** | Control Flow (If, Loops) | `01_control_flow.py` | |
| **Tuesday** | List Comprehensions | `02_list_comprehensions.py` | |
| **Wednesday** | Functions Basics | `03_functions_basics.py` | |
| **Thursday** | Advanced Functions (*args) | `04_functions_advanced.py` | |
| **Friday** | Validation Logic Challenge | `05_validation_challenge.py` | |
| **Sat-Sun** | Mini-Project: `llm_response_validator.py` | | |

**Total: 9 hours**

---

## Practice Files Guide

Week 3 has **FIVE practice files** building up to the mini-project:

### 1. `practice/01_control_flow.py` (Monday)
- `if/elif/else` logic trees
- `for` loops over lists/dicts
- `while` loops (waiting for input)
- `break` and `continue`

### 2. `practice/02_list_comprehensions.py` (Tuesday)
- Turning loops into one-liners
- Filtering logic inside lists
- Transformation logic

### 3. `practice/03_functions_basics.py` (Wednesday)
- Defining functions with `def`
- Arguments and Parameters
- Return statements vs Printing
- Docstrings

### 4. `practice/04_functions_advanced.py` (Thursday)
- Default arguments
- `*args` (Variable positional arguments)
- `**kwargs` (Variable keyword arguments)
- Scope (Global vs Local)

### 5. `practice/05_validation_challenge.py` (Friday)
- Building small validation functions
- chaining functions together
- simulating LLM response validation

---

# 📚 LEARNING TRACK

## Monday: Control Flow (1 hour)

Create `week3/practice/01_control_flow.py`:

```python
# Exercise 1: If/Else (LLM Response Check)
# Create a variable 'response_length' = 150
# If length < 100, print "Too short"
# If length > 500, print "Too long"
# Else, print "Perfect"

# Exercise 2: For Loop (Model Names)
models = ["gpt-4", "gpt-3.5", "claude-3", "llama-2"]
# Loop through and print "Testing model: [model]"
# If model == "llama-2", print "Skipping local model" and continue

# Exercise 3: While Loop (Retry Logic)
# Create a variable 'retries' = 0
# While retries < 3:
#   Print "Attempt [retries]..."
#   Increment retries
#   If retries == 2, print "Success!" and break
```

---

## Tuesday: List Comprehensions (1 hour)

Create `week3/practice/02_list_comprehensions.py`:

```python
# Exercise 1: Basic Transformation
scores = [0.1, 0.5, 0.8, 0.9]
# Create a new list 'percentages' that multiplies each by 100
# Expected: [10.0, 50.0, 80.0, 90.0]

# Exercise 2: Filtering
responses = ["Error: Timeout", "Success", "Error: 500", "Success"]
# Create a list 'errors' that only contains strings starting with "Error"

# Exercise 3: Logic inside list
# Create a list where for numbers 1-5:
# If even -> "Even"
# If odd -> "Odd"
# Result: ["Odd", "Even", "Odd", "Even", "Odd"]
```

---

## Wednesday: Functions Basics (1 hour)

Create `week3/practice/03_functions_basics.py`:

```python
# Exercise 1: Basic Function
# Define 'check_safety(score)'
# If score < 0.5, return "Unsafe"
# Else, return "Safe"

# Exercise 2: Multiple Arguments
# Define 'format_prompt(system, user)'
# Return f"System: {system}\nUser: {user}"

# Exercise 3: Return vs Print
# Write a function that CALCULATES the word count of a string and RETURNS it.
# Then print that result outside the function.
```

---

## Thursday: Advanced Functions (1 hour)

Create `week3/practice/04_functions_advanced.py`:

```python
# Exercise 1: Default Arguments
# Define 'call_llm(input_text, model="gpt-3.5")'
# Print f"Calling {model} with {input_text}"
# Call it once with just input, once with a different model

# Exercise 2: *args (Multiple Inputs)
# Define 'validate_all(*prompts)'
# Loop through prompts and check if they are not empty

# Exercise 3: **kwargs (Config)
# Define 'configure_test(**settings)'
# Print "Temperature is: " + settings.get('temperature', 0.7)
# Call with temperature=0.2 and verbose=True
```

---

## Friday: Validation Challenge (1 hour)

Create `week3/practice/05_validation_challenge.py`:

```python
"""
Challenge: Build a Mini-Validator Library
"""

# 1. Write 'is_valid_json(text)' -> returns True/False (Check if it starts with '{')
# 2. Write 'check_length(text, min_len, max_len)' -> returns True/False
# 3. Write 'validate_response(text)' that uses BOTH functions above.
#    - It should start with '{' AND be between 10-100 chars
# 4. Test it with:
#    - "fail"
#    - "{success}"
#    - "{too long...}" * 20
```

---

## Week 3 Deliverables

### Practice Files
- [x] `week3/practice/01_control_flow.py` - COMPLETE
- [x] `week3/practice/02_list_comprehensions.py` - COMPLETE
- [x] `week3/practice/03_functions_basics.py` - COMPLETE
- [x] `week3/practice/04_functions_advanced.py` - COMPLETE
- [x] `week3/practice/05_validation_challenge.py` - COMPLETE

### Mini-Project
- [x] `week3/mini_project/llm_response_validator.py` - COMPLETE

**Week 3 Status: COMPLETE - Ready for Week 4!**
