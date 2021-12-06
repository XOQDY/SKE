# Problem 1
try:
    v = float(input('Input v: '))
    s = 0
    value = 0
    n = 0
    while s < v:
        n += 1
        s += (2 ** (1 / 2)) * n - 1

    print(f"n = {n}, S = {s:.2f}")
except ValueError:
    print('Invalid input')

# Problem 2
digit = input('Input 12-digit string: ')
if len(digit) == 12:
    index = 0
    multiplied = 1
    s = 0
    while index < len(digit):
        s += int(digit[index]) * multiplied
        if multiplied == 1:
            multiplied = 3
        else:
            multiplied = 1
        index += 1
    t = 10 - (s % 10)
    if t == 10:
        print('check digit = 0')
    else:
        print(f'check digit = {t}')
else:
    print('Invalid input')
