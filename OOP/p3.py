class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        # Encapsulated attribute (convention: leading underscore means "internal use")
        self._balance = float(initial_balance)
        self.account_holder = account_holder

    # Public method: user can deposit money
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self._balance += amount
        print(f"Deposited: {amount}. New balance: {self._balance}")

    # Public method: user can withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self._balance:
            print("Insufficient balance.")
            return
        self._balance -= amount
        print(f"Withdrew: {amount}. New balance: {self._balance}")

    # Public method: user can check balance
    def check_balance(self):
        return self._balance


# Example usage
account = BankAccount("Rahul", 1000)
account.deposit(500)
account.withdraw(300)
print("Final balance:", account.check_balance())
