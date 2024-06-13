from abc import ABC, abstractmethod

class AccountManagement(ABC):
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