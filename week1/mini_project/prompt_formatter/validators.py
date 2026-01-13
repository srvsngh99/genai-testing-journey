

def validate_not_empty(value: str) -> bool:
    """
    Check if the value is not empty after stripping whitespace.
    """
    return bool(value and value.strip())

def validate_max_length(value: str, max_length: int) -> bool:
    """
    Check if the value's length is less than or equal to max_length.
    """
    return len(value) <= max_length

def validate_contains_keywords(value: str, keywords: list[str]) -> bool:
    """
    Check if the value contains all of the specified keywords.
    """ 
    return all(keyword in value for keyword in keywords)