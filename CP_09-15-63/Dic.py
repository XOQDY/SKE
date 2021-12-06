# eng2sp = dict()
# print(eng2sp)
# eng2sp['one'] = 'uno'
# print(eng2sp)
# eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
# print(eng2sp)
# print(eng2sp['one'])
# print(eng2sp['two'])
# print(eng2sp['three'])
# print(len(eng2sp))
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


hist = histogram('parrot')
print(hist)
inverse = invert_dict(hist)
print(inverse)
