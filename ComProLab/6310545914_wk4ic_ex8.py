def read_list(number):
    list = []
    for x in range(number):
        value = float(input(f"Enter value{x + 1}: "))
        list.append(value)
    return list


def compute_rectangle_area(s1_list, s2_list, number):
    list = []
    for x in range(number):
        x = s1_list[x] * s2_list[x]
        list.append(x)
    return list


def compute_rectangle_perimeter(s1_list, s2_list, number):
    list = []
    for x in range(number):
        x = (s1_list[x] * 2) + (s2_list[x] * 2)
        list.append(x)
    return list


def chose_area_or_perimeter(chose, s1_list, s2_list, number):
    if chose == "A":
        return compute_rectangle_area(s1_list, s2_list, number)
    elif chose == "P":
        return compute_rectangle_perimeter(s1_list, s2_list, number)


def print_result(chose, s1_list, s2_list, number):
    for i in range(number):
        print(chose_area_or_perimeter(chose, s1_list, s2_list, number)[i])


number = int(input("Enter n: "))
chose = input("Area (A) or Perimeter (P)? ")
print("Side 1")
s1_list = read_list(number)
print("Side 2")
s2_list = read_list(number)
print_result(chose, s1_list, s2_list, number)
