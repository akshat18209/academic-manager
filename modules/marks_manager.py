# modules/marks_manager.py

from utils.validators import is_valid_marks


def enter_marks(student, subjects, max_marks):
    """Ask the user to enter marks for every subject for one student."""
    print(f"\nEntering marks for {student['name']} (Roll {student['roll']})")

    for subject in subjects:
        marks_text = input(f"  {subject} (out of {max_marks[subject]}): ")
        if is_valid_marks(marks_text, max_marks[subject]):
            student["marks"][subject] = int(marks_text)
        else:
            print(f"  Invalid marks for {subject}. Keeping previous value.")

    return student


def calculate_total(student):
    """Total marks scored across all subjects."""
    return sum(student["marks"].values())


def calculate_max_total(max_marks):
    """Maximum possible marks across all subjects."""
    return sum(max_marks.values())


def calculate_percentage(student, max_marks):
    """Percentage score, rounded to 2 decimal places."""
    total = calculate_total(student)
    max_total = calculate_max_total(max_marks)
    if max_total == 0:
        return 0.0
    return round((total / max_total) * 100, 2)


def calculate_grade(percentage):
    """Convert a percentage into a letter grade."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B+"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


def is_pass(student, max_marks, pass_percentage=40):
    """A student passes if their overall percentage is >= pass_percentage
    AND they score at least 33% in every individual subject."""
    if calculate_percentage(student, max_marks) < pass_percentage:
        return False

    for subject, marks in student["marks"].items():
        subject_percentage = (marks / max_marks[subject]) * 100
        if subject_percentage < 33:
            return False

    return True
