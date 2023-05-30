# from transformers import ChatGPT

class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited successfully to - {self.account_number}. Balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Amount withdrawn successfully from - {self.account_number}")
        else:
            print(f"Insufficient funds in Account: {self.account_number}")

    def get_balance(self):
        return self.balance

def ai_assistant():
    assistant = ChatGPT("gpt-3.5-turbo")

    print("Welcome to the AI Banking Assistant!")
    while True:
        user_input = input("How can I assist you today? (Type 'exit' to quit) ")

        if user_input.lower() == "exit":
            print("Thank you for using the AI Banking Assistant. Goodbye!")
            break

        response = assistant.generate(user_input)
        print(response.choices[0].text.strip())

num = int(input("Enter the number of accounts: "))
account_numbers = 1000
bank_accounts = []

for i in range(num):
    acc_num = account_numbers + (i + 1)
    account = BankAccount(acc_num)
    bank_accounts.append(account)

    print(f"Account created successfully: {acc_num}")
    print()
    opt = input("Enter choice (1-deposit, 2-withdraw, 3-check balance, 9-cancel, AI-assistant): ")

    if opt == "1":
        deposit_amount = float(input("Enter the amount to deposit: "))
        account.deposit(deposit_amount)
    elif opt == "2":
        withdrawal_amount = int(input("Enter the amount to withdraw: "))
        account.withdraw(withdrawal_amount)
    elif opt == "3":
        print(f"Your balance is: {account.get_balance()}")
    elif opt == "9":
        print("Transaction canceled")
    elif opt.lower() == "ai-assistant":
        ai_assistant()
    else:
        print("Invalid choice")
        break

    print(f"Account number: {account.account_number}, Current balance: {account.get_balance()}")
    print()

