"""
Write a function to count the total number of characters in a string.
assert count_charac("python programming")==18
"""

def count_charac(string):
    """
    Count the total number of characters in a string
    :param string: string
    :return: int
    """
    count = 0
    for char in string:
        count += 1
    return count


# assert count_charac("python programming")==18
# print(count_charac("python programming"))