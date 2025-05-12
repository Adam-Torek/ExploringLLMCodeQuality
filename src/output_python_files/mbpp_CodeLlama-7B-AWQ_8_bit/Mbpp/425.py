"""
Write a function to count the number of sublists containing a particular element.
assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3
"""


def count_element_in_list(lst, element):
    """
    :param lst: list of lists
    :param element: element to count
    :return: number of sublists containing element
    """
    count = 0
    for sublist in lst:
        if element in sublist:
            count += 1
    return count


if __name__ == '__main__':
    print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 1))
    print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 5))
    print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 11))
    print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 7))
    print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 15))
    print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 10))
    print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 16))
    print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 17))
    print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 18))
    print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 19))
    print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 20))
    print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 21))
    print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 22))
    print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 23))
    print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 24))
    print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 25))
    print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 26))
    print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 27))
    print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 28))
    print(count_element_in_list([