"""
Write a function to find tuples which have all elements divisible by k from the given list of tuples.
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]
"""


def find_tuples(tuples, k):
    return [t for t in tuples if all(x % k == 0 for x in t)]


if __name__ == '__main__':
    print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6))
    print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 3))
    print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 1))
    print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 2))
    print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 4))
    print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 5))
    print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 7))
    print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 8))
    print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 9))
    print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 10))
    print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 11))
    print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 12))
    print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 13))
    print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 14))
    print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 15))
    print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 16))
    print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 17))
    print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 18))
    print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 19))
    print(find_tuples([(6, 24, 12), (7,