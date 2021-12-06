import random


class DB:
    def __init__(self):
        self.bank_account_DB = {}

    def insert(self, bank_account):
        self.bank_account_DB[bank_account[0]] = [bank_account[1], bank_account[2]]

    def search(self, account_id):
        if account_id in self.bank_account_DB:
            return True
        else:
            return False

    def delete(self, account_id):
        if self.search(account_id) is True:
            del self.bank_account_DB[account_id]
        else:
            print('Record not found.')

    def __str__(self):
        d = ''
        for entry in database.bank_account_DB:
            d += f"{entry} : {str(database.bank_account_DB[entry])}\n"
        return d


class BankAccount:
    def __init__(self):
        self.account = ''
        self.amount = 0

    def deposit(self):
        if database.search(self.account) is True:
            database.bank_account_DB[self.account][1] += self.amount
        else:
            print('Record not found.')

    def withdraw(self):
        if database.search(self.account) is False:
            print('Record not found.')
        else:
            if database.bank_account_DB[self.account][1] < self.amount:
                print('Insufficient funds. Transacion aborted.')
            else:
                database.bank_account_DB[self.account][1] -= self.amount

    def transfer(self):
        if database.search(self.account) is True:
            self.withdraw()
            bank.account = input('Enter an account number to transfer: ')
            if database.search(self.account) is True:
                self.deposit()
            else:
                print('Record not found.')
        else:
            print('Record not found.')


database = DB()
for i in range(10):
    bank_account = [str(random.randint(1000, 9999)), 'account' + str(i), random.randint(20, 2000)]
    database.insert(bank_account)
bank = BankAccount()
while True:
    print('Banking System Menu:')
    print('Press 1 to display all records.')
    print('Press 2 to search for a record')
    print('Press 3 to delete a record')
    print('Press 4 to deposit amount')
    print('Press 5 to withdraw amount')
    print('Press 6 to transfer amount')
    print('Press 0 to exit')
    choice = input('Enter a choice (0-4): ')
    if choice == '0':
        break
    elif choice == '1':
        print(database)
    elif choice == '2':
        bank.account = input('Enter an account number to search: ')
        if database.search(bank.account) is True:
            print(bank.account + ':' + str(database.bank_account_DB[bank.account]))
        else:
            print('Record not found.')
    elif choice == '3':
        bank.account = input('Enter an account number to delete: ')
        database.delete(bank.account)
    elif choice == '4':
        bank.account = input('Enter an account number to deposit: ')
        bank.amount = float(input('Enter an amount to deposit: '))
        bank.deposit()
    elif choice == '5':
        bank.account = input('Enter an account number to withdraw: ')
        bank.amount = float(input('Enter an amount to withdraw: '))
        bank.withdraw()
    elif choice == '6':
        bank.account = input('Enter you account number: ')
        bank.amount = float(input('Enter an amount to transfer: '))
        bank.transfer()
    else:
        print('Invalid choice selection. Please try again')
