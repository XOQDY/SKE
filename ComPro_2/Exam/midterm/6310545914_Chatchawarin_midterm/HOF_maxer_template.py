def square(x):
    return x * x

def maxer(smoke):
    """Return a repeatable function fire(y) that prints the largest smoke(y) so far.
    >>> g = maxer(square)
    >>> h = g(2)(1)(3)(2)(-4) # print the largest square(y) so far
    4
    4
    9
    9
    16
    >>> h = maxer(abs)(2)(1)(3)(2)(-4) # print the largest abs(y) so far
    2
    2
    3
    3
    4
    """
    def fire(y):
        # fill one line of code here
        print(smoke(y))
        def haze(z):
            # fill an if condition and a line of code in the if block here
            if smoke(z) > smoke(y):
                return maxer(smoke)(z)
            # fill a return line here
            return maxer(smoke)(y)
        return haze
    return fire

