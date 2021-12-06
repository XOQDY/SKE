# format dictionary entry (account_ID: [account_name, balance])
bank_account_DB = {}

# display all bank accounts in the database
def display():
    for entry in bank_account_DB:
        print(entry + ':' + str(bank_account_DB[entry]))

# search for a given bank account with ID
def search(account_ID):
    if account_ID in bank_account_DB:
        return True
    else:
        return False

# deposit an amount to a given bank account ID
def deposit(account_ID, amount):
    if search(account_ID) == True:
        bank_account_DB[account_ID][1] += amount
    else:
        print('Record not found.')

# withdraw an amount from a given bank account ID
def withdraw(account_ID, amount):
    if search(account_ID) == False:
        print('Record not found.')
    else:
        if bank_account_DB[account_ID][1] < amount:
            print('Insufficient funds. Transacion aborted.')
        else:
            bank_account_DB[account_ID][1] -= amount
        
# generate 10 random bank accounts and put them in the bank account database, bank_account_DB
import random
for i in range(10):
    account_ID = str(random.randint(1000, 9999))
    accout_name = 'account' + str(i)
    balance = random.randint(20, 2000)
    bank_account_DB[account_ID] = [accout_name, balance]

# main loop to run our banking system
while True:
    print('Banking System Menu:')
    print('Press 1 to display all records.')
    print('Press 2 to search for a record')
    print('Press 3 to deposit amount')
    print('Press 4 to withdraw amount')
    print('Press 0 to exit')
    choice = input('Enter a choice (0-4): ')
    if choice == '0':
        break
    elif choice == '1':
        display()
    elif choice == '2':
        search_account = input('Enter an account number to search: ')
        if search(search_account) == True:
            print(search_account + ':' + str(bank_account_DB[search_account]))
        else:
            print('Record not found.')
    elif choice == '3':
        deposit_account = input('Enter an account number to deposit: ')
        deposit_amount = float(input('Enter an amount to deposit: '))
        deposit(deposit_account, deposit_amount)
    elif choice == '4':
        withdraw_account = input('Enter an account number to withdraw: ')
        withdraw_amount = float(input('Enter an amount to withdraw: '))
        withdraw(withdraw_account, withdraw_amount)
    else:
        print('Invalid choice selection. Please try again')
