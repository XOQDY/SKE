# def RecExpo(base, exp):
#     """
#     Recursively computes base^exp for nonnegative exponents and return the result
#
#     Examples:
#         >>> RecExpo(0,200)
#         0
#         >>> RecExpo(200,0)
#         1
#         >>> RecExpo(2,10)
#         1024
#         >>> RecExpo(10,4)
#         10000
#         >>> from math import pi, e
#         >>> RecExpo(pi, 2)
#         9.869604401089358
#         >>> RecExpo(e, 50)
#         5.18470552858706e+21
#
#     """
#     pass


def strlen(s):
    """
    Returns the length of string s using recursion.

    Examples:
        >>> strlen("input")
        5
        >>> strlen("")
        0
        >>> strlen('123456789')
        9
        >>> strlen("I love software engineering")
        27
        >>> strlen('a'*527)
        527
    """
    if s == "":
        return 0
    else:
        return 1 + strlen(s[1:])


def count_zero(n):
    """
    Returns the number of zero in the number `n`

    Examples:
        >>> count_zero(1001)
        2
        >>> count_zero(0)
        1
        >>> count_zero(20202002)
        4
        >>> count_zero(10**200)
        200
        >>> count_zero(1)
        0
    """
    if n < 10:
        if n == 0:
            return 1
        else:
            return 0
    else:
        if (n % 10) == 0:
            return 1 + count_zero(n // 10)
        else:
            return count_zero(n // 10)


