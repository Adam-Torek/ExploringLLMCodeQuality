"""
Write a python function to find the length of the longest word.
assert len_log(["python","PHP","bigdata"]) == 7
"""
def len_log(str_list):
    """
    Function to find the length of the longest word in a given list of strings.

    Parameters:
    str_list (list): List of strings.

    Returns:
    int: The length of the longest word in the given list.
    """
    longest_word = ""
    for word in str_list:
        if len(word) > len(longest_word):
            longest_word = word
    return len(longest_word)

assert len_log(["python","PHP","bigdata"]) == 7