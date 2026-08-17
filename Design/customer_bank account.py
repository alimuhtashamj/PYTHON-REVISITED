class Customer:
    def __init__( self, account):
        self.account = account 
class Account:
    def __init__(self, balance):
       self.balance = balance 
       
    def withdraw(self, withdrawing_amount):
        if withdrawing_amount > self.balance:
            return ' Insufficient Balance'
        else:
            self.balance = self.balance - withdrawing_amount
            return self.balance
    
    def deposit(self, deposit_amount):
        self.balance = self.balance + deposit_amount
        return self.balance
    
account = Account(300000)    
customer = Customer(account)
print(customer.account.withdraw(100))
    