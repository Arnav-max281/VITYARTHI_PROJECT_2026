# Student Academic Performance System

A simple Python program to manage student grades using a dictionary.

## Features

* Add, update, delete and search students
* View all students with their grades
* Class average, highest grade and lowest grade
* Grades are saved to `students.txt` when you exit

## How to run

```bash
python main.py
```

## How to test

```bash
cd tests
python test_system.py
```

## Files

* `main.py` - menu and program start
* `student_manager.py` - dictionary, add, delete, search
* `marks_manager.py` - update grade
* `grade_calculator.py` - class average, letter grade
* `performance_analysis.py` - highest and lowest grade
* `report_generator.py` - display all students
* `validation.py` - checks grade is between 0 and 100
* `file_handler.py` - save and load students from a file
* `tests/test_system.py` - tests for core functionality
