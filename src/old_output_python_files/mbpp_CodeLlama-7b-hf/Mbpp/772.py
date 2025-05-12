"""
Write a function to remove all the words with k length in the given string.
assert remove_length('The person is most value tet', 3) == 'person is most value'
"""


def remove_length(string, k):
    """
    :param string: string to remove words from
    :param k: length of words to remove
    :return: string with words of length k removed
    """
    words = string.split()
    new_words = []
    for word in words:
        if len(word) != k:
            new_words.append(word)
    return ' '.join(new_words)


if __name__ == '__main__':
    print(remove_length('The person is most value tet', 3))
    print(remove_length('The person is most value tet', 4))
    print(remove_length('The person is most value tet', 5))
    print(remove_length('The person is most value tet', 6))
    print(remove_length('The person is most value tet', 7))
    print(remove_length('The person is most value tet', 8))
    print(remove_length('The person is most value tet', 9))
    print(remove_length('The person is most value tet', 10))
    print(remove_length('The person is most value tet', 11))
    print(remove_length('The person is most value tet', 12))
    print(remove_length('The person is most value tet', 13))
    print(remove_length('The person is most value tet', 14))
    print(remove_length('The person is most value tet', 15))
    print(remove_length('The person is most value tet', 16))
    print(remove_length('The person is most value tet', 17))
    print(remove_length('The person is most value tet', 18))
    print(remove_length('The person is most value tet', 19))
    print(remove_length('The person is most value tet', 20))
    print(remove_length('The person is most value tet', 21))
    print(remove_length('The person is most value tet', 22))
    print(remove_length('The person is most value tet', 23))
    print(remove_length('The person is most value tet', 24))
    print(remove_length('The person is most value tet', 25))
    print(remove_length('The person is most value tet', 26))
    print(remove_length('The person is most value tet', 27))
    print(remove_length('The person is most value tet', 28))
    print(remove_length('The person is most value tet', 29))
    print(remove_length('The person is most value tet', 30))
    print(remove_length('The person is most value tet', 31))
    print(remove_length('The person is most value tet', 32))
    print(remove_length('The person is most value tet', 33))
    print(remove_length('The person is most value tet', 34))
    print(remove_length('The person is most value tet', 35))
    print(remove_length('The person is most value tet', 36))
    print(remove_length('The person is most value tet', 37))
    print(remove_length('The person is most value tet', 38))
    print(remove_length('The person is most value tet', 39))
    print(remove_length('The person is most value tet', 40))
    print(remove_length('The person is most value tet', 41))
    print(remove_length('The person is most value tet', 42))
    print(remove_length('The person is most value tet', 43))
    print(remove_length('The person is most value tet', 44))
    print(remove_length('The person is most value tet', 45))
    print(remove_length