from savingsaccount import SavingsAccount
from checkingaccount import CheckingAccount

# saving account instances
sa1 = SavingsAccount("LeBron James", 1000.00, 230.00, 0.04)
sa2 = SavingsAccount("Stephen Curry", 3000.00, 400.00, 0.03)

sa1.print_customer_info()
sa1.deposit(100.00)
sa1.withdraw(300.00)
sa1.withdraw(1230.00)  # Should fail
sa1.apply_interest()
sa1.print_customer_info()

sa2.print_customer_info()
sa2.deposit(150.00)
sa2.withdraw(600.00)
sa2.withdraw(50.00)
sa2.apply_interest()
sa2.print_customer_info()

# checking Account instances
ca1 = CheckingAccount("Kevin Durant", 2000.00, 200.00, 2)
ca2 = CheckingAccount("Michael Jordan", 2500.00, 300.00, 1)

ca1.print_customer_info()
ca1.transfer(500.00)
ca1.transfer(300.00)
ca1.transfer(100.00)  # Should fail due to transfer limit
ca1.print_customer_info()

ca2.print_customer_info()
ca2.transfer(800.00)
ca2.transfer(100.00)  # Should fail due to transfer limit
ca2.print_customer_info()