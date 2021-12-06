# Original Doctest by Mai Norapong (one of the TAs in this course)

def RecMult(num_1, num_2):
    """
    Takes in two nonnegative numbers and return the multiplication result of the two numbers without using the
    multiplication operator *

    Examples:
        >>> RecMult(0,500)
        0
        >>> RecMult(500,0)
        0
        >>> RecMult(1,500)
        500
        >>> RecMult(500,1)
        500
        >>> RecMult(78,16)
        1248
    """
    if num_2 == 0:
        return 0
    num_1 += RecMult(num_1, num_2 - 1)
    return num_1


def RecCountup(n):
    """
    Prints the numbers from 0 to `n`.

    Examples:
        >>> RecCountup(0)
        0

        >>> RecCountup(7)
        0
        1
        2
        3
        4
        5
        6
        7

    """
    if n == 0:
        print(0)
    else:
        RecCountup(n - 1)
        print(n)


def reverse_list(l):
    """
    Returns a new list that enumerates all the elements in `l` in reverse order

    Examples:
        >>> reverse_list([2, 4, 6, 7])
        [7, 6, 4, 2]
        >>> reverse_list(range(20))
        [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        >>> reverse_list([x**2 + x + 1 for x in range(10)])
        [91, 73, 57, 43, 31, 21, 13, 7, 3, 1]
        >>> field = [[3, 0, 1, 1, 1],
        ...          [3, 0, 0, 0, 0],
        ...          [3, 3, 0, 0, 0],
        ...          [0, 2, 2, 2, 0],
        ...          [0, 0, 2, 0, 0]]
        >>> reverse_list(field)
        [[0, 0, 2, 0, 0], [0, 2, 2, 2, 0], [3, 3, 0, 0, 0], [3, 0, 0, 0, 0], [3, 0, 1, 1, 1]]
    """
    if not l:
        return []
    d = (reverse_list(l[1:]))
    d.append(l[0])
    return d


def replace_list(l):
    """
    Returns a new list that replaces the element that is less than 10 with 0 asumming `l` is a list of integers

    Examples:
        >>> replace_list([2, 4, 6, 7])
        [0, 0, 0, 0]
        >>> replace_list([2, 0, 20, 0, 2, 456, 90])
        [0, 0, 20, 0, 0, 456, 90]
        >>> sum(replace_list(range(101))) == 5050 - 45
        True
        >>> sum(replace_list(range(-10, 11)))
        10
        >>> replace_list([])
        []
    """
    l = list(l)
    if not l:
        return []
    elif l[0] < 10:
        l.pop(0)
        return [0] + replace_list(l)
    else:
        n = l[0]
        l.pop(0)
        return [n] + replace_list(l)


def replace_and_reverse_list(l):
    """
    Returns a new list that replaces the element that is less than 10 with 0 assuming `l` is a list of integers

    Examples:
        >>> replace_and_reverse_list([2, 4, 6, 7])
        [0, 0, 0, 0]
        >>> replace_and_reverse_list([2, 0, 20, 0, 2, 456, 90])
        [90, 456, 0, 0, 20, 0, 0]
        >>> replace_and_reverse_list(range(101))
        [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        >>> replace_and_reverse_list(range(-10, 11))
        [10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        >>> replace_and_reverse_list([])
        []
    """
    if not l:
        return []
    elif l[0] < 10:
        d = (replace_and_reverse_list(l[1:]))
        d.append(0)
    else:
        d = (replace_and_reverse_list(l[1:]))
        d.append(l[0])
    return d


def num_digits(n):
    """
    Returns the number of digits in the number n

    Examples:
        >>> num_digits(89556)
        5
        >>> num_digits(20)
        2
        >>> num_digits(10**200)
        201
        >>> num_digits(0)
        1
        >>> num_digits(1)
        1
    """
    if n < 10:
        return 1
    return 1 + num_digits(n // 10)


def sum_digits(n):
    """
    Returns the sum of all the digits in the number n

    Examples:
        >>> sum_digits(12345)
        15
        >>> sum_digits(2040)
        6
    """
    if n < 10:
        return n
    return (n % 10) + sum_digits(n // 10)


def null_odd_digits(n):
    """
    Returns the number that cancels out the effect of the weight of the odd digits

    Examples:
        >>> null_odd_digits(6354)
        6004
        >>> null_odd_digits(3250)
        200
        >>> null_odd_digits(3050)
        0
        >>> null_odd_digits(10**20)
        0
        >>> null_odd_digits(9876543210)
        806040200
    """
    if n < 10:
        if n % 2 == 0:
            return n
        else:
            return 0
    if n % 2 == 0:
        return (n % 10) + (10 * null_odd_digits(n // 10))
    elif n % 2 == 1:
        return 0 + (10 * null_odd_digits(n // 10))


def num_complement(n):
    """
    Returns the number that flips every digit of n from k to 10 - k

    Examples:
        >>> num_complement(3257)
        7853
        >>> num_complement(1289)
        9821
        >>> num_complement(445566)
        665544
        >>> num_complement(917348526)
        193762584
        >>> num_complement(1000128)
        Traceback (most recent call last):
          ...
        ValueError: number cannot contain 0
    """
    if n % 10 == 0:
        raise ValueError("number cannot contain 0")
    if n < 10:
        return 10 - n
    return (10 - (n % 10)) + (10 * num_complement(n // 10))


def count_vowels(word):
    """
    Returns the number of vowels (a, e, i, o, u) in a string using recursion

    Examples:
        >>> count_vowels('Autodifferentiation')
        10
        >>> count_vowels("avada kedavra")
        6
        >>> count_vowels("STAMPEDE")
        3
        >>> count_vowels("stpd")
        0
        >>> count_vowels('A '*350)
        350
    """
    word = word.lower()
    if word == '':
        return 0
    elif word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u':
        return 1 + count_vowels(word[1:])
    return 0 + count_vowels(word[1:])


def sum_rec(nums):
    """
    Returns the sum of a list of numbers using recursion

    Examples:
        >>> sum_rec([3,1,4,1,5,9,2,6,5])
        36
        >>> sum_rec(range(101))
        5050
        >>> sum_rec(range(901))
        405450
        >>> sum_rec([x**3 - 2*x**2  + x - 13 for x in range(901)])
        163903285937
        >>> sum_rec([-1 for x in range(900)])
        -900
    """
    if not nums:
        return 0
    return nums[0] + sum_rec(nums[1:])
