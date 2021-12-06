def new_item():
    name = input("Name : ")
    print(name + " added")
    return name


def delete_item(list_name):
    while True:
        try:
            number = int(input("Number? : "))
            if number <= len(list_name):
                list_name.pop(number - 1)
                show_item(list_name)
                break
            elif len(list_name) < number or number <= 0:
                print("Not in range")
        except ValueError:
            print("Not a number")


def show_item(list_name):
    for i in range(len(list_name)):
        print(f"({i + 1}) {list_name[i]}")


def menu_text(action, list_name):
    if action == "N" or action == "n":
        list_name.append(new_item())
    elif action == "Q" or action == "q":
        print("Bye")
    if list_name != []:
        if action == "S" or action == "s":
            show_item(list_name)
        elif action == "D" or action == "d":
            delete_item(list_name)
    else:
        print("Incorrect Menu")


list_name = []
action = ""
while action != "Q" and action != "q":
    if list_name == []:
        action = input("(N)ew (Q)uit : ")
    else:
        action = input("(N)ew (S)how (D)elete (Q)uit : ")
    menu_text(action, list_name)

