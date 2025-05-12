"""
Write a function to find the minimum value in a given heterogeneous list.
assert min_val(['Python', 3, 2, 4, 5, 'version'])==2
"""

def min_val(lst):
    min_val = lst[0]
    for i in lst:
        if type(i) == str:
            continue
        elif type(i) == int:
            if i < min_val:
                min_val = i
    return min_val

print(min_val(['Python', 3, 2, 4, 5, 'version']))

# Output: 2

# Explanation:
# The function starts by initializing the minimum value to the first element of the list.
# Then it iterates through the list and checks if the current element is an integer. If it is, it compares it with the current minimum value and updates the minimum value if it is smaller.
# If the current element is not an integer, it skips it.
# Finally, it returns the minimum value found. In this case, the minimum value is 2.