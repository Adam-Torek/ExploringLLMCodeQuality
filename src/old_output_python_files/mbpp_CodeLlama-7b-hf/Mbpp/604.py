"""
Write a function to reverse words seperated by spaces in a given string.
assert reverse_words("python program")==("program python")
"""


def reverse_words(string):
    """
    Reverse words in a string
    :param string: string to reverse
    :return: reversed string
    """
    return " ".join(string.split()[::-1])


if __name__ == '__main__':
    print(reverse_words("python program"))
    print(reverse_words("python program is fun"))
    print(reverse_words("python program is fun and easy"))
    print(reverse_words("python program is fun and easy to use"))
    print(reverse_words("python program is fun and easy to use and easy to learn"))
    print(reverse_words("python program is fun and easy to use and easy to learn and easy to master"))
    print(reverse_words("python program is fun and easy to use and easy to learn and easy to master and easy to master"))
    print(reverse_words("python program is fun and easy to use and easy to learn and easy to master and easy to master and easy to master"))
    print(reverse_words("python program is fun and easy to use and easy to learn and easy to master and easy to master and easy to master and easy to master"))
    print(reverse_words("python program is fun and easy to use and easy to learn and easy to master and easy to master and easy to master and easy to master and easy to master"))
    print(reverse_words("python program is fun and easy to use and easy to learn and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master"))
    print(reverse_words("python program is fun and easy to use and easy to learn and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master"))
    print(reverse_words("python program is fun and easy to use and easy to learn and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master"))
    print(reverse_words("python program is fun and easy to use and easy to learn and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master"))
    print(reverse_words("python program is fun and easy to use and easy to learn and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master"))
    print(reverse_words("python program is fun and easy to use and easy to learn and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master"))
    print(reverse_words("python program is fun and easy to use and easy to learn and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master"))
    print(reverse_words("python program is fun and easy to use and easy to learn and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master"))
    print(reverse_words("python program is fun and easy to use and easy to learn and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master"))
    print(reverse_words("python program is fun and easy to use and easy to learn and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master and easy to master"))
    print(reverse_words("python program is fun and easy to use and easy to learn and easy to master and easy to master and easy