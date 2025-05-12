"""
Write a function to find frequency of each element in a flattened list of lists, returned in a dictionary.
assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]])=={1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
"""

def frequency_lists(list_of_lists):
    """
    :param list_of_lists:
    :return:
    """
    flat_list = [item for sublist in list_of_lists for item in sublist]
    return {item: flat_list.count(item) for item in flat_list}


def frequency_lists_2(list_of_lists):
    """
    :param list_of_lists:
    :return:
    """
    return {item: sum([item in sublist for sublist in list_of_lists]) for item in set([item for sublist in list_of_lists for item in sublist])}


def frequency_lists_3(list_of_lists):
    """
    :param list_of_lists:
    :return:
    """
    return {item: sum([item in sublist for sublist in list_of_lists]) for item in set(sum(list_of_lists, []))}


def frequency_lists_4(list_of_lists):
    """
    :param list_of_lists:
    :return:
    """
    return {item: sum([item in sublist for sublist in list_of_lists]) for item in set(sum(list_of_lists, []))}


def frequency_lists_5(list_of_lists):
    """
    :param list_of_lists:
    :return:
    """
    return {item: sum([item in sublist for sublist in list_of_lists]) for item in set(sum(list_of_lists, []))}


def frequency_lists_6(list_of_lists):
    """
    :param list_of_lists:
    :return:
    """
    return {item: sum([item in sublist for sublist in list_of_lists]) for item in set(sum(list_of_lists, []))}


def frequency_lists_7(list_of_lists):
    """
    :param list_of_lists:
    :return:
    """
    return {item: sum([item in sublist for sublist in list_of_lists]) for item in set(sum(list_of_lists, []))}


def frequency_lists_8(list_of_lists):
    """
    :param list_of_lists:
    :return:
    """
    return {item: sum([item in sublist for sublist in list_of_lists]) for item in set(sum(list_of_lists, []))}


def frequency_lists_9(list_of_lists):
    """
    :param list_of_lists:
    :return:
    """
    return {item: sum([item in sublist for sublist in list_of_lists]) for item in set(sum(list_of_lists, []))}


def frequency_lists_10(list_of_lists):
    """
    :param list_of_lists:
    :return:
    """
    return {item: sum([item in sublist for sublist in list_of_lists]) for item in set(sum(list_of_lists, []))}


def frequency_lists_11(list_of_lists):
    """
    :param list_of_lists:
    :return:
    """
    return {item: sum([item in sublist for sublist in list_of_lists]) for item in set(sum(list_of_lists, []))}


def frequency_lists_12(list_of_lists):
    """
    :param list_of_lists:
    :return:
    """
    return {item: sum([item in sublist for sublist in list_of_lists]) for item in set(sum(list_of_lists, []))}


def frequency_lists_13(list_of_lists):
    """
    :param list_of_lists:
    :return:
    """
    return {item: sum([item in sublist for sublist in list_of_lists]) for item in set(sum(list_of_lists, []))}


def