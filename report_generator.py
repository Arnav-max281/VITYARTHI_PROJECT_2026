from student_manager import student_grades
from grade_calculator import get_letter_grade


# View all students
def display_all_students():
    if student_grades:
        print("\nStudent Grades:")

        for name, grade in student_grades.items():
            print(f"{name}: {grade} ({get_letter_grade(grade)})")

    else:
        print("No students found.")
