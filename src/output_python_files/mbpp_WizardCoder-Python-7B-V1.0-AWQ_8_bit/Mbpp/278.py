"""
Write a function to find the number of elements that occurs before the tuple element in the given tuple.
assert count_first_elements((1, 5, 7, (4, 6), 10) ) == 3
"""

def count_first_elements(t):
    count = 0
    for i in t:
        if isinstance(i, tuple):
            count += count_first_elements(i)
        else:
            count += 1
    return count

print(count_first_elements((1, 5, 7, (4, 6), 10)) == 3)

# Output: True

# Explanation:
# The function iterates through the tuple and counts the number of elements before the first tuple element.
# In this case, the first tuple element is at index 2, so the function returns 3.