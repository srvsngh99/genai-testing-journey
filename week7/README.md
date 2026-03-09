# Week 7: pytest Fundamentals

## Week 7 Goal
By end of this week, you will:
- Understand pytest installation and basic configuration
- Write test functions following proper naming conventions
- Use assertions and matchers for robust verification
- Master test discovery and organization patterns
- Run and filter tests using CLI options
- Build test-suite-basics (Mini-project)
- Push your seventh deliverable to GitHub

## Daily Breakdown

### Time Budget: 9 hours total
| Day | Focus | Time |
|-----|-------|------|
| Monday | Learn: pytest installation and naming | 1 hr |
| Tuesday | Learn: Assertions and matchers | 1 hr |
| Wednesday | Learn: Test discovery patterns | 1 hr |
| Thursday | Learn: Running and filtering tests | 1 hr |
| Friday | Practice: Test organization | 1 hr |
| Saturday | Project: Start test-suite-basics | 2 hrs |
| Sunday | Complete mini-project + Push to GitHub | 1 hr |

## Resources

### YouTube
- [freeCodeCamp: Pytest Tutorial - How to Test Python Code](https://www.youtube.com/watch?v=cHYq1MRoyI0)

### Documentation
- [pytest Documentation](https://docs.pytest.org/en/latest/)
- [Using pytest with existing test suites](https://docs.pytest.org/en/latest/getting-started.html)

## Practice Files Guide

Week 7 has 4 practice files to cover everything for the mini-project:

### File 1: `practice/01_first_test.py`
**Covers:**
- Writing basic test functions
- Proper naming conventions for tests
- Running tests from the command line
- **Time:** 1 hour

### File 2: `practice/02_assertions.py`
**Covers:**
- Using the assert statement effectively
- Testing for expected exceptions
- Verifying complex data structures (lists, dicts)
- **Time:** 1 hour

### File 3: `practice/03_test_discovery.py`
**Covers:**
- Organizing tests into files and folders
- How pytest finds tests automatically
- Using classes to group related tests
- **Time:** 1 hour

### File 4: `practice/04_running_tests.py`
**Covers:**
- Command line arguments for pytest
- Filtering tests by keywords (-k)
- Controlling test execution (verbose, stop on failure)
- **Time:** 1 hour

# LEARNING TRACK

## Monday: pytest Basics (1 hour)

### Watch These Videos
1. **freeCodeCamp: Pytest Tutorial**
   - URL: https://www.youtube.com/watch?v=cHYq1MRoyI0
   - Why: Understand the power of pytest and how it differs from unittest.

### Practice Exercises
Run `week7/practice/01_first_test.py`.

## Tuesday: Assertions (1 hour)

### Practice Exercises
Run `week7/practice/02_assertions.py`.

## Wednesday: Test Discovery (1 hour)

### Practice Exercises
Run `week7/practice/03_test_discovery.py`.

## Thursday: Filtering Tests (1 hour)

### Practice Exercises
Run `week7/practice/04_running_tests.py`.

## Friday: Review (1 hour)

Ensure you understand how pytest identifies and executes your tests.

## Week 7 Deliverables

## Saturday-Sunday: Build `test-suite-basics`

**Mini-Project: `test-suite-basics`**

### Why this matters in AI testing?
An AI testing framework is only as good as its test suite. You need to know how to organize hundreds of test cases, run specific subsets, and interpret the results efficiently.

### Learning Focus
- Structural organization of test files
- Comprehensive verification using assertions
- Handling edge cases and failure scenarios in tests
- Using pytest CLI for efficient test execution

### Mini-Project Overview
**A foundational test suite for validating LLM utility functions with organized test discovery.**
```
test-suite-basics/
├── tests/
│   ├── test_validators.py
│   ├── test_formatters.py
│   └── test_loaders.py
└── pytest.ini
```
