# Week 1 Practice: Functions and Classes (The Missing Prerequisites!)
# These concepts weren't in Week 1's syllabus but were needed for the mini-project.

"""
This practice file covers:
1. Basic functions
2. Type hints
3. **kwargs (flexible parameters)
4. Classes and __init__
5. Instance methods
"""

print("="*70)
print("PART 1: BASIC FUNCTIONS")
print("="*70)

# A function is a reusable block of code
# Syntax: def function_name(parameters):
#             return result

# Example 1: Simple function
def greet(name):
    """This is a docstring - it describes what the function does."""
    return f"Hello, {name}!"

# Using the function:
message = greet("Sourav")
print(message)  # Hello, Sourav!

# Exercise 1: Write a function that counts words in a string
def count_words(text):
    # Your code here
    # Hint: use .split() and len()
    pass

# Test it:
# test_text = "This is a test sentence"
# print(f"Word count: {count_words(test_text)}")  # Should be 5


print("\n" + "="*70)
print("PART 2: TYPE HINTS (Optional but helpful!)")
print("="*70)

# Type hints tell you (and Python) what type of data is expected
# Syntax: def function_name(param: type) -> return_type:

def add_numbers(a: int, b: int) -> int:
    """Add two integers and return the result."""
    return a + b

result = add_numbers(5, 10)
print(f"5 + 10 = {result}")

# For strings:
def make_uppercase(text: str) -> str:
    """Convert text to uppercase."""
    return text.upper()

# For booleans:
def is_valid(text: str) -> bool:
    """Check if text is not empty."""
    return bool(text and text.strip())

# Exercise 2: Add type hints to this function
def validate_length(text, max_length):
    # Add type hints! What types are text and max_length? What does it return?
    return len(text) <= max_length

# Better version:
def validate_length_typed(text: str, max_length: int) -> bool:
    """Check if text length is within max_length."""
    return len(text) <= max_length

print(f"'Hello' within 10 chars? {validate_length_typed('Hello', 10)}")


print("\n" + "="*70)
print("PART 3: THE MIGHTY **kwargs")
print("="*70)

# **kwargs allows a function to accept ANY number of keyword arguments
# It's pronounced "keyword args" or just "kwargs"

def print_info(**kwargs):
    """Print all keyword arguments passed to this function."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# You can pass any keywords:
print_info(name="Alice", age=30, city="NYC")
print()
print_info(role="engineer", company="Google", level="senior")

# This is EXACTLY what .format() uses!
def fill_template(template: str, **kwargs) -> str:
    """Fill a template with keyword arguments."""
    return template.format(**kwargs)

# Example:
template = "Hello {name}, you are {age} years old"
result = fill_template(template, name="Bob", age=25)
print(f"\n{result}")

# Exercise 3: Create a function that builds a test case dictionary
def create_test_case(test_id: str, **kwargs) -> dict:
    """
    Create a test case dictionary with id and any additional fields.
    
    Example:
        create_test_case("TC001", prompt="Test this", priority="high")
        Returns: {"id": "TC001", "prompt": "Test this", "priority": "high"}
    """
    # Your code here
    # Hint: Start with {"id": test_id}, then add all kwargs to it
    pass

# Test it:
# test = create_test_case("TC001", prompt="Summarize", category="accuracy", score=95)
# print(f"\nCreated test: {test}")


print("\n" + "="*70)
print("PART 4: CLASSES - Creating Your Own Types")
print("="*70)

# A class is a blueprint for creating objects
# Think of it like a cookie cutter - the class is the cutter, objects are cookies

# Basic class syntax:
class Person:
    def __init__(self, name, age):
        """
        __init__ is the constructor - it runs when you create a new Person.
        'self' refers to the specific instance being created.
        """
        self.name = name  # Store name in this instance
        self.age = age    # Store age in this instance
    
    def greet(self):
        """Instance method - it can use self.name and self.age"""
        return f"Hi, I'm {self.name} and I'm {self.age} years old"
    
    def birthday(self):
        """Another method - increment age"""
        self.age += 1
        return f"{self.name} is now {self.age}!"

# Creating objects (instances) from the class:
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(person1.greet())
print(person2.greet())

# Each object has its own data:
print(f"\nAlice's age: {person1.age}")
print(f"Bob's age: {person2.age}")

# Call methods:
print(person1.birthday())


print("\n" + "="*70)
print("PART 5: Classes with Type Hints")
print("="*70)

class PromptTemplate:
    """A reusable template for prompts - this is what we used in the project!"""
    
    def __init__(self, template: str):
        """
        Initialize with a template string containing {placeholders}.
        
        Args:
            template: String with {variable} placeholders
        """
        self.template = template
    
    def fill(self, **kwargs) -> str:
        """
        Fill the template with provided values.
        
        Args:
            **kwargs: Variable names and values to insert
        
        Returns:
            Filled template string
        """
        return self.template.format(**kwargs)

# Using the class:
my_template = PromptTemplate("You are a {role}. Task: {task}")
prompt = my_template.fill(role="Python tutor", task="explain classes")
print(prompt)


print("\n" + "="*70)
print("PART 6: EXERCISES - Build Your Own Classes")
print("="*70)

# Exercise 4: Create a TestCase class
class TestCase:
    """
    A test case with id, prompt, and status.
    
    Usage:
        test = TestCase("TC001", "Test this prompt")
        test.mark_passed()
        print(test.status)  # "passed"
    """
    
    def __init__(self, test_id: str, prompt: str):
        # Your code here
        # Store test_id, prompt, and set status to "pending"
        pass
    
    def mark_passed(self):
        """Set status to 'passed'"""
        # Your code here
        pass
    
    def mark_failed(self):
        """Set status to 'failed'"""
        # Your code here
        pass
    
    def get_info(self) -> str:
        """Return a formatted string with test info"""
        # Your code here
        # Return something like: "TC001: Test this prompt (Status: pending)"
        pass

# Test your class:
# test1 = TestCase("TC001", "Validate this response")
# print(test1.get_info())
# test1.mark_passed()
# print(test1.get_info())


# Exercise 5: Create a Validator class
class Validator:
    """
    A validator with a name and a validation function.
    
    This shows how you can store functions inside objects!
    """
    
    def __init__(self, name: str):
        self.name = name
        self.validations_run = 0  # Counter
    
    def validate(self, text: str) -> bool:
        """
        Override this in your implementation.
        
        For now, just check if text is not empty.
        """
        self.validations_run += 1  # Increment counter
        # Your code here
        # Return True if text is not empty, False otherwise
        pass

# Test your validator:
# validator = Validator("EmptyCheck")
# print(f"Is 'hello' valid? {validator.validate('hello')}")
# print(f"Is '' valid? {validator.validate('')}")
# print(f"Validations run: {validator.validations_run}")


print("\n" + "="*70)
print("SOLUTIONS SECTION")
print("="*70)
print("Scroll down to see solutions after trying exercises yourself!")
print("="*70)

# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

print("\n" + "="*70)
print("SOLUTIONS")
print("="*70)

# Solution to Exercise 1:
def count_words_solution(text: str) -> int:
    """Count words in a string."""
    return len(text.split())

test_text = "This is a test sentence"
print(f"Solution 1 - Word count: {count_words_solution(test_text)}")


# Solution to Exercise 3:
def create_test_case_solution(test_id: str, **kwargs) -> dict:
    """Create a test case dictionary."""
    result = {"id": test_id}
    result.update(kwargs)  # Add all keyword arguments
    return result

test = create_test_case_solution("TC001", prompt="Summarize", category="accuracy")
print(f"\nSolution 3 - Test case: {test}")


# Solution to Exercise 4:
class TestCaseSolution:
    """A complete test case class."""
    
    def __init__(self, test_id: str, prompt: str):
        self.test_id = test_id
        self.prompt = prompt
        self.status = "pending"
    
    def mark_passed(self):
        self.status = "passed"
    
    def mark_failed(self):
        self.status = "failed"
    
    def get_info(self) -> str:
        return f"{self.test_id}: {self.prompt} (Status: {self.status})"

# Test:
test1 = TestCaseSolution("TC001", "Validate this response")
print(f"\nSolution 4:")
print(test1.get_info())
test1.mark_passed()
print(test1.get_info())


# Solution to Exercise 5:
class ValidatorSolution:
    """A working validator class."""
    
    def __init__(self, name: str):
        self.name = name
        self.validations_run = 0
    
    def validate(self, text: str) -> bool:
        self.validations_run += 1
        return bool(text and text.strip())

validator = ValidatorSolution("EmptyCheck")
print(f"\nSolution 5:")
print(f"Is 'hello' valid? {validator.validate('hello')}")
print(f"Is '' valid? {validator.validate('')}")
print(f"Validations run: {validator.validations_run}")


print("\n" + "="*70)
print("CONGRATULATIONS!")
print("="*70)
print("You now understand the 'hidden prerequisites' from Week 1!")
print()
print("Concepts mastered:")
print("✅ Functions with parameters and return values")
print("✅ Type hints (str, int, bool, dict)")
print("✅ **kwargs for flexible function arguments")
print("✅ Classes with __init__ constructors")
print("✅ Instance variables (self.variable)")
print("✅ Instance methods (functions inside classes)")
print()
print("These are EXACTLY what you used in the prompt-formatter project!")
print("="*70)
