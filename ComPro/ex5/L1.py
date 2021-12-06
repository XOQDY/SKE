def char_index_list(s, c):
    """This function returns the list of indices of a specified character,c, in an input string, s.

    Args:
        s (str) : input str
        c (str) : input character

    Returns:
        list : list of indices of a specified character,c, in an input string, s.

    Exception:
        type(s) != str
        type(c) != str

    Examples:
        >>> char_index_list("aabaabaacca", 'a')
        [0, 1, 3, 4, 6, 7, 10]
        >>> char_index_list("aabaabaacca", 'b')
        [2, 5]
        >>> char_index_list("aabaabaacca", 'c')
        [8, 9]
        >>> char_index_list("aabaabaacca", 'e')
        []
    """
    list_index = []
    for x in range(len(s)):
        if s[x] == c:
            list_index.append(x)
    return list_index

if __name__ == '__main__':
    import doctest
    doctest.testmod()
