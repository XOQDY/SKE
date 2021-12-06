# Problem 2
# first_day_one_str = input()
# second_day_one_str = input()
# third_day_one_str = input()
#
# if first_day_one_str == "S":
#     if second_day_one_str == "M":
#         first_day_two_str = "Su"
#     else:
#         first_day_two_str = "Sa"
# elif first_day_one_str == "M":
#     first_day_two_str = "Mo"
# elif first_day_one_str == "T":
#     if second_day_one_str == "W":
#         first_day_two_str = "Tu"
#     else:
#         first_day_two_str = "Th"
# elif first_day_one_str == "W":
#     first_day_two_str = "We"
# elif first_day_one_str == "F":
#     first_day_two_str = "Fr"
#
# if second_day_one_str == "S":
#     if third_day_one_str == "M":
#         second_day_two_str = "Su"
#     else:
#         second_day_two_str = "Sa"
# elif second_day_one_str == "M":
#     second_day_two_str = "Mo"
# elif second_day_one_str == "T":
#     if third_day_one_str == "W":
#         second_day_two_str = "Tu"
#     else:
#         second_day_two_str = "Th"
# elif second_day_one_str == "W":
#     second_day_two_str = "We"
# elif second_day_one_str == "F":
#     second_day_two_str = "Fr"
#
# if third_day_one_str == "S":
#     if second_day_one_str == "S":
#         third_day_two_str = "Su"
#     else:
#         third_day_two_str = "Sa"
# elif third_day_one_str == "M":
#     third_day_two_str = "Mo"
# elif third_day_one_str == "T":
#     if second_day_one_str == "M":
#         third_day_two_str = "Tu"
#     else:
#         third_day_two_str = "Th"
# elif third_day_one_str == "W":
#     third_day_two_str = "We"
# elif third_day_one_str == "F":
#     third_day_two_str = "Fr"
#
# print(first_day_two_str)
# print(second_day_two_str)
# print(third_day_two_str)

# Problem 4
import math

n = int(input())
decimals = int(input())
multiplier = 10 ** decimals

i = 1
xn = n
# while i != decimals:
#     xn = xn // 10
#     i += 1
# xn = xn % 10
xn = (xn // (multiplier / 10)) % 10

if xn >= 5:
    result = math.ceil(n / multiplier) * multiplier
else:
    result = math.floor(n / multiplier) * multiplier
print(result)
