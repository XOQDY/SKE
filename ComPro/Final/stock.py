class Stock:
    def __init__(self, item, amount, price):
        self.__item = item
        self.__amount = amount
        self.__price = price

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value

    @property
    def price(self):
        return self.__price

    def __str__(self):
        return '{0},{1},{2},{3},{4}'.format(self.__item.id, self.__item.type, self.__item.color, self.__amount,
                                            self.__price)
