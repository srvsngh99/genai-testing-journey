# Week 3 Day 2: List Comprehensions
# Goal: Write concise, Pythonic loops

# Exercise 1: Transformation
# --------------------------
# Context: Converting toxicity scores (0-1) to percentages (0-100).
scores = [0.1, 0.5, 0.8, 0.95, 0.2]

# Create a new list 'percentages' where each score is multiplied by 100
# Expected output: [10.0, 50.0, 80.0, 95.0, 20.0]

# TODO: Write your list comprehension here


# Exercise 2: Filtering
# ---------------------
# Context: Keeping only failed test results.
results = ["PASS", "FAIL", "PASS", "FAIL", "ERROR"]

# Create a new list 'failures' that only contains items that are NOT "PASS"
# Expected output: ['FAIL', 'FAIL', 'ERROR']

# TODO: Write your list comprehension here


# Exercise 3: Conditional Logic
# -----------------------------
# Context: Labeling latency as 'Fast' or 'Slow'
latencies = [100, 500, 50, 1200, 300] # in milliseconds

# Create a new list 'labels'
# If latency < 400 -> "Fast"
# Else -> "Slow"
# Expected output: ['Fast', 'Slow', 'Fast', 'Slow', 'Fast']

# TODO: Write your list comprehension here
