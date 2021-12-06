from item import *
from order import *
from stock import *


def print_stock_list(stock_list):
    print('Stock :ist:')
    for x in range(len(stock_list)):
        print(stock_list[x])


def print_item_list(item_list):
    print('Item List:')
    for x in range(len(item_list)):
        print(item_list[x])


def read_order_list(item_list):
    order_list = []
    print('Read order list from user...')
    while True:
        id = int(input('Enter item id (negative to quit): '))
        if id < 0:
            break
        else:
            amount = int(input('Enter amount: '))
            order_list.append(Order(item_list[id - 1], amount))
    return order_list


def print_order_list(order_list):
    print('Order List:')
    for x in range(len(order_list)):
        print(order_list[x])


def process_order_list(order_list, stock_list):
    for x in range(len(order_list)):
        if order_list[x].amount <= stock_list[x].amount:
            order_list[x].status = 'Delivered'
        else:
            order_list[x].status = 'Insufficient'


item1 = Item(1,'T-shirt', 'White')
item2 = Item(2,'T-shirt', 'Black')
item3 = Item(3,'Polo-shirt', 'White')
item4 = Item(4,'Polo-shirt', 'Green')
item5 = Item(5,'Shirt', 'Green')
item6 = Item(6,'Shirt', 'Black')
print(item1)
print(item2)

print(item1 == item2)
print(item2 == item2)

stock1 = Stock(item1, 100, 60)
stock2 = Stock(item2, 100, 90)
stock3 = Stock(item3, 100, 120)
stock4 = Stock(item4, 100, 140)
stock5 = Stock(item5, 100, 200)
stock6 = Stock(item6, 100, 220)
print(stock3)
print(stock5)

order1 = Order(item1, 10)
print(order1)

## Add your own code to create a list of stocks
stock_list = [stock1, stock2, stock3, stock4, stock5, stock6]

print_stock_list(stock_list)

item_list = [item1, item2, item3, item4, item5, item6]

print_item_list(item_list)
## Add your own code to read orders from user and use them to create a list of orders

order_list = read_order_list(item_list)
print_order_list(order_list)

process_order_list(order_list, stock_list)

print_order_list(order_list)

print_stock_list(stock_list)
