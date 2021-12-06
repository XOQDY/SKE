# def change_second_char(string, char):
#     first = string[0:1]
#     second = string[2:]
#     result = first + char + second
#     return result
#
#
# print(change_second_char("bald", "o"))
# print(change_second_char("stitch", "w"))
# print(change_second_char("shell", "m"))

#
# def change_index_char(string, char, index):
#     len_string = len(string)
#     if index > 0:
#         if index < len_string or index > len_string * -1:
#             index_for_second = index + 1
#             first = string[0:index]
#             second = string[index_for_second:]
#             result = first + char + second
#             return result
#     elif index
#     else:
#         return "Error: index out of range"
#
#
# print(change_index_char("bald", "m", 3))
# print(change_index_char("bald", "o", -3))
# print(change_index_char("bald", "m", 4))
# print(change_index_char("bald", "m", -5))

def fix_start(string):
    start_char = string[0]
    result = ""
    for char in string:
        if char == start_char:
            result += "*"
        else:
            result += char


print(fix_start("babble"))
print(fix_start("electrotelethermometer"))
