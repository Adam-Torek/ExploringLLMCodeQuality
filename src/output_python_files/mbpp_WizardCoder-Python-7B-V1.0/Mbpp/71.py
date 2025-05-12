"""
Write a function to sort a list of elements.
assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
"""

def comb_sort(lst):
    def swap(i, j):
        lst[i], lst[j] = lst[j], lst[i]

    n = len(lst)
    shrink = 1.3
    gap = n
    sorted = False
    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            sorted = True
        i = 0
        while i + gap < n:
            if lst[i] > lst[i + gap]:
                swap(i, i + gap)
                sorted = False
            i += 1
    return lst

# Test the function
print(comb_sort([5, 15, 37, 25, 79])) # Output: [5, 15, 25, 37, 79]