"""
Write a function to remove uneven elements in the nested mixed tuple.
assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
"""


def extract_even(t):
    if isinstance(t, tuple):
        return tuple(extract_even(x) for x in t if isinstance(x, tuple) or x % 2 == 0)
    else:
        return t


if __name__ == '__main__':
    print(extract_even((4, 5, (7, 6, (2, 4)), 6, 8)))
    print(extract_even((4, 5, (7, 6, (2, 4)), 6, 8, 9)))
    print(extract_even((4, 5, (7, 6, (2, 4)), 6, 8, 9, 10)))
    print(extract_even((4, 5, (7, 6, (2, 4)), 6, 8, 9, 10, 11)))
    print(extract_even((4, 5, (7, 6, (2, 4)), 6, 8, 9, 10, 11, 12)))
    print(extract_even((4, 5, (7, 6, (2, 4)), 6, 8, 9, 10, 11, 12, 13)))
    print(extract_even((4, 5, (7, 6, (2, 4)), 6, 8, 9, 10, 11, 12, 13, 14)))
    print(extract_even((4, 5, (7, 6, (2, 4)), 6, 8, 9, 10, 11, 12, 13, 14, 15)))
    print(extract_even((4, 5, (7, 6, (2, 4)), 6, 8, 9, 10, 11, 12, 13, 14, 15, 16)))
    print(extract_even((4, 5, (7, 6, (2, 4)), 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17)))
    print(extract_even((4, 5, (7, 6, (2, 4)), 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18)))
    print(extract_even((4, 5, (7, 6, (2, 4)), 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)))
    print(extract_even((4, 5, (7, 6, (2, 4)), 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)))
    print(extract_even((4, 5, (7, 6, (2, 4)), 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21)))
    print(extract_even((4, 5, (7, 6, (2, 4)), 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22)))
    print(extract_even((4, 5