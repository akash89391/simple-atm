account = {}

class Bank:
    def __init__(self):
        self.name = ""
        self.show()

    def create_acc(self):
        print("\n**CREATE ACCOUNT**")
        self.name = input("1. Create User Name: ")
        pin = input("2. Create PIN (numbers): ")
        if len(pin) != 4:
            print("\n**Pin must have only 4 characters**")
            self.create_acc()
            return
        if self.name in account:
            print("\nUser already exists.")
            return
            
        account[self.name] = {"pin": pin, "balance": 0}
        print("\nAccount Created Successfully")
        self.bank()

    def login(self):
        print("\n**LOGIN**")
        self.name = input("1. Enter User Name: ")
        pin = input("2. Enter PIN: ")
        if self.name in account and account[self.name]["pin"] == pin:
            print("Successfully Logged In")
            self.bank()
        else:
            print("\nInvalid username or PIN")
            self.show()

    def bank(self):
        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Log Out")
            option = int(input("Enter the option: "))
            if option == 1:
                amount = int(input("Enter the amount: "))
                if amount > 0:
                    account[self.name]["balance"] += amount
                    print(f"Successfully deposited Rs.{amount}. New balance is Rs.{account[self.name]['balance']}")
                else:
                    print("Invalid amount")
            elif option == 2:
                amount = int(input("Enter the amount: "))
                if amount > 0 and account[self.name]["balance"] >= amount:
                    account[self.name]["balance"] -= amount
                    print(f"Successfully withdrew Rs.{amount}. New balance is Rs.{account[self.name]['balance']}")
                else:
                    print("Insufficient funds or invalid amount")
            elif option == 3:
                print(f"Your current balance is Rs.{account[self.name]['balance']}")
            elif option == 4:
                print("Logged out successfully")
                self.show()
                break
            else:
                print("Invalid option")

    def show(self):
        print("\n**WELCOME**")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        option = int(input("Enter the option: "))
        if option == 1:
            self.create_acc()
        elif option == 2:
            self.login()
        elif option == 3:
            print("Thank you for using the ATM")
        else:
            print("Invalid option")
            self.show()

Bank()
