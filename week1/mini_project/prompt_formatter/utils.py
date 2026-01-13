def count_tokens_estimate(text: str) -> int:
    """
    Rough estimate of token count (~4 characters per token).
    """
    return len(text) // 4

def format_list_as_text(items: list, style: str = "numbered") -> str:
    """
    Format a list of strings into a pretty string for prompts.
    """
    if style == "numbered":
        # Use enumerate to get the index (1, 2, 3...) and the item
        return "\n".join(f"{i+1}. {item}" for i, item in enumerate(items))
    elif style == "bullet":
        # Join items with a newline and a dash
        return "\n".join(f"- {item}" for item in items)
    
    return "\n".join(items)