from abc import ABC, abstractmethod

def account_exist(func):
    def _wrapper(self, account_id, *args, **kwargs):
        if account_id in self.accounts:
            return func(self, account_id, *args, **kwargs)
        else:
            return print(f"Account {account_id} does not exist.")

    return _wrapper

class AccountManagement:
    def __init__(self):
        self.accounts = {}
        
    def open_account(self, account_type, name, passward, initial_balance):
        new_account = account_type(name, passward, initial_balance)
        self.accounts[str(new_account.account_id)] = new_account
        print(f"Account {new_account.account_id} open successfully.")

    @account_exist
    def close_account(self, account_id):
        del self.accounts[account_id]
        print(f"Account {account_id} closed successfully.")

    @account_exist
    def get_account_info(self, account_id):
            print(self.accounts[account_id])

    @account_exist
    def deposit(self, account_id, amount):
        print(self.accounts[account_id].deposit(amount))

    @account_exist   
    def withdraw(self, account_id, amount):
        print(self.accounts[account_id].withdraw(amount))
    
    def transfer(self, from_account_id, to_account_id, amount):
        if from_account_id in self.accounts:
            if to_account_id in self.accounts:
                if "Failed" not in self.accounts[from_account_id].withdraw(amount):
                    self.accounts[to_account_id].deposit(amount)
                    print(f"Transferred {amount} from account {from_account_id} to account {to_account_id}.")
            else:
                print(f"Account {to_account_id} does not exist.")
        else:
            print(f"Account {from_account_id} does not exist.")