from item import *
from order import *
from stock import *
from customer import *

# Copy 4 functions from Level 1 here:
# print_stock_list, print_item_list, print_order_list, process_order_list


def print_stock_list(stock_list):
    print('Stock List:')
    for x in range(len(stock_list)):
        print(stock_list[x])


def print_item_list(item_list):
    print('Item List:')
    for x in range(len(item_list)):
        print(item_list[x])


def print_order_list(order_list):
    print('Order List:')
    for x in range(len(order_list)):
        print(order_list[x])


def process_order_list(order_list, stock_list):
    for x in range(len(order_list)):
        if order_list[x].amount <= stock_list[x].amount:
            order_list[x].status = 'Delivered'
            stock_list[x].amount -= order_list[x].amount
        else:
            order_list[x].status = 'Insufficient'


item1 = Item(1,'T-shirt', 'White')
item2 = Item(2,'T-shirt', 'Black')
item3 = Item(3,'Polo-shirt', 'White')
item4 = Item(4,'Polo-shirt', 'Green')
item5 = Item(5,'Shirt', 'Green')
item6 = Item(6,'Shirt', 'Black')

stock1 = Stock(item1, 100, 60)
stock2 = Stock(item2, 100, 90)
stock3 = Stock(item3, 100, 120)
stock4 = Stock(item4, 100, 140)
stock5 = Stock(item5, 100, 200)
stock6 = Stock(item6, 100, 220)

## Add your own code to create a list of stocks here
stock_list = [stock1, stock2, stock3, stock4, stock5, stock6]
print_stock_list(stock_list)

## Add your own code to create a list of 6 items here
item_list = [item1, item2, item3, item4, item5, item6]
print_item_list(item_list)


## Add your own code to create a list of customers
## Hint: For each customer, you need to read two things from user: 1) name and 2) order_list
## After reading information of each customer, create and print this customer, append each customer to a list of customers
print()
print('Customer')
x = 1
continue_to_read = 'y'
customer = []
while continue_to_read == 'y':
    print(f'Customer #{x}')
    name = input('Enter name of customer: ')
    order_list = []
    while True:
        id = int(input('Enter item id (negative to quit): '))
        if id < 0:
            break
        else:
            amount = int(input('Enter amount: '))
            order_list.append(Order(item_list[id - 1], amount))
    customer.append(Customer(name, order_list))
    print(customer[x - 1])
    x += 1
    continue_to_read = input('Continue to read new customer (y/n): ')


price_list = [stock_list[x].price for x in range(len(stock_list))]
## In the list of customers, process order list of each customer
for x in range(len(customer)):
    process_order_list(customer[x].order_list, stock_list)
    customer[x].price_list = price_list
    customer[x].compute_total_cost()
    print(customer[x])
## After processing order list of all customers, print information of each customer
print_stock_list(stock_list)





