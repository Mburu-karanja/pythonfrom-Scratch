#banking application 
from datetime import datetime

class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
      
    def deposit(self, amount):
        self.balance += amount
        return amount
    
    def withdraw(self, amount):
        if self.balance < amount:
            return "Insufficient balance."
        else:
            self.balance -= amount
            return amount
    
    def check_balance(self):
        print("Current balance:", self.balance)
    
    def customer_details(self):
        print("Customer Name:", self.customer_name)
        print("Account Number:", self.account_number)
        print("Date of Account Opening:", self.date_of_opening)
        print("Balance:", self.balance)

# Create an instance of BankAccount
account = BankAccount("123456789", 1000, datetime.now(), "John Doe")

# Deposit an amount
deposit_amount = account.deposit(500)
print("Deposited amount:", deposit_amount)

# Withdraw an amount
withdraw_amount = account.withdraw(200)
print("Withdrawn amount:", withdraw_amount)

# Check the current balance
account.check_balance()

# Print customer details
account.customer_details()
