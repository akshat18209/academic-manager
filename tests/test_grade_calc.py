# tests/test_grade_calc.py

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.marks_manager import calculate_grade, calculate_percentage, is_pass


def test_calculate_grade():
    assert calculate_grade(95) == "A+"
    assert calculate_grade(85) == "A"
    assert calculate_grade(75) == "B+"
    assert calculate_grade(65) == "B"
    assert calculate_grade(55) == "C"
    assert calculate_grade(45) == "D"
    assert calculate_grade(20) == "F"
    print("test_calculate_grade passed")


def test_calculate_percentage():
    max_marks = {"Maths": 100, "Science": 100}
    student = {"roll": 1, "name": "Test Student", "marks": {"Maths": 50, "Science": 50}}
    assert calculate_percentage(student, max_marks) == 50.0
    print("test_calculate_percentage passed")


def test_is_pass():
    max_marks = {"Maths": 100, "Science": 100}
    passing_student = {"roll": 1, "name": "Pass Student", "marks": {"Maths": 60, "Science": 60}}
    failing_student = {"roll": 2, "name": "Fail Student", "marks": {"Maths": 10, "Science": 10}}

    assert is_pass(passing_student, max_marks) == True
    assert is_pass(failing_student, max_marks) == False
    print("test_is_pass passed")


if __name__ == "__main__":
    test_calculate_grade()
    test_calculate_percentage()
    test_is_pass()
    print("\nAll tests passed!")
