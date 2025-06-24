from bankaccount import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance)
        self._transfer_limit = transfer_limit
        self.__account_number = "ca-0001"
        self.__routing_number = "rt-1002"
        self._transfers_made = 0

    def transfer(self, amount):
        if self._transfers_made >= self._transfer_limit:
            print("Transfer Failed: Transfer limit reached.")
        elif amount > 0 and (self.current_balance - amount) >= self.minimum_balance:
            self.current_balance -= amount
            self._transfers_made += 1
            print(f"Transfer Successful. Amount: ${amount:.2f}. New Balance: ${self.current_balance:.2f}")
        else:
            print("Transfer Failed: Invalid amount or insufficient balance.")