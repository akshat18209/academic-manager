# modules/report_generator.py

from modules.marks_manager import (
    calculate_total,
    calculate_max_total,
    calculate_percentage,
    calculate_grade,
    is_pass,
)


def build_report_text(student, max_marks):
    """Build the report card as one big string (used for both printing
    to the screen and saving to a file)."""
    total = calculate_total(student)
    max_total = calculate_max_total(max_marks)
    percentage = calculate_percentage(student, max_marks)
    grade = calculate_grade(percentage)
    result = "PASS" if is_pass(student, max_marks) else "FAIL"

    lines = []
    lines.append("=" * 40)
    lines.append("           STUDENT REPORT CARD")
    lines.append("=" * 40)
    lines.append(f"Roll Number : {student['roll']}")
    lines.append(f"Name        : {student['name']}")
    lines.append("-" * 40)
    lines.append(f"{'Subject':<20}{'Marks':<10}{'Max':<10}")
    for subject, marks in student["marks"].items():
        lines.append(f"{subject:<20}{marks:<10}{max_marks[subject]:<10}")
    lines.append("-" * 40)
    lines.append(f"Total       : {total} / {max_total}")
    lines.append(f"Percentage  : {percentage}%")
    lines.append(f"Grade       : {grade}")
    lines.append(f"Result      : {result}")
    lines.append("=" * 40)

    return "\n".join(lines)


def generate_report_card(student, max_marks):
    """Print the report card to the screen and save it to a .txt file
    inside the reports/ folder."""
    report_text = build_report_text(student, max_marks)
    print("\n" + report_text)

    file_name = f"reports/report_{student['roll']}.txt"
    file = open(file_name, "w")
    file.write(report_text)
    file.close()

    print(f"\nReport card saved to {file_name}")
