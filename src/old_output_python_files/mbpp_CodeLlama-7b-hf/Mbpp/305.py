"""
Write a function to return two words from a list of words starting with letter 'p'.
assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
"""


def start_withp(words):
    """
    :param words: list of words
    :return: tuple of two words starting with letter 'p'
    """
    return tuple(word for word in words if word.startswith('p'))


if __name__ == '__main__':
    print(start_withp(["Python PHP", "Java JavaScript", "c c++"]))
    print(start_withp(["Python PHP", "Java JavaScript", "c c++", "Python PHP"]))
    print(start_withp(["Python PHP", "Java JavaScript", "c c++", "Python PHP", "Python PHP"]))
    print(start_withp(["Python PHP", "Java JavaScript", "c c++", "Python PHP", "Python PHP", "Python PHP"]))
    print(start_withp(["Python PHP", "Java JavaScript", "c c++", "Python PHP", "Python PHP", "Python PHP", "Python PHP"]))
    print(start_withp(["Python PHP", "Java JavaScript", "c c++", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP"]))
    print(start_withp(["Python PHP", "Java JavaScript", "c c++", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP"]))
    print(start_withp(["Python PHP", "Java JavaScript", "c c++", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP"]))
    print(start_withp(["Python PHP", "Java JavaScript", "c c++", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP"]))
    print(start_withp(["Python PHP", "Java JavaScript", "c c++", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP"]))
    print(start_withp(["Python PHP", "Java JavaScript", "c c++", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP"]))
    print(start_withp(["Python PHP", "Java JavaScript", "c c++", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP"]))
    print(start_withp(["Python PHP", "Java JavaScript", "c c++", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP"]))
    print(start_withp(["Python PHP", "Java JavaScript", "c c++", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP"]))
    print(start_withp(["Python PHP", "Java JavaScript", "c c++", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP"]))
    print(start_withp(["Python PHP", "Java JavaScript", "c c++", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP"]))
    print(start_withp(["Python PHP", "Java JavaScript", "c c++", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP", "Python PHP