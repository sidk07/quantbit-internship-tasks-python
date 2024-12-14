# Task 4 
# Design a BankAccount class with methods for deposit, withdrawal, and balance inquiry. 

class BankAccount :
    balance = 0

    def deposit(self, value) :
        self.balance += value
        print("Balace after deposit : ", self.balance)

    def withdraw(self, value) :
        self.balance -= value
        print("Balace after withdraw : ", self.balance)

    def get_balance(self):
        print("Balance : ", self.balance)

account = BankAccount() 
account.deposit(1000) 
account.withdraw(200) 
account.get_balance() 
