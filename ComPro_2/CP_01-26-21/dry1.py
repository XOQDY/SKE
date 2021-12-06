# Make this code DRY

def digits(n):  # add this function
    """Return digits of integer n"""
    n_digits = 0
    while n > 0:
        n //= 10
        n_digits += 1
    return n_digits


def same_length(a, b):
    """Return whether positive integers a and b have the same number of digits."""
    return digits(a) == digits(b)


print(same_length(50, 70))
print(same_length(50, 100))
print(same_length(10000, 12345))
