"""
Write a python function to interchange the first and last elements in a list.
assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
"""
def swap_list(input_list):
    """
    This function takes a list as an argument and returns a new list with the first and last elements interchanged.
    """
    if len(input_list) < 2:
        return input_list

    first = input_list[0]
    last = input_list[-1]

    return [last] + input_list[1:-1] + [first]

assert swap_list([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
assert swap_list([]) == []
assert swap_list([1]) == [1]
assert swap_list([1, 2]) == [2, 1]