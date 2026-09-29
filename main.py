from student_manager import add_student, delete_student, search_student
from marks_manager import update_student
from grade_calculator import class_average
from performance_analysis import highest_grade, lowest_grade
from report_generator import display_all_students
from validation import get_valid_grade
from file_handler import save_students, load_students


# Main function
def main():

    load_students()

    while True:

        print("\n===== STUDENT GRADE MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Search Student")
        print("6. Class Average")
        print("7. Highest Grade")
        print("8. Lowest Grade")
        print("9. Exit")

        choice = input("Enter your choice: ")

        # Add student
        if choice == "1":

            name = input("Enter student name: ")
            grade = get_valid_grade("Enter student grade (0-100): ")
            add_student(name, grade)

        # Update student
        elif choice == "2":

            name = input("Enter student name to update: ")
            grade = get_valid_grade("Enter new grade (0-100): ")
            update_student(name, grade)

        # Delete student
        elif choice == "3":

            name = input("Enter student name to delete: ")

            delete_student(name)

        # Display students
        elif choice == "4":

            display_all_students()

        elif choice == "5":
            name = input("Enter student name to search: ")
            search_student(name)

        elif choice == "6":
            class_average()

        elif choice == "7":
            highest_grade()

        elif choice == "8":
            lowest_grade()

        elif choice == "9":
            save_students()
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
main()
