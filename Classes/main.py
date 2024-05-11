import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox
from savings_account import SavingAccount

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Banking Application")
        self.setGeometry(100, 100, 400, 300)  # window size

        layout = QVBoxLayout()

        # Account Name
        self.name_label = QLabel("Account Name:")
        self.name_input = QLineEdit()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)

        # Initialize Account
        self.init_account_button = QPushButton("Initialize Account")
        self.init_account_button.clicked.connect(self.init_account)
        layout.addWidget(self.init_account_button)

        # Amount
        self.amount_label = QLabel("Amount:")
        self.amount_input = QLineEdit()
        layout.addWidget(self.amount_label)
        layout.addWidget(self.amount_input)

        # Deposit button
        self.deposit_button = QPushButton("Deposit")
        self.deposit_button.clicked.connect(self.deposit)
        layout.addWidget(self.deposit_button)

        # Withdraw button
        self.withdraw_button = QPushButton("Withdraw")
        self.withdraw_button.clicked.connect(self.withdraw)
        layout.addWidget(self.withdraw_button)

        # Interest button
        self.apply_interest_button = QPushButton("Apply Interest")
        self.apply_interest_button.clicked.connect(self.apply_interest)
        layout.addWidget(self.apply_interest_button)

        # Show Balance
        self.show_balance_button = QPushButton("Show Balance")
        self.show_balance_button.clicked.connect(self.show_balance)
        layout.addWidget(self.show_balance_button)

        self.setLayout(layout)

        self.account = None  # Initialize account

    # Inits the account
    def init_account(self):
        name = self.name_input.text()  # Get account name
        self.account = SavingAccount(name)  # Create SavingAccount instance
        QMessageBox.information(self, "Success", "Account initialized successfully!")

    # Deposit amount
    def deposit(self):
        amount = float(self.amount_input.text())
        if self.account is not None and self.account.deposit(amount):
            QMessageBox.information(self, "Success", f"Deposited {amount} successfully!")
            self.show_balance()  # Show updated balance
        else:
            QMessageBox.warning(self, "Error", "Invalid amount or account not initialized!")

    # Withdraw amount from the account
    def withdraw(self):
        amount = float(self.amount_input.text())
        if self.account is not None and self.account.withdraw(amount):
            QMessageBox.information(self, "Success", f"Withdrew {amount} successfully!")
            self.show_balance()  # Show updated balance
        else:
            QMessageBox.warning(self, "Error", "Invalid amount or account not initialized!")

    # Applies interest to the account
    def apply_interest(self):
        if self.account is not None:  # Check if account is initialized
            self.account.apply_interest()  # Apply interest to the account
            self.show_balance()  # Show updated balance

    # Displays account balance
    def show_balance(self):
        if self.account is not None:  # Check if account is initialized
            balance_msg = f"Account Balance: {self.account.get_balance():.2f}"
            QMessageBox.information(self, "Account Balance", balance_msg)  #msg popup


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
