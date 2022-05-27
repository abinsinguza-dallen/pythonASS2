class Account:
    bank="PostBank"
    def __init__(self,account_number,account_name,balance):
        self.account_name=account_name
        self.account_number=account_number
        self.balance=balance
    def withdraw(self,amount):
        self.amount=amount  
        self.balance-=self.amount
        return self.balance  

    def deposit(self,amount):
        self.amount=amount
        self.balance+=self.amount
        return self.balance   