def read_list(number):
    list = []
    for x in range(number):
        value = float(input(f"Enter value{x + 1}: "))
        list.append(value)
    return list


def compute_area_list(s1_list, s2_list, number):
    list = []
    for x in range(number):
        x = s1_list[x] * s2_list[x]
        list.append(x)
    return list


def print_result(s1_list, s2_list, number):
    for x in range(number):
        print(compute_area_list(s1_list, s2_list, number)[x])


number = int(input("Enter n: "))
print("Side 1:")
side1_list = read_list(number)
print("Side 2:")
side2_list = read_list(number)
print_result(side1_list, side2_list, number)
