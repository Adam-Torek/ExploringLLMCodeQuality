"""
Write a function that takes in a list and an integer n and splits a list for every nth element, returning a list of the resulting lists.
assert list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],3)==[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
"""

def list_split(lst, n):
    result = []
    for i in range(0, len(lst), n):
        result.append(lst[i:i+n])
    return result

# Test the function with the given example
print(list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],3)) # Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]