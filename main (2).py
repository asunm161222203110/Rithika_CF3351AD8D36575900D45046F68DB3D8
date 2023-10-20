class BankAccount:
    def __init__(self, account_number, account_holder_name):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = 0.0

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.__account_balance:.2f}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.__account_balance:.2f}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def display_balance(self):
        """Display the current account balance."""
        print(f"Account balance for {self.__account_holder_name}: ${self.__account_balance:.2f}")


# Example usage:
if __name__ == "__main__":
    my_account = BankAccount(account_number="123456", account_holder_name="John Doe")
    my_account.deposit(1000)
    my_account.withdraw(200)
    my_account.display_balance()
