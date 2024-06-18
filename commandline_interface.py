from abc import ABC, abstractmethod
from account_management import AccountManagement
from account import CheckingAccount

class CommandLineInterface(ABC):
    @abstractmethod
    def display_menu(self):
        pass

    @abstractmethod
    def user_input(self):
        pass

    @abstractmethod
    def run(self):
        pass

class BankingSystemInterface(CommandLineInterface):
    def __init__(self, account_management):
        self.account_management = account_management

    def user_input(self, message):
        return input(message)

    def display_menu(self):
        menu = """
        Banking System Menu:
        1. Open Account
        2. Close Account
        3. Get Account Info
        4. Deposit
        5. Withdraw
        6. Transfer
        7. Exit
        """
        print(menu)

    def open_account(self):
        try:
            customer_name = self.user_input("Enter your name: ")
            passward = self.user_input("Enter your passward: ")
            initial_balance = int(self.user_input("Enter initial balance: "))
            if initial_balance >= 0:
                self.account_management.open_account(CheckingAccount, customer_name, passward, initial_balance)
            else:
                print("Invalid initial balance. Failed to open new account")
        except ValueError:
            print("Invalid amount.")

    def close_account(self):
            account_id = self.user_input("Enter account ID: ")
            self.account_management.close_account(account_id)

    def display_account_info(self):
            account_id = self.user_input("Enter account ID: ")
            self.account_management.get_account_info(account_id)

    def deposit(self):
        try:
            account_id = self.user_input("Enter account ID: ")
            amount = int(self.user_input("Enter amount to deposit: "))
            if amount >= 0:
                self.account_management.deposit(account_id, amount)
            else:
                print("Please input positive amount")
        except ValueError:
            print("Invalid amount.")

    def withdraw(self):
        try:
            account_id = self.user_input("Enter account ID: ")
            amount = int(self.user_input("Enter amount to withdraw: "))
            if amount >= 0:
                self.account_management.withdraw(account_id, amount)
            else:
                print("Please input positive amount")
        except ValueError:
            print("Invalid amount.")

    def transfer(self):
        try:
            from_account_id = self.user_input("Enter source account ID: ")
            to_account_id = self.user_input("Enter destination account ID: ")
            amount = int(self.user_input("Enter amount to transfer: "))
            if amount >= 0:
                self.account_management.transfer(from_account_id, to_account_id, amount)
            else:
                print("Please input positive amount")
        except ValueError:
            print("Invalid amount.")       

    def run(self):
        while True:
            self.display_menu()
            choice = self.user_input("Enter your command: ")
            if choice == '1':
                self.open_account()
            elif choice == '2':
                self.close_account()
            elif choice == '3':
                self.display_account_info()
            elif choice == '4':
                self.deposit()
            elif choice == '5':
                self.withdraw()
            elif choice == '6':
                self.transfer()
            elif choice == '7':
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    account_management = AccountManagement()
    interface = BankingSystemInterface(account_management)
    interface.run()