class BankAccount:
    bank_name = "Akhi's Bank"

    # instance attributes
    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    # deposit amount into account
    def deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
            print(f"Deposit Successful. New Balance: ${self.current_balance:.2f}")
        else:
            print("Deposit Failed (must be greater than $0.00)")

    # withdraw amount from account
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal Failed (must be greater than $0.00)")
            return
        if self.current_balance - amount < self.minimum_balance:
            print(f"Withdraw Failed Account balance can not be less than ${self.minimum_balance}")
        else:
            self.current_balance -= amount
            print(f"Withdraw Successful. New Balance: ${self.current_balance:.2f}")

    # prints all customer info
    def print_customer_info (self):
        print ("Account Information:")
        print (f"Bank: {self.bank_name}")
        print (f"Current Balance: ${self.current_balance:.2f}")
        print (f"Minimum Balance: ${self.minimum_balance:.2f}")
