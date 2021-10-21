class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = 0.1
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        if self.balance < amount:
            print("Insufficient funds charge $5")
            self.balance -= amount+5
        return self
    
    def display_account_info(self):
        print(self.balance)
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance*self.int_rate
        return self

checking=BankAccount(0.1, 100)
savings=BankAccount(0.1, 500)

checking.deposit(100).deposit(100).deposit(100).withdraw(50).yield_interest().display_account_info()
savings.deposit(100).deposit(100).withdraw(25).withdraw(25).withdraw(25).withdraw(25).yield_interest().display_account_info()

