buy = "buy"
fill = "fill"
take = "take"
remaining = "remaining"
exit = "exit"

money = 550
water = 400
milk = 540
coffee_beans = 120
cups = 9


def fill_coffee():
    fill_water = int(input("Write how many ml of water do you want to add: "))
    fill_milk = int(input("Write how many ml of milk do you want to add: "))
    fill_coffee_beans = int(input("Write how many grams of coffee beans do you want to add: "))
    fill_disposable_cups = int(input("Write how many disposable cups of coffee do you want to add: "))
    return fill_water, fill_milk, fill_coffee_beans, fill_disposable_cups


def take_money(money):
    print(f"I gave you ${money}")
    return 0


def type_coffee(type_of_coffee):
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
    elif type_of_coffee == "back":
        pass


def order(action, money, water, milk, coffee_beans, disposable_cups):
    if action == buy:
        type_of_coffee = input(
            "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        if type_of_coffee == "back":
            return water, milk, coffee_beans, disposable_cups, money
        else:
            use_water, use_milk, use_coffee_beans, use_money = type_coffee(type_of_coffee)
            water -= use_water
            milk -= use_milk
            coffee_beans -= use_coffee_beans
            disposable_cups -= 1
            money += use_money
            if water < 0 or milk < 0 or coffee_beans < 0 or disposable_cups < 0:
                if water < 0:
                    print("Sorry, not enough water!")
                if milk < 0:
                    print("Sorry, not enough milk!")
                if coffee_beans < 0:
                    print("Sorry, not enough coffee_beans!")
                if disposable_cups < 0:
                    print("Sorry, no cup left!")
                water += use_water
                milk += use_milk
                coffee_beans += use_coffee_beans
                disposable_cups += 1
                money -= use_money
                return water, milk, coffee_beans, disposable_cups, money
            else:
                print("I have enough resources, making you a coffee!")
                return water, milk, coffee_beans, disposable_cups, money
    elif action == fill:
        fill_water, fill_milk, fill_coffee_beans, fill_disposable_cups = fill_coffee()
        water += fill_water
        milk += fill_milk
        coffee_beans += fill_coffee_beans
        disposable_cups += fill_disposable_cups
        money += 0
        return water, milk, coffee_beans, disposable_cups, money
    elif action == take:
        water += 0
        milk += 0
        coffee_beans += 0
        disposable_cups += 0
        print(f"I gave you ${money}")
        money = 0
        return water, milk, coffee_beans, disposable_cups, money
    elif action == remaining:
        water += 0
        milk += 0
        coffee_beans += 0
        disposable_cups += 0
        money += 0
        left_coffee()
        return water, milk, coffee_beans, disposable_cups, money


def left_coffee():
    print(f"The coffee machine has:")
    print(f"{water} of water")
    print(f"{milk} of milk")
    print(f"{coffee_beans} of coffee beans")
    print(f"{cups} of disposable cups")
    print(f"${money} of money")


action = input("Write action (buy, fill, take, remaining, exit): ")
while action != exit:
    water, milk, coffee_beans, cups, money = order(action, money, water, milk, coffee_beans, cups)
    print("")
    action = input("Write action (buy, fill, take, remaining, exit): ")
