from accounts import Account


class SavingAccount(Account):
    MINIMUM = 100
    RATE = 0.02

    def __init__(self, name):
        super().__init__(name, SavingAccount.MINIMUM)
        self.__deposit_count = 0

    def apply_interest(self):
        """Apply interest to the account balance."""
        interest_amount = self.get_balance() * SavingAccount.RATE
        self.set_balance(self.get_balance() + interest_amount)

    def deposit(self, amount):
        """Deposit money into the saving account."""
        if amount > 0:
            self.set_balance(self.get_balance() + amount)
            self.__deposit_count += 1
            return True
        else:
            return False

    def withdraw(self, amount):
        """Withdraw money from the saving account."""
        x = self.get_balance() - amount
        if 0 < amount <= self.get_balance():
            self.set_balance(x)
            return True
        else:
            return False

    def set_balance(self, value):
        """Set the balance of the saving account."""
        if value < SavingAccount.MINIMUM:
            super().set_balance(SavingAccount.MINIMUM)
        else:
            super().set_balance(value)

    def __str__(self):
        """Return a string representation of the saving account."""
        return f'SAVING ACCOUNT: {super().__str__()}'
