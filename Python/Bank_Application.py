# You are tasked with creating a simple banking application. Implement a Python class called BankAccount that represents a bank account. The BankAccount class should have the following attributes and methods:
# Attributes:
# account_number (integer): A unique identifier for the bank account.
# balance (float): The current balance in the account.
# Methods:
# _init_(self, account_number): Initializes a new bank account with the given account number and a balance of 0.
# deposit(self, amount): Deposits the specified amount into the account and updates the balance accordingly.
# withdraw(self, amount): Withdraws the specified amount from the account, if the account has sufficient funds, and updates the balance accordingly.
# get_balance(self): Returns the current balance in the account.
# Write the BankAccount class implementation and provide a sample code snippet that demonstrates the usage of the class by creating instances of BankAccount and performing various operations on them.

# Feel free to add any additional helper methods or attributes to enhance the functionality of the BankAccount class if you wish.
#.......................................................................................

class BankAccount :

    # account_number=int()
    # balance=float(0.0)

    def __init__(self,account_number):
        self.account_number =account_number
        self.balance=0.0
        

    def deposit(self,amount):
        self.balance +=amount

        if self.deposit:
            print(f"Amount deposited successfully to - {self.account_number}",f"balance : {self.balance}")
        else:
            print("You have canceld Thank You!")
        

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Amount withdraw successfully from -{self.account_number} ")
            
        else :
            print(f"Insaficient found in Account:  {self.account_number}")

    def get_balance(self):
        return self.balance

num = int(input("Enter account numbers: "))
account_numbers=1000

bankaccount = []

for i in range(num):
    num1=BankAccount(account_numbers)
    bankaccount.append(num1)
    print(f"Account created successfully:{account_numbers}")
    opt = input("Enter choice (1-deposit, 2-withdraw,3-check balance 9-cancel): ")
    
    if opt == "1":
            deposit_amount = float(input("Enter the amount to deposit: "))
            num1.deposit(deposit_amount)
    elif opt == "2":
            withdrawal_amount = int(input("Enter the amount to withdraw: "))
            num1.withdraw(withdrawal_amount)

    elif opt == "3":
            print(f"Your balance is : {num1.get_balance()}")
    elif opt == "9":
            print("Transaction canceled")
        
    else:
            print("Invalid choice")
            break

    print(f"Account number:{num1.account_number} ",f"Current balance:{num1.get_balance()}")

#...........................................................................................................
       
# bankaccount=[]

# account_numbers=int(input("Enter account number:"))
# # account_number =1000

# account=BankAccount(account_numbers)
# print(f"Account created successfully: {account_numbers}")
# bankaccount.append(account_numbers)

# for i in range(account_numbers):
#     print(f"Account as created successfully: {account_numbers}")
#     bankaccount.append(account_numbers)

# opt =input( "Enter choice (1-deposit,2-withdrow,9-cancal)" )
# if opt == "1":
#     deposit_amount = float(input("Enter the amount to deposit: "))
#     account.deposit(deposit_amount)
# elif opt == "2":
#     withdrawal_amount = float(input("Enter the amount to withdraw: "))
#     account.withdraw(withdrawal_amount)

# elif opt == "9":
#     print("Transaction cancelled")
# else:
#     print("Invalid choice")

# print(f"Account number :{account_numbers}",f"Diposit : {account.deposit}")
# print("Current balance:", account.get_balance())
# print("Bank account numbers:", bankaccount)
######################################################################################

#.......................................................................................
# class BankAccount: 
#     account_numbers=1000
#     def __init__(self, account_number):
#         self.account_number = account_number
#         self.balance = 0.0

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Amount deposited successfully to Account {self.account_numbers}. Current balance: {self.balance}")

#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             print(f"Amount {amount} withdrawn successfully from Account {self.account_number}")
#         else:
#             print(f"Insufficient funds in Account {self.account_number}")

#     def get_balance(self):
#         return self.balance

# bankaccount=[]

# account_numbers=int(input("Enter account number:"))
# # account_number =1000

# account=BankAccount(account_numbers)
# print(f"Account created successfully: {account_numbers}")
# bankaccount.append(account_numbers)

# for i in range(account_numbers):
#     print(f"Account as created successfully: {account_numbers}")
#     bankaccount.append(account_numbers)

# opt =input( "Enter choice (1-deposit,2-withdrow,9-cancal)" )
# if opt == "1":
#     deposit_amount = float(input("Enter the amount to deposit: "))
#     account.deposit(deposit_amount)
# elif opt == "2":
#     withdrawal_amount = float(input("Enter the amount to withdraw: "))
#     account.withdraw(withdrawal_amount)

# elif opt == "9":
#     print("Transaction cancelled")
# else:
#     print("Invalid choice")

# print(f"Account number :{account_numbers}",f"Diposit : {account.deposit}")
# print("Current balance:", account.get_balance())
# print("Bank account numbers:", bankaccount)

#..............................................................................

        
    

    
   







    


    

# BankAccount.deposit(10.0)

# Ac1= BankAccount(123456789)

# cr1=Ac1.deposit(int(input("Enter amount to deposit for Ac1 :")))
# cr1=Ac1.deposit(5000)
# w1=Ac1.withdraw(float(input("Enter amount to withdraw for Ac1 :")))
# w1=Ac1.withdraw(1500)
# b1=Ac1.get_balance()

# Ac2= BankAccount(987654321)
# cr2=Ac2.deposit(int(input("Enter amount to deposit for Ac2:")))
# cr2=Ac2.deposit(500)
# w2=Ac2.withdraw(float(input("Enter amount to withdraw Ac2:")))
# w2=Ac2.withdraw(102)
# b2=Ac2.get_balance()


# print(f"Account No :-{Ac1.account_number} :" , f"   Debited :",w1 ,"Credited : ",cr1, "    Balance",b1)
# print(f"Account No :-{Ac1.account_number} :" , f"   Debited :{Ac1.deposit}",w1 ,"Credited : ",cr1, "    Balance",b1)
# print(f"Account No :-{Ac2.account_number} :" , "   Debited :", w2, "Credited : ",cr2 ,"    Balance",b2)


# obj.deposit(input("Enter Amount :"))
# obj.withdraw(input("Enter Amount to withdraw :"))
# id(obj1)
# obj.deposit(100.2)

# obj2=account_number.get_balance()



    # def deposit(self,amount):
    #     self.amount=
    







# class BankAccount:
#     def __init__(self, account_number):
#         self.account_number = account_number
#         self.balance = 0.0

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Amount deposited successfully to Account {self.account_number}. Current balance: {self.balance}")

#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             print(f"Amount {amount} withdrawn successfully from Account {self.account_number}")
#         else:
#             print(f"Insufficient funds in Account {self.account_number}")

#     def get_balance(self):
#         return self.balance


# num = int(input("Enter account numbers: "))
# account_numbers=1000

# bankaccount = []

# for i in range(num):
#     num1=BankAccount(account_numbers)
#     bankaccount.append(num1)
#     print(f"Account created successfully:{num1.account_number}")

# for i, num2 in enumerate(bankaccount):
#     print("Account number:", num2.account_number)
#     print("Current balance:", num2.get_balance())
#     print()

# while True:
#     print("Select an account:")
#     for i, num1 in enumerate(bankaccount, 1):
#         print(f"{i}. Account {i}")
#     print("0. Exit")
#     print()

#     opt = input("Enter choice (1-deposit, 2-withdraw,3-check balance 9-cancel): ".format(num))
    
#     if opt == "1":
#         deposit_amount = float(input("Enter the amount to deposit: "))
#         num2.deposit(deposit_amount)
#     elif opt == "2":
#         withdrawal_amount = int(input("Enter the amount to withdraw: "))
#         BankAccount.withdraw(withdrawal_amount)

#     elif opt == "3":
#         print(f"Your balance is : {BankAccount.get_balance()}")
#     elif opt == "9":
#         print("Transaction canceled")
        
#     else:
#         print("Invalid choice")
#     break
# print(f"Account number:{BankAccount.account_numbers} .Current balance:{num1.get_balance}")

