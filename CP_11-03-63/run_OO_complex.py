import OO_complex
import OO_fraction


def test_complex_op(x, y):
    print("First operand: ", end='')
    print(x)
    print("Second operand: ", end='')
    print(y)
    print("First + Second = ", end='')
    print(x + y)
    print("Second + First = ", end='')
    print(y + x)
    print("First - Second = ", end='')
    print(x - y)
    print("Second - First = ", end='')
    print(y - x)
    print("First * Second = ", end='')
    print(x * y)
    print("Second * First = ", end='')
    print(y * x)


x = OO_complex.Complex(5.0, 6.0)
y = OO_complex.Complex(-3.0, 4.0)
test_complex_op(x, y)
print()

'''
Output:
First operand: 5.0 + 6.0j
Second operand: -3.0 + 4.0j
First + Second = 2.0 + 10.0j
Second + First = 2.0 + 10.0j
First - Second = 8.0 + 2.0j
Second - First = -8.0 + -2.0j
First * Second = -39.0 + 2.0j
Second * First = -39.0 + 2.0j
'''

# Create two Fraction objects and make a first Complex object of the form 1/2 + 1/3j
# Create another two Fraction objects and make a second Complex object of the form 1/3 + 1/6j
# Run test_complex_op with the two Complex objects, put the first object as the first argument and the second object as the second argument

# Create 1/2 + 1/3j object
x1 = OO_fraction.Fraction(1, 2)
y1 = OO_fraction.Fraction(1, 3)
c1 = OO_complex.Complex(x1, y1)

# Create 1/3 + 1/6j object
x2 = OO_fraction.Fraction(1, 3)
y2 = OO_fraction.Fraction(1, 6)
c2 = OO_complex.Complex(x2, y2)

# Run test_complex with the above two objects
test_complex_op(c1, c2)

'''
Output:
First operand: 1/2 + 1/3j
Second operand: 1/3 + 1/6j
First + Second = 5/6 + 1/2j
Second + First = 5/6 + 1/2j
First - Second = 1/6 + 1/6j
Second - First = -1/6 + -1/6j
First * Second = 1/9 + 7/36j
Second * First = 1/9 + 7/36j
'''
