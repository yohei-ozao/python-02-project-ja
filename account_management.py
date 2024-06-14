from abc import ABC, abstractmethod
from account import Account

def account_exist(func):
    """decorator to confirm the account exists"""
    def _wrapper(self, account_id, *args, **kwargs):
        if account_id in self.accounts:
            return func(self, account_id, *args, **kwargs)
        else:
            return print(f"Account {account_id} does not exist.")

    return _wrapper

class AccountManagement:
    def __init__(self):
        self.accounts = {}
        
    def open_account(self, account_type: Account, name: str, passward: str, initial_balance: int) -> None:
        """open new account

        Args:
            account_type (Account): class of account
            name (str): account name
            passward (str): passward for transaction
            initial_balance (int): balance when the account open
        """
        new_account = account_type(name, passward, initial_balance)
        self.accounts[str(new_account.account_id)] = new_account
        print(f"Account {new_account.account_id} open successfully.")

    @account_exist
    def close_account(self, account_id: str) -> None:
        """close exist account

        Args:
            account_id (str): Account ID to be closed
        """
        del self.accounts[account_id]
        print(f"Account {account_id} closed successfully.")

    @account_exist
    def get_account_info(self, account_id: str) -> None:
        """show the information of the account

        Args:
            account_id (str): Account ID to get the information
        """
        print(self.accounts[account_id])

    @account_exist
    def deposit(self, account_id: str, amount: int) -> None:
        """deposit money to the account

        Args:
            account_id (str): Account ID to be deposited
            amount (int): Deposit Amount
        """
        print(self.accounts[account_id].deposit(amount))

    @account_exist   
    def withdraw(self, account_id: str, amount: int) -> None:
        """withdraw money from the account

        Args:
            account_id (str): Account ID to withdraw
            amount (int): Withdraw Amount
        """
        print(self.accounts[account_id].withdraw(amount))
    
    def transfer(self, from_account_id: str, to_account_id: str, amount: int) -> None:
        """transfer money to another account

        Args:
            from_account_id (str): Remittance Source Account
            to_account_id (str): Recipient Account
            amount (int): Transfer Amount
        """
        if from_account_id in self.accounts:
            if to_account_id in self.accounts:
                if "Failed" not in self.accounts[from_account_id].withdraw(amount):
                    self.accounts[to_account_id].deposit(amount)
                    print(f"Transferred {amount} from account {from_account_id} to account {to_account_id}.")
            else:
                print(f"Account {to_account_id} does not exist.")
        else:
            print(f"Account {from_account_id} does not exist.")