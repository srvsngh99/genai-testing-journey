# Week 3 Day 2: List Comprehensions
# Goal: Write concise, Pythonic loops

# Exercise 1: Transformation
# --------------------------
# Context: Converting toxicity scores (0-1) to percentages (0-100).
scores = [0.1, 0.5, 0.8, 0.95, 0.2]

# Create a new list 'percentages' where each score is multiplied by 100
# Expected output: [10.0, 50.0, 80.0, 95.0, 20.0]

# using for loop
percentage = []

for score in scores:
    percentage.append(score * 100)

print(percentage)

# list comprehension
percentage = [score * 100 for score in scores]
print(percentage)


# Exercise 2: Filtering
# ---------------------
# Context: Keeping only failed test results.
results = ["PASS", "FAIL", "PASS", "FAIL", "ERROR"]

# Create a new list 'failures' that only contains items that are NOT "PASS"
# Expected output: ['FAIL', 'FAIL', 'ERROR']

failures = [f for f in results if f != "PASS"]
print (failures)

# Exercise 3: Conditional Logic
# -----------------------------
# Context: Labeling latency as 'Fast' or 'Slow'
latencies = [100, 500, 50, 1200, 300] # in milliseconds

# Create a new list 'labels'
# If latency < 400 -> "Fast"
# Else -> "Slow"
# Expected output: ['Fast', 'Slow', 'Fast', 'Slow', 'Fast']

labels = ['Fast' if l < 400 else 'Slow' for l in latencies]
print(labels)
