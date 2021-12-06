# Not DRY code
#
# def sum_naturals(n):
#    """Sum the first N natural numbers.
#    """
#    total, k = 0, 1
#    while k <= n:
#        total, k = total + k, k + 1
#    return total
#
# def sum_cubes(n):
#    """Sum the first N cubes of natural numbers.
#    """
#   total, k = 0, 1
#    while k <= n:
#        total, k = total + pow(k, 3), k + 1
#    return total
#
# print(sum_naturals(5))
# print(sum_cubes(5))

# DRY code; factoring out the general method of summation into a function that takes a function as an argument

def identity(k):
    return k


def cube(k):
    return pow(k, 3)


def summation(n, term):
    """Sum the first N terms of a sequence.
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total


def sum_naturals(n):
    """Sum the first N natural numbers.
    """
    return summation(n, identity)


def sum_cubes(n):
    """Sum the first N cubes of natural numbers.
    """
    return summation(n, cube)


print(sum_naturals(5))
print(sum_cubes(5))
