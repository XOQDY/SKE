bank_account = {}

# Format dictionary entry (ID, [Name, Balance])

def create_account(ID, Name, Balance=0.0):
    # Assuming you have checked that there is no duplicated ID
    bank_account[ID] = [Name, Balance]

def deposit(ID, amount):
    """ Make a deposit """
    prev_balance = bank_account.get(ID)[1]
    new_balance = prev_balance + amount
    bank_account[ID] = [bank_account.get(ID)[0], new_balance]

def withdraw(ID, amount):
    """ Make a withdraw """
    prev_balance = bank_account.get(ID)[1]
    if amount > prev_balance:
        raise ValueError("insufficient funds")
    new_balance = prev_balance - amount
    bank_account[ID] = [bank_account.get(ID)[0], new_balance]

def transfer(from_id, to_id, amount):
    """ Make a transfer """
    from_id_prev_balance = bank_account.get(from_id)[1]
    if amount > from_id_prev_balance:
        raise ValueError("insufficient funds")
    new_from_id_balance = from_id_prev_balance - amount
    bank_account[from_id] = [bank_account.get(from_id)[0], new_from_id_balance]
    to_id_prev_balance = bank_account.get(to_id)[1]
    to_id_new_balance = to_id_prev_balance + amount
    bank_account[to_id] = [bank_account.get(to_id)[0], to_id_new_balance]


