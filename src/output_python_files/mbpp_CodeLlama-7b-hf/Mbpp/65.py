"""
Write a function to flatten a list and sum all of its elements.
assert recursive_list_sum(([1, 2, [3,4],[5,6]]))==21
"""


def recursive_list_sum(list_to_sum):
    """
    :param list_to_sum: list
    :return: int
    """
    if not isinstance(list_to_sum, list):
        raise TypeError("list_to_sum must be a list")
    if not list_to_sum:
        return 0
    if isinstance(list_to_sum[0], list):
        return recursive_list_sum(list_to_sum[0]) + recursive_list_sum(list_to_sum[1:])
    else:
        return list_to_sum[0] + recursive_list_sum(list_to_sum[1:])


def iterative_list_sum(list_to_sum):
    """
    :param list_to_sum: list
    :return: int
    """
    if not isinstance(list_to_sum, list):
        raise TypeError("list_to_sum must be a list")
    if not list_to_sum:
        return 0
    sum_list = 0
    for item in list_to_sum:
        if isinstance(item, list):
            sum_list += iterative_list_sum(item)
        else:
            sum_list += item
    return sum_list


def main():
    print(recursive_list_sum([1, 2, [3, 4], [5, 6]]))
    print(iterative_list_sum([1, 2, [3, 4], [5, 6]]))


if __name__ == '__main__':
    main()