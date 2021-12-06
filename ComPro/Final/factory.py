from customer import *
from order import *
from item import *


class Factory:
    def __init__(self, stock_list, item_list, file_name):
        self.__stock_list = stock_list
        self.__item_list = item_list
        self.__customer_list = []
        self.__price_list = []
        self.__file_name = file_name

    def create_custom_list(self):
        name_check = 'Ann'
        order_list = []
        with open(self.__file_name) as x:
            for line in x:
                line = line.split(',')
                if line[0] == name_check:
                    order_list.append(Order(self.__item_list[int(line[1]) - 1], int(line[2])))
                else:
                    self.__customer_list.append(Customer(name_check, order_list))
                    name_check = line[0]
                    order_list = []

    def print_stock_list(self):
        print('Stock List:')
        for x in range(len(self.__stock_list)):
            print(self.__stock_list[x])

    def print_item_list(self):
        print('Item List:')
        for x in range(len(self.__item_list)):
            print(self.__item_list[x])

    def print_customer_list(self):
        print('Customer List:')
        for x in range(len(self.__customer_list)):
            print(self.__customer_list[x])

    def process_all_customer_list(self):
        for x in range(len(self.__customer_list)):
            for i in range(len(self.__customer_list[x])):
                if self.__customer_list[x].order_list[x].amount <= \
                        self.__stock_list[self.__customer_list[x].order_list[x].item.id].amount:
                    self.__customer_list[x].order_list[x].status = 'Delivered'
                    self.__stock_list[self.__customer_list[x].order_list[x].item.id].amount -= \
                        self.__customer_list[x].order_list[x].amount
                else:
                    self.__customer_list[x].order_list[x].status = 'Insufficient'
            self.__customer_list[x].price_list = self.__price_list
            self.__customer_list[x].compute_total_cost()

    def process_one_customer(self, name):
        for x in range(len(self.__customer_list)):
            if self.__customer_list[x].name == name:
                for i in range(len(self.__customer_list[x])):
                    if self.__customer_list[x].order_list[x].amount <= \
                            self.__stock_list[self.__customer_list[x].order_list[x].item.id].amount:
                        self.__customer_list[x].order_list[x].status = 'Delivered'
                        self.__stock_list[self.__customer_list[x].order_list[x].item.id].amount -= \
                            self.__customer_list[x].order_list[x].amount
                    else:
                        self.__customer_list[x].order_list[x].status = 'Insufficient'
                self.__customer_list[x].price_list = self.__price_list
                self.__customer_list[x].compute_total_cost()
            print(self.__customer_list[x])


    def update_stock(self, item_id, amount):
        for x in range(len(self.__stock_list)):
            if self.__stock_list[x].item.id == item_id:
                self.__stock_list[x].amount += amount

    @property
    def price_list(self):
        return self.__price_list

    @price_list.setter
    def price_list(self, value):
        self.__price_list = value



