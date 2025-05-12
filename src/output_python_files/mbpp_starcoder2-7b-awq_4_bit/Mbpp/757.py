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
assert count_reverse_pairs(["a", "b", "c", "d", "e"])== 0
assert count_reverse_pairs(["a", "b", "c", "d", "e", "f"])== 3
assert count_reverse_pairs(["a", "b", "c", "d", "e", "f", "g"])== 6
assert count_reverse_pairs(["a", "b", "c", "d", "e", "f", "g", "h"])== 10
assert count_reverse_pairs(["a", "b", "c", "d", "e", "f", "g", "h", "i"])== 15
assert count_reverse_pairs(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])== 21
assert count_reverse_pairs(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"])== 28
assert count_reverse_pairs(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"])== 36
assert count_reverse_pairs(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"])== 45
assert count_reverse_pairs(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"])== 55
assert count_reverse_pairs(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"])== 66
assert count_reverse_pairs(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"])== 78
assert count_reverse_pairs(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q"])== 91
assert count_reverse_pairs(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r"])== 105
assert count_reverse_pairs(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s"])== 120
assert count_reverse_pairs(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t"])== 136
assert count_reverse_pairs(["a", "b", "c