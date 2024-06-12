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
        self.account_number = account_number
        self.balance = balance
        self.history = []

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