class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional initial balance."""
        self.__account_balance = initial_balance  # Encapsulation: private attribute

    def deposit(self, amount):
        """Deposit a positive amount into the account."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw a positive amount if funds are sufficient."""
        if amount > self.__account_balance:
            return False
        elif amount > 0:
            self.__account_balance -= amount
            return True
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.__account_balance}")
