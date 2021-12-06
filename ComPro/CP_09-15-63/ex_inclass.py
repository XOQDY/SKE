# 1
def print_dictionary_1(n):
    dic = dict()
    for x in range(1, n+1):
        dic[x] = x * x
    return dic


print(print_dictionary_1(5))


# 2
key = ["red", "green", "blue"]
values = ["#FF0000", "#008000", "#0000FF"]


def print_dictionary_2(key, values):
    dic = dict()
    for x in range(3):
        dic[key[x]] = values[x]
    return dic


print(print_dictionary_2(key, values))


# 3
def print_dictionary_3(my_dict):
    max = my_dict["y"]
    min = my_dict["x"]
    return max, min


my_dict = {"x": 500, "y": 5874, "z": 560}
max, mix = print_dictionary_3(my_dict)
print(f"Maximum Value: {max}")
print(f"Minimum Value: {mix}")
