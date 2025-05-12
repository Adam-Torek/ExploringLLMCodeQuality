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
    string = string.split()
    string = [word for word in string if len(word) != k]
    string = ' '.join(string)
    return string


if __name__ == '__main__':
    assert remove_length('The person is most value tet', 3) == 'person is most value'