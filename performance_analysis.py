from student_manager import student_grades


# Find highest grade
def highest_grade():
    if student_grades:
        highest = max(student_grades.values())

        for name, grade in student_grades.items():
            if grade == highest:
                print(f"Highest Grade: {name} - {grade}")
    else:
        print("No students found.")


# Find lowest grade
def lowest_grade():
    if student_grades:
        lowest = min(student_grades.values())

        for name, grade in student_grades.items():
            if grade == lowest:
                print(f"Lowest Grade: {name} - {grade}")
    else:
        print("No students found.")
