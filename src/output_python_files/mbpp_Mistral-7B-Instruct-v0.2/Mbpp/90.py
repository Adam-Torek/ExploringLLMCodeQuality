"""
Write a python function to find the length of the longest word.
assert len_log(["python","PHP","bigdata"]) == 7
"""
def len_log(lst):
    """
    This function takes a list of strings as an argument and returns the length of the longest string in the list.

    :param lst: list of strings
    :return: int, the length of the longest string in the list
    """
    longest_string = ""
    for string in lst:
        if len(string) > len(longest_string):
            longest_string = string
    return len(longest_string)

assert len_log(["python","PHP","bigdata"]) == 7
print(len_log(["python","PHP","bigdata"]))