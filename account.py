from abc import ABC, abstractmethod

class AccountManagement(ABC):
    @abstractmethod
    def open_account(self, account_id, initial_balance):
        pass
    
    @abstractmethod
    def close_account(self, account_id):
        pass
    
    @abstractmethod
    def get_account_info(self, account_id):
        pass

class TransactionProcessing(ABC):
    @abstractmethod
    def deposit(self, account_id, amount):
        pass
    
    @abstractmethod
    def withdraw(self, account_id, amount):
        pass
    
    @abstractmethod
    def transfer(self, from_account_id, to_account_id, amount):
        pass

class CommandLineInterface(ABC):
    @abstractmethod
    def get_user_input(self):
        pass
    
    @abstractmethod
    def display_information(self, message):
        pass
    
    @abstractmethod
    def display_menu(self):
        pass

'''

def record_history(func):
    """decorator for Account to record history"""

    def _wrapper(self, *args, **kwargs):
        msg = func(self, *args, **kwargs)
        self.history.append(msg)
        return msg

    return _wrapper
'''

class Account(AccountManagement, TransactionProcessing, CommandLineInterface):
    def __init__(self, account_number, balance=0):
        # Initialize any necessary data structures
        self.accounts = {}

    def open_account(self, account_id, initial_balance):
        if account_id not in self.accounts:
            self.accounts[account_id] = initial_balance
            self.display_information(f"Account {account_id} opened successfully.")
        else:
            self.display_information(f"Account {account_id} already exists.")
    
    def close_account(self, account_id):
        if account_id in self.accounts:
            del self.accounts[account_id]
            self.display_information(f"Account {account_id} closed successfully.")
        else:
            self.display_information(f"Account {account_id} does not exist.")
    
    def get_account_info(self, account_id):
        if account_id in self.accounts:
            balance = self.accounts[account_id]
            self.display_information(f"Account ID: {account_id}, Balance: {balance}")
        else:
            self.display_information(f"Account {account_id} does not exist.")
    
    def deposit(self, account_id, amount):
        if account_id in self.accounts:
            self.accounts[account_id] += amount
            self.display_information(f"Deposited {amount} into account {account_id}.")
        else:
            self.display_information(f"Account {account_id} does not exist.")
    
    def withdraw(self, account_id, amount):
        if account_id in self.accounts:
            if self.accounts[account_id] >= amount:
                self.accounts[account_id] -= amount
                self.display_information(f"Withdrew {amount} from account {account_id}.")
            else:
                self.display_information("Insufficient funds.")
        else:
            self.display_information(f"Account {account_id} does not exist.")
    
    def transfer(self, from_account_id, to_account_id, amount):
        if from_account_id in self.accounts and to_account_id in self.accounts:
            if self.accounts[from_account_id] >= amount:
                self.accounts[from_account_id] -= amount
                self.accounts[to_account_id] += amount
                self.display_information(f"Transferred {amount} from account {from_account_id} to account {to_account_id}.")
            else:
                self.display_information("Insufficient funds.")
        else:
            self.display_information("One or both accounts do not exist.")
    

    def get_user_input(self):
        return input("Enter your command: ")
    
    def display_information(self, message):
        print(message)

    
    def display_menu(self):
        menu = """
        Menu:
        1. Open Account
        2. Close Account
        3. Get Account Info
        4. Deposit
        5. Withdraw
        6. Transfer
        7. Exit
        """
        self.display_information(menu)

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

'''
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
'''


'''
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


if __name__ == "__main__":
    alice_savings = SavingsAccount("123456", 1000)
    bob_checking = CheckingAccount("987654", 500)

    accounts = [alice_savings, bob_checking]

    print("Initial Account Details:")
    print(alice_savings)
    print(bob_checking)

    print(alice_savings.deposit(200))
    print(alice_savings.withdraw(500))
    print(bob_checking.deposit(300))
    print(bob_checking.withdraw(1000))

    print(alice_savings.get_transaction_history())
    print(bob_checking.get_transaction_history())

    print(alice_savings)
    print(bob_checking)
    
'''

account = Account()
account.run()