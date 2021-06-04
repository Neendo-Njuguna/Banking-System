class Account:
    def __init__(self,name,accnumber,phone):
        self.name = name
        self.accnumber = accnumber
        self.phone = phone
        self.balance = 0
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
            return f"Dear {self.name} you have withdrawn {amount}. Your new balance is {self.balance} "
