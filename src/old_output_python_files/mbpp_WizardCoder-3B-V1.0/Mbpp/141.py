"""
Write a function to sort a list of elements.
assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
"""

def pancake_sort(lst):
    n = len(lst)
    for i in range(n):
        # Find the maximum element in the unsorted part of the list
        max_idx = i
        for j in range(i+1, n):
            if lst[j] > lst[max_idx]:
                max_idx = j
        # Swap the maximum element with the first element of the unsorted part
        lst[i], lst[max_idx] = lst[max_idx], lst[i]
    return lst

# Test the function
print(pancake_sort([15, 79, 25, 38, 69])) # Output: [15, 25, 38, 69, 79]<|endoftext|>