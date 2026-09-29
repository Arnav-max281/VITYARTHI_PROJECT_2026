# Student Academic Performance System

A simple Python program to manage student grades using a dictionary.

## Features
- Add, update, delete and search students
- View all students with their grades
- Class average, highest grade and lowest grade
- Grades are saved to `students.txt` when you exit

## Project Structure

```
Student-Academic-Performance-System/
│
├── main.py                   # Entry point: menu loop wiring everything together
│
├── student_manager.py         # Add / delete / search / display students
├── marks_manager.py           # Add / update / delete subject marks
├── grade_calculator.py        # Average + letter grade calculation
├── performance_analysis.py    # Class average, highest/lowest, subject topper
├── report_generator.py        # Build & save student/class text reports
├── validation.py              # Shared input validation helpers
├── file_handler.py            # Load/save the student database (JSON)
│
├── tests/
│   └── test_system.py         # Unit tests for the core modules
│
└── README.md
```
## How to run
    python main.py

## How to test
    cd tests
    python test_system.py

## Files
- main.py - menu and program start
- student_manager.py - dictionary, add, delete, search
- marks_manager.py - update grade
- grade_calculator.py - class average, letter grade
- performance_analysis.py - highest and lowest grade
- report_generator.py - display all students
- validation.py - checks grade is between 0 and 100
- file_handler.py - save and load students from a file
- tests/test_system.py - simple tests
