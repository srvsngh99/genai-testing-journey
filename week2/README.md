# Week 2: Data Structures — Lists, Dicts, Sets

## Week 2 Goal
By end of this week, you will:
- Master Lists, Dictionaries, Sets, and Tuples
- Learn **basic functions** (just enough for the project)
- Build `test-data-organizer` — a simple test case manager
- Push your second deliverable to GitHub

---

## Daily Breakdown

### Time Budget: 9 hours total
| Day | Focus | Time |
|-----|-------|------|
| Monday | Learn: Lists (Creation, Methods, Iteration) | 1 hr |
| Tuesday | Learn: Dictionaries & Nested Structures | 1 hr |
| Wednesday | Learn: Sets & Tuples | 1 hr |
| Thursday | Practice: Functions Intro | 1 hr |
| Friday | Practice: Integration Challenge | 1 hr |
| Saturday | Project: Start `test-data-organizer` | 2 hrs |
| Sunday | Project: Complete + Push to GitHub | 2 hrs |

---

## Resources

### YouTube
- [Corey Schafer: Lists, Tuples, and Sets](https://www.youtube.com/watch?v=W8KRzm-HUcc)
- [Corey Schafer: Dictionaries - Key-Value Pairs](https://www.youtube.com/watch?v=daefaLgNkw0)

### Documentation
- [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)

---

## Practice Files Guide

Week 2 has **FIVE practice files** building up to the mini-project:

### File 1: `practice/01_lists.py` (Monday)
**Covers:**
- Basic list operations (Grocery List example)
- Indexing, slicing, and methods
- Iteration and comprehensions
- **Time:** 1 hour

### File 2: `practice/02_dicts_nested.py` (Tuesday)
**Covers:**
- Dictionary CRUD operations (User Profile example)
- Nested dictionaries (Company structure)
- Lists of dictionaries
- **Time:** 1 hour

### File 3: `practice/03_sets_tuples.py` (Wednesday)
**Covers:**
- Sets for unique items (Deduplication)
- Tuples for immutable data (Coordinates)
- Basic set operations
- **Time:** 1 hour

### File 4: `practice/04_functions_intro.py` (Thursday)
**Covers:**
- Function definition and calling
- Parameters and return values
- **Time:** 1 hour

### File 5: `practice/05_data_structures_challenge.py` (Friday)
**Covers:**
- Combining lists, dicts, and loops
- Building a mini "database" in memory
- **Time:** 1 hour

---

# LEARNING TRACK

## Monday: Lists (1 hour)

### Watch These Videos (XX mins)
1. **Corey Schafer: Lists, Tuples, and Sets**
   - URL: https://www.youtube.com/watch?v=W8KRzm-HUcc
   - Focus on: First 20 minutes (Lists)

### Practice Exercises
Create `week2/practice/01_lists.py`:

```python
# Exercise 1: Basic list operations (Grocery List)
# Create a list with: "apples", "bananas", "milk"
# Add "bread" and "eggs"
# Print the final list

# Exercise 2: Slice operations (Numbers)
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Get first 3 numbers
# Get last 2 numbers
# Get every other number

# Exercise 3: Iteration & Math (Grades)
grades = [85, 92, 78, 95, 88]
# Calculate average grade
# Find maximum grade
# Count grades above 90

# Exercise 4: Filtering (Light Test Case context)
# You have a list of test names: ["test_login", "test_signup", "test_api", "test_ui"]
# Create a new list called 'ui_tests' that only contains names with "ui" or "api"
```

### Monday Checkpoint
- [ ] Understand lists vs arrays
- [ ] Can slice lists confidently
- [ ] Can iterate using for loops

---

## Tuesday: Dictionaries & Nested Structures (1 hour)

### Watch These Videos
1. **Corey Schafer: Dictionaries**
   - URL: https://www.youtube.com/watch?v=daefaLgNkw0

### Practice Exercises
Create `week2/practice/02_dicts_nested.py`:

```python
# Exercise 1: Create a simple dictionary (User Profile)
# Create a dict with: name, age, city, and a list of skills

# Exercise 2: Update and access
# Add a "favorite_color" field
# Update the age
# Safely get a field called "occupation" with a default value

# Exercise 3: Nested dictionary (Company structure)
company = {
    "engineering": {"headCount": 50, "budget": 100000},
    "marketing": {"headCount": 20, "budget": 50000}
}
# Calculate total budget
# Print the headCount for engineering

# Exercise 4: List of dictionaries (Light Test Context)
# Create a list of 3 dictionaries, each representing a test case
# Each should have: "id", "status" (passed/failed), and "score"
# Calculate the average score
```

### Tuesday Checkpoint
- [ ] Understand Key-Value pairs
- [ ] Can nested dictionaries
- [ ] Can access data safely with .get()

---

## Wednesday: Sets & Tuples (1 hour)

### Watch These Videos
1. **Corey Schafer: Lists, Tuples, and Sets** (Finish the video)

### Practice Exercises
Create `week2/practice/03_sets_tuples.py`:

```python
# Exercise 1: Unique Items (Sets)
# You have a list with duplicates: ["python", "java", "python", "c++", "java"]
# Convert it to a set to remove duplicates

# Exercise 2: Set Operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
# Find items in both (Intersection)
# Find items only in set_a (Difference)

# Exercise 3: Fixed Data (Tuples)
# Create a tuple representing a point (x, y) = (10, 20)
# Try to change it (and see it fail!)
# Unpack the tuple into two variables
```

### Wednesday Checkpoint
- [ ] Know when to use a Set vs List
- [ ] Understand Tuple immutability

---

## Thursday: Functions Intro (1 hour)

### Practice Exercises
Create `week2/practice/04_functions_intro.py`:

```python
# Exercise 1: Simple greeting
# Write a function that takes a name and returns "Hello, [name]!"

# Exercise 2: Math operation
# Write a function that take two numbers and returns their sum

# Exercise 3: Light Test Context
# Write a function called 'format_test_info' that takes an ID and a status
# and returns a formatted string: "Test [ID] status is: [STATUS]"
```

---

## Friday: Practice Challenge (1 hour)

### Practice Exercises
Create `week2/practice/05_data_structures_challenge.py`:

```python
"""
Challenge: Build a mini test case database using only data structures
"""

# 1. Create a function 'create_test_case(id, status)' that returns a dict
# 2. Create a list called 'test_db'
# 3. Use your function to add 3 test cases to the list
# 4. Filter the list to find only 'passed' tests
# 5. Print the IDs of the passed tests
```

---

## Week 2 Deliverables

## Saturday-Sunday: Build `test-data-organizer`

**Mini-Project: `test-data-organizer` (Simplified)**
```
Build a test case organizer (single Python file):
├── Store test cases as list of dictionaries (in memory)
├── Add, search, filter test cases
├── Calculate statistics (pass rate, category breakdown)
└── Simple menu-driven interface

Note: JSON export/import moved to Week 5
      Package structure moved to Week 4
```
