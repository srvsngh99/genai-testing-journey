# Week 6: Error Handling & Logging

## Week 6 Goal
By end of this week, you will:
- Master try/except/finally patterns for robust code
- Create and raise custom exceptions for specific failure modes
- Configure the Python logging module for tracking test execution
- Implement structured log formatting and multiple log levels
- Build robust-api-caller (Mini-project)
- Push your sixth deliverable to GitHub

## Daily Breakdown

### Time Budget: 9 hours total
| Day | Focus | Time |
|-----|-------|------|
| Monday | Learn: try/except/finally patterns | 1 hr |
| Tuesday | Learn: Custom exceptions | 1 hr |
| Wednesday | Learn: Python logging module | 1 hr |
| Thursday | Learn: Log levels and formatting | 1 hr |
| Friday | Practice: Debugging techniques | 1 hr |
| Saturday | Project: Start robust-api-caller | 2 hrs |
| Sunday | Complete mini-project + Push to GitHub | 1 hr |

## Resources

### YouTube
- [Corey Schafer: Exceptions - Try/Except/Else/Finally](https://www.youtube.com/watch?v=NIWwJbo-9_8)
- [Corey Schafer: Logging Basics](https://www.youtube.com/watch?v=-ARI4Cz-awo)

### Documentation
- [Python Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Python Logging HOWTO](https://docs.python.org/3/howto/logging.html)

## Practice Files Guide

Week 6 has 4 practice files to cover everything for the mini-project:

### File 1: `practice/01_try_except.py`
**Covers:**
- Basic error handling with try/except
- Catching specific exceptions
- Using else and finally blocks
- **Time:** 1 hour

### File 2: `practice/02_custom_exceptions.py`
**Covers:**
- Defining custom exception classes
- Raising exceptions programmatically
- Carrying data in exceptions
- **Time:** 1 hour

### File 3: `practice/03_logging_basics.py`
**Covers:**
- Basic logging configuration
- Logging to console and files
- Log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- **Time:** 1 hour

### File 4: `practice/04_log_formatting.py`
**Covers:**
- Customizing log message formats
- Adding timestamps and location info to logs
- Best practices for logging in test utilities
- **Time:** 1 hour

# LEARNING TRACK

## Monday: Exception Handling (1 hour)

### Watch These Videos
1. **Corey Schafer: Exceptions**
   - URL: https://www.youtube.com/watch?v=NIWwJbo-9_8
   - Why: Learn how to handle runtime errors gracefully.

### Practice Exercises
Run `week6/practice/01_try_except.py`.

## Tuesday: Custom Exceptions (1 hour)

### Practice Exercises
Run `week6/practice/02_custom_exceptions.py`.

## Wednesday: Logging Module (1 hour)

### Watch These Videos
1. **Corey Schafer: Logging Basics**
   - URL: https://www.youtube.com/watch?v=-ARI4Cz-awo

### Practice Exercises
Run `week6/practice/03_logging_basics.py`.

## Thursday: Log Formatting (1 hour)

### Practice Exercises
Run `week6/practice/04_log_formatting.py`.

## Friday: Integration (1 hour)

Review how error handling and logging work together to create maintainable test automation.

## Week 6 Deliverables

## Saturday-Sunday: Build `robust-api-caller`

**Mini-Project: `robust-api-caller`**

### Why this matters in AI testing?
LLM APIs are prone to timeouts, rate limits, and transient failures. A tester must build utilities that can handle these errors gracefully using retries, exponential backoff, and clear logging for debugging.

### Learning Focus
- Strategic use of try/except for API calls
- modern `requests` library
- Comprehensive logging for request/response tracking
- Custom exceptions for different API failure modes
- Resilience patterns (retry logic targeting 5xx errors)

### Mini-Project Overview
**A resilient HTTP caller utility for LLM APIs with built-in logging and error recovery.**
```
robust-api-caller/
├── core/
│   ├── api_client.py
│   ├── exceptions.py
│   └── logger_config.py
└── main.py
```
