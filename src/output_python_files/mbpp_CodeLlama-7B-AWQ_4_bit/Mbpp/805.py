"""
Write a function that returns the list in a list of lists whose sum of elements is the highest.
assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]
"""


def max_sum_list(list_of_lists):
    """
    :param list_of_lists: list of lists
    :return: list of lists with the highest sum of elements
    """
    max_sum = 0
    max_sum_list = []
    for i in list_of_lists:
        sum_list = 0
        for j in i:
            sum_list += j
        if sum_list > max_sum:
            max_sum = sum_list
            max_sum_list = i
    return max_sum_list


print(max_sum_list([[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]))
print(max_sum_list([[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9], [1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]))
print(max_sum_list([[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9], [1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9],
                    [1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9], [1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9],
                    [1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9], [1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9],
                    [1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9], [1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9],
                    [1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9], [1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9],
                    [1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9], [1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9],
                    [1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9], [1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9],
                    [1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9], [1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9],
                    [1, 2, 3], [4, 5