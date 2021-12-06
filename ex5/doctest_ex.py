import itertools


def string_interleave(s1, s2):
    """ Interleave string with the first character from the larger of s1 or s2, take each character from the smaller
    string from index 0 on and interleave it with each character from the larger string.

    Args:
        s1 (str) : input str
        s2 (str) : input str

    Returns:
        str: the  new interleaved string of s1 and s2

    Raises:
        TypeError: if s1 or s2 is not a string

    Examples:
        >>> string_interleave("abc", "mnopq")
        'manbocpq'
        >>> string_interleave("mnopq", "abc")
        'manbocpq'
        >>> string_interleave("Hello", "Sawasdee Thailand")
        'SHaewlalsodee Thailand'
        >>> string_interleave("Mine", "Thai")
        'TMhianie'
        >>> string_interleave(45651, "game")
        Traceback (most recent call last):
        ...
        TypeError: s1 is not string

    """
    if type(s1) != str:
        raise TypeError('s1 is not string')
    if type(s2) != str:
        raise TypeError('s2 is not string')
    if type(s1) == int or type(s2) == int:
        pass
    elif s1[0] > s2[0]:
        s = "".join([x + y for x, y in itertools.zip_longest(s1, s2, fillvalue="")])
        return s
    elif s1[0] < s2[0]:
        s = "".join([x + y for x, y in itertools.zip_longest(s2, s1, fillvalue="")])
        return s


def selective_sum(n, k):
    """ Calculate the sum of the k largest digits of n

    Args:
        n (int) : input integer value
        k (int) : input integer value

    Returns:
        int: the sum of the k largest digits of n

    Raises:
        TypeError: if n or k is not an integer
        Exception: if k is negative

    Examples:
        >>> selective_sum(3018, 2)
        11
        >>> selective_sum(593796, 3)
        25
        >>> selective_sum(12345, 10)
        15
        >>> selective_sum(-7894, 3)
        24
        >>> selective_sum("KU", 2)
        Traceback (most recent call last):
        ...
        TypeError: n is not integer

    """
    n_str = tuple(str(n))
    sum = 0
    if type(n) != int:
        raise TypeError('n is not integer')
    if type(k) != int:
        raise TypeError('k is not integer')
    if k < 0:
        raise Exception('k must be greater than zero')
    if k > len(str(n)):
        for x in range(len(n_str)):
            sum += int(n_str[x])
        return sum
    for x in range(k):
        sum += int(max(n_str))
        for i in range(len(n_str)):
            if max(n_str) == n_str[i]:
                n_str = n_str[0: i] + n_str[i + 1:]
                break
    return sum


def list_intersect(l1, l2):
    """Given l1 and l2 are lists, returns the intersection list of l1 and l2. The intersection list contains elements
    that are in both l1 and contains no duplicate elements.

    Args:
        l1 (list) : input list
        l2 (list) : input list

    Returns:
        the intersection list of l1 and l2. The intersection list contains elements
    that are in both l1 and contains no duplicate elements.

    Raises:
        TypeError: if l1 or l2 is not a list

    Examples:
        >>> list_intersect([1, 2, 3, 4], [1, 2, 2, 3, 4])
        [1, 2, 3, 4]
        >>> list_intersect([1, 2, 3, 4], [1, 2, 3, 4 , 5, 6, 7, 8])
        [1, 2, 3, 4]
        >>> list_intersect([9, 10, 11, 12], [5, 6, 7, 8])
        []
        >>> list_intersect([9, 10 ,11 ,12], [5, 6, 9, 10, 7, 8])
        [9, 10]
        >>> list_intersect([1, 2, 3, 4, 4, 1], [7, 8, 9, 10 ,1 ,2 ,3])
        [1, 2, 3]

    """
    list_result = []
    for x in range(len(l1)):
        for i in range(len(l2)):
            if l1[x] not in list_result:
                if l1[x] == l2[i]:
                    list_result.append(l1[x])
    return list_result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
