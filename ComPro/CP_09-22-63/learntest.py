# def print_large(*large):
#     print(large)
#
#
# print_large("hello", 2, min(1, 2, 20))
# result = divmod(*(66, 9))
# print(result)
#
# str1 = "hello"
# str2 = "KU"
# zip = zip(str1, str2)
# for x in zip:
#     print(x)
# t = [('a', 0), ('b', 1), ('c', 2)]
# for letter in t:
#     print(letter)
# for letter, number in t:
#     print(letter, number)
# d = {'a': 0, 'b': 1, 'c': 2}
# t = d.items()
# x = d.keys()
# z = d.values()
# print(z)
# print(x)
# print(t)
# for key, value in t:
#     print(key, value)
# for key in d:
#     print(key)
#     print(d[key])

with open("words.txt") as f:
    word_list = []
    for line in f:
        word_list.append(line[0:-1])


print(word_list[0:30])
print(word_list[-30:-1])


def remove_duplicates(s):
    str = ""
    for c in s:
        if c not in str:
            str += c
    return str


print(remove_duplicates("aaaaabbbbbccccd"))


def generate_key(s):
    new_str = remove_duplicates(s)
    temp_list = list(new_str)
    temp_list.sort()
    return tuple(temp_list)


print(generate_key("aaaabbbbbbbcccc"))
print(generate_key("aaasfabcds"))
print(generate_key("sssssffffgg"))


def generate_dict(word_list):
    d = dict()
    for each_word in word_list:
        new_key = generate_key(each_word)
        if new_key not in d:
            d[new_key] = [each_word]
        else:
            d[new_key].append(each_word)
    return d


word_list = ["tea", "ate", "aabbcc", "desalt", "lasted"]
my_dict = generate_dict(word_list)
print(my_dict)
for key, value in my_dict.items():
    print(key, value)



