"""
Write a function to count the pairs of reverse strings in the given string list. https://www.geeksforgeeks.org/python-program-to-count-the-pairs-of-reverse-strings/
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2
"""


def count_reverse_pairs(string_list):
    """
    :param string_list: list of strings
    :return: count of pairs of reverse strings
    """
    count = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if string_list[i][::-1] == string_list[j]:
                count += 1
    return count


if __name__ == '__main__':
    print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"]))
    print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia"]))
    print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia", "best"]))
    print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia", "best", "tseb"]))
    print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia", "best", "tseb", "for"]))
    print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia", "best", "tseb", "for", "ailuj"]))
    print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia", "best", "tseb", "for", "ailuj", "julia"]))
    print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia", "best", "tseb", "for", "ailuj", "julia", "best"]))
    print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia", "best", "tseb", "for", "ailuj", "julia", "best", "tseb"]))
    print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia", "best", "tseb", "for", "ailuj", "julia", "best", "tseb", "for"]))
    print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia", "best", "tseb", "for", "ailuj", "julia", "best", "tseb", "for", "ailuj"]))
    print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia", "best", "tseb", "for", "ailuj", "julia", "best", "tseb", "for", "ailuj", "julia"]))
    print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia", "best", "tseb", "for", "ailuj", "julia", "best", "tseb", "for", "ailuj", "julia", "best"]))
    print(count_reverse_pairs(["julia", "best", "tseb", "