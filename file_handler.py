from student_manager import student_grades


# Save all students to a file
def save_students():
    file = open("students.txt", "w")
    for name, grade in student_grades.items():
        file.write(f"{name},{grade}\n")
    file.close()


# Load students from the file
def load_students():
    try:
        file = open("students.txt", "r")
        for line in file:
            name, grade = line.strip().split(",")
            student_grades[name] = int(grade)
        file.close()
    except FileNotFoundError:
        pass
