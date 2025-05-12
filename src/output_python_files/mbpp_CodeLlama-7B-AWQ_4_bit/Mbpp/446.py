"""
Write a python function to count the occurence of all elements of list in a tuple.
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3
"""


def count_Occurrence(tuple, list):
    """
    Write a python function to count the occurence of all elements of list in a tuple.
    assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3
    """
    count = 0
    for i in list:
        for j in tuple:
            if i == j:
                count += 1
    return count


if __name__ == '__main__':
    print(count_Occurrence(('a', 'a', 'c', 'b', 'd'), ['a', 'b']))
    print(count_Occurrence(('a', 'a', 'c', 'b', 'd'), ['a', 'b', 'c']))
    print(count_Occurrence(('a', 'a', 'c', 'b', 'd'), ['a', 'b', 'c', 'd']))
    print(count_Occurrence(('a', 'a', 'c', 'b', 'd'), ['a', 'b', 'c', 'd', 'e']))
    print(count_Occurrence(('a', 'a', 'c', 'b', 'd'), ['a', 'b', 'c', 'd', 'e', 'f']))
    print(count_Occurrence(('a', 'a', 'c', 'b', 'd'), ['a', 'b', 'c', 'd', 'e', 'f', 'g']))
    print(count_Occurrence(('a', 'a', 'c', 'b', 'd'), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']))
    print(count_Occurrence(('a', 'a', 'c', 'b', 'd'), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']))
    print(count_Occurrence(('a', 'a', 'c', 'b', 'd'), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']))
    print(count_Occurrence(('a', 'a', 'c', 'b', 'd'), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']))
    print(count_Occurrence(('a', 'a', 'c', 'b', 'd'), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']))
    print(count_Occurrence(('a', 'a', 'c', 'b', 'd'), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']))
    print(count_Occurrence(('a', 'a', 'c', 'b', 'd'), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']))
    print(count_Occurrence(('a', 'a', 'c', 'b', 'd'), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']))
    print(count_Occurrence(('a', 'a', 'c', 'b', 'd'), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']))
    print(count_Occurrence(('a', 'a', 'c', 'b', 'd'), ['a',