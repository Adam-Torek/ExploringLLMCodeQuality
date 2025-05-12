"""
Write a function to remove all the words with k length in the given string.
assert remove_length('The person is most value tet', 3) == 'person is most value'
"""

def remove_length(string, k):
    """
    :param string: string
    :param k: int
    :return: string
    """
    # split the string into a list
    string_list = string.split()
    # remove all the words with k length
    string_list = [word for word in string_list if len(word) != k]
    # join the list back into a string
    string = ' '.join(string_list)
    return string


# test the function
assert remove_length('The person is most value tet', 3) == 'person is most value'