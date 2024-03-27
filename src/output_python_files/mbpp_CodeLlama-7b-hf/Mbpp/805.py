"""
Write a function that returns the list in a list of lists whose sum of elements is the highest.
assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]
"""


def max_sum_list(list_of_lists):
    """
    :param list_of_lists: list of lists
    :return: list with the highest sum of elements
    """
    max_sum = 0
    max_sum_list = []
    for list_ in list_of_lists:
        sum_ = 0
        for element in list_:
            sum_ += element
        if sum_ > max_sum:
            max_sum = sum_
            max_sum_list = list_
    return max_sum_list


if __name__ == '__main__':
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
                        [1,