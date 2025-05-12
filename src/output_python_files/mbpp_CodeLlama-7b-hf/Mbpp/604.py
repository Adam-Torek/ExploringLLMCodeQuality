"""
Write a function to reverse words seperated by spaces in a given string.
assert reverse_words("python program")==("program python")
"""


def reverse_words(string):
    """
    :param string: string
    :return: reversed string
    """
    return " ".join(string.split()[::-1])


if __name__ == '__main__':
    print(reverse_words("python program"))
    print(reverse_words("hello world"))
    print(reverse_words("hello world how are you"))
    print(reverse_words("hello world how are you doing"))
    print(reverse_words("hello world how are you doing this"))
    print(reverse_words("hello world how are you doing this is a test"))
    print(reverse_words("hello world how are you doing this is a test for your sanity"))
    print(reverse_words("hello world how are you doing this is a test for your sanity and my own"))
    print(reverse_words("hello world how are you doing this is a test for your sanity and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own and my own