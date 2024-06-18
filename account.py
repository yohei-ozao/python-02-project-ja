from abc import ABC, abstractmethod

def record_history(func):
    """decorator for Account to record history"""

    def _wrapper(self, *args, **kwargs):
        msg = func(self, *args, **kwargs)
        self.history.append(msg)
        return msg

    return _wrapper

def require_password(func):
    """decorator for Account to check passward"""

    def _wrapper(self, *args, **kwargs):
        passward = input("Input the passward: ")
        if passward == self.passward:
            return func(self, *args, **kwargs)
        else:
            return "Failed to operate. Your passward is incorrect."

    return _wrapper
    
class Account(ABC):
    __account_id = 0
    def __init__(self, name, passward, balance=0,):
        self.account_id = Account.__account_id
        self.name = name
        Account.__account_id += 1
        self.passward = passward
        self.balance = balance
        self.history = []

    def __str__(self):
        return (
            f"---ACCOUNT INFORMATION---\n"
            f"Account ID: {self.account_id}\n"
            f"Name: {self.name}\n"
            f"Balance: {self.balance}\n"
            f"{self.get_transaction_history()}\n"
        )

    @abstractmethod
    def can_withdraw(self, amount):
        """check if a user can withdraw the given amount"""
        pass

    @record_history
    def deposit(self, amount):
        self.balance += amount
        return f"Deposit {amount} to the account {self.account_id}"

    # @record_history
    def withdraw(self, amount):
        if not self.can_withdraw(amount):
            return f"Failed to withdraw {amount} from the account {self.account_id}"
        self.balance -= amount
        return f"Withdraw {amount} from the account {self.account_id}"

    @record_history
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

    @record_history
    @require_password
    def withdraw(self, amount):
        if amount > 1_000:
            return f"Failed to withdraw {amount} from the account {self.account_id}"
        return super().withdraw(amount)