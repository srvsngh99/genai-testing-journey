from prompt_formatter.validators import validate_not_empty, validate_contains_keywords, validate_max_length

print(validate_not_empty("Hello"))
print(validate_not_empty("   "))

print(validate_contains_keywords("Hello World", ["Hello", "World"]))
print(validate_contains_keywords("Hello World", ["Hello", "Python"]))

print(validate_max_length("Hello World", 10))   
print(validate_max_length("Hello World", 11))   
