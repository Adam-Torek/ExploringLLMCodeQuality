"""
Write a function to find the median of two sorted lists of same size.
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
"""

def get_median(list1, list2, size):
    if size % 2 == 0:
        return (list1[size//2] + list2[size//2]) / 2
    else:
        return list1[size//2]

# Test cases
print(get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5)) # 16.0
print(get_median([1, 2, 3, 4, 5], [6, 7, 8, 9], 4)) # 4.5
print(get_median([1, 2, 3, 4], [5, 6, 7, 8], 4) # 4.5
print(get_median([1, 2, 3], [4, 5, 6], 3) # 3.5
print(get_median([1, 2, 3], [4, 5, 6, 7, 8, 9], 4) # 4.5
print(get_median([1, 2, 3, 4], [5, 6, 7, 8, 9], 4) # 4.5
print(get_median([1, 2, 3, 4, 5], [6, 7, 8, 9], 4) # 4.5
print(get_median([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 4) # 4.5
print(get_median([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5) # 5.0
print(get_median([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 6) # 6.0
print(get_median([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 7) # 6.5
print(get_median([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 8) # 7.0
print(get_median([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 9) # 7.5
print(get_median([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 10) # 8.0
print(get_median([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 11) # 8.0
print(get_median([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 12) # 8.0
print(get_median([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 13) # 8.0
print(get_median([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 14) # 8.0
print(get_median([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 15) # 8.0
print(get_median([1, 2, 3, 4, 5], [6, 7, 8