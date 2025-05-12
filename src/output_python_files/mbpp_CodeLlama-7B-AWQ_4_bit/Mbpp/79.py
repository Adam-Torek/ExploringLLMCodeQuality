"""
Write a python function to check whether the length of the word is odd or not.
assert word_len("Hadoop") == False
"""


def word_len(word):
    """
    :param word: str
    :return: bool
    """
    if len(word) % 2 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(word_len("Hadoop"))
    print(word_len("