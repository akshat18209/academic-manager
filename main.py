# main.py

from utils.file_handler import save_data, load_data
from utils.validators import is_valid_roll
from modules.student_manager import (
    add_student,
    view_all_students,
    find_student,
    delete_student,
)
from modules.marks_manager import enter_marks
from modules.report_generator import generate_report_card
from modules.analytics import print_class_report


def print_menu():
    print("\n" + "=" * 40)
    print("   STUDENT RESULT MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Enter/Update Marks")
    print("4. Generate Report Card")
    print("5. View Class Analytics")
    print("6. Delete Student")
    print("7. Save & Exit")
    print("=" * 40)


def main():
    subjects, max_marks, students = load_data()

    while True:
        print_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            students = add_student(students, subjects)

        elif choice == "2":
            view_all_students(students)

        elif choice == "3":
            roll_text = input("Enter roll number of student: ")
            if is_valid_roll(roll_text):
                student = find_student(students, int(roll_text))
                if student is None:
                    print("No student found with that roll number.")
                else:
                    student = enter_marks(student, subjects, max_marks)
            else:
                print("Invalid roll number.")

        elif choice == "4":
            roll_text = input("Enter roll number of student: ")
            if is_valid_roll(roll_text):
                student = find_student(students, int(roll_text))
                if student is None:
                    print("No student found with that roll number.")
                else:
                    generate_report_card(student, max_marks)
            else:
                print("Invalid roll number.")

        elif choice == "5":
            print_class_report(students, subjects, max_marks)

        elif choice == "6":
            roll_text = input("Enter roll number of student to delete: ")
            if is_valid_roll(roll_text):
                students = delete_student(students, int(roll_text))
            else:
                print("Invalid roll number.")

        elif choice == "7":
            save_data(subjects, max_marks, students)
            print("Data saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

        # auto-save after every action so data is never lost
        save_data(subjects, max_marks, students)


if __name__ == "__main__":
    main()
