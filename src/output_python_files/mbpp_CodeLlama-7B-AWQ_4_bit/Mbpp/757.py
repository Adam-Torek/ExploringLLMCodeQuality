"""
Write a function to count the pairs of reverse strings in the given string list. https://www.geeksforgeeks.org/python-program-to-count-the-pairs-of-reverse-strings/
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2
"""


def count_reverse_pairs(words):
    """
    :param words: list of strings
    :return: number of pairs of reverse strings
    """
    count = 0
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if words[i][::-1] == words[j]:
                count += 1
    return count


if __name__ == '__main__':
    print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"]))
    print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia"]))
    print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia", "julia"]))
    print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia", "julia", "julia"]))
    print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia", "julia", "julia", "julia"]))
    print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia", "julia", "julia", "julia", "julia"]))
    print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia", "julia", "julia", "julia", "julia", "julia"]))
    print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia", "julia", "julia", "julia", "julia", "julia", "julia"]))
    print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia", "julia", "julia", "julia", "julia", "julia", "julia", "julia"]))
    print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia", "julia", "julia", "julia", "julia", "julia", "julia", "julia", "julia"]))
    print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia", "julia", "julia", "julia", "julia", "julia", "julia", "julia", "julia", "julia"]))
    print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia", "julia", "julia", "julia", "julia", "julia", "julia", "julia", "julia", "julia", "julia"]))
    print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia", "julia", "julia", "julia", "julia", "