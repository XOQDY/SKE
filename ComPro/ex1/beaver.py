# def repeat_string(a_string, target_length):
#     number_of_repeats = target_length // len(a_string) + 1
#     a_string_repeated = a_string * number_of_repeats
#     a_string_repeated_to_target = a_string_repeated[:target_length]
#     return a_string_repeated_to_target
#
# repeated_string = repeat_string("abc", 5)
import math
x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = float(input("Enter z: "))
a1 = math.pow(x, y)+z
a2 = math.cos(math.pi*2)+math.lgamma(x)
print(math.log(x))
print()
a3 = math.fabs(x)+math.fabs(y)
a4 = math.sqrt(x**2+y**2+z**2)
a5 = math.sin(x)**2+math.cos(x)**2
a6 = math.pow(x+y, 1/5)
a7 = math.e**(x*math.log(y))
print("{:.2f}".format(a1))
print(a2)
print("{:.2f}".format(a3))
print("{:.2f}".format(a4))
print("{:.2f}".format(a5))
print("{:.2f}".format(a6))
print(a7)
