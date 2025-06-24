from bankaccount import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, interest_rate):
        super().__init__(customer_name, current_balance, minimum_balance)
        self._interest_rate = interest_rate
        self.__account_number = "sa-0001"
        self.__routing_number = "rt-1001"

    def apply_interest(self):
        interest = self.current_balance * self._interest_rate
        self.current_balance += interest
        print(f"Interest Applied: ${interest:.2f}. New Balance: ${self.current_balance:.2f}")