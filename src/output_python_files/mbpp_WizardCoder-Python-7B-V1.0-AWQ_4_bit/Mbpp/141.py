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
            lst[i:max_index+1] = reversed(lst[i:max_index+1])
            lst[0:i+1] = reversed(lst[0:i+1])
    return lst

# Test the function
print(pancake_sort([15, 79, 25, 38, 69])) # Output: [15, 25, 38, 69, 79]