# Making a Dictionary of subjects and Credit unit.
subject_cu = {
    "MTH-101": 3.5,
    "CSC-101": 3.5,
    "CHM-101": 3.5,
    "PHY-101": 3.5,
    "PHY-103": 3.5,
    "STA-105": 3.5,
    "GST-103": 3.5,
    "GST-105": 3.5,
}

# Making a Dictionary to compare the letter grade and grade point.
letter_grade_to_grade_point = {
    "A": 4.00,
    "AB": 3.50,
    "B": 3.25,
    "BC": 3.00,
    "C": 2.75,
    "CD": 2.50,
    "D": 2.25,
    "E": 2.00,
    "F": 0.00
}

# Seperating the keys (courses) from the values(credit unit).
for course, credit_unit in subject_cu.items():
    score = int(input(f"Enter score of {course}: "))

    # determine the corresponding letter grade for the score
    if score >= 75:
        letter_grade = "A"
    elif score >= 70:
        letter_grade = "AB"
    elif score >= 65:
        letter_grade = "B"
    elif score >= 60:
        letter_grade = "BC"
    elif score >= 55:
        letter_grade = "C"
    elif score >= 50:
        letter_grade = "CD"
    elif score >= 45:
        letter_grade = "D"
    elif score >= 40:
        letter_grade = "E"
    else:
        letter_grade = "F"
    
    # To display the course, examination score, and letter_grade.    
    print(f"{course}: {score} {letter_grade}")
