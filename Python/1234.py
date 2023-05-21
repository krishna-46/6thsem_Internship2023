import numpy as np

class Account:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            print("Please enter a valid amount.")
        else:
            self.balance += amount
            print("Deposit successful.")
            print("Deposited amount:", amount)
            print("Updated balance:", self.balance)

    def withdraw(self, amount):
        if amount <= 0:
            print("Please enter a valid amount.")
        elif self.balance < amount:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print("Withdrawal successful.")
            print("Withdrawn amount:", amount)
            print("Updated balance:", self.balance)

    def get_balance(self):
        return self.balance

num = int(input("Enter the number of bank accounts to create: "))
print()
accounts = []

for _ in range(num):
    account_number = np.random.randint(100000000000, 999999999999)
    a = Account(account_number)
    accounts.append(a)
    print("Bank account created successfully.")
    print("Account number:", account_number)
    print()

for i, account in enumerate(accounts):
    print(f"Account {i+1}:")
    print("Account number:", account.account_number)
    print("Balance:", account.get_balance())
    print()
    while True:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        print()
        choice = int(input("Enter your choice (1-4): "))
        print()
        if choice == 1:
            deposit_amount = float(input("Enter the deposit amount: "))
            account.deposit(deposit_amount)
        elif choice == 2:
            withdrawal_amount = float(input("Enter the withdrawal amount: "))
            account.withdraw(withdrawal_amount)
        elif choice == 3:
            print("Current balance:", account.get_balance())
        elif choice == 4:
            print("Exit")
            break
        else:
            print("Invalid choice. Please try again.")

    print()
