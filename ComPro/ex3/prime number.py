def check_prime_number(number):
    check = True
    for i in range(2, number):
        if number % i != 0:
            check = True
        else:
            check = False
            break
    return check


def print_result(result):
    if result:
        print("Yes is prime number")
    else:
        print("No isn't prime number")


number = int(input("Number want to test: "))
print_result(check_prime_number(number))
