# Week 4: Modules, Packages & Virtual Environments

## Week 4 Goal
By end of this week, you will:
- Stop writing "single file" scripts and start building **Software Projects**
- Master **Modules** (Splitting code into files)
- Master **Packages** (Organizing files into folders)
- Understand **Virtual Environments** (Managing dependencies)
- Build `llm-test-utils` — your first reusable Python package
- Push your fourth deliverable to GitHub

---

## Daily Breakdown

### Time Budget: 9 hours total
| Day | Focus | Time |
|-----|-------|------|
| Monday | Learn: Modules Basics | 1 hr |
| Tuesday | Learn: Packages & `__init__` | 1 hr |
| Wednesday | Learn: Virtual Environments | 1 hr |
| Thursday | Learn: Paths & Imports | 1 hr |
| Friday | Practice: Structure Refactor Challenge | 1 hr |
| Saturday | Project: Start `llm_test_utils` | 2 hrs |
| Sunday | Project: Complete + Push to GitHub | 2 hrs |

---

## Resources

### YouTube
- [Corey Schafer: Import Modules](https://www.youtube.com/watch?v=CqvZ3vGoGs0)
- [Corey Schafer: Virtual Environments](https://www.youtube.com/watch?v=Kg1Yvry_Ydk)

### Documentation
- [Python Modules](https://docs.python.org/3/tutorial/modules.html)
- [venv — Creation of virtual environments](https://docs.python.org/3/library/venv.html)

---

## Practice Files Guide

Week 4 is different. **You cannot just run the file.** You often need to create *other* files to import.

### File 1: `practice/01_modules_basics.py` (Monday)
**Covers:**
- Creating a separate `.py` file and importing it
- `import module` vs `from module import function`
- Aliasing with `as`
- **Time:** 1 hour

### File 2: `practice/02_packages_intro.py` (Tuesday)
**Covers:**
- Creating distinct folders for your code
- The role of `__init__.py`
- Converting a folder into a Python Package
- **Time:** 1 hour

### File 3: `practice/03_venv_setup.py` (Wednesday)
**Covers:**
- Why we need virtual environments (separation)
- Creating and activating a `venv`
- Installing packages (e.g., `requests`, `pytest`)
- **Time:** 1 hour

### File 4: `practice/04_paths_and_imports.py` (Thursday)
**Covers:**
- How Python finds modules (`sys.path`)
- Debugging "Module Not Found" errors
- Relative vs Absolute imports
- **Time:** 1 hour

### File 5: `practice/05_structure_challenge.py` (Friday)
**Covers:**
- **The Boss Level:** Taking a messy 100-line script and refactoring it into a clean package structure
- **Time:** 1 hour

---

# LEARNING TRACK

## Monday: Modules Basics (1 hour)

Run `week4/practice/01_modules_basics.py`. It will ask you to create a helper file `my_math.py`.
- **Goal:** Understand that code can live in other files.

## Tuesday: Packages (1 hour)

Run `week4/practice/02_packages_intro.py`. It will ask you to create a folder `text_tools` with an `__init__.py`.
- **Goal:** Understand directories as namespaces.

## Wednesday: Virtual Envs (1 hour)

Run `week4/practice/03_venv_setup.py`. It will check if you are running inside a virtual environment.
- **Goal:** Never pollute your global Python install again.

## Thursday: Imports & Paths (1 hour)

Run `week4/practice/04_paths_and_imports.py`. It will simulate common import errors.
- **Goal:** Be able to fix `ModuleNotFoundError`.

## Friday: Refactor Challenge (1 hour)

Run `week4/practice/05_structure_challenge.py`. It contains a "monolith" of code.
- **Goal:** Break it apart into `helpers.py`, `config.py`, and `main.py`.

---

## Week 4 Deliverables

## Saturday-Sunday: Build `llm-test-utils`

**Mini-Project: `llm-test-utils`**
```
Create a reusable package:
llm_test_utils/
├── __init__.py
├── validators.py      # From week 3
├── formatters.py      # From week 1
├── test_cases.py      # From week 2
├── helpers.py         # Common utilities
└── requirements.txt
```
