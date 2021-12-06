class BankAccount():
    def __init__(self, acc_id, name, balance):
        self.account_id = acc_id
        self.account_name = name
        self.balance = balance
        bank_DB.add_new_account(self)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print('Insufficient funds. Transaction aborted.')
            raise Exception()
        else:
            self.balance -= amount
    
    def display(self):
        print("Name:" + self.account_name, "ID:" + self.account_id, "balance:" + str(self.balance), end = '')

class BankDataBase():
    def __init__(self):
        self.database = []

    def display(self):
        for account in self.database:
            account.display()

    def search_account(self, account_id):
        for account in self.database:
            if account.account_id == account_id:
                return account
        return None

    def add_new_account(self, account):
        self.database.append(account)

class CheckingAccount(BankAccount):
    def __init__(self, acc_id, name, balance):
        super().__init__(acc_id, name, balance)

    def withdraw(self, amount):
        amount += 2
        if self.balance < amount:
            print('Insufficient funds. Transaction aborted.')
            raise Exception()
        else:
            self.balance -= amount

    def display(self):
        print("Name:" + self.account_name, "ID:" + self.account_id, "balance:" + str(self.balance),
              "checking account withdraw charge:2 interest:0.01", end = '')
        print()


class SavingsAccount(BankAccount):
    def __init__(self, acc_id, name, balance):
        super().__init__(acc_id, name, balance)

    def deposit(self, amount):
        self.balance += amount - 1

    def display(self):
        print("Name:" + self.account_name, "ID:" + self.account_id, "balance:" + str(self.balance),
              "saving account deposit charge:1 interest:0.02", end='')
        print()

import random

bank_DB = BankDataBase()

for i in range(4):
    account_id = str(random.randint(1000, 9999))
    account_name = "account" + str(i)
    balance = random.randint(20, 2000)
    if i % 2 == 0:
        bank_account = CheckingAccount(account_id, account_name, balance)
    else:
        bank_account = SavingsAccount(account_id, account_name, balance)

while 1:
    print('Banking System Menu:')
    print('Press 1 to display all records.')
    print('Press 2 to search for a record')
    print('Press 3 to deposit amount')
    print('Press 4 to withdraw amount')
    print('Press 0 to exit')
    opt = input("Enter a choice (0-4): ")
    if opt == "0":
        break
    elif opt == "1":
        bank_DB.display()
        print()
    elif opt == "2":
        search_account = input("Enter an account number to search: ")
        acc = bank_DB.search_account(search_account)
        if acc:
            acc.display()
        else:
            print("Record not found.")
        print()
    elif opt == "3":
        deposit_account = input("Enter an account number to deposit: ")
        acc = bank_DB.search_account(deposit_account)
        if acc:
            amount = float(input("Enter an amount to deposit: "))
            acc.deposit(amount)
        else:
            print("Record not found.")
        print()
    elif opt == "4":
        withdraw_account = input("Enter an account number to withdraw: ")
        acc = bank_DB.search_account(withdraw_account)
        if acc:
            amount = float(input("Enter an amount to withdraw: "))
            try:
                acc.withdraw(amount)
            except:
                pass
        else:
            print("Record not found.")
        print()
    else:
        print('Invalid choice selection. Please try again')
