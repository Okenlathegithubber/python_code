courses = {
    "MTH-101" : int(input("Enter the score for MTH-101 >> ")),
    "CSC-101" : int(input("Enter the score for CSC-101 >> ")),
    "CHM-101" : int(input("Enter the score for CHM-101 >> ")),
    "PHY-101" : int(input("Enter the score for PHY-101 >> ")),
    "PHY-103" : int(input("Enter the score for PHY-103 >> ")),
    "STA-105" : int(input("Enter the score for STA-105 >> ")),
    "GST-103" : int(input("Enter the score for GST-103 >> ")),
    "GST-105" : int(input("Enter the score for GST-105 >> "))
}    

total_credit_unit = 28
courses_cu = {
    "MTH-101" : 3.5,
    "CSC-101" : 3.5,
    "CHM-101" : 3.5,
    "PHY-101" : 3.5,
    "PHY-103" : 3.5,
    "STA-105" : 3.5,
    "GST-103" : 3.5,
    "GST-105" : 3.5
}

letter_grade_range = {
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

def letter_grade_to_score(score):
    if score >= 75:
        return "A"
    elif score >= 70:
        return "AB"
    elif score >= 65:
        return "B"
    elif score >= 60:
        return "BC"
    elif score >= 55:
        return "C"
    elif score >= 50:
        return "CD"
    elif score >= 45:
        return "D"
    elif score >= 40:
        return "E"
    else:
        return "F"

def get_letter_grade_to_gp(grade):
    if grade == "A":
        return 4.00
    elif grade == "AB":
        return 3.50
    elif grade == "B":
        return 3.25
    elif grade == "BC":
        return 3.00
    elif grade == "C":
        return 2.75
    elif grade == "CD":
        return 2.50
    elif grade == "D":
        return 2.25
    elif grade == "E":
        return 2.00
    elif grade == "F":
        return "0.00"

table = []
total_unit = 0
course_num = 8
for course, score in courses.items():
    letter_grade = letter_grade_to_score(score)
    weight_point = get_letter_grade_to_gp(letter_grade)
    unit = float(weight_point) * float(total_credit_unit / course_num)
    total_unit += unit
    gpa = round(total_unit / total_credit_unit, 2)
    # print(f"{course}: {score} ({letter_grade}) {weight_point}")
    table.append((course, score, letter_grade, round(unit, 2)))

print("{:<15}{:<15}{:<15}{:<15}".format("Subject", "Score", "Letter Grade", "Unit"))
for row in table:
    print("{:<15}{:<15}{:<15}{:<15}".format(row[0], row[1], row[2], row[3]))
    
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

print(f"\nGrade Point Average: {gpa}")
print(f"Range: {range}")
