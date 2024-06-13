from abc import ABC, abstractmethod

class CommandLineInterface(ABC):
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