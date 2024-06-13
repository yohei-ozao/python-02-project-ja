from abc import ABC, abstractmethod


# def record_history(func):
#     """decorator for Account to record history"""

#     def _wrapper(self, *args, **kwargs):
#         msg = func(self, *args, **kwargs)
#         self.history.append(msg)
#         return msg

#     return _wrapper
    
class Account(ABC):
    __account_id = 0
    def __init__(self, name, balance=0):
        # Initialize any necessary data structures
        self.account_id = Account.__account_id
        self.name = name
        Account.__account_id += 1
        self.balance = balance
        self.histroy = []

    def __str__(self):
        return (
            f"---ACCOUNT INFORMATION---\n"
            f"Account number: {self.account_id}\n"
            f"Name: {self.name}\n"
            f"Balance: {self.balance}\n"
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

    # @record_history
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit {amount} to the account {self.account_id}")
        return True

    # @record_history
    def withdraw(self, amount):
        if not self.can_withdraw(amount):
            print(f"Failed to withdraw {amount} from the account {self.account_id}")
            return False
        self.balance -= amount
        print(f"Withdraw {amount} from the account {self.account_id}")
        return True

    # @record_history
    def apply_interest(self):
        self.balance *= (100 + self.interest) / 100
        return f"Apply interest: {self.interest}% to the account {self.account_id}"

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

    # @record_history
    def withdraw(self, amount):
        if amount > 1_000:
            print(f"Failed to withdraw {amount} from the account {self.account_id}")
            return False
        return super().withdraw(amount)