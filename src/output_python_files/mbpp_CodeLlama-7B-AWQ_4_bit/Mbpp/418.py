"""
Write a python function to find the element of a list having maximum length.
assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
"""


def Find_Max(lst):
    """
    :param lst: list of lists
    :return: list with maximum length
    """
    max_len = 0
    max_len_list = []
    for i in lst:
        if len(i) > max_len:
            max_len = len(i)
            max_len_list = i
    return max_len_list


if __name__ == '__main__':
    print(Find_Max([['A'], ['A', 'B'], ['A', 'B', 'C']]))
    print(Find_Max([['A', 'B'], ['A', 'B', 'C'], ['A', 'B', 'C', 'D']]))
    print(Find_Max([['A', 'B', 'C'], ['A', 'B', 'C', 'D'], ['A', 'B', 'C', 'D', 'E']]))
    print(Find_Max([['A', 'B', 'C', 'D'], ['A', 'B', 'C', 'D', 'E'], ['A', 'B', 'C', 'D', 'E', 'F']]))
    print(Find_Max([['A', 'B', 'C', 'D', 'E'], ['A', 'B', 'C', 'D', 'E', 'F'], ['A', 'B', 'C', 'D', 'E', 'F', 'G']]))
    print(Find_Max([['A', 'B', 'C', 'D', 'E', 'F'], ['A', 'B', 'C', 'D', 'E', 'F', 'G'], ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']]))
    print(Find_Max([['A', 'B', 'C', 'D', 'E', 'F', 'G'], ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'], ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']]))
    print(Find_Max([['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'], ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']]))
    print(Find_Max([['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']]))
    print(Find_Max([['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'], ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']]))
    print(Find_Max([['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'], ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'], ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']]))
    print(Find_Max([['A', 'B', 'C', 'D',