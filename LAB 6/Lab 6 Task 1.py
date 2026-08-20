class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
            print("New balance:", self.balance)
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("New balance:", self.balance)

    def check_balance(self):
        print("Account Number:", self.account_number)
        print("Customer Name:", self.customer_name)
        print("Date of Opening:", self.date_of_opening)
        print("Current Balance:", self.balance)


# Creating an object
account1 = BankAccount(
    "ACC1001",
    5000,
    "20-08-2026",
    "Pranto"
)

# Checking account information
account1.check_balance()

# Deposit
account1.deposit(2000)

# Withdraw
account1.withdraw(1500)

# Final balance
account1.check_balance()