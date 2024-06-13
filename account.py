from accountmanagement import AccountManagement
from commandlineinterface import CommandLineInterface
from transactionprocessing import TransactionProcessing
from abc import ABC, abstractmethod


def record_history(func):
    """decorator for Account to record history"""

    def _wrapper(self, *args, **kwargs):
        msg = func(self, *args, **kwargs)
        self.history.append(msg)
        return msg

    return _wrapper
    
class Account(ABC):
    def __init__(self, account_number, balance=0):
        # Initialize any necessary data structures
        self.account_number = account_number
        self.balance = balance
        self.histroy = []

    def __str__(self):
        return (
            f"---ACCOUNT INFORMATION---\n"
            f"Account number: {self.account_number}\n"
            f"Balance: {self.balance}\n"
            f"Interest: {self.interest}%\n"
        )

    @property
    def interest(self):
        """helper function to calculate simple interest

        1 <= amount < THRESHOLD: 20.0
        THRESHOLD <= amount: 15.0
        """
        THRESHOLD = 800

        if self.balance >= 1 and self.balance < THRESHOLD:
            return 20.0
        elif self.balance >= THRESHOLD:
            return 15.0

    @abstractmethod
    def can_withdraw(self, amount):
        """check if a user can withdraw the given amount"""
        pass

    @record_history
    def deposit(self, amount):
        self.balance += amount
        return f"Deposit {amount} to the account {self.account_number}"

    @record_history
    def withdraw(self, amount):
        if not self.can_withdraw(amount):
            return f"Failed to withdraw {amount} from the account {self.account_number}"
        self.balance -= amount
        return f"Withdraw {amount} from the account {self.account_number}"

    @record_history
    def apply_interest(self):
        self.balance *= (100 + self.interest) / 100
        return f"Apply interest: {self.interest}% to the account {self.account_number}"

    def get_transaction_history(self):
        result = "---YOUR HISTORY---\n"
        for item in self.history:
            result += item + "\n"
        return result

class SavingsAccount(Account):
    def can_withdraw(self, amount):
        return self.balance - amount >= 50


class CheckingAccount(Account):
    def can_withdraw(self, amount):
        return self.balance >= amount

    @record_history
    def withdraw(self, amount):
        if amount > 1_000:
            return f"Failed to withdraw {amount} from the account {self.account_number}"
        return super().withdraw(amount)

class AccountManager(AccountManagement, CommandLineInterface, TransactionProcessing):
    def __init__(self):
        self.accounts = {}

    def run(self):
        while True:
            self.display_menu()
            choice = self.get_user_input()
            if choice == '1':
                account_id = input("Enter account ID: ")
                initial_balance = float(input("Enter initial balance: "))
                self.open_account(account_id, initial_balance)
            elif choice == '2':
                account_id = input("Enter account ID: ")
                self.close_account(account_id)
            elif choice == '3':
                account_id = input("Enter account ID: ")
                self.get_account_info(account_id)
            elif choice == '4':
                account_id = input("Enter account ID: ")
                amount = float(input("Enter amount to deposit: "))
                self.deposit(account_id, amount)
            elif choice == '5':
                account_id = input("Enter account ID: ")
                amount = float(input("Enter amount to withdraw: "))
                self.withdraw(account_id, amount)
            elif choice == '6':
                from_account_id = input("Enter source account ID: ")
                to_account_id = input("Enter destination account ID: ")
                amount = float(input("Enter amount to transfer: "))
                self.transfer(from_account_id, to_account_id, amount)
            elif choice == '7':
                break
            else:
                self.display_information("Invalid choice. Please try again.")
                
if __name__ == "__main__":
    account = AccountManager()
    account.run()