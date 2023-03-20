# PROJECT II
experience = int(input("What is your working experience? >> "))
age = int(input("How old are you? >> "))

if experience > 10 and age >= 35:
    print("Your Salary is 600,000 Naira")
elif experience > 5 and 28 <= age < 35:
    print("Your Salary is 480,000 Naira")
elif experience < 5 and age < 28:
    print("Your Salary is 250,000 Naira")