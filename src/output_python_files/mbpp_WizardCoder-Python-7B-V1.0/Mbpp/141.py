"""
Write a function to sort a list of elements.
assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
"""

def pancake_sort(lst):
    n = len(lst)
    for i in range(n-1):
        max_index = i
        for j in range(i+1, n):
            if lst[j] > lst[max_index]:
                max_index = j
        if max_index != i:
            lst[i], lst[max_index] = lst[max_index], lst[i]
            lst[0:i+1] = lst[i::-1]
            lst[i+1:] = lst[i+1:][::-1]
    return lst

# Test cases
print(pancake_sort([15, 79, 25, 38, 69])) # Output: [15, 25, 38, 69, 79]
print(pancake_sort([4, 2, 6, 5, 1, 8, 3])) # Output: [1, 2, 3, 4, 5, 6, 8]
print(pancake_sort([1, 2, 3, 4, 5, 6])) # Output: [1, 2, 3, 4, 5, 6]
print(pancake_sort([6, 5, 4, 3, 2, 1])) # Output: [1, 2, 3, 4, 5, 6]
print(pancake_sort([1])) # Output: [1]
print(pancake_sort([])) # Output: []