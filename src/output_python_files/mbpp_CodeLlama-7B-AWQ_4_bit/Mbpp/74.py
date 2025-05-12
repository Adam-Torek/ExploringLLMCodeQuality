"""
Write a function to check whether it follows the sequence given in the patterns array.
assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
"""


def is_samepatterns(patterns, words):
    if len(patterns) != len(words):
        return False
    for i in range(len(patterns)):
        if patterns[i] != words[i] and patterns[i] != words[i][0]:
            return False
    return True


if __name__ == '__main__':
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "b"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "c"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "b", "b"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "b", "c"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "b", "b", "b"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "b", "b", "c"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "b", "b", "b", "b"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "b", "b", "b", "c"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "b", "b", "b", "b", "b"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "b", "b", "b", "b", "c"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "b", "b", "b", "b", "b", "b"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "b", "b", "b", "b", "b", "c"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "b", "b", "b", "b", "b", "b", "c"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "c"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "c"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b",