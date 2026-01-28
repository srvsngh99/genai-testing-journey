"""
Week 3 Mini-Project: LLM Response Validator
============================================

This is a comprehensive validation library for LLM responses.
It combines all concepts learned in Week 3:
- Control Flow (if/else, loops)
- List Comprehensions
- Functions (basic and advanced)
- Validation Logic

"""

import json
from typing import List, Dict, Optional, Tuple


# ============================================
# CORE VALIDATION FUNCTIONS
# ============================================

def is_valid_json(text: str) -> bool:
    """
    Check if text is valid JSON.
    
    Args:
        text: The text to validate
        
    Returns:
        True if text is valid JSON, False otherwise
    """
    try:
        json.loads(text)
        return True
    except (json.JSONDecodeError, TypeError):
        return False


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


def contains_keywords(text: str, keywords: List[str], case_sensitive: bool = False) -> bool:
    """
    Check if text contains all specified keywords.
    
    Args:
        text: The text to search in
        keywords: List of keywords to search for
        case_sensitive: Whether to perform case-sensitive search
        
    Returns:
        True if all keywords are found, False otherwise
    """
    if not case_sensitive:
        text = text.lower()
        keywords = [kw.lower() for kw in keywords]
    
    return all(keyword in text for keyword in keywords)


def check_forbidden_words(text: str, forbidden: List[str]) -> Tuple[bool, List[str]]:
    """
    Check if text contains any forbidden words.
    
    Args:
        text: The text to check
        forbidden: List of forbidden words
        
    Returns:
        Tuple of (is_clean, found_forbidden_words)
        - is_clean: True if no forbidden words found
        - found_forbidden_words: List of forbidden words that were found
    """
    text_lower = text.lower()
    found = [word for word in forbidden if word.lower() in text_lower]
    return (len(found) == 0, found)


def extract_json_field(text: str, field: str) -> Optional[str]:
    """
    Extract a specific field from JSON text.
    
    Args:
        text: JSON text
        field: Field name to extract
        
    Returns:
        Field value if found, None otherwise
    """
    try:
        data = json.loads(text)
        return data.get(field)
    except (json.JSONDecodeError, TypeError, AttributeError):
        return None


# ============================================
# ADVANCED VALIDATION FUNCTIONS
# ============================================

def validate_response(
    response: str,
    min_length: int = 10,
    max_length: int = 1000,
    required_keywords: Optional[List[str]] = None,
    forbidden_words: Optional[List[str]] = None,
    must_be_json: bool = False,
    verbose: bool = False
) -> Dict[str, any]:
    """
    Comprehensive validation of an LLM response.
    
    Args:
        response: The response text to validate
        min_length: Minimum allowed length
        max_length: Maximum allowed length
        required_keywords: List of keywords that must be present
        forbidden_words: List of words that must not be present
        must_be_json: Whether response must be valid JSON
        verbose: If True, print detailed validation results
        
    Returns:
        Dictionary with validation results:
        {
            'valid': bool,
            'errors': List[str],
            'warnings': List[str],
            'metadata': Dict
        }
    """
    errors = []
    warnings = []
    metadata = {
        'length': len(response),
        'is_json': False,
        'found_keywords': [],
        'found_forbidden': []
    }
    
    # Check 1: Length validation
    if not check_length(response, min_length, max_length):
        errors.append(f"Length {len(response)} not in range [{min_length}, {max_length}]")
    
    # Check 2: JSON validation (if required)
    if must_be_json:
        if is_valid_json(response):
            metadata['is_json'] = True
        else:
            errors.append("Response is not valid JSON")
    else:
        # Just check if it's JSON for metadata
        metadata['is_json'] = is_valid_json(response)
    
    # Check 3: Required keywords
    if required_keywords:
        if contains_keywords(response, required_keywords):
            metadata['found_keywords'] = required_keywords
        else:
            # Find which keywords are missing
            missing = [kw for kw in required_keywords if kw.lower() not in response.lower()]
            errors.append(f"Missing required keywords: {missing}")
    
    # Check 4: Forbidden words
    if forbidden_words:
        is_clean, found = check_forbidden_words(response, forbidden_words)
        if not is_clean:
            metadata['found_forbidden'] = found
            errors.append(f"Contains forbidden words: {found}")
    
    # Check 5: Empty response
    if not response.strip():
        errors.append("Response is empty")
    
    # Compile results
    is_valid = len(errors) == 0
    
    if verbose:
        print("\n" + "=" * 60)
        print("VALIDATION REPORT")
        print("=" * 60)
        print(f"Response: {response[:100]}{'...' if len(response) > 100 else ''}")
        print(f"\nStatus: {'[VALID]' if is_valid else '[INVALID]'}")
        print(f"\nMetadata:")
        print(f"  - Length: {metadata['length']}")
        print(f"  - Is JSON: {metadata['is_json']}")
        if metadata['found_keywords']:
            print(f"  - Found Keywords: {metadata['found_keywords']}")
        if metadata['found_forbidden']:
            print(f"  - Found Forbidden: {metadata['found_forbidden']}")
        
        if errors:
            print(f"\nErrors ({len(errors)}):")
            for i, error in enumerate(errors, 1):
                print(f"  {i}. {error}")
        
        if warnings:
            print(f"\nWarnings ({len(warnings)}):")
            for i, warning in enumerate(warnings, 1):
                print(f"  {i}. {warning}")
        
        if is_valid:
            print("\n[PASS] All validations passed!")
        print("=" * 60)
    
    return {
        'valid': is_valid,
        'errors': errors,
        'warnings': warnings,
        'metadata': metadata
    }


def batch_validate(
    responses: List[str],
    **validation_kwargs
) -> Dict[str, any]:
    """
    Validate multiple responses at once.
    
    Args:
        responses: List of response texts to validate
        **validation_kwargs: Arguments to pass to validate_response
        
    Returns:
        Dictionary with batch validation results
    """
    results = []
    
    for i, response in enumerate(responses):
        result = validate_response(response, verbose=False, **validation_kwargs)
        result['index'] = i
        result['response'] = response
        results.append(result)
    
    # Summary statistics
    valid_count = sum(1 for r in results if r['valid'])
    invalid_count = len(results) - valid_count
    
    return {
        'total': len(responses),
        'valid': valid_count,
        'invalid': invalid_count,
        'success_rate': (valid_count / len(responses) * 100) if responses else 0,
        'results': results
    }


# ============================================
# UTILITY FUNCTIONS
# ============================================

def filter_valid_responses(
    responses: List[str],
    **validation_kwargs
) -> List[str]:
    """
    Filter a list of responses, keeping only valid ones.
    
    Args:
        responses: List of response texts
        **validation_kwargs: Arguments to pass to validate_response
        
    Returns:
        List of valid responses
    """
    return [
        response for response in responses
        if validate_response(response, verbose=False, **validation_kwargs)['valid']
    ]


def get_validation_summary(batch_results: Dict) -> str:
    """
    Generate a human-readable summary of batch validation results.
    
    Args:
        batch_results: Results from batch_validate
        
    Returns:
        Formatted summary string
    """
    summary = f"""
Validation Summary
==================
Total Responses: {batch_results['total']}
Valid: {batch_results['valid']} ({batch_results['success_rate']:.1f}%)
Invalid: {batch_results['invalid']} ({100 - batch_results['success_rate']:.1f}%)
"""
    return summary


# ============================================
# DEMO / TESTING
# ============================================

def run_demo():
    """Run a comprehensive demo of the validation library."""
    
    print("\n" + "=" * 60)
    print("WEEK 3 MINI-PROJECT: LLM RESPONSE VALIDATOR")
    print("=" * 60)
    
    # Test Case 1: Valid JSON response
    print("\n" + "=" * 60)
    print("TEST 1: Valid JSON Response")
    print("=" * 60)
    response1 = '{"status": "success", "message": "Task completed", "data": [1, 2, 3]}'
    result1 = validate_response(
        response1,
        min_length=10,
        max_length=200,
        required_keywords=["success"],
        must_be_json=True,
        verbose=True
    )
    
    # Test Case 2: Invalid - too short
    print("\n" + "=" * 60)
    print("TEST 2: Too Short Response")
    print("=" * 60)
    response2 = "OK"
    result2 = validate_response(
        response2,
        min_length=10,
        max_length=200,
        verbose=True
    )
    
    # Test Case 3: Invalid - contains forbidden words
    print("\n" + "=" * 60)
    print("TEST 3: Contains Forbidden Words")
    print("=" * 60)
    response3 = "This response contains error and failure messages"
    result3 = validate_response(
        response3,
        forbidden_words=["error", "failure"],
        verbose=True
    )
    
    # Test Case 4: Invalid - missing required keywords
    print("\n" + "=" * 60)
    print("TEST 4: Missing Required Keywords")
    print("=" * 60)
    response4 = "The task has been completed successfully"
    result4 = validate_response(
        response4,
        required_keywords=["success", "validation", "complete"],
        verbose=True
    )
    
    # Test Case 5: Batch validation
    print("\n" + "=" * 60)
    print("TEST 5: Batch Validation")
    print("=" * 60)
    
    test_responses = [
        '{"status": "success", "result": "done"}',
        "Short",
        '{"status": "success", "message": "All validations passed"}',
        "This is a valid response with enough length",
        "",
        '{"error": "Something went wrong"}',
    ]
    
    batch_results = batch_validate(
        test_responses,
        min_length=10,
        max_length=200,
        required_keywords=["success"]
    )
    
    print(get_validation_summary(batch_results))
    
    print("\nDetailed Results:")
    for result in batch_results['results']:
        status = "[VALID]" if result['valid'] else "[INVALID]"
        response_preview = result['response'][:50] + "..." if len(result['response']) > 50 else result['response']
        print(f"  [{result['index']}] {status}: {response_preview}")
        if result['errors']:
            for error in result['errors']:
                print(f"      - {error}")
    
    # Test Case 6: Filter valid responses
    print("\n" + "=" * 60)
    print("TEST 6: Filter Valid Responses")
    print("=" * 60)
    
    valid_only = filter_valid_responses(
        test_responses,
        min_length=10,
        max_length=200,
        required_keywords=["success"]
    )
    
    print(f"\nOriginal count: {len(test_responses)}")
    print(f"Valid count: {len(valid_only)}")
    print("\nValid responses:")
    for i, response in enumerate(valid_only, 1):
        print(f"  {i}. {response}")
    
    # Test Case 7: JSON field extraction
    print("\n" + "=" * 60)
    print("TEST 7: JSON Field Extraction")
    print("=" * 60)
    
    json_response = '{"status": "success", "user": "Sourav", "score": 95}'
    print(f"Response: {json_response}")
    print(f"\nExtracted fields:")
    print(f"  - status: {extract_json_field(json_response, 'status')}")
    print(f"  - user: {extract_json_field(json_response, 'user')}")
    print(f"  - score: {extract_json_field(json_response, 'score')}")
    print(f"  - missing_field: {extract_json_field(json_response, 'missing_field')}")
    
    print("\n" + "=" * 60)
    print("DEMO COMPLETE!")
    print("=" * 60)


if __name__ == "__main__":
    run_demo()
