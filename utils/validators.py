# utils/validators.py


def is_valid_roll(roll_text):
    """Roll number must be a whole number of digits."""
    return roll_text.isdigit()


def is_valid_name(name_text):
    """Name must not be empty and should only contain letters/spaces."""
    if name_text.strip() == "":
        return False
    return all(char.isalpha() or char == " " for char in name_text)


def is_valid_marks(marks_text, max_mark):
    """Marks must be a whole number between 0 and the subject's max marks."""
    if not marks_text.isdigit():
        return False
    marks = int(marks_text)
    return 0 <= marks <= max_mark


def roll_exists(roll, students):
    """Check whether a roll number is already used."""
    for student in students:
        if student["roll"] == roll:
            return True
    return False
