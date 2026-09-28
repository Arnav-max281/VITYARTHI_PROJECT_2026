from student_manager import student_grades


# Calculate class average
def class_average():
    if student_grades:
        total = sum(student_grades.values())
        average = total / len(student_grades)
        print(f"Class Average: {average:.2f}")
    else:
        print("No students found.")


# Convert marks into a letter grade
def get_letter_grade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"
