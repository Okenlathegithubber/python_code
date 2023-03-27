from time import *

print("Welcome to ATM SERVICES")
print("-----------------------")
pin = int(input("Enter 4-digit PIN >> "))
account_details = {"pin_num": 1234}

if pin == account_details["pin_num"]:
    print("Access Granted")
    sleep(1)
    print("1. Savings \n2. Current")

    choice = int(input(""))

    if choice == 1:
        while True:
            print("\nChoose an option from the menu:")
            print("1. Check account balance")
            print("2. Transfer cash into account")
            print("3. Withdraw cash from account")
            print("4. Exit")

            option = input()

            if option == "1":
                print(f"Your account balance is N{account_details['balance']}.")
            elif option == "2":
                amount = int(input("Enter amount to transfer: "))

                if amount < 1:
                    print("Invalid amount.")
                else:
                    account_details["balance"] += amount
                    print(f"Transfer successful. Your new balance is N{account_details['balance']}.")
            elif option == "3":
                amount = int(input("Enter amount to withdraw: "))

                if amount < 1000 or amount % 1000 != 0 or amount % 1000 != 0 or amount % 2000 != 0 or amount % 5000 != 0 or amount % 10000 != 0:
                    print("Invalid amount. You can only withdraw in multiples of N1,000, N2,000, N5,000, N10,000.")
                elif amount > account_details["balance"]:
                    print("Insufficient funds.")
                else:
                    account_details["balance"] -= amount
                    print(f"Withdrawal successful. Your new balance is N{account_details['balance']}.")
            elif option == "4":
                break
            else:
                print("Invalid option. Please try again.")

    elif choice == 2:
        print("Sorry, Your account type is not currently supported. Please contact the bank manager for assistance.")
else:
    print("Access Denied")
