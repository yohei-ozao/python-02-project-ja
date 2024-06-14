from abc import ABC, abstractmethod
from account_management import AccountManagement
from account import CheckingAccount

class CommandLineInterface(ABC):
    @abstractmethod
    def display_menu(self):
        pass

    @abstractmethod
    def run(self):
        pass

class BankingSystemInterface(CommandLineInterface):
    def __init__(self, account_management):
        self.account_management = account_management

    def get_amount(self, message):
        user_input = input(message)
        try:
            if int(user_input) < 0:
                print("Input positive value")
            else:
                return int(user_input)
        except ValueError:
            print("Input the number isn't appropriate\n") 

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

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your command: ")
            if choice == '1':
                customer_name = input("Enter your name: ")
                passward = input("Enter your passward: ")
                initial_balance = self.get_amount("Enter initial balance: ")
                self.account_management.open_account(CheckingAccount, customer_name, passward, initial_balance)
            elif choice == '2':
                account_id = input("Enter account ID: ")
                self.account_management.close_account(account_id)
            elif choice == '3':
                account_id = input("Enter account ID: ")
                self.account_management.get_account_info(account_id)
            elif choice == '4':
                account_id = input("Enter account ID: ")
                amount = self.get_amount("Enter amount to deposit: ")
                self.account_management.deposit(account_id, amount)
            elif choice == '5':
                account_id = input("Enter account ID: ")
                amount = self.get_amount("Enter amount to withdraw: ")
                self.account_management.withdraw(account_id, amount)
            elif choice == '6':
                from_account_id = input("Enter source account ID: ")
                to_account_id = input("Enter destination account ID: ")
                amount = self.get_amount("Enter amount to transfer: ")
                self.account_management.transfer(from_account_id, to_account_id, amount)
            elif choice == '7':
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    account_management = AccountManagement()
    interface = BankingSystemInterface(account_management)
    interface.run()