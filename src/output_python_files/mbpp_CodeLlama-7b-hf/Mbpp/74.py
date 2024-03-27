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
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "a"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "a"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "c"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c", "a"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c", "b"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c", "c"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c", "d"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "b"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "c"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c", "c"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c", "d"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "b", "a"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "b", "c"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "c", "c"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "c", "d"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c", "c", "a"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c", "c", "b"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c", "c", "c"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c", "c", "d"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c", "d", "a"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c", "d", "b"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c", "d", "c"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "c", "d", "d"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "b", "b", "a"]))
    print(is_samepatterns(["red", "green", "green"], ["a", "b", "b", "b", "b",