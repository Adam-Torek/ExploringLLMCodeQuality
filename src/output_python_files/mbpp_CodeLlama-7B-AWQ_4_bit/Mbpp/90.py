"""
Write a python function to find the length of the longest word.
assert len_log(["python","PHP","bigdata"]) == 7
"""


def len_log(words):
    """
    :param words: list of words
    :return: length of the longest word
    """
    return max(len(word) for word in words)


if __name__ == '__main__':
    print(len_log(["python", "PHP", "bigdata"]))
    print(len_log(["python", "PHP", "bigdata", "data", "data", "data", "data", "data", "data", "data", "data", "data",
                   "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data",
                   "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data",
                   "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data",
                   "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data",
                   "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data",
                   "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data",
                   "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data",
                   "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data",
                   "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data",
                   "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data",
                   "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data",
                   "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data",
                   "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data",
                   "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data",
                   "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data",
                   "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data",
                   "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data",
                   "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data",
                   "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data",
                   "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data",
                   "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data", "data",
                   "data", "data", "data", "data", "data", "data", "data", "