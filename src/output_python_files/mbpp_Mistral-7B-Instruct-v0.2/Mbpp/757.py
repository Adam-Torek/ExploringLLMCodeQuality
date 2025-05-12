"""
Write a function to count the pairs of reverse strings in the given string list. https://www.geeksforgeeks.org/python-program-to-count-the-pairs-of-reverse-strings/
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2
"""
from collections import defaultdict

def count_reverse_pairs(strings):
    """
    :param strings: list of strings
    :return: int
    """
    d = defaultdict(int)
    count = 0
    for s in strings:
        r = s[::-1]
        count += d[r]
        d[s] += 1
    return sum(d.values())

if __name__ == "__main__":
    assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"]) == 2
    assert count_reverse_pairs(["hello", "olleh"]) == 1
    assert count_reverse_pairs(["abba", "baab"]) == 2
    assert count_reverse_pairs(["abba", "baab", "abba"]) == 3
    assert count_reverse_pairs([]) == 0
    assert count_reverse_pairs(["abba"]) == 1
    assert count_reverse_pairs(["abba", "abba"]) == 2
    assert count_reverse_pairs(["abba", "baab", "abba"]) == 3
    assert count_reverse_pairs(["abba", "baab", "abba", "abba"]) == 4
    assert count_reverse_pairs(["abba", "baab", "abba", "abba", "abba"]) == 5
    assert count_reverse_pairs(["abba", "baab", "abba", "abba", "abba", "abba"]) == 6
    assert count_reverse_pairs(["abba", "baab", "abba", "abba", "abba", "abba", "abba"]) == 7
    assert count_reverse_pairs(["abba", "baab", "abba", "abba", "abba", "abba", "abba", "abba"]) == 8
    assert count_reverse_pairs(["abba", "baab", "abba", "abba", "abba", "abba", "abba", "abba", "abba"]) == 9
    assert count_reverse_pairs(["abba", "baab", "abba", "abba", "abba", "abba", "abba", "abba", "abba", "abba"]) == 10
    assert count_reverse_pairs(["abba", "baab", "abba", "abba", "abba", "abba", "abba", "abba", "abba", "abba", "abba"]) == 11
    assert count_reverse_pairs(["abba", "baab", "abba", "abba", "abba", "abba", "abba", "abba", "abba", "abba", "abba", "abba"]) == 12
    assert count_reverse_pairs(["abba", "baab", "abba", "abba", "abba", "abba", "abba", "abba", "abba", "abba", "abba", "abba", "abba"]) == 13
    assert count_reverse_pairs(["abba", "baab", "abba", "abba", "abba", "abba", "abba", "abba", "abba", "abba", "abba", "abba", "abba", "abba"]) == 14
    assert count_reverse_pairs(["abba", "baab", "abba", "abba", "abba", "abba", "abba", "abba", "abba", "abba", "ab