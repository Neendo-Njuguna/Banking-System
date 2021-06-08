from datetime import datetime
class Account:
    def __init__(self,name,accnumber,phone,loan_limit,loan):
        self.name = name
        self.accnumber = accnumber
        self.phone = phone
        self.balance = 0
        self.loan = loan
        self.loan_limit = loan_limit
        self.transaction = []
    def info (self):
        return f"Hello {self.name}, your account number is {self.accnumber}"
    def send_money (self):
        return f"Greetings {self.name}. The transaction from account number {self.accnumber} was successful"
    def deposit (self, amount):
        if amount <= 0:
            return f" The amount must be greater than zero"
        else:
            self.balance += amount
            transaction = {"amount":amount,"balance":self.balance, "time":datetime.now(),"narration":"Deposit"}
            self.transaction.append(transaction)
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
            transaction = {"amount":amount,"balance":self.balance, "time":datetime.now(),"narration":"Withdraw"}
            self.transaction.append(transaction)
            return f"Dear {self.name} you have withdrawn {amount}. Your new balance is {self.balance}"
    def borrow (self,amount):
        if self.loan > 0:
            return f"Transaction unsuccessful. You have an existing loan."
        else:
            amount <= self.loan_limit
            self.balance += amount
            self.loan += amount
            transaction = {"amount":amount,"balance":self.balance, "time":datetime.now(),"narration":"Loan"}
            self.transaction.append(transaction)
            return f"Hurray! Transaction successful. Your new balance is {self.balance}. Your loan balance is {self.loan} "
    def get_statement(self):
        for transaction in self.transaction:
            narration = transaction["narration"]
            amount = transaction["amount"]
            balance = transaction["balance"]
            time = transaction["time"]
            print (f"{time.strftime('%D')}{narration}You have deposited{amount} and your account balance is {balance}")
    def repay_loan(self,amount):
        if amount < 0 :
            return "Transaction Failed"
        elif amount <= self.loan:
             self.loan -= amount
             return f" Thank you for paying your loan. Your loan balance is {self.loan}"
        else:
            over_payment = amount = self.loan
            self.balance += amount
            transaction = {"amount":amount,"balance":self.balance, "time":datetime.now(),"narration":"PayLoan"}
            self.transaction.append(transaction)
            return f"Hurray! Your loan is fully paid. Your new account balance is {self.balance}"