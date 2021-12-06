import math
import random

# 1.Particles
spin = input("Spin: ")
charge = input("Charge: ")

if spin == "1/2" and charge == "-1/3":
    print("Strange Quark")
elif spin == "1/2" and charge == "2/3":
    print("Charm Quark")
elif spin == "1/2" and charge == "-1":
    print("Election Lepton")
elif spin == "1/2" and charge == "0":
    print("Neutrino Lepton")
elif spin == "1" and charge == "0":
    print("Photon Boson")


# 2.Calculator
first_number = float(input("The first number: "))
second_number = float(input("The second number: "))
arithmetic_operation = input("The arithmetic operations: ")

if arithmetic_operation == "+":
    print(first_number + second_number)
elif arithmetic_operation == "-":
    print(first_number - second_number)
elif arithmetic_operation == "/" and second_number != 0:
    print(first_number / second_number)
elif arithmetic_operation == "*":
    print(first_number * second_number)
elif arithmetic_operation == "mod" and second_number != 0:
    print(first_number % second_number)
elif arithmetic_operation == "pow":
    print(first_number ** second_number)
elif arithmetic_operation == "div" and second_number != 0:
    print(first_number // second_number)
elif second_number == 0:
    print("Division by 0!")


# 3.Farm
money = int(input("Your money: "))
chicken = 23
goat = 678
pig = 1296
cow = 3848
sheep = 6769

# use function to get correct grammar


def nouns(animal_amount, animal_name):
    if animal_amount == 1:
        print(animal_amount, animal_name)
    elif animal_amount > 1 and animal_name != "sheep":
        print(f"{animal_amount} {animal_name}s")
    else:
        print(animal_amount, animal_name)


if money >= sheep:
    name = "sheep"
    amount = money // sheep
    nouns(amount, name)
elif money >= cow:
    name = "cow"
    amount = money // cow
    nouns(amount, name)
elif money >= pig:
    name = "pig"
    amount = money // pig
    nouns(amount, name)
elif money >= goat:
    name = "goat"
    amount = money // goat
    nouns(amount, name)
elif money >= chicken:
    name = "chicken"
    amount = money // chicken
    nouns(amount, name)
else:
    print("None")


# 4.Day
offset = input("Offset: ")
# separate number and operator out
offset_number = int(offset[1:])
offset_operator = offset[0]

if offset_operator == "+" and offset_number >= 12:
    print("Wednesday")
elif offset_operator == "+" and offset_number < 12:
    print("Tuesday")
elif offset_operator == "-" and offset_number >= 10:
    print("Monday")
elif offset_operator == "-" and offset_number < 10:
    print("Tuesday")


# 5.
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


print(is_even(2))
print(is_even(24))
print(is_even(27))


# 6.
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


print(is_year_leap(2000))
print(is_year_leap(1220))
print(is_year_leap(1234))


# 7.
def interval_intersect(a, b, c, d):
    if a <= b and c <= d:
        return True
    else:
        return False


print(interval_intersect(10, 9, 8, 7))
print(interval_intersect(100, 90, 100, 60))
print(interval_intersect(4, 5, 10, 20))


# 8.
def print_digits(number):
    if number >= 100 or number <= 0:
        return "Error: Input is not a two-digit number."
    else:
        number = str(number)
        ten_digit = number[0]
        one_digit = number[1]
        return f"The tens digit is {ten_digit} and the ones digits is {one_digit}"


print(print_digits(14))
print(print_digits(101))
print(print_digits(0))


# 9.
def smaller_root(a, b, c):
    d = b**2 - (4 * a * c)
    if d < 0 or a == 0:
        print("Error: No real solutions")
    elif d >= 0:
        x = (-b - math.sqrt(d) / (2*a))
        return x


print(smaller_root(4, 8, 10))
print(smaller_root(0, 28, 10))
print(smaller_root(2, 4, 2))


# 10.
def there_is_odd(x, y, z):
    x_check = x % 2
    y_check = y % 2
    z_check = z % 2
    check_list = [x, y, z]

    if x_check == 0:
        check_list.remove(x)
    if y_check == 0:
        check_list.remove(y)
    if z_check == 0:
        check_list.remove(z)

    if x_check == 0 and y_check == 0 and z_check == 0:
        return "There is no odd number"
    else:
        return f"There is an odd whose value is {random.choice(check_list)}"


print(there_is_odd(2, 5, 10))
print(there_is_odd(1, 13, 70))
print(there_is_odd(41, 53, 15))


# 11.
def list_all_odds(w, x, y, z):
    w_check = w % 2
    x_check = x % 2
    y_check = y % 2
    z_check = z % 2
    if w_check != 0:
        return f"This value is odd {w}"
    if x_check != 0:
        return f"This value is odd {x}"
    if y_check != 0:
        return f"This value is odd {y}"
    if z_check != 0:
        return f"This value is odd {z}"
    if w_check == 0 and x_check == 0 and y_check == 0 and z_check == 0:
        return "There is no odd number"


print(list_all_odds(1, 5, 48, 20))
print(list_all_odds(14, 55, 8, 10))
print(list_all_odds(210, 94, 46, 20))


# 12.
def max_off_three(x, y, z):
    if x >= y and x >= z:
        return f"The max value is {x}"
    elif y >= x and y >= z:
        return f"The max value is {y}"
    elif z >= x and z >= y:
        return f"The max value is {z}"


print(max_off_three(45, 100, 90))
print(max_off_three(78, 21, 6))
print(max_off_three(25, 17, 788))
