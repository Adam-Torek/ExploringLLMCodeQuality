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

def find_kth_2(a, b, k):
    if len(a) > len(b):
        return find_kth_2(b, a, k)
    if len(a) == 0:
        return b[k-1]
    if k == 1:
        return min(a[0], b[0])
    pa = min(k//2, len(a))
    pb = k - pa
    if a[pa-1] < b[pb-1]:
        return find_kth_2(a[pa:], b, pb)
    else:
        return find_kth_2(a, b[pb:], pa)

def find_kth_3(a, b, k):
    if len(a) > len(b):
        return find_kth_3(b, a, k)
    if len(a) == 0:
        return b[k-1]
    if k == 1:
        return min(a[0], b[0])
    pa = min(k//2, len(a))
    pb = k - pa
    if a[pa-1] < b[pb-1]:
        return find_kth_3(a[pa:], b, pb)
    else:
        return find_kth_3(a, b[pb:], pa)

def find_kth_4(a, b, k):
    if len(a) > len(b):
        return find_kth_4(b, a, k)
    if len(a) == 0:
        return b[k-1]
    if k == 1:
        return min(a[0], b[0])
    pa = min(k//2, len(a))
    pb = k - pa
    if a[pa-1] < b[pb-1]:
        return find_kth_4(a[pa:], b, pb)
    else:
        return find_kth_4(a, b[pb:], pa)

def find_kth_5(a, b, k):
    if len(a) > len(b):
        return find_kth_5(b, a, k)
    if len(a) == 0:
        return b[k-1]
    if k == 1:
        return min(a[0], b[0])
    pa = min(k//2, len(a))
    pb = k - pa
    if a[pa-1] < b[pb-1]:
        return find_kth_5(a[pa:], b, pb)
    else:
        return find_kth_5(a, b[pb:], pa)

def find_kth_6(a, b, k):
    if len(a) > len(b):
        return find_kth_6(b, a, k)
    if len(a) == 0:
        return b[k-1]
    if k == 1:
        return min(a[0], b[0])
    pa = min(k//2, len(a))
    pb = k - pa
    if a[pa-1] < b[pb-1]:
        return find_kth_6(a[pa:], b, pb)
    else:
        return find_kth_6(a, b[pb:], pa)

def find_kth_7(a, b, k):
    if len(a) > len(b):
        return find_kth_7(b, a, k)
    if len(a) == 0:
        return b[k-1]
    if k == 1:
        return min(a[