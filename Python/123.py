import numpy as np
class account:
    def __init__(self,account_number):
        self.account_number=account_number
        print(account_number)
        self.balance=0
        
    def deposite(self,amount):

        if (amount<=0):
            print("Please Enter Valid Amount")
            print()
        else:
            if(self.balance>=0):
                self.balance=self.balance+amount
                print("deposite sucessfully")
                print("deposite amount is",amount)
                print("updated balance amount is",self.balance)
                print()
    def withdraw(self,amount):
        if(amount<=0):
            print("Please Enter Valid Amount")
            print()
        else:
            if(self.balance<amount):
                print("Your amount is More then balance amount")
            else:
                self.balance=self.balance-amount
                print("withdraw sucessfully!!!!")
                print("withdraw amount is",amount)
                print("updated balance amount is",self.balance)
                print()
    def get_balance(self):
        return self.balance

num=int(input("Enter Number of bank accounts to create:=="))
print()
l=[]
for i in range(num):
    a=account(np.random.randint(8,size=12))
    l.append(a)
    print("this is your account:=")
    print()
    
    
for i in l:
    ans=int(input("select bank account:="))
    if ans < 1 or ans > num:
        print("Invalid account number.")
        break
    else:
        if ans >= 1 and ans <= num:
            account = l[ans - 1]
        
    print()
    print("Your banck account Number:==",account.account_number)
    print("your balance is:=",account.get_balance())
    while True:
        print()
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        print()
        choice = int(input("Enter your choice (1-4):== "))
        print()
        if choice == 1:
            deop=int(input("Enter your deposite amount:"))
            account.deposite(deop)
    
        elif choice == 2:
            withd=int(input("Enter your Withdraw amount:"))
            account.withdraw(withd)
        
        elif choice == 3:

            print("updated balance is",account.get_balance)
        
        elif choice == 4:
            print("Exit")
            break
        else:
            print("Invalid choice. Please try again.")


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






class BankAccount :

    # account_number=int()
    # balance=float(0.0)

    def __init__(self,account_number):
        self.account_number =account_number
        self.balance=0.0


    def deposit(self,amount):
        self.balance +=amount

        if self.deposit:
            print(f"Amount deposited successfully to - {self.balance}")
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
