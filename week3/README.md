# Week 3: Control Flow & Functions

## Week 3 Goal
By end of this week, you will:
- Master `if/else` logic and Loops (`for`, `while`)
- Learn **List Comprehensions** (Pythonic way to loop)
- Deep Dive into **Functions** (*args, **kwargs, return values)
- Build `llm-response-validator` — a validation library
- Push your third deliverable to GitHub

---

## Daily Breakdown

### Time Budget: 9 hours total
| Day | Focus | Time |
|-----|-------|------|
| Monday | Learn: Control Flow (If, Loops) | 1 hr |
| Tuesday | Learn: List Comprehensions | 1 hr |
| Wednesday | Learn: Functions Basics | 1 hr |
| Thursday | Learn: Advanced Functions (*args) | 1 hr |
| Friday | Practice: Validation Logic Challenge | 1 hr |
| Saturday | Project: Start `llm_response_validator.py` | 2 hrs |
| Sunday | Project: Complete + Push to GitHub | 2 hrs |

---

## Resources

### YouTube
- [Corey Schafer: Conditionals and Booleans](https://www.youtube.com/watch?v=DZwmZ8OtBWw)
- [Corey Schafer: Loops and Iterations](https://www.youtube.com/watch?v=6iF8Xb7Z3wQ)
- [Corey Schafer: Functions](https://www.youtube.com/watch?v=9Os0o3w8yB4)
- [Corey Schafer: List Comprehensions](https://www.youtube.com/watch?v=3dt4PRnOE50)

### Documentation
- [Python Control Flow](https://docs.python.org/3/tutorial/controlflow.html)

---

## Practice Files Guide

Week 3 has **FIVE practice files** building up to the mini-project:

### File 1: `practice/01_control_flow.py` (Monday)
**Covers:**
- `if/elif/else` logic trees
- `for` loops and `while` loops
- `break` and `continue`
- **Time:** 1 hour

### File 2: `practice/02_list_comprehensions.py` (Tuesday)
**Covers:**
- Turning loops into one-liners
- Filtering logic inside lists
- Transformation logic
- **Time:** 1 hour

### File 3: `practice/03_functions_basics.py` (Wednesday)
**Covers:**
- Defining functions with `def`
- Arguments and Parameters
- Return statements vs Printing
- **Time:** 1 hour

### File 4: `practice/04_functions_advanced.py` (Thursday)
**Covers:**
- Default arguments
- `*args` and `**kwargs`
- Scope (Global vs Local)
- **Time:** 1 hour

### File 5: `practice/05_validation_challenge.py` (Friday)
**Covers:**
- Building small validation functions
- Chaining functions together
- **Time:** 1 hour

---

# LEARNING TRACK

## Monday: Control Flow (1 hour)

### Practice Exercises
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

### Monday Checkpoint
- [ ] Understand `break` vs `continue`
- [ ] Can write basic if/else logic

---

## Tuesday: List Comprehensions (1 hour)

### Practice Exercises
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

### Tuesday Checkpoint
- [ ] Can write a list comprehension
- [ ] Understand the syntax `[x for x in list if condition]`

---

## Wednesday: Functions Basics (1 hour)

### Practice Exercises
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

### Wednesday Checkpoint
- [ ] Know difference between Return and Print
- [ ] Can pass arguments to functions

---

## Thursday: Advanced Functions (1 hour)

### Practice Exercises
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

### Thursday Checkpoint
- [ ] Understand `*args` for variable inputs
- [ ] Understand default parameters

---

## Friday: Validation Challenge (1 hour)

### Practice Exercises
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

## Saturday-Sunday: Build `llm-response-validator`

**Mini-Project: `llm-response-validator`**
```
Build validation functions:
├── validate_not_empty(response)
├── validate_max_length(response, limit)
├── validate_contains_keywords(response, keywords)
├── validate_json_format(response)
└── validate_no_pii(response)  # Basic patterns
```
