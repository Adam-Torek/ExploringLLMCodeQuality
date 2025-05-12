"""
Write a function to count the pairs of reverse strings in the given string list. https://www.geeksforgeeks.org/python-program-to-count-the-pairs-of-reverse-strings/
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2
"""

def count_reverse_pairs(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i][::-1] == lst[j]:
                count += 1
    return count

assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia"])== 3
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia", "best"])== 4
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia", "best", "tseb"])== 5
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia", "best", "tseb", "for"])== 6
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia", "best", "tseb", "for", "ailuj"])== 7
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia", "best", "tseb", "for", "ailuj", "julia"])== 8
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia", "best", "tseb", "for", "ailuj", "julia", "best"])== 9
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia", "best", "tseb", "for", "ailuj", "julia", "best", "tseb"])== 10
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia", "best", "tseb", "for", "ailuj", "julia", "best", "tseb", "for"])== 11
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia", "best", "tseb", "for", "ailuj", "julia", "best", "tseb", "for", "ailuj"])== 12
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia", "best", "tseb", "for", "ailuj", "julia", "best", "tseb", "for", "ailuj", "julia"])== 13
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia", "best", "tseb", "for", "ailuj", "julia", "best", "tseb", "for", "ailuj", "julia", "best"])== 14
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia", "best", "tseb", "for", "ailuj", "julia", "best", "tseb", "for", "ailuj", "julia", "best", "tseb"])== 15
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj", "julia", "best", "tseb", "for", "ailuj", "julia", "best", "tseb", "for", "ailuj", "julia", "best", "tseb", "for"])== 16
assert count_reverse_pairs(["julia", "best", "tseb", "for