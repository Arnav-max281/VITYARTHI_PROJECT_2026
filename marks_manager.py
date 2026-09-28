from student_manager import student_grades


# Update a student
def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"Student {name} updated with new grade {grade}.")
    else:
        print(f"Student {name} not found.")
