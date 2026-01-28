# Exercise 1: Unique Items (Sets)
# You have a list with duplicates: ["python", "java", "python", "c++", "java"]
languages = ["python", "java", "python", "c++", "java"]

# Convert it to a set to remove duplicates
unique_languages = set(languages)
print("Unique Languages:", unique_languages)

# Exercise 2: Set Operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Find items in both (Intersection)
intersection = set_a & set_b
print("Intersection:", intersection)

# Find items only in set_a (Difference)
only_a = set_a - set_b
print("Only in set_a:", only_a)

# Union of both sets
union = set_a | set_b
print("Union:", union) 

# Exercise 3: Fixed Data (Tuples)
# Create a tuple representing a point (x, y)
point = (10, 20)
print("Point:", point)

# Try to change it (and see it fail!)
# point[0] = 30 # This would cause a TypeError

# Unpack the tuple into two variables
x, y = point
print(f"Unpacked: x={x}, y={y}")
