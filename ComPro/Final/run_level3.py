from item import *
from order import *
from stock import *
from customer import *
from factory import *

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
## Add your own code to create a list of 6 items here
item_list = [item1, item2, item3, item4, item5, item6]
price_list = [stock_list[x].price for x in range(len(stock_list))]

factory = Factory(stock_list, item_list, 'customer_orders.txt')
factory.print_stock_list()
factory.print_item_list()
factory.create_custom_list()
factory.print_customer_list()

## Add your own code from here
print('--------------')
while True:
    print('1. Process all customers')
    print('2. Process one customer')
    print('3. Add stock')
    print('4. Quit')
    choice = input("Enter your choice: ")
    if choice == '1':
        factory.process_all_customer_list()
        factory.print_customer_list()
    elif choice == '2':
        name = int(input('Enter customer name: '))
        factory.process_one_customer(name)
        factory.print_stock_list()
    elif choice == '3':
        item_id = int(input('Enter item id: '))
        amount = int(input('Enter item amount: '))
        factory.update_stock(item_id, amount)
        factory.print_stock_list()
    elif choice == '4':
        break
