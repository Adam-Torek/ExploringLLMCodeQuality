"""
Write a function to count the total number of characters in a string.
assert count_charac("python programming")==18
"""
def count_charac(string):
    """
    Function to count the total number of characters in a string
    :param string: string to count the characters of
    :return: int, the total number of characters in the string
    """
    return len(string)

assert count_charac("python programming") == 18