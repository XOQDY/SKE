import doctest
"""
Instruction:
- write a proper docstring that includes any exception conditions
- add two more meaningful testcases to the doctests part of each function
- write the body of the function where a marker "YOUR CODE HERE" appear

To test these functions, use the following command:

python3 -m doctest week5_inclass_ex.py
"""

# return the sum all the digits of n.
def sum_digits(n):
    """
    
    *** write a proper docstring here ***

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12

    *** add two more testcases here ***
    >>> sum_digits(1996) # 1 + 9 + 9 + 6 = 25
    25
    >>> sum_digits(123456789) # 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 50
    45
    """

    # *** YOUR CODE HERE ***
    if isinstance(n, int) == False:
        raise TypeError('n is not integer; n value is {} and n type is {}'.format(n, type(n)))
    result = []
    while n > 0:
        result += n % 10
        n = n // 10

    return result

# return true if n has two eights in a row.
def double_eights(n):
    """
    
    *** write a proper docstring here ***
    Args:
        n (int): input integer >=

    Returns:
        (bool): True if two consecutive 8 is detected in n, returns False, otherwise

    Raise:
        ValueError: if n is negative
        TypeError: if n is not an integer
        OverflowError: if n > 1e30

    >>> double_eights(8)
    False
    >>> double_eights(88)
    True

    *** add two more testcases here ***
    >>> double_eights(-88)
    False
    >>> double_eights(78.88)
    Traceback (most recent call last):
    """

    # *** YOUR CODE HERE ***
    if isinstance(n ,int) == False:
        raise TypeError('n is not integer; n value is {} and n type is {}'.format(n, type(n)))
    if n < 0:
        raise TypeError("n is negative")
    if n > 1e30:
        raise TypeError("OverflowError n is to large")
    state = 0
    while n > 0:
        digit = n % 10
        if state == 0:
            if digit == 8:
                state = 1
            else:
                state = 0
        elif state == 1:
            if digit == 8:
                state = 2
                return True
            else:
                state = 0
        n = n // 10
    return False


# return x*x + y*y, where x and y are the two largest members of the positive numbers a, b, and c.
def two_of_three(a, b, c):
    """
    
    *** write a proper docstring here ***

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    
    *** add two more testcases here ***

    """
 
    # *** YOUR CODE HERE ***

    return a

# return the largest factor of n that is smaller than n.
def largest_factor(n):
    """
    
    *** write a proper docstring here ***

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1

    *** add two more testcases here ***

    """
 
    # *** YOUR CODE HERE ***

    return n

"""
1. Pick a positive integer n as the start.
2. If n is even, divide it by 2.
3. If n is odd, multiply it by 3 and add 1.
4. Continue this process until n is 1.

The number n will travel up and down but eventually end at 1. This sequence of values of n is often called a Hailstone sequence, Write a function that takes a single argument with formal parameter name n, prints out the hailstone sequence starting at n, and returns the number of steps in the sequence:
"""
def hailstone(n):
    """

    *** write a proper docstring here ***

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    
    *** add two more testcases here ***

    """
 
    # *** YOUR CODE HERE ***

    return n

"""
For the following problems, you have to write at least 5 testcases of your own.
"""

# return True if year is a leap year, otherwise return False.
def is_leap_year(year):
    """

    *** write a proper docstring here ***

    *** add five more testcases here ***

    """
 
    # *** YOUR CODE HERE ***

    return False

# return True if the intervals [a,b] and [c,d] intersect and False otherwise.
def interval_intersect(a, b, c, d):
    """

    *** write a proper docstring here ***

    *** add five more testcases here ***

    """
 
    # *** YOUR CODE HERE ***

    return False

# return the smaller root of a quadratic equation a*x^2 + b*x + c = 0 if one exists. If the equation has no real solution, print the message "Error: No real solutions" and simply return.
def smaller_root(a, b, c):
    """

    *** write a proper docstring here ***

    *** add five more testcases here ***

    """
 
    # *** YOUR CODE HERE ***

    return a