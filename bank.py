class Account:
    def __init__(self,name,accnumber,phone,loan_limit):
        self.name = name
        self.accnumber = accnumber
        self.phone = phone
        self.balance = 0
        self.loan = 0
        self.loan_limit = loan_limit
    def info (self):
        return f"Hello {self.name}, your account number is {self.accnumber}"
    def send_money (self):
        return f"Greetings {self.name}. The transaction from account number {self.accnumber} was successful"
    def deposit (self, amount):
        if amount <= 0:
            return f" The amount must be greater than zero"
        else:
            self.balance += amount
            return f"Dear {self.name} you have deposited {amount}. Your new balance is {self.balance}"
    def show_balance(self):
        return self.balance
    def withdraw (self, amount):
        if amount <= 0:
            return f"Transaction not successful"

        elif amount > self.balance:
            return f"Transaction not successful"
        else:
            self.balance -= amount
            return f"Dear {self.name} you have withdrawn {amount}. Your new balance is {self.balance}"
    def borrow (self,amount):
        if self.loan > 0:
            return f"Transaction unsuccessful. You have an existing loan."
        else:
            amount <= self.loan_limit
            self.balance += amount
            self.loan += amount
            return f"Hurray! Transaction successful. Your new balance is {self.balance}. Your loan balance is {self.loan} "
