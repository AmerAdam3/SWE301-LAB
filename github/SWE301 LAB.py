class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self.balance

    def display_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.holder_name}")
        print(f"Current Balance: ${self.balance}")


def main():
    # Create a sample bank account
    account = BankAccount("1234567890", "John Doe", 1000)

    while True:
        print("\nBank System Menu:")
        print("1. Display Account Information")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            account.display_info()
        elif choice == '2':
            amount = float(input("Enter deposit amount: $"))
            account.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter withdrawal amount: $"))
            account.withdraw(amount)
        elif choice == '4':
            print(f"Current Balance: ${account.get_balance()}")
        elif choice == '5':
            print("Thank you for using our bank system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
