class Order:
    def __init__(self, item, amount):
        self.__item = item
        self.__amount = amount
        self.__status = 'To process'
        self.__cost = 0

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, value):
        self.__cost = value

    @property
    def item(self):
        return self.__item

    def __str__(self):
        return '{0},{1},{2},{3},{4} Baht,{5}'.format(self.__item.id, self.__item.type, self.__item.color, self.__amount,
                                                     self.__cost, self.__status)
