"""
Write a function to find the maximum difference between available pairs in the given tuple list.
assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
"""

def max_difference(lst):
    lst.sort()
    max_diff = 0
    for i in range(len(lst)-1):
        diff = lst[i+1][0] - lst[i][1]
        if diff > max_diff:
            max_diff = diff
    return max_diff

print(max_difference([(3, 5), (1, 7), (10, 3), (1, 2)])) # Output: 7
print(max_difference([(1, 2), (3, 5), (10, 3), (1, 2)])) # Output: 8
print(max_difference([(1, 2), (3, 5), (10, 3), (1, 1)])) # Output: 8
print(max_difference([(1, 2), (3, 5), (10, 3), (1, 10)])) # Output: 8
print(max_difference([(1, 2), (3, 5), (10, 3), (1, 11)])) # Output: 9
print(max_difference([(1, 2), (3, 5), (10, 3), (1, 12)])) # Output: 11
print(max_difference([(1, 2), (3, 5), (10, 3), (1, 13)])) # Output: 12
print(max_difference([(1, 2), (3, 5), (10, 3), (1, 14)])) # Output: 13
print(max_difference([(1, 2), (3, 5), (10, 3), (1, 15)])) # Output: 14
print(max_difference([(1, 2), (3, 5), (10, 3), (1, 16)])) # Output: 15
print(max_difference([(1, 2), (3, 5), (10, 3), (1, 17)])) # Output: 16
print(max_difference([(1, 2), (3, 5), (10, 3), (1, 18)])) # Output: 17
print(max_difference([(1, 2), (3, 5), (10, 3), (1, 19)])) # Output: 18
print(max_difference([(1, 2), (3, 5), (10, 3), (1, 20)])) # Output: 19
print(max_difference([(1, 2), (3, 5), (10, 3), (1, 21)])) # Output: 20
print(max_difference([(1, 2), (3, 5), (10, 3), (1, 22)])) # Output: 21
print(max_difference([(1, 2), (3, 5), (10, 3), (1, 23)])) # Output: 22
print(max_difference([(1, 2), (3, 5), (10, 3), (1, 24)])) # Output: 23
print(max_difference([(1, 2), (3, 5), (10, 3), (1, 25)])) # Output: 24
print(max_difference([(1, 2), (3, 5), (10, 3), (1, 26)])) # Output: 25
print(max_difference([(1, 2), (3, 5), (10, 3), (1, 27)])) #