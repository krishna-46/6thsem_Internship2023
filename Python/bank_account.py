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






class BankAccount :

    account_number=int()
    balance=float(0.0)


    def __init__(self,account_number):
        self.account_number=account_number
        self.balance=0.0
        

    def deposit(self,amount):
        self.balance +=amount
        print(f"Amount deposited successfully to - {self.account_number}")
        

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Amount withdraw successfully from -{self.account_number} ")
            
        else :
            print("Insaficient found")

    def get_balance(self):
        return self.balance
    

# BankAccount.deposit(10.0)

Ac1= BankAccount(123456789)
cr1=Ac1.deposit(int(input("Enter amount to deposit for Ac1 :")))
# cr1=Ac1.deposit(5000)
w1=Ac1.withdraw(float(input("Enter amount to withdraw for Ac1 :")))
# w1=Ac1.withdraw(1500)
b1=Ac1.get_balance()

Ac2= BankAccount(987654321)
cr2=Ac2.deposit(int(input("Enter amount to deposit for Ac2:")))
# cr2=Ac2.deposit(500)
w2=Ac2.withdraw(float(input("Enter amount to withdraw Ac2:")))
# w2=Ac2.withdraw(102)
b2=Ac2.get_balance()

print(f"Account No :-{Ac1.account_number} :" , f"   Debited :",w1 ,"Credited : ",cr1, "    Balance",b1)
# print(f"Account No :-{Ac1.account_number} :" , f"   Debited :{Ac1.deposit}",w1 ,"Credited : ",cr1, "    Balance",b1)
print(f"Account No :-{Ac2.account_number} :" , "   Debited :", w2, "Credited : ",cr2 ,"    Balance",b2)


# obj.deposit(input("Enter Amount :"))
# obj.withdraw(input("Enter Amount to withdraw :"))
# id(obj1)
# obj.deposit(100.2)

# obj2=account_number.get_balance()



    # def deposit(self,amount):
    #     self.amount=


