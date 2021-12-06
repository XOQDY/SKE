water_cup = 200
milk_cup = 50
coffee_beans_cup = 15
water_have = int(input("Write how many ml of water the coffee machine has: "))
milk_have = int(input("Write how many ml of milk the coffee machine has: "))
coffee_beans_have = int(input("Write how many grams of coffee beans the coffee machine has: "))
need_cups = int(input("Write how many cups of coffee you will need: "))

# How many cups of coffee we can make
water = water_have // water_cup
milk = milk_have // milk_cup
coffee_beans = coffee_beans_have // coffee_beans_cup
cups = 0

# Chose the smaller
if water > 0 and milk > 0 and coffee_beans > 0:
    if water <= milk and water <= coffee_beans:
        cups = water
    elif milk <= water and milk <= coffee_beans:
        cups = milk
    elif coffee_beans <= milk and coffee_beans <= milk:
        cups = coffee_beans

# check we can make enough or not
make_cups = cups - need_cups

if make_cups > 0:
    print(f"Yes, I can make that amount of coffee (and even {cups - need_cups} more than that)")
elif make_cups == 0:
    print("Yes, I can make that amount of coffee")
elif make_cups <= 0:
    print(f"No, I can make only {cups} cups of coffee")
