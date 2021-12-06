x = 0
odd = 0
even = -1
while x != -999:
    try:
        x = int(input('Enter: '))
        if x % 2 == 0:
            odd += 1
        elif x % 2 == 1:
            even += 1
    except ValueError:
        print("Error: this is not an integer")

print(f"The number of odd numbers = {odd}")
print(f"The number of even numbers = {even}")
