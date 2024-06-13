from abc import ABC, abstractmethod

class TransactionProcessing(ABC):
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
