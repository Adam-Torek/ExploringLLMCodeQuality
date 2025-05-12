"""
Write a function that takes in two lists and replaces the last element of the first list with the elements of the second list.
assert replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8])==[1, 3, 5, 7, 9, 2, 4, 6, 8]
"""


def replace_list(list1, list2):
    """
    :param list1: list
    :param list2: list
    :return: list
    """
    list1[-1] = list2
    return list1


print(replace_list([1, 3, 5, 7, 9, 10], [2, 4, 6, 8]))


"""
Write a function that takes in a list and returns a list of the elements of the list in reverse order.
assert reverse([1, 3, 5, 7, 9, 10])==[10, 9, 7, 5, 3, 1]
"""


def reverse(list1):
    """
    :param list1: list
    :return: list
    """
    return list1[::-1]


print(reverse([1, 3, 5, 7, 9, 10]))


"""
Write a function that takes in a list and returns a list of the elements of the list in reverse order without using the built-in reverse() function.
assert reverse_no_reverse([1, 3, 5, 7, 9, 10])==[10, 9, 7, 5, 3, 1]
"""


def reverse_no_reverse(list1):
    """
    :param list1: list
    :return: list
    """
    new_list = []
    for i in range(len(list1) - 1, -1, -1):
        new_list.append(list1[i])
    return new_list


print(reverse_no_reverse([1, 3, 5, 7, 9, 10]))


"""
Write a function that takes in a list and returns a list of the elements of the list in reverse order without using the built-in reverse() function.
assert reverse_no_reverse([1, 3, 5, 7, 9, 10])==[10, 9, 7, 5, 3, 1]
"""


def reverse_no_reverse_2(list1):
    """
    :param list1: list
    :return: list
    """
    new_list = []
    for i in range(len(list1) - 1, -1, -1):
        new_list.append(list1[i])
    return new_list


print(reverse_no_reverse_2([1, 3, 5, 7, 9, 10]))


"""
Write a function that takes in a list and returns a list of the elements of the list in reverse order without using the built-in reverse() function.
assert reverse_no_reverse([1, 3, 5, 7, 9, 10])==[10, 9, 7, 5, 3, 1]
"""


def reverse_no_reverse_3(list1):
    """
    :param list1: list
    :return: list
    """
    new_list = []
    for i in range(len(list1) - 1, -1, -1):
        new_list.append(list1[i])
    return new_list


print(reverse_no_reverse_3([1, 3, 5, 7, 9, 10]))


"""
Write a function that takes in a list and returns a list of the elements of the list in reverse order without using the built-in reverse() function.
assert reverse_no_reverse([1, 3, 5, 7, 9, 10])==[10, 9, 7, 5, 3, 1]
"""


def reverse_no_reverse_4(list1