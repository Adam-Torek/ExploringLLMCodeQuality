"""
Write a function that returns the list in a list of lists whose sum of elements is the highest.
assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]
"""
def max_sum_list(lst):
    """
    :param lst: list of lists
    :return: list with the highest sum of elements
    """
    max_sum = sum(lst[0])
    max_sum_index = 0
    for i, sub_lst in enumerate(lst):
        current_sum = sum(sub_lst)
        if current_sum > max_sum:
            max_sum = current_sum
            max_sum_index = i
    return lst[max_sum_index]

assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]
assert max_sum_list([[1,2], [3,4], [5,6]])==[5, 6]
assert max_sum_list([[1], [2], [3]])==[3]
assert max_sum_list([]) is None
assert max_sum_list([[1], [2], [3], [4]])==[4]