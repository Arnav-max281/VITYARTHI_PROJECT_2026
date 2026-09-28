# Initialising dictionary
student_grades = {}


# Add a new student
def add_student(name, grade):
    student_grades[name] = grade
    print(f"Student {name} added with grade {grade}.")


# Delete a student
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"Student {name} has been deleted.")
    else:
        print(f"Student {name} not found.")


# Search for a student
def search_student(name):
    if name in student_grades:
        print(f"{name}: {student_grades[name]}")
    else:
        print(f"Student {name} not found.")
