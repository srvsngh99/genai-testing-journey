# Week 5: File Handling & JSON

## Week 5 Goal
By end of this week, you will:
- Master reading and writing text files
- Understand JSON serialization and deserialization
- Adopt modern path handling with `pathlib`
- Work with JSONL (JSON Lines) format
- Build `dataset-loader` — a dataset manager
- Push your fifth deliverable to GitHub

---

## Daily Breakdown

### Time Budget: 9 hours total
| Day | Focus | Time |
|-----|-------|------|
| Monday | Learn: Reading/Writing Text Files | 1 hr |
| Tuesday | Learn: JSON Serialization | 1 hr |
| Wednesday | Learn: Pathlib (Modern Paths) | 1 hr |
| Thursday | Learn: JSONL (Large Datasets) | 1 hr |
| Friday | Practice: Integration of concepts | 1 hr |
| Saturday | Project: Start `dataset-loader` | 2 hrs |
| Sunday | Project: Complete + Push to GitHub | 2 hrs |

---

## Resources

### YouTube
- [Corey Schafer: File Objects (Reading/Writing)](https://www.youtube.com/watch?v=Uh2ebFW8OYM)
- [Real Python: Python JSON](https://realpython.com/python-json/)

### Documentation
- [Python Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)
- [Pathlib Documentation](https://docs.python.org/3/library/pathlib.html)

---

## Practice Files Guide

Week 5 has **FOUR practice files** building up to the mini-project:

### File 1: `practice/01_text_files.py` (Monday)
**Covers:**
- Basic file I/O operations (read, write, append)
- Context managers (`with` statement) for safe file handling
- Error handling for file operations
- **Time:** 1 hour

### File 2: `practice/02_json_basics.py` (Tuesday)
**Covers:**
- `json.dumps` vs `json.dump` usage
- Loading and interacting with JSON data
- Parsing JSON strings from simulated API responses
- **Time:** 1 hour

### File 3: `practice/03_pathlib_intro.py` (Wednesday)
**Covers:**
- Modern file path manipulation using `pathlib` (replacing `os.path`)
- Creating cross-platform compatible paths
- Reading/writing directly from Path objects
- **Time:** 1 hour

### File 4: `practice/04_jsonl_handling.py` (Thursday)
**Covers:**
- Processing JSONL files (line-delimited JSON)
- Reading and appending to large datasets efficiently
- **Time:** 1 hour

---

# LEARNING TRACK

## Monday: Text Files (1 hour)

### Watch These Videos
1. **Corey Schafer: File Objects**
   - URL: https://www.youtube.com/watch?v=Uh2ebFW8OYM
   - Focus on: Reading, Writing, Context Managers (`with`)

### Practice Exercises
Run `week5/practice/01_text_files.py`.
- **Goal:** Be comfortable reading and writing simple `.txt` files without leaking resources (using `with`).

## Tuesday: JSON Basics (1 hour)

### Practice Exercises
Run `week5/practice/02_json_basics.py`.
- **Goal:** Understand the difference between `json.load()` (file) and `json.loads()` (string). This is CRITICAL for LLM API testing.

## Wednesday: Pathlib (1 hour)

### Practice Exercises
Run `week5/practice/03_pathlib_intro.py`.
- **Goal:** Stop using `os.path.join`. Start using `Path("folder") / "file.txt"`. It's cleaner and safer.

## Thursday: JSONL Handling (1 hour)

### Practice Exercises
Run `week5/practice/04_jsonl_handling.py`.
- **Goal:** Learn JSONL (JSON Lines). This is the standard for fine-tuning data (OpenAI/Anthropic) and storing large test logs.

## Friday: Review & Integration (1 hour)

Review the concepts from the week. Ensure you can:
1. Open a file safely.
2. Read JSON data from it.
3. Modify the data.
4. Save it back to a new path using `pathlib`.

---

## Week 5 Deliverables

## Saturday-Sunday: Build `dataset-loader`

**Mini-Project: `dataset-loader`**

### Why this matters in AI testing?
Prompt engineering is only half the battle; the other half is data. In production GenAI testing, you'll work with large datasets stored in JSON or JSONL formats (like fine-tuning data or batch evaluation logs). Mastering file handling allows you to automate the process of loading thousands of test cases, running them, and saving the results without manual intervention.

### Learning Focus
- Safe file I/O using Context Managers (`with`)
- Parsing and generating JSON and JSONL data
- cross-platform path handling with `pathlib`

### Mini-Project Overview
**A dataset manager that loads, validates, and saves test case data using modern Python file handling.**

```
dataset-loader/
├── datasets/               # Folder for JSON/JSONL samples
├── dataset_loader.py       # Main logic for loading and saving
├── schema_validator.py     # Logic to check JSON structure
└── README.md               # Project specific instructions
```
