"""
Write a function to count the pairs of reverse strings in the given string list. https://www.geeksforgeeks.org/python-program-to-count-the-pairs-of-reverse-strings/
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2
"""
from collections import defaultdict

def count_reverse_pairs(strings):
    """
    :param strings: list of strings
    :return: int, number of pairs of reverse strings
    """
    reverse_dict = defaultdict(list)
    count = 0
    for string in strings:
        reverse_string = string[::-1]
        reverse_dict[reverse_string].append(string)
        count += len(reverse_dict[reverse_string]) - 1
    return count // 2

if __name__ == "__main__":
    assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"]) == 2
    assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "racecar"]) == 3
    assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "racecar", "level"]) == 4
    assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "racecar", "level", "radar"]) == 5
    assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "racecar", "level", "radar", "stas"]) == 6
    assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "racecar", "level", "radar", "stas", "stats"]) == 7
    assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "racecar", "level", "radar", "stas", "stats", "tenet"]) == 8
    assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "racecar", "level", "radar", "stas", "stats", "tenet", "tenet"]) == 9
    assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "racecar", "level", "radar", "stas", "stats", "tenet", "tenet", "tenet"]) == 10
    assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "racecar", "level", "radar", "stas", "stats", "tenet", "tenet", "tenet", "tenet"]) == 11
    assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "racecar", "level", "radar", "stas", "stats", "tenet", "tenet", "tenet", "tenet", "tenet"]) == 12
    assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "racecar", "level", "radar", "stas", "stats", "tenet", "tenet", "tenet", "tenet", "tenet", "tenet"]) == 13
    assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "racecar", "level", "radar", "stas", "stats", "tenet", "tenet", "tenet", "tenet", "tenet", "tenet", "tenet"]) == 14
    assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "racecar", "level", "radar", "stas", "stats", "tenet", "tenet", "tenet", "tenet", "tenet", "