"""
Write a function to return two words from a list of words starting with letter 'p'.
assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
"""


def start_withp(words):
    """
    :param words: list of words
    :return: tuple of two words starting with letter 'p'
    """
    for word in words:
        if word[0] == 'p':
            return word.split()


if __name__ == '__main__':
    print(start_withp(["Python PHP", "Java JavaScript", "c c++"]))
    print(start_withp(["Python PHP", "Java JavaScript", "c c++", "p ppp"]))
    print(start_withp(["Python PHP", "Java JavaScript", "c c++", "p ppp", "p pppp"]))
    print(start_withp(["Python PHP", "Java JavaScript", "c c++", "p ppp", "p pppp", "p ppppp"]))
    print(start_withp(["Python PHP", "Java JavaScript", "c c++", "p ppp", "p pppp", "p ppppp", "p pppppp"]))
    print(start_withp(["Python PHP", "Java JavaScript", "c c++", "p ppp", "p pppp", "p ppppp", "p pppppp", "p ppppppp"]))
    print(start_withp(["Python PHP", "Java JavaScript", "c c++", "p ppp", "p pppp", "p ppppp", "p pppppp", "p ppppppp", "p pppppppp"]))
    print(start_withp(["Python PHP", "Java JavaScript", "c c++", "p ppp", "p pppp", "p ppppp", "p pppppp", "p ppppppp", "p pppppppp", "p ppppppppp"]))
    print(start_withp(["Python PHP", "Java JavaScript", "c c++", "p ppp", "p pppp", "p ppppp", "p pppppp", "p ppppppp", "p pppppppp", "p ppppppppp", "p pppppppppp"]))
    print(start_withp(["Python PHP", "Java JavaScript", "c c++", "p ppp", "p pppp", "p ppppp", "p pppppp", "p ppppppp", "p pppppppp", "p ppppppppp", "p pppppppppp", "p ppppppppppp"]))
    print(start_withp(["Python PHP", "Java JavaScript", "c c++", "p ppp", "p pppp", "p ppppp", "p pppppp", "p ppppppp", "p pppppppp", "p ppppppppp", "p pppppppppp", "p ppppppppppp", "p pppppppppppp"]))
    print(start_withp(["Python PHP", "Java JavaScript", "c c++", "p ppp", "p pppp", "p ppppp", "p pppppp", "p ppppppp", "p pppppppp", "p ppppppppp", "p pppppppppp", "p ppppppppppp", "p pppppppppppp", "p ppppppppppppp"]))
    print(start_withp(["Python PHP", "Java JavaScript", "c c++", "p ppp", "p pppp", "p ppppp", "p pppppp", "p ppppppp", "p pppppppp", "p ppppppppp", "p pppppppppp", "p ppppppppppp", "p pppppppppppp", "p ppppppppppppp", "p pppppppppppppp"]))