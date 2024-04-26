class BankAccount:
    def __init__(self, bankName, accountName, Age, accountNomine, initialBalance=0):
        self.bankName = bankName
        self.initialBalance = initialBalance
        self.accountName = accountName
        self.accountNomine = accountNomine

    def deposit(self, amount):
        amount = float(amount)
        if amount > 0:
            self.initialBalance += amount
            print(
                f"Congratulation! you deposited \"{amount}\". \n Your new balance: {self.initialBalance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        amount = float(amount)
        if 0 < amount <= self.initialBalance:
            self.initialBalance -= amount
            print(
                f"Congratulation! your withdrew amount is \"{amount}\". \n Your new balance: {self.initialBalance}")
        else:
            print("Opps! Insufficient funds")

    def checkBalance(self):
        print(f" Your current balance:{self.initialBalance}")

    def accountInfo(self):
        print(
            f"The owner of this account is  Dr \"{self.accountName}\". \n The nomine of this account is Dr \"{self.accountNomine}\". \n This account current balance:{self.initialBalance}")


if __name__ == '__main__':
    account = BankAccount('ABC', 'Sahabuddin', 18, 'sujon', 1000)

    # Perform transactions
    # account.deposit(500)
    # account.withdraw(200)
    # account.withdraw(2000)
    # account.check_balance()
    # account.accountInfo()
    while (True):
        print(
            f"Welcome to the \"{account.bankName}\" Bank. \n Please Enter your choice to continue")
        print("1 Deposit")
        print("2 Withdraw")
        print("3 Check Balance")
        print("4 Check account information")
        user_choice = input()
        if user_choice not in ['1', '2', '3', '4']:
            print("Please enter a valid choice number")
            continue
        else:
            user_choice = int(user_choice)

            if user_choice == 1:
                amount = input("Please enter your ammount: \n")
                account.deposit(amount)

            elif user_choice == 2:
                amount = input("Please enter your ammount: \n")
                account.withdraw(amount)

            elif user_choice == 3:
                account.checkBalance()

            elif user_choice == 4:
                account.accountInfo()

            else:
                print("Not a valid option")

            print("Press q to quit and c to continue")

            user_choice2 = ""

            while (user_choice2 != "c" and user_choice2 != "q"):
                user_choice2 = input()
                if user_choice2 == "q":
                    exit()

                elif user_choice2 == "c":
                    continue
