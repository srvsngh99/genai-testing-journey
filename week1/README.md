# Week 1: Python Basics — Strings, Variables, and Prompt Handling

## Week 1 Goal
By end of this week, you will:
- Master Python string manipulation (the foundation of ALL prompt work)
- Build `prompt-formatter` — a reusable prompt template engine
- Push your first project to GitHub

---

## Daily Breakdown

### Time Budget: 8 hours total
| Day | Focus | Time |
|-----|-------|------|
| Monday | Learn: Variables, Strings, f-strings | 1 hr |
| Tuesday | Learn: String methods deep dive | 1 hr |
| Wednesday | Practice: Exercises + experiments | 1 hr |
| Thursday | Project: Start `prompt-formatter` | 1 hr |
| Friday | Project: Continue building | 1 hr |
| Saturday | Project: Complete + tests | 2 hrs |
| Sunday | Complete mini-project + Push to GitHub | 1 hr |

---

## Resources

### YouTube
- [Corey Schafer: Python Tutorial for Beginners 1 - Install and Setup](https://www.youtube.com/watch?v=YYXdXT2l-Gg)
- [Corey Schafer: Python Tutorial for Beginners 2 - Strings](https://www.youtube.com/watch?v=k9TUPpGqYTo)
- [Corey Schafer: Python String Formatting - f-Strings](https://www.youtube.com/watch?v=nghuHvKLhJA)

### Documentation
- [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [f-strings guide](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)

---

## Practice Files Guide

Week 1 has **TWO practice files** to cover everything for the mini-project:

### File 1: `practice/01_basics_and_strings.py`
**Covers:** Week 1 official syllabus
- Variables and data types
- String methods (`.strip()`, `.split()`, `.replace()`)
- f-strings for formatting
- **Time:** 1-2 hours (Mon-Tue)

### File 2: `practice/02_functions_and_classes.py`
**Covers:** Prerequisites for mini-project (not in Week 1 syllabus!)
- Functions: `def`, parameters, `return`
- Type hints: `def func(text: str) -> bool:`
- `**kwargs`: Flexible arguments
- Classes: `class`, `__init__`, `self`
- **Time:** 1-2 hours (Wednesday)

> **Why two files?** The mini-project needs functions and classes (Week 3 concepts). File 02 teaches just enough to succeed now. Week 3 goes deeper.

**Recommended order:**
1. Mon-Tue: Complete File 01 (strings)
2. Wednesday: Complete File 02 (functions & classes)
3. Thu-Sun: Build mini-project with confidence!

---


# LEARNING TRACK

## Monday: Variables, Strings, f-strings (1 hour)

### Watch These Videos (45 mins)
1. **Corey Schafer: Python Tutorial for Beginners 1 - Install and Setup**
   - URL: https://www.youtube.com/watch?v=YYXdXT2l-Gg
   - Duration: 15 mins
   - Why: Even if you know Python, watch at 1.5x to ensure your setup is correct

2. **Corey Schafer: Python Tutorial for Beginners 2 - Strings**
   - URL: https://www.youtube.com/watch?v=k9TUPpGqYTo
   - Duration: 21 mins
   - Why: This is THE video for string fundamentals
   - **Take notes on:** String creation, indexing, slicing

3. **Corey Schafer: Python String Formatting - f-Strings**
   - URL: https://www.youtube.com/watch?v=nghuHvKLhJA
   - Duration: 13 mins
   - Why: f-strings are how you'll build EVERY prompt template
   - **Take notes on:** f-string syntax, expressions inside f-strings

### Practice While Watching (15 mins)
Open a Python file or Jupyter notebook and type along:

```python
# Variables
name = "Claude"
role = "AI Assistant"
temperature = 0.7

# Basic string
prompt = "You are a helpful assistant"

# f-string (THIS IS KEY FOR PROMPTS)
prompt_template = f"You are {name}, a {role}. Respond helpfully."
print(prompt_template)

# Multi-line f-string (common for prompts)
system_prompt = f"""
You are {name}.
Your role: {role}
Temperature setting: {temperature}

Instructions:
- Be helpful
- Be concise
- Be accurate
"""
print(system_prompt)
```

### Monday Checkpoint
- [ ] Python installed and working
- [ ] Can create variables
- [ ] Understand f-strings
- [ ] Created at least 3 prompt templates using f-strings

---

## Tuesday: String Methods Deep Dive (1 hour)

### Watch These Videos (40 mins)
1. **Corey Schafer: Python Tutorial for Beginners 2 - Strings** (rewatch specific parts)
   - Focus on: 8:00-21:00 (string methods section)
   - Methods to master: `split()`, `join()`, `strip()`, `replace()`, `lower()`, `upper()`

2. **Corey Schafer: String Slicing**
   - This is covered in the Strings video above
   - Practice: `text[0:5]`, `text[-3:]`, `text[::2]`

### Key String Methods for AI Testing
These methods come up CONSTANTLY in prompt/response handling:

```python
# --- METHODS YOU'LL USE DAILY ---

response = "  The answer is 42.  \n"

# 1. strip() - Remove whitespace (LLM responses often have extra spaces)
clean = response.strip()
print(f"'{clean}'")  # 'The answer is 42.'

# 2. split() - Break into parts (parsing structured responses)
text = "apple,banana,cherry"
items = text.split(",")
print(items)  # ['apple', 'banana', 'cherry']

# 3. join() - Combine list into string (building prompts from parts)
parts = ["Step 1: Think", "Step 2: Analyze", "Step 3: Answer"]
combined = "\n".join(parts)
print(combined)

# 4. replace() - Substitute text (cleaning responses)
messy = "The answer is: ```42```"
clean = messy.replace("```", "")
print(clean)  # 'The answer is: 42'

# 5. lower()/upper() - Normalize case (for comparison)
user_input = "YES"
if user_input.lower() == "yes":
    print("User agreed")

# 6. startswith()/endswith() - Check patterns
response = "Error: Invalid input"
if response.startswith("Error"):
    print("Handle error!")

# 7. find()/index() - Locate substrings
text = "The capital of France is Paris"
pos = text.find("Paris")
print(f"'Paris' found at position {pos}")

# 8. in operator - Check if substring exists
if "Paris" in text:
    print("Found it!")
```

### Practice Exercises (20 mins)
Create a file `string_practice.py` and solve these:

```python
# Exercise 1: Clean LLM Response
# Given this messy response, extract just the answer
response = "\n\n  The answer is: **42**  \n\n"
# Your code here - result should be "42"

# Exercise 2: Parse Structured Output
# Extract each item from this response
llm_output = "1. Apple\n2. Banana\n3. Cherry"
# Your code here - result should be ['Apple', 'Banana', 'Cherry']

# Exercise 3: Build a Prompt from Parts
# Combine these into a single prompt with proper formatting
role = "helpful assistant"
task = "summarize the following text"
constraints = ["be concise", "use bullet points", "max 100 words"]
# Your code here - build a complete system prompt

# Exercise 4: Validate Response Format
# Check if the response follows expected format
response = "ANSWER: Paris"
# Your code here - check if response starts with "ANSWER:"

# Exercise 5: Template Substitution
# Replace placeholders in this template
template = "Hello {name}, your order {order_id} is {status}."
# Your code here - replace with: name="John", order_id="12345", status="shipped"
# Hint: Use .format() or f-strings
```

### Tuesday Checkpoint
- [ ] Know all 8 key string methods
- [ ] Completed all 5 exercises
- [ ] Can explain when to use each method

---

## Wednesday: Practice & Experiments (1 hour)

### Deep Practice Session
Today is about building muscle memory. Do these exercises WITHOUT looking at solutions first.

### Exercise Set 1: Prompt Template Builder (20 mins)
```python
"""
Build a function that creates prompts from templates.

Requirements:
1. Accept a template string with {placeholders}
2. Accept a dictionary of values
3. Return the filled template
4. Handle missing keys gracefully (return error message)
"""

def fill_template(template: str, values: dict) -> str:
    # Your implementation here
    pass
```

### Exercise Set 2: Response Cleaner (20 mins)
```python
"""
Build a function that cleans LLM responses.

Common issues to handle:
1. Leading/trailing whitespace
2. Multiple newlines → single newline
3. Markdown code blocks (```) → remove
4. Weird unicode characters → normalize
"""

def clean_response(response: str) -> str:
    # Your implementation here
    pass
```

### Exercise Set 3: Response Validator (20 mins)
```python
"""
Build validators for LLM responses.

Create these validation functions:
1. is_not_empty(response) → bool
2. is_within_length(response, max_chars) → bool
3. contains_keywords(response, keywords) → bool
4. is_valid_json(response) → bool
5. has_no_prohibited_words(response, prohibited) → bool
"""

import json

def is_not_empty(response: str) -> bool:
    # Your implementation
    pass
```

### Wednesday Checkpoint
- [ ] Built fill_template function
- [ ] Built clean_response function
- [ ] Built all 5 validators
- [ ] All test cases passing

---

## Week 1 Deliverables

## Thursday-Saturday: Build `prompt-formatter`

### Project Overview
**What you're building:** A Python package that handles prompt template creation, validation, and formatting — the foundation for all LLM testing.

**Why this matters:** Every LLM test starts with a prompt. Having a robust, reusable prompt handling system is essential.

### Project Structure
```
prompt-formatter/
├── prompt_formatter/
│   ├── __init__.py
│   ├── templates.py      # Template handling
│   ├── validators.py     # Input validation
│   ├── cleaners.py       # Response cleaning
│   └── utils.py          # Helper functions
├── tests/
│   ├── __init__.py
│   ├── test_templates.py
│   ├── test_validators.py
│   └── test_cleaners.py
├── examples/
│   └── basic_usage.py
├── README.md
├── requirements.txt
└── .gitignore
```
