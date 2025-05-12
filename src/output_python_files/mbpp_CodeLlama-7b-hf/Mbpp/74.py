"""
Write a function to check whether it follows the sequence given in the patterns array.
assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
"""


def is_samepatterns(patterns, words):
    if len(patterns) != len(words):
        return False
    for i in range(len(patterns)):
        if patterns[i] != words[i] * len(patterns[i]):
            return False
    return True


if __name__ == '__main__':
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "a"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "b"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "a"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c", "d"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "a", "b"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "a", "b", "a"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c", "d", "e", "f"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "a", "b", "a", "b"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "a", "b", "a", "b", "a"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c", "d", "e", "f", "g", "h"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "a", "b", "a", "b", "a", "b"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "a", "b", "a", "b", "a", "b", "a"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "a", "b", "a", "b", "a", "b", "a", "b"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "a", "b", "a", "b", "a", "b", "a", "b", "a"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "a", "b", "a", "b", "a", "b", "a", "b", "a", "b"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "a", "b", "a", "b", "a", "b", "a", "b", "a", "b", "a"]))
    print(is_samepatterns(["red", "green", "green"], ["a",