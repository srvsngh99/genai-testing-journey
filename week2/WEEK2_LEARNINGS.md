# 🧠 Week 2 Learnings: Data Structures & Application

These are the core practical patterns mastered in the Week 2 Mini-Project.

## 1. Taking User Input
In a command-line tool, we use `input()` to pause the program and wait for the user to type something.

**Code Snippet:**
```python
# The program pauses here until user hits Enter
user_text = input("Enter your details: ")

# We can use that variable immediately
print(f"You entered: {user_text}")
```

---

## 2. In-Memory Data Storage
How do we save data without a database? We use a **List of Dictionaries**.
- The **List** acts as the generic container (the "table").
- The **Dictionary** acts as the specific record (the "row").

**Code Snippet:**
```python
# 1. The Global Store (Our "Database" in RAM)
# This sits at the top level of the script so it persists while running.
test_cases_db = [] 

def add_new_data():
    # 2. The Record (One row of data)
    new_record = {
        "id": "TC001",
        "status": "passed",
        "input": "User Input Here"
    }
    
    # 3. Storing it
    # We put the dictionary INSIDE the list
    test_cases_db.append(new_record)

# Visualizing the Memory:
# test_cases_db = [
#    {"id": "TC001", ...},  <-- Index 0
#    {"id": "TC002", ...},  <-- Index 1
# ]
```

---

## 3. Key Concepts Summary
- **Lists (`[]`)**: Used to keep our items in order.
- **Dictionaries (`{}`)**: Used to label data fields (like `id`, `prompt`).
- **RAM Persistence**: This data lives only while the script runs. If you close the script, the list is cleared (reset inputs).
