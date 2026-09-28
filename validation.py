# Get a grade between 0 and 100
def get_valid_grade(message):
    grade = int(input(message))
    while grade < 0 or grade > 100:
        print("Grade must be between 0 and 100.")
        grade = int(input(message))
    return grade
