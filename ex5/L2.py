def replace_first_occurrence(s, pattern1, pattern2):
    for x in range(len(s)):
        if s[x:x + len(pattern1)] == pattern1:
            s = s[0:x] + pattern2 + s[x + len(pattern1):-1]
            break
    return s


print(replace_first_occurrence('good bad good bad', 'bad', 'good'))
print(replace_first_occurrence('good good good good', 'bad', 'good'))
print(replace_first_occurrence('aaaaa aaa', 'aa', 'zxz'))
print(replace_first_occurrence('bbab baa', 'aa', 'zxz'))
print(replace_first_occurrence('bbaaabbaaaabcccaa', 'aa', 'zxz'))
print()


def remove_adjacent_duplicates(int_list):
    result_list = []
    for x in range(len(int_list)):
        if int_list[x] not in result_list:
            result_list.append(int_list[x])
    return result_list


print(remove_adjacent_duplicates([1, 1, 5, 5, 10, 8, 7, 5, 5, 5, 12, 4, 12, 12]))
print(remove_adjacent_duplicates([1, 1, 1, 1, 2, 5, 5, 5, 3]))
print(remove_adjacent_duplicates([12, 12, 12]))
print(remove_adjacent_duplicates([1, 2, 3]))
print(remove_adjacent_duplicates([]))
print()
