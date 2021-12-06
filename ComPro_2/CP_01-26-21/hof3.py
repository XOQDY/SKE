def search(f):
    """Return the smallest non-negative integer x for which f(x) is a true value."""
    x = 0
    while True:
        if f(x):
            return x
        x += 1

def square(x):
    return x * x

def inverse(f):
    """Return a function g(y) that returns x such that f(x) == y.
    """
    return lambda y: search(lambda x: f(x) == y)

print(inverse(square)(100))
print(inverse(square)(49))
print(inverse(square)(25))
print(inverse(square)(16))
print()
sqrt = inverse(square)
print(sqrt(100))
print(sqrt(49))
print(sqrt(25))
print(sqrt(16))
