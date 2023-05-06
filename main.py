total_credit_unit = 28

#  course titles and credit unit
subject_cu = {
    "MTH-101": 3.5,
    "CSC-101": 3.5,
    "CHM-101": 3.5,
    "PHY-101": 3.5,
    "PHY-103": 3.5,
    "STA-105": 3.5,
    "GST-103": 3.5,
    "GST-105": 3.5
}


# course titles and corresponding scores
courses = {
    "MTH-101": int(input("Insert MTH-101 score >> ")),
    "CSC-101": int(input("Insert CSC-101 score >> ")),
    "CHM-101": int(input("Insert CHM-101 score >> ")),
    "PHY-101": int(input("Insert PHY-101 score >> ")),
    "PHY-103": int(input("Insert PHY-103 score >> ")),
    "STA-105": int(input("Insert STA-105 score >> ")),
    "GST-103": int(input("Insert GST-103 score >> ")),
    "GST-105": int(input("Insert GST-105 score >> "))
}

# dictionary of letter grades and their corresponding weight points
grades = {
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

# create a table to store subject, score, letter grade and unit of each course
table = []
total_unit = 0

# loop through the courses and calculate the unit of each subject/course
for course, score in courses.items():
    if score >= 75:
        grade = "A"
    elif score >= 70:
        grade = "AB"
    elif score >= 65:
        grade = "B"
    elif score >= 60:
        grade = "BC"
    elif score >= 55:
        grade = "C"
    elif score >= 50:
        grade = "CD"
    elif score >= 45:
        grade = "D"
    elif score >= 40:
        grade = "E"
    else:
        grade = "F"
    weight_point = grades[grade]
    unit = weight_point * total_credit_unit / len(courses)
    total_unit += unit
    table.append((course, score, grade, round(unit, 2)))

    # calculate the grade point average and round to 2 decimal places
    gpa = total_unit / total_credit_unit
    gpa = round(gpa, 2)

    # print the course table
    print("{:<15}{:<15}{:<15}{:<15}".format("Subject", "Score", "Letter Grade", "Unit"))
    for row in table:
        print("{:<15}{:<15}{:<15}{:<15}".format(row[0], row[1], row[2], row[3]))

    # determine the range of the grade point average
    if gpa >= 3.50:
        range = "Distinction"
    elif gpa >= 3.00:
        range = "Upper Credit"
    elif gpa >= 2.50:
        range = "Lower Credit"
    elif gpa >= 2.00:
        range = "Pass"
    else:
        range = "Fail"

    # print the grade point average and the range
    print("\nGrade Point Average: {}".format(gpa))
    print("Range: {}".format(range))

