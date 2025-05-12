"""
Write a function that takes in two lists and replaces the last element of the first list with the elements of the second list.
assert replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8])==[1, 3, 5, 7, 9, 2, 4, 6, 8]
"""


def replace_list(list1, list2):
    """
    :param list1: list of numbers
    :param list2: list of numbers
    :return: list of numbers
    """
    list1[-1] = list2[0]
    for i in range(1, len(list2)):
        list1.append(list2[i])
    return list1


print(replace_list([1, 3, 5, 7, 9, 10], [2, 4, 6, 8]))
print(replace_list([1, 3, 5, 7, 9, 10], [2, 4, 6, 8, 10]))
print(replace_list([1, 3, 5, 7, 9, 10], [2, 4, 6, 8, 10, 12]))
print(replace_list([1, 3, 5, 7, 9, 10], [2, 4, 6, 8, 10, 12, 14]))
print(replace_list([1, 3, 5, 7, 9, 10], [2, 4, 6, 8, 10, 12, 14, 16]))
print(replace_list([1, 3, 5, 7, 9, 10], [2, 4, 6, 8, 10, 12, 14, 16, 18]))
print(replace_list([1, 3, 5, 7, 9, 10], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]))
print(replace_list([1, 3, 5, 7, 9, 10], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]))
print(replace_list([1, 3, 5, 7, 9, 10], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]))
print(replace_list([1, 3, 5, 7, 9, 10], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26]))
print(replace_list([1, 3, 5, 7, 9, 10], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]))
print(replace_list([1, 3, 5, 7, 9, 10], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]))
print(replace_list([1, 3, 5, 7, 9, 10], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]))
print(replace_list([1, 3, 5, 7, 9, 10], [2, 4, 6, 8, 10,