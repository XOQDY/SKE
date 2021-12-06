from OO_fraction import *

# 1/2 + 1/3 = 5/6
x = Fraction(1, 2)
y = Fraction(1, 3)
z = x.add(y)
print(z)
z1 = x + y
print(z1)
print()

# 1/3 + 1/6 = 1/2
x = Fraction(1, 3)
y = Fraction(1, 6)
z = x.add(y)
print(z)
z1 = x + y
print(z1)
print()

# 8/9 + 1/9 = 1
x = Fraction(8, 9)
y = Fraction(1, 9)
z = x.add(y)
print(z)
z1 = x + y
print(z1)
print()

# 1/200000000 + 1/300000000 = 1/120000000
x = Fraction(1, 200000000)
y = Fraction(1, 300000000)
z = x.add(y)
print(z)
z1 = x + y
print(z1)
print()

# 1073741789/20 + 1073741789/30 = 1073741789/12
x = Fraction(1073741789, 20)
y = Fraction(1073741789, 30)
z = x.add(y)
print(z)
z1 = x + y
print(z1)
print()

#  4/17 + 17/4 = 305/68
x = Fraction(4, 17)
y = Fraction(17, 4)
z = x.add(y)
print(z)
z1 = x + y
print(z1)
print()

#  4/17 * 17/4 = 1
x = Fraction(4, 17)
y = Fraction(17, 4)
z = x.multiply(y)
print(z)
z1 = x * y
print(z1)
print()

# 3037141/3247033 * 3037547/3246599 = 841/961 
x = Fraction(3037141, 3247033)
y = Fraction(3037547, 3246599)
z = x.multiply(y)
print(z)
z1 = x * y
print(z1)
print()

# 1/6 - -4/-8 = -1/3
x = Fraction( 1,  6)
y = Fraction(-4, -8)
z = x.subtract(y)
print(z)
z1 = x - y
print(z1)
