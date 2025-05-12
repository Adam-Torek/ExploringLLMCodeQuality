"""
Write a function that takes in a list of tuples and returns a dictionary mapping each unique tuple to the number of times it occurs in the list.
assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)] ) == {(1, 3): 2, (2, 5): 2, (3, 6): 1}
"""


def check_occurences(tuples):
    """
    :param tuples: list of tuples
    :return: dictionary mapping each unique tuple to the number of times it occurs in the list
    """
    result = {}
    for tuple in tuples:
        if tuple in result:
            result[tuple] += 1
        else:
            result[tuple] = 1
    return result


if __name__ == '__main__':
    print(check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]))
    print(check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3), (3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]))
    print(check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3), (3, 1), (1, 3), (2, 5), (5, 2), (6, 3), (3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]))
    print(check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3), (3, 1), (1, 3), (2, 5), (5, 2), (6, 3), (3, 1), (1, 3), (2, 5), (5, 2), (6, 3), (3, 1), (1, 3), (2, 5), (5, 2), (6, 3), (3, 1), (1, 3), (2, 5), (5, 2), (6, 3), (3, 1), (1, 3), (2, 5), (5, 2), (6, 3), (3, 1), (1, 3), (2, 5), (5, 2), (6, 3), (3, 1), (1, 3), (2, 5), (5, 2), (6, 3), (3, 1), (1, 3), (2, 5), (5, 2), (6, 3), (3, 1), (1, 3), (2, 5), (5, 2), (6, 3), (3, 1), (1, 3), (2, 5), (5, 2), (6, 3), (3, 1), (1, 3), (2, 5), (5, 2), (6, 3), (3, 1), (1, 3), (2, 5), (5, 2), (6, 3), (3, 1), (1, 3), (2, 5), (5, 2), (6, 3), (3, 1), (1, 3), (2, 5), (5, 2), (6, 3), (3, 1), (1, 3), (2, 5), (5, 2), (6, 3), (3, 1), (1, 3), (2, 5), (5, 2), (6, 3), (3, 1), (1, 3), (2, 5), (5, 2), (6, 3), (3, 1), (1, 3), (2, 5), (5, 2), (6, 3), (3, 1), (1, 3), (2, 5),