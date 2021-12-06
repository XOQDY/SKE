buy = "buy"
fill = "fill"
take = "take"

money = 550
water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9


def fill_coffee():
    fill_water = int(input("Write how many ml of water do you want to add: "))
    fill_milk = int(input("Write how many ml of milk do you want to add: "))
    fill_coffee_beans = int(input("Write how many grams of coffee beans do you want to add: "))
    fill_disposable_cups = int(input("Write how many disposable cups of coffee do you want to add: "))
    return fill_water, fill_milk, fill_coffee_beans, fill_disposable_cups


def take_money(money):
    print(f"I gave you ${money}")
    return 0


def type_coffee():
    type_of_coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
    if type_of_coffee == "1":
        use_water = 250
        use_milk = 0
        use_coffee_beans = 16
        use_money = 4
        return use_water, use_milk, use_coffee_beans, use_money
    elif type_of_coffee == "2":
        use_water = 350
        use_milk = 75
        use_coffee_beans = 20
        use_money = 7
        return use_water, use_milk, use_coffee_beans, use_money
    elif type_of_coffee == "3":
        use_water = 200
        use_milk = 100
        use_coffee_beans = 12
        use_money = 6
        return use_water, use_milk, use_coffee_beans, use_money


def pwater(action, water, use_water, fill_water):
    if action == buy:
        water -= use_water
        return water
    elif action == fill:
        water += fill_water
        return water
    else:
        return water


def pmilk(action, milk, use_milk, fill_milk):
    if action == buy:
        milk -= use_milk
        return milk
    elif action == fill:
        milk += fill_milk
        return milk
    else:
        return milk


def pcoffee_beans(action, coffee_beans, use_coffee_beans, fill_coffee_beans):
    if action == buy:
        coffee_beans -= use_coffee_beans
        return coffee_beans
    elif action == fill:
        coffee_beans += fill_coffee_beans
        return coffee_beans
    else:
        return coffee_beans


def pdisposable_cups(action, disposable_cups, fill_disposable_cups):
    if action == buy:
        disposable_cups -= 1
        return disposable_cups
    elif action == fill:
        disposable_cups += fill_disposable_cups
        return disposable_cups
    else:
        return disposable_cups


def pmoney(action, money, use_money):
    if action == buy:
        money += use_money
        return money
    else:
        return money


def order(action, money, water, milk, coffee_beans, disposable_cups):
    if action == buy:
        use_water, use_milk, use_coffee_beans, use_money = type_coffee()
        water = pwater(action, water, use_water, 0)
        milk = pmilk(action, milk, use_milk, 0)
        coffee_beans = pcoffee_beans(action, coffee_beans, use_coffee_beans, 0)
        disposable_cups = pdisposable_cups(action, disposable_cups, 0)
        money = pmoney(action, money, use_money)
        return water, milk, coffee_beans, disposable_cups, money
    elif action == fill:
        fill_water, fill_milk, fill_coffee_beans, fill_disposable_cups = fill_coffee()
        water = pwater(action, water, 0, fill_water)
        milk = pmilk(action, milk, 0, fill_milk)
        coffee_beans = pcoffee_beans(action, coffee_beans, 0, fill_coffee_beans)
        disposable_cups = pdisposable_cups(action, disposable_cups, fill_disposable_cups)
        money = pmoney(action, money, 0)
        return water, milk, coffee_beans, disposable_cups, money
    elif action == take:
        water = pwater(action, water, 0, 0)
        milk = pmilk(action, milk, 0, 0)
        coffee_beans = pcoffee_beans(action, coffee_beans, 0, 0)
        disposable_cups = pdisposable_cups(action, disposable_cups, 0)
        money = take_money(money)
        return water, milk, coffee_beans, disposable_cups, money


def has_coffee():
    print("The coffee machine has:")
    print(f"{water} of water")
    print(f"{milk} of milk")
    print(f"{coffee_beans} of coffee beans")
    print(f"{disposable_cups} of disposable cups")
    print(f"{money} of money")


def left_coffee():
    print(f"The coffee machine has:")
    print(f"{water_left} of water")
    print(f"{milk_left} of milk")
    print(f"{cbleft} of coffee beans")
    print(f"{cups_left} of disposable cups")
    print(f"{money_left} of money")


has_coffee()
print("")
action = input("Write action (buy, fill, take): ")
water_left, milk_left, cbleft, cups_left, money_left = order(action, money, water, milk, coffee_beans, disposable_cups)
print("")
left_coffee()
