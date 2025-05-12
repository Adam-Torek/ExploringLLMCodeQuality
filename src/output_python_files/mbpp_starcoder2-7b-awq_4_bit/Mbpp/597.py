"""
Write a function to find kth element from the given two sorted arrays.
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
"""

def find_kth(a, b, k):
    if len(a) > len(b):
        return find_kth(b, a, k)
    if len(a) == 0:
        return b[k-1]
    if k == 1:
        return min(a[0], b[0])
    pa = min(k//2, len(a))
    pb = k - pa
    if a[pa-1] < b[pb-1]:
        return find_kth(a[pa:], b, pb)
    else:
        return find_kth(a, b[pb:], pa)

assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 1) == 1
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 2) == 2
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 3) == 3
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 4) == 4
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 6) == 7
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 7) == 8
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 8) == 9
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 9) == 10
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 10) == 10
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 11) == 10
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 12) == 10
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 13) == 10
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 14) == 10
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 15) == 10
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 16) == 10
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 17) == 10
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 18) == 10
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 19) == 10