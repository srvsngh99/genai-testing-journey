# Week 3 Day 5: Validation Challenge
# Goal: Build a mini validation library

"""
Scenario:
You are building the core logic for the Week 3 Mini-Project.
You need small, reusable functions to check if an LLM response is valid.
"""

# 1. JSON Validator
# -----------------
# Write a function 'is_valid_json_start(text)'
# It should return True if the stripped text starts with '{'
# Otherwise False

def is_valid_json_start(text: str) -> bool:
    """
    Check if text starts with '{' (indicating JSON).
    
    Args:
        text: The text to validate
        
    Returns:
        True if text starts with '{', False otherwise
    """
    return text.strip().startswith("{")


# 2. Length Validator
# -------------------
# Write a function 'check_length(text, min_len, max_len)'
# Returns True if text length is within bounds, else False

def check_length(text: str, min_len: int, max_len: int) -> bool:
    """
    Check if text length is within specified bounds.
    
    Args:
        text: The text to check
        min_len: Minimum allowed length (inclusive)
        max_len: Maximum allowed length (inclusive)
        
    Returns:
        True if length is within bounds, False otherwise
    """
    return min_len <= len(text) <= max_len


# 3. Keyword Check
# ----------------
# Write a function 'contains_word(text, word)'
# Returns True if 'word' is inside 'text' (case insensitive), else False

def contains_word(text: str, word: str) -> bool:
    """
    Check if a word exists in text (case insensitive).
    
    Args:
        text: The text to search in
        word: The word to search for
        
    Returns:
        True if word is found (case insensitive), False otherwise
    """
    return word.lower() in text.lower()


# 4. Master Validator
# -------------------
# Write a function 'validate_response(response)'
# It should use the functions above to check:
# - It starts with '{'
# - It is between 10 and 200 characters long
# - It contains the word "success"

# If ALL pass, return True. If ANY fail, return False (and maybe print which one failed)

def validate_response(response: str, verbose: bool = False) -> bool:
    """
    Validate an LLM response using multiple checks.
    
    Args:
        response: The response text to validate
        verbose: If True, print which validation failed
        
    Returns:
        True if all validations pass, False otherwise
    """
    # Check 1: Starts with '{'
    if not is_valid_json_start(response):
        if verbose:
            print("[FAIL] Validation failed: Response doesn't start with '{'")
        return False
    
    # Check 2: Length between 10 and 200 characters
    if not check_length(response, 10, 200):
        if verbose:
            print(f"[FAIL] Validation failed: Length {len(response)} not in range [10, 200]")
        return False
    
    # Check 3: Contains "success"
    if not contains_word(response, "success"):
        if verbose:
            print("[FAIL] Validation failed: Response doesn't contain 'success'")
        return False
    
    if verbose:
        print("[PASS] All validations passed!")
    return True


# ============================================
# TEST CASES
# ============================================

print("=" * 50)
print("TESTING INDIVIDUAL FUNCTIONS")
print("=" * 50)

# Test 1: is_valid_json_start
print("\n1. Testing is_valid_json_start():")
print(f"   '{{test}}' -> {is_valid_json_start('{test}')}")  # True
print(f"   '  {{test}}' -> {is_valid_json_start('  {test}')}")  # True (strips whitespace)
print(f"   'test' -> {is_valid_json_start('test')}")  # False

# Test 2: check_length
print("\n2. Testing check_length():")
print(f"   'hello' (5 chars) in [3, 10] -> {check_length('hello', 3, 10)}")  # True
print(f"   'hi' (2 chars) in [3, 10] -> {check_length('hi', 3, 10)}")  # False
print(f"   'very long text' (14 chars) in [3, 10] -> {check_length('very long text', 3, 10)}")  # False

# Test 3: contains_word
print("\n3. Testing contains_word():")
print(f"   'Hello World' contains 'hello' -> {contains_word('Hello World', 'hello')}")  # True
print(f"   'SUCCESS!' contains 'success' -> {contains_word('SUCCESS!', 'success')}")  # True
print(f"   'Hello World' contains 'goodbye' -> {contains_word('Hello World', 'goodbye')}")  # False

print("\n" + "=" * 50)
print("TESTING MASTER VALIDATOR")
print("=" * 50)

# Test Case 1: Should FAIL (doesn't start with '{')
print("\nTest 1: 'fail'")
result1 = validate_response("fail", verbose=True)
print(f"Result: {result1}\n")

# Test Case 2: Should PASS
print("Test 2: '{\"status\": \"success\"}'")
result2 = validate_response('{"status": "success"}', verbose=True)
print(f"Result: {result2}\n")

# Test Case 3: Should FAIL (too long)
print("Test 3: Very long text")
long_text = "{too long...}" * 20
result3 = validate_response(long_text, verbose=True)
print(f"Result: {result3}\n")

# Test Case 4: Should FAIL (no "success" word)
print("Test 4: '{\"status\": \"complete\"}'")
result4 = validate_response('{"status": "complete"}', verbose=True)
print(f"Result: {result4}\n")

# Test Case 5: Should FAIL (too short)
print("Test 5: '{success}'")
result5 = validate_response('{success}', verbose=True)
print(f"Result: {result5}\n")

# Test Case 6: Should PASS (edge case - exactly 10 chars with success)
print("Test 6: '{SUCCESS}' (10 chars)")
result6 = validate_response('{SUCCESS}', verbose=True)
print(f"Result: {result6}\n")

print("=" * 50)
print("CHALLENGE COMPLETE!")
print("=" * 50)
