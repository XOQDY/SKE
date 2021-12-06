class VendingMachine:
    """A vending machine that vends some product for some price.
    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Inventory empty. Restocking required.'
    >>> v.add_funds(15)
    'Inventory empty. Restocking required. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'You must add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Inventory empty. Restocking required. Here is your $15.'
    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, item, price):
        self.item = item
        self.price = price
        self.balance = 0
        self.current_item = 0
        self.change = 0

    def vend(self):
        if self.current_item == 0:
            return 'Inventory empty. Restocking required.'
        elif self.balance < self.price:
            return f'You must add ${self.price - self.balance} more funds.'
        else:
            self.current_item -= 1
            self.change = self.balance - self.price
            self.balance = 0
            if self.change == 0:
                return f'Here is your {self.item}.'
            else:
                return f'Here is your {self.item} and ${self.change} change.'

    def add_funds(self, value):
        if self.current_item == 0:
            return f'Inventory empty. Restocking required. Here is your ${value}.'
        else:
            self.balance += value
            return f'Current balance: ${self.balance}'

    def restock(self, value):
        self.current_item += value
        return f'Current {self.item} stock: {self.current_item}'
