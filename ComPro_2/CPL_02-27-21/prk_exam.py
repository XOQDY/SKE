# import math
#
# # Problem 1
# p = input("Input P: ")
# p = float(p)
# r = input("Input R: ")
# r = float(r)
# t = input("Input t: ")
# t = float(t)
#
# if t < 0:
#     print("invalid input")
# else:
#     a = p * (math.e ** (r * t / 100))
#     print(a)
#
# # Problem 2
# year = input("Input the number of years your car is bought: ")
# if year.isnumeric() and 1 <= int(year) <= 30:
#     year = int(year)
#     total_distance = 0
#     if 1 <= year <= 5:
#         travel_distance = []
#         for i in range(year):
#             d = input(f"Input the distance travelled in year {i + 1}: ")
#             travel_distance.append(d.split(" "))
#         for x in travel_distance:
#             if x[1] == 'mi':
#                 distance = 1.61 * int(x[0])
#                 total_distance += distance
#             else:
#                 total_distance += int(x[0])
#         print("Your car is", year, "years old and the total distance travelled is", total_distance, "km.")
#         if total_distance < 100000:
#             print("Therefore, your car is under the warranty.")
#         else:
#             print("Therefore, your car's warranty is terminated.")
#     else:
#         print("Your car is", year, "years old.")
#         print("Therefore, your car's warranty is terminated.")
# else:
#     print("Invalid input.")

import random

string1 = input("Enter string#1: ")
string2 = input("Enter string#2: ")
string3 = input("Enter string#3: ")
string4 = input("Enter string#4: ")
sentence = [string1, string2, string3, string4]
random.shuffle(sentence)
print("Random order of sentence:", sentence[0], sentence[1], sentence[2], sentence[3])
