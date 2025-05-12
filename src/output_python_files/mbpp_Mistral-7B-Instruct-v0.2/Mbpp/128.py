"""
Write a function to find words that are longer than n characters from a given list of words.
assert long_words(3,"python is a programming language")==['python','programming','language']
"""
def long_words(n, string_of_words):
    """
    :param n: int
    :param string_of_words: str
    :return: list
    """
    words = string_of_words.split()
    long_words = [word for word in words if len(word) > n]
    return long_words

assert long_words(3,"python is a programming language")==['python','programming','language']