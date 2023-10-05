#Implement a class called BankAccount that represents a bank account. The class should have private attributes for account number, account holder name, and account balance. Include methods to deposit money, withdraw money, and display the account balance. Ensure that the account balance cannot be accessed directly from outside the class. Write a program to create an instance of the BankAccount class and test the deposit and withdrawal functionality.
class BankAccount:
    def _init_(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance_inr = initial_balance

    def deposit(self, amount_inr):
        if amount_inr > 0:
            self.__account_balance_inr += amount_inr
            return f"Deposited ₹{amount_inr}. New balance: ₹{self.__account_balance_inr}"
        else:
            return "Invalid deposit amount. Please deposit a positive amount."

    def withdraw(self, amount_inr):
        if 0 < amount_inr <= self.__account_balance_inr:
            self.__account_balance_inr -= amount_inr
            return f"Withdrew ₹{amount_inr}. New balance: ₹{self.__account_balance_inr}"
        elif amount_inr > self.__account_balance_inr:
            return f"Insufficient funds. available balance ₹{self.__account_balance_inr}."
        else:
            return "Invalid withdrawal amount."

    def display_balance(self):
        return f"Account Balance for {self._account_holder_name} (Acc num:{self.account_number}): ₹{self._account_balance_inr}"

# Creating an instance of BankAccount
account = BankAccount("123456", "Jhon", 1000)

# Testing deposit and withdrawal functionality
print(account.display_balance())      # Display initial balance
print(account.deposit(500))            # Deposit ₹500
print(account.withdraw(400))          # Withdraw ₹400
print(account.withdraw(2000))          #withdraw more than balance
print(account.display_balance())
   #display updated balance