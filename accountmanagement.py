from abc import ABC, abstractmethod

class AccountManagement:
    def __init__(self):
        self.accounts = {}
        
    def open_account(self, account_type, name, initial_balance):
        new_account = account_type(name, initial_balance)
        self.accounts[str(new_account.account_id)] = new_account
        print(f"Account {new_account.account_id} open successfully.")
    
    def close_account(self, account_id):
        if account_id in self.accounts:
            del self.accounts[account_id]
            print(f"Account {account_id} closed successfully.")
        else:
            print(f"Account {account_id} does not exist.")
    
    def get_account_info(self, account_id):
        if account_id in self.accounts:
            print(self.accounts[account_id])
        else:
            print(f"Account {account_id} does not exist.")
        
    def deposit(self, account_id, amount):
        if account_id in self.accounts:
            self.accounts[account_id].deposit(amount)
        else:
            print(f"Account {account_id} does not exist." )
        
    def withdraw(self, account_id, amount):
        if account_id in self.accounts:
            self.accounts[account_id].withdraw(amount)
        else:
            print(f"Account {account_id} does not exist.")
        
    def transfer(self, from_account_id, to_account_id, amount):
        if from_account_id in self.accounts:
            if to_account_id in self.accounts:
                if self.accounts[from_account_id].withdraw(amount):
                    self.accounts[to_account_id].deposit(amount)
                print(f"Transferred {amount} from account {from_account_id} to account {to_account_id}.")
            else:
                print(f"Account {to_account_id} does not exist.")
        else:
            print(f"Account {from_account_id} does not exist.")