class Customer:
    def __init__(self, name, order_list):
        self.__name = name
        self.__order_list = order_list
        self.__total_cost = 0
        self.__price_list = []

    def compute_total_cost(self):
        for x in range(len(self.__order_list)):
            if self.__order_list[x].status == 'Delivered':
                self.__order_list[x].cost = self.__order_list[x].amount * \
                                            self.__price_list[self.__order_list[x].item.id - 1]
                self.__total_cost += self.__order_list[x].cost

    @property
    def name(self):
        return self.__name

    @property
    def order_list(self):
        return self.__order_list

    @property
    def price_list(self):
        return self.__price_list

    @price_list.setter
    def price_list(self, value):
        self.__price_list = value

    def __str__(self):
        d = f"Customer {self.__name}\n"
        d += f'Total_cost = {self.__total_cost}\n'
        for x in range(len(self.__order_list)):
            d += '{0},{1},{2},{3},{4} Baht,{5}\n'.format(self.__order_list[x].item.id, self.__order_list[x].item.type,
                                                       self.__order_list[x].item.color, self.__order_list[x].amount,
                                                       self.__order_list[x].cost, self.__order_list[x].status)
        return d

