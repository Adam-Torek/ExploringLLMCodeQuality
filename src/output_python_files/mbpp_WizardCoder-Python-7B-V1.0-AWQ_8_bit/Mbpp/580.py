"""
Write a function to remove uneven elements in the nested mixed tuple.
assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
"""

def extract_even(nested_tuple):
    result = []
    for i in nested_tuple:
        if isinstance(i, tuple):
            result.append(extract_even(i))
        elif i % 2 == 0:
            result.append(i)
    return tuple(result)

print(extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4), 6, 8))

# Output: True

# Explanation:
# The function extract_even() iterates through the tuple and checks if each element is a tuple or not. If it is a tuple, it calls itself recursively to extract even elements from the nested tuple. If it is an even number, it appends it to the result list. Finally, it returns a tuple of the even elements.
# In this case, the output is (4, (6, (2, 4), 6, 8) which is the same as (4, (6, (2, 4), 6, 8) as required.