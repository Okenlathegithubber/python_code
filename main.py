# PROJECT I
MTH = int(input("Insert your MTH-101 score >> "))
CSC = int(input("Insert your CSC-101 score >> "))
CHM = int(input("Insert your CHM-101 score >> "))
PHY = int(input("Insert your PHY-101 score >> "))
PHY_2 = int(input("Insert your PHY-103 score >> "))
STA = int(input("Insert your STA-101 score >> "))
GST = int(input("Insert your GST-103 score >> "))
GST_2 = int(input("Insert your GST-105 score >> "))
subjects = [MTH, CSC, CHM, PHY, PHY_2, STA, GST, GST_2]
total = sum(subjects)
average = total / len(subjects)

percentage = average * 100
print(f"Your G.P.A is {percentage}")