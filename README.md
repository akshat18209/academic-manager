# Student Result Management System

A command-line Python application to manage student records, calculate
grades, generate report cards, and view class-wide performance analytics —
built for the Python Essentials course project.

## Overview

Manually tracking and calculating student results is slow and error-prone.
This project automates the process: teachers/admins can add students, enter
subject-wise marks, instantly generate formatted report cards, and view
class analytics such as toppers, averages, and pass percentages.

Instead of a database or file formats like JSON/CSV, this project stores
all data inside a plain Python file (`data/data_store.py`), which the
program automatically rewrites every time data changes. This keeps
everything readable in pure Python — no external formats needed.

## Features

- **Student Management** — add, view, and delete student records
- **Marks Entry** — enter/update subject-wise marks with input validation
- **Grade Calculation** — automatic percentage, letter grade (A+ to F), and pass/fail
- **Report Card Generation** — printed to screen and saved as a `.txt` file per student
- **Class Analytics** — class average, topper, pass percentage, subject-wise averages
- **Persistent Storage** — all data is saved to `data/data_store.py` and reloaded automatically next time you run the program

## Technologies / Tools Used

- Python 3 (standard library only — no external packages required)
- Plain functions, lists, dictionaries, and tuples (no OOP, no try/except)
- Git for version control

## Project Structure

```
student-result-management-system/
├── README.md
├── statement.md
├── main.py                     # CLI entry point / menu
├── modules/
│   ├── student_manager.py      # Add/view/delete students, add subjects
│   ├── marks_manager.py        # Marks entry & grade calculation
│   ├── report_generator.py     # Report card generation
│   └── analytics.py            # Class-level statistics
├── data/
│   └── data_store.py           # Auto-generated "database" (subjects, marks, students)
├── utils/
│   ├── file_handler.py         # Save/load data to/from data_store.py
│   └── validators.py           # Input validation helpers
├── tests/
│   └── test_grade_calc.py      # Unit tests for grading logic
└── reports/                    # Generated report cards are saved here
```

## Steps to Install & Run

1. Make sure Python 3 is installed:
   ```
   python3 --version
   ```
2. Clone this repository:
   ```
   git clone https://github.com/{your-username}/student-result-management-system.git
   cd student-result-management-system
   ```
3. Run the program:
   ```
   python3 main.py
   ```
4. Follow the on-screen menu (1–7) to add students, enter marks, generate
   report cards, and view analytics.

No external dependencies or installation steps are needed — the whole
project runs with Python's standard library.

## Instructions for Testing

Run the included unit tests from the project's root folder:

```
python3 tests/test_grade_calc.py
```

You should see:
```
test_calculate_grade passed
test_calculate_percentage passed
test_is_pass passed

All tests passed!
```

You can also test manually by running `main.py` and trying each menu
option (add a student, enter marks, generate a report card, view class
analytics, delete a student).

## Grading Scheme

| Percentage | Grade |
|------------|-------|
| 90–100     | A+    |
| 80–89      | A     |
| 70–79      | B+    |
| 60–69      | B     |
| 50–59      | C     |
| 40–49      | D     |
| Below 40   | F     |

A student passes if their overall percentage is 40% or higher and
they score at least 33% in every individual subject.
