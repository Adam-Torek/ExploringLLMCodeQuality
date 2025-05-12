"""
Write a function to check whether it follows the sequence given in the patterns array.
assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
"""


def is_samepatterns(patterns, strings):
    if len(patterns) != len(strings):
        return False
    for i in range(len(patterns)):
        if patterns[i] != strings[i]:
            return False
    return True


if __name__ == '__main__':
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "a"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "b"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "c"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c", "c"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c", "d"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c", "d", "e"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c", "d", "e", "f"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c", "d", "e", "f", "g"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c", "d", "e", "f", "g", "h"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c", "d", "e", "f", "g", "h", "i"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p