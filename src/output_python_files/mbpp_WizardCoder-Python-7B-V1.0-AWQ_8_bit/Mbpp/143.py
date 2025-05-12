"""
Write a function to find number of lists present in the given tuple.
assert find_lists(([1, 2, 3, 4], [5, 6, 7, 8])) == 2
"""

def find_lists(tup):
    count = 0
    for i in tup:
        if type(i) == list:
            count += 1
    return count

# Test cases
print(find_lists(([1, 2, 3, 4], [5, 6, 7, 8])) == 2) # True
print(find_lists(([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11])) == 3) # True
print(find_lists((1, 2, 3, 4, 5)) == 0) # True
print(find_lists(([1, 2, 3], 4, 5, [6, 7, 8], 9, [10, 11])) == 2) # True
print(find_lists(([1, 2, 3], 4, 5, [6, 7, 8], 9, [10, 11], [12, 13, 14])) == 3) # True
print(find_lists(([1, 2, 3], 4, 5, [6, 7, 8], 9, [10, 11], [12, 13, 14], [15, 16, 17, 18])) == 4) # True
print(find_lists(([1, 2, 3], 4, 5, [6, 7, 8], 9, [10, 11], [12, 13, 14], [15, 16, 17, 18], [19, 20, 21, 22, 23])) == 5) # True

# Edge cases
print(find_lists(()) == 0) # True
print(find_lists(([], [], [])) == 3) # True
print(find_lists(([], [1, 2, 3], [])) == 1) # True
print(find_lists(([], [1, 2, 3], [4, 5, 6], [])) == 2) # True
print(find_lists(([], [1, 2, 3], [4, 5, 6], [], [7, 8, 9], [])) == 3) # True
print(find_lists(([], [1, 2, 3], [4, 5, 6], [], [7, 8, 9], [], [10, 11, 12])) == 4) # True
print(find_lists(([], [1, 2, 3], [4, 5, 6], [], [7, 8, 9], [], [10, 11, 12], [])) == 5) # True

# Negative cases
print(find_lists(1) == 0) # False
print(find_lists("abc") == 0) # False
print(find_lists((1, 2, 3, "abc")) == 0) # False
print(find_lists((1, 2, 3, [4, 5, 6], "abc")) == 1) # False
print(find_lists((1, 2, 3, [4, 5, 6], [7, 8, 9])) == 2) # False
print(find_lists((1, 2, 3, [4, 5, 6], [7, 8, 9], [10, 11, 12], "abc")) == 3) # False
print(find_lists((1, 2, 3, [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], "abc")) == 4) # False
print(find_lists((1, 2, 3, [4, 5,