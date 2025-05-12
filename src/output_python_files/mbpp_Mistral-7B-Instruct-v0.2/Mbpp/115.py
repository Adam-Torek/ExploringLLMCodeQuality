"""
Write a function to check whether all dictionaries in a list are empty or not.
assert empty_dit([{},{},{}])==True
"""
def empty_dict(dict_list):
    """
    :param dict_list: list of dictionaries
    :return: boolean value
    """
    return all(len(d) == 0 for d in dict_list)

assert empty_dict([{},{},{}]) == True
assert empty_dict([{'a': 1}, {'b': 2}, {}]) == False