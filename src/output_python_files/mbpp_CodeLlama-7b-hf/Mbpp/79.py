"""
Write a python function to check whether the length of the word is odd or not.
assert word_len("Hadoop") == False
"""


def word_len(word):
    if len(word) % 2 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(word_len("Hadoop"))
    print(word_len("Hadoop1"))
    print(word_len("Hadoop12"))
    print(word_len("Hadoop123"))
    print(word_len("Hadoop1234"))
    print(word_len("Hadoop12345"))
    print(word_len("Hadoop123456"))
    print(word_len("Hadoop1234567"))
    print(word_len("Hadoop12345678"))
    print(word_len("Hadoop123456789"))
    print(word_len("Hadoop1234567890"))
    print(word_len("Hadoop12345678901"))
    print(word_len("Hadoop123456789012"))
    print(word_len("Hadoop1234567890123"))
    print(word_len("Hadoop12345678901234"))
    print(word_len("Hadoop123456789012345"))
    print(word_len("Hadoop1234567890123456"))
    print(word_len("Hadoop12345678901234567"))
    print(word_len("Hadoop123456789012345678"))
    print(word_len("Hadoop1234567890123456789"))
    print(word_len("Hadoop12345678901234567890"))
    print(word_len("Hadoop123456789012345678901"))
    print(word_len("Hadoop1234567890123456789012"))
    print(word_len("Hadoop12345678901234567890123"))
    print(word_len("Hadoop123456789012345678901234"))
    print(word_len("Hadoop1234567890123456789012345"))
    print(word_len("Hadoop12345678901234567890123456"))
    print(word_len("Hadoop123456789012345678901234567"))
    print(word_len("Hadoop1234567890123456789012345678"))
    print(word_len("Hadoop12345678901234567890123456789"))
    print(word_len("Hadoop123456789012345678901234567890"))
    print(word_len("Hadoop1234567890123456789012345678901"))
    print(word_len("Hadoop12345678901234567890123456789012"))