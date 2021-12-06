# Local function definitions; returning functions

def make_adder(n):
    """Return a function that takes one argument K and returns K + N.

    >>> 
    7
    """
    def adder(k):
        return k + n
    return adder


add_three = make_adder(3)
print(add_three(4))
print(make_adder(3)(4))

# Lambda expressions

x = 10
square = x * x
square = lambda x: x * x
print(square(4))
