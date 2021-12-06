from math import sqrt

# 1
FEET_IN_MILE = 5280
miles = 13

feet = FEET_IN_MILE * miles

print(feet)

# 2
hours = 7
minutes = 21
seconds = 37

all_seconds = (hours * 3600) + (minutes * 60) + seconds

print(all_seconds)

# 3
width = 4
height = 7

perimeter = (2 * width) + (2 * height)

print(perimeter)

# 4
pi = 3.14
radius = 8

area = pi * radius**2

print(area)

# 5
present_value = 1000
annual_rate = 7
years = 10

future_value = present_value * (1 + 0.01 * annual_rate)**years

print(future_value)

# 6
x0 = 2
y0 = 2
x1 = 5
y1 = 6

distance = sqrt((x0 - x1)**2 + (y0 - y1)**2)

print(distance)

# 7
x0 = 1
y0 = 1
x1 = 4
y1 = 1
x2 = 4
y2 = 5

a = x1 - x0
b = y2 - y1
c = sqrt(a**2 + b**2)
s = 0.5 * (a + b + c)
area = sqrt(s * (s - a) * (s - b) * (s - c))

print(area)

# 8
cup_of_coffee = int(input("Write how many cup of coffee you will need: "))

water = 200 * cup_of_coffee
milk = 50 * cup_of_coffee
coffee_beans = 15 * cup_of_coffee

print(f"For {cup_of_coffee} cups of coffee you will need:")
print(f"{water} ml of water")
print(f"{milk} ml of milk")
print(f"{coffee_beans} g of coffee beans")
