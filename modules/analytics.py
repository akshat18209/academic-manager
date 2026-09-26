# modules/analytics.py

from modules.marks_manager import calculate_percentage, is_pass


def class_average_percentage(students, max_marks):
    """Average percentage across every student in the class."""
    if len(students) == 0:
        return 0.0

    total_percentage = 0
    for student in students:
        total_percentage = total_percentage + calculate_percentage(student, max_marks)

    return round(total_percentage / len(students), 2)


def find_topper(students, max_marks):
    """Return the student with the highest percentage."""
    if len(students) == 0:
        return None

    topper = students[0]
    for student in students:
        if calculate_percentage(student, max_marks) > calculate_percentage(topper, max_marks):
            topper = student

    return topper


def pass_percentage(students, max_marks):
    """Percentage of the class that passed."""
    if len(students) == 0:
        return 0.0

    pass_count = 0
    for student in students:
        if is_pass(student, max_marks):
            pass_count = pass_count + 1

    return round((pass_count / len(students)) * 100, 2)


def subject_wise_average(students, subjects):
    """Average marks scored in each subject across the whole class."""
    averages = {}

    for subject in subjects:
        if len(students) == 0:
            averages[subject] = 0.0
            continue

        total = 0
        for student in students:
            total = total + student["marks"][subject]

        averages[subject] = round(total / len(students), 2)

    return averages


def print_class_report(students, subjects, max_marks):
    """Print a full class-wide analytics report."""
    print("\n" + "=" * 40)
    print("           CLASS ANALYTICS REPORT")
    print("=" * 40)
    print(f"Total Students   : {len(students)}")
    print(f"Class Average    : {class_average_percentage(students, max_marks)}%")
    print(f"Pass Percentage  : {pass_percentage(students, max_marks)}%")

    topper = find_topper(students, max_marks)
    if topper is not None:
        topper_percentage = calculate_percentage(topper, max_marks)
        print(f"Topper           : {topper['name']} (Roll {topper['roll']}) - {topper_percentage}%")

    print("-" * 40)
    print("Subject-wise Class Average:")
    averages = subject_wise_average(students, subjects)
    for subject, avg in averages.items():
        print(f"  {subject:<20}: {avg}")
    print("=" * 40)
