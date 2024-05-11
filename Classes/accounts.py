
class Account:
    def __init__(self, name, balance=0):
        self.__account_name = name 
        self.__account_balance = balance
        self.set_balance(self.__account_balance)

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > 0 and self.__account_balance >= amount:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        """Get the current balance of the account."""
        return self.__account_balance

    def get_name(self):
        """Get the name of the account."""
        return self.__account_name

    def set_balance(self, value):
        """Set the balance of the account."""
        if value > 0:
            self.__account_balance = value
        else:
            self.__account_balance = 0

    def __str__(self):
        """Return a string representation of the account."""
        return f'Account name = {self.get_name()}, Account balance = {self.get_balance():.2f}'
