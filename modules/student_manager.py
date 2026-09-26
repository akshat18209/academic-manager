# modules/student_manager.py
# Handles adding, viewing, updating and deleting student records.

from utils.validators import is_valid_roll, is_valid_name, roll_exists


def add_student(students, subjects):
    """Ask the user for a new student's details and add them to the list."""
    roll_text = input("Enter roll number: ")
    if not is_valid_roll(roll_text):
        print("Invalid roll number. Please enter digits only.")
        return students

    roll = int(roll_text)
    if roll_exists(roll, students):
        print("A student with this roll number already exists.")
        return students

    name = input("Enter student name: ")
    if not is_valid_name(name):
        print("Invalid name. Please enter letters and spaces only.")
        return students

    # start every subject at 0 marks -- marks are entered later
    marks = {}
    for subject in subjects:
        marks[subject] = 0

    new_student = {"roll": roll, "name": name, "marks": marks}
    students.append(new_student)
    print(f"Student '{name}' (Roll {roll}) added successfully.")
    return students


def find_student(students, roll):
    """Return the student dict matching a roll number, or None."""
    for student in students:
        if student["roll"] == roll:
            return student
    return None


def view_all_students(students):
    """Print a simple list of every student."""
    if len(students) == 0:
        print("No students found.")
        return

    print("\nRoll\tName")
    print("-" * 30)
    for student in students:
        print(f"{student['roll']}\t{student['name']}")


def delete_student(students, roll):
    """Remove a student by roll number. Returns the updated list."""
    student = find_student(students, roll)
    if student is None:
        print("No student found with that roll number.")
        return students

    students.remove(student)
    print(f"Student '{student['name']}' (Roll {roll}) deleted.")
    return students


def add_subject(subjects, max_marks, students, subject_name, max_mark):
    """Add a new subject and give every existing student 0 marks in it."""
    if subject_name in subjects:
        print("Subject already exists.")
        return subjects, max_marks, students

    subjects.append(subject_name)
    max_marks[subject_name] = max_mark

    for student in students:
        student["marks"][subject_name] = 0

    print(f"Subject '{subject_name}' added.")
    return subjects, max_marks, students
