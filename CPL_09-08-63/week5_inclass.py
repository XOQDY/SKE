# 1.1
num = 0
read_number = 0

while num != -99:
    read_number += 1
    num = int(input(f"Enter value{read_number}: "))

print(f"You entered {read_number - 1} numbers")

# 1.2
read_number = 0
while True:
    read_number += 1
    num = int(input(f"Enter value{read_number}: "))
    if num == -99:
        break
print(f"You entered {read_number - 1} numbers")


# 2.1
num = 0
read_number = 0
sum_number = 0

while num != -99:
    read_number += 1
    num = int(input(f"Enter value{read_number}: "))
    sum_number += num

print(f"You entered {read_number - 1} numbers")
print(f"Sum of them = {sum_number + 99}")

# 2.2
read_number = 0
sum_number = 0
while True:
    read_number += 1
    num = int(input(f"Enter value{read_number}: "))
    sum_number += num
    if num == -99:
        break
print(f"You entered {read_number - 1} numbers")
print(f"Sum of them = {sum_number + 99}")


# 3.1
num = 0
read_number = 0
sum_number = 0
list_number = []
avg_number = 0

while num != -99:
    read_number += 1
    num = int(input(f"Enter value{read_number}: "))
    if num != -99:
        list_number.append(num)
        sum_number += num
        avg_number = sum_number / read_number

print(list_number)
print(f"{avg_number:.2f}")

# 3.2
num = 0
read_number = 0
sum_number = 0
list_number = []
avg_number = 0

while True:
    read_number += 1
    num = int(input(f"Enter value{read_number}: "))
    if num != -99:
        list_number.append(num)
        sum_number += num
        avg_number = sum_number / read_number
    elif num == -99:
        break

print(list_number)
print(f"{avg_number:.2f}")


# 4.2
def read_list_while():
    read_number = 0
    sum_number = 0
    list_number = []

    while True:
        read_number += 1
        num = int(input(f"Enter value{read_number}: "))
        if num != -99:
            list_number.append(num)
            sum_number += num
        elif num == -99:
            break
    return list_number


list1 = read_list_while()
print(list1)
print(f"{sum(list1) / len(list1):.2f}")


# 5.
def read_list_while():
    read_number = 0
    sum_number = 0
    list_number = []

    while True:
        read_number += 1
        num = int(input(f"Enter value{read_number}: "))
        if num != -99:
            list_number.append(num)
            sum_number += num
        elif num == -99:
            break
    return list_number


def read_two_vectors():
    print("Enter vector 1:")
    print(read_list_while())
    print("Enter vector 2:")
    print(read_list_while())


read_two_vectors()


# 6.
def sum_vector(list1, list2):
    list_result = []
    for i in range(len(list1)):
        result = list1[i] + list2[i]
        list_result.append(result)
    return list_result


def diff_vector(list1, list2):
    list_result = []
    for i in range(len(list1)):
        result = list1[i] - list2[i]
        list_result.append(result)
    return list_result


def dot_vector(list1, list2):
    result = 0
    for i in range(len(list1)):
        result += list1[i] * list2[i]
    return result


print('Enter vector 1:')
v1 = read_list_while()
print('Vector 1:')
print(v1)
print('Enter vector 2:')
n = len(v1)
v2 = read_list_while()
print('Vector 2:')
print(v2)
v_sum = sum_vector(v1, v2)
print('Sum result: ')
print(v_sum)
v_diff = diff_vector(v1, v2)
print('Diff result: ')
print(v_diff)
dot_result = dot_vector(v1, v2)
print('Dot product: ')
print(dot_result)


# 7.
def print_every_n(list1, n):
    index = len(list1)
    for i in range(1, index + 1):
        if i % n == 0:
            print(list1[i - 1])


def print_mod_n(list1, n):
    for i in range(len(list1)):
        if list1[i] % n == 0:
            print(list1[i])


def find_n(list1, n):
    list_every_n = []
    for i in range(len(list1)):
        if list1[i] == n:
            list_every_n.append(i)
    return list_every_n


v1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 3, 3, 9, 3, 99]
n_ex7 = 3
print('Initial vector:')
print(v1)
print(f'Print every {n_ex7}th number:')
print_every_n(v1, n_ex7)
print(f'Print numbers divisible by {n_ex7}')
print_mod_n(v1, n_ex7)
print(f'Print list index of {n_ex7}')
index_result = find_n(v1, n_ex7)
print(index_result)
