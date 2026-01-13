

def normalize_whitespace(text: str) -> str:
    return " ".join(text.split())

def clean_response(response: str) -> str:
    return normalize_whitespace(response.strip())
