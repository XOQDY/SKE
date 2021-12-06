# Simulating an ATM
DEPOSIT = "DEPOSIT"
WITHDRAW = "WITHDRAW"
DISPLAY = "DISPLAY"
UNDEF = "UNDEF"
# read the data
card_number = input("Enter card number: ")
input_pin = input("Enter PIN: ")
# card_pin and card_balance are read from the database
card_pin = "1234"
card_balance = 450


def deposit_money(amount, card_balance):
   card_balance += amount
   return card_balance


def withdraw_money(amount, card_balance):
   card_balance -= amount
# save new balance to the database
   return card_balance


def log_transaction(action, money, card_balance):
   if action in (DEPOSIT, WITHDRAW):
    print(action + ": $", money)
    print("Current balance:", card_balance)
   elif action == DISPLAY:
    print("Current balance:", card_balance)
   else:
    print("Undefined action")


def move_money(action, money, card_balance):
  if action == DEPOSIT:
   return deposit_money(money, card_balance)
  elif action == WITHDRAW:
   return withdraw_money(money, card_balance)
  elif action == DISPLAY:
   return card_balance
  else:
   return UNDEF


def get_amount_of_money(action):
  if action == DISPLAY:
      return 0.0
  money = input("Enter the sum of money to " + action + ": ")
  return float(money)


def make_transaction(action, card_balance):
    money = get_amount_of_money(action)
    card_balance = move_money(action, money, card_balance)
    log_transaction(action, money, card_balance)


if card_pin == input_pin:
      action = input("Enter desired action: ")
      make_transaction(action, card_balance)
else:
      print("Incorrect pin!")











































































